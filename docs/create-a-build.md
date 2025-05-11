Create a development build - Expo Documentation

[Docs](/)

[Blog](https://expo.dev/blog)[Changelog](https://expo.dev/changelog)[Star Us on GitHub](https://github.com/expo/expo)

Search

[Home](/)[Guides](/guides/overview)[EAS](/eas)[Reference](/versions/latest)[Learn](/tutorial/overview)

Get started

[Introduction](/get-started/introduction)[Create a project](/get-started/create-a-project)[Set up your environment](/get-started/set-up-your-environment)[Start developing](/get-started/start-developing)[Next steps](/get-started/next-steps)

Develop

[Tools for development](/develop/tools)

Navigation

User interface

Development builds

[Introduction](/develop/development-builds/introduction)[Create a build](/develop/development-builds/create-a-build)[Use a build](/develop/development-builds/use-development-builds)[Share with your team](/develop/development-builds/share-with-your-team)[Tools, workflows and extensions](/develop/development-builds/development-workflows)[Next steps](/develop/development-builds/next-steps)

Config plugins

Debugging

[Authentication](/develop/authentication)[Unit testing](/develop/unit-testing)

Review

[Distributing apps for review](/review/overview)[Share previews with your team](/review/share-previews-with-your-team)[Open updates with Orbit](/review/with-orbit)

Deploy

[Build project for app stores](/deploy/build-project)[Submit to app stores](/deploy/submit-to-app-stores)[App stores metadata](/deploy/app-stores-metadata)[Send over-the-air updates](/deploy/send-over-the-air-updates)[Deploy web apps](/deploy/web)

Monitor

[Monitoring services](/monitoring/services)

More

[Core concepts](/core-concepts)[FAQ](/faq)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Create a development build
==========================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/development-builds/create-a-build.mdx)

Learn how to create development builds for a project.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/development-builds/create-a-build.mdx)

---

When you create a new Expo app with `npx create-expo-app`, you start off with a project where you update the JavaScript code on your local machine and view the changes in the Expo Go app. A development build is essentially your own version of Expo Go where you are free to use any native libraries and change any native config. In this guide, you will learn how to convert your project that runs on Expo Go into a development build, which will make the native side of your app fully customizable.

[![How to create a development build](https://i3.ytimg.com/vi/uQCE9zl3dXU/maxresdefault.jpg)

How to create a development build](https://www.youtube.com/watch?v=uQCE9zl3dXU)

Prerequisites
-------------

The instructions assume you already have an existing Expo project that runs on Expo Go.

The requirements for building the native app depend on which platform you are using, which platform you are building for, and whether you want to build on EAS or on your local machine.

Build on EAS

This is the easiest way to build your native app, as it requires no native build tools on your side. The builds happen on the EAS servers, which makes it possible to trigger iOS builds from non-macOS platforms.

|  | Android | iOS Simulator | iPhone device |
| --- | --- | --- | --- |
| macOS |  |  | (\*) |
| Windows |  |  | (\*) |
| Linux |  |  | (\*) |

(\*) All builds that run on an iPhone device require a paid [Apple Developer](/develop/development-builds/developer.apple.com) account for build signing.

Build locally using the EAS CLI

Any EAS CLI command can be built on your local machine with the `--local` flag. This requires your local [development environment](https://reactnative.dev/docs/set-up-your-environment?os=macos&platform=ios) to be set up with native build tools. Read more about [local app development](/build-reference/local-builds).

|  | Android | iOS Simulator | iPhone device |
| --- | --- | --- | --- |
| macOS |  |  | (\*) |
| Windows | (\*\*) |  |  |
| Linux |  |  |  |

(\*) All builds that run on an iPhone device require a paid [Apple Developer](/develop/development-builds/developer.apple.com) account for build signing.

(\*\*) No first-class support, but possible with [WSL](http://expo.fyi/wsl.md).

Build locally without EAS

To build locally without EAS requires your local [development environment](https://reactnative.dev/docs/set-up-your-environment?os=macos&platform=ios) to be set up with native build tools. This is the only way to test your iOS build on an iPhone device without a paid Apple Developer Account (only possible on macOS). Read more about [local app compilation](/guides/local-app-development#local-app-compilation).

|  | Android | iOS Simulator | iPhone device |
| --- | --- | --- | --- |
| macOS |  |  |  |
| Windows |  |  |  |
| Linux |  |  |  |

Get started
-----------

For detailed, step-by-step instructions, see our [EAS Tutorial](/tutorial/eas/introduction). Available also as a [tutorial series](https://www.youtube.com/playlist?list=PLsXDmrmFV_AS14tZCBin6m9NIS_VCUKe2) on YouTube.

1

### Install expo-dev-client

Terminal

Copy

`-Â``npx expo install expo-dev-client`

Are you using this library in a existing (bare) React Native apps?

Apps that don't use [Continuous Native Generation](/workflow/continuous-native-generation) or are created with `npx react-native`, require further configuration after installing this library. See steps 1 and 2 from [Install `expo-dev-client` in an existing React Native app](/bare/install-dev-builds-in-bare).

2

### Build the native app (Android)

Build on EAS

On your local machine

Prerequisites

3 requirements

1.

Expo account

Sign up for an [Expo](https://expo.dev/signup) account, if you haven't already.

2.

EAS CLI

The [EAS CLI](/build/setup#install-the-latest-eas-cli) installed and logged in.

Terminal

Copy

`-Â``npm install -g eas-cli && eas login`

3.

An Android Emulator (optional)

An [Android Emulator](/workflow/android-studio-emulator) is optional if you want to test your
app on an emulator.

Terminal

Copy

`-Â``eas build --platform android --profile development`

Read more about [Android builds on EAS](/tutorial/eas/android-development-build).

Prerequisites

2 requirements

1.

Development environment set up

A macOS, Windows, or Linux machine with your local [development
environment](https://reactnative.dev/docs/set-up-your-environment?os=windows&platform=android)
set up.

2.

An Android Emulator (optional)

An [Android Emulator](/workflow/android-studio-emulator) is optional if you want to test your
app on an emulator.

Terminal

Copy

`-Â``npx expo run:android`

The same `apk` can be installed on Android devices as well as emulators.

Read more about [local app development](/guides/local-app-development#local-builds-with-expo-dev-client).

2

### Build the native app (iOS Simulator)

Build on EAS

On your local machine

Prerequisites

3 requirements

1.

Expo account

Sign up for an [Expo](https://expo.dev/signup) account, if you haven't already.

2.

EAS CLI

The [EAS CLI](/build/setup#install-the-latest-eas-cli) installed and logged in.

Terminal

Copy

`-Â``npm install -g eas-cli && eas login`

3.

macOS with iOS Simulator installed

iOS Simulators are available only on macOS. Make sure you have the [iOS
Simulator](/workflow/ios-simulator) installed.

Edit `development` profile in eas.json and set the [`simulator`](/eas/json#simulator) option to `true` (you have to create a separate profile for simulator builds if you also want to create iOS device builds for this project).

eas.json

Copy

```
{
  "build": {
    "development": {
      "ios": {
        "simulator": true
      }
    }
  }
}

```

Terminal

Copy

`-Â``eas build --platform ios --profile development`

iOS Simulator builds can only be installed on simulators and not on real devices.

Read more about [iOS Simulator builds on EAS](/tutorial/eas/ios-development-build-for-simulators).

Prerequisites

2 requirements

1.

macOS

iOS Simulators are available only on macOS.

2.

Development environment set up

Set up your local [development
environment](https://reactnative.dev/docs/set-up-your-environment?os=macos&platform=ios).

Terminal

Copy

`-Â``npx expo run:ios`

Read more about [local app development](/guides/local-app-development#local-builds-with-expo-dev-client).

2

### Build the native app (iOS device)

Build on EAS

On your local machine

Prerequisites

3 requirements

1.

Expo account

Sign up for an [Expo](https://expo.dev/signup) account, if you haven't already.

2.

EAS CLI

The [EAS CLI](/build/setup#install-the-latest-eas-cli) installed and logged in.

Terminal

Copy

`-Â``npm install -g eas-cli && eas login`

3.

Apple Developer account

A paid [Apple Developer](https://developer.apple.com/) account for creating [signing
credentials](/app-signing/managed-credentials#generating-app-signing-credentials) so the app
could be installed on an iOS device.

Terminal

Copy

`-Â``eas build --platform ios --profile development`

iOS device builds can only be installed on iPhone devices and not on iOS Simulators.

Read more about [iOS device builds on EAS](/tutorial/eas/ios-development-build-for-devices).

Prerequisites

2 requirements

1.

macOS

macOS is required to compile the native app for iOS devices.

2.

Development environment set up

Set up your local [development
environment](https://reactnative.dev/docs/set-up-your-environment?os=macos&platform=ios).

Terminal

Copy

`-Â``npx expo run:ios --device`

Read more about [local app development](/guides/local-app-development#local-builds-with-expo-dev-client).

3

### Install the app

You'll need to install the native app on your device, emulator, or simulator.

#### When building on EAS

If you create your development build on EAS, the CLI will prompt you to install the app after the build is finished. You can also install previous builds from the [expo.dev](https://expo.dev/) dashboard or using [Expo Orbit](https://expo.dev/orbit).

#### When building locally using EAS CLI

When building locally the output of the build will be an archive. You may drag and drop this on your Android Emulator/iOS Simulator to install it, or use [Expo Orbit](https://expo.dev/orbit) to install a build from your local machine.

#### When building locally without EAS CLI

Local builds will get installed automatically once the build finishes.

4

### Start the bundler

The development client built in step 2 is the native side of your app (basically your own version of Expo Go). To continue developing, you'll also want to start the JavaScript bundler.

Depending on how you built the app, this may already be running, but if you close the process for any reason, there is no need to rebuild your development client. Simply restart the JavaScript bundler with:

Terminal

Copy

`-Â``npx expo start`

This is the same command you would have used with Expo Go. It detects whether your project has `expo-dev-client` installed, in which case it will default to targeting your development build instead of Expo Go.

Video walkthroughs
------------------

["EAS Tutorial Series"

A course on YouTube: learn how to speed up your development with Expo Application Services.](https://www.youtube.com/playlist?list=PLsXDmrmFV_AS14tZCBin6m9NIS_VCUKe2)
["Async Office Hours: How to make a development build with EAS Build"

Learn how to make a development build with EAS Build in this video tutorial hosted by Developer Success Engineer: Keith Kurak.](https://www.youtube.com/watch?v=LUFHXsBcW6w)

[Previous (Develop - Development builds)

Introduction](/develop/development-builds/introduction)[Next (Develop - Development builds)

Use a build](/develop/development-builds/use-development-builds)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/development-builds/create-a-build.mdx)
* Last updated on April 28, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Prerequisites](/develop/development-builds/create-a-build/#prerequisites)[Get started](/develop/development-builds/create-a-build/#get-started)[Install expo-dev-client](/develop/development-builds/create-a-build/#install-expo-dev-client)[Build the native app (Android)](/develop/development-builds/create-a-build/#build-the-native-app-android)[Build the native app (iOS Simulator)](/develop/development-builds/create-a-build/#build-the-native-app-ios-simulator)[Build the native app (iOS device)](/develop/development-builds/create-a-build/#build-the-native-app-ios-device)[Install the app](/develop/development-builds/create-a-build/#install-the-app)[Start the bundler](/develop/development-builds/create-a-build/#start-the-bundler)[Video walkthroughs](/develop/development-builds/create-a-build/#video-walkthroughs)