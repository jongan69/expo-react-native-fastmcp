Using Libraries · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/libraries)

* [Next](/docs/next/libraries)* [0.79](/docs/libraries)* [0.78](/docs/0.78/libraries)* [0.77](/docs/0.77/libraries)* [0.76](/docs/0.76/libraries)* [0.75](/docs/0.75/libraries)* [0.74](/docs/0.74/libraries)* [0.73](/docs/0.73/libraries)* [0.72](/docs/0.72/libraries)* [0.71](/docs/0.71/libraries)* [0.70](/docs/0.70/libraries)* [All versions](/versions)

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

Using Libraries
===============

React Native provides a set of built-in [Core Components and APIs](/docs/components-and-apis) ready to use in your app. You're not limited to the components and APIs bundled with React Native. React Native has a community of thousands of developers. If the Core Components and APIs don't have what you are looking for, you may be able to find and install a library from the community to add the functionality to your app.

Selecting a Package Manager[​](#selecting-a-package-manager "Direct link to Selecting a Package Manager")
---------------------------------------------------------------------------------------------------------

React Native libraries are typically installed from the [npm registry](https://www.npmjs.com/) using a Node.js package manager such as [npm CLI](https://docs.npmjs.com/cli/npm) or [Yarn Classic](https://classic.yarnpkg.com/en/).

If you have Node.js installed on your computer then you already have the npm CLI installed. Some developers prefer to use Yarn Classic for slightly faster install times and additional advanced features like Workspaces. Both tools work great with React Native. We will assume npm for the rest of this guide for simplicity of explanation.

> 💡 The terms "library" and "package" are used interchangeably in the JavaScript community.

Installing a Library[​](#installing-a-library "Direct link to Installing a Library")
------------------------------------------------------------------------------------

To install a library in your project, navigate to your project directory in your terminal and run the installation command. Let's try this with `react-native-webview`:

* npm* Yarn

shell

```
npm install react-native-webview  

```

shell

```
yarn add react-native-webview  

```

The library that we installed includes native code, and we need to link to our app before we use it.

Linking Native Code on iOS[​](#linking-native-code-on-ios "Direct link to Linking Native Code on iOS")
------------------------------------------------------------------------------------------------------

React Native uses CocoaPods to manage iOS project dependencies and most React Native libraries follow this same convention. If a library you are using does not, then please refer to their README for additional instruction. In most cases, the following instructions will apply.

Run `pod install` in our `ios` directory in order to link it to our native iOS project. A shortcut for doing this without switching to the `ios` directory is to run `npx pod-install`.

bash

```
npx pod-install  

```

Once this is complete, re-build the app binary to start using your new library:

* npm* Yarn

shell

```
npm run ios  

```

shell

```
yarn ios  

```

Linking Native Code on Android[​](#linking-native-code-on-android "Direct link to Linking Native Code on Android")
------------------------------------------------------------------------------------------------------------------

React Native uses Gradle to manage Android project dependencies. After you install a library with native dependencies, you will need to re-build the app binary to use your new library:

* npm* Yarn

shell

```
npm run android  

```

shell

```
yarn android  

```

Finding Libraries[​](#finding-libraries "Direct link to Finding Libraries")
---------------------------------------------------------------------------

[React Native Directory](https://reactnative.directory) is a searchable database of libraries built specifically for React Native. This is the first place to look for a library for your React Native app.

Many of the libraries you will find on the directory are from [React Native Community](https://github.com/react-native-community/) or [Expo](https://docs.expo.dev/versions/latest/).

Libraries built by the React Native Community are driven by volunteers and individuals at companies that depend on React Native. They often support iOS, tvOS, Android, Windows, but this varies across projects. Many of the libraries in this organization were once React Native Core Components and APIs.

Libraries built by Expo are all written in TypeScript and support iOS, Android, and `react-native-web` wherever possible.

After React Native Directory, the [npm registry](https://www.npmjs.com/) is the next best place if you can't find a library specifically for React Native on the directory. The npm registry is the definitive source for JavaScript libraries, but the libraries that it lists may not all be compatible with React Native. React Native is one of many JavaScript programming environments, including Node.js, web browsers, Electron, and more, and npm includes libraries that work for all of these environments.

Determining Library Compatibility[​](#determining-library-compatibility "Direct link to Determining Library Compatibility")
---------------------------------------------------------------------------------------------------------------------------

### Does it work with React Native?[​](#does-it-work-with-react-native "Direct link to Does it work with React Native?")

Usually libraries built *specifically for other platforms* will not work with React Native. Examples include `react-select` which is built for the web and specifically targets `react-dom`, and `rimraf` which is built for Node.js and interacts with your computer file system. Other libraries like `lodash` use only JavaScript language features and work in any environment. You will gain a sense for this over time, but until then the easiest way to find out is to try it yourself. You can remove packages using `npm uninstall` if it turns out that it does not work in React Native.

### Does it work for the platforms that my app supports?[​](#does-it-work-for-the-platforms-that-my-app-supports "Direct link to Does it work for the platforms that my app supports?")

[React Native Directory](https://reactnative.directory) allows you to filter by platform compatibility, such as iOS, Android, Web, and Windows. If the library you would like to use is not currently listed there, refer to the README for the library to learn more.

### Does it work with my app version of React Native?[​](#does-it-work-with-my-app-version-of-react-native "Direct link to Does it work with my app version of React Native?")

The latest version of a library is typically compatible with the latest version of React Native. If you are using an older version, you should refer to the README to know which version of the library you should install. You can install a particular version of the library by running `npm install <library-name>@<version-number>`, for example: `npm install @react-native-community/netinfo@^2.0.0`.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/libraries.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/libraries.md)

Last updated on **Apr 14, 2025**

[Previous

Metro](/docs/metro)[Next

Using TypeScript](/docs/typescript)

* [Selecting a Package Manager](#selecting-a-package-manager)* [Installing a Library](#installing-a-library)* [Linking Native Code on iOS](#linking-native-code-on-ios)* [Linking Native Code on Android](#linking-native-code-on-android)* [Finding Libraries](#finding-libraries)* [Determining Library Compatibility](#determining-library-compatibility)
            + [Does it work with React Native?](#does-it-work-with-react-native)+ [Does it work for the platforms that my app supports?](#does-it-work-for-the-platforms-that-my-app-supports)+ [Does it work with my app version of React Native?](#does-it-work-with-my-app-version-of-react-native)

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