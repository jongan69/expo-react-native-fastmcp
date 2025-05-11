Using ESLint and Prettier - Expo Documentation

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

Using ESLint and Prettier
=========================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/using-eslint.mdx)

A guide on configuring ESLint and Prettier to format Expo apps.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/using-eslint.mdx)

---

[ESLint](https://eslint.org/) is a JavaScript linter that helps you find and fix errors in your code. It's a great tool to help you write better code and catch mistakes before they make it to production. In conjunction, you can use [Prettier](https://prettier.io/docs/en/), a code formatter that ensures all the code files follow a consistent styling.

This guide provides steps to set up and configure ESLint and Prettier.

ESLint
------

### Setup

> From SDK 53 onwards, the default ESLint config file uses the [Flat config](https://eslint.org/blog/2022/08/new-config-system-part-2/) format. It also supports legacy config. For SDK 52 and below, the default ESLint config file uses legacy config and does not support Flat config.

To set up ESLint in your Expo project, you can use the Expo CLI to install the necessary dependencies. Running this command also creates a eslint.config.js file at the root of your project which extends configuration from [`eslint-config-expo`](https://github.com/expo/expo/tree/main/packages/eslint-config-expo).

Terminal

Copy

`# Install and configure ESLint`

`-Â``npx expo lint`

### Usage

> Recommended: If you're using VS Code, install the [ESLint extension](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) to lint your code as you type.

You can lint your code manually from the command line with the `npx expo lint` script:

Terminal

Copy

`# After ESLint has been configured, run the command again to lint your code.`

`-Â``npx expo lint`

Running the above command will run the `lint` script from package.json.

Terminal

`# Example output for npx expo lint command`  
`/app/components/HelloWave.tsx` `22:6 warning React Hook useEffect has a missing dependency: "rotateAnimation".` `Either include it or remove the dependency array react-hooks/exhaustive-deps`  
`â 1 problem (0 errors, 1 warning)`

### Environment configuration

ESLint is generally configured for a single environment. However, the source code is written in JavaScript in an Expo app that runs in multiple different environments. For example, the app.config.js, metro.config.js, babel.config.js, and app/+html.tsx files are run in a Node.js environment. It means they have access to the global `__dirname` variable and can use Node.js modules such as `path`. Standard Expo project files like app/index.js can be run in Hermes, Node.js, or the web browser.

You can add the `eslint-env` comment directive to the top of a file to tell ESLint which environment the file is running in. For example, to tell ESLint that a file is run in Node.js, add the following comment to the top of the file:

metro.config.js

Copy

```
/* eslint-env node */
const { getDefaultConfig } = require('expo/metro-config');

/** @type {import('expo/metro-config').MetroConfig} */
const config = getDefaultConfig(
  __dirname
);

module.exports = config;

```

Prettier
--------

### Installation

To install Prettier in your project:

macOS/Linux

Windows

Terminal

Copy

`-Â``npx expo install prettier eslint-config-prettier eslint-plugin-prettier --dev`

Terminal

Copy

`-Â``npx expo install prettier eslint-config-prettier eslint-plugin-prettier "--" --dev`

### Setup

Flat config

Legacy config

To integrate Prettier with ESLint, update your eslint.config.js:

eslint.config.js

Copy

```
const { defineConfig } = require('eslint/config');
const expoConfig = require('eslint-config-expo/flat');
const eslintPluginPrettierRecommended = require('eslint-plugin-prettier/recommended');

module.exports = defineConfig([
  expoConfig,
  eslintPluginPrettierRecommended,
  {
    ignores: ['dist/*'],
  },
]);

```

To integrate Prettier with ESlint, update your .eslintrc.js:

.eslintrc.js

Copy

```
module.exports = {
  extends: ['expo', 'prettier'],
  ignorePatterns: ['/dist/*'],
  plugins: ['prettier'],
  rules: {
    'prettier/prettier': 'error',
  },
};

```

> Note: In the above configuration, you can use `"prettier/prettier": "warn"` if you prefer these formatting issues as warnings instead of errors.

Now, when you run `npx expo lint`, anything that is not aligned with Prettier formatting will be caught as an error.

To customize Prettier settings, create a .prettierrc file at the root of your project and add your configuration.

[Custom Prettier configuration

Learn more about customizing Prettier configuration.](https://github.com/expo/expo/tree/main/packages/eslint-config-universe#customizing-prettier)

Troubleshooting
---------------

### ESLint is not updating in VS Code

If you're using VS Code, install the [ESLint extension](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) to lint your code as you type. You can try restarting the ESLint server by running the command `ESLint: Restart ESLint Server` from the [command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette).

### ESLint is slow

ESLint can be slow to run on large projects. The easiest way to speed up the process is to lint fewer files. Add a .eslintignore file to your project root to ignore certain files and directories such as:

.eslintignore

Copy

```
/.expo
node_modules

```

Migration to Flat config
------------------------

> Note: Flat config is supported in Expo SDK 53 and above.

Upgrade ESLint and `eslint-config-expo`:

macOS/Linux

Windows

Terminal

Copy

`-Â``npx expo install eslint eslint-config-expo --dev`

Terminal

Copy

`-Â``npx expo install eslint eslint-config-expo "--" --dev`

If you haven't customized your ESLint config at all, delete your .eslintrc.js and generate the new config with:

Terminal

Copy

`-Â``npx expo lint`

Alternatively, migrate your config based on the [ESLint's migration guide](https://eslint.org/docs/latest/use/configure/migration-guide). `npx expo lint` supports both legacy and flat config, so the new config will automatically be picked up by the CLI.

[Previous (More - Integrations)

Using Google authentication](/guides/google-authentication)[Next (More - Integrations)

Using Next.js](/guides/using-nextjs)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/using-eslint.mdx)
* Last updated on May 02, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[ESLint](/guides/using-eslint/#eslint)[Setup](/guides/using-eslint/#setup)[Usage](/guides/using-eslint/#usage)[Environment configuration](/guides/using-eslint/#environment-configuration)[Prettier](/guides/using-eslint/#prettier)[Installation](/guides/using-eslint/#installation)[Setup](/guides/using-eslint/#setup-1)[Troubleshooting](/guides/using-eslint/#troubleshooting)[ESLint is not updating in VS Code](/guides/using-eslint/#eslint-is-not-updating-in-vs-code)[ESLint is slow](/guides/using-eslint/#eslint-is-slow)[Migration to Flat config](/guides/using-eslint/#migration-to-flat-config)