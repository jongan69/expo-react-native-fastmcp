Override update configuration at runtime - Expo Documentation

[Docs](/)

[Blog](https://expo.dev/blog)[Changelog](https://expo.dev/changelog)[Star Us on GitHub](https://github.com/expo/expo)

Search

[Home](/)[Guides](/guides/overview)[EAS](/eas)[Reference](/versions/latest)[Learn](/tutorial/overview)

[Introduction](/eas)[Configuration with eas.json](/eas/json)[Environment variables](/eas/environment-variables)

EAS Workflows

[Get started](/eas/workflows/get-started)[Example CI/CD workflows](/eas/workflows/examples)[Syntax for EAS Workflows](/eas/workflows/syntax)[Automating EAS CLI commands](/eas/workflows/automating-eas-cli)

Reference

EAS Build

[Introduction](/build/introduction)[Create your first build](/build/setup)[Configure with eas.json](/build/eas-json)[Internal distribution](/build/internal-distribution)[Automate submissions](/build/automate-submissions)[Using EAS Update](/build/updates)[Trigger builds from CI](/build/building-on-ci)[Trigger builds from GitHub App](/build/building-from-github)[Expo Orbit](/build/orbit)

App signing

Custom builds

Reference

EAS Hosting

[Introduction](/eas/hosting/introduction)[Get started](/eas/hosting/get-started)[Deployments and aliases](/eas/hosting/deployments-and-aliases)[Environment variables](/eas/hosting/environment-variables)[Custom domain](/eas/hosting/custom-domain)[Monitoring API routes](/eas/hosting/api-routes)[Workflows](/eas/hosting/workflows)

Reference

EAS Submit

[Introduction](/submit/introduction)[Submit to the Google Play Store](/submit/android)[Submit to the Apple App Store](/submit/ios)[Configure with eas.json](/submit/eas-json)

EAS Update

[Introduction](/eas-update/introduction)[Get started](/eas-update/getting-started)

Preview

[Preview updates](/eas-update/preview)[Override update configuration at runtime](/eas-update/override)[Using development builds](/eas-update/expo-dev-client)[Github PR previews](/eas-update/github-actions)

Deployment

Concepts

Troubleshooting

Reference

EAS Metadata

[Introduction](/eas/metadata)[Get started](/eas/metadata/getting-started)

Reference

EAS Insights

[Introduction](/eas-insights/introduction)

Distribution

[Overview](/distribution/introduction)[App stores best practices](/distribution/app-stores)[App transfers](/distribution/app-transfers)[Understanding app size](/distribution/app-size)

Reference

[Webhooks](/eas/webhooks)

Expo accounts

Billing

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Override update configuration at runtime
========================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/override.mdx)

Learn how to override the update URL and request headers at runtime to control which update is loaded on the client side.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/override.mdx)

---

> The features described in this guide are available in Expo SDK 52 with the `expo-updates` version 0.27.0 and later. Using the `disableAntiBrickingMeasures` option is not recommended for production apps, it is currently primarily intended for preview environments.

The typical way to use EAS Update is to have a single update URL and a set of request headers (such as update channel name) embedded in a build of your app. To control which update is loaded you make changes on the server through the `eas update` command or the EAS dashboard. For example, you publish a new update to a channel that your build is pointing to, then the build fetches that update on the next launch. Updates published to a channel different from the one your build is pointing to will not be downloaded with this approach.

This guide explains how you can change the update URL and request headers at runtime, making it possible to load a specific update by ID or change the channel that updates are pulled from without creating and installing a new build.

Use cases for changing the update URL and request headers at runtime
--------------------------------------------------------------------

The primary use case that this is intended for is to enable switching between updates in a preview build, similar to what is possible in a development build. This is useful to enable non-technical stakeholders to test and validate updates of work-in-progress (such as from a pull request or different feature branches) without having to use a development build or create a separate preview build for each change.

