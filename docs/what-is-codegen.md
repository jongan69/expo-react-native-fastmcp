What is Codegen? · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/the-new-architecture/what-is-codegen)

* [Next](/docs/next/the-new-architecture/what-is-codegen)* [0.79](/docs/the-new-architecture/what-is-codegen)* [0.78](/docs/0.78/the-new-architecture/what-is-codegen)* [0.77](/docs/0.77/the-new-architecture/what-is-codegen)* [0.76](/docs/0.76/the-new-architecture/what-is-codegen)* [0.75](/docs/0.75/getting-started)* [0.74](/docs/0.74/getting-started)* [0.73](/docs/0.73/getting-started)* [0.72](/docs/0.72/getting-started)* [0.71](/docs/0.71/getting-started)* [0.70](/docs/0.70/getting-started)* [All versions](/versions)

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

                  + [What is Codegen?](/docs/the-new-architecture/what-is-codegen)+ [Using Codegen](/docs/the-new-architecture/using-codegen)+ [The Codegen CLI](/docs/the-new-architecture/codegen-cli)* [Native Development](/docs/native-platform)

                    * [Android and iOS guides](/docs/headless-js-android)

                      * [Legacy Architecture](/docs/legacy/native-modules-intro)

On this page

What is Codegen?
================

**Codegen** is a tool to avoid writing a lot of repetitive code. Using Codegen **is not mandatory**: you can write all the generated manually. However, **Codegen** generates scaffolding code that could save you a lot of time.

React Native invokes **Codegen** automatically every time an iOS or Android app is built. Occasionally, you would like to manually run the **Codegen** scripts to know which types and files are actually generated: this is a common scenario when developing Turbo Native Modules and Fabric Native Components.

How does Codegen works[​](#how-does-codegen-works "Direct link to How does Codegen works")
------------------------------------------------------------------------------------------

**Codegen** is a process that is tightly coupled with a React Native app. The **Codegen** scripts live inside the `react-native` NPM package and the apps call those scripts at build time.

**Codegen** crawls the folders in your project, starting from a directory you specify in your `package.json`, looking for some specific JS files that contains the specification (or specs) for your custom modules and components. Spec files are JS files written in a typed dialect: React Native currently supports Flow and TypeScript.

Every time **Codegen** finds a spec file, it generates the boilerplate code associated to it. **Codegen** generates some C++ glue-code and then it generates platform-specific code, using Java for Android and Objective-C++ for iOS.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/the-new-architecture/what-is-codegen.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/the-new-architecture/what-is-codegen.md)

Last updated on **Apr 14, 2025**

[Previous

Using Hermes](/docs/hermes)[Next

Using Codegen](/docs/the-new-architecture/using-codegen)

* [How does Codegen works](#how-does-codegen-works)

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