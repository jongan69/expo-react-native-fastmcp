Debugging Native Code · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/debugging-native-code)

* [Next](/docs/next/debugging-native-code)* [0.79](/docs/debugging-native-code)* [0.78](/docs/0.78/debugging-native-code)* [0.77](/docs/0.77/debugging-native-code)* [0.76](/docs/0.76/debugging-native-code)* [0.75](/docs/0.75/debugging-native-code)* [0.74](/docs/0.74/getting-started)* [0.73](/docs/0.73/getting-started)* [0.72](/docs/0.72/getting-started)* [0.71](/docs/0.71/getting-started)* [0.70](/docs/0.70/getting-started)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [The Basics](/docs/getting-started)

  * [Environment setup](/docs/environment-setup)

    * [Workflow](/docs/running-on-device)

      * [UI & Interaction](/docs/style)

        * [Debugging](/docs/debugging)

          + [Debugging Basics](/docs/debugging)+ [React Native DevTools](/docs/react-native-devtools)+ [Debugging Native Code](/docs/debugging-native-code)+ [Debugging Release Builds](/docs/debugging-release-builds)+ [Other Debugging Methods](/docs/other-debugging-methods)* [Testing](/docs/testing-overview)

            * [Performance](/docs/performance)

              * [JavaScript Runtime](/docs/javascript-environment)

                * [Codegen](/docs/the-new-architecture/what-is-codegen)

                  * [Native Development](/docs/native-platform)

                    * [Android and iOS guides](/docs/headless-js-android)

                      * [Legacy Architecture](/docs/legacy/native-modules-intro)

On this page

Debugging Native Code
=====================

### Projects with Native Code Only

The following section only applies to projects with native code exposed. If you are using the managed Expo workflow, see the guide on [prebuild](https://docs.expo.dev/workflow/prebuild/) to use this API.

Accessing Logs[​](#accessing-logs "Direct link to Accessing Logs")
------------------------------------------------------------------

You can display the native logs for an iOS or Android app by using the following commands in a terminal while the app is running:

shell

```
# For Android:  
npx react-native log-android  
# Or, for iOS:  
npx react-native log-ios  

```

You may also access these through Debug > Open System Log… in the iOS Simulator or by running `adb logcat "*:S" ReactNative:V ReactNativeJS:V` in a terminal while an Android app is running on a device or emulator.

**💡 Custom Native Logs**

If you are writing a Native Module and want to add custom logs to your module for debugging purposes, you can use the following method:

#### Android (Java/Kotlin)[​](#android-javakotlin "Direct link to Android (Java/Kotlin)")

In your native module, use the `Log` class to add logs that can be viewed in Logcat:

java

```
import android.util.Log;  
  
private void log(String message) {  
    Log.d("YourModuleName", message);  
}  

```

To view these logs in Logcat, use this command, replacing `YourModuleName` with your custom tag:

shell

```
adb logcat "*:S" ReactNative:V ReactNativeJS:V YourModuleName:D  

```

#### iOS (Objective-C/Swift)[​](#ios-objective-cswift "Direct link to iOS (Objective-C/Swift)")

In your native module, use `NSLog` for custom logs:

objective-c

```
NSLog(@"YourModuleName: %@", message);  

```

Or, in Swift:

swift

```
print("YourModuleName: \(message)")  

```

These logs will appear in the Xcode console when running the app.

Debugging in a Native IDE[​](#debugging-in-a-native-ide "Direct link to Debugging in a Native IDE")
---------------------------------------------------------------------------------------------------

When working with native code, such as when writing native modules, you can launch the app from Android Studio or Xcode and take advantage of the native debugging features (setting up breakpoints, etc.) as you would in case of building a standard native app.

Another option is to run your application using the React Native CLI and attach the native debugger of the native IDE (Android Studio or Xcode) to the process.

### Android Studio[​](#android-studio "Direct link to Android Studio")

On Android Studio you can do this by going on the "Run" option on the menu bar, clicking on "Attach to Process..." and selecting the running React Native app.

### Xcode[​](#xcode "Direct link to Xcode")

On Xcode click on "Debug" on the top menu bar, select the "Attach to process" option, and select the application in the list of "Likely Targets".

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/debugging-native-code.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/debugging-native-code.md)

Last updated on **Apr 14, 2025**

[Previous

React Native DevTools](/docs/react-native-devtools)[Next

Debugging Release Builds](/docs/debugging-release-builds)

* [Accessing Logs](#accessing-logs)* [Debugging in a Native IDE](#debugging-in-a-native-ide)
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