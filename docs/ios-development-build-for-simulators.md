Create and run a cloud build for iOS Simulator - Expo Documentation

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

Create and run a cloud build for iOS Simulator
==============================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/tutorial/eas/ios-development-build-for-simulators.mdx)

Learn how to configure a development build for iOS Simulators using EAS Build.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/tutorial/eas/ios-development-build-for-simulators.mdx)

---

In this chapter, we'll create a development build that can run on an iOS Simulator with EAS Build.

Development builds for iOS Simulators are generated in the .app format which is different from iOS devices.

[![Watch: Creating a development build for iOS Simulator](https://i3.ytimg.com/vi/SgL97PFZctg/maxresdefault.jpg)

Watch: Creating a development build for iOS Simulator](https://www.youtube.com/watch?v=SgL97PFZctg)


---

Create a simulator build profile in eas.json
--------------------------------------------

In eas.json, add a new build profile called `ios-simulator` with the property [`ios.simulator`](/eas/json#simulator) property. Set its value `true`:

eas.json

Copy

```
{
  "build": {
    "development": {
      %%placeholder-start%%... %%placeholder-end%%
    },
    "ios-simulator": {
      "ios": {
        "simulator": true
      }
    }
  }
}

```

For a development build, it's necessary to have the `developmentClient` and `distribution` properties defined in the profile. To avoid redundancy, we can extend the `development` profile properties:

eas.json

Copy

```
{
  "ios-simulator": {
    "extends": "development",
    "ios": {
      "simulator": true
    }
  }
}

```

Development build for iOS Simulator
-----------------------------------

1

### Create

Run the `eas build` command with `ios` as a platform and `ios-simulator` as the build profile:

Terminal

Copy

`-Â``eas build --platform ios --profile ios-simulator`

This command prompts us with the following questions when we create the build for the first time:

* What would you like your iOS bundle identifier to be? Press `return` to select the default value provided for this prompt. This will add [`ios.bundleIdentifier`](/versions/latest/config/app#package) in app.json.

After responding to the prompts, our EAS Build is queued, and the EAS CLI provides a link to view build details and track progress on the Expo dashboard:

![iOS Simulator build details page](/static/images/tutorial/eas/ios-sim-build.png)What does a build details page contain?

The build details page displays the build type, profile, Expo SDK version, app version, build number, last commit hash, and the identity of the developer or account owner who initiated the build.

In the above image, the current status of the Build artifact shows that the build is in progress. Upon completion, this section will offer an option to download the build. The Logs outlines every step taken during the iOS build process on EAS Build. For the sake of brevity, we won't explore each step in detail here. To learn more, see [iOS build process](/build-reference/ios-builds).

What is iOS bundle identifier?

The `ios.bundleIdentifier` is a unique name of our app. If we publish our app right now, the Apple App Store will use this property and its value to identify our app on the store.

This notation is defined as `host.owner.app-name`. For example, our example app has `com.owner.stickersmash` where `com.owner` is the domain and `stickersmash` is our app name.

2

### Install

In the terminal, once the build finishes, EAS CLI prompts us by asking whether we want to run the build on an iOS Simulator. Press `Y`.

![EAS CLI automatically gives option to run a build on iOS Simulator](/static/images/tutorial/eas/ios-sim-cli.png)Alternate: Use Expo Orbit

You can use [Expo Orbit](https://expo.dev/orbit) to install the development build. From Build artifact on the Expo dashboard, click Open with Expo Orbit to install the development build on the iOS Simulator.

3

### Run

Start the development server by running the `npx expo start` command from the project directory:

Terminal

Copy

`-Â``npx expo start`

Press `i` in the terminal window to open the project on the iOS Simulator.

Summary
-------

Chapter 3: Create and run a cloud build for iOS Simulator

We successfully used EAS Build to create and run development builds on iOS Simulators.

Mark this chapter as read

In the next chapter, let's create a development build for iOS, install it on a device, and get it running.

[Next: Create and run a cloud build for iOS device](/tutorial/eas/ios-development-build-for-devices)

[Previous (EAS tutorial)

Android development build](/tutorial/eas/android-development-build)[Next (EAS tutorial)

iOS development build for devices](/tutorial/eas/ios-development-build-for-devices)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/tutorial/eas/ios-development-build-for-simulators.mdx)

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Create a simulator build profile in eas.json](/tutorial/eas/ios-development-build-for-simulators/#create-a-simulator-build-profile-in-easjson)[Development build for iOS Simulator](/tutorial/eas/ios-development-build-for-simulators/#development-build-for-ios-simulator)[Create](/tutorial/eas/ios-development-build-for-simulators/#create)[Install](/tutorial/eas/ios-development-build-for-simulators/#install)[Run](/tutorial/eas/ios-development-build-for-simulators/#run)[Summary](/tutorial/eas/ios-development-build-for-simulators/#summary)