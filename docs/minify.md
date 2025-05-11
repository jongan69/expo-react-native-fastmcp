Minifying JavaScript - Expo Documentation

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

[Bundle with Metro](/guides/customizing-metro)[Analyzing JavaScript bundles](/guides/analyzing-bundles)[Tree shaking](/guides/tree-shaking)[Minification](/guides/minify)[Why Metro?](/guides/why-metro)

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

Minifying JavaScript
====================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/minify.mdx)

Learn about customizing the JavaScript minification process in Expo CLI with Metro bundler.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/minify.mdx)

---

Minification is an optimization build step. It removes unnecessary characters such as collapses whitespace, removes comments, and shortens static operations, from the source code. This process reduces the final size and improves load times.

Minification in Expo CLI
------------------------

In Expo CLI, minification is performed on JavaScript files during the production export (when `npx expo export`, `npx expo export:embed`, `eas build`, and so on, commands run).

For example, consider following code snippet in a project:

Input

Copy

```
// This comment will be stripped
console.log('a' + ' ' + 'long' + ' string' + ' to ' + 'collapse');

```

This will be minified by the Expo CLI:

Output

Copy

```
console.log('a long string to collapse');

```

> Tip: Comments can be preserved by using the `/** @preserve */` directive.

The default minification of Expo CLI is sufficient for most projects. However, you can customize the minifier to optimize for speed or remove additional features like logs.

Remove console logs
-------------------

You can remove console logs from your production build. Use the `drop_console` option in the Terser minifier config.

metro.config.js

Copy

```
const { getDefaultConfig } = require('expo/metro-config');

const config = getDefaultConfig(__dirname);

config.transformer.minifierConfig = {
  compress: {
    // The option below removes all console logs statements in production.
    drop_console: true,
  },
};

module.exports = config;

```

You can also pass an array of console types to drop if you want to preserve certain logs. For example: `drop_console: ['log', 'info']` will remove `console.log` and `console.info` but preserve `console.warn` and `console.error`.

Customizing the minifier
------------------------

Different minifiers have tradeoffs between speed and compression. You can customize the minifier used by Expo CLI by modifying the metro.config.js file in your project.

### Terser

> [`terser`](https://github.com/terser/terser) is the default minifier ([Metro@0.73.0 changelog](https://github.com/facebook/metro/releases/tag/v0.73.0)).

1

To install Terser in a project, run the command:

Terminal

Copy

`-Â``yarn add --dev metro-minify-terser`

2

Set Terser as a minifier with `transformer.minifierPath`, and pass in [`terser` options](https://github.com/terser/terser#compress-options) to `transformer.minifierConfig`.

metro.config.js

Copy

```
const { getDefaultConfig } = require('expo/metro-config');

const config = getDefaultConfig(__dirname);

config.transformer.minifierPath = 'metro-minify-terser';
config.transformer.minifierConfig = {
  // Terser options...
};

module.exports = config;

```

### Unsafe Terser options

For additional compression that may not work in all JavaScript engines, enable the [`unsafe` `compress` options](https://terser.org/docs/miscellaneous/#the-unsafe-compress-option):

metro.config.js

Copy

```
const { getDefaultConfig } = require('expo/metro-config');

const config = getDefaultConfig(__dirname);

config.transformer.minifierPath = 'metro-minify-terser';

config.transformer.minifierConfig = {
  compress: {
    // Enable all unsafe optimizations.
    unsafe: true,
    unsafe_arrows: true,
    unsafe_comps: true,
    unsafe_Function: true,
    unsafe_math: true,
    unsafe_symbols: true,
    unsafe_methods: true,
    unsafe_proto: true,
    unsafe_regexp: true,
    unsafe_undefined: true,
    unused: true,
  },
};

module.exports = config;

```

### esbuild

[`esbuild`](https://esbuild.github.io/) is used to minify exponentially faster than `uglify-es` and `terser`. For more information, see [`metro-minify-esbuild`](https://github.com/EvanBacon/metro-minify-esbuild#usage) usage.

### Uglify

For projects SDK 48 and above, you can use [`uglify-es`](https://github.com/mishoo/UglifyJS) by following the steps below:

1

To install Uglify in a project, run the command:

Terminal

Copy

`-Â``yarn add --dev metro-minify-uglify`

> Make sure the version of `metro-minify-uglify` matches the version of `metro` in your project.

2

Set Uglify as a minifier with `transformer.minifierPath`, and pass in [options](https://github.com/mishoo/UglifyJS#compress-options) to `transformer.minifierConfig`.

metro.config.js

Copy

```
const { getDefaultConfig } = require('expo/metro-config');

const config = getDefaultConfig(__dirname);

config.transformer.minifierPath = 'metro-minify-uglify';
config.transformer.minifierConfig = {
  // Options: https://github.com/mishoo/UglifyJS#compress-options
};

module.exports = config;

```

[Previous (Development process - Bundling)

Tree shaking](/guides/tree-shaking)[Next (Development process - Bundling)

Why Metro?](/guides/why-metro)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/minify.mdx)
* Last updated on June 19, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Minification in Expo CLI](/guides/minify/#minification-in-expo-cli)[Remove console logs](/guides/minify/#remove-console-logs)[Customizing the minifier](/guides/minify/#customizing-the-minifier)[Terser](/guides/minify/#terser)[Unsafe Terser options](/guides/minify/#unsafe-terser-options)[esbuild](/guides/minify/#esbuild)[Uglify](/guides/minify/#uglify)