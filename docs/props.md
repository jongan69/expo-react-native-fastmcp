Props · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/props)

* [Next](/docs/next/props)* [0.79](/docs/props)* [0.78](/docs/0.78/props)* [0.77](/docs/0.77/props)* [0.76](/docs/0.76/props)* [0.75](/docs/0.75/props)* [0.74](/docs/0.74/props)* [0.73](/docs/0.73/props)* [0.72](/docs/0.72/props)* [0.71](/docs/0.71/props)* [0.70](/docs/0.70/props)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

Props
=====

Most components can be customized when they are created, with different parameters. These created parameters are called `props`, short for properties.

For example, one basic React Native component is the `Image`. When you create an image, you can use a prop named `source` to control what image it shows.

Notice the braces surrounding `{pic}` - these embed the variable `pic` into JSX. You can put any JavaScript expression inside braces in JSX.

Your own components can also use `props`. This lets you make a single component that is used in many different places in your app, with slightly different properties in each place by referring to `props` in your `render` function. Here's an example:

* TypeScript* JavaScript

Using `name` as a prop lets us customize the `Greeting` component, so we can reuse that component for each of our greetings. This example also uses the `Greeting` component in JSX, similar to the [Core Components](/docs/intro-react-native-components). The power to do this is what makes React so cool - if you find yourself wishing that you had a different set of UI primitives to work with, you can invent new ones.

The other new thing going on here is the [`View`](/docs/view) component. A [`View`](/docs/view) is useful as a container for other components, to help control style and layout.

With `props` and the basic [`Text`](/docs/text), [`Image`](/docs/image), and [`View`](/docs/view) components, you can build a wide variety of static screens. To learn how to make your app change over time, you need to [learn about State](/docs/state).

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/props.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/props.md)

Last updated on **Apr 14, 2025**

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