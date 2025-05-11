Using Next.js with Expo for Web - Expo Documentation

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

[Using Analytics](/guides/using-analytics)[Using Facebook authentication](/guides/facebook-authentication)[Using Supabase](/guides/using-supabase)[Using Firebase](/guides/using-firebase)[Using Google authentication](/guides/google-authentication)[Using ESLint and Prettier](/guides/using-eslint)[Using Next.js](/guides/using-nextjs)[Using LogRocket](/guides/using-logrocket)[Using Sentry](/guides/using-sentry)[Using BugSnag](/guides/using-bugsnag)[Using Vexo](/guides/using-vexo)[Build apps for TV](/guides/building-for-tv)[Using TypeScript](/guides/typescript)[Using In-app purchase](/guides/in-app-purchases)[Using push notifications](/guides/using-push-notifications-services)

Troubleshooting

Regulatory compliance

[Data and Privacy protection](/regulatory-compliance/data-and-privacy-protection)[GDPR compliance](/regulatory-compliance/gdpr)[HIPAA compliance](/regulatory-compliance/hipaa)[Privacy Shield](/regulatory-compliance/privacy-shield)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Using Next.js with Expo for Web
===============================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/using-nextjs.mdx)

A guide for integrating Next.js with Expo for the web.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/using-nextjs.mdx)

---

> Using Next.js is not an official part of Expo's universal app development workflow.

