Native Debugging · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.74](/docs/0.74/native-debugging)

* [Next](/docs/next/getting-started)* [0.79](/docs/getting-started)* [0.78](/docs/0.78/getting-started)* [0.77](/docs/0.77/getting-started)* [0.76](/docs/0.76/getting-started)* [0.75](/docs/0.75/getting-started)* [0.74](/docs/0.74/native-debugging)* [0.73](/docs/0.73/native-debugging)* [0.72](/docs/0.72/native-debugging)* [0.71](/docs/0.71/getting-started)* [0.70](/docs/0.70/getting-started)* [All versions](/versions)

[Development](#)

* [Guides](/docs/0.74/getting-started)* [Components](/docs/0.74/components-and-apis)* [APIs](/docs/0.74/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [The Basics](/docs/0.74/getting-started)

  * [Environment setup](/docs/0.74/environment-setup)

    * [Workflow](/docs/0.74/running-on-device)

      * [UI & Interaction](/docs/0.74/style)

        * [Debugging](/docs/0.74/debugging)

          + [Debugging Basics](/docs/0.74/debugging)+ [React DevTools](/docs/0.74/react-devtools)+ [Native Debugging](/docs/0.74/native-debugging)+ [Debugging Release Builds](/docs/0.74/debugging-release-builds)+ [Other Debugging Methods](/docs/0.74/other-debugging-methods)* [Testing](/docs/0.74/testing-overview)

            * [Performance](/docs/0.74/performance)

              * [JavaScript Runtime](/docs/0.74/javascript-environment)

                * [Native Modules](/docs/0.74/native-modules-intro)

                  * [Native Components](/docs/0.74/native-components-android)

                    * [Android and iOS guides](/docs/0.74/headless-js-android)

                      * [New Architecture](/docs/0.74/the-new-architecture/landing-page)

This is documentation for React Native **0.74**, which is no longer in active development.

For up-to-date documentation, see the **[latest version](/docs/getting-started)** (0.79).

Version: 0.74

On this page

Native Debugging
================

### Projects with Native Code Only

The following section only applies to projects with native code exposed. If you are using the managed Expo workflow, see the guide on [prebuild](https://docs.expo.dev/workflow/prebuild/) to use this API.

Accessing native logs[​](#accessing-native-logs "Direct link to Accessing native logs")
---------------------------------------------------------------------------------------

You can display the console logs for an iOS or Android app by using the following commands in a terminal while the app is running:

shell

```
# For Android:  
npx react-native log-android  
# Or, for iOS:  
npx react-native log-ios  

```

You may also access these through Debug > Open System Log… in the iOS Simulator or by running `adb logcat "*:S" ReactNative:V ReactNativeJS:V` in a terminal while an Android app is running on a device or emulator.

info

If you're using Expo CLI, console logs already appear in the same terminal output as the bundler.

Debugging native code[​](#debugging-native-code "Direct link to Debugging native code")
---------------------------------------------------------------------------------------

When working with native code, such as when writing native modules, you can launch the app from Android Studio or Xcode and take advantage of the native debugging features (setting up breakpoints, etc.) as you would in case of building a standard native app.

Another option is to run your application using the React Native CLI and attach the native debugger of the native IDE (Android Studio or Xcode) to the process.

### Android Studio[​](#android-studio "Direct link to Android Studio")

On Android Studio you can do this by going on the "Run" option on the menu bar, clicking on "Attach to Process..." and selecting the running React Native app.

### Xcode[​](#xcode "Direct link to Xcode")

On Xcode click on "Debug" on the top menu bar, select the "Attach to process" option, and select the application in the list of "Likely Targets".

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/native-debugging.md)[Edit page for 0.74 release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.74/native-debugging.md)

Last updated on **Oct 10, 2024**

[Previous

React DevTools](/docs/0.74/react-devtools)[Next

Debugging Release Builds](/docs/0.74/debugging-release-builds)

* [Accessing native logs](#accessing-native-logs)* [Debugging native code](#debugging-native-code)
    + [Android Studio](#android-studio)+ [Xcode](#xcode)

Develop

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

Participate

* [Showcase](/showcase)* [Contributing](/contributing/overview)* [Community](/community/overview)* [Directory](https://reactnative.directory/)* [Stack Overflow](https://stackoverflow.com/questions/tagged/react-native)

Find us

* [Blog](/blog)* [X](https://x.com/reactnative)* [Bluesky](https://bsky.app/profile/reactnative.dev)* [GitHub](https://github.com/facebook/react-native)

Explore More

* [ReactJS](https://react.dev/)* [Privacy Policy](https://opensource.fb.com/legal/privacy/)* [Terms of Service](https://opensource.fb.com/legal/terms/)

[![Meta Open Source Logo](/img/oss_logo.svg)![Meta Open Source Logo](/img/oss_logo.svg)](https://opensource.fb.com/)

Copyright © 2025 Meta Platforms, Inc.