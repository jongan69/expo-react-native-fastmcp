Local app development - Expo Documentation

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

[Development](/guides/local-app-development)[Production](/guides/local-app-production)[Cache builds remotely](/guides/cache-builds-remotely)

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

Local app development
=====================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/local-app-development.mdx)

Learn how to compile and build your Expo app locally.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/local-app-development.mdx)

---

To build your project into an app locally using your machine, you have to manually generate native code before testing the debug build or creating a production build for it to submit to the app store. There are two ways you can build your app locally. This guide provides a brief introduction to both methods and references to other guides that are necessary to create this workflow.

Prerequisites
-------------

You need to install and set up Android Studio and Xcode to compile and run Android and iOS projects on your local machine. See the following on how to set up these tools:

* [Android Studio](/get-started/set-up-your-environment?platform=android&device=physical&mode=development-build&buildEnv=local#set-up-an-android-device-with-a-development-build)
* [Xcode](/get-started/set-up-your-environment?platform=ios&device=physical&mode=development-build&buildEnv=local#set-up-an-ios-device-with-a-development-build)

Local app compilation
---------------------

To build your project locally you can use compile commands from Expo CLI which generates the android and ios directories:

Terminal

`# Build native Android project`

`-Â``npx expo run:android`

`# Build native iOS project`

`-Â``npx expo run:ios`

The above commands compile your project, using your locally installed Android SDK or Xcode, into a debug build of your app.

* These compilation commands initially run `npx expo prebuild` to generate native directories (android and ios) before building, if they do not exist yet. If they already exist, this will be skipped.
* You can also add the `--device` flag to select a device to run the app on â you can select a physically connected device or emulator/simulator.
* You can pass in `--variant release` (Android) or `--configuration Release` (iOS) to build a [production build of your app](/deploy/build-project#production-builds-locally). Note that these builds are not signed and you cannot submit them to app stores. To sign your production build, see [Local app production](/guides/local-app-production).

To modify your project's configuration or native code after the first build, you will have to rebuild your project. Running `npx expo prebuild` again layers the changes on top of existing files. It may also produce different results after the build.

To avoid this, add native directories to the project's .gitignore and use `npx expo prebuild --clean` command. This ensures that the project is always managed, and the [`--clean` flag](/workflow/prebuild#clean) will delete existing directories before regenerating them. You can use [app config](/workflow/configuration) or create a [config plugin](/config-plugins/introduction) to modify your project's configuration or code inside the native directories.

To learn more about how compilation and prebuild works, see the following guides:

[Compiling with Expo CLI

Learn how Expo CLI uses `run` commands to compile your app locally, arguments you can pass to the CLI and more.](/more/expo-cli#compiling)
[Prebuild

Learn how Expo CLI generates native code of your project before compiling it.](/workflow/prebuild)

Local builds with `expo-dev-client`
-----------------------------------

If you install [`expo-dev-client`](/develop/development-builds/introduction#what-is-expo-dev-client) to your project, then a debug build of your project will include the `expo-dev-client` UI and tooling, and we call these development builds.

Terminal

Copy

`-Â``npx expo install expo-dev-client`

To create a development build, you can use [local app compilation](/guides/local-app-development#local-app-compilation) commands (`npx expo run:[android|ios]`) which will create a debug build and start the development server.

Local builds using Android product flavors
------------------------------------------

> This feature is only available for SDK 52 and above.

If you have a custom Android project with multiple product flavors using different application IDs, you can configure `npx expo run:android` to use the correct flavor and build type. Expo supports both `--variant` and `--app-id` to customize the build and launch behavior.

The `--variant` flag can switch the Android build type from debug to release. This flag can also configure a product flavor and build type, when formatted in camelCase. For example, if you have both [free and paid product flavors](https://developer.android.com/build/build-variants#change-app-id), you can build a development version of your app with:

Terminal

`-Â``npx expo run:android --variant freeDebug`

  

`-Â``npx expo run:android --variant paidDebug`

The `--app-id` flag can be used to launch the app after building using a customized application id. For example, if your product flavor free is using `applicationIdSuffix ".free"` or `applicationId "dev.expo.myapp.free"` you can run build and launch the app with:

Terminal

Copy

`-Â``npx expo run:android --variant freeDebug --app-id dev.expo.myapp.free`

> Customizing the Android build type is also possible, but that would break Expo's assumption that the build type release is used for production. You might build unoptimized code in your app using a different build type instead of release.

Local builds with EAS
---------------------

[Run builds on your infrastructure

Learn how to run EAS Build on your custom infrastructure or locally on your machine with the `--local` flag.](/build-reference/local-builds)

[Previous (Development process - Write native code)

Adopt Prebuild](/guides/adopting-prebuild)[Next (Development process - Compile locally)

Production](/guides/local-app-production)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/local-app-development.mdx)
* Last updated on October 07, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Prerequisites](/guides/local-app-development/#prerequisites)[Local app compilation](/guides/local-app-development/#local-app-compilation)[Local builds with expo-dev-client](/guides/local-app-development/#local-builds-with-expo-dev-client)[Local builds using Android product flavors](/guides/local-app-development/#local-builds-using-android-product-flavors)[Local builds with EAS](/guides/local-app-development/#local-builds-with-eas)