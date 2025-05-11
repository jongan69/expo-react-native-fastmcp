React DevTools · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.75](/docs/0.75/react-devtools)

* [Next](/docs/next/getting-started)* [0.79](/docs/getting-started)* [0.78](/docs/0.78/getting-started)* [0.77](/docs/0.77/getting-started)* [0.76](/docs/0.76/getting-started)* [0.75](/docs/0.75/react-devtools)* [0.74](/docs/0.74/react-devtools)* [0.73](/docs/0.73/react-devtools)* [0.72](/docs/0.72/react-devtools)* [0.71](/docs/0.71/getting-started)* [0.70](/docs/0.70/getting-started)* [All versions](/versions)

[Development](#)

* [Guides](/docs/0.75/getting-started)* [Components](/docs/0.75/components-and-apis)* [APIs](/docs/0.75/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [The Basics](/docs/0.75/getting-started)

  * [Environment setup](/docs/0.75/environment-setup)

    * [Workflow](/docs/0.75/running-on-device)

      * [UI & Interaction](/docs/0.75/style)

        * [Debugging](/docs/0.75/debugging)

          + [Debugging Basics](/docs/0.75/debugging)+ [React DevTools](/docs/0.75/react-devtools)+ [Debugging Native Code](/docs/0.75/debugging-native-code)+ [Debugging Release Builds](/docs/0.75/debugging-release-builds)+ [Other Debugging Methods](/docs/0.75/other-debugging-methods)* [Testing](/docs/0.75/testing-overview)

            * [Performance](/docs/0.75/performance)

              * [JavaScript Runtime](/docs/0.75/javascript-environment)

                * [Native Modules](/docs/0.75/native-modules-intro)

                  * [Native Components](/docs/0.75/native-components-android)

                    * [Android and iOS guides](/docs/0.75/headless-js-android)

                      * [New Architecture](/docs/0.75/the-new-architecture/landing-page)

This is documentation for React Native **0.75**, which is no longer in active development.

For up-to-date documentation, see the **[latest version](/docs/getting-started)** (0.79).

Version: 0.75

On this page

React DevTools
==============

[React DevTools](https://github.com/facebook/react/tree/main/packages/react-devtools) can be used to debug the React component hierarchy within your app.

The standalone version of React DevTools allows connecting to React Native apps. To use it, install or run the `react-devtools` package. It should connect to your simulator within a few seconds.

sh

```
npx react-devtools  

```

![The React DevTools interface](/assets/images/debugging-react-devtools-detail-914f08a97163dd51ebe732fd8ae4ea3c.jpg)

💡 Installing React DevTools globally

We recommend running `react-devtools` via `npx`, but you can also install a given version globally.

* npm* Yarn

sh

```
npm install -g react-devtools  

```

shell

```
yarn global add react-devtools  

```

Then, run the global `react-devtools` command:

sh

```
react-devtools  

```

💡 Adding React DevTools as a project dependency

If you prefer to avoid global installations, you can add `react-devtools` as a project dependency. Add the `react-devtools` package to your project using `npm install --save-dev react-devtools`, then add `"react-devtools": "react-devtools"` to the `scripts` section in your `package.json`, and then run `npm run react-devtools` from your project folder to open the DevTools.

tip

Learn more about using DevTools in the [React Developer Tools guide on react.dev](https://react.dev/learn/react-developer-tools).

Integration with the Element Inspector[​](#integration-with-the-element-inspector "Direct link to Integration with the Element Inspector")
------------------------------------------------------------------------------------------------------------------------------------------

React Native provides an Element Inspector, available under the Dev Menu as "Show Element Inspector". The inspector lets you tap on any UI element and see information about it.

![Video of the Element Inspector interface](/assets/images/debugging-element-inspector-32d08229496f834721bb5ce30b841876.gif)

When React DevTools is connected, the Element Inspector will enter a **collapsed mode**, and instead use DevTools as the primary UI. In this mode, clicking on something in the simulator will navigate to the relevant component in DevTools.

You can select "Hide Element Inspector" in the same menu to exit this mode.

![React DevTools Element Inspector integration](/assets/images/debugging-element-inspector-react-devtools-55e10feae83b21884933506ab29c07ae.gif)

Debugging application state[​](#debugging-application-state "Direct link to Debugging application state")
---------------------------------------------------------------------------------------------------------

[Reactotron](https://github.com/infinitered/reactotron) is an open-source desktop app that allows you to inspect Redux or MobX-State-Tree application state as well as view custom logs, run custom commands such as resetting state, store and restore state snapshots, and other helpful debugging features for React Native apps.

You can view installation instructions [in the README](https://github.com/infinitered/reactotron). If you're using Expo, here is an article detailing [how to install on Expo](https://shift.infinite.red/start-using-reactotron-in-your-expo-project-today-in-3-easy-steps-a03d11032a7a).

Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")
---------------------------------------------------------------------

tip

Once you have React DevTools running, follow the instructions. If you had your application running prior to opening React DevTools, you may need to [open the Dev Menu](/docs/0.75/debugging#accessing-the-dev-menu) to connect it.

![React DevTools connection flow](/assets/images/debugging-react-devtools-connection-ceb2fbb2b7c3d3c70c2560457464e7ae.gif)

info

If connecting to an Android emulator proves troublesome, try running `adb reverse tcp:8097 tcp:8097` in a new terminal.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/react-devtools.md)[Edit page for 0.75 release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.75/react-devtools.md)

Last updated on **Aug 15, 2024**

[Previous

Debugging Basics](/docs/0.75/debugging)[Next

Debugging Native Code](/docs/0.75/debugging-native-code)

* [Integration with the Element Inspector](#integration-with-the-element-inspector)* [Debugging application state](#debugging-application-state)* [Troubleshooting](#troubleshooting)

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