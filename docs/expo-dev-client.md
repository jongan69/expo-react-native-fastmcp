Preview updates in development builds - Expo Documentation

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

Preview updates in development builds
=====================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/expo-dev-client.mdx)

Learn how to use the expo-dev-client library to preview a published EAS Update inside a development build.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/expo-dev-client.mdx)

---

[`expo-dev-client`](/develop/development-builds/introduction) library allows launching different versions of a project by creating a development build. Any compatible EAS Update can be previewed in a development build.

This guide walks through the steps required to load and preview a published update inside a development build using the Extensions tab or constructing a specific Update URL.

Prerequisites
-------------

* [Create a development build and install it](/develop/development-builds/create-a-build) on your device or Android Emulator or iOS Simulator.
* Make sure your development build has the [`expo-updates` library installed](/eas-update/getting-started#configure-your-project).

What is an Extensions tab
-------------------------

![Extensions tab in a development build.](/static/images/eas-update/extensions-01.png)

When using the `expo-updates` library inside a development build, the Extensions tab provides the ability to load and preview a published update automatically.

### Preview an update using the Extensions tab

1

Make non-native changes locally in your project and then [publish them using `eas update`](/eas-update/getting-started#publish-an-update). The update will be published on a branch.

2

After publishing the update, open your development build, go to Extensions, and tap Login to log in to your Expo account within the development build. This step is required for the Extensions tab to load any published updates associated with the project under your Expo account.

3

After logging in, an EAS Update section will appear inside the Extensions tab with one or more of the latest published updates. Tap Open next to the update you want to preview.

In the Extensions tab, you can view the list of all published updates for a branch. Tap the branch name in the Extensions tab.

![Extensions tab in a development build.](/static/images/eas-update/extensions-02.png)

Preview an update using the Expo dashboard
------------------------------------------

You can also preview an update using the Expo dashboard by following the steps below:

* Click the published updated link in the CLI after running the command to publish an update. This will open the update's details on the Updates page in the Expo dashboard.
* Click Preview. This will open the Preview dialog.
* To preview the update, you can either scan the QR code with your device's camera or select a platform to [launch the update under Open with Orbit](/review/with-orbit).

Construct an update URL
-----------------------

As an alternative to the methods described in the previous sections, you can construct a specific URL to open your EAS Update in the development build. The URL will look like the following:

```
[slug]://expo-development-client/?url=[https://u.expo.dev/project-id]/group/[group-id]

# Example
my-app://expo-development-client/?url=https://u.expo.dev/675cb1f0-fa3c-11e8-ac99-6374d9643cb2/group/47839bf2-9e01-467b-9378-4a978604ab11

```

Let's break this URL to understand what each part does:

| Part of URL | Description |
| --- | --- |
| `slug` | The project's [slug](/versions/latest/config/app#slug) found in the app config. |
| `://expo-development-client/` | Necessary for the deep link to work with the [`expo-dev-client`](/versions/latest/sdk/dev-client) library. |
| `?url=` | Defines a `url` query parameter. |
| `https://u.expo.dev/675cb1f0-fa3c-11e8-ac99-6374d9643cb2` | This is the updates URL, which is inside the project's app config under [`updates.url`](/versions/latest/config/app#url). |
| `/group/47839bf2-9e01-467b-9378-4a978604ab11` | The group ID of the update. |

Once you've constructed the URL, copy and paste it directly into the development build's launcher screen under Enter URL Manually.

Alternatively, you can [create a QR code for the URL](/more/qr-codes) and scan it using your device's camera. When scanned, the URL will open up the development build to the specified channel.

Example
-------

[See a working example

See a working example of using `expo-dev-client` with EAS Update.](https://github.com/jonsamp/test-expo-dev-client-eas-update)

[Previous (EAS Update - Preview)

Override update configuration at runtime](/eas-update/override)[Next (EAS Update - Preview)

Github PR previews](/eas-update/github-actions)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/expo-dev-client.mdx)
* Last updated on March 03, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Prerequisites](/eas-update/expo-dev-client/#prerequisites)[What is an Extensions tab](/eas-update/expo-dev-client/#what-is-an-extensions-tab)[Preview an update using the Extensions tab](/eas-update/expo-dev-client/#preview-an-update-using-the-extensions-tab)[Preview an update using the Expo dashboard](/eas-update/expo-dev-client/#preview-an-update-using-the-expo-dashboard)[Construct an update URL](/eas-update/expo-dev-client/#construct-an-update-url)[Example](/eas-update/expo-dev-client/#example)