Permissions - Expo Documentation

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

Regulatory compliance

[Data and Privacy protection](/regulatory-compliance/data-and-privacy-protection)[GDPR compliance](/regulatory-compliance/gdpr)[HIPAA compliance](/regulatory-compliance/hipaa)[Privacy Shield](/regulatory-compliance/privacy-shield)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Permissions
===========

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/permissions.mdx)

Learn about configuring and adding permissions in an app config file.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/permissions.mdx)

---

When developing a native app that requires access to potentially sensitive information on a user's device, such as their location or contacts, the app must request the user's permission first. For example, to access the user's media library, the app will need to run [`MediaLibrary.requestPermissionsAsync()`](/versions/latest/sdk/media-library#medialibraryrequestpermissionsasync).

Permissions in standalone and [development builds](/develop/development-builds/introduction) require native build-time configuration before they can be requested using runtime JavaScript code. This is not required when testing projects in the [Expo Go](https://expo.dev/go) app.

> If you don't configure or explain the native permissions properly it may result in your app getting rejected or pulled from the stores.

Android
-------

Permissions are configured with the [`android.permissions`](/versions/latest/config/app#permissions) and [`android.blockedPermissions`](/versions/latest/config/app#blockedpermissions) keys in your [app config](/workflow/configuration).

Most permissions are added automatically by libraries that you use in your app either with [config plugins](/config-plugins/plugins-and-mods#create-a-plugin) or with a package-level AndroidManifest.xml. You only need to use `android.permissions` to add additional permissions that are not included by default in a library.

app.json

Copy

```
{
  "android": {
    "permissions": ["android.permission.SCHEDULE_EXACT_ALARM"]
  }
}

```

The only way to remove permissions that are added by package-level AndroidManifest.xml files is to block them with the [`android.blockedPermissions`](/versions/latest/config/app#blockedpermissions) property. To do this, specify the full permission name. For example, if you want to remove the audio recording permissions added by `expo-av`:

app.json

Copy

```
{
  "android": {
    "blockedPermissions": ["android.permission.RECORD_AUDIO"]
  }
}

```

* See [`android.permissions`](/versions/latest/config/app#permissions) to learn about which permissions are included in the default [prebuild template](/workflow/prebuild#templates).
* Apps using *dangerous* or *signature* permissions without valid reasons may be rejected by Google. Ensure you follow the [Android permissions best practices](https://developer.android.com/training/permissions/usage-notes) when submitting your app.
* [All available Android `Manifest.permissions`](https://developer.android.com/reference/android/Manifest.permission).

Are you using this library in an existing React Native app?

Modify AndroidManifest.xml to exclude specific permissions: add the `tools:node="remove"` attribute to a `<use-permission>` tag to ensure it is removed, even if it's included in a library's AndroidManifest.xml.

```
<manifest xmlns:tools="http://schemas.android.com/tools">
  <uses-permission tools:node="remove" android:name="android.permission.ACCESS_FINE_LOCATION" />
</manifest>

```

> You have to define the `xmlns:tools` attribute on `<manifest>` before you can use the `tools:node` attribute on permissions.

iOS
---

Your iOS app can ask for system permissions from the user. For example, to use the device's camera or access photos, Apple requires an explanation for how your app makes use of that data. Most packages will automatically provide a boilerplate reason for a given permission with [config plugins](/config-plugins/introduction). These default messages will most likely need to be tailored to your specific use case for your app to be accepted by the App Store.

To set permission messages, use the [`ios.infoPlist`](/versions/latest/config/app#infoplist) key in your [app config](/workflow/configuration), for example:

app.json

Copy

```
{
  "ios": {
    "infoPlist": {
      "NSCameraUsageDescription": "This app uses the camera to scan barcodes on event tickets."
    }
  }
}

```

Many of these properties are also directly configurable using the [config plugin](/config-plugins/introduction) properties associated with the library that adds them. For example, with [`expo-media-library`](/versions/latest/sdk/media-library) you can configure photo permission messages like this:

app.json

Copy

```
{
  "plugins": [
    [
      "expo-media-library",
      {
        "photosPermission": "Allow $(PRODUCT_NAME) to access your photos.",
        "savePhotosPermission": "Allow $(PRODUCT_NAME) to save photos."
      }
    ]
  ]
}

```

* Changes to the Info.plist cannot be updated over-the-air, they will only be deployed when you submit a new native binary. For example, with [`eas build`](/build/introduction).
* Apple's official [permission message recommendations](https://developer.apple.com/design/human-interface-guidelines/privacy#Requesting-permission).
* [All available Info.plist properties](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html).

Are you using this library in an existing React Native app?

Add and modify the permission message values in Info.plist file directly. We recommend doing this directly in Xcode for autocompletion.

Web
---

On the web, permissions like the `Camera` and `Location` can only be requested from a [secure context](https://developer.mozilla.org/en-US/docs/Web/Security/Secure_Contexts#When_is_a_context_considered_secure). For example, using `https://` or `http://localhost`. This limitation is similar to Android's manifest permissions and iOS's Info.plist usage messages and is enforced to increase privacy.

Resetting permissions
---------------------

Often you want to be able to test what happens when a user rejects permissions, to ensure your app reacts gracefully. An operating-system level restriction on both Android and iOS prohibits an app from asking for the same permission more than once (you can imagine how this could be annoying for the user to be repeatedly prompted for permissions after rejecting them). To test different flows involving permissions in development, you may need to uninstall and reinstall the native app.

When testing in [Expo Go](https://expo.dev/go), you can delete the app and reinstall it by running `npx expo start` and pressing `i` or `a` in the [Expo CLI](/more/expo-cli) Terminal UI.

[Previous (Development process)

Privacy manifests](/guides/apple-privacy)[Next (Development process)

Environment variables](/guides/environment-variables)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/permissions.mdx)
* Last updated on February 12, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Android](/guides/permissions/#android)[iOS](/guides/permissions/#ios)[Web](/guides/permissions/#web)[Resetting permissions](/guides/permissions/#resetting-permissions)