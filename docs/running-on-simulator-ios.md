Running On Simulator · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/running-on-simulator-ios)

* [Next](/docs/next/running-on-simulator-ios)* [0.79](/docs/running-on-simulator-ios)* [0.78](/docs/0.78/running-on-simulator-ios)* [0.77](/docs/0.77/running-on-simulator-ios)* [0.76](/docs/0.76/running-on-simulator-ios)* [0.75](/docs/0.75/running-on-simulator-ios)* [0.74](/docs/0.74/running-on-simulator-ios)* [0.73](/docs/0.73/running-on-simulator-ios)* [0.72](/docs/0.72/running-on-simulator-ios)* [0.71](/docs/0.71/running-on-simulator-ios)* [0.70](/docs/0.70/running-on-simulator-ios)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [The Basics](/docs/getting-started)

  * [Environment setup](/docs/environment-setup)

    * [Workflow](/docs/running-on-device)

      * [UI & Interaction](/docs/style)

        * [Debugging](/docs/debugging)

          * [Testing](/docs/testing-overview)

            * [Performance](/docs/performance)

              * [JavaScript Runtime](/docs/javascript-environment)

                * [Codegen](/docs/the-new-architecture/what-is-codegen)

                  * [Native Development](/docs/native-platform)

                    * [Android and iOS guides](/docs/headless-js-android)

                      + Android

                        - [Headless JS](/docs/headless-js-android)- [Publishing to Google Play Store](/docs/signed-apk-android)- [Communication between native and React Native](/docs/communication-android)- [React Native Gradle Plugin](/docs/react-native-gradle-plugin)+ iOS

                          - [Linking Libraries](/docs/linking-libraries-ios)- [Running On Simulator](/docs/running-on-simulator-ios)- [Communication between native and React Native](/docs/communication-ios)- [App Extensions](/docs/app-extensions)- [Publishing to Apple App Store](/docs/publishing-to-app-store)* [Legacy Architecture](/docs/legacy/native-modules-intro)

On this page

Running On Simulator
====================

Starting the simulator[​](#starting-the-simulator "Direct link to Starting the simulator")
------------------------------------------------------------------------------------------

Once you have your React Native project initialized, you can run the following command inside the newly created project directory.

* npm* Yarn

shell

```
npm run ios  

```

shell

```
yarn ios  

```

If everything is set up correctly, you should see your new app running in the iOS Simulator shortly.

Specifying a device[​](#specifying-a-device "Direct link to Specifying a device")
---------------------------------------------------------------------------------

You can specify the device the simulator should run with the `--simulator` flag, followed by the device name as a string. The default is `"iPhone 14"`. If you wish to run your app on an iPhone SE (3rd generation), run the following command:

* npm* Yarn

shell

```
npm run ios -- --simulator="iPhone SE (3rd generation)"  

```

shell

```
yarn ios --simulator "iPhone SE (3rd generation)"  

```

The device names correspond to the list of devices available in Xcode. You can check your available devices by running `xcrun simctl list devices` from the console.

### Specifying a version of device[​](#specifying-a-version-of-device "Direct link to Specifying a version of device")

If you have multiple iOS versions installed, you also need to specify its appropriate version. E.g. To run your app on an iPhone 14 Pro (16.0) run the following command:

* npm* Yarn

shell

```
npm run ios -- --simulator="iPhone 14 Pro (16.0)"  

```

shell

```
yarn ios --simulator "iPhone 14 Pro (16.0)"  

```

Specifying an UDID[​](#specifying-an-udid "Direct link to Specifying an UDID")
------------------------------------------------------------------------------

You can specify the device UDID returned from `xcrun simctl list devices` command. E.g. To run your app with UDID `AAAAAAAA-AAAA-AAAA-AAAA-AAAAAAAAAAAA` run the following command:

* npm* Yarn

shell

```
npm run ios -- --udid="AAAAAAAA-AAAA-AAAA-AAAA-AAAAAAAAAAAA"  

```

shell

```
yarn ios --udid "AAAAAAAA-AAAA-AAAA-AAAA-AAAAAAAAAAAA"  

```

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/running-on-simulator-ios.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/running-on-simulator-ios.md)

Last updated on **Apr 14, 2025**

[Previous

Linking Libraries](/docs/linking-libraries-ios)[Next

Communication between native and React Native](/docs/communication-ios)

* [Starting the simulator](#starting-the-simulator)* [Specifying a device](#specifying-a-device)
    + [Specifying a version of device](#specifying-a-version-of-device)* [Specifying an UDID](#specifying-an-udid)

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