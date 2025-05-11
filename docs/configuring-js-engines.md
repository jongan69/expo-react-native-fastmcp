Configure JS engines - Expo Documentation

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

Configure JS engines
====================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/configuring-js-engines.mdx)

A guide on configuring JS engines for both Android and iOS in an Expo project.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/configuring-js-engines.mdx)

---

JavaScript engines execute your application code and provide various features such as memory management, optimization, and error handling. By default, Expo projects use [Hermes](https://hermesengine.dev/) as the JavaScript engine (in SDK 47 and lower, the default was [JavaScriptCore](https://developer.apple.com/documentation/javascriptcore)). Switching to other engines, such as JSC or V8, for Android and iOS platforms is possible. However, not for the web because the JavaScript engine is included in the web browser.

Configuring the `jsEngine` through app config
---------------------------------------------

> Changing the JS engine is unavailable in Expo Go from SDK 52 (only the Hermes engine is available). A [development build](/develop/development-builds/introduction) is required to use this customization.

We recommend Hermes because it is purpose built and optimized for React Native apps, and it has the best debugging experience. If you are familiar with the tradeoffs of different JavaScript engines and would like to change away from Hermes, the [`jsEngine`](/versions/latest/config/app#jsengine) field inside [app config](/workflow/configuration) allows you to specify the JavaScript engine for your app. The default value is `hermes`.

If you want to use JSC instead, set the `jsEngine` field in the app config:

app.json

Copy

```
{
  "expo": {
    "jsEngine": "jsc"
  }
}

```

Usage in bare React Native projects

To change the JavaScript engine in a bare React Native project, update theÂ `expo.jsEngine` value inÂ android/gradle.properties and ios/Podfile.properties.json.

It's important to highlight that changing the JS engine will require you to recompile development builds with `eas build` to work properly.

Using the V8 engine
-------------------

To use the V8 engine, you need to install [`react-native-v8`](https://github.com/Kudo/react-native-v8), an opt-in package that adds V8 runtime support for React Native. You can install it by running the following command:

Terminal

Copy

`-Â``npx expo install react-native-v8 v8-android-jit`

Make sure to remove the `jsEngine` field from the app config.

Usage with Expo Prebuild

Run `npx expo prebuild -p android --clean` after the installation to prebuild again.

Switch JavaScript engine on a specific platform
-----------------------------------------------

To use a different engine on one specific platform, you can set the `"jsEngine"` value at the top level and then override it with a different value under the `"android"` or `"ios"` key. The value specified for the platform will take precedence over the common field.

app.json

Copy

```
{
  "expo": {
    "jsEngine": "hermes",
    "ios": {
      "jsEngine": "jsc"
    }
  }
}

```

[Previous (More - Assorted)

Localization](/guides/localization)[Next (More - Assorted)

Using Bun](/guides/using-bun)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/configuring-js-engines.mdx)
* Last updated on October 14, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Configuring the jsEngine through app config](/guides/configuring-js-engines/#configuring-the-jsengine-through-app-config)[Using the V8 engine](/guides/configuring-js-engines/#using-the-v8-engine)[Switch JavaScript engine on a specific platform](/guides/configuring-js-engines/#switch-javascript-engine-on-a-specific-platform)