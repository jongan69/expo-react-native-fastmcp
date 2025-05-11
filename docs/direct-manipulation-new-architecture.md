Direct Manipulation · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/the-new-architecture/direct-manipulation-new-architecture)

* [Next](/docs/next/the-new-architecture/direct-manipulation-new-architecture)* [0.79](/docs/the-new-architecture/direct-manipulation-new-architecture)* [0.78](/docs/0.78/the-new-architecture/direct-manipulation-new-architecture)* [0.77](/docs/0.77/the-new-architecture/direct-manipulation-new-architecture)* [0.76](/docs/0.76/the-new-architecture/direct-manipulation-new-architecture)* [0.75](/docs/0.75/getting-started)* [0.74](/docs/0.74/getting-started)* [0.73](/docs/0.73/getting-started)* [0.72](/docs/0.72/getting-started)* [0.71](/docs/0.71/getting-started)* [0.70](/docs/0.70/getting-started)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

On this page

Direct Manipulation
===================

It is sometimes necessary to make changes directly to a component without using state/props to trigger a re-render of the entire subtree. When using React in the browser for example, you sometimes need to directly modify a DOM node, and the same is true for views in mobile apps. `setNativeProps` is the React Native equivalent to setting properties directly on a DOM node.

caution

Use `setNativeProps` when frequent re-rendering creates a performance bottleneck!

Direct manipulation will not be a tool that you reach for frequently. You will typically only be using it for creating continuous animations to avoid the overhead of rendering the component hierarchy and reconciling many views.
`setNativeProps` is imperative and stores state in the native layer (DOM, UIView, etc.) and not within your React components, which makes your code more difficult to reason about.

Before you use it, try to solve your problem with `setState` and [`shouldComponentUpdate`](https://reactjs.org/docs/optimizing-performance.html#shouldcomponentupdate-in-action).

setNativeProps to edit TextInput value[​](#setnativeprops-to-edit-textinput-value "Direct link to setNativeProps to edit TextInput value")
------------------------------------------------------------------------------------------------------------------------------------------

Another very common use case of `setNativeProps` is to edit the value of the TextInput. The `controlled` prop of TextInput can sometimes drop characters when the `bufferDelay` is low and the user types very quickly. Some developers prefer to skip this prop entirely and instead use `setNativeProps` to directly manipulate the TextInput value when necessary.

For example, the following code demonstrates editing the input when you tap a button:

* TypeScript* JavaScript

You can use the [`clear`](/docs/textinput#clear) method to clear the `TextInput` which clears the current input text using the same approach.

Avoiding conflicts with the render function[​](#avoiding-conflicts-with-the-render-function "Direct link to Avoiding conflicts with the render function")
---------------------------------------------------------------------------------------------------------------------------------------------------------

If you update a property that is also managed by the render function, you might end up with some unpredictable and confusing bugs because anytime the component re-renders and that property changes, whatever value was previously set from `setNativeProps` will be completely ignored and overridden.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/the-new-architecture/direct-manipulation.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/the-new-architecture/direct-manipulation.md)

Last updated on **Apr 14, 2025**

* [setNativeProps to edit TextInput value](#setnativeprops-to-edit-textinput-value)* [Avoiding conflicts with the render function](#avoiding-conflicts-with-the-render-function)

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