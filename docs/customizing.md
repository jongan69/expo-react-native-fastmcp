Add custom native code - Expo Documentation

[Docs](/)

[Blog](https://expo.dev/blog)[Changelog](https://expo.dev/changelog)[Star Us on GitHub](https://github.com/expo/expo)

Search

[Home](/)[Guides](/guides/overview)[EAS](/eas)[Reference](/versions/latest)[Learn](/tutorial/overview)

[Overview](/guides/overview)

Development process

[Develop an app with Expo](/workflow/overview)[Configure with app config](/workflow/configuration)[Continuous Native Generation](/workflow/continuous-native-generation)[Using libraries](/workflow/using-libraries)[Privacy manifests](/guides/apple-privacy)[Permissions](/guides/permissions)[Environment variables](/guides/environment-variables)

Linking

Write native code

[Add custom native code](/workflow/customizing)[Adopt Prebuild](/guides/adopting-prebuild)

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

Add custom native code
======================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/workflow/customizing.mdx)

Learn how to add custom native code to your Expo project.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/workflow/customizing.mdx)

---

You can add custom native code by using one or both of the following approaches:

* Using libraries that include native code
* Writing native code

Using libraries that include native code
----------------------------------------

Expo and React Native developers typically spend the vast majority of their time writing JavaScript code and using native APIs and components that are made available through libraries like `expo-camera`, `react-native-safe-area-context`, and `react-native` itself. These libraries allow developers to access and use device features (such as Camera) from their JavaScript code. They may also provide access to a third-party service SDK that is implemented in native code (such as `@sentry/react-native`, which provides bindings to the Sentry native SDK for Android and iOS).

If you are using the sandbox app, Expo Go, you can only access native libraries that are included in the Expo SDK, or libraries that do not include any custom native code. In contrast, by [creating a development build](/develop/development-builds/introduction), you can control any part of your app. You can change the native code or configuration that is possible in any other native app. For more details on how to determine if a third-party library depends on custom code, see [Using third party libraries](/workflow/using-libraries#third-party-libraries).

### Installing libraries with custom native code in development builds

When using [development builds](/develop/development-builds/introduction), using libraries with custom native code is straightforward:

* Install the library with npm, for example: `npx expo install react-native-localize`
* If the library includes a [config plugin](/config-plugins/introduction), you can specify your preferred configuration in your app config.
* Create a new development build (either [locally](/guides/local-app-development) or with [EAS](/develop/development-builds/create-a-build)).

You can now use the library in your application code.

Key concepts and development workflow

[The development overview](/workflow/overview) provides details on key concepts for developing an app with Expo and the flow of the core development loop.

Writing native code
-------------------

It's common to encounter situations where a library doesn't help you get your job done. For example, the library might not provide access to a specific platform feature, or a third-party library might not provide bindings for React Native. To solve this, you can write Kotlin (or Java) and/or Swift (or Objective-C) code to add any native functionality to your app directly, or to provide bindings to your JavaScript code. There are different tools you can use for this in React Native, and we typically recommend using the Expo Modules API. If you intend to write C++ code, you may want to explore the [Turbo Modules API](https://github.com/reactwg/react-native-new-architecture/blob/main/docs/turbo-modules.md) provided by React Native.

### Using the Expo Modules API

The Expo Modules API allows you to write Swift and Kotlin to add new capabilities to your app with native modules and views. We believe that using the Expo Modules API makes building and maintaining nearly all kinds of React Native modules about as easy as it can be. We think that the Expo Modules API is the best choice for most developers building native modules for their apps.

[Expo Modules API: Overview

An overview of the APIs and utilities provided by Expo to develop native modules.](/modules/overview)
[Tutorial: Creating a native module

A tutorial on creating a native module that persists settings with the Expo Modules API.](/modules/native-module-tutorial)
[Tutorial: Creating a native view

A tutorial on creating a native view that renders a native WebView component with the Expo Modules API.](/modules/native-view-tutorial)

### Creating a local module

If you intend to use your native module in a single app (you can always change your mind later), we recommend [using a "local" Expo module](/modules/get-started#creating-the-local-expo-module) to write custom native code. Local Expo Modules function similarly to [Expo Modules](/modules/overview) used by library developers and within the Expo SDK, like `expo-camera`, but they are not published on npm. Instead, you create them directly inside your project.

Creating a local module scaffolds a Swift and Kotlin module inside the `modules` directory in your project, and these modules are automatically linked to your app.

Terminal

`-Â``npx create-expo-module@latest --local`

`-Â``npx expo run`

### Sharing a module with multiple apps

If you intend to use your native module with multiple apps, then use `npx create-expo-module@latest,` leave out the `--local` flag, and [create a standalone module](/modules/use-standalone-expo-module-in-your-project). You can publish your package to npm, or you can put it in a packages directory in your [monorepo](/guides/monorepos) (if you have one) to use it in [a similar way to local modules](/modules/use-standalone-expo-module-in-your-project).

Considerations when using Continuous Native Generation (CNG)
------------------------------------------------------------

The following suggestions are most important when using CNG, but are good guidelines even if you don't use it.

### Build locally for the best debugging experience and fast feedback

By default, Expo projects created with `create-expo-app` use CNG and do not contain android or ios native directories until you've run the `npx expo prebuild` command in your project. When using CNG, developers typically do not commit the android and ios directories to source control and do not generate them locally, since EAS Build will do it automatically during the build process. That said, it is common to generate native directories and build locally with `npx expo run` when writing custom native code, to have a fast feedback loop and full access to native debugging tools in Android Studio / Xcode.

### Use config plugins for native project configuration

If your native code requires that you make changes to your project configuration, such as modifying the project's AndroidManifest.xml or Info.plist, [you should apply these changes through a config plugin](/modules/config-plugin-and-native-module-tutorial) rather than by modifying the files directly in the android and ios directories. Remember that changes made directly to native project directories will be lost the next time you run prebuild when you use CNG.

### Use event subscribers to hook into app lifecycle events

Additionally, if you need to hook into Android lifecycle events or `AppDelegate` methods, use the APIs provided by Expo Modules for [Android](/modules/android-lifecycle-listeners) and [iOS](/modules/appdelegate-subscribers) to accomplish this rather than modifying the source files in your native project directories directly or using a config plugin to add the code, which does not compose well with other plugins.

[Previous (Development process - Linking)

iOS Universal Links](/linking/ios-universal-links)[Next (Development process - Write native code)

Adopt Prebuild](/guides/adopting-prebuild)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/workflow/customizing.mdx)
* Last updated on April 24, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Using libraries that include native code](/workflow/customizing/#using-libraries-that-include-native-code)[Installing libraries with custom native code in development builds](/workflow/customizing/#installing-libraries-with-custom-native-code-in-development-builds)[Writing native code](/workflow/customizing/#writing-native-code)[Using the Expo Modules API](/workflow/customizing/#using-the-expo-modules-api)[Creating a local module](/workflow/customizing/#creating-a-local-module)[Sharing a module with multiple apps](/workflow/customizing/#sharing-a-module-with-multiple-apps)[Considerations when using Continuous Native Generation (CNG)](/workflow/customizing/#considerations-when-using-continuous-native-generation-cng)[Build locally for the best debugging experience and fast feedback](/workflow/customizing/#build-locally-for-the-best-debugging-experience-and-fast-feedback)[Use config plugins for native project configuration](/workflow/customizing/#use-config-plugins-for-native-project-configuration)[Use event subscribers to hook into app lifecycle events](/workflow/customizing/#use-event-subscribers-to-hook-into-app-lifecycle-events)