Development and production modes - Expo Documentation

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

Development and production modes
================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/workflow/development-mode.mdx)

Learn how to run a project in development mode or production mode.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/workflow/development-mode.mdx)

---

Your project will always run in either development or production mode. By default, running your project locally with `npx expo start` runs it in development mode, whereas a published project (with `eas update`), or any standalone app, will run in production mode.

Development mode includes useful warnings and gives you access to tools that make development and debugging easier. Production mode [minifies your code](/guides/customizing-metro#minification) and better represents the performance your app will have on end users' devices. Let's look at each of these modes in more detail and learn how you can switch between them.

Development mode
----------------

React Native includes some very useful tools for development: remote JavaScript debugging in Chrome, live reload, hot reloading, and an element inspector similar to the beloved inspector you use in Chrome. If you want to see how to use those tools, see [Debugging](/debugging/runtime-issues).

Development mode also performs validations while your app is running to give you warnings. For example, if you're using a deprecated property or if you forgot to pass a required property into a component. The video below shows the Element Inspector and Performance Monitor in action on both Android Emulator and iOS Simulator:

> This comes at a cost. Your app runs slower in development mode.   
>  You can switch it on and off with the Expo CLI, see [Production mode](/workflow/development-mode#production-mode). When you switch it, close and re-open your app for the change to take effect. Any time you are testing your app's performance, make sure to disable development mode.

### View the developer menu

The menu gives access to a host of features that make development and debugging much easier. For more information on how to open it on Android and iOS, see [Developer menu](/debugging/tools#developer-menu).

Production mode
---------------

Production mode is most useful for two things:

* Testing your app's performance, as Development slows your app down considerably.
* Catching bugs that only show up in production.

The easiest way to simulate how your project will run on end users' devices is with the command:

Terminal

Copy

`-Â``npx expo start --no-dev --minify`

It runs the JavaScript of your app in production mode (which tells the Metro bundler to set the `__DEV__` environment variable to `false`, among a few other things). The `--minify` flag minifies your app. This flag also eliminates unnecessary data such as comments, formatting, and unused code. If you are getting an error or crash in your standalone app, running your project with this command can save you a lot of time in finding the root cause.

To completely compile your app for production see [Compiling Android](/more/expo-cli#compiling-android) and [Compiling iOS](/more/expo-cli#compiling-ios).

[Previous (Development process - Reference)

View logs](/workflow/logging)[Next (Development process - Reference)

Common development errors](/workflow/common-development-errors)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/workflow/development-mode.mdx)
* Last updated on August 31, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Development mode](/workflow/development-mode/#development-mode)[View the developer menu](/workflow/development-mode/#view-the-developer-menu)[Production mode](/workflow/development-mode/#production-mode)