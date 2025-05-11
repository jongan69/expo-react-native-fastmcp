React 18 & React Native · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.75](/docs/0.75/react-18-and-react-native)

* [Next](/docs/next/getting-started)* [0.79](/docs/getting-started)* [0.78](/docs/0.78/getting-started)* [0.77](/docs/0.77/getting-started)* [0.76](/docs/0.76/getting-started)* [0.75](/docs/0.75/react-18-and-react-native)* [0.74](/docs/0.74/react-18-and-react-native)* [0.73](/docs/0.73/react-18-and-react-native)* [0.72](/docs/0.72/react-18-and-react-native)* [0.71](/docs/0.71/react-18-and-react-native)* [0.70](/docs/0.70/react-18-and-react-native)* [All versions](/versions)

[Development](#)

* [Guides](/docs/0.75/getting-started)* [Components](/docs/0.75/components-and-apis)* [APIs](/docs/0.75/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

This is documentation for React Native **0.75**, which is no longer in active development.

For up-to-date documentation, see the **[latest version](/docs/getting-started)** (0.79).

Version: 0.75

On this page

React 18 & React Native
=======================

caution

This documentation is still **experimental** and details are subject to changes as we iterate. Feel free to share your feedback on the [discussion inside the working group](https://github.com/reactwg/react-native-new-architecture/discussions/8) for this page.

Moreover, it contains several **manual steps**. Please note that this won't be representative of the final developer experience once the New Architecture is stable. We're working on tools, templates and libraries to help you get started fast on the New Architecture, without having to go through the whole setup.

This page describes how to use React 18 with React Native using the React Native's New Architecture.

> **tl;dr:** The first version of React Native compatible with React 18 is **0.69.0**. In order to use the new features in React 18 including automatic batching, `startTransition`, and `useDeferredValue`, you must migrate your React Native app to the New Architecture.

React 18 and the React Native New Architecture[​](#react-18-and-the-react-native-new-architecture "Direct link to React 18 and the React Native New Architecture")
------------------------------------------------------------------------------------------------------------------------------------------------------------------

React 18 introduces [several new features](https://reactjs.org/blog/2022/03/29/react-v18.html) including:

* Automatic batching
* New Strict Mode behaviors
* New hooks (`useId`, `useSyncExternalStore`)

It also includes new concurrent features:

* `startTransition`
* `useTransition`
* `useDeferredValue`
* Full Suspense support

The concurrent features in React 18 are built on top of the new concurrent rendering engine. Concurrent rendering is a new behind-the-scenes mechanism that enables React to prepare multiple versions of your UI at the same time.

Previous versions of React Native built on the old architecture **cannot** support concurrent rendering or concurrent features. This is because the old architecture relied on mutating the native trees, which doesn’t allow for React to prepare multiple versions of the tree at the same time.

Fortunately, the New Architecture was written bottom-up with concurrent rendering in mind, and is fully compatible with React 18. This means, in order to upgrade to React 18 in your React Native app, your application **needs to use the React Native's New Architecture** including Fabric Native Components and Turbo Native Modules.

This means you’re able to use the new features in React 18 as soon as flip the New Architecture switch. Since the new concurrent features are opt-in by using features like `startTransition` or `Suspense`, we expect React 18 to work out-of-the-box with minimal changes for users who migrate to the New Architecture or create a new app with the New Architecture enabled.

### Note for the Old Architecture users[​](#note-for-the-old-architecture-users "Direct link to Note for the Old Architecture users")

Apps that are still on the Old Architecture will use React 17 mode even if React 18 is listed as a dependency in the `package.json` file.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/react-18-and-react-native.md)[Edit page for 0.75 release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.75/react-18-and-react-native.md)

Last updated on **Aug 15, 2024**

* [React 18 and the React Native New Architecture](#react-18-and-the-react-native-new-architecture)
  + [Note for the Old Architecture users](#note-for-the-old-architecture-users)

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