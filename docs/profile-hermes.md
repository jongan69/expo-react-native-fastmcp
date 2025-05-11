Profiling with Hermes · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.75](/docs/0.75/profile-hermes)

* [Next](/docs/next/getting-started)* [0.79](/docs/getting-started)* [0.78](/docs/0.78/getting-started)* [0.77](/docs/0.77/getting-started)* [0.76](/docs/0.76/getting-started)* [0.75](/docs/0.75/profile-hermes)* [0.74](/docs/0.74/profile-hermes)* [0.73](/docs/0.73/profile-hermes)* [0.72](/docs/0.72/profile-hermes)* [0.71](/docs/0.71/profile-hermes)* [0.70](/docs/0.70/profile-hermes)* [All versions](/versions)

[Development](#)

* [Guides](/docs/0.75/getting-started)* [Components](/docs/0.75/components-and-apis)* [APIs](/docs/0.75/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [The Basics](/docs/0.75/getting-started)

  * [Environment setup](/docs/0.75/environment-setup)

    * [Workflow](/docs/0.75/running-on-device)

      * [UI & Interaction](/docs/0.75/style)

        * [Debugging](/docs/0.75/debugging)

          * [Testing](/docs/0.75/testing-overview)

            * [Performance](/docs/0.75/performance)

              + [Performance Overview](/docs/0.75/performance)+ [Speeding up your Build phase](/docs/0.75/build-speed)+ [Optimizing Flatlist Configuration](/docs/0.75/optimizing-flatlist-configuration)+ [Optimizing JavaScript loading](/docs/0.75/optimizing-javascript-loading)+ [Profiling](/docs/0.75/profiling)+ [Profiling with Hermes](/docs/0.75/profile-hermes)* [JavaScript Runtime](/docs/0.75/javascript-environment)

                * [Native Modules](/docs/0.75/native-modules-intro)

                  * [Native Components](/docs/0.75/native-components-android)

                    * [Android and iOS guides](/docs/0.75/headless-js-android)

                      * [New Architecture](/docs/0.75/the-new-architecture/landing-page)

This is documentation for React Native **0.75**, which is no longer in active development.

For up-to-date documentation, see the **[latest version](/docs/getting-started)** (0.79).

Version: 0.75

On this page

Profiling with Hermes
=====================

You can visualize JavaScript's performance in a React Native app using [Hermes](https://github.com/facebook/hermes). Hermes is a small and lightweight JavaScript engine optimized for running React Native (you can [read more about using it with React Native here](/docs/0.75/hermes)). Hermes helps improve app performance and also exposes ways to analyze the performance of the JavaScript that it runs.

In this section, you will learn how to profile your React Native app running on Hermes and how to visualize the profile using [the Performance tab on Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools/evaluate-performance/reference)

caution

Be sure to [enable Hermes in your app](/docs/0.75/hermes) before you get started!

Follow the instructions below to get started profiling:

1. [Record a Hermes sampling profile](/docs/0.75/profile-hermes#record-a-hermes-sampling-profile)
2. [Execute command from CLI](/docs/0.75/profile-hermes#execute-command-from-cli)
3. [Open the downloaded profile on Chrome DevTools](/docs/0.75/profile-hermes#open-the-downloaded-profile-on-chrome-devtools)

Record a Hermes sampling profile[​](#record-a-hermes-sampling-profile "Direct link to Record a Hermes sampling profile")
------------------------------------------------------------------------------------------------------------------------

To record a sampling profiler from the Dev Menu:

1. Navigate to your running Metro server terminal.
2. Press `d` to open the **Dev Menu.**
3. Select **Enable Sampling Profiler.**
4. Execute your JavaScript by in your app (press buttons, etc.)
5. Open the **Dev Menu** by pressing `d` again.
6. Select **Disable Sampling Profiler** to stop recording and save the sampling profiler.

A toast will show the location where the sampling profiler has been saved, usually in `/data/user/0/com.appName/cache/*.cpuprofile`

![Toast Notification of Profile saving](/docs/assets/HermesProfileSaved.png)

Execute command from CLI[​](#execute-command-from-cli "Direct link to Execute command from CLI")
------------------------------------------------------------------------------------------------

You can use the [React Native CLI](https://github.com/react-native-community/cli) to convert the Hermes tracing profile to Chrome tracing profile, and then pull it to your local machine using:

sh

```
npx react-native profile-hermes [destinationDir]  

```

### Enabling source map[​](#enabling-source-map "Direct link to Enabling source map")

info

You may read about source maps on the [Debugging Release Builds](/docs/0.75/debugging-release-builds) page.

### Common errors[​](#common-errors "Direct link to Common errors")

#### `adb: no devices/emulators found` or `adb: device offline`[​](#adb-no-devicesemulators-found-or-adb-device-offline "Direct link to adb-no-devicesemulators-found-or-adb-device-offline")

* **Why this happens** The CLI cannot access the device or emulator (through adb) you are using to run the app.
* **How to fix** Make sure your Android device/emulator is connected and running. The command only works when it can access adb.

#### `There is no file in the cache/ directory`[​](#there-is-no-file-in-the-cache-directory "Direct link to there-is-no-file-in-the-cache-directory")

* **Why this happens** The CLI cannot find any **.cpuprofile** file in your app's **cache/** directory. You might have forgotten to record a profile from the device.
* **How to fix** Follow the [instructions](/docs/0.75/profile-hermes#record-a-hermes-sampling-profile) to enable/disable profiler from device.

#### `Error: your_profile_name.cpuprofile is an empty file`[​](#error-your_profile_namecpuprofile-is-an-empty-file "Direct link to error-your_profile_namecpuprofile-is-an-empty-file")

* **Why this happens** The profile is empty, it might be because Hermes is not running correctly.
* **How to fix** Make sure your app is running on the latest version of Hermes.

Open the downloaded profile in Chrome DevTools[​](#open-the-downloaded-profile-in-chrome-devtools "Direct link to Open the downloaded profile in Chrome DevTools")
------------------------------------------------------------------------------------------------------------------------------------------------------------------

To open the profile in Chrome DevTools:

1. Open Chrome DevTools.
2. Select the **Performance** tab.
3. Right click and choose **Load profile...**

![Loading a performance profile on Chrome DevTools](/docs/assets/openChromeProfile.png)

How does the Hermes Profile Transformer work?[​](#how-does-the-hermes-profile-transformer-work "Direct link to How does the Hermes Profile Transformer work?")
--------------------------------------------------------------------------------------------------------------------------------------------------------------

The Hermes Sample Profile is of the `JSON object format`, while the format that Google's DevTools supports is `JSON Array Format`. (More information about the formats can be found on the [Trace Event Format Document](https://docs.google.com/document/d/1CvAClvFfyA5R-PhYUmn5OOQtYMH4h6I0nSsKchNAySU/preview))

ts

```
export interface HermesCPUProfile {  
  traceEvents: SharedEventProperties[];  
  samples: HermesSample[];  
  stackFrames: {[key in string]: HermesStackFrame};  
}  

```

The Hermes profile has most of its information encoded into the `samples` and `stackFrames` properties. Each sample is a snapshot of the function call stack at that particular timestamp as each sample has a `sf` property which corresponds to a function call.

ts

```
export interface HermesSample {  
  cpu: string;  
  name: string;  
  ts: string;  
  pid: number;  
  tid: string;  
  weight: string;  
  /**  
   * Will refer to an element in the stackFrames object of the Hermes Profile  
   */  
  sf: number;  
  stackFrameData?: HermesStackFrame;  
}  

```

The information about a function call can be found in `stackFrames` which contains key-object pairs, where the key is the `sf` number and the corresponding object gives us all the relevant information about the function including the `sf` number of its parent function. This parent-child relationship can be traced upwards to find the information of all the functions running at a particular timestamp.

ts

```
export interface HermesStackFrame {  
  line: string;  
  column: string;  
  funcLine: string;  
  funcColumn: string;  
  name: string;  
  category: string;  
  /**  
   * A parent function may or may not exist  
   */  
  parent?: number;  
}  

```

At this point, you should define a few more terms, namely:

1. Nodes: The objects corresponding to `sf` numbers in `stackFrames`
2. Active Nodes: The nodes which are currently running at a particular timestamp. A node is classified as running if its `sf` number is in the function call stack. This call stack can be obtained from the `sf` number of the sample and tracing upwards till parent `sf`s are available

The `samples` and the `stackFrames` in tandem can then be used to generate all the start and end events at the corresponding timestamps, wherein:

1. Start Nodes/Events: Nodes absent in the previous sample's function call stack but present in the current sample's.
2. End Nodes/Events: Nodes present in the previous sample's function call stack but absent in the current sample's.

![CallStack Terms Explained](/docs/assets/CallStackDemo.jpg)

You can now construct a `flamechart` of function calls as you have all the function information including its start and end timestamps.

The `hermes-profile-transformer` can convert any profile generated using Hermes into a format that can be directly displayed in Chrome DevTools. More information about this can be found on  [`@react-native-community/hermes-profile-transformer`](https://github.com/react-native-community/hermes-profile-transformer)

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/profile-hermes.md)[Edit page for 0.75 release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.75/profile-hermes.md)

Last updated on **Aug 15, 2024**

[Previous

Profiling](/docs/0.75/profiling)[Next

JavaScript Environment](/docs/0.75/javascript-environment)

* [Record a Hermes sampling profile](#record-a-hermes-sampling-profile)* [Execute command from CLI](#execute-command-from-cli)
    + [Enabling source map](#enabling-source-map)+ [Common errors](#common-errors)* [Open the downloaded profile in Chrome DevTools](#open-the-downloaded-profile-in-chrome-devtools)* [How does the Hermes Profile Transformer work?](#how-does-the-hermes-profile-transformer-work)

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