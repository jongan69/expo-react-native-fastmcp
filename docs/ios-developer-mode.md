iOS Developer Mode - Expo Documentation

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

[Authentication with OAuth or OpenID providers](/guides/authentication)[Using Hermes](/guides/using-hermes)[iOS Developer Mode](/guides/ios-developer-mode)[Expo Vector Icons](/guides/icons)[Localization](/guides/localization)[Configure JS engines](/guides/configuring-js-engines)[Using Bun](/guides/using-bun)[Edit rich text](/guides/editing-richtext)[App store assets](/guides/store-assets)[Local-first](/guides/local-first)[Keyboard handling](/guides/keyboard-handling)

Integrations

Troubleshooting

Regulatory compliance

[Data and Privacy protection](/regulatory-compliance/data-and-privacy-protection)[GDPR compliance](/regulatory-compliance/gdpr)[HIPAA compliance](/regulatory-compliance/hipaa)[Privacy Shield](/regulatory-compliance/privacy-shield)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

iOS Developer Mode
==================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/ios-developer-mode.mdx)

Learn how to enable iOS developer mode on iOS 16 and above to run internal distribution builds and local development builds.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/ios-developer-mode.mdx)

---

> This does not apply to builds signed using enterprise provisioning or to any builds installed on an iOS Simulator.

Devices running iOS 16 and above need to enable OS-level Developer Mode setting before they can run [internal distribution](/build/internal-distribution) builds (including those built with EAS) or local development builds after installing them on the device.

There are two ways you can enable Developer Mode on your device:

* Directly on an iOS device
* By connecting an iOS device with a Mac that has Xcode installed

Prerequisites
-------------

The instructions specified below need to be followed once per device.

Enable Developer Mode
---------------------

### Directly on an iOS device

To follow the steps below, install your development build on your device before enabling the Developer Mode. When the build is created, follow the instructions on the Expo dashboard to install it on your iOS device.

1

Once the build is installed on your device, press the app icon. This will open an alert asking you to enable Developer Mode. Press OK.

![Navigating to Developer Mode setting](/static/images/ios-dev-mode/ios-16-developer-mode-0.jpg)

2

Go to the Settings app, and navigate to Privacy & Security > Developer Mode.

![Navigating to Developer Mode setting](/static/images/ios-dev-mode/ios-16-developer-mode-1.png)

3

Enable the toggle. You will receive a prompt from iOS to restart your device. Press Restart.

![Developer Mode restart prompt](/static/images/ios-dev-mode/ios-16-developer-mode-2.png)

4

After the device restarts, unlock your device. A system alert should appear. Press Turn On and then, when prompted, enter your device's passcode.

![Alert and passcode prompt](/static/images/ios-dev-mode/ios-16-developer-mode-3.png)

Developer Mode is now enabled. You can now interact with your internal distribution builds and local development builds.

You can turn off Developer Mode at any time. However, you'll need to repeat this same process to re-enable it.

### Connect an iOS device with a Mac

> Note: Xcode must be installed on the Mac device before following the steps below.

You don't need to install the development build on your iOS device first to enable Developer Mode by connecting it to a Mac. You can:

1

Connect your iOS device to a Mac using a USB cable. Press Trust on your iOS device when Trust This Computer? alert is prompted.

2

Open Xcode, and from the menu bar, navigate to Window > Devices and Simulators.

Under Devices, you'll see a warning "Previous preparation error: Developer Mode disabled" with instructions on enabling Developer Mode on the iOS device.

![Xcode Devices and Simulators window with Developer Mode warning](/static/images/ios-dev-mode/with-xcode-01.png)

3

On the iOS device, open Settings > Privacy & Security > Developer Mode.

Enable the toggle. You will receive a prompt from iOS to restart your device. Press Restart.

![Developer Mode restart prompt](/static/images/ios-dev-mode/with-xcode-02.png)

4

After the device restarts, unlock your device. A system alert should appear. Press Turn On, and enter your device's passcode when prompted.

![Developer Mode restart prompt](/static/images/ios-dev-mode/with-xcode-03.jpg)

Developer Mode is now enabled. You can now interact with your internal distribution builds and local development builds.

You can turn off Developer Mode at any time. However, you'll need to repeat this same process to re-enable it.

[Previous (More - Assorted)

Using Hermes](/guides/using-hermes)[Next (More - Assorted)

Expo Vector Icons](/guides/icons)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/ios-developer-mode.mdx)
* Last updated on June 16, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Prerequisites](/guides/ios-developer-mode/#prerequisites)[Enable Developer Mode](/guides/ios-developer-mode/#enable-developer-mode)[Directly on an iOS device](/guides/ios-developer-mode/#directly-on-an-ios-device)[Connect an iOS device with a Mac](/guides/ios-developer-mode/#connect-an-ios-device-with-a-mac)