Common development errors - Expo Documentation

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

Common development errors
=========================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/workflow/common-development-errors.mdx)

A list of common development errors that are encountered by developers using Expo.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/workflow/common-development-errors.mdx)

---

This page outlines a list of errors that are commonly encountered by developers using Expo. For each error, the first bullet provides an explanation for why the error occurs and the second bullet contains debugging suggestions. If there is an error you think belongs here, we welcome and encourage you to [create a PR](https://github.com/expo/expo/pulls)!

### Metro bundler ECONNREFUSED 127.0.0.1:19001

* An error is preventing the connection to your local development server.
* Run `rm -rf .expo` to clear your local state. Check for firewalls or [proxies](/troubleshooting/proxies) affecting the network you are currently connected to.

### Module AppRegistry is not a registered callable module (calling runApplication)

* An error in your code is preventing the JavaScript bundle from being executed on startup.
* Try running `npx expo start --no-dev --minify` to reproduce the production JS bundle locally. If possible, connect your device and access the device logs via Android Studio or Xcode. Device logs contain much more detailed stacktraces and information. Check to see if you have any changes or errors in your Babel configuration. In some rare cases, this issue could be caused by incompatibility between the Metro JavaScript minifier and certain code in your app ([more information](https://forums.expo.dev/t/change-minifierconfig-for-minify-uglify/36460/2)).

### npm ERR! No git binary found in $PATH

* Either you do not have git installed or it is not properly configured in your `$PATH`.
* [Install git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) if you have not already. Otherwise, check how to set it in your `$PATH` based on your OS.

### XX.X.X is not a valid SDK version

* The SDK version you are running has been deprecated and is no longer supported.
* [Upgrade your project](/workflow/upgrading-expo-sdk-walkthrough) to a supported SDK version. If you are using a supported version and see this message, you'll need to update your Expo Go app.

### React Native version mismatch

* The development server running in your terminal is bundling a different version of React Native than the app in your device or simulator.
* [Align your versions of react-native](/troubleshooting/react-native-version-mismatch) by checking the versions in your app.json and package.json

### Application has not been registered

* There is a mismatch between the AppKey registered in the native and JS portion of your app.
* [Align your AppKey](/troubleshooting/application-has-not-been-registered) with the native side of your project.

### Application not behaving as expected

* It is possible caches may be preventing you from seeing the current state of your application.
* Clear all caches associated with your project in [Unix-like](/troubleshooting/clear-cache-macos-linux) or [Windows](/troubleshooting/clear-cache-windows) systems.

[Previous (Development process - Reference)

Development and production modes](/workflow/development-mode)[Next (Development process - Reference)

Android Studio Emulator](/workflow/android-studio-emulator)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/workflow/common-development-errors.mdx)
* Last updated on July 04, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Metro bundler ECONNREFUSED 127.0.0.1:19001](/workflow/common-development-errors/#metro-bundler-econnrefused-12700119001)[Module AppRegistry is not a registered callable module (calling runApplication)](/workflow/common-development-errors/#module-appregistry-is-not-a-registered-callable-module-calling-runapplication)[npm ERR! No git binary found in $PATH](/workflow/common-development-errors/#npm-err-no-git-binary-found-in-path)[XX.X.X is not a valid SDK version](/workflow/common-development-errors/#xxxx-is-not-a-valid-sdk-version)[React Native version mismatch](/workflow/common-development-errors/#react-native-version-mismatch)[Application has not been registered](/workflow/common-development-errors/#application-has-not-been-registered)[Application not behaving as expected](/workflow/common-development-errors/#application-not-behaving-as-expected)