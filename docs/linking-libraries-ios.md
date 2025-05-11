Linking Libraries · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/linking-libraries-ios)

* [Next](/docs/next/linking-libraries-ios)* [0.79](/docs/linking-libraries-ios)* [0.78](/docs/0.78/linking-libraries-ios)* [0.77](/docs/0.77/linking-libraries-ios)* [0.76](/docs/0.76/linking-libraries-ios)* [0.75](/docs/0.75/linking-libraries-ios)* [0.74](/docs/0.74/linking-libraries-ios)* [0.73](/docs/0.73/linking-libraries-ios)* [0.72](/docs/0.72/linking-libraries-ios)* [0.71](/docs/0.71/linking-libraries-ios)* [0.70](/docs/0.70/linking-libraries-ios)* [All versions](/versions)

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

Linking Libraries
=================

Not every app uses all the native capabilities, and including the code to support all those features would impact the binary size... But we still want to support adding these features whenever you need them.

With that in mind we exposed many of these features as independent static libraries.

For most of the libs it will be as quick as dragging two files, sometimes a third step will be necessary, but no more than that.

note

All the libraries we ship with React Native live in the `Libraries` folder in the root of the repository. Some of them are pure JavaScript, and you only need to `require` it.
Other libraries also rely on some native code, in that case you'll have to add these files to your app, otherwise the app will throw an error as soon as you try to use the library.

Here are the few steps to link your libraries that contain native code[​](#here-are-the-few-steps-to-link-your-libraries-that-contain-native-code "Direct link to Here are the few steps to link your libraries that contain native code")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Automatic linking[​](#automatic-linking "Direct link to Automatic linking")

Install a library with native dependencies:

shell

```
npm install <library-with-native-dependencies> --save  

```

info

`--save` or `--save-dev` flag is very important for this step. React Native will link your libs based on `dependencies` and `devDependencies` in your `package.json` file.

That's it! Next time you build your app the native code will be linked thanks to the [autolinking](https://github.com/react-native-community/cli/blob/main/docs/autolinking.md) mechanism.

### Manual linking[​](#manual-linking "Direct link to Manual linking")

#### Step 1[​](#step-1 "Direct link to Step 1")

If the library has native code, there must be an `.xcodeproj` file inside its folder. Drag this file to your project on Xcode (usually under the `Libraries` group on Xcode);

![](/assets/images/AddToLibraries-92a6a7f58c75a8344d9bbeeae4ac167b.png)

#### Step 2[​](#step-2 "Direct link to Step 2")

Click on your main project file (the one that represents the `.xcodeproj`) select `Build Phases` and drag the static library from the `Products` folder inside the Library you are importing to `Link Binary With Libraries`

![](/assets/images/AddToBuildPhases-3e79422ff24780db618eae2d7a5ea604.png)

#### Step 3[​](#step-3 "Direct link to Step 3")

Not every library will need this step, what you need to consider is:

*Do I need to know the contents of the library at compile time?*

What that means is, are you using this library on the native side or only in JavaScript? If you are only using it in JavaScript, you are good to go!

If you do need to call it from native, then we need to know the library's headers. To achieve that you have to go to your project's file, select `Build Settings` and search for `Header Search Paths`. There you should include the path to your library. (This documentation used to recommend using `recursive`, but this is no longer recommended, as it can cause subtle build failures, especially with CocoaPods.)

![](/assets/images/AddToSearchPaths-7b278a6ea5ef28cfa94e8d22da5a8b13.png)

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/linking-libraries-ios.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/linking-libraries-ios.md)

Last updated on **Apr 14, 2025**

[Previous

React Native Gradle Plugin](/docs/react-native-gradle-plugin)[Next

Running On Simulator](/docs/running-on-simulator-ios)

* [Here are the few steps to link your libraries that contain native code](#here-are-the-few-steps-to-link-your-libraries-that-contain-native-code)
  + [Automatic linking](#automatic-linking)+ [Manual linking](#manual-linking)

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