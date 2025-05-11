Using List Views · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/using-a-listview)

* [Next](/docs/next/using-a-listview)* [0.79](/docs/using-a-listview)* [0.78](/docs/0.78/using-a-listview)* [0.77](/docs/0.77/using-a-listview)* [0.76](/docs/0.76/using-a-listview)* [0.75](/docs/0.75/using-a-listview)* [0.74](/docs/0.74/using-a-listview)* [0.73](/docs/0.73/using-a-listview)* [0.72](/docs/0.72/using-a-listview)* [0.71](/docs/0.71/using-a-listview)* [0.70](/docs/0.70/using-a-listview)* [All versions](/versions)

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

Using List Views
================

React Native provides a suite of components for presenting lists of data. Generally, you'll want to use either [FlatList](/docs/flatlist) or [SectionList](/docs/sectionlist).

The `FlatList` component displays a scrolling list of changing, but similarly structured, data. `FlatList` works well for long lists of data, where the number of items might change over time. Unlike the more generic [`ScrollView`](/docs/using-a-scrollview), the `FlatList` only renders elements that are currently showing on the screen, not all the elements at once.

The `FlatList` component requires two props: `data` and `renderItem`. `data` is the source of information for the list. `renderItem` takes one item from the source and returns a formatted component to render.

This example creates a basic `FlatList` of hardcoded data. Each item in the `data` props is rendered as a `Text` component. The `FlatListBasics` component then renders the `FlatList` and all `Text` components.

If you want to render a set of data broken into logical sections, maybe with section headers, similar to `UITableView`s on iOS, then a [SectionList](/docs/sectionlist) is the way to go.

One of the most common uses for a list view is displaying data that you fetch from a server. To do that, you will need to [learn about networking in React Native](/docs/network).

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/using-a-listview.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/using-a-listview.md)

Last updated on **Apr 14, 2025**

[Previous

Using a ScrollView](/docs/using-a-scrollview)[Next

Troubleshooting](/docs/troubleshooting)

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