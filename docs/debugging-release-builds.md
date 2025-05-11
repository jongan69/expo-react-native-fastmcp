Debugging Release Builds · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/debugging-release-builds)

* [Next](/docs/next/debugging-release-builds)* [0.79](/docs/debugging-release-builds)* [0.78](/docs/0.78/debugging-release-builds)* [0.77](/docs/0.77/debugging-release-builds)* [0.76](/docs/0.76/debugging-release-builds)* [0.75](/docs/0.75/debugging-release-builds)* [0.74](/docs/0.74/debugging-release-builds)* [0.73](/docs/0.73/debugging-release-builds)* [0.72](/docs/0.72/getting-started)* [0.71](/docs/0.71/getting-started)* [0.70](/docs/0.70/getting-started)* [All versions](/versions)

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

Debugging Release Builds
========================

Symbolicating a stack trace[​](#symbolicating-a-stack-trace "Direct link to Symbolicating a stack trace")
---------------------------------------------------------------------------------------------------------

If a React Native app throws an unhandled exception in a release build, the output may be obfuscated and hard to read.

shell

```
07-15 10:58:25.820 18979 18998 E AndroidRuntime: FATAL EXCEPTION: mqt_native_modules  
07-15 10:58:25.820 18979 18998 E AndroidRuntime: Process: com.awesomeproject, PID: 18979 07-15 10:58:25.820 18979 18998 E AndroidRuntime: com.facebook.react.common.JavascriptException: Failed, js engine: hermes, stack:  
07-15 10:58:25.820 18979 18998 E AndroidRuntime: p@1:132161  
07-15 10:58:25.820 18979 18998 E AndroidRuntime: p@1:132084  
07-15 10:58:25.820 18979 18998 E AndroidRuntime: f@1:131854  
07-15 10:58:25.820 18979 18998 E AndroidRuntime: anonymous@1:131119  

```

In the above stack trace, entries like `p@1:132161` are minified function names and bytecode offsets. To debug these calls, we want to translate these into file, line, and function name, e.g. `AwesomeProject/App.js:54:initializeMap`. This is known as **symbolication.**

You can symbolicate minified function names and bytecode like the above by passing the stack trace and a generated source map to [`metro-symbolicate`](http://npmjs.com/package/metro-symbolicate).

### Enabling source maps[​](#enabling-source-maps "Direct link to Enabling source maps")

Source maps are required to symbolicate stack traces. Make sure that source maps are enabled within the build config for the target platform.

* Android* iOS

info

On Android, source maps are **enabled** by default.

To enable source map generation, ensure the following `hermesFlags` are present in `android/app/build.gradle`.

groovy

```
react {  
    hermesFlags = ["-O", "-output-source-map"]  
}  

```

If done correctly you should see the output location of the source map during Metro build output.

text

```
Writing bundle output to:, android/app/build/generated/assets/react/release/index.android.bundle  
Writing sourcemap output to:, android/app/build/intermediates/sourcemaps/react/release/index.android.bundle.packager.map  

```

info

On iOS, source maps are **disabled** by default. Use the following instructions to enable them.

To enable source map generation:

* Open Xcode and edit the build phase "Bundle React Native code and images".
* Above the other exports, add a `SOURCEMAP_FILE` entry with the desired output path.

diff

```
+ SOURCEMAP_FILE="$(pwd)/../main.jsbundle.map";  
  WITH_ENVIRONMENT="../node_modules/react-native/scripts/xcode/with-environment.sh"  

```

If done correctly you should see the output location of the source map during Metro build output.

text

```
Writing bundle output to:, Build/Intermediates.noindex/ArchiveIntermediates/application/BuildProductsPath/Release-iphoneos/main.jsbundle  
Writing sourcemap output to:, Build/Intermediates.noindex/ArchiveIntermediates/application/BuildProductsPath/Release-iphoneos/main.jsbundle.map  

```

### Using `metro-symbolicate`[​](#using-metro-symbolicate "Direct link to using-metro-symbolicate")

With source maps being generated, we can now translate our stack traces.

shell

```
# Print usage instructions  
npx metro-symbolicate  
  
# From a file containing the stack trace  
npx metro-symbolicate android/app/build/generated/sourcemaps/react/release/index.android.bundle.map < stacktrace.txt  
  
# From adb logcat (Android)  
adb logcat -d | npx metro-symbolicate android/app/build/generated/sourcemaps/react/release/index.android.bundle.map  

```

### Notes on source maps[​](#notes-on-source-maps "Direct link to Notes on source maps")

* Multiple source maps may be generated by the build process. Make sure to use the one in the location shown in the examples.
* Make sure that the source map you use corresponds to the exact commit of the crashing app. Small changes in source code can cause large differences in offsets.
* If `metro-symbolicate` exits immediately with success, make sure the input comes from a pipe or redirection and not from a terminal.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/debugging-release-builds.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/debugging-release-builds.md)

Last updated on **Apr 14, 2025**

[Previous

Debugging Native Code](/docs/debugging-native-code)[Next

Other Debugging Methods](/docs/other-debugging-methods)

* [Symbolicating a stack trace](#symbolicating-a-stack-trace)
  + [Enabling source maps](#enabling-source-maps)+ [Using `metro-symbolicate`](#using-metro-symbolicate)+ [Notes on source maps](#notes-on-source-maps)

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