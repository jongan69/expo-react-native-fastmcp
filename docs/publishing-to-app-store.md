Publishing to Apple App Store · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/publishing-to-app-store)

* [Next](/docs/next/publishing-to-app-store)* [0.79](/docs/publishing-to-app-store)* [0.78](/docs/0.78/publishing-to-app-store)* [0.77](/docs/0.77/publishing-to-app-store)* [0.76](/docs/0.76/publishing-to-app-store)* [0.75](/docs/0.75/publishing-to-app-store)* [0.74](/docs/0.74/publishing-to-app-store)* [0.73](/docs/0.73/publishing-to-app-store)* [0.72](/docs/0.72/publishing-to-app-store)* [0.71](/docs/0.71/publishing-to-app-store)* [0.70](/docs/0.70/publishing-to-app-store)* [All versions](/versions)

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

Publishing to Apple App Store
=============================

The publishing process is the same as any other native iOS app, with some additional considerations to take into account.

info

If you are using Expo, read the Expo guide for [Deploying to App Stores](https://docs.expo.dev/distribution/app-stores/) to build and submit your app for the Apple App Store. This guide works with any React Native app to automate the deployment process.

### 1. Configure release scheme[​](#1-configure-release-scheme "Direct link to 1. Configure release scheme")

Building an app for distribution in the App Store requires using the `Release` scheme in Xcode. Apps built for `Release` will automatically disable the in-app Dev Menu, which will prevent your users from inadvertently accessing the menu in production. It will also bundle the JavaScript locally, so you can put the app on a device and test whilst not connected to the computer.

To configure your app to be built using the `Release` scheme, go to **Product** → **Scheme** → **Edit Scheme**. Select the **Run** tab in the sidebar, then set the Build Configuration dropdown to `Release`.

![](/assets/images/ConfigureReleaseScheme-68e17e8d9a2cf2b73adb47865b45399d.png)

#### Pro Tips[​](#pro-tips "Direct link to Pro Tips")

As your App Bundle grows in size, you may start to see a blank screen flash between your splash screen and the display of your root application view. If this is the case, you can add the following code to `AppDelegate.m` in order to keep your splash screen displayed during the transition.

objectivec

```
  // Place this code after "[self.window makeKeyAndVisible]" and before "return YES;"  
  UIStoryboard *sb = [UIStoryboard storyboardWithName:@"LaunchScreen" bundle:nil];  
  UIViewController *vc = [sb instantiateInitialViewController];  
  rootView.loadingView = vc.view;  

```

The static bundle is built every time you target a physical device, even in Debug. If you want to save time, turn off bundle generation in Debug by adding the following to your shell script in the Xcode Build Phase `Bundle React Native code and images`:

shell

```
 if [ "${CONFIGURATION}" == "Debug" ]; then  
  export SKIP_BUNDLING=true  
 fi  

```

### 2. Build app for release[​](#2-build-app-for-release "Direct link to 2. Build app for release")

You can now build your app for release by tapping `Cmd ⌘` + `B` or selecting **Product** → **Build** from the menu bar. Once built for release, you'll be able to distribute the app to beta testers and submit the app to the App Store.

info

You can also use the `React Native CLI` to perform this operation using the option `--mode` with the value `Release` (e.g. from the root of your project: `npm run ios -- --mode="Release"` or `yarn ios --mode Release`).

Once you are done with the testing and ready to publish to App Store, follow along with this guide.

* Launch your terminal, and navigate into the iOS folder of your app and type `open .`.
* Double click on YOUR\_APP\_NAME.xcworkspace. It should launch XCode.
* Click on `Product` → `Archive`. Make sure to set the device to "Any iOS Device (arm64)".

note

Check your Bundle Identifier and make sure it is exactly same as the one you have created in the Identifiers in Apple Developer Dashboard.

* After the archive is completed, in the archive window, click on `Distribute App`.
* Click on `App Store Connect` now (if you want to publish in App Store).
* Click `Upload` → Make sure all the check boxes are selected, hit `Next`.
* Choose between `Automatically manage signing` and `Manually manage signing` based on your needs.
* Click on `Upload`.
* Now you can find it in the App Store Connect under TestFlight.

Now fill up the necessary information and in the Build Section, select the build of the app and click on `Save` → `Submit For Review`.

### 4. Screenshots[​](#4-screenshots "Direct link to 4. Screenshots")

The Apple Store requires you have screenshots for the latest devices. The reference for such devices would be found [here](https://developer.apple.com/help/app-store-connect/reference/screenshot-specifications/). Note that screenshots for some display sizes are not required if they are provided for other sizes.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/publishing-to-app-store.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/publishing-to-app-store.md)

Last updated on **Apr 14, 2025**

[Previous

App Extensions](/docs/app-extensions)[Next

Native Modules Intro](/docs/legacy/native-modules-intro)

* [1. Configure release scheme](#1-configure-release-scheme)* [2. Build app for release](#2-build-app-for-release)* [4. Screenshots](#4-screenshots)

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