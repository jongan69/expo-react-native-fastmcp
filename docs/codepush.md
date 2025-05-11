Migrate from CodePush - Expo Documentation

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

Deployment

Concepts

Troubleshooting

Reference

[Code signing](/eas-update/code-signing)[Asset selection and exclusion](/eas-update/asset-selection)[Using without other EAS services](/eas-update/standalone-service)[Migrate from CodePush](/eas-update/codepush)[Migrate from Classic Updates](/eas-update/migrate-from-classic-updates)[Trace update ID back to the Expo Dashboard](/eas-update/trace-update-id-expo-dashboard)[Estimate bandwidth usage](/eas-update/estimate-bandwidth)[Integrate in existing native apps](/eas-update/integration-in-existing-native-apps)[FAQ](/eas-update/faq)

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

Migrate from CodePush
=====================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/codepush.mdx)

A guide to help migrate from CodePush to EAS Update.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/codepush.mdx)

---

This guide explains how to transition a React Native project that uses CodePush to use EAS Update which offers [many advantages](/eas-update/introduction#pitch). It assumes that you're using the default React Native project structure. For assistance with migrating brownfield native apps to EAS Update, see [Using EAS Update in an existing native app](/eas-update/integration-in-existing-native-apps).

To learn more about the differences between CodePush and EAS Update, see [Conceptual differences between CodePush and EAS Update](/eas-update/codepush#conceptual-differences-between-codepush-and-eas-update) and the [What to do without CodePush post on the Expo Blog](https://expo.dev/blog/what-to-do-without-codepush).

1

Ensure your app is using the latest Expo SDK version
----------------------------------------------------

To migrate from CodePush to EAS Update, we recommend that you use the latest Expo SDK version. Instructions are not available for older Expo SDK and React Native version. While you may be able to migrate successfully by adapting the instructions as needed for the older Expo SDK and React Native version that your app uses, additional hands-on support for integrating with older versions can only be provided for enterprise customers ([contact us](https://expo.dev/contact)).

2

Uninstall CodePush
------------------

To avoid conflicts and unexpected behavior, it's recommended to uninstall CodePush if you're using EAS Update. This is because your app could periodically fetch updates from both services, leading to issues, especially if you're using different configurations for each service.

Remove the CodePush SDK from your project by uninstalling the `react-native-code-push` package:

Terminal

Copy

`-Â``npm uninstall react-native-code-push`

You'll also need to remove CodePush references from JS and native code. See this [GitHub comment](https://github.com/Microsoft/react-native-code-push/issues/1101#issuecomment-350204507) for more detailed instructions.

3

Add an `expo` key to your `app.json`
------------------------------------

Ensure that your project has an app.json file with an `expo` object. If you don't have anything specific to configure in your app.json file yet, you can create a minimal file with an empty `expo` object like this:

app.json

Copy

```
{
  "expo": {
    //... any other existing keys you have
  }
}

```

4

Follow the "Getting Started" guide
----------------------------------

The instructions in the [EAS Update Getting Started guide](/eas-update/getting-started) will guide you through setting up EAS Update in your project.

5

Resubmit your app
-----------------

Since you have changed the update provider from CodePush to EAS Update, you will need to rebuild your app and submit the new build to the respective app stores (Google Play Store and Apple App Store) to ensure the update mechanism works as expected for your end-users.

Follow the respective store guidelines for submitting a new build of your application:

* [Submitting to Google Play Store](/submit/android)
* [Submitting to Apple App Store](/submit/ios)

After successfully submitting your app, users will be able to download and use the latest build with EAS Update integration. If your app is not updating as expected, [validate your configuration](/eas-update/debug).

Common questions
----------------

How do I release mandatory/critical updates with EAS Update?

CodePush CLI has a `--mandatory` flag that allows you to release mandatory updates. You can build this functionality with EAS Update but there is no specific flag for it.

[Learn more about mandatory/critical updates](/eas-update/download-updates#criticalmandatory-updates).

How do I include a message in an update?

CodePush CLI has a `--description` flag that allows you to include a message in an update. You can build this functionality with EAS Update using the `extra` field in your app config.

Refer the `--message` flag in this example: [`expo/UpdatesAPIDemo`](https://github.com/expo/UpdatesAPIDemo).

How do I switch the 'deployment' that is being used at runtime, similar to the sync() function in CodePush?

This is possible using `Updates.setUpdateURLAndRequestHeadersOverride()`. Learn more in the [Override update configuration at runtime](/eas-update/override) guide.

How do I handle different environments (such as staging and production) with EAS Update?

With EAS Update, you can use channels and branches to manage different environments and rollouts. [Learn more](/eas-update/eas-cli).

How do I roll back updates with EAS Update?

You can roll back updates using `eas update:rollback`. Learn more in the [Rollback to a previous update](/eas-update/rollbacks) guide.

How do I gradually roll out updates with EAS Update?

EAS Update supports various strategies for gradually rolling out updates, so you can pick which approach best fits your needs. [Learn more](/eas-update/rollouts).

How can I have direct control over when an update is downloaded and applied?

Learn more about different strategies for downloading and applying updates in the [Downloading updates](/eas-update/download-updates) guide, such as checking for updates while the app is running or even when backgrounded with `Updates.checkForUpdateAsync()`.

Does EAS Update support end-to-end code signing?

Yes, EAS Update supports end-to-end code signing. It is available for EAS Production and Enterprise plan subscribers. Learn more in the [Code signing](/eas-update/code-signing) guide.

What else should I know about?

* Expo Orbit: The macOS, Windows, and Linux desktop launcher app. You can [launch updates](/review/with-orbit) directly from the website with it in one click, among other features.
* You can monitor the adoption of updates from the EAS website. [Learn more](/eas-update/download-updates#monitoring-adoption-of-updates). You can also roll out and roll back updates from the website.
* You can use EAS Update to achieve a web-like preview workflow. [Learn more](/eas-update/preview).
* Each update and build created with EAS is associated with a [fingerprint](/versions/latest/sdk/fingerprint). You can diff these fingerprints through the website UI or with `eas fingerprint:compare` to see what changed in the native runtime of your app between your builds and updates, to understand build/update compatibility, and guide your decision about when to bump the [`runtimeVersion`](/eas-update/runtime-versions).

Conceptual differences between CodePush and EAS Update
------------------------------------------------------

CodePush and EAS Update are both services that allow you to send hotfixes to the JavaScript code of your app, but they take slightly different approaches, and so you may need to adapt your release process when moving to EAS Update.

Differences in how updates are organized within streams

CodePush has single streams of updates for deployments. What this means is that you can point a build to a deployment, and it will pull updates from that. If you want to change the deployment that is targeted by a build, you can do this at runtime through a JavaScript API.

EAS Update has multiple streams of updates â one that correspond to your source control branches (called branches), and another called channels, which point to branches. The mapping between channels and branches is handled on the server side, and a channel can point to different branches for each runtime version (additionally, more advanced logic may be expressed, such as to support incremental rollouts). Builds are not directly associated with branches, but rather with channels. Each build points to a single channel, which is set at build time and cannot be modified at runtime. The reason for this is that it ensures that certain branches (for example: development, staging) don't automatically go out to production â your preview updates don't go to your production users. This helps you separate the two main uses of EAS Update: previews and production hotfixes.

Differences in how updates are selected at runtime

A key distinction between CodePush and EAS Update that can impact your release process is that with CodePush, the client controls the target update deployment at runtime, and with EAS Update, it is controlled on the server side, by mapping channels to branches. This means that you can't include code in your app using EAS Update to instruct it to load a different stream of updates depending on runtime criteria, such as the current user role (for example: distribute beta releases to employees) - it will only load the branch that is mapped on EAS Update servers to the corresponding channel (such as production or staging).

The ability to control the target deployment at runtime is commonly used with CodePush in staging environments to allow non-technical stakeholders to test features from a single build on Google Play Beta / TestFlight. The current alternative for this with EAS Update is to use [development builds](/eas-update/expo-dev-client). We're currently working on providing a way to do this with release builds.

[Previous (EAS Update - Reference)

Using without other EAS services](/eas-update/standalone-service)[Next (EAS Update - Reference)

Migrate from Classic Updates](/eas-update/migrate-from-classic-updates)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/codepush.mdx)
* Last updated on March 12, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Ensure your app is using the latest Expo SDK version](/eas-update/codepush/#ensure-your-app-is-using-the-latest-expo-sdk-version)[Uninstall CodePush](/eas-update/codepush/#uninstall-codepush)[Add an expo key to your app.json](/eas-update/codepush/#add-an-expo-key-to-your-appjson)[Follow the "Getting Started" guide](/eas-update/codepush/#follow-the-getting-started-guide)[Resubmit your app](/eas-update/codepush/#resubmit-your-app)[Common questions](/eas-update/codepush/#common-questions)[Conceptual differences between CodePush and EAS Update](/eas-update/codepush/#conceptual-differences-between-codepush-and-eas-update)