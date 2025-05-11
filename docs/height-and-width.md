Height and Width · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/height-and-width)

* [Next](/docs/next/height-and-width)* [0.79](/docs/height-and-width)* [0.78](/docs/0.78/height-and-width)* [0.77](/docs/0.77/height-and-width)* [0.76](/docs/0.76/height-and-width)* [0.75](/docs/0.75/height-and-width)* [0.74](/docs/0.74/height-and-width)* [0.73](/docs/0.73/height-and-width)* [0.72](/docs/0.72/height-and-width)* [0.71](/docs/0.71/height-and-width)* [0.70](/docs/0.70/height-and-width)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [The Basics](/docs/getting-started)

  * [Environment setup](/docs/environment-setup)

    * [Workflow](/docs/running-on-device)

      * [UI & Interaction](/docs/style)

        + [Style](/docs/style)+ [Height and Width](/docs/height-and-width)+ [Layout with Flexbox](/docs/flexbox)+ [Images](/docs/images)+ [Color Reference](/docs/colors)+ Interaction

                    - [Handling Touches](/docs/handling-touches)- [Navigating Between Screens](/docs/navigation)- [Animations](/docs/animations)- [Gesture Responder System](/docs/gesture-responder-system)+ Connectivity

                      - [Networking](/docs/network)- [Security](/docs/security)+ Inclusion

                        - [Accessibility](/docs/accessibility)* [Debugging](/docs/debugging)

          * [Testing](/docs/testing-overview)

            * [Performance](/docs/performance)

              * [JavaScript Runtime](/docs/javascript-environment)

                * [Codegen](/docs/the-new-architecture/what-is-codegen)

                  * [Native Development](/docs/native-platform)

                    * [Android and iOS guides](/docs/headless-js-android)

                      * [Legacy Architecture](/docs/legacy/native-modules-intro)

On this page

Height and Width
================

A component's height and width determine its size on the screen.

Fixed Dimensions[​](#fixed-dimensions "Direct link to Fixed Dimensions")
------------------------------------------------------------------------

The general way to set the dimensions of a component is by adding a fixed `width` and `height` to style. All dimensions in React Native are unitless, and represent density-independent pixels.

Setting dimensions this way is common for components whose size should always be fixed to a number of points and not calculated based on screen size.

caution

There is no universal mapping from points to physical units of measurement. This means that a component with fixed dimensions might not have the same physical size, across different devices and screen sizes. However, this difference is unnoticeable for most use cases.

Flex Dimensions[​](#flex-dimensions "Direct link to Flex Dimensions")
---------------------------------------------------------------------

Use `flex` in a component's style to have the component expand and shrink dynamically based on available space. Normally you will use `flex: 1`, which tells a component to fill all available space, shared evenly amongst other components with the same parent. The larger the `flex` given, the higher the ratio of space a component will take compared to its siblings.

info

A component can only expand to fill available space if its parent has dimensions greater than `0`. If a parent does not have either a fixed `width` and `height` or `flex`, the parent will have dimensions of `0` and the `flex` children will not be visible.

After you can control a component's size, the next step is to [learn how to lay it out on the screen](/docs/flexbox).

Percentage Dimensions[​](#percentage-dimensions "Direct link to Percentage Dimensions")
---------------------------------------------------------------------------------------

If you want to fill a certain portion of the screen, but you *don't* want to use the `flex` layout, you *can* use **percentage values** in the component's style. Similar to flex dimensions, percentage dimensions require parent with a defined size.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/height-and-width.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/height-and-width.md)

Last updated on **Apr 14, 2025**

[Previous

Style](/docs/style)[Next

Layout with Flexbox](/docs/flexbox)

* [Fixed Dimensions](#fixed-dimensions)* [Flex Dimensions](#flex-dimensions)* [Percentage Dimensions](#percentage-dimensions)

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