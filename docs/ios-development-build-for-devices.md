Create and run a cloud build for iOS device - Expo Documentation

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

Create and run a cloud build for iOS device
===========================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/tutorial/eas/ios-development-build-for-devices.mdx)

Learn how to configure a development build for iOS devices using EAS Build.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/tutorial/eas/ios-development-build-for-devices.mdx)

---

In this chapter, we'll create a development build that can run on an iOS device with EAS Build.

Development builds for iOS devices are generated in the .ipa format, which is standard for iOS app installations.

[![Watch: Creating a development build for iOS physical device](https://i3.ytimg.com/vi/HbfWU7_o4cU/maxresdefault.jpg)

Watch: Creating a development build for iOS physical device](https://www.youtube.com/watch?v=HbfWU7_o4cU)


---

Prerequisites
-------------

Before we begin, ensure you have:

* Apple Developer Account: This is required to access [necessary credentials](/app-signing/app-credentials#ios) for signing our app, as each build needs to be signed to verify that the app comes from a trusted source. EAS Build helps manage these credentials.
* Developer Mode activated on iOS 16 and higher: Installing development builds on your device requires Developer Mode to be enabled. If this is your first time or if it's currently disabled, see these instructions to [activate Developer Mode](/guides/ios-developer-mode).

Provisioning profile
--------------------

To initiate development on an iOS device, we have to:

* Register the device by creating a new [provisioning profile](/app-signing/app-credentials#provisioning-profiles).
* Download and install this profile onto the device.

1

### Register an iOS device

With EAS CLI, run the command to register a new Apple device:

Terminal

Copy

`-Â``eas device:create`

This command prompts us with the following questions

* You're inside the project directory. Would you like to use the your-account-name account? Press `Y`.
* Apple ID. For this step, enter your Apple ID. It will then log in to our Apple Developer account. Follow the steps in the terminal window.
* How would you like to register your devices? Select Website that generates a registration URL that can be opened on the iOS device.

> Tip: If you or your team have multiple devices, you can share the provisioning profile link with those devices for downloading and installing the profile.

2

### Download and install profile

On a device's web browser, open the link provided in the previous step and tap the Download Profile button.

![Download the provisioning profile](/static/images/tutorial/eas/ios-ad-hoc-01.jpg)

Open the Settings app, which prompts us to register our device.

![Install the provisioning profile](/static/images/tutorial/eas/ios-ad-hoc-02.jpg)

Tap Install to register the iOS device.

![Provisioning profile installed successfully](/static/images/tutorial/eas/ios-ad-hoc-03.jpg)

After the provisioning profile is installed, our device redirects us back to the web browser, displaying a success message indicating the completion of the process.

Development build for iOS device
--------------------------------

1

### Create

To create a development build on an iOS device, make sure that under the `build.development` profile:

* The `developmentClient` is set to `true` in eas.json, which is done by the default configuration.
* Then, run the `eas build` command with `ios` as the platform and `development` as the build profile:

Terminal

Copy

`-Â``eas build --platform ios --profile development`

> Tip: Next time you run `eas build` command, you can also use `-p` to specify the platform. It is short for `--platform`.

This command prompts us with the following questions when we create the build for the first time:

* What would you like your iOS bundle identifier to be? Press `return` to select the default value provided for this prompt. This will add [`ios.bundleIdentifier`](/versions/latest/config/app#package) in app.json if it isn't already defined.
* Log in to our Apple Developer account. Since we are creating a development build for the first time, it will ask us to Generate a new Apple Distribution Certificate. Press `Y`.
* Select a device for ad hoc build. This is the key part, which is why we had to register a provisioning profile before. We can select one or all of our registered devices here and then press return to install that build on those devices later.

After responding, the build will queue up, and we can track its progress via a provided link by the EAS CLI in the Expo dashboard:

![iOS preview build details and progress in Expo dashboard](/static/images/tutorial/eas/ios-build.png)What does a build details page contain?

The build details page displays the build type, profile, Expo SDK version, app version, build number, last commit hash, and the identity of the developer or account owner who initiated the build.

In the above image, the current status of the Build artifact shows that the build is in progress. Upon completion, this section will offer an option to download the build. The Logs outlines every step taken during the iOS build process on EAS Build. For the sake of brevity, we won't explore each step in detail here. To learn more, see [iOS build process](/build-reference/ios-builds).

What is iOS bundle identifier?

The `ios.bundleIdentifier` is a unique name of our app. If we publish our app right now, the Apple App Store will use this property and its value to identify our app on the store.

This notation is defined as `host.owner.app-name`. For example, our example app has `com.owner.stickersmash` where `com.owner` is the domain and `stickersmash` is our app name.

2

### Install

Once the build finishes, the Build artifact section gets updated, indicating that the build is complete:

![Build artifact gives the option to download development build for iOS devices and emulators](/static/images/tutorial/eas/ios-build-artifact.png)

This section provides the methods available for running the development build on an iOS device: Expo Orbit and Install button.

[Expo Orbit](https://expo.dev/orbit) allows for seamless installation of the development build on an iOS device. To use this method:

* Connect our iOS device to our developer machine using USB.
* Open the Orbit menu bar app.
* Select the Device in the Orbit app.

![Open with Orbit button on Expo dashboard in Build artifact](/static/images/tutorial/eas/ios-orbit.png)

* On the Expo dashboard, under Build artifact, click the Open with Orbit.

After the build is installed, the Orbit app launches the development build on the device.

Alternate: Use the Install button and QR code

The Install button in the Build artifact section generates a QR code for easy installation:

* Click Install to display a popup with the QR code.

![Install button generates a QR code for easy installation on iOS devices and emulators](/static/images/tutorial/eas/ios-qr-code.png)

* Scan the QR code with our iOS device's camera to open and tap the link to download the development build on the device.

3

### Run

Start the development server by running the `npx expo start` command from the project directory:

Terminal

Copy

`-Â``npx expo start`

* On the device, tap the app icon to open the development build.

![Development build's launcher UI on iOS device](/static/images/tutorial/eas/ios-dev-build-01.jpg)

* Use the account syncing feature by ensuring we're logged into both the EAS CLI and development build. As we're already logged into the EAS CLI, the next step is to log in through the UI of your development build.

![Modal to login to Expo account on iOS device](/static/images/tutorial/eas/ios-dev-build-02.jpg)

* Tap Fetch development servers and select the server running from the list under Development servers.

![Fetching development servers to connect](/static/images/tutorial/eas/ios-dev-build-03.jpg)

Summary
-------

Chapter 4: Create and run a cloud build for iOS device

We successfully used EAS Build to create and run development builds on iOS devices.

Mark this chapter as read

In the next chapter, learn how to configure our app config to install multiple app variants on a single device.

[Next: Configure multiple app variants](/tutorial/eas/multiple-app-variants)

[Previous (EAS tutorial)

iOS development build for simulators](/tutorial/eas/ios-development-build-for-simulators)[Next (EAS tutorial)

Multiple app variants](/tutorial/eas/multiple-app-variants)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/tutorial/eas/ios-development-build-for-devices.mdx)

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Prerequisites](/tutorial/eas/ios-development-build-for-devices/#prerequisites)[Provisioning profile](/tutorial/eas/ios-development-build-for-devices/#provisioning-profile)[Register an iOS device](/tutorial/eas/ios-development-build-for-devices/#register-an-ios-device)[Download and install profile](/tutorial/eas/ios-development-build-for-devices/#download-and-install-profile)[Development build for iOS device](/tutorial/eas/ios-development-build-for-devices/#development-build-for-ios-device)[Create](/tutorial/eas/ios-development-build-for-devices/#create)[Install](/tutorial/eas/ios-development-build-for-devices/#install)[Run](/tutorial/eas/ios-development-build-for-devices/#run)[Summary](/tutorial/eas/ios-development-build-for-devices/#summary)