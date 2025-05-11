Handling Text Input · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/handling-text-input)

* [Next](/docs/next/handling-text-input)* [0.79](/docs/handling-text-input)* [0.78](/docs/0.78/handling-text-input)* [0.77](/docs/0.77/handling-text-input)* [0.76](/docs/0.76/handling-text-input)* [0.75](/docs/0.75/handling-text-input)* [0.74](/docs/0.74/handling-text-input)* [0.73](/docs/0.73/handling-text-input)* [0.72](/docs/0.72/handling-text-input)* [0.71](/docs/0.71/handling-text-input)* [0.70](/docs/0.70/handling-text-input)* [All versions](/versions)

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

Handling Text Input
===================

[`TextInput`](/docs/textinput#content) is a [Core Component](/docs/intro-react-native-components) that allows the user to enter text. It has an `onChangeText` prop that takes a function to be called every time the text changed, and an `onSubmitEditing` prop that takes a function to be called when the text is submitted.

For example, let's say that as the user types, you're translating their words into a different language. In this new language, every single word is written the same way: 🍕. So the sentence "Hello there Bob" would be translated as "🍕 🍕 🍕".

In this example, we store `text` in the state, because it changes over time.

There are a lot more things you might want to do with a text input. For example, you could validate the text inside while the user types. For more detailed examples, see the [React docs on controlled components](https://react.dev/reference/react-dom/components/input#controlling-an-input-with-a-state-variable), or the [reference docs for TextInput](/docs/textinput).

Text input is one of the ways the user interacts with the app. Next, let's look at another type of input and [learn how to handle touches](/docs/handling-touches).

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/handling-text-input.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/handling-text-input.md)

Last updated on **Apr 14, 2025**

[Previous

React Fundamentals](/docs/intro-react)[Next

Using a ScrollView](/docs/using-a-scrollview)

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