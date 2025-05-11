Native Modules NPM Package Setup · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/legacy/native-modules-setup)

* [Next](/docs/next/legacy/native-modules-setup)* [0.79](/docs/legacy/native-modules-setup)* [0.78](/docs/0.78/legacy/native-modules-setup)* [0.77](/docs/0.77/legacy/native-modules-setup)* [0.76](/docs/0.76/legacy/native-modules-setup)* [0.75](/docs/0.75/getting-started)* [0.74](/docs/0.74/getting-started)* [0.73](/docs/0.73/getting-started)* [0.72](/docs/0.72/getting-started)* [0.71](/docs/0.71/getting-started)* [0.70](/docs/0.70/getting-started)* [All versions](/versions)

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

Native Modules NPM Package Setup
================================

info

Native Module and Native Components are our stable technologies used by the legacy architecture.
They will be deprecated in the future when the New Architecture will be stable. The New Architecture uses [Turbo Native Module](https://github.com/reactwg/react-native-new-architecture/blob/main/docs/turbo-modules.md) and [Fabric Native Components](https://github.com/reactwg/react-native-new-architecture/blob/main/docs/fabric-native-components.md) to achieve similar results.

Native modules are usually distributed as npm packages, except that on top of the usual JavaScript they will include some native code per platform. To understand more about npm packages you may find [this guide](https://docs.npmjs.com/packages-and-modules/contributing-packages-to-the-registry) useful.

To get set up with the basic project structure for a native module we will use the community tool called [create-react-native-library](https://callstack.github.io/react-native-builder-bob/create). You can go ahead further and dive deep into how that library works, but for our needs we will only execute the basic script:

shell

```
npx create-react-native-library@latest react-native-awesome-module  

```

Where `react-native-awesome-module` is the name you would like for the new module. After doing this you will navigate into `react-native-awesome-module` folder and bootstrap the example project by running:

shell

```
yarn  

```

When the bootstrap is done, you will be able to start the example app by executing one of the following commands:

shell

```
# Android app  
yarn example android  
# iOS app  
yarn example ios  

```

When all steps above are done, you will be able to continue with [Android Native Modules](/docs/legacy/native-modules-android) or [iOS Native Modules](/docs/legacy/native-modules-ios) guides to add in some code.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/legacy/native-modules-setup.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/legacy/native-modules-setup.md)

Last updated on **Apr 14, 2025**

[Previous

iOS Native Modules](/docs/legacy/native-modules-ios)[Next

Local libraries setup](/docs/legacy/local-library-setup)

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