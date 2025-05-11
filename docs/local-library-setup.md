Local libraries setup · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/legacy/local-library-setup)

* [Next](/docs/next/legacy/local-library-setup)* [0.79](/docs/legacy/local-library-setup)* [0.78](/docs/0.78/legacy/local-library-setup)* [0.77](/docs/0.77/legacy/local-library-setup)* [0.76](/docs/0.76/legacy/local-library-setup)* [0.75](/docs/0.75/getting-started)* [0.74](/docs/0.74/getting-started)* [0.73](/docs/0.73/getting-started)* [0.72](/docs/0.72/getting-started)* [0.71](/docs/0.71/getting-started)* [0.70](/docs/0.70/getting-started)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [The Basics](/docs/getting-started)

  * [Environment setup](/docs/environment-setup)

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

                        + [Native Modules](/docs/legacy/native-modules-intro)

                          - [Native Modules Intro](/docs/legacy/native-modules-intro)- [Android Native Modules](/docs/legacy/native-modules-android)- [iOS Native Modules](/docs/legacy/native-modules-ios)- [Native Modules NPM Package Setup](/docs/legacy/native-modules-setup)- [Local libraries setup](/docs/legacy/local-library-setup)+ [Native Components](/docs/legacy/native-components-android)

On this page

Local libraries setup
=====================

A local library is a library containing views or modules that's local to your app and not published to a registry. This is different from the traditional setup for view and modules in the sense that a local library is decoupled from your app's native code.

The local library is created outside of the `android/` and `ios/` folders and makes use of autolinking to integrate with your app. The structure with a local library may look like this:

plaintext

```
MyApp  
├── node_modules  
├── modules <-- folder for your local libraries  
│ └── awesome-module <-- your local library  
├── android  
├── ios  
├── src  
├── index.js  
└── package.json  

```

Since a local library's code exists outside of `android/` and `ios/` folders, it makes it easier to upgrade React Native versions in the future, copy to other projects etc.

To create local library we will use [create-react-native-library](https://callstack.github.io/react-native-builder-bob/create). This tool contains all the necessary templates.

### Getting Started[​](#getting-started "Direct link to Getting Started")

Inside your React Native application's root folder, run the following command:

shell

```
npx create-react-native-library@latest awesome-module  

```

Where `awesome-module` is the name you would like for the new module. After going through the prompts, you will have a new folder called `modules` in your project's root directory which contains the new module.

### Linking[​](#linking "Direct link to Linking")

By default, the generated library is automatically linked to the project using `link:` protocol when using Yarn and `file:` when using npm:

* npm* Yarn

json

```
"dependencies": {  
  "awesome-module": "file:./modules/awesome-module"  
}  

```

json

```
"dependencies": {  
  "awesome-module": "link:./modules/awesome-module"  
}  

```

This creates a symlink to the library under `node_modules` which makes autolinking work.

### Installing dependencies[​](#installing-dependencies "Direct link to Installing dependencies")

To link the module you need to install dependencies:

* npm* Yarn

shell

```
npm install  

```

shell

```
yarn install  

```

### Using module inside your app[​](#using-module-inside-your-app "Direct link to Using module inside your app")

To use the module inside your app, you can import it by its name:

js

```
import {multiply} from 'awesome-module';  

```

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/legacy/local-library-setup.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/legacy/local-library-setup.md)

Last updated on **Apr 14, 2025**

[Previous

Native Modules NPM Package Setup](/docs/legacy/native-modules-setup)[Next

Android Native UI Components](/docs/legacy/native-components-android)

* [Getting Started](#getting-started)* [Linking](#linking)* [Installing dependencies](#installing-dependencies)* [Using module inside your app](#using-module-inside-your-app)

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