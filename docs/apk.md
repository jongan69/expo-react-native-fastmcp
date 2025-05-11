Build APKs for Android Emulators and devices - Expo Documentation

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

[Build lifecycle hooks](/build-reference/npm-hooks)[Using private npm packages](/build-reference/private-npm-packages)[Git submodules](/build-reference/git-submodules)[Using npm cache with Yarn 1 (Classic)](/build-reference/npm-cache-with-yarn)[Set up EAS Build with a monorepo](/build-reference/build-with-monorepos)[Build APKs for Android Emulators and devices](/build-reference/apk)[Build for iOS Simulators](/build-reference/simulators)[App version management](/build-reference/app-versions)[Troubleshoot build errors and crashes](/build-reference/troubleshooting)[Install app variants on the same device](/build-reference/variants)[iOS capabilities](/build-reference/ios-capabilities)[Run EAS Build locally](/build-reference/local-builds)[Cache dependencies](/build-reference/caching)[Android build process](/build-reference/android-builds)[iOS build process](/build-reference/ios-builds)[Configuration process](/build-reference/build-configuration)[Server infrastructure](/build-reference/infrastructure)[iOS App Extensions](/build-reference/app-extensions)[Ignore files via .easignore](/build-reference/easignore)[Limitations](/build-reference/limitations)

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

Build APKs for Android Emulators and devices
============================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/apk.mdx)

Learn how to configure and install a .apk for Android Emulators and devices when using EAS Build.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/apk.mdx)

---

The default file format used when building Android apps with EAS Build is an [Android App Bundle](https://developer.android.com/platform/technology/app-bundle) (AAB/.aab). This format is optimized for distribution to the Google Play Store. However, AABs can't be installed directly on your device. To install a build directly to your Android device or emulator, you need to build an [Android Package](https://en.wikipedia.org/wiki/Android_application_package) (APK/.apk) instead.

Configuring a profile to build APKs
-----------------------------------

To generate an .apk, modify the [eas.json](/build/eas-json) by adding one of the following properties in a build profile:

* `developmentClient` to `true` (default)
* `distribution` to `internal`
* `android.buildType` to `apk`
* `android.gradleCommand` to `:app:assembleRelease`, `:app:assembleDebug` or any other gradle command that produces .apk

eas.json

Copy

```
{
  "build": {
    "preview": {
      "android": {
        "buildType": "apk"
      }
    },
    "preview2": {
      "android": {
        "gradleCommand": ":app:assembleRelease"
      }
    },
    "preview3": {
      "developmentClient": true
    },
    "preview4": {
      "distribution": "internal"
    },
    "production": {}
  }
}

```

Now you can run your build with the following command:

Terminal

Copy

`-Â``eas build -p android --profile preview`

Remember that you can name the profile whatever you like. We named the profile `preview`. However, you can call it `local`, `emulator`, or whatever makes the most sense for you.

Installing your build
---------------------

### Emulator (virtual device)

> If you haven't installed or run an Android Emulator before, follow the [Android Studio emulator guide](/workflow/android-studio-emulator) before proceeding.

Once your build is completed, the CLI will prompt you to automatically download and install it on the Android Emulator. When prompted, press `Y` to directly install it on the emulator.

In case you have multiple builds, you can also run the `eas build:run` command at any time to download a specific build and automatically install it on the Android Emulator:

Terminal

Copy

`-Â``eas build:run -p android`

The command also shows a list of available builds of your project. You can select the build to install on the emulator from this list. Each build in the list has a build ID, the time elapsed since the build creation, the build number, the version number, and the git commit information. The list also displays invalid builds if a project has any.

For example, the image below lists the build of a project:

![Running eas build:run command shows a list of available builds in a project.](/static/images/eas-build/eas-build-run-on-android.png)

When the build's installation is complete, it will appear on the home screen. If it's a development build, open a terminal window and start the development server by running the command `npx expo start`.

#### Running the latest build

Pass the `--latest` flag to the `eas build:run` command to download and install the latest build on the Android Emulator:

Terminal

Copy

`-Â``eas build:run -p android --latest`

### Physical device

#### Download directly to the device

* Once your build is completed, copy the URL to the APK from the build details page or the link provided when `eas build` is done.
* Send that URL to your device. Maybe by email? Up to you.
* Open the URL on your device, install the APK and run it.

#### Install with `adb`

* [Install adb](https://developer.android.com/studio/command-line/adb) if you don't have it installed already.
* Connect your device to your computer and [enable adb debugging on your device](https://developer.android.com/studio/command-line/adb#Enabling) if you haven't already.
* Once your build is completed, download the APK from the build details page or the link provided when `eas build` is done.
* Run `adb install path/to/the/file.apk`.
* Run the app on your device.

[Previous (EAS Build - Reference)

Set up EAS Build with a monorepo](/build-reference/build-with-monorepos)[Next (EAS Build - Reference)

Build for iOS Simulators](/build-reference/simulators)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/apk.mdx)
* Last updated on August 01, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Configuring a profile to build APKs](/build-reference/apk/#configuring-a-profile-to-build-apks)[Installing your build](/build-reference/apk/#installing-your-build)[Emulator (virtual device)](/build-reference/apk/#emulator-virtual-device)[Physical device](/build-reference/apk/#physical-device)