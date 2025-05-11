Additional platform support - Expo Documentation

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

[Create a native module](/modules/native-module-tutorial)[Create a native view](/modules/native-view-tutorial)[Create a module with a config plugin](/modules/config-plugin-and-native-module-tutorial)[How to use a standalone Expo module](/modules/use-standalone-expo-module-in-your-project)[Wrap third-party native libraries](/modules/third-party-library)[Integrate in an existing library](/modules/existing-library)[Additional platform support](/modules/additional-platform-support)

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

Additional platform support
===========================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/modules/additional-platform-support.mdx)

Learn how to add support for macOS and tvOS platforms.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/modules/additional-platform-support.mdx)

---

Expo Modules API provides first-class support for Android and iOS. However, since all Apple platforms are based on the same foundation and use the same programming language, targeting other [Out-of-Tree platforms](https://reactnative.dev/docs/out-of-tree-platforms) in the Expo module is possible.

Currently, only macOS and tvOS platforms are supported. This guide will walk you through adding support for these platforms.

1

Use the `"apple"` platform in `expo-module.config.json`
-------------------------------------------------------

To provide seamless support for other Apple platforms, Expo SDK introduced a universal `"apple"` platform to instruct the [autolinking](/modules/autolinking) that the module may support any of the Apple platform and whether to link the module in the specific CocoaPods target is moved off to the podspec. If you have used `"ios"` before, you can safely replace it:

expo-module.config.json

Copy

```
{
-   "platforms": ["ios"],
-   "ios": {
-     "modules": ["MyModule"]
-   }
+   "platforms": ["apple"],
+   "apple": {
+     "modules": ["MyModule"]
+   }
}

```

2

Update the podspec to declare support for other platforms
---------------------------------------------------------

The module's podspec needs to be updated with a list of the supported platforms. Otherwise, CocoaPods would fail to install the pod on targets for the other platforms. As mentioned in the first step, this part of the spec is the source of truth for autolinking when the module is configured with a universal `"apple"` platform.

Module's podspec

Copy

```
- s.platform       = :ios, '13.4'
+ s.platforms = {
+   :ios => '13.4',
+   :tvos => '13.4',
+   :osx => '10.15'
+ }

```

Any changes in the podspec require running `pod install` to have an effect.

3

Set up `react-native-macos` or `react-native-tvos` in the app
-------------------------------------------------------------

If you are writing a local module and your app is already set up, you can skip this step. Otherwise, you will need to set up your app or the example app if you are writing a standalone (non-local) module.

* For macOS: follow the official [Install React Native for macOS](https://microsoft.github.io/react-native-windows/docs/rnm-getting-started#install-the-macos-extension) guide from `react-native-macos` documentation.
* For tvOS: follow the instructions in the [`react-native-tvos`](https://github.com/react-native-tvos/react-native-tvos) repository. If you are building an Expo app, you should also follow the instructions in the [Build Expo apps for TV guide](/guides/building-for-tv).

4

Review the code for using APIs not supported on these platforms
---------------------------------------------------------------

Platform APIs may differ between Apple platforms. The most noticeable difference comes from relying on different UI frameworks â`UIKit` on iOS/tvOS and `AppKit` on macOS.

Both `react-native-macos` and `expo-modules-core` provide aliases and polyfills to reference`UIKit` classes on macOS target (for example, `UIView` is an alias to `NSView`, `UIApplication` is an alias to `NSApplication`), but it's usually not enough for iOS-first libraries to support other platforms out of the box. You may need to write conditionally compiled code that uses different implementations depending on the platform.

To do this, use Swift compiler directives with the `os` condition, which includes a given piece of code when our app is being built for a specific platform. In combination with the `#if` and `#else` directives, lets you set up platform-specific branches within the cross-platform code.

```
#if os(iOS)
  // iOS implementation
#elseif os(macOS)
  // macOS implementation
#elseif os(tvOS)
  // tvOS implementation
#endif

```

Your module is now ready to be used on Out-of-Tree platform.

[Previous (Expo Modules API - Tutorials)

Integrate in an existing library](/modules/existing-library)[Next (Expo Modules API - Reference)

Module API](/modules/module-api)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/modules/additional-platform-support.mdx)
* Last updated on May 01, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Use the "apple" platform in expo-module.config.json](/modules/additional-platform-support/#use-the-apple-platform-in-expo-moduleconfigjson)[Update the podspec to declare support for other platforms](/modules/additional-platform-support/#update-the-podspec-to-declare-support-for-other-platforms)[Set up react-native-macos or react-native-tvos in the app](/modules/additional-platform-support/#set-up-react-native-macos-or-react-native-tvos-in-the-app)[Review the code for using APIs not supported on these platforms](/modules/additional-platform-support/#review-the-code-for-using-apis-not-supported-on-these-platforms)