Privacy manifests - Expo Documentation

[Docs](/)

[Blog](https://expo.dev/blog)[Changelog](https://expo.dev/changelog)[Star Us on GitHub](https://github.com/expo/expo)

Search

[Home](/)[Guides](/guides/overview)[EAS](/eas)[Reference](/versions/latest)[Learn](/tutorial/overview)

[Overview](/guides/overview)

Development process

[Develop an app with Expo](/workflow/overview)[Configure with app config](/workflow/configuration)[Continuous Native Generation](/workflow/continuous-native-generation)[Using libraries](/workflow/using-libraries)[Privacy manifests](/guides/apple-privacy)[Permissions](/guides/permissions)[Environment variables](/guides/environment-variables)

Linking

Write native code

Compile locally

Web

Bundling

Existing React Native apps

Existing native apps

Reference

Expo Router

[Introduction](/router/introduction)[Installation](/router/installation)

Router 101

Navigation patterns

Advanced

Reference

Migration

Expo Modules API

[Overview](/modules/overview)[Get started](/modules/get-started)

Tutorials

Reference

Push notifications

[Overview](/push-notifications/overview)[About notification types](/push-notifications/what-you-need-to-know)[Expo push notifications setup](/push-notifications/push-notifications-setup)[Send notifications with the Expo Push Service](/push-notifications/sending-notifications)[Handle incoming notifications](/push-notifications/receiving-notifications)

Reference

More

[Upgrade Expo SDK](/workflow/upgrading-expo-sdk-walkthrough)

Assorted

Integrations

Troubleshooting

Regulatory compliance

[Data and Privacy protection](/regulatory-compliance/data-and-privacy-protection)[GDPR compliance](/regulatory-compliance/gdpr)[HIPAA compliance](/regulatory-compliance/hipaa)[Privacy Shield](/regulatory-compliance/privacy-shield)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Privacy manifests
=================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/apple-privacy.mdx)

Learn about configuring iOS privacy manifests for your mobile app.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/apple-privacy.mdx)

---

If you're using a native iOS library that uses a "restricted reason" APIs, you'll need to configure an iOS privacy manifest to declare why you're including native code to call those APIs.

More details and a list of "required reason" APIs can be found in the [Apple Developer Documentation](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files).

> The information and steps included in this guide are still in development and may change due to new tools built for this purpose or new requirements from Apple.

What is a Privacy manifest?
---------------------------

A privacy manifest is a file named PrivacyInfo.xcprivacy that is included in your iOS native project. This file is used to declare why the app includes native code that calls into certain APIs that Apple considers sensitive.

These APIs currently include accessing UserDefaults, file timestamp, system boot time, disk space, and active keyboard. Apple considers it an open list that can be expanded in the future.

Configuration in app config
---------------------------

You can include an iOS privacy manifest by using the `privacyManifests` field under `expo.ios` in your app config.

app.json

Copy

```
{
  "expo": {
    "name": "My App",
    "slug": "my-app",
    %%placeholder-start%%... %%placeholder-end%%
    "ios": {
      "privacyManifests": {
        "NSPrivacyAccessedAPITypes": [
          {
            "NSPrivacyAccessedAPIType": "NSPrivacyAccessedAPICategoryUserDefaults",
            "NSPrivacyAccessedAPITypeReasons": ["CA92.1"]
          }
        ]
      }
    }
  }
}

```

Make sure you have updated your Expo SDK libraries to the latest versions for your SDK version using `npx expo install --fix`.

Are you using this library in an existing React Native app?

You can include an iOS privacy manifest in a bare Expo app by creating a PrivacyInfo.xcprivacy file using Xcode and adding it to your iOS app target.
Follow [Apple's Privacy manifest files](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files) guide to create a PrivacyInfo.xcprivacy file.

You can identify the `NSPrivacyAccessedAPITypes` and `NSPrivacyAccessedAPITypeReasons` values by looking at the [Apple Developer documentation](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_use_of_required_reason_api).

### Including required reasons for Expo SDK packages and other third-party libraries

As of now, Apple does not correctly parse all the PrivacyInfo files included by static CocoaPods dependencies (such as Expo SDK packages and other ecosystem libraries). You may need to include the required reasons for the APIs used by those dependencies in your app's PrivacyInfo.xcprivacy file or the configuration in the app.json.

All Expo SDK packages that use "required reason" APIs file have a PrivacyInfo file included in the package directory. Here's [an example file](https://github.com/expo/expo/blob/main/packages/expo-application/ios/PrivacyInfo.xcprivacy) included with the `expo-application` library.

You can usually identify the required reasons for the APIs used by other third-party libraries by checking if the library you intend to use has a PrivacyInfo.xcprivacy file in the node\_modules/package\_name/ios directory. If it does, you can check the `NSPrivacyAccessedAPITypes` and `NSPrivacyAccessedAPITypeReasons` values in that file and copy those values to your configuration.

As an alternative, Apple notifies developers after they submit a build with missing privacy manifest files or specific reasons. You can wait until you receive a notification email from Apple and then include the required reasons listed in the email in your app's PrivacyInfo.xcprivacy file (if you don't use [CNG](/workflow/continuous-native-generation)) or the configuration in your app.json file.

Testing the Privacy manifest
----------------------------

You can test the privacy manifest by building your app and submitting it, either through App Store review process or to TestFlight's external review. Apple will email you within a few minutes of submitting if your app is missing any required reasons for the APIs used.

[Previous (Development process)

Using libraries](/workflow/using-libraries)[Next (Development process)

Permissions](/guides/permissions)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/apple-privacy.mdx)
* Last updated on May 01, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[What is a Privacy manifest?](/guides/apple-privacy/#what-is-a-privacy-manifest)[Configuration in app config](/guides/apple-privacy/#configuration-in-app-config)[Including required reasons for Expo SDK packages and other third-party libraries](/guides/apple-privacy/#including-required-reasons-for-expo-sdk-packages-and-other-third-party-libraries)[Testing the Privacy manifest](/guides/apple-privacy/#testing-the-privacy-manifest)