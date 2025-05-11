App version management - Expo Documentation

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

App version management
======================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/app-versions.mdx)

Learn about different version types and how to manage them remotely or locally.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/app-versions.mdx)

---

Android and iOS each expose two values to identify the version of an app: the version visible in stores (user-facing version) and the version visible only to developers (developer-facing build version). This guide explains how you can manage those versions remotely or locally.

[![Automatic App Version Management](https://i3.ytimg.com/vi/Gk7RHDWsLsQ/maxresdefault.jpg)

Automatic App Version Management

In this Expo feature focus video you'll learn about automatic app version management in Expo EAS Build.](https://www.youtube.com/watch?v=Gk7RHDWsLsQ)

App versions
------------

In Expo projects, the following properties can be used to define app versions in the [app config](/workflow/configuration) file.

| Property | Description |
| --- | --- |
| [`version`](/versions/latest/config/app#version) | The user-facing version visible in stores. On Android, it represents `versionName` name in android/app/build.gradle. On iOS, it represents `CFBundleShortVersionString` in Info.plist. |
| [`android.versionCode`](/versions/latest/config/app#versioncode) | The developer-facing build version for Android. It represents `versionCode` in android/app/build.gradle. |
| [`ios.buildNumber`](/versions/latest/config/app#buildnumber) | The developer-facing build version for iOS. It represents `CFBundleVersion` in Info.plist. |

### Using app versions in your app

To show the user-facing version inside your app, you can use [`Application.nativeApplicationVersion`](/versions/latest/sdk/application#applicationnativeapplicationversion) from the `expo-application` library.

To show the developer-facing build version inside your app, you can use [`Application.nativeBuildVersion`](/versions/latest/sdk/application#applicationnativebuildversion) from the `expo-application` library.

Recommended workflow
--------------------

### User-facing version

When you are doing a production release, the user-facing version should be explicitly set and updated by you. You can update the `version` property in app config when production build is submitted to the app stores. This also applies if your project uses `expo-updates` with an automatic runtime version policy. This marks the beginning of a new development cycle for a new version of your app. Learn more about [deployment patterns](/eas-update/deployment-patterns).

### Developer-facing build version

For developer-facing build version, you can set them to autoincrement on every build. This will help you avoid making manual changes to the project every time you upload a new archive on Play Store testing channels or TestFlight. One common cause for app store rejections is submitting a build with a duplicate version number. It happens when a developer forgets to increment the developer-facing build version number before creating a new build.

EAS Build can help manage developer-facing build versions automatically by incrementing these versions for you if you opt into using the [`remote` version source](/build-reference/app-versions#remote-version-source), which is the recommended behaviour. Optionally, you can choose to use a `local` app version source, which means you control versions manually in their respective config files.

Remote version source
---------------------

> The `remote` version source is the recommended behavior from EAS CLI version `12.0.0`. If you are using an older version of the EAS CLI, `local` is the default.

EAS servers can store and manage your app's developer-facing build version (`android.versionCode` and `ios.buildNumber`) remotely. To enable it, you need to set `cli.appVersionSource` to `remote` in eas.json. Then, under the `production` build profile, you can set the `autoIncrement` property to `true`.

eas.json

Copy

```
{
  "cli": {
    "appVersionSource": "remote"
  },
  "build": {
    "development": {
      %%placeholder-start%%... %%placeholder-end%%
    },
    "preview": {
      %%placeholder-start%%... %%placeholder-end%%
    },
    "production": {
      "autoIncrement": true
    }
  }
  %%placeholder-start%%... %%placeholder-end%%
}

```

The remote version is initialized with the value from the local project. For example, if you have `android.versionCode` set to `1` in app config, when you create a new build using the remote version source, it will auto increment to `2`. However, if you do not have build versions set in your app config, the remote version will initialize with `1` when the first build is created.

When the `remote` version property is enabled inside eas.json, the build version values stored in app config are ignored and not updated when the version is incremented remotely. The remote version source values are set on the native project when running a build, which is considered the source of truth for these values. You can safely remove these values from your app config.

### Syncing already defined versions to remote

There are different scenarios where you already have versions set up for your project and want to increment from those versions when you create a new EAS Build. However, these existing versions might not be synced remotely with EAS. Some of these scenarios are:

* You have already published your app in the app stores and want to continue using the same version numbers.
* EAS CLI is not able to detect what version the app is on.
* For any other reason, you have versions explicitly set, such as inside your app config.

In these scenarios, you can sync the current version to EAS Build using the EAS CLI using the following steps:

* In the terminal window, run the following command:

  Terminal

  Copy

  `-Â``eas build:version:set`
* Select the platform (Android or iOS) when prompted.
* When prompted Do you want to set app version source to remote now?, select yes. This will set the `cli.appVersionSource` to `remote` in eas.json.
* When prompted What version would you like to initialize it with?, enter the last version number that you have set in the app stores.

After these steps, the app versions will be synced to EAS Build remotely. You can now set `build.production.autoIncrement` to `true` in eas.json. When you create a new production build, the `versionCode` and `buildNumber` will be automatically incremented.

### Syncing versions from remote to local

To build your project locally in Android Studio or Xcode using the same version stored remotely on EAS, update your local project with the remote versions using the following command:

Terminal

Copy

`-Â``eas build:version:sync`

### Limitations

* `eas build:version:sync` command on Android does not support bare projects with multiple flavors. However, the rest of the remote versioning functionality should work with all projects.
* `autoIncrement` does not support the `version` option.
* It's not supported if you are using EAS Update and runtime policy set to `"runtimeVersion": { "policy": "nativeVersion" }`. For similar behavior, use the `"appVersion"` policy instead.

Local version source
--------------------

> The `remote` version source as a recommended behavior has been introduced in `eas-cli` version `12.0.0`. If you are using an older version of the CLI, you don't need to specify the version source explicitly to `local`.

You can configure your project so that the source of truth for project versions is the local project source code itself. To do this, set `cli.appVersionSource` to `local` in your eas.json.

With this setup, EAS reads app version values and builds projects as they are. It doesn't write to the project. You can also enable auto incrementing versions locally by setting the `autoIncrement` option on a build profile.

eas.json

Copy

```
{
  "cli": {
    "appVersionSource": "local"
  },
  "build": {
    "development": {
      %%placeholder-start%%... %%placeholder-end%%
    },
    "preview": {
      %%placeholder-start%%... %%placeholder-end%%
    },
    "production": {
      "autoIncrement": true
    }
  }
  %%placeholder-start%%... %%placeholder-end%%
}

```

In the case of [existing React Native projects](/bare/overview), the values in native code take precedence. The libraries `expo-constants` and `expo-updates` read values from the app config file. If you rely on version values from a manifest, you should keep them in sync with native code. Keeping these values in sync is especially important if you are using EAS Update with the runtime policy set to `"runtimeVersion": { "policy": "nativeVersion" }`, because mismatched versions may result in the delivery of updates to the wrong version of an application. We recommend using [`expo-application`](/versions/latest/sdk/application#constants) to read the version instead of depending on values from app config.

### Limitations

* With `autoIncrement`, you need to commit your changes on every build if you want the version change to persist. This can be difficult to coordinate when building on CI.
* For existing React Native projects with Gradle configuration that supports multiple flavors, EAS CLI is not able to read or modify the version, so `autoIncrement` option is not supported, and versions will not be listed in the build details page on [expo.dev](https://expo.dev).

[Previous (EAS Build - Reference)

Build for iOS Simulators](/build-reference/simulators)[Next (EAS Build - Reference)

Troubleshoot build errors and crashes](/build-reference/troubleshooting)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/app-versions.mdx)
* Last updated on January 10, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[App versions](/build-reference/app-versions/#app-versions)[Using app versions in your app](/build-reference/app-versions/#using-app-versions-in-your-app)[Recommended workflow](/build-reference/app-versions/#recommended-workflow)[User-facing version](/build-reference/app-versions/#user-facing-version)[Developer-facing build version](/build-reference/app-versions/#developer-facing-build-version)[Remote version source](/build-reference/app-versions/#remote-version-source)[Syncing already defined versions to remote](/build-reference/app-versions/#syncing-already-defined-versions-to-remote)[Syncing versions from remote to local](/build-reference/app-versions/#syncing-versions-from-remote-to-local)[Limitations](/build-reference/app-versions/#limitations)[Local version source](/build-reference/app-versions/#local-version-source)[Limitations](/build-reference/app-versions/#limitations-1)