Another potential use case is to provide different updates to different users, for example so that a group of internal users (such as employees) receive updates before end-users. It is important to be familiar with the [security considerations](/eas-update/override#security-considerations) before deciding to use this feature in production. In the future, we may add support for a more restricted version of the feature that would be more suitable for this use case.

How it works
------------

There are two relevant APIs:

1. `Updates.setUpdateURLAndRequestHeadersOverride({ url: string, requestHeaders: Object })` - this method overrides the update URL and the request headers that are specified in app.json / Expo.plist / AndroidManifest.xml, such as the `expo-channel-name` header.
2. `disableAntiBrickingMeasures` - this field in the app config disables anti-bricking measures built-in to `expo-updates` which ensure subsequent updates can always be published to fix issues in previously-installed update. When you change this value, you will need to create a new build for it to take effect. Do not enable this in your production builds. The reason for this name is to clearly indicate that when you override the update URL/headers, we're no longer able to safely rollback to the previous update that was loaded. So, if the new update you have loaded causes the app to crash then `expo-updates`cannot automatically recover, because this field in conjunction with `setUpdateURLAndRequestHeadersOverride` will disable embedded updates and therefore there will not be any update to rollback to. The user would need to uninstall and reinstall the app. You should only use this feature in preview builds.

How to use these APIs:

1. Override the update URL/headers, instruct user to close the app: Somewhere in your app, you would provide a way for users to trigger the change to the URL and/or request headers. This may be in a hidden menu that only trusted users have access to, or some other mechanism depending on your use case. When the parameters are changed, notify the user that they need to close and re-open the app, such as via an alert. The `expo-updates` library, with methods like `checkForUpdateAsync()`, will not use the new overridden URL and request headers until the app is closed and reopened.
2. The new update will be downloaded and launched on the next app open: After the app is completely closed ("killed" and not just backgrounded) and re-opened, the update and its related assets will all be downloaded. Once they are ready, the app will launch. While it's downloading, the user will have to wait on the splash screen. We understand that waiting on the splash screen is not ideal, and we intend to improve this experience in the future if this feature is widely used. For the currently recommended use case (previews), this is likely an acceptable compromise.

Security considerations
-----------------------

The anti-bricking measures that can be disabled with `disableAntiBrickingMeasures` ensure that, no matter what update is published, you can always publish another update afterwards that will be applied. By disabling the anti-bricking measures, certain categories of attacks and exploits become possible, especially around in-house (malicious employee) publishing of malicious updates. For example, an employee with the ability to publish updates could publish a malicious update that changes the update URL and request headers to point to their own server, and take over installations of the app. This risk can be mitigated, but not eliminated, by using [code signing](/eas-update/code-signing) for production updates and limiting access to the key.

Did similar usage of CodePush carry the same risk?

Yes. CodePush allowed developers to swap deployment keys with `sync({ deploymentKey: string })` which could be used maliciously take over an app installation in this same way.

Example code
------------

Here's an example of how you might use these APIs:

```
import * as Updates from 'expo-updates';

// Where you call this method depends on your use case - it may make sense to
// have a menu in your preview builds that allows testers to pick from available
// pull requests, for example.
function overrideUpdateURLAndHeaders() {
  Updates.setUpdateURLAndRequestHeadersOverride({
    url: '<https://u.expo.dev/>...',
    requestHeaders: { 'expo-channel-name': 'pr-123' },
  });

  alert('Close and re-open the app to load the latest version.');
}

```

```
{
  "expo": {
    "updates": {
      // We recommend only enabling this in preview builds.
      // You can use app.config.js to configure it dynamically.
      "disableAntiBrickingMeasures": true
      // etc..
    }
  }
}

```

[Previous (EAS Update - Preview)

Preview updates](/eas-update/preview)[Next (EAS Update - Preview)

Using development builds](/eas-update/expo-dev-client)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/override.mdx)
* Last updated on February 21, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Use cases for changing the update URL and request headers at runtime](/eas-update/override/#use-cases-for-changing-the-update-url-and-request-headers-at-runtime)[How it works](/eas-update/override/#how-it-works)[Security considerations](/eas-update/override/#security-considerations)[Example code](/eas-update/override/#example-code)