[Next.js](https://nextjs.org/) is a React framework that provides simple page-based routing as well as server-side rendering. To use Next.js with the Expo SDK, we recommend using [`@expo/next-adapter`](https://github.com/expo/expo-cli/tree/main/packages/next-adapter) library to handle the configuration.

Using Expo with Next.js means you can share some of your existing components and APIs across your mobile and web app. Next.js has its own CLI that you'll need to use when developing for the web platform, so you'll need to start your web projects with the Next.js CLI and not with `npx expo start`.

> Next.js can only be used with Expo for web as there is no support for Server-Side Rendering (SSR) for native apps.

Automatic setup
---------------

To quickly get started, create a new project using [with-nextjs](https://github.com/expo/examples/tree/master/with-nextjs) template:

Terminal

Copy

`-Â``npx create-expo-app -e with-nextjs`

* Native: `npx expo start` â start the Expo project
* Web: `npx next dev` â start the Next.js project

Manual setup
------------

### Install dependencies

Ensure you have `expo`, `next`, `@expo/next-adapter` installed in your project:

Terminal

Copy

`-Â``yarn add expo next @expo/next-adapter`

### Transpilation

Configure Next.js to transform language features:

Next.js with swc. (Recommended)

Using Next.js with SWC is recommended. You can configure the [babel.config.js](/versions/latest/config/babel) to only account for native:

babel.config.js

Copy

```
module.exports = function (api) {
  api.cache(true);
  return {
    presets: ['babel-preset-expo'],
  };
};

```

You will also have to [force Next.js to use SWC](https://nextjs.org/docs/messages/swc-disabled) by adding the following to your next.config.js:

next.config.js

Copy

```
module.exports = {
  experimental: {
    forceSwcTransforms: true,
  },
};

```

Next.js with Babel. (Not recommended)

Adjust your babel.config.js to conditionally add `next/babel` when bundling with webpack for web:

babel.config.js

Copy

```
module.exports = function (api) {
  // Detect web usage (this may change in the future if Next.js changes the loader)
  const isWeb = api.caller(
    caller =>
      caller && (caller.name === 'babel-loader' || caller.name === 'next-babel-turbo-loader')
  );
  return {
    presets: [
      // Only use next in the browser, it'll break your native project
      isWeb && require('next/babel'),
      'babel-preset-expo',
    ].filter(Boolean),
  };
};

```

### Next.js configuration

Add the following to your next.config.js:

next.config.js

Copy

```
const { withExpo } = require('@expo/next-adapter');

module.exports = withExpo({
  // transpilePackages is a Next.js +13.1 feature.
  // older versions can use next-transpile-modules
  transpilePackages: [
    'react-native',
    'react-native-web',
    'expo',
    // Add more React Native/Expo packages here...
  ],
});

```

The fully qualified Next.js config may look like:

next.config.js

Copy

```
const { withExpo } = require('@expo/next-adapter');

/** @type {import('next').NextConfig} */
const nextConfig = withExpo({
  reactStrictMode: true,
  swcMinify: true,
  transpilePackages: [
    'react-native',
    'react-native-web',
    'expo',
    // Add more React Native/Expo packages here...
  ],
  experimental: {
    forceSwcTransforms: true,
  },
});

module.exports = nextConfig;

```

### React Native Web styling

The package `react-native-web` builds on the assumption of reset CSS styles. Here's how you reset styles in Next.js using the pages directory.

pages/\_document.js

Copy

```
import { Children } from 'react';
import Document, { Html, Head, Main, NextScript } from 'next/document';
import { AppRegistry } from 'react-native';

// Follows the setup for react-native-web:
// https://necolas.github.io/react-native-web/docs/setup/#root-element
// Plus additional React Native scroll and text parity styles for various
// browsers.
// Force Next-generated DOM elements to fill their parent's height
const style = `
html, body, #__next {
  -webkit-overflow-scrolling: touch;
}
#__next {
  display: flex;
  flex-direction: column;
  height: 100%;
}
html {
  scroll-behavior: smooth;
  -webkit-text-size-adjust: 100%;
}
body {
  /* Allows you to scroll below the viewport; default value is visible */
  overflow-y: auto;
  overscroll-behavior-y: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  -ms-overflow-style: scrollbar;
}
`;

export default class MyDocument extends Document {
  static async getInitialProps({ renderPage }) {
    AppRegistry.registerComponent('main', () => Main);
    const { getStyleElement } = AppRegistry.getApplication('main');
    const page = await renderPage();
    const styles = [
      <style key="react-native-style" dangerouslySetInnerHTML={{ __html: style }} />,
      getStyleElement(),
    ];
    return { ...page, styles: Children.toArray(styles) };
  }

  render() {
    return (
      <Html style={{ height: '100%' }}>
        <Head />
        <body style={{ height: '100%', overflow: 'hidden' }}>
          <Main />
          <NextScript />
        </body>
      </Html>
    );
  }
}

```

pages/\_app.js

Copy

```
import Head from 'next/head';

export default function App({ Component, pageProps }) {
  return (
    <>
      <Head>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </Head>
      <Component {...pageProps} />
    </>
  );
}

```

Transpiling modules
-------------------

By default, modules in the React Native ecosystem are not transpiled to run in web browsers. React Native relies on advanced caching in Metro to reload quickly. Next.js uses webpack, which does not have the same level of caching, so no node modules are transpiled by default. You will have to manually mark every module you want to transpile with the `transpilePackages` option in next.config.js:

next.config.js

Copy

```
const { withExpo } = require('@expo/next-adapter');

module.exports = withExpo({
  experimental: {
    transpilePackages: [
      // NOTE: Even though `react-native` is never used in Next.js,
      // you need to list `react-native` because `react-native-web`
      // is aliased to `react-native`.
      'react-native',
      'react-native-web',
      'expo',
      // Add more React Native/Expo packages here...
    ],
  },
});

```

Deploy to Vercel
----------------

This is Vercel's preferred method for deploying Next.js projects to production.

1

Add a `build` script to your package.json:

package.json

Copy

```
{
  "scripts": {
    "build": "next build"
  }
}

```

2

Install the Vercel CLI:

Terminal

Copy

`-Â``npm i -g vercel`

3

Deploy to Vercel:

Terminal

Copy

`-Â``vercel`

Limitations or differences compared to the default Expo for Web
---------------------------------------------------------------

Using Next.js for the web means you will be bundling with the Next.js webpack config. This will lead to some core differences in how you develop your app vs your website.

* Expo Next.js adapter does not support the experimental app directory.
* For file-based routing on native, we recommend using [Expo Router](https://github.com/expo/router).

Contributing
------------

If you would like to help make Next.js support in Expo better, feel free to open a PR or submit an issue:

* [@expo/next-adapter](https://github.com/expo/expo-cli/tree/main/packages/next-adapter)

Troubleshooting
---------------

### Cannot use import statement outside a module

Figure out which module has the import statement and add it to the `transpilePackages` option in next.config.js:

next.config.js

Copy

```
const { withExpo } = require('@expo/next-adapter');

module.exports = withExpo({
  experimental: {
    transpilePackages: [
      'react-native',
      'react-native-web',
      'expo',
      // Add the failing package here, and restart the server...
    ],
  },
});

```

[Previous (More - Integrations)

Using ESLint and Prettier](/guides/using-eslint)[Next (More - Integrations)

Using LogRocket](/guides/using-logrocket)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/using-nextjs.mdx)
* Last updated on January 01, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Automatic setup](/guides/using-nextjs/#automatic-setup)[Manual setup](/guides/using-nextjs/#manual-setup)[Install dependencies](/guides/using-nextjs/#install-dependencies)[Transpilation](/guides/using-nextjs/#transpilation)[Next.js configuration](/guides/using-nextjs/#nextjs-configuration)[React Native Web styling](/guides/using-nextjs/#react-native-web-styling)[Transpiling modules](/guides/using-nextjs/#transpiling-modules)[Deploy to Vercel](/guides/using-nextjs/#deploy-to-vercel)[Limitations or differences compared to the default Expo for Web](/guides/using-nextjs/#limitations-or-differences-compared-to-the-default-expo-for-web)[Contributing](/guides/using-nextjs/#contributing)[Troubleshooting](/guides/using-nextjs/#troubleshooting)[Cannot use import statement outside a module](/guides/using-nextjs/#cannot-use-import-statement-outside-a-module)