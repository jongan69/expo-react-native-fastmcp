Using a ScrollView · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/using-a-scrollview)

* [Next](/docs/next/using-a-scrollview)* [0.79](/docs/using-a-scrollview)* [0.78](/docs/0.78/using-a-scrollview)* [0.77](/docs/0.77/using-a-scrollview)* [0.76](/docs/0.76/using-a-scrollview)* [0.75](/docs/0.75/using-a-scrollview)* [0.74](/docs/0.74/using-a-scrollview)* [0.73](/docs/0.73/using-a-scrollview)* [0.72](/docs/0.72/using-a-scrollview)* [0.71](/docs/0.71/using-a-scrollview)* [0.70](/docs/0.70/using-a-scrollview)* [All versions](/versions)

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

Using a ScrollView
==================

The [ScrollView](/docs/scrollview) is a generic scrolling container that can contain multiple components and views. The scrollable items can be heterogeneous, and you can scroll both vertically and horizontally (by setting the `horizontal` property).

This example creates a vertical `ScrollView` with both images and text mixed together.

ScrollViews can be configured to allow paging through views using swiping gestures by using the `pagingEnabled` props. Swiping horizontally between views can also be implemented on Android using the [ViewPager](https://github.com/react-native-community/react-native-viewpager) component.

On iOS a ScrollView with a single item can be used to allow the user to zoom content. Set up the `maximumZoomScale` and `minimumZoomScale` props and your user will be able to use pinch and expand gestures to zoom in and out.

The ScrollView works best to present a small number of things of a limited size. All the elements and views of a `ScrollView` are rendered, even if they are not currently shown on the screen. If you have a long list of items which cannot fit on the screen, you should use a `FlatList` instead. So let's [learn about list views](/docs/using-a-listview) next.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/using-a-scrollview.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/using-a-scrollview.md)

Last updated on **Apr 14, 2025**

[Previous

Handling Text Input](/docs/handling-text-input)[Next

Using List Views](/docs/using-a-listview)

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