React Native's New Architecture - Expo Documentation

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

React Native's New Architecture
===============================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/new-architecture.mdx)

Learn about React Native's "New Architecture" and how and why to migrate to it.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/new-architecture.mdx)

---

> We recommend using the latest Expo version for the best experience with the New Architecture.

The New Architecture is a name that we use to describe a complete refactoring of the internals of React Native. It is also used to solve limitations of the original React Native architecture discovered over years of usage in production at Meta and other companies.

In this guide, we'll talk about how to use the New Architecture in Expo projects today.

[New Architecture is here

A blog post from the React Native team at Meta that gives an overview of the features of the New Architecture and the motivations behind building it.](https://reactnative.dev/blog/2024/10/23/the-new-architecture-is-here)
Why migrate to the New Architecture?

The New Architecture is the future of React Native â yet, for many apps, there may not be many immediate benefits to migrating today. You may want to think of migrating to the New Architecture as an investment in the future of your app, rather than as a way to immediately improve your app.

That said, new React and React Native features are coming to the New Architecture only. For example, the New Architecture includes [full support for Suspense](https://reactnative.dev/blog/2024/10/23/the-new-architecture-is-here#full-support-for-suspense) and [new styling capabilities](https://reactnative.dev/blog/2025/01/21/version-0.77#new-css-features-for-better-layouts-sizing-and-blending) are not implemented in the legacy architecture. Libraries such as [@shopify/flash-list](https://github.com/Shopify/flash-list) and [react-native-reanimated](https://github.com/software-mansion/react-native-reanimated) will be shipping new major versions that take full advantage of new features to deliver better performance than was possible before, and will drop support for the legacy architecture.

The legacy architecture will not be around forever â it's possible that the legacy architecture will be removed from React Native in a late 2025 release. When it is removed, you will not be able to upgrade React Native or the Expo SDK without migrating to the New Architecture.

Expo tools and the New Architecture
-----------------------------------

As of SDK 53, all `expo-*` packages in the [Expo SDK](/versions/latest) support the New Architecture (including [bridgeless](https://github.com/reactwg/react-native-new-architecture/discussions/154)). [Learn more about known issues](/guides/new-architecture#known-issues-in-expo-sdk-libraries).

Additionally, all modules written using the [Expo Modules API](/modules/overview) support the New Architecture by default! So if you have built your own native modules using this API, no additional work is needed to use them with the New Architecture.

As of April 2025, approximately 75% of SDK 52+ projects built with [EAS Build](/build/introduction) use the New Architecture.

Third-party libraries and the New Architecture
----------------------------------------------

The compatibility status of many of the most popular libraries is tracked on [React Native Directory](https://reactnative.directory/) ([learn more about known issues in third-party libraries](/guides/new-architecture#known-issues-in-third-party-libraries)). We've built tooling into Expo Doctor to integrate with React Native Directory to help you validate your dependencies, so you can quickly learn which libraries are unmaintained and which incompatible or untested with the New Architecture.

### Validate your dependencies with React Native Directory

Run `npx expo-doctor` to check your dependencies against the data in React Native Directory.

Terminal

Copy

`-Â``npx expo-doctor@latest`

You can configure the React Native Directory check in your package.json file. For example, if you would like to exclude a package from validation:

package.json

Copy

```
{
  "expo": {
    "doctor": {
      "reactNativeDirectoryCheck": {
        "exclude": ["react-redux"]
      }
    }
  }
}

```

See all available options

* enabled: If `true`, the check will warn if any packages are missing from React Native Directory. Set this to `false` to disable this behavior. On SDK 52 and above, this is set to `true` by default, otherwise it is `false` by default. You can also override this setting with the `EXPO_DOCTOR_ENABLE_DIRECTORY_CHECK` environment variable (0 is `false`, 1 is `true`).
* exclude: List any packages you want to exclude from the check. Supports exact package names and regex patterns. For example, `["exact-package", "/or-a-regex-.*/"]`.
* listUnknownPackages: By default, the check will warn if any packages are missing from React Native Directory. Set this to false to disable this behavior.

Initialize a new project with the New Architecture
--------------------------------------------------

As of SDK 52, all new projects will be initialized with the New Architecture enabled by default.

Terminal

Copy

`-Â``npx create-expo-app@latest`

Enable the New Architecture in an existing project
--------------------------------------------------

SDK 53 and above

SDK 52

SDK 51 and below

The New Architecture is enabled by default in SDK 53 and above. If you have explicitly disabled it, remove that configuration to enable it.

We recommend upgrading to SDK 53 to ensure that your app can take advantage of all of the latest New Architecture related fixes and improvements with libraries and React Native itself. If you want to try it on SDK 52 first, follow the instructions below.

1

To enable it on both Android and iOS, use the `newArchEnabled` at the root of the `expo` object in your app config. You can selectively enable it for a single platform by setting, for example, `"android": { "newArchEnabled": true }`.

app.json

Copy

```
{
  "expo": {
    "newArchEnabled": true
  }
}

```

2

Create a new build:

Android

iOS

Terminal

`# Run a clean prebuild and start a local build, if you like`

`-Â``npx expo prebuild --clean && npx expo run:android`

`# Run a build with EAS if you prefer`

`-Â``eas build -p android`

Terminal

`# Run a clean prebuild and start a local build, if you like`

`-Â``npx expo prebuild --clean && npx expo run:ios`

`# Run a build with EAS if you prefer`

`-Â``eas build -p ios`

If the build succeeds, you will now be running your app with the New Architecture! Depending on the native modules you use, your app may work properly immediately.

Now you can tap around your app and test it out. For most non-trivial apps, you're likely to encounter some issues, such as missing native views that haven't been implemented for the New Architecture yet. Many of the issues you encounter are actionable and can be resolved with some configuration or code changes. We recommend reading [Troubleshooting](/guides/new-architecture#troubleshooting) sections below for more information.

We recommend upgrading to at least SDK 52, preferably SDK 53. It's possible to enable the New Architecture in SDK 51, but you are likely to encounter a variety of issues that have been resolved in more recent releases. To enable it, you need to [install the `expo-build-properties` plugin](/versions/latest/sdk/build-properties#installation) and set `newArchEnabled` on target platforms.

Are you enabling the New Architecture in a bare React Native app?

If you are using Expo SDK 53 or higher, it will be enabled by default. The following instructions apply to older projects.

* Android: Set `newArchEnabled=true` in the gradle.properties file.
* iOS: If your project has a Podfile.properties.json file (which is created by `npx create-expo-app` or `npx expo prebuild`), you can enable the New Architecture by setting the `newArchEnabled` property to `"true"` in the Podfile.properties.json file. Otherwise, refer to the ["Enable the New Architecture for Apps"](https://github.com/reactwg/react-native-new-architecture/blob/main/docs/enable-apps.md) section of the React Native New Architecture working group.

Disable the New Architecture in an existing project
---------------------------------------------------

> : Expo Go only supports the New Architecture.

If you want to opt out of using the New Architecture, set the `newArchEnabled` property to `false` in app config and create a [development build](/develop/development-builds/introduction).

app.json

Copy

```
{
  "expo": {
    "newArchEnabled": false
  }
}

```

Are you disabling the New Architecture in a bare React Native app?

* Android: Set `newArchEnabled=false` in the gradle.properties file.
* iOS: If your project has a Podfile.properties.json file (which is created by `npx create-expo-app` or `npx expo prebuild`), you can enable the New Architecture by setting the `newArchEnabled` property to `"false"` in the Podfile.properties.json file. Otherwise, refer to the ["Enable the New Architecture for Apps"](https://github.com/reactwg/react-native-new-architecture/blob/main/docs/enable-apps.md) section of the React Native New Architecture working group.

Troubleshooting
---------------

Meta and Expo are working towards making the New Architecture the default for all new apps and ensuring it is as easy as possible to migrate existing apps. However, the New Architecture isn't just a name â many of the internals of React Native has been re-architected and rebuilt from the ground up. As a result, you may encounter issues when enabling the New Architecture in your app. The following is some advice for troubleshooting these issues.

Can I still try the New Architecture even if some of the libraries I use aren't supported?

You may be able to try the New Architecture in your app even if some of the libraries you use aren't supported, but it will require temporarily removing those libraries. Create a new branch in your repository and remove any of the libraries that aren't compatible until your app is running. This will give you a good idea of what libraries still need work before you can fully migrate to the New Architecture. We recommend creating issues or pull requests on those libraries' repositories to help them become compatible with the New Architecture. Alternatively, you could switch to other libraries that are compatible with the New Architecture. Refer to [React Native Directory](https://reactnative.directory/) to find compatible libraries.

Known issues in React Native

Refer to the [issues labeled with "Type: New Architecture" on the React Native GitHub repository](https://github.com/facebook/react-native/issues?q=is%3Aopen+is%3Aissue+label%3A%22Type%3A+New+Architecture%22).

Known issues in Expo libraries

There are no known issues specific to the New Architecture in Expo libraries.

Known issues in third-party libraries

Since React Native 0.74, there are various Interop Layers enabled by default. This allows many libraries built for the old architecture to work on the New Architecture without any changes. However, the interop is not perfect and some libraries will need to be updated. The libraries that are most likely to require updates are those that ship or depend on third-party native code. [Learn more about library support in the New Architecture](https://github.com/reactwg/react-native-new-architecture/discussions/167).

Refer to [React Native Directory](https://reactnative.directory/) a more complete list of libraries and their compatibility with the New Architecture. The following libraries were found to be popular among Expo apps and are known to be incompatible:

The following are known issues with libraries that are popular among Expo apps.

* react-native-maps: Version 1.20.x, which is the default for SDK 53, supports the New Architecture with the interop layer and works well for most features. A New Architecture-first version is available in version 1.21.0, which is still stabilizing. We encourage your to test it in your app, report issues that you find, and [follow along with the discussion on GitHub](https://github.com/react-native-maps/react-native-maps/discussions/5355). We are also investigating another approach that may provider a smoother migration path, by leaning on the [interop layer](https://github.com/reactwg/react-native-new-architecture/discussions/175) rather than rewriting the module. It's worth mentioning that if your app can force a minimum version of iOS 17, or does not need to support maps on iOS, then you can consider using [`expo-maps`](/versions/latest/sdk/maps) instead.
* @stripe/react-native: The New Architecture is supported starting with version 0.45.0, which is the default for SDK 53.
* @react-native-community/masked-view: Use `@react-native-masked-view/masked-view` instead.
* @react-native-community/clipboard: Use `@react-native-clipboard/clipboard` instead.
* rn-fetch-blob: Use `react-native-blob-util` instead.
* react-native-fs: Use `expo-file-system` or [a fork of react-native-fs](https://github.com/birdofpreyru/react-native-fs) instead.
* react-native-geolocation-service: Use `expo-location` instead.
* react-native-datepicker: Use `react-native-date-picker` or `@react-native-community/datetimepicker` instead.

My build failed after enabling the New Architecture

This isn't entirely surprising! Not all libraries are compatible yet, and in some cases compatibility was only recently added and so you will want to ensure you update your libraries to their latest versions. Read the logs to determine which library is incompatible. Also, run `npx expo-doctor@latest` to check your dependencies against the data in React Native Directory.

When you are using the latest version of a library and it is not compatible, report any issues you encounter to the respective GitHub repository. Create a [minimal reproducible example](https://stackoverflow.com/help/minimal-reproducible-example) and report the issue to the library author. If you believe the issue originates in React Native itself, rather than a library, report it to the React Native team (again, with a minimal reproducible example).

[Previous (Development process - Reference)

iOS Simulator](/workflow/ios-simulator)[Next (Development process - Reference)

React Compiler](/guides/react-compiler)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/new-architecture.mdx)
* Last updated on April 30, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Expo tools and the New Architecture](/guides/new-architecture/#expo-tools-and-the-new-architecture)[Third-party libraries and the New Architecture](/guides/new-architecture/#third-party-libraries-and-the-new-architecture)[Validate your dependencies with React Native Directory](/guides/new-architecture/#validate-your-dependencies-with-react-native-directory)[Initialize a new project with the New Architecture](/guides/new-architecture/#initialize-a-new-project-with-the-new-architecture)[Enable the New Architecture in an existing project](/guides/new-architecture/#enable-the-new-architecture-in-an-existing-project)[Disable the New Architecture in an existing project](/guides/new-architecture/#disable-the-new-architecture-in-an-existing-project)[Troubleshooting](/guides/new-architecture/#troubleshooting)