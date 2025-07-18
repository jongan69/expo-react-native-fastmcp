Glossary · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [Architecture](/architecture/overview)

  + [Architecture Overview](/architecture/overview)+ [About the New Architecture](/architecture/landing-page)+ Rendering

        - [Fabric](/architecture/fabric-renderer)- [Render, Commit, and Mount](/architecture/render-pipeline)- [Cross Platform Implementation](/architecture/xplat-implementation)- [View Flattening](/architecture/view-flattening)- [Threading Model](/architecture/threading-model)+ Build Tools

          - [Bundled Hermes](/architecture/bundled-hermes)+ [Glossary](/architecture/glossary)

On this page

Glossary
========

Dev Menu[​](#dev-menu "Direct link to Dev Menu")
------------------------------------------------

The in-app developer menu (available in development builds) that offers access to various development and debugging actions. [Learn more about the Dev Menu in the docs](/docs/debugging).

Fabric Renderer[​](#fabric-renderer "Direct link to Fabric Renderer")
---------------------------------------------------------------------

React Native executes the same React framework code as React for the web. However, React Native renders to general platform views (host views) instead of DOM nodes (which can be considered web’s host views). Rendering to host views is made possible by the Fabric Renderer. Fabric lets React talk to each platform and manage its host view instances. The Fabric Renderer exists in JavaScript and targets interfaces made available by C++ code. [Read more about React renderers in this blog post.](https://overreacted.io/react-as-a-ui-runtime/#renderers)

Host platform[​](#host-platform "Direct link to Host platform")
---------------------------------------------------------------

The platform embedding React Native (e.g., Android, iOS, macOS, Windows).

Host View Tree (and Host View)[​](#host-view-tree-and-host-view "Direct link to Host View Tree (and Host View)")
----------------------------------------------------------------------------------------------------------------

Tree representation of views in the host platform (e.g. Android, iOS). On Android, the host views are instances of `android.view.ViewGroup`, `android.widget.TextView`, etc. which are the building blocks of the host view tree. The size and location of each host view are based on `LayoutMetrics` calculated with Yoga, and the style and content of each host view are based on information from the React Shadow Tree.

JavaScript Interfaces (JSI)[​](#javascript-interfaces-jsi "Direct link to JavaScript Interfaces (JSI)")
-------------------------------------------------------------------------------------------------------

A lightweight API to embed a JavaScript engine in a C++ application. Fabric uses it to communicate between Fabric’s C++ core and React.

Java Native Interface (JNI)[​](#java-native-interface-jni "Direct link to Java Native Interface (JNI)")
-------------------------------------------------------------------------------------------------------

An [API to write Java native methods](https://docs.oracle.com/javase/8/docs/technotes/guides/jni/) used to communicate between Fabric’s C++ core and Android, written in Java.

React Component[​](#react-component "Direct link to React Component")
---------------------------------------------------------------------

A JavaScript function or class that instructs how to create a React Element. [Read more about React components, elements in this blog post.](https://reactjs.org/blog/2015/12/18/react-components-elements-and-instances.html)

React Composite Components[​](#react-composite-components "Direct link to React Composite Components")
------------------------------------------------------------------------------------------------------

React Components with `render` implementations that reduce to other React Composite Components or React Host Components.

React Host Components or Host Components[​](#react-host-components-or-host-components "Direct link to React Host Components or Host Components")
------------------------------------------------------------------------------------------------------------------------------------------------

React Components whose view implementation is provided by a host view (e.g., `<View>, <Text>` ). On the Web, ReactDOM's Host components would be components like `<p>` and `<div>`.

React Element Tree (and React Element)[​](#react-element-tree-and-react-element "Direct link to React Element Tree (and React Element)")
----------------------------------------------------------------------------------------------------------------------------------------

A *React Element Tree* is created by React in JavaScript and consists of React Elements. A *React Element* is a plain JavaScript object that describes what should appear on the screen. It includes props, styles, and children. React Elements only exist in JavaScript and can represent instantiations of either React Composite Components or React Host Components. [Read more about React components and elements in this blog post.](https://reactjs.org/blog/2015/12/18/react-components-elements-and-instances.html)

React Native Framework[​](#react-native-framework "Direct link to React Native Framework")
------------------------------------------------------------------------------------------

React Native allows developers to use the [React programming paradigm](https://react.dev/learn/thinking-in-react) to ship applications to native targets. The React Native team is focused on creating **core APIs** and **functionalities** that fit the most general use case when developing native apps.

Shipping native apps to production usually requires a set of tools and libraries that are not provided by default as part of React Native, but are still crucial to ship an app to production. Examples of such tools are: support for publishing applications to a dedicated store or support for routing and navigation mechanisms.

When those tools and libraries are collected to form a cohesive framework built on top of React Native, we define it as a **React Native Framework**.

An example of Open Source React Native Framework is [Expo](https://expo.dev/).

React Shadow Tree (and React Shadow Node)[​](#react-shadow-tree-and-react-shadow-node "Direct link to React Shadow Tree (and React Shadow Node)")
-------------------------------------------------------------------------------------------------------------------------------------------------

A *React Shadow Tree* is created by the Fabric Renderer and consists of React Shadow Nodes. A React Shadow Node is an object that represents a React Host Component to be mounted, and contains props that originate from JavaScript. They also contain layout information (x, y, width, height). In Fabric, React Shadow Node objects exist in C++. Before Fabric, these existed in the mobile runtime heap (e.g. Android JVM).

Yoga Tree (and Yoga Node)[​](#yoga-tree-and-yoga-node "Direct link to Yoga Tree (and Yoga Node)")
-------------------------------------------------------------------------------------------------

The *Yoga Tree* is used by [Yoga](https://www.yogalayout.dev/) to calculate layout information for a React Shadow Tree. Each React Shadow Node typically creates a *Yoga Node* because React Native employs Yoga to calculate layout. However, this is not a hard requirement. Fabric can also create React Shadow Nodes that do not use Yoga; the implementation of each React Shadow Node determines how to calculate layout.

[Edit this page](https://github.com/facebook/react-native-website/edit/main/docs/architecture-glossary.md)

Last updated on **May 14, 2024**

[Previous

Bundled Hermes](/architecture/bundled-hermes)

* [Dev Menu](#dev-menu)* [Fabric Renderer](#fabric-renderer)* [Host platform](#host-platform)* [Host View Tree (and Host View)](#host-view-tree-and-host-view)* [JavaScript Interfaces (JSI)](#javascript-interfaces-jsi)* [Java Native Interface (JNI)](#java-native-interface-jni)* [React Component](#react-component)* [React Composite Components](#react-composite-components)* [React Host Components or Host Components](#react-host-components-or-host-components)* [React Element Tree (and React Element)](#react-element-tree-and-react-element)* [React Native Framework](#react-native-framework)* [React Shadow Tree (and React Shadow Node)](#react-shadow-tree-and-react-shadow-node)* [Yoga Tree (and Yoga Node)](#yoga-tree-and-yoga-node)

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