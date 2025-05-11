Develop websites with Expo - Expo Documentation

[Docs](/)

[Blog](https://expo.dev/blog)[Changelog](https://expo.dev/changelog)[Star Us on GitHub](https://github.com/expo/expo)

Search

[Home](/)[Guides](/guides/overview)[EAS](/eas)[Reference](/versions/latest)[Learn](/tutorial/overview)

[Overview](/guides/overview)

Development process

[Develop an app with Expo](/workflow/overview)[Configure with app config](/workflow/configuration)[Continuous Native Generation](/workflow/continuous-native-generation)[Using libraries](/workflow/using-libraries)[Privacy manifests](/guides/apple-privacy)[Permissions](/guides/permissions)[Environment variables](/guides/environment-variables)

Linking

Write native code

Compile locally

Web

[Develop websites](/workflow/web)[Publish websites](/guides/publishing-websites)[DOM components](/guides/dom-components)[Progressive web apps](/guides/progressive-web-apps)[Tailwind CSS](/guides/tailwind)

Bundling

Existing React Native apps

Existing native apps

Reference

Expo Router

[Introduction](/router/introduction)[Installation](/router/installation)

Router 101

Navigation patterns

Advanced

Reference

Migration

Expo Modules API

[Overview](/modules/overview)[Get started](/modules/get-started)

Tutorials

Reference

Push notifications

[Overview](/push-notifications/overview)[About notification types](/push-notifications/what-you-need-to-know)[Expo push notifications setup](/push-notifications/push-notifications-setup)[Send notifications with the Expo Push Service](/push-notifications/sending-notifications)[Handle incoming notifications](/push-notifications/receiving-notifications)

Reference

More

[Upgrade Expo SDK](/workflow/upgrading-expo-sdk-walkthrough)

Assorted

Integrations

Troubleshooting

Regulatory compliance

[Data and Privacy protection](/regulatory-compliance/data-and-privacy-protection)[GDPR compliance](/regulatory-compliance/gdpr)[HIPAA compliance](/regulatory-compliance/hipaa)[Privacy Shield](/regulatory-compliance/privacy-shield)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Develop websites with Expo
==========================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/workflow/web.mdx)

Learn how to develop your app for the web so you can build a universal app.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/workflow/web.mdx)

---

Expo has first-class support for building full-stack websites with React. Expo websites can be [statically rendered](/router/reference/static-rendering) for SEO and performance, or client-rendered for a more app-like experience in the browser.

Universal

Web-only

Render text on any platform with the `<Text>` component from [React Native for web](https://github.com/necolas/react-native-web).

app/index.js

Copy

```
import { Text } from 'react-native';

export default function Page() {
  return <Text>Home page</Text>;
}

```

React Native for web (RNW) is a set of component libraries such as `<View>`, and `<Text>`, that wrap `react-dom` primitives such as `<div>`, `<p>`, and `<img>`. RNW is optional when developing for web since you can use React DOM directly, but we often recommended it when building across platforms as it maximizes code reuse.

> React Native for web is used to power the entire [X](https://x.com/) website.

Alternatively, you can write web-only React DOM components such as `<div>`, `<p>`, and so on, however, these components won't render on native platforms.

app/index.js

Copy

```
export default function Page() {
  return <p>Home page</p>;
}

```

Building web-only components is fully supported by Expo, however, you may want to organize your code to better support building for both web and native platforms simultaneously. Learn more in [platform-specific modules](/router/advanced/platform-specific-modules).

All of the libraries in the Expo SDK are built to support both browser and server rendering environments (when applicable). Libraries are also optimized for the individual platforms they target.

Development features like Fast Refresh, debugging, environment variables, and [bundling](/guides/customizing-metro) are also fully universal, enabling a unified developer experience. Expo CLI automatically optimizes code for individual platforms when you build for production, using techniques like [platform shaking](/guides/tree-shaking#platform-shaking).

Getting started
---------------

### Install web dependencies

Terminal

Copy

`-Â``npx expo install react-dom react-native-web @expo/metro-runtime`

Not using the `expo` package in your app yet?

If you haven't added Expo to your React Native app yet, you can either [install Expo modules](/bare/installing-expo-modules) (recommended) or just install the `expo` package and configure the app entry file. This will allow you to target web, but it will not include support for the Expo SDK.

1. Install [Expo CLI](/more/expo-cli) in your project:

Terminal

Copy

`-Â``npm install expo`

2. Modify the entry file to use [`registerRootComponent`](/versions/latest/sdk/register-root-component#registerrootcomponentcomponent) instead of `AppRegistry.registerComponent`:

```
+ import {registerRootComponent} from 'expo';

import App from './App';
- import {AppRegistry} from 'react-native';
- import {name as appName} from './app.json';

- AppRegistry.registerComponent(appName, () => App);
+ registerRootComponent(App);

```

### Start the dev server

You can now start the dev server and develop in the browser with:

Terminal

Copy

`-Â``npx expo start --web`

The app can be exported as a production website with:

Terminal

Copy

`-Â``npx expo export --platform web`

Next
----

[File-based routing

Build routes and navigation with Expo Router.](/router/introduction)
[Static rendering and SEO

Render your website as static HTML with Expo Router to improve SEO and performance.](/router/reference/static-rendering)
[Deploy instantly with EAS Hosting

EAS Hosting is the best way to deploy your Expo Router and React Native web apps with support for custom domains, SSL, and more.](/eas/hosting/get-started)
[Customizing the JavaScript bundler

Customize Metro bundler for your project.](/guides/customizing-metro)

[Previous (Development process - Compile locally)

Cache builds remotely](/guides/cache-builds-remotely)[Next (Development process - Web)

Publish websites](/guides/publishing-websites)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/workflow/web.mdx)
* Last updated on January 21, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).