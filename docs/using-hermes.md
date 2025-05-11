Using Hermes Engine - Expo Documentation

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

Using Hermes Engine
===================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/using-hermes.mdx)

A guide on configuring Hermes for both Android and iOS in an Expo project.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/using-hermes.mdx)

---

[Hermes](https://hermesengine.dev/) is a JavaScript engine optimized for React Native. By compiling JavaScript into bytecode ahead of time, Hermes can improve your app start-up time. The binary size of Hermes is also smaller than other JavaScript engines, such as JavaScriptCore (JSC). It also uses less memory at runtime, which is particularly valuable on lower-end Android devices.

Support
-------

The Hermes engine is the default JavaScript engine used by Expo and it is fully supported across all Expo tooling.

### Switch JavaScript engine on a specific platform

You may want to use Hermes on one platform and JSC on another. One way to do this is to set the `"jsEngine"` to `"hermes"` at the top level in app config and then override it with `"jsc"` under the `"ios"` key. You may alternatively prefer to explicitly set `"hermes"` on just the `"android"` key in this case.

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

Publish updates
---------------

Publishing updates with `eas update` and `npx expo export` will generate Hermes bytecode bundles and their source maps.

Note that the Hermes bytecode format may change between different Hermes versions â an update produced for a specific version of Hermes will not run on a different version of Hermes. Starting from Expo SDK 46 (React Native 0.69), [Hermes is bundled within React Native](https://reactnative.dev/architecture/bundled-hermes). Updating React Native version or Hermes version can be thought of in the same way as updating any other native module. So if you update the `react-native` version you should also update the `runtimeVersion` in app.json. If you don't do this, your app may crash on launch because the update may be loaded by an existing binary that uses an older Hermes version that is incompatible with the updated bytecode format. See [`runtimeVersion`](/eas-update/runtime-versions) for more information.

JavaScript debugger
-------------------

To debug JavaScript code running with Hermes, you can start your project with `npx expo start` then press `j` to open the debugger in Google Chrome or Microsoft Edge. The developer menu of development builds and Expo Go also have the Open JS Debugger option to do the same.

Alternatively, you can use the JavaScript inspector by opening [Google Chrome DevTools manually](https://reactnative.dev/docs/other-debugging-methods#remote-javascript-debugging-deprecated)

### Troubleshooting

> `No compatible apps connected. JavaScript Debugging can only be used with the Hermes engine.` when opening the debugger.

* Make sure you [set up Hermes in the `jsEngine` field](/guides/using-hermes#setup).
* If your app is built by `eas build`, `npx expo run:android` or `npx expo run:ios`, make sure it is a debug build.
* Internally, the app will establish a WebSocket connection, make sure your app is connected to the development server.

  + Try to reload the app by pressing `r` in the Expo CLI Terminal UI.
  + Test debugging availability by running the command: `curl http://127.0.0.1:8081/json/list` (adjust the `127.0.0.1:8081` to match your dev server URL). The HTTP response should be an array, as shown below. If it is an empty response, add either the `--localhost` or `--tunnel` flag to the `npx expo start` command.

  ```
  [
    {
      "id": "0-2",
      "description": "host.exp.Exponent",
      "title": "Hermes ABI47_0_0React Native",
      "faviconUrl": "https://react.dev/favicon.ico",
      "devtoolsFrontendUrl": "devtools://devtools/bundled/js_app.html?experiments=true&v8only=true&ws=%5B%3A%3A1%5D%3A8081%2Finspector%2Fdebug%3Fdevice%3D0%26page%3D2",
      "type": "node",
      "webSocketDebuggerUrl": "ws://[::1]:8081/inspector/debug?device=0&page=2",
      "vm": "Hermes"
    },
    {
      "id": "0--1",
      "description": "host.exp.Exponent",
      "title": "React Native Experimental (Improved Chrome Reloads)",
      "faviconUrl": "https://react.dev/favicon.ico",
      "devtoolsFrontendUrl": "devtools://devtools/bundled/js_app.html?experiments=true&v8only=true&ws=%5B%3A%3A1%5D%3A8081%2Finspector%2Fdebug%3Fdevice%3D0%26page%3D-1",
      "type": "node",
      "webSocketDebuggerUrl": "ws://[::1]:8081/inspector/debug?device=0&page=-1",
      "vm": "don't use"
    }
  ]

  ```

### Can I use Remote Debugging with Hermes?

One of the many limitations of [remote debugging](/more/glossary-of-terms#remote-debugging) is that it does not work with modules built on top of [JSI](https://github.com/react-native-community/discussions-and-proposals/issues/91), such as [`react-native-reanimated`](https://github.com/software-mansion/react-native-reanimated) version 2 or higher.

Hermes supports [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/v8/) to debug JavaScript in place by connecting to the engine running on the device, as opposed to remote debugging, which executes JavaScript within a desktop Chrome tab. Hermes apps use this debugging technique automatically when you open the debugger in Expo Go or a development build.

[Previous (More - Assorted)

Authentication with OAuth or OpenID providers](/guides/authentication)[Next (More - Assorted)

iOS Developer Mode](/guides/ios-developer-mode)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/using-hermes.mdx)
* Last updated on March 11, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Support](/guides/using-hermes/#support)[Switch JavaScript engine on a specific platform](/guides/using-hermes/#switch-javascript-engine-on-a-specific-platform)[Publish updates](/guides/using-hermes/#publish-updates)[JavaScript debugger](/guides/using-hermes/#javascript-debugger)[Troubleshooting](/guides/using-hermes/#troubleshooting)[Can I use Remote Debugging with Hermes?](/guides/using-hermes/#can-i-use-remote-debugging-with-hermes)