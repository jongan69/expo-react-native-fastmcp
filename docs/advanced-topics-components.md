Advanced Topics on Native Modules Development · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/the-new-architecture/advanced-topics-components)

* [Next](/docs/next/the-new-architecture/advanced-topics-components)* [0.79](/docs/the-new-architecture/advanced-topics-components)* [0.78](/docs/0.78/getting-started)* [0.77](/docs/0.77/getting-started)* [0.76](/docs/0.76/getting-started)* [0.75](/docs/0.75/getting-started)* [0.74](/docs/0.74/getting-started)* [0.73](/docs/0.73/getting-started)* [0.72](/docs/0.72/getting-started)* [0.71](/docs/0.71/getting-started)* [0.70](/docs/0.70/getting-started)* [All versions](/versions)

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

Advanced Topics on Native Modules Development
=============================================

This document contains a set of advanced topics to implement more complex functionalities of Native Components. It is recommended to first read the [Codegen](/docs/the-new-architecture/what-is-codegen) section and the guides on [Native Components](/docs/fabric-native-components-introduction).

This guide will cover the following topics:

* [Direct Manipulation](/docs/the-new-architecture/direct-manipulation-new-architecture)
* [Measuring the Layout](/docs/the-new-architecture/layout-measurements)
* [Invoking native functions on your native component](/docs/next/the-new-architecture/fabric-component-native-commands)

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/the-new-architecture/advanced-topics-components.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/the-new-architecture/advanced-topics-components.md)

Last updated on **Apr 14, 2025**

[Previous

Android & iOS](/docs/fabric-native-components-introduction)[Next

Appendix](/docs/appendix)

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