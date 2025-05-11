React Native DevTools · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/react-native-devtools)

* [Next](/docs/next/react-native-devtools)* [0.79](/docs/react-native-devtools)* [0.78](/docs/0.78/react-native-devtools)* [0.77](/docs/0.77/react-native-devtools)* [0.76](/docs/0.76/react-native-devtools)* [0.75](/docs/0.75/getting-started)* [0.74](/docs/0.74/getting-started)* [0.73](/docs/0.73/getting-started)* [0.72](/docs/0.72/getting-started)* [0.71](/docs/0.71/getting-started)* [0.70](/docs/0.70/getting-started)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [The Basics](/docs/getting-started)

  * [Environment setup](/docs/environment-setup)

    * [Workflow](/docs/running-on-device)

      * [UI & Interaction](/docs/style)

        * [Debugging](/docs/debugging)

          + [Debugging Basics](/docs/debugging)+ [React Native DevTools](/docs/react-native-devtools)+ [Debugging Native Code](/docs/debugging-native-code)+ [Debugging Release Builds](/docs/debugging-release-builds)+ [Other Debugging Methods](/docs/other-debugging-methods)* [Testing](/docs/testing-overview)

            * [Performance](/docs/performance)

              * [JavaScript Runtime](/docs/javascript-environment)

                * [Codegen](/docs/the-new-architecture/what-is-codegen)

                  * [Native Development](/docs/native-platform)

                    * [Android and iOS guides](/docs/headless-js-android)

                      * [Legacy Architecture](/docs/legacy/native-modules-intro)

On this page

React Native DevTools
=====================

React Native DevTools is our modern debugging experience for React Native. Purpose-built from the ground up, it aims to be fundamentally more integrated, correct, and reliable than previous debugging methods.

![React Native DevTools opened to the &quot;Welcome&quot; pane](/assets/images/debugging-rndt-welcome-ac9602807bddf2752fc2a73c57028122.jpg)

React Native DevTools is designed for debugging React app concerns, and not to replace native tools. If you want to inspect React Native’s underlying platform layers (for example, while developing a Native Module), please use the debugging tools available in Android Studio and Xcode (see [Debugging Native Code](/docs/debugging-native-code)).

**💡 Compatibility** — released in 0.76

React Native DevTools supports all React Native apps running Hermes. It replaces the previous Flipper, Experimental Debugger, and Hermes debugger (Chrome) frontends.

It is not possible to set up React Native DevTools with any older versions of React Native.

* **Chrome Browser DevTools — unsupported**
  + Connecting to React Native via `chrome://inspect` is no longer supported. Features may not work correctly, as the latest versions of Chrome DevTools (which are built to match the latest browser capabilities and APIs) have not been tested, and this frontend lacks our customisations. Instead, we ship a supported version with React Native DevTools.
* **Visual Studio Code — unsupported** (pre-existing)
  + Third party extensions such as [Expo Tools](https://github.com/expo/vscode-expo) and [Radon IDE](https://ide.swmansion.com/) may have improved compatibility, but are not directly supported by the React team.

**💡 Feedback & FAQs**

We want the tooling you use to debug React across all platforms to be reliable, familiar, simple, and cohesive. All the features described on this page are built with these principles in mind, and we also want to offer more capabilities in future.

We are actively iterating on the future of React Native DevTools, and have created a centralized [GitHub discussion](https://github.com/react-native-community/discussions-and-proposals/discussions/819) to keep track of issues, frequently asked questions, and feedback.

Core features[​](#core-features "Direct link to Core features")
---------------------------------------------------------------

React Native DevTools is based on the Chrome DevTools frontend. If you have a web development background, its features should be familiar. As a starting point, we recommend browsing the [Chrome DevTools docs](https://developer.chrome.com/docs/devtools) which contain full guides as well as video resources.

### Console[​](#console "Direct link to Console")

![A series of logs React Native DevTools Sources view, alongside a device](/assets/images/debugging-rndt-console-f0a53e3d62458a8ff1b7164fb5e5564c.jpg)

The Console panel allows you to view and filter messages, evaluate JavaScript, inspect object properties, and more.

[Console features reference | Chrome DevTools](https://developer.chrome.com/docs/devtools/console/reference)

#### Useful tips[​](#useful-tips "Direct link to Useful tips")

* If your app has a lot of logs, use the filter box or change the log levels that are shown.
* Watch values over time with [Live Expressions](https://developer.chrome.com/docs/devtools/console/live-expressions).
* Persist messages across reloads with [Preserve Logs](https://developer.chrome.com/docs/devtools/console/reference#persist).
* Use `Ctrl` + `L` to clear the console view.

### Sources & breakpoints[​](#sources--breakpoints "Direct link to Sources & breakpoints")

![A paused breakpoint in the React Native DevTools Sources view, alongside a device](/assets/images/debugging-rndt-sources-paused-with-device-d1d48a3df5a69d3bf92a16845f0f9c12.jpg)

The Sources panel allows you to view the source files in your app and register breakpoints. Use a breakpoint to define a line of code where your app should pause — allowing you to inspect the live state of the program and incrementally step through code.

[Pause your code with breakpoints | Chrome DevTools](https://developer.chrome.com/docs/devtools/javascript/breakpoints)

tip

#### Mini-guide[​](#mini-guide "Direct link to Mini-guide")

Breakpoints are a fundamental tool in your debugging toolkit!

1. Navigate to a source file using the sidebar or `Cmd ⌘`+`P` / `Ctrl`+`P`.
2. Click in the line number column next to a line of code to add a breakpoint.
3. Use the navigation controls at the top right to [step through code](https://developer.chrome.com/docs/devtools/javascript/reference#stepping) when paused.

#### Useful tips[​](#useful-tips-1 "Direct link to Useful tips")

* A "Paused in Debugger" overlay will appear when your app is paused. Tap it to resume.
* Pay attention to the right hand side panels when on a breakpoint, which allow you to inspect the current scope and call stack, and set watch expressions.
* Use a `debugger;` statement to quickly set a breakpoint from your text editor. This will reach the device immediately via Fast Refresh.
* There are multiple kinds of breakpoints! For example, [Conditional Breakpoints and Logpoints](https://developer.chrome.com/docs/devtools/javascript/breakpoints#overview).

### Memory[​](#memory "Direct link to Memory")

![Inspecting a heap snapshot in the Memory panel](/assets/images/debugging-rndt-memory-3f71040a2e688a5029db8326de0ce8dd.jpg)

The Memory panel allows you to take a heap snapshot and view the memory usage of your JavaScript code over time.

[Record heap snapshots | Chrome DevTools](https://developer.chrome.com/docs/devtools/memory-problems/heap-snapshots)

#### Useful tips[​](#useful-tips-2 "Direct link to Useful tips")

* Use `Cmd ⌘`+`F` / `Ctrl`+`F` to filter for specific objects in the heap.
* Taking an [allocation timeline report](https://developer.chrome.com/docs/devtools/memory-problems/allocation-profiler) can be useful to see memory usage over time as a graph, to identify possible memory leaks.

React DevTools features[​](#react-devtools-features "Direct link to React DevTools features")
---------------------------------------------------------------------------------------------

In the integrated Components and Profiler panels, you'll find all the features of the [React DevTools](https://react.dev/learn/react-developer-tools) browser extension. These work seamlessly in React Native DevTools.

### React Components[​](#react-components "Direct link to React Components")

![Selecting and locating elements using the React Components panel](/assets/images/debugging-rndt-react-components-628d33c662dc37b0a7c3c21d840fc63c.gif)

The React Components panel allows you to inspect and update the rendered React component tree.

* Hover or select an element in DevTools to highlight it on device.
* To locate an element in DevTools, click the top-left "Select element" button, then tap any element in the app.

#### Useful tips[​](#useful-tips-3 "Direct link to Useful tips")

* Props and state on a component can be viewed and modified at runtime using the right hand panel.
* Components optimized with [React Compiler](https://react.dev/learn/react-compiler) will be annotated with a "Memo ✨" badge.

tip

#### Protip: Highlight re-renders[​](#protip-highlight-re-renders "Direct link to Protip: Highlight re-renders")

Re-renders can be a significant contributor to performance issues in React apps. DevTools can highlight component re-renders as they happen.

* To enable, click the View Settings (`⚙︎`) icon and check "Highlight updates when components render".

![Location of the &quot;highlight updates&quot; setting, next to a recording of the live render overlay](/assets/images/debugging-rndt-highlight-renders-bc20258bbc79dba4fe1866c227943e37.gif)

### React Profiler[​](#react-profiler "Direct link to React Profiler")

![A profile rendered as a flame graph](/assets/images/debugging-rndt-react-profiler-997ef2d9e169d059ba7d4850ee8ce181.jpg)

The React Profiler panel allows you to record performance profiles to understand the timing of component renders and React commits.

For more info, see the [original 2018 guide](https://legacy.reactjs.org/blog/2018/09/10/introducing-the-react-profiler.html#reading-performance-data) (note that parts of this may be outdated).

Reconnecting DevTools[​](#reconnecting-devtools "Direct link to Reconnecting DevTools")
---------------------------------------------------------------------------------------

Occasionally, DevTools might disconnect from the target device. This can happen if:

* The app is closed.
* The app is rebuilt (a new native build is installed).
* The app has crashed on the native side.
* The dev server (Metro) is quit.
* A physical device is disconnected.

On disconnect, a dialog will be shown with the message "Debugging connection was closed".

![A reconnect dialog shown when a device is disconnected](/assets/images/debugging-reconnect-menu-2eb1659f4b9d58ccb839c6efccfccf7f.jpg)

From here, you can either:

* **Dismiss**: Select the close (`×`) icon or click outside the dialog to return to the DevTools UI in the last state before disconnection.
* **Reconnect**: Select "Reconnect DevTools", having addressed the reason for disconnection.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/react-native-devtools.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/react-native-devtools.md)

Last updated on **Apr 14, 2025**

[Previous

Debugging Basics](/docs/debugging)[Next

Debugging Native Code](/docs/debugging-native-code)

* [Core features](#core-features)
  + [Console](#console)+ [Sources & breakpoints](#sources--breakpoints)+ [Memory](#memory)* [React DevTools features](#react-devtools-features)
    + [React Components](#react-components)+ [React Profiler](#react-profiler)* [Reconnecting DevTools](#reconnecting-devtools)

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