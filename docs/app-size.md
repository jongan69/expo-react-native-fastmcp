Understanding app size - Expo Documentation

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

Understanding app size
======================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/distribution/app-size.mdx)

Learn about how to determine what the actual size of your app will be when distributed to users, and how to get insights into your app size and optimize it.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/distribution/app-size.mdx)

---

A common concern for developers is how much space their app takes up on the app store. This guide will help you:

* Understand what different build artifacts are used for
* Figure out the actual size of your app when distributed to users
* Get insights into your app size and optimize it

Why is my app so big?
---------------------

It probably isn't, actually! When examining the resulting artifact of a release build for an app, it's common for developers who are unfamiliar with native Android and iOS development to be surprised by the file size â it's usually much larger than they would expect for an app if they were to download it from an app store. This is not the actual size of your app, which will be distributed on app stores! When people talk about app sizes, they mean the size of the app that they will download to their device, not the size that will be uploaded to app stores or shared in development and testing.

There are various types of build artifacts that serve different purposes, and they are almost all larger than what users will see when they download your app from a store. This is because these builds are not optimized to target specific devices like they would when downloading from a store, but rather they typically include all of the code and resources that your app needs to run on a wide range of devices.

Android apps
------------

There are two types of Android build artifacts that you will interact with: APKs and AABs.

### `.apk` (Android Package)

When you build an APK with Gradle in a React Native project, the default behavior is to create a universal binary, which contains all the resources for all the different device types that your app supports. For example, it includes asset for every screen size, every CPU architecture, and every language, even though a single device will only need one of each. This means you can share this one file with anybody to install directly to their device, perhaps with [Orbit](https://expo.dev/orbit) or `adb` directly, and that will work.

Of course, if you're running an incredibly popular app store that serves millions of users, you don't want to send the same 50 MB file to every single user, especially if they're only going to use a fraction of the resources in the APK. This is why the Google Play Store and other app stores have a feature called "App Bundles" (Android) that allows you to upload a single binary and then the store will generate a custom binary for each user based on their device's needs.

### `.aab` (Android App Bundle)

On Android, all new apps submitted to the Play Store must be built as an [Android App Bundle (.aab)](https://developer.android.com/platform/technology/app-bundle). Once you have submitted the binaries to their respective stores, you will be able to see the download size for various device types.

### Determining Android app download and install size

Typically, what app developers care about the "download size" on the Play Store (what the users see in the store listing when they go to download the app). This will be the size of the APK that Google Play generates from your AAB, which is tailored to the user's device.

The only truly accurate way to see what your final app size will be shipped to users is to upload your app to the stores and download it on a physical device. Google Play also provides a reliable estimate for the expected download size on your developer dashboard. You can find this under the App size page in Android vitals on the [Google Play Developer Console](https://play.google.com/console/). For more information, see [Optimize your appâs size and stay within Google Play app size limits](https://support.google.com/googleplay/android-developer/answer/9859372?hl=en).

Why did my APK size increase after upgrading to React Native 0.73 and above?

React Native 0.73 bumped the Android `minSdkVersion` to `23`. This had the side effect of changing the default value of [`extractNativeLibs`](https://developer.android.com/guide/topics/manifest/application-element#extractNativeLibs%60) to `false`.

> If set to `false`, your native libraries are stored uncompressed in the APK. Although your APK might be larger, your application loads faster because the libraries load directly from the APK at runtime.

The following table shows that while the APK size increased, which may slightly impact download time for testers with [internal distribution](/build/internal-distribution), the Google Play Store size remained the same.

| SDK | APK (debug variant) | APK (release variant) | AAB | Google Play |
| --- | --- | --- | --- | --- |
| 49 | 66 MB | 27.6 MB | 28.2 MB | 11.7 MB |
| 50 | 168.1 MB | 62.1 MB | 27.4 MB | 11.7 MB |

If you would like to revert to the previous behavior, you can set `useLegacyPackaging` to `true` in your gradle.properties or by using [`expo-build-properties`](/versions/latest/sdk/build-properties).

iOS apps
--------

The download size on the App Store of a minimal React Native app (created using the blank template) [is just under 4 MB](https://x.com/aleqsio/status/1844045829973344457).

There are two types of iOS build artifacts that you will interact with: APPs and IPAs.

### `.app` (iOS application bundle)

This is the actual application bundle for your app. When you download and install a build of your app into an iOS Simulator, you are downloading the `.app` bundle. These can either target specific architectures or be universal binaries. The size of your `.app` doesn't necessarily tell you too much about what the download size of your app will be on the store. You can't install a `.app` file directly to a physical iOS device.

### `.ipa` (iOS App Store Package)

IPA files are [ZIP](https://en.wikipedia.org/wiki/ZIP)) files that include the `.app` bundle and other resources that are needed to run the app on an iOS device. They are used for various types of distribution, including App Store, Ad Hoc, Enterprise, and TestFlight.

They include security and code signing information, such as the provisioning profile and entitlements. The App Store will process the IPA file and split it into smaller binaries for each device type, so the size of the IPA also does not represent the download size of your app.

### Determining iOS app download and install size

Typically, app developers care about the "download size" on the App Store (what the users see in the store listing when they go to download the app). This will be the size of the split IPA generated by the store from your universal IPA.

The only truly accurate way to see what your final app size will be shipped to users is to upload your app to the App Store and download it on a physical device. You can get accurate estimates from TestFlight: on [App Store Connect](https://appstoreconnect.apple.com/), navigate to TestFlight and select your build by clicking on the build number, then switch to the Build Metadata tab and click App File Sizes. You will see a list of estimated download and install sizes depending on the device type. Actually install sizes may also vary slightly depending on the iOS version of the device.

Optimizing app size
-------------------

As you add features to your app, you will add code, libraries, and assets, which may increase its size. If app size is important to you and your users, you may want to routinely review the size and optimize it. The following sections will help you understand what you can do to optimize several aspects of your app.

### Static assets

One of the most common sources of app size bloat is assets, such as fonts, icons, images, videos, and sounds. These can come from the assets that you import directly into your code, as well as JavaScript and native libraries. You won't be able to get a complete picture by reviewing your app assets directory.

Start by examining a build artifact to determine what assets are included in it.

* For Android, you can use [Android APK Analyzer](https://developer.android.com/studio/debug/apk-analyzer) or [apktool](https://apktool.org/) to inspect the contents of your app
* For iOS, rename an IPA file from `app.ipa` to `app.zip` and extract it to examine the contents, using the macOS utility `assetutil` to inspect Assets.car.

### JavaScript bundle size

To analyze JavaScript bundles, [use Expo Atlas](/guides/analyzing-bundles). You may find libraries that you thought were very small actually have a large impact on the bundle, or that you forgot to remove a library after you stopped using it, and so on.

### Platform-specific optimizations

Independent of React Native and Expo, you can optimize your app for Android and iOS by using the following tools:

[Android Developers: Reduce your app size

Advice directly from Google about reducing your Android app size.](https://developer.android.com/topic/performance/reduce-apk-size)
[Apple Developer: Reducing your app's size

Advice directly from Apple about reducing your iOS app size.](https://developer.apple.com/documentation/xcode/reducing-your-app-s-size)

[Previous (Distribution)

App transfers](/distribution/app-transfers)[Next (Reference)

Webhooks](/eas/webhooks)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/distribution/app-size.mdx)
* Last updated on May 07, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Why is my app so big?](/distribution/app-size/#why-is-my-app-so-big)[Android apps](/distribution/app-size/#android-apps)[.apk (Android Package)](/distribution/app-size/#apk-android-package)[.aab (Android App Bundle)](/distribution/app-size/#aab-android-app-bundle)[Determining Android app download and install size](/distribution/app-size/#determining-android-app-download-and-install-size)[iOS apps](/distribution/app-size/#ios-apps)[.app (iOS application bundle)](/distribution/app-size/#app-ios-application-bundle)[.ipa (iOS App Store Package)](/distribution/app-size/#ipa-ios-app-store-package)[Determining iOS app download and install size](/distribution/app-size/#determining-ios-app-download-and-install-size)[Optimizing app size](/distribution/app-size/#optimizing-app-size)[Static assets](/distribution/app-size/#static-assets)[JavaScript bundle size](/distribution/app-size/#javascript-bundle-size)[Platform-specific optimizations](/distribution/app-size/#platform-specific-optimizations)