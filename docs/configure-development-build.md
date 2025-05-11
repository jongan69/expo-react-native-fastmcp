Configure a development build in cloud - Expo Documentation

[Docs](/)

[Blog](https://expo.dev/blog)[Changelog](https://expo.dev/changelog)[Star Us on GitHub](https://github.com/expo/expo)

Search

[Home](/)[Guides](/guides/overview)[EAS](/eas)[Reference](/versions/latest)[Learn](/tutorial/overview)

[Overview](/tutorial/overview)

Expo tutorial

0 of 9

[Introduction](/tutorial/introduction)[Create your first app](/tutorial/create-your-first-app)[Add navigation](/tutorial/add-navigation)[Build a screen](/tutorial/build-a-screen)[Use an image picker](/tutorial/image-picker)[Create a modal](/tutorial/create-a-modal)[Add gestures](/tutorial/gestures)[Take a screenshot](/tutorial/screenshot)[Handle platform differences](/tutorial/platform-differences)[Configure status bar, splash screen and app icon](/tutorial/configuration)[Learning resources](/tutorial/follow-up)

EAS tutorial

0 of 11

[Introduction](/tutorial/eas/introduction)[Configure development build](/tutorial/eas/configure-development-build)[Android development build](/tutorial/eas/android-development-build)[iOS development build for simulators](/tutorial/eas/ios-development-build-for-simulators)[iOS development build for devices](/tutorial/eas/ios-development-build-for-devices)[Multiple app variants](/tutorial/eas/multiple-app-variants)[Internal distribution build](/tutorial/eas/internal-distribution-builds)[Manage app versions](/tutorial/eas/manage-app-versions)[Android production build](/tutorial/eas/android-production-build)[iOS production build](/tutorial/eas/ios-production-build)[Share previews](/tutorial/eas/team-development)[Builds from GitHub](/tutorial/eas/using-github)[Next steps](/tutorial/eas/next-steps)

More

[Additional resources](/additional-resources)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Configure a development build in cloud
======================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/tutorial/eas/configure-development-build.mdx)

Learn how to configure a development build for a project using EAS Build.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/tutorial/eas/configure-development-build.mdx)

---

In this chapter, we'll set up and configure a development build with EAS for our example app.

[![Watch: How to configure a development build](https://i3.ytimg.com/vi/uQCE9zl3dXU/maxresdefault.jpg)

Watch: How to configure a development build](https://www.youtube.com/watch?v=uQCE9zl3dXU)


---

Understanding development builds
--------------------------------

Let's start by learning about what are development builds and why we need them.

A [development build](/develop/development-builds/introduction) is a debug version of our project. It is optimized for quick iterations when creating an app. It contains the [`expo-dev-client`](/versions/latest/sdk/dev-client) library, which offers a robust and complete development environment. This setup allows us to integrate any native library or change code inside the [native directories](/workflow/overview#android-and-ios-native-projects) as required.

### Key highlights

> Note: If you are familiar with [Expo Go](/get-started/expo-go), think of a development build as a customizable version of Expo Go that is unique to the requirements of a project.

| Feature | Development Builds | Expo Go |
| --- | --- | --- |
| Development phase | Offers web-like iteration speed for mobile app development. | Allows for quick iteration and testing of Expo SDK projects using the client app. |
| Collaboration | Facilitates team testing with shared native runtime. | Easy project sharing via QR codes on a device. |
| Third-party libraries support | Full support for any [third-party library](/workflow/using-libraries#third-party-libraries), including those that require custom native code. | Limited to libraries within the Expo SDK, not suitable for custom native dependencies. |
| Customization | Extensive customization with [config plugins](/config-plugins/introduction) and direct access to native code. | Limited customization with a focus on Expo SDK capabilities without direct native code modification. |
| Intended use | Ideal for full-fledged app development aimed at store deployment, offering a complete development environment and tools. | Ideal for learning, prototyping, and experimenting. Not recommended for production apps. |

1

Install expo-dev-client library
-------------------------------

To initialize our project for a development build, let's [`cd`](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Understanding_client-side_tools/Command_line#basic_built-in_terminal_commands) inside our project directory and run the following command to install the library:

Terminal

Copy

`-Â``npx expo install expo-dev-client`

### Start the development server

Run the `npx expo start` to start the [development server](/get-started/start-developing#start-a-development-server):

Terminal

Copy

`-Â``npx expo start`

This command starts the metro bundler. In the terminal window, we see the QR code followed by the `Metro waiting on...` and a manifest URL:

![Running development server](/static/images/tutorial/eas/development-server.png)

Let's notice the changes installing the `expo-dev-client` library:

* The manifest URL contains `expo-development-client` along with the app scheme
* The development server now operates for a development build (instead of Expo Go).

Since we do not have a development build installed on one of our devices or an emulator/simulator, we can't run our project yet.

2

Initialize a development build
------------------------------

### Install EAS CLI

We need to install the EAS Command Line Interface (CLI) tool as a global dependency on our local machine. Run the following command:

Terminal

Copy

`-Â``npm install -g eas-cli`

### Log in or sign up for an Expo account

> If you have an Expo account and are signed in using Expo CLI, skip this step. If you don't have an Expo account, [sign up here](https://expo.dev/signup) and proceed with the login command described below.

To log in, run the following command:

Terminal

Copy

`-Â``eas login`

This command asks for our Expo account email or username and password to complete the login.

### Initialize and link the project to EAS

For any new project, the first step is to initialize and link it to the EAS servers. Run the following command:

Terminal

Copy

`-Â``eas init`

On running, this command:

* Requests verification of the account owner by entering our Expo account credentials and asks if we want to create a new EAS project:

Terminal

`# Output after running eas init``â Which account should own this project? > your-username``â Would you like to create a project for @your-username/sticker-smash? â¦ yes``â Created @your-username/sticker-smash``â Project successfully linked (ID: XXXX-XX-XX-XXXX) (modified app.json)`

* Creates EAS project and provides a link to that project which we can open in the Expo dashboard:

![New project in Expo dashboard](/static/images/tutorial/eas/new-project.png)

* Generates a unique `projectId` and links this EAS project to the example app on our development machine.
* Modifies app.json to include [`extra.eas.projectId`](/versions/latest/sdk/constants#easconfig) and updates its value with the unique ID created.

What is `projectId` in app.json?

When `eas init` runs, it associates a unique identifier for our project in app.json under `extra.eas.projectId`. The value of this property is used to identify our project on EAS servers.

```
{
  "extra": {
    "eas": {
      "projectId": "0cd3da2d-xxx-xxx-xxx-xxxxxxxxxx"
    }
  }
}

```

3

Configure project for EAS Build
-------------------------------

To set up our project for EAS Build, run the following command:

Terminal

Copy

`-Â``eas build:configure`

On running, this command:

* Prompts to select a platform: Android, iOS, or All. Since we are creating Android and iOS apps, let's select All.
* Creates eas.json in the root of our project's directory with the following configuration:

eas.json

Copy

```
{
  "cli": {
    "version": ">= 14.2.0",
    "appVersionSource": "remote"
  },
  "build": {
    "development": {
      "developmentClient": true,
      "distribution": "internal"
    },
    "preview": {
      "distribution": "internal"
    },
    "production": {
      "autoIncrement": true
    }
  },
  "submit": {
    "production": {}
  }
}

```

This is the default configuration for eas.json in a new project. It does two things:

* Defines the current EAS CLI version.
* Adds three [build profiles](/build/eas-json#build-profiles): `development`, `preview`, and `production`.

Explore development profile further

eas.json is a collection of different build profiles. Each profile is tailored with distinct configurations to produce specific build types. These profiles can also include platform-specific settings for Android or iOS.

Currently, our focus is on the `development` profile, which includes the following configuration:

* [`developmentClient`](/eas/json#developmentclient): Enabled (`true`) for creating a debug build. It loads the app using the `expo-dev-client` library, which provides development tools and generates a build artifact for device or emulator/simulator installation and allows using the app for local development as it supports updating the JavaScript on the fly.
* [`distribution`](/eas/json#distribution): Configured as `internal` to indicate that we want to share the build internally (instead of uploading it on app stores).

> Note: Builds offer extensive customization options, including platform-specific settings and the ability to extend configurations across different build profiles. Learn more about [customizing build profiles](/build/eas-json#build-profiles).

Summary
-------

Chapter 1: Configure development build in cloud

We successfully used the EAS CLI to initialize, and configure our project, link it to EAS servers, and prepare a development build.

Mark this chapter as read

In the next chapter, let's create a development build for Android, install it on a device and an emulator, and get it running with the development server.

[Next: Create and run a cloud build for Android](/tutorial/eas/android-development-build)

[Previous (EAS tutorial)

Introduction](/tutorial/eas/introduction)[Next (EAS tutorial)

Android development build](/tutorial/eas/android-development-build)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/tutorial/eas/configure-development-build.mdx)

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Understanding development builds](/tutorial/eas/configure-development-build/#understanding-development-builds)[Key highlights](/tutorial/eas/configure-development-build/#key-highlights)[Install expo-dev-client library](/tutorial/eas/configure-development-build/#install-expo-dev-client-library)[Start the development server](/tutorial/eas/configure-development-build/#start-the-development-server)[Initialize a development build](/tutorial/eas/configure-development-build/#initialize-a-development-build)[Install EAS CLI](/tutorial/eas/configure-development-build/#install-eas-cli)[Log in or sign up for an Expo account](/tutorial/eas/configure-development-build/#log-in-or-sign-up-for-an-expo-account)[Initialize and link the project to EAS](/tutorial/eas/configure-development-build/#initialize-and-link-the-project-to-eas)[Configure project for EAS Build](/tutorial/eas/configure-development-build/#configure-project-for-eas-build)[Summary](/tutorial/eas/configure-development-build/#summary)