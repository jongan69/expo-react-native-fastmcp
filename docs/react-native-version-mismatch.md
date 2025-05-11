"React Native version mismatch" errors - Expo Documentation

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

Integrations

Troubleshooting

[Overview](/troubleshooting/overview)["Application has not been registered" error](/troubleshooting/application-has-not-been-registered)[Clear bundler caches on macOS and Linux](/troubleshooting/clear-cache-macos-linux)[Clear bundler caches on Windows](/troubleshooting/clear-cache-windows)["React Native version mismatch" errors](/troubleshooting/react-native-version-mismatch)[Proxies](/troubleshooting/proxies)

Regulatory compliance

[Data and Privacy protection](/regulatory-compliance/data-and-privacy-protection)[GDPR compliance](/regulatory-compliance/gdpr)[HIPAA compliance](/regulatory-compliance/hipaa)[Privacy Shield](/regulatory-compliance/privacy-shield)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

"React Native version mismatch" errors
======================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/troubleshooting/react-native-version-mismatch.mdx)

Learn about what React Native version mismatch means and how to resolve it in an Expo or React Native app.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/troubleshooting/react-native-version-mismatch.mdx)

---

When developing an Expo or React Native app, it's common to run into an error that looks like:

Terminal

`React Native version mismatch.`  
`JavaScript version: X.XX.X``Native version: X.XX.X`  
`Make sure you have rebuilt the native code...`

What this error means
---------------------

The bundler that you're running in your terminal (using `npx expo start`) is using a different JavaScript version of `react-native` than the native app on your device or emulator. This can happen after upgrading your React Native or Expo SDK version, *or* when connecting to the wrong local development server.

How to fix it
-------------

* Close out any development servers that you have running (you can list all terminal processes with the `ps` command, and search for Expo CLI or React Native community CLI processes with `ps -A | grep "expo\|react-native"`).
* If this is a Expo project, either remove the `sdkVersion` field from your app.json file, or make sure it matches the value of the `expo` dependency in your package.json file.
* If this is a Expo project, you should make sure your `react-native` version is correct. Run `npx expo-doctor` will show a warning where the `react-native` version you should install. If you did upgrade to a newer SDK, make sure to run `npx expo install --fix` and follow the prompts. Expo CLI will make sure that your dependency versions for packages like `expo` and `react-native` are aligned.
* If this is a bare React Native project, and this error is occurring right after upgrading your React Native version, you should double-check that you have performed each of the upgrade steps correctly.
* Finally:

  + Clear your bundler caches by running `rm -rf node_modules && npm cache clean --force && npm install && watchman watch-del-all && rm -rf $TMPDIR/haste-map-* && rm -rf $TMPDIR/metro-cache && npx expo start --clear`
    - Commands if you are using npm can be found [here.](/troubleshooting/clear-cache-macos-linux)
    - Commands if you are using Windows can be found [here.](/troubleshooting/clear-cache-windows)
  + If this is a bare React Native project, run `npx pod-install`, then rebuild your native projects (run `yarn android` to rebuild for Android, and `yarn ios` to rebuild iOS)

[Previous (More - Troubleshooting)

Clear bundler caches on Windows](/troubleshooting/clear-cache-windows)[Next (More - Troubleshooting)

Proxies](/troubleshooting/proxies)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/troubleshooting/react-native-version-mismatch.mdx)
* Last updated on September 17, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[What this error means](/troubleshooting/react-native-version-mismatch/#what-this-error-means)[How to fix it](/troubleshooting/react-native-version-mismatch/#how-to-fix-it)