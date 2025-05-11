Upgrading to new versions · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/upgrading)

* [Next](/docs/next/upgrading)* [0.79](/docs/upgrading)* [0.78](/docs/0.78/upgrading)* [0.77](/docs/0.77/upgrading)* [0.76](/docs/0.76/upgrading)* [0.75](/docs/0.75/upgrading)* [0.74](/docs/0.74/upgrading)* [0.73](/docs/0.73/upgrading)* [0.72](/docs/0.72/upgrading)* [0.71](/docs/0.71/upgrading)* [0.70](/docs/0.70/upgrading)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [The Basics](/docs/getting-started)

  * [Environment setup](/docs/environment-setup)

    * [Workflow](/docs/running-on-device)

      + [Running On Device](/docs/running-on-device)+ [Fast Refresh](/docs/fast-refresh)+ [Metro](/docs/metro)+ [Using Libraries](/docs/libraries)+ [Using TypeScript](/docs/typescript)+ [Upgrading to new versions](/docs/upgrading)* [UI & Interaction](/docs/style)

        * [Debugging](/docs/debugging)

          * [Testing](/docs/testing-overview)

            * [Performance](/docs/performance)

              * [JavaScript Runtime](/docs/javascript-environment)

                * [Codegen](/docs/the-new-architecture/what-is-codegen)

                  * [Native Development](/docs/native-platform)

                    * [Android and iOS guides](/docs/headless-js-android)

                      * [Legacy Architecture](/docs/legacy/native-modules-intro)

On this page

Upgrading to new versions
=========================

Upgrading to new versions of React Native will give you access to more APIs, views, developer tools and other goodies. Upgrading requires a small amount of effort, but we try to make it straightforward for you.

Expo projects[​](#expo-projects "Direct link to Expo projects")
---------------------------------------------------------------

Upgrading your Expo project to a new version of React Native requires updating the `react-native`, `react`, and `expo` package versions in your `package.json` file. Expo recommends upgrading SDK versions incrementally, one at a time. Doing so will help you pinpoint breakages and issues that arise during the upgrade process. See the [Upgrading Expo SDK Walkthrough](https://docs.expo.dev/workflow/upgrading-expo-sdk-walkthrough/) for up-to-date information about upgrading your project.

React Native projects[​](#react-native-projects "Direct link to React Native projects")
---------------------------------------------------------------------------------------

Because typical React Native projects are essentially made up of an Android project, an iOS project, and a JavaScript project, upgrading can be rather tricky. The [Upgrade Helper](https://react-native-community.github.io/upgrade-helper/) is a web tool to help you out when upgrading your apps by providing the full set of changes happening between any two versions. It also shows comments on specific files to help understanding why that change is needed.

### 1. Select the versions[​](#1-select-the-versions "Direct link to 1. Select the versions")

You first need to select from and to which version you wish to upgrade, by default the latest major versions are selected. After selecting you can click the button "Show me how to upgrade".

💡 Major updates will show a "useful content" section on the top with links to help you out when upgrading.

### 2. Upgrade dependencies[​](#2-upgrade-dependencies "Direct link to 2. Upgrade dependencies")

The first file that is shown is the `package.json`, it's good to update the dependencies that are showing in there. For example, if `react-native` and `react` appears as changes then you can install it in your project by running following commands:

* npm* Yarn

shell

```
# {{VERSION}} and {{REACT_VERSION}} are the release versions showing in the diff  
npm install react-native@{{VERSION}}  
npm install react@{{REACT_VERSION}}  

```

shell

```
# {{VERSION}} and {{REACT_VERSION}} are the release versions showing in the diff  
yarn add react-native@{{VERSION}}  
yarn add react@{{REACT_VERSION}}  

```

### 3. Upgrade your project files[​](#3-upgrade-your-project-files "Direct link to 3. Upgrade your project files")

The new release may contain updates to other files that are generated when you run `npx react-native init`, those files are listed after the `package.json` in the [Upgrade Helper](https://react-native-community.github.io/upgrade-helper/) page. If there aren't other changes then you only need to rebuild the project to continue developing. In case there are changes you need to manually apply them into your project.

### Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

#### I have done all the changes but my app is still using an old version[​](#i-have-done-all-the-changes-but-my-app-is-still-using-an-old-version "Direct link to I have done all the changes but my app is still using an old version")

These sort of errors are usually related to caching, it's recommended to install [react-native-clean-project](https://github.com/pmadruga/react-native-clean-project) to clear all your project's cache and then you can run it again.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/upgrading.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/upgrading.md)

Last updated on **Apr 14, 2025**

[Previous

Using TypeScript](/docs/typescript)[Next

Style](/docs/style)

* [Expo projects](#expo-projects)* [React Native projects](#react-native-projects)
    + [1. Select the versions](#1-select-the-versions)+ [2. Upgrade dependencies](#2-upgrade-dependencies)+ [3. Upgrade your project files](#3-upgrade-your-project-files)+ [Troubleshooting](#troubleshooting)

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