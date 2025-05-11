expo-module.config.json - Expo Documentation

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

[Module API](/modules/module-api)[Android lifecycle listeners](/modules/android-lifecycle-listeners)[iOS AppDelegate subscribers](/modules/appdelegate-subscribers)[Autolinking](/modules/autolinking)[expo-module.config.json](/modules/module-config)[Mocking native calls](/modules/mocking)[Design considerations](/modules/design)

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

expo-module.config.json
=======================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/modules/module-config.mdx)

Learn about different configuration options available in expo-module.config.json.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/modules/module-config.mdx)

---

Expo modules are configured in expo-module.config.json. This file currently is capable of configuring autolinking and module registration. The following properties are available:

* `platforms` â An array of supported platforms. Acceptable values are `android`, `apple` (or use the more granular `ios` / `macos` / `tvos`), `web` and `devtools` (see [Create a dev tools plugin](/debugging/create-devtools-plugins)).
* `apple` â Config with options specific to Apple platforms
  + `modules` â Names of Swift native modules classes to put to the generated modules provider file.
  + `appDelegateSubscribers` â Names of Swift classes that hook into `ExpoAppDelegate` to receive AppDelegate lifecycle events.
* `android` â Config with options specific to Android platform
  + `modules` â Full names (package + class name) of Kotlin native modules classes to put to the generated package provider file.

[Previous (Expo Modules API - Reference)

Autolinking](/modules/autolinking)[Next (Expo Modules API - Reference)

Mocking native calls](/modules/mocking)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/modules/module-config.mdx)
* Last updated on February 10, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).