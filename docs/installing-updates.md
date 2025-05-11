Install expo-updates in an existing React Native project - Expo Documentation

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

[Overview](/bare/overview)[Install Expo modules](/bare/installing-expo-modules)[Migrate to Expo CLI](/bare/using-expo-cli)[Install expo-updates](/bare/installing-updates)[Install expo-dev-client](/bare/install-dev-builds-in-bare)[Native project upgrade helper](/bare/upgrade)

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

Install expo-updates in an existing React Native project
========================================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/bare/installing-updates.mdx)

Learn how to install and configure expo-updates in your existing React Native project.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/bare/installing-updates.mdx)

---

`expo-updates` is a library that enables your app to manage remote updates to your application code. It communicates with the configured remote update service to get information about available updates. This guide explains how to set up a bare React Native project for use with [EAS Update](/eas-update/introduction), a hosted remote update service that includes tools to simplify installation and configuration of the `expo-updates` library.

Do you use Continuous Native Generation (CNG) in your project?

You may be reading the wrong guide. To use `expo-updates` in a project that uses [CNG](/workflow/continuous-native-generation), see [EAS Update "Get started"](/eas-update/getting-started).

Prerequisites
-------------

The `expo` package must be installed and configured. If you created your project with `npx @react-native-community/cli@latest init` and do not have any other Expo libraries installed, you will need to [install Expo modules](/bare/installing-expo-modules) before proceeding.

Installation
------------

To get started, install `expo-updates`:

Terminal

Copy

`-Â``npx expo install expo-updates`

Then, install pods for iOS:

Terminal

Copy

`-Â``npx pod-install`

Configuring expo-updates library
--------------------------------

Apply the changes from the diffs from the following sections to configure `expo-updates` in your project.

### JavaScript and JSON

Run `eas update:configure` to set the `updates` URL and `projectId` in app.json.

Terminal

Copy

`-Â``eas update:configure`

Modify the `expo` section of app.json. If you created your project using `npx @react-native-community/cli@latest init`, you will need to add the following changes including the [`updates` URL](/versions/latest/config/app#url).

> The example `updates` URL and `projectId` shown below are used with EAS Update. The EAS CLI sets this URL correctly for the EAS Update service when running `eas update:configure`.

If you want to set up a [custom `expo-updates` server](https://github.com/expo/custom-expo-updates-server) instead, add your URL to `updates.url` in app.json.

app.json

Copy

```
 {
   "name": "MyApp",
   "displayName": "MyApp",
   "expo": {
     "name": "MyApp",
      ...
     "updates": {
-      "url": "https://u.expo.dev/[your-project-id]"
+      "url": "http://localhost:3000/api/manifest"
     }
   }
 }

```

### Android

Modify android/app/build.gradle to check for the JS engine configuration (JSC or Hermes) in Expo files:

Modify android/app/src/main/AndroidManifest.xml to add the `expo-updates` configuration XML so that it matches the contents of app.json:

If using the updates server URL (a custom non-HTTPS update server running on the same machine), you will need to modify android/app/src/main/AndroidManifest.xml to add the update server URL and enable `usesCleartextTraffic`:

android/app/src/main/AndroidManifest.xml

Copy

```
 <application
  android:name=".MainApplication"
  android:label="@string/app_name"
  android:icon="@mipmap/ic_launcher"
  android:roundIcon="@mipmap/ic_launcher_round"
  android:allowBackup="false"
  android:theme="@style/AppTheme"
+ android:usesCleartextTraffic="true"
 >

- <meta-data android:name="expo.modules.updates.EXPO_UPDATE_URL" android:value="https://u.expo.dev/[your-project-id]"/>
+ <meta-data android:name="expo.modules.updates.EXPO_UPDATE_URL" android:value="http://localhost:3000/api/manifest"/>
 </application>

```

Add the Expo runtime version string key to android/app/src/main/res/values/strings.xml:

### iOS

Add the file Podfile.properties.json to the ios directory:

ios/Podfile.properties.json

Copy

```
{
  "expo.jsEngine": "hermes"
}

```

Modify ios/Podfile to check for the JS engine configuration (JSC or Hermes) in Expo files:

Using Xcode, add Expo.plist file to ios/your-project/Supporting with the following content to match the contents of app.json:

Expo.plist

Copy

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>EXUpdatesCheckOnLaunch</key>
    <string>ALWAYS</string>
    <key>EXUpdatesEnabled</key>
    <true/>
    <key>EXUpdatesLaunchWaitMs</key>
    <integer>0</integer>
    <key>EXUpdatesRuntimeVersion</key>
    <string>1.0.0</string>
    <key>EXUpdatesURL</key>
    <string>http://localhost:3000/api/manifest</string>
  </dict>
</plist>

```

Next steps
----------

* To start using EAS Update with EAS Build, see the EAS Update [Get started](/eas-update/getting-started).
* See [`expo-updates` API reference](/versions/latest/sdk/updates) for more information on how to use the library.
* See how to use [EAS Update with a local build directly](/eas-update/standalone-service).
* It is also possible to use `expo-updates` with a custom server that implements the [Expo Updates protocol](/technical-specs/expo-updates-1). See [`custom-expo-updates-server` README](https://github.com/expo/custom-expo-updates-server#readme).

[Previous (Development process - Existing React Native apps)

Migrate to Expo CLI](/bare/using-expo-cli)[Next (Development process - Existing React Native apps)

Install expo-dev-client](/bare/install-dev-builds-in-bare)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/bare/installing-updates.mdx)
* Last updated on February 11, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Prerequisites](/bare/installing-updates/#prerequisites)[Installation](/bare/installing-updates/#installation)[Configuring expo-updates library](/bare/installing-updates/#configuring-expo-updates-library)[JavaScript and JSON](/bare/installing-updates/#javascript-and-json)[Android](/bare/installing-updates/#android)[iOS](/bare/installing-updates/#ios)[Next steps](/bare/installing-updates/#next-steps)