Native Modules Intro · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/legacy/native-modules-intro)

* [Next](/docs/next/legacy/native-modules-intro)* [0.79](/docs/legacy/native-modules-intro)* [0.78](/docs/0.78/legacy/native-modules-intro)* [0.77](/docs/0.77/legacy/native-modules-intro)* [0.76](/docs/0.76/legacy/native-modules-intro)* [0.75](/docs/0.75/getting-started)* [0.74](/docs/0.74/getting-started)* [0.73](/docs/0.73/getting-started)* [0.72](/docs/0.72/getting-started)* [0.71](/docs/0.71/getting-started)* [0.70](/docs/0.70/getting-started)* [All versions](/versions)

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

                      * [Legacy Architecture](/docs/legacy/native-modules-intro)

                        + [Native Modules](/docs/legacy/native-modules-intro)

                          - [Native Modules Intro](/docs/legacy/native-modules-intro)- [Android Native Modules](/docs/legacy/native-modules-android)- [iOS Native Modules](/docs/legacy/native-modules-ios)- [Native Modules NPM Package Setup](/docs/legacy/native-modules-setup)- [Local libraries setup](/docs/legacy/local-library-setup)+ [Native Components](/docs/legacy/native-components-android)

On this page

Native Modules Intro
====================

info

Native Module and Native Components are our stable technologies used by the legacy architecture.
They will be deprecated in the future when the New Architecture will be stable. The New Architecture uses [Turbo Native Module](https://github.com/reactwg/react-native-new-architecture/blob/main/docs/turbo-modules.md) and [Fabric Native Components](https://github.com/reactwg/react-native-new-architecture/blob/main/docs/fabric-native-components.md) to achieve similar results.

Sometimes a React Native app needs to access a native platform API that is not available by default in JavaScript, for example the native APIs to access Apple or Google Pay. Maybe you want to reuse some existing Objective-C, Swift, Java or C++ libraries without having to reimplement it in JavaScript, or write some high performance, multi-threaded code for things like image processing.

The NativeModule system exposes instances of Java/Objective-C/C++ (native) classes to JavaScript (JS) as JS objects, thereby allowing you to execute arbitrary native code from within JS. While we don't expect this feature to be part of the usual development process, it is essential that it exists. If React Native doesn't export a native API that your JS app needs you should be able to export it yourself!

Native Module Setup[​](#native-module-setup "Direct link to Native Module Setup")
---------------------------------------------------------------------------------

There are different ways to write a native module for your React Native application:

1. Creating a local library that can be imported in your React Native application. Read [Creating local libraries](/docs/legacy/local-library-setup) guide to learn more.
2. Directly within your React Native application's iOS/Android projects
3. As an NPM package that can be installed as a dependency by your/other React Native applications.

This guide will first walk you through implementing a native module directly within a React Native application. However the native module you build in the following guide can be distributed as an NPM package. Check out the [Setting Up a Native Module as an NPM Package](/docs/legacy/native-modules-setup) guide if you are interested in doing so.

Getting Started[​](#getting-started "Direct link to Getting Started")
---------------------------------------------------------------------

In the following sections we will walk you through guides on how to build a native module directly within a React Native application. As a prerequisite, you will need a React Native application to work within. You can follow the steps [here](/docs/getting-started) to setup a React Native application if you do not already have one.

Imagine that you want to access the iOS/Android native calendar APIs from JavaScript within a React Native application in order to create calendar events. React Native does not expose a JavaScript API to communicate with the native calendar libraries. However, through native modules, you can write native code that communicates with native calendar APIs. Then you can invoke that native code through JavaScript in your React Native application.

In the following sections you will create such a Calendar native module for both [Android](/docs/legacy/native-modules-android) and [iOS](/docs/legacy/native-modules-ios).

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/legacy/native-modules-intro.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/legacy/native-modules-intro.md)

Last updated on **Apr 14, 2025**

[Previous

Publishing to Apple App Store](/docs/publishing-to-app-store)[Next

Android Native Modules](/docs/legacy/native-modules-android)

* [Native Module Setup](#native-module-setup)* [Getting Started](#getting-started)

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