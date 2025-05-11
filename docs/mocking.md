Mocking native calls in Expo modules - Expo Documentation

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

Mocking native calls in Expo modules
====================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/modules/mocking.mdx)

Learn about mocking native calls in Expo modules.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/modules/mocking.mdx)

---

The recommended way to write unit tests for an Expo project is to use [Jest](https://jestjs.io/) and the `jest-expo` preset.

To write a unit test for an app that uses native code, you need to mock native calls.
The term Mocking means to replace the actual implementation of a function with a fake version that does not perform any actions. This approach is useful for running unit tests on a local computer as it involves bypassing the need for native code which is only available on a device, and any code that calls native functions on a local machine will not work.

Expo SDK includes a set of default mocks for each of our community packages. You can also mock any JS code yourself using built-in Jest APIs such as [mock functions](https://jestjs.io/docs/mock-functions).

However, to provide default mocks in your Expo Module, we offer a method to bundle them. This ensures that when your module user runs unit tests, they will automatically use a mocked implementation.

Providing mocks for a module
----------------------------

Create a file with the same name as the native module you want to mock and place it in your module's mocks directory. Make sure to export the mock implementation from this file.
The `jest-expo` preset will automatically return the exported functions because of a `requireNativeModule` call when running during a unit test.

For example, the `expo-clipboard` library has a native module called `ExpoClipboard`. You will create a ExpoClipboard.ts in the mocks directory to mock it.

ExpoClipboard.ts

Copy

```
export async function hasStringAsync(): Promise<boolean> {
  return false;
}

```

Now, in a unit test, calling `ExpoClipboard.hasStringAsync()` returns `false`.

Automatic generation of mocks
-----------------------------

Maintaining mocks for native modules can be a lot of work if the native module has multiple methods. To make this easier, we provide a script that automatically generates mocks for all native functions in a module.
It works for generating mocks in TypeScript and JavaScript based on the Swift implementation in your module.

To use this script, you have to install [SourceKitten](https://github.com/jpsim/SourceKitten) framework. Then, navigate to the module directory (where your module's expo-module.config.json is located) and run the `generate-ts-mocks` command.

Terminal

Copy

`-Â``brew install sourcekitten`

`-Â``npx expo-modules-test-core generate-ts-mocks`

The command above generates ExpoModuleName.ts in the mocks directory of your module. It contains a mock implementation for each native method and view in your module.

> Tip: You can also run `generate-js-mocks` to generate mocks in JavaScript.

More
----

[Unit testing with Jest

Learn how to set up and configure the jest-expo package to write unit and snapshot tests for a project.](/develop/unit-testing)

[Previous (Expo Modules API - Reference)

expo-module.config.json](/modules/module-config)[Next (Expo Modules API - Reference)

Design considerations](/modules/design)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/modules/mocking.mdx)
* Last updated on December 18, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Providing mocks for a module](/modules/mocking/#providing-mocks-for-a-module)[Automatic generation of mocks](/modules/mocking/#automatic-generation-of-mocks)[More](/modules/mocking/#more)