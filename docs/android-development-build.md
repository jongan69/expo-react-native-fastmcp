Create and run a cloud build for Android - Expo Documentation

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

Create and run a cloud build for Android
========================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/tutorial/eas/android-development-build.mdx)

Learn how to configure a development build for Android devices and emulators using EAS Build.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/tutorial/eas/android-development-build.mdx)

---

In this chapter, we'll create a development build that can run on Android with EAS Build.

The process for creating and running a build on Android devices or emulators is identical, with differences only in the installation of the development build.

[![Watch: How to create and run a cloud build for Android](https://i3.ytimg.com/vi/D612BUtvvl8/maxresdefault.jpg)

Watch: How to create and run a cloud build for Android](https://www.youtube.com/watch?v=D612BUtvvl8)


---

Create a build for the development profile
------------------------------------------

For Android, the development build must be in the .apk. While the default Android format is .aab, which is ideal for Google Play Store distribution, it cannot be installed on devices or emulators.

To create a .apk:

* In eas.json, make sure that `developmentClient` is set to `true` under `build.development` profile.
* Then, run the `eas build` command with `android` as the platform and `development` as the build profile:

  Terminal

  Copy

  `-Â``eas build --platform android --profile development`

  > Tip: Next time you run `eas build` command, you can also use `-p` to specify the platform. It is short for `--platform`.

This command prompts us with the following questions:

* What would you like your Android application id to be? Press `return` to select the default value provided for this prompt. This will add [`android.package`](/versions/latest/config/app#package) in app.json.
* Generate a new Android Keystore? Press `Y`.

After responding, the build will queue up, and we can track its progress via a provided link by the EAS CLI in the Expo dashboard:

![Android development build details and progress in Expo dashboard](/static/images/tutorial/eas/android-build-details.png)
What information does a build details page contain?

The build details page displays the build type, profile, Expo SDK version, app version, version code, last commit hash, and the identity of the developer or account owner who initiated the build.

In the above image, the current status of the Build artifact shows that the build is in progress. Upon completion, this section will offer an option to download the build. The Logs outlines every step taken during the Android build process on EAS Build. For the sake of brevity, we won't explore each step in detail here. To learn more, see [Android build process](/build-reference/android-builds).

What is an Android application ID?

Also known as the package name of our Android app, it stores the value in DNS reverse notation format (`com.owner.appname`). Each component of this notation should start with a lowercase letter.

For example, our example app has `com.owner.stickersmash` where `com.owner` is the domain and `stickersmash` is our app name.

Android device
--------------

1

### Install development build

Once the build finishes, the Build artifact section gets updated, indicating that the build is complete:

![Build artifact gives the option to download development build for Android devices and emulators](/static/images/tutorial/eas/android-build-artifact.png)

This section provides the methods available for running the development build on an Android device: Expo Orbit and Install button.

[Expo Orbit](https://expo.dev/orbit) allows for seamless installation of the development build on an Android device. To use this method:

* Connect our Android device to our local machine using USB.
* Open the Orbit menu bar app.
* Select the Device in the Orbit app.

![Expo Orbit app interface when connected to an Android device](/static/images/tutorial/eas/android-orbit.png)

* On the Expo dashboard, under Build artifact, click the Open with Orbit.

After the build is installed, the Orbit app launches the development build on the device.

Alternate: Use the Install button and QR code

The Install button in the Build artifact generates a QR code for installation:

* Click Install to display a popup with the QR code.

![Install button generates a QR code for easy installation on Android devices and emulators](/static/images/tutorial/eas/android-qr-code.png)

* Scan the QR code with our Android device's camera to open the build link in the default web browser.
* Tap the Install button on the webpage to download the .apk file.
* Once downloaded, open the .apk to start the installation process.
* If an Unsafe app blocked message appears, select Install anyway. This warning can safely be ignored as the source of the .apk (which we generated) is trusted.

![Unsafe app message dialog on Android device when installing development build](/static/images/tutorial/eas/android-unsafe-dialog.png)

2

### Run development build

Start the development server by running `npx expo start` from the project directory. Once the server is running, press `a` in the terminal window to open the project:

Terminal

Copy

`-Â``npx expo start`

Android Emulator
----------------

1

### Install the development build

In the terminal, once the build finishes, EAS CLI prompts us by asking whether we want to run the build on an Android Emulator. Press `Y`.

![EAS CLI automatically gives to run build on Android Emulator](/static/images/tutorial/eas/android-emulator-cli.png)Alternate: Use Expo Orbit

Alternatively, [Expo Orbit](/build/orbit) can be used for installation. From Build artifact on the Expo dashboard, click Open with Expo Orbit to install the development build on the Android Emulator.

2

### Run the development build

Start the development server by running `npx expo start` from the project directory. Once the server is running, press `a` in the terminal window to open the project:

Terminal

Copy

`-Â``npx expo start`

Summary
-------

Chapter 2: Create and run a cloud build for Android

We successfully used EAS Build to create and run development builds on Android devices and emulators, and learned about .apk and .aab file formats.

Mark this chapter as read

In the next chapter, learn how to configure a development build for iOS Simulators using EAS Build and get it running.

[Next: Create and run a cloud build for iOS Simulator](/tutorial/eas/ios-development-build-for-simulators)

[Previous (EAS tutorial)

Configure development build](/tutorial/eas/configure-development-build)[Next (EAS tutorial)

iOS development build for simulators](/tutorial/eas/ios-development-build-for-simulators)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/tutorial/eas/android-development-build.mdx)

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Create a build for the development profile](/tutorial/eas/android-development-build/#create-a-build-for-the-development-profile)[Android device](/tutorial/eas/android-development-build/#android-device)[Install development build](/tutorial/eas/android-development-build/#install-development-build)[Run development build](/tutorial/eas/android-development-build/#run-development-build)[Android Emulator](/tutorial/eas/android-development-build/#android-emulator)[Install the development build](/tutorial/eas/android-development-build/#install-the-development-build)[Run the development build](/tutorial/eas/android-development-build/#run-the-development-build)[Summary](/tutorial/eas/android-development-build/#summary)