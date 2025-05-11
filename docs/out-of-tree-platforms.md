Out-of-Tree Platforms · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/out-of-tree-platforms)

* [Next](/docs/next/out-of-tree-platforms)* [0.79](/docs/out-of-tree-platforms)* [0.78](/docs/0.78/out-of-tree-platforms)* [0.77](/docs/0.77/out-of-tree-platforms)* [0.76](/docs/0.76/out-of-tree-platforms)* [0.75](/docs/0.75/out-of-tree-platforms)* [0.74](/docs/0.74/out-of-tree-platforms)* [0.73](/docs/0.73/out-of-tree-platforms)* [0.72](/docs/0.72/out-of-tree-platforms)* [0.71](/docs/0.71/out-of-tree-platforms)* [0.70](/docs/0.70/out-of-tree-platforms)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [The Basics](/docs/getting-started)

  * [Environment setup](/docs/environment-setup)

    + [Get Started with React Native](/docs/environment-setup)+ [Set Up Your Environment](/docs/set-up-your-environment)+ [Integration with Existing Apps](/docs/integration-with-existing-apps)+ [Integration with an Android Fragment](/docs/integration-with-android-fragment)+ [Building For TV Devices](/docs/building-for-tv)+ [Out-of-Tree Platforms](/docs/out-of-tree-platforms)* [Workflow](/docs/running-on-device)

      * [UI & Interaction](/docs/style)

        * [Debugging](/docs/debugging)

          * [Testing](/docs/testing-overview)

            * [Performance](/docs/performance)

              * [JavaScript Runtime](/docs/javascript-environment)

                * [Codegen](/docs/the-new-architecture/what-is-codegen)

                  * [Native Development](/docs/native-platform)

                    * [Android and iOS guides](/docs/headless-js-android)

                      * [Legacy Architecture](/docs/legacy/native-modules-intro)

On this page

Out-of-Tree Platforms
=====================

React Native is not only for Android and iOS devices - our partners and the community maintain projects that bring React Native to other platforms, such as:

**From Partners**

* [React Native macOS](https://github.com/microsoft/react-native-macos) - React Native for macOS and Cocoa.
* [React Native Windows](https://github.com/microsoft/react-native-windows) - React Native for Microsoft's Universal Windows Platform (UWP).
* [React Native visionOS](https://github.com/callstack/react-native-visionos) - React Native for Apple's visionOS.

**From Community**

* [React Native tvOS](https://github.com/react-native-tvos/react-native-tvos) - React Native for Apple TV and Android TV devices.
* [React Native Web](https://github.com/necolas/react-native-web) - React Native on the web using React DOM.
* [React Native Skia](https://github.com/react-native-skia/react-native-skia) - React Native using [Skia](https://skia.org/) as a renderer. Currently supports Linux and macOS.

Creating your own React Native platform[​](#creating-your-own-react-native-platform "Direct link to Creating your own React Native platform")
---------------------------------------------------------------------------------------------------------------------------------------------

Right now the process of creating a React Native platform from scratch is not very well documented - one of the goals of the upcoming re-architecture ([Fabric](/blog/2018/06/14/state-of-react-native-2018)) is to make maintaining a platform easier.

### Bundling[​](#bundling "Direct link to Bundling")

As of React Native 0.57 you can now register your React Native platform with React Native's JavaScript bundler, [Metro](https://metrobundler.dev/). This means you can pass `--platform example` to `npx react-native bundle`, and it will look for JavaScript files with the `.example.js` suffix.

To register your platform with RNPM, your module's name must match one of these patterns:

* `react-native-example` - It will search all top-level modules that start with `react-native-`
* `@org/react-native-example` - It will search for modules that start with `react-native-` under any scope
* `@react-native-example/module` - It will search in all modules under scopes with names starting with `@react-native-`

You must also have an entry in your `package.json` like this:

json

```
{  
  "rnpm": {  
    "haste": {  
      "providesModuleNodeModules": ["react-native-example"],  
      "platforms": ["example"]  
    }  
  }  
}  

```

`"providesModuleNodeModules"` is an array of modules that will get added to the Haste module search path, and `"platforms"` is an array of platform suffixes that will be added as valid platforms.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/out-of-tree-platforms.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/out-of-tree-platforms.md)

Last updated on **Apr 14, 2025**

[Previous

Building For TV Devices](/docs/building-for-tv)[Next

Running On Device](/docs/running-on-device)

* [Creating your own React Native platform](#creating-your-own-react-native-platform)
  + [Bundling](#bundling)

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