Expo Orbit - Expo Documentation

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

Expo Orbit
==========

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build/orbit.mdx)

Accelerate your development workflow with one-click build and update launches and simulator management.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build/orbit.mdx)

---

[Expo Orbit](https://expo.dev/orbit) for macOS and Windows enables faster to install and launch builds or updates from EAS, local files, or run Snack projects, on simulators and physical devices.

Why Orbit
---------

Before Orbit, installing builds or updates from EAS (on Android and iOS physical devices or emulator/simulator) or running Snack projects on simulators was manual. You had to run `eas build:run` command and select a build for your chosen device or download the archive and then drag and drop it to the simulator (in the case of iOS). Also, for Snack projects, additional steps included installing Expo Go on the virtual device, logging in, and then selecting the Snack from the list. Orbit makes all of these steps as seamless as possible.

Highlights
----------

* List and launch simulators, including running Android emulators without audio.
* Install and launch builds from EAS on simulators and real devices in one click.
* [Install and open updates from EAS](/review/with-orbit) on Android Emulators or iOS Simulators.
* Launch Snack projects in your simulators in one click.
* Install and launch apps from local files using Finder or drag and drop a file into the menu bar app. Orbit supports any Android .apk, iOS Simulator compatible .app, or ad hoc signed apps.
* See pinned projects from your [EAS dashboard](https://expo.dev) and quickly launch your latest builds.

Installation
------------

> Orbit relies on the Android SDK on both macOS and Windows and `xcrun` for device management only on macOS, which requires setting up both [Android Studio](/workflow/android-studio-emulator) and [Xcode](/workflow/ios-simulator).

macOS

Windows

You can download Orbit with Homebrew for macOS, or directly from the [GitHub releases](https://github.com/expo/orbit/releases).

Terminal

Copy

`-Â``brew install expo-orbit`

If you want Orbit to start when you log in automatically, click on the Orbit icon in the menu bar, then Settings and select the Launch on Login option.

> Note: Orbit for Windows is in preview and is only compatible with x64 and x86 machines. Compatibility for other architectures will be added in the future.

You can download Orbit for Windows directly from the [GitHub releases](https://github.com/expo/orbit/releases).

[Previous (EAS Build)

Trigger builds from GitHub App](/build/building-from-github)[Next (EAS Build - App signing)

App credentials](/app-signing/app-credentials)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build/orbit.mdx)
* Last updated on July 01, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Why Orbit](/build/orbit/#why-orbit)[Highlights](/build/orbit/#highlights)[Installation](/build/orbit/#installation)