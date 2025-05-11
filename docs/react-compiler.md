React Compiler - Expo Documentation

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

[Work with monorepos](/guides/monorepos)[View logs](/workflow/logging)[Development and production modes](/workflow/development-mode)[Common development errors](/workflow/common-development-errors)[Android Studio Emulator](/workflow/android-studio-emulator)[iOS Simulator](/workflow/ios-simulator)[New Architecture](/guides/new-architecture)[React Compiler](/guides/react-compiler)

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

React Compiler
==============

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/react-compiler.mdx)

Learn how to enable and use the React Compiler in Expo apps.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/react-compiler.mdx)

---

> Warning: React Compiler is experimental. Currently, it is on hold and we'll soon provide more updates on its usage.

The new [React Compiler](https://react.dev/learn/react-compiler) automatically memoizes components and hooks to enable fine-grained reactivity. This can lead to significant performance improvements in your app. The React Compiler is currently experimental and is not enabled by default. You can enable it in your app by following the instructions below.

Enabling React Compiler
-----------------------

1

[Check how compatible](https://react.dev/learn/react-compiler#checking-compatibility) your project is with the React Compiler.

Terminal

Copy

`-Â``npx react-compiler-healthcheck@latest`

This will generally verify if your app is following the [rules of React](https://react.dev/reference/rules).

2

Install `babel-plugin-react-compiler` and the React compiler runtime in your project:

SDK 53 and above

SDK 52 and below

Terminal

Copy

`-Â``npx expo install babel-plugin-react-compiler@beta`

Terminal

Copy

`-Â``npx expo install babel-plugin-react-compiler@beta react-compiler-runtime@beta`

3

Toggle on the React Compiler experiment in your app config file:

app.json

Copy

```
{
  "experiments": {
    "reactCompiler": true
  }
}

```

### Enabling the linter

> In the future, all of the following steps below will be automated by Expo CLI.

Additionally, you should use the ESLint plugin to continuously enforce the rules of React in your project.

1

Run [`npx expo lint`](/guides/using-eslint#eslint) to ensure ESLint is setup in your app, then install the ESLint plugin for React Compiler:

Terminal

Copy

`-Â``npx expo install eslint-plugin-react-compiler`

2

Update your [ESLint configuration](/guides/using-eslint) to include the plugin:

.eslintrc.js

Copy

```
// https://docs.expo.dev/guides/using-eslint/
const { defineConfig } = require('eslint/config');
const expoConfig = require('eslint-config-expo/flat');

module.exports = defineConfig([
  expoConfig,
  {
    ignores: ['dist/*'],
    plugins: ['react-compiler'],
    rules: {
      'react-compiler/react-compiler': 'error',
    },
  },
]);

```

Incremental adoption
--------------------

You can incrementally adopt the React Compiler in your app using a few strategies:

1

Configure the Babel plugin to only run on specific files or components. To do this:

1. If your project doesn't have [babel.config.js](/versions/latest/config/babel), create one by running `npx expo customize babel.config.js`.
2. Add the following configuration to babel.config.js:

babel.config.js

Copy

```
module.exports = function (api) {
  api.cache(true);

  return {
    presets: [
      [
        'babel-preset-expo',
        {
          'react-compiler': {
            sources: filename => {
              // Match file names to include in the React Compiler.
              return filename.includes('src/path/to/dir');
            },
          },
        },
      ],
    ],
  };
};

```

Whenever you change your babel.config.js file, you need to restart the Metro bundler to apply the changes:

Terminal

Copy

`-Â``npx expo start --clear`

2

Use the `"use no memo"` directive to opt out of the React Compiler for specific components or files.

```
function MyComponent() {
  'use no memo';

  return <Text>Will not be optimized</Text>;
}

```

Usage
-----

> To better understand how React Compiler works, check out the [React Playground](https://playground.react.dev/).

Improvements are primarily automatic. You can remove instances of `useCallback`, `useMemo`, and `React.memo` in favor of the automatic memoization. Class components will not be optimized. Instead, migrate to function components.

Expo's implementation of the React Compiler will only run on application code (no node modules), and only when bundling for the client (disabled in server rendering).

Configuration
-------------

You can pass additional settings to the React Compiler Babel plugin by using the `react-compiler` object in the Babel configuration:

babel.config.js

Copy

```
module.exports = function (api) {
  api.cache(true);

  return {
    presets: [
      [
        'babel-preset-expo',
        {
          'react-compiler': {
            // Passed directly to the React Compiler Babel plugin.
            compilationMode: 'strict',
            panicThreshold: 'all_errors',
          },
          web: {
            'react-compiler': {
              // Web-only settings...
            },
          },
        },
      ],
    ],
  };
};

```

[Previous (Development process - Reference)

New Architecture](/guides/new-architecture)[Next (Expo Router)

Introduction](/router/introduction)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/react-compiler.mdx)
* Last updated on April 26, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Enabling React Compiler](/guides/react-compiler/#enabling-react-compiler)[Enabling the linter](/guides/react-compiler/#enabling-the-linter)[Incremental adoption](/guides/react-compiler/#incremental-adoption)[Usage](/guides/react-compiler/#usage)[Configuration](/guides/react-compiler/#configuration)