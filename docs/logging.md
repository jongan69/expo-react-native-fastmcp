View logs - Expo Documentation

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

[Work with monorepos](/guides/monorepos)[View logs](/workflow/logging)[Development and production modes](/workflow/development-mode)[Common development errors](/workflow/common-development-errors)[Android Studio Emulator](/workflow/android-studio-emulator)[iOS Simulator](/workflow/ios-simulator)[New Architecture](/guides/new-architecture)[React Compiler](/guides/react-compiler)

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

View logs
=========

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/workflow/logging.mdx)

Learn how to view logs when using Expo CLI, native logs in Android Studio and Xcode, and system logs.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/workflow/logging.mdx)

---

Logging information in a React Native app works similarly to in a web browser. You can use `console.log`, `console.warn` and `console.error`. However, at times, you might want to dive deep to get more useful information about what's happening in your app. For that, you can use native logs and system logs.

Console logs
------------

When you run `npx expo start` and connect a device, console logs will show up in the terminal process. These logs are sent from the runtime to Expo CLI over web sockets, meaning the results are lower fidelity than connecting dev tools directly to the engine.

You can view high fidelity logs and use advanced logging functions like `console.table` by creating a development build with [Hermes](/guides/using-hermes), and [connecting the inspector](/guides/using-hermes#javascript-inspector-for-hermes).

Native logs
-----------

You can view native runtime logs in Android Studio and Xcode by compiling the native app locally. For more information, see [native debugging](/debugging/runtime-issues#native-debugging).

System logs
-----------

While it's usually not necessary, if you want to see logs for everything happening on your device, for example, even the logs from other apps and the OS, you can use the following commands:

Terminal

`# Show system logs for an Android device with adb logcat`

`-Â``npx react-native log-android`

`# Show system logs for an iOS device`

`-Â``npx react-native log-ios`

[Previous (Development process - Reference)

Work with monorepos](/guides/monorepos)[Next (Development process - Reference)

Development and production modes](/workflow/development-mode)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/workflow/logging.mdx)
* Last updated on May 16, 2023

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Console logs](/workflow/logging/#console-logs)[Native logs](/workflow/logging/#native-logs)[System logs](/workflow/logging/#system-logs)