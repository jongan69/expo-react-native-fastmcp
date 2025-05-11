Appendix · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/appendix)

* [Next](/docs/next/appendix)* [0.79](/docs/appendix)* [0.78](/docs/0.78/appendix)* [0.77](/docs/0.77/appendix)* [0.76](/docs/0.76/appendix)* [0.75](/docs/0.75/getting-started)* [0.74](/docs/0.74/getting-started)* [0.73](/docs/0.73/getting-started)* [0.72](/docs/0.72/getting-started)* [0.71](/docs/0.71/getting-started)* [0.70](/docs/0.70/getting-started)* [All versions](/versions)

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

                          - [Android & iOS](/docs/fabric-native-components-introduction)- [Advanced Topics](/docs/the-new-architecture/advanced-topics-components)+ [Miscellaneous](/docs/appendix)

                            - [Appendix](/docs/appendix)- [Create a Library for Your Module](/docs/the-new-architecture/create-module-library)* [Android and iOS guides](/docs/headless-js-android)

                      * [Legacy Architecture](/docs/legacy/native-modules-intro)

On this page

Appendix
========

I. Terminology[​](#i-terminology "Direct link to I. Terminology")
-----------------------------------------------------------------

* **Spec** - TypeScript or Flow code that describes the API for a Turbo Native Module or Fabric Native component. Used by **Codegen** to generate boilerplate code.
* **Native Modules** - Native libraries that have no User Interface (UI) for the user. Examples would be persistent storage, notifications, network events. These are accessible to your JavaScript application code as functions and objects.
* **Native Component** - Native platform views that are available to your application JavaScript code through React Components.
* **Legacy Native Components** - Components which are running on the old React Native architecture.
* **Legacy Native Modules** - Modules which are running on the old React Native architecture.

II. Codegen Typings[​](#ii-codegen-typings "Direct link to II. Codegen Typings")
--------------------------------------------------------------------------------

You may use the following table as a reference for which types are supported and what they map to in each platform:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Flow TypeScript Flow Nullable Support TypeScript Nullable Support Android (Java) iOS (ObjC)|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `string` `string` `?string` `string | null` `string` `NSString`| `boolean` `boolean` `?boolean` `boolean | null` `Boolean` `NSNumber`| Object Literal `{| foo: string, ...|}` `{ foo: string, ...} as const` `?{| foo: string, ...|}` `?{ foo: string, ...} as const` - -|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Object [[1](#notes)] Object [[1](#notes)] `?Object` `Object | null` `ReadableMap` `@` (untyped dictionary)| `Array<T>` `Array<T>` `?Array<T>` `Array<T> | null` `ReadableArray` `NSArray` (or `RCTConvertVecToArray` when used inside objects)| `Function` `Function` `?Function` `Function | null` - -|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `Promise<T>` `Promise<T>` `?Promise<T>` `Promise<T> | null` `com.facebook.react.bridge.Promise` `RCTPromiseResolve` and `RCTPromiseRejectBlock`| Type Unions `'SUCCESS'|'FAIL'` Type Unions `'SUCCESS'|'FAIL'` Only as callbacks - -|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Callbacks `() =>` Callbacks `() =>` Yes `com.facebook.react.bridge.Callback` `RCTResponseSenderBlock`| `number` `number` No `double` `NSNumber` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

### Notes:[​](#notes "Direct link to Notes:")

**[1]** We strongly recommend using Object literals instead of Objects.

info

You may also find it useful to refer to the JavaScript specifications for the core modules in React Native. These are located inside the `Libraries/` directory in the React Native repository.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/appendix.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/appendix.md)

Last updated on **Apr 14, 2025**

[Previous

Advanced Topics](/docs/the-new-architecture/advanced-topics-components)[Next

Create a Library for Your Module](/docs/the-new-architecture/create-module-library)

* [I. Terminology](#i-terminology)* [II. Codegen Typings](#ii-codegen-typings)
    + [Notes:](#notes)

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