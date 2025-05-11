Source Maps · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.72](/docs/0.72/sourcemaps)

* [Next](/docs/next/getting-started)* [0.79](/docs/getting-started)* [0.78](/docs/0.78/getting-started)* [0.77](/docs/0.77/getting-started)* [0.76](/docs/0.76/getting-started)* [0.75](/docs/0.75/getting-started)* [0.74](/docs/0.74/getting-started)* [0.73](/docs/0.73/getting-started)* [0.72](/docs/0.72/sourcemaps)* [0.71](/docs/0.71/sourcemaps)* [0.70](/docs/0.70/getting-started)* [All versions](/versions)

[Development](#)

* [Guides](/docs/0.72/getting-started)* [Components](/docs/0.72/components-and-apis)* [APIs](/docs/0.72/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [The Basics](/docs/0.72/getting-started)

  * [Environment setup](/docs/0.72/environment-setup)

    * [Workflow](/docs/0.72/running-on-device)

      + [Running On Device](/docs/0.72/running-on-device)+ [Fast Refresh](/docs/0.72/fast-refresh)+ [Metro](/docs/0.72/metro)+ [Symbolicating a stack trace](/docs/0.72/symbolication)+ [Source Maps](/docs/0.72/sourcemaps)+ [Using Libraries](/docs/0.72/libraries)+ [Using TypeScript](/docs/0.72/typescript)+ [Upgrading to new versions](/docs/0.72/upgrading)* [UI & Interaction](/docs/0.72/style)

        * [Debugging](/docs/0.72/debugging)

          * [Testing](/docs/0.72/testing-overview)

            * [Performance](/docs/0.72/performance)

              * [JavaScript Runtime](/docs/0.72/javascript-environment)

                * [Native Modules](/docs/0.72/native-modules-intro)

                  * [Native Components](/docs/0.72/native-components-android)

                    * [Android and iOS guides](/docs/0.72/headless-js-android)

                      * [Experimental](/docs/0.72/the-new-architecture/landing-page)

This is documentation for React Native **0.72**, which is no longer in active development.

For up-to-date documentation, see the **[latest version](/docs/getting-started)** (0.79).

Version: 0.72

On this page

Source Maps
===========

Source maps allow you to map a transformed file back to the original source file. The main purpose of source maps is to aid debugging and help with investigating issues from release builds.

Without the source maps, when running into an error in the release build you will see a stacktrace like:

text

```
TypeError: Cannot read property 'data' of undefined  
  at anonymous(app:///index.android.bundle:1:4277021)  
  at call(native)  
  at p(app:///index.android.bundle:1:227785)  

```

With source maps generated, a stacktrace will include path, file name, and line number of the original source file:

text

```
TypeError: Cannot read property 'data' of undefined  
  at anonymous(src/modules/notifications/Permission.js:15:requestNotificationPermission)  
  at call(native)  
  at p(node_modules/regenerator-runtime/runtime.js:64:Generator)  

```

This allows you to triage release issues using a decipherable stacktrace.

Follow the instructions below to get started with source maps.

Enable source maps on Android[​](#enable-source-maps-on-android "Direct link to Enable source maps on Android")
---------------------------------------------------------------------------------------------------------------

### Hermes[​](#hermes "Direct link to Hermes")

info

Source maps are built in Release mode by default, unless `hermesFlagsRelease` is set. In that case source maps will have to be enabled.

To do so, ensure the following is set in your app's `android/app/build.gradle` file.

groovy

```
project.ext.react = [  
    enableHermes: true,  
    hermesFlagsRelease: ["-O", "-output-source-map"], // plus whichever flag was required to set this away from default  
]  

```

If done correctly you should see the output location of the source map during Metro build output.

text

```
Writing bundle output to:, android/app/build/generated/assets/react/release/index.android.bundle  
Writing sourcemap output to:, android/app/build/intermediates/sourcemaps/react/release/index.android.bundle.packager.map  

```

Development builds do not produce a bundle and thus already have symbols, but if the development build is bundled you may use `hermesFlagsDebug` like above to enable source maps.

Enable source maps on iOS[​](#enable-source-maps-on-ios "Direct link to Enable source maps on iOS")
---------------------------------------------------------------------------------------------------

Source maps are disabled by default. To enable them one has to define a `SOURCEMAP_FILE` environment variable.

In order to do so, within Xcode head to the Build Phase - "Bundle React Native code and images".

At the top of the file near the other exports, add an entry for `SOURCEMAP_FILE` to the preferred location and name. Like below:

```
export SOURCEMAP_FILE="$(pwd)/../main.jsbundle.map";  
  
export NODE_BINARY=node  
../node_modules/react-native/scripts/react-native-xcode.sh  

```

If done correctly you should see the output location of the source map during Metro build output.

text

```
Writing bundle output to:, Build/Intermediates.noindex/ArchiveIntermediates/application/BuildProductsPath/Release-iphoneos/main.jsbundle  
Writing sourcemap output to:, Build/Intermediates.noindex/ArchiveIntermediates/application/BuildProductsPath/Release-iphoneos/main.jsbundle.map  

```

Manual Symbolication[​](#manual-symbolication "Direct link to Manual Symbolication")
------------------------------------------------------------------------------------

info

You may read about manual symbolication of a stack trace on the [symbolication](/docs/0.72/symbolication) page.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/sourcemaps.md)[Edit page for 0.72 release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.72/sourcemaps.md)

Last updated on **Jun 21, 2023**

[Previous

Symbolicating a stack trace](/docs/0.72/symbolication)[Next

Using Libraries](/docs/0.72/libraries)

* [Enable source maps on Android](#enable-source-maps-on-android)
  + [Hermes](#hermes)* [Enable source maps on iOS](#enable-source-maps-on-ios)* [Manual Symbolication](#manual-symbolication)

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