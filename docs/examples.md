Example CI/CD workflows - Expo Documentation

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

Example CI/CD workflows
=======================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas/workflows/examples.mdx)

Common CI/CD workflows that are useful for your project.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas/workflows/examples.mdx)

---

The following workflows are examples of how you can use EAS Workflows to automate your development and release processes. They can help you and your team develop, review each other's PRs, and release changes to your users.

Development builds workflow
---------------------------

[Development builds](/develop/development-builds/introduction) are specialized builds of your project that include Expo's developer tools. These types of builds include all native dependencies inside your project, enabling you to run a production-like build of your project on a simulator, emulator, or a physical device.

Prerequisites

2 requirements

1.

Set up your environment

To get started, you'll need to configure your project and devices to build and run development builds. Learn how to set up your environment for development builds with the following guides:

[Android device setup

Get your project ready for development builds.](/get-started/set-up-your-environment?mode=development-build&platform=android&device=physical)[Android Emulator setup

Get your project ready for development builds.](/get-started/set-up-your-environment?mode=development-build&platform=android&device=simulated)[iOS device setup

Get your project ready for development builds.](/get-started/set-up-your-environment?mode=development-build&platform=ios&device=physical)[iOS Simulator setup

Get your project ready for development builds.](/get-started/set-up-your-environment?mode=development-build&platform=ios&device=simulated)

2.

Create build profiles

After you've configured your project and devices, add the following build profiles to your eas.json file.

eas.json

Copy

```
{
  "build": {
    "development": {
      "developmentClient": true,
      "distribution": "internal"
    },
    "development-simulator": {
      "developmentClient": true,
      "distribution": "internal",
      "ios": {
        "simulator": true
      }
    }
  }
}

```

The following workflow creates a build for each platform and for both physical devices, Android emulators, and iOS simulators. They all will run in parallel.

.eas/workflows/create-development-builds.yml

Copy

```
name: Create development builds

jobs:
  android_development_build:
    name: Build Android
    type: build
    params:
      platform: android
      profile: development
  ios_device_development_build:
    name: Build iOS device
    type: build
    params:
      platform: ios
      profile: development
  ios_simulator_development_build:
    name: Build iOS simulator
    type: build
    params:
      platform: ios
      profile: development-simulator

```

Run the above workflow with:

Terminal

Copy

`-Â``eas workflow:run .eas/workflows/create-development-builds.yml`

Preview updates workflow
------------------------

Once you've made changes to your project, you can share a preview of your changes with your team by publishing a [preview update](/review/share-previews-with-your-team).

You can access preview updates in the development build UI and through scannable QR codes on the Expo dashboard. When publishing a preview on every commit, your team can review changes without pulling the latest changes and running them locally.

Prerequisites

2 requirements

1.

Set up EAS Update

Your project needs to have [EAS Update](/eas-update/introduction) setup to publish preview updates. You can set up your project with:

Terminal

Copy

`-Â``eas update:configure`

2.

Create new development builds

After you've configured your project, create new [development builds](/develop/development-builds/create-a-build) for each platform.

The following workflow publishes a preview update for every commit on every branch.

.eas/workflows/publish-preview-update.yml

Copy

```
name: Publish preview update

on:
  push:
    branches: ['*']

jobs:
  publish_preview_update:
    name: Publish preview update
    type: update
    params:
      branch: ${{ github.ref_name || 'test' }}

```

Deploy to production workflow
-----------------------------

When you're ready to deliver changes to your users, you can build and submit to the app stores or you can send an over-the-air update. The following workflow detects if you need new builds, and if so, it sends them to the app stores. If new builds are not required, it will send an over-the-air update.

Prerequisites

3 requirements

1.

Set up EAS Build

To set up EAS Build, follow this guide:

[EAS Build prerequisites

Get your project ready for EAS Build.](/build/setup)

2.

Set up EAS Submit

To set up EAS Submit, follow the Google Play Store and Apple App Store submissions guides:

[Google Play Store CI/CD submission guide

Get your project ready for Google Play Store submissions.](/submit/android#submitting-your-app-using-cicd-services)[Apple App Store CI/CD submission guide

Get your project ready for Apple App Store submissions.](/submit/ios#submitting-your-app-using-cicd-services)

3.

Set up EAS Update

And finally, you'll need to set up EAS Update, which you can do with:

Terminal

Copy

`-Â``eas update:configure`

The following workflow runs on each push to the `main` branch and performs the following:

* Takes a hash of the native characteristics of the project using [Expo Fingerprint](/versions/latest/sdk/fingerprint).
* Checks if a build already exists for the fingerprint.
* If a build does not exist, it will build the project and submit it to the app stores.
* If a build exists, it will send an over-the-air update.

.eas/workflows/deploy-to-production.yml

Copy

```
name: Deploy to production

on:
  push:
    branches: ['main']

jobs:
  fingerprint:
    name: Fingerprint
    type: fingerprint
  get_android_build:
    name: Check for existing android build
    needs: [fingerprint]
    type: get-build
    params:
      fingerprint_hash: ${{ needs.fingerprint.outputs.android_fingerprint_hash }}
      profile: production
  get_ios_build:
    name: Check for existing ios build
    needs: [fingerprint]
    type: get-build
    params:
      fingerprint_hash: ${{ needs.fingerprint.outputs.ios_fingerprint_hash }}
      profile: production
  build_android:
    name: Build Android
    needs: [get_android_build]
    if: ${{ !needs.get_android_build.outputs.build_id }}
    type: build
    params:
      platform: android
      profile: production
  build_ios:
    name: Build iOS
    needs: [get_ios_build]
    if: ${{ !needs.get_ios_build.outputs.build_id }}
    type: build
    params:
      platform: ios
      profile: production
  submit_android_build:
    name: Submit Android Build
    needs: [build_android]
    type: submit
    params:
      build_id: ${{ needs.build_android.outputs.build_id }}
  submit_ios_build:
    name: Submit iOS Build
    needs: [build_ios]
    type: submit
    params:
      build_id: ${{ needs.build_ios.outputs.build_id }}
  publish_android_update:
    name: Publish Android update
    needs: [get_android_build]
    if: ${{ needs.get_android_build.outputs.build_id }}
    type: update
    params:
      branch: production
      platform: android
  publish_ios_update:
    name: Publish iOS update
    needs: [get_ios_build]
    if: ${{ needs.get_ios_build.outputs.build_id }}
    type: update
    params:
      branch: production
      platform: ios

```

[Previous (EAS Workflows)

Get started](/eas/workflows/get-started)[Next (EAS Workflows)

Syntax for EAS Workflows](/eas/workflows/syntax)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas/workflows/examples.mdx)
* Last updated on April 07, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Development builds workflow](/eas/workflows/examples/#development-builds-workflow)[Preview updates workflow](/eas/workflows/examples/#preview-updates-workflow)[Deploy to production workflow](/eas/workflows/examples/#deploy-to-production-workflow)