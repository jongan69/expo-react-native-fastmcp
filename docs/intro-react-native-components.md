Core Components and Native Components · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/intro-react-native-components)

* [Next](/docs/next/intro-react-native-components)* [0.79](/docs/intro-react-native-components)* [0.78](/docs/0.78/intro-react-native-components)* [0.77](/docs/0.77/intro-react-native-components)* [0.76](/docs/0.76/intro-react-native-components)* [0.75](/docs/0.75/intro-react-native-components)* [0.74](/docs/0.74/intro-react-native-components)* [0.73](/docs/0.73/intro-react-native-components)* [0.72](/docs/0.72/intro-react-native-components)* [0.71](/docs/0.71/intro-react-native-components)* [0.70](/docs/0.70/intro-react-native-components)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [The Basics](/docs/getting-started)

  + [Introduction](/docs/getting-started)+ [Core Components and Native Components](/docs/intro-react-native-components)+ [React Fundamentals](/docs/intro-react)+ [Handling Text Input](/docs/handling-text-input)+ [Using a ScrollView](/docs/using-a-scrollview)+ [Using List Views](/docs/using-a-listview)+ [Troubleshooting](/docs/troubleshooting)+ [Platform-Specific Code](/docs/platform-specific-code)+ [More Resources](/docs/more-resources)* [Environment setup](/docs/environment-setup)

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

On this page

Core Components and Native Components
=====================================

React Native is an open source framework for building Android and iOS applications using [React](https://reactjs.org/) and the app platform’s native capabilities. With React Native, you use JavaScript to access your platform’s APIs as well as to describe the appearance and behavior of your UI using React components: bundles of reusable, nestable code. You can learn more about React in the next section. But first, let’s cover how components work in React Native.

Views and mobile development[​](#views-and-mobile-development "Direct link to Views and mobile development")
------------------------------------------------------------------------------------------------------------

In Android and iOS development, a **view** is the basic building block of UI: a small rectangular element on the screen which can be used to display text, images, or respond to user input. Even the smallest visual elements of an app, like a line of text or a button, are kinds of views. Some kinds of views can contain other views. It’s views all the way down!

![Diagram of Android and iOS app showing them both built on top of atomic elements called views.](/docs/assets/diagram_ios-android-views.svg)

Just a sampling of the many views used in Android and iOS apps.

Native Components[​](#native-components "Direct link to Native Components")
---------------------------------------------------------------------------

In Android development, you write views in Kotlin or Java; in iOS development, you use Swift or Objective-C. With React Native, you can invoke these views with JavaScript using React components. At runtime, React Native creates the corresponding Android and iOS views for those components. Because React Native components are backed by the same views as Android and iOS, React Native apps look, feel, and perform like any other apps. We call these platform-backed components **Native Components.**

React Native comes with a set of essential, ready-to-use Native Components you can use to start building your app today. These are React Native's **Core Components**.

caution

This documentation references a legacy set of API and needs to be updated to reflect the New Architecture

React Native also lets you build your own Native Components for [Android](/docs/legacy/native-components-android) and [iOS](/docs/legacy/native-components-ios) to suit your app’s unique needs. We also have a thriving ecosystem of these **community-contributed components.** Check out [Native Directory](https://reactnative.directory) to find what the community has been creating.

Core Components[​](#core-components "Direct link to Core Components")
---------------------------------------------------------------------

React Native has many Core Components for everything from controls to activity indicators. You can find them all [documented in the API section](/docs/components-and-apis). You will mostly work with the following Core Components:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| React Native UI Component Android View iOS View Web Analog Description|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `<View>` `<ViewGroup>` `<UIView>` A non-scrolling `<div>` A container that supports layout with flexbox, style, some touch handling, and accessibility controls|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `<Text>` `<TextView>` `<UITextView>` `<p>` Displays, styles, and nests strings of text and even handles touch events|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `<Image>` `<ImageView>` `<UIImageView>` `<img>` Displays different types of images|  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `<ScrollView>` `<ScrollView>` `<UIScrollView>` `<div>` A generic scrolling container that can contain multiple components and views|  |  |  |  |  | | --- | --- | --- | --- | --- | | `<TextInput>` `<EditText>` `<UITextField>` `<input type="text">` Allows the user to enter text | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

In the next section, you will start combining these Core Components to learn about how React works. Have a play with them here now!

---

Because React Native uses the same API structure as React components, you’ll need to understand React component APIs to get started. The [next section](/docs/intro-react) makes for a quick introduction or refresher on the topic. However, if you’re already familiar with React, feel free to [skip ahead](/docs/handling-text-input).

![A diagram showing React Native's Core Components are a subset of React Components that ship with React Native.](/docs/assets/diagram_react-native-components.svg)![A diagram showing React Native's Core Components are a subset of React Components that ship with React Native.](/docs/assets/diagram_react-native-components_dark.svg)

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/intro-react-native-components.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/intro-react-native-components.md)

Last updated on **Apr 14, 2025**

[Previous

Introduction](/docs/getting-started)[Next

React Fundamentals](/docs/intro-react)

* [Views and mobile development](#views-and-mobile-development)* [Native Components](#native-components)* [Core Components](#core-components)

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