Native Platform · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/native-platform)

* [Next](/docs/next/native-platform)* [0.79](/docs/native-platform)* [0.78](/docs/0.78/native-platform)* [0.77](/docs/0.77/native-platform)* [0.76](/docs/0.76/native-platform)* [0.75](/docs/0.75/getting-started)* [0.74](/docs/0.74/getting-started)* [0.73](/docs/0.73/getting-started)* [0.72](/docs/0.72/getting-started)* [0.71](/docs/0.71/getting-started)* [0.70](/docs/0.70/getting-started)* [All versions](/versions)

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

                    + [Introduction](/docs/native-platform)+ Modules

                        - [Android and iOS](/docs/turbo-native-modules-introduction)- [Cross-Platform with C++](/docs/the-new-architecture/pure-cxx-modules)- [Advanced Topics](/docs/the-new-architecture/advanced-topics-modules)+ Components

                          - [Android & iOS](/docs/fabric-native-components-introduction)- [Advanced Topics](/docs/the-new-architecture/advanced-topics-components)+ [Miscellaneous](/docs/appendix)* [Android and iOS guides](/docs/headless-js-android)

                      * [Legacy Architecture](/docs/legacy/native-modules-intro)

Native Platform
===============

Your application may need access to platform features that aren’t directly available from react-native or one of the hundreds of [third-party libraries](https://reactnative.directory/) maintained by the community. Maybe you want to reuse some existing Objective-C, Swift, Java, Kotlin or C++ code from the JavaScript runtime. Whatever your reason, React Native exposes a powerful set of API to connect your native code to your JavaScript application code.

This guide introduces:

* **Native Modules:** native libraries that have no User Interface (UI) for the user. Examples would be persistent storage, notifications, network events. These are accessible to your user as JavaScript functions and objects.
* **Native Component:** native platform views, widgets and controllers that are available to your application's JavaScript code through React Components.

note

You might have previously been familiar with:

* [Legacy Native Modules](/docs/legacy/native-modules-intro);
* [Legacy Native Components](/docs/legacy/native-components-android);

These are our deprecated native module and component API. You can still use many of these legacy libraries with the New Architecture thanks to our interop layers. You should consider:

* using alternative libraries,
* upgrading to newer library versions that have first-class support for the New Architecture, or
* port these libraries yourself to Turbo Native Modules or Fabric Native Components.

1. Native Modules
   * [Android & iOS](/docs/turbo-native-modules-introduction)
   * [Cross-Platform with C++](/docs/the-new-architecture/pure-cxx-modules)
   * [Advanced: Custom C++ Types](/docs/the-new-architecture/custom-cxx-types)
2. Fabric Native Components
   * [Android & iOS](/docs/fabric-native-components-introduction)

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/native-platforms.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/native-platforms.md)

Last updated on **Apr 14, 2025**

[Previous

The Codegen CLI](/docs/the-new-architecture/codegen-cli)[Next

Android and iOS](/docs/turbo-native-modules-introduction)

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