Metro · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/metro)

* [Next](/docs/next/metro)* [0.79](/docs/metro)* [0.78](/docs/0.78/metro)* [0.77](/docs/0.77/metro)* [0.76](/docs/0.76/metro)* [0.75](/docs/0.75/metro)* [0.74](/docs/0.74/metro)* [0.73](/docs/0.73/metro)* [0.72](/docs/0.72/metro)* [0.71](/docs/0.71/getting-started)* [0.70](/docs/0.70/getting-started)* [All versions](/versions)

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

Metro
=====

React Native uses [Metro](https://metrobundler.dev/) to build your JavaScript code and assets.

Configuring Metro[​](#configuring-metro "Direct link to Configuring Metro")
---------------------------------------------------------------------------

Configuration options for Metro can be customized in your project's `metro.config.js` file. This can export either:

* **An object (recommended)** that will be merged on top of Metro's internal config defaults.
* [**A function**](#advanced-using-a-config-function) that will be called with Metro's internal config defaults and should return a final config object.

tip

Please see [**Configuring Metro**](https://metrobundler.dev/docs/configuration) on the Metro website for documentation on all available config options.

In React Native, your Metro config should extend either [`@react-native/metro-config`](https://www.npmjs.com/package/@react-native/metro-config) or [`@expo/metro-config`](https://www.npmjs.com/package/@expo/metro-config). These packages contain essential defaults necessary to build and run React Native apps.

Below is the default `metro.config.js` file in a React Native template project:

js

```
const {getDefaultConfig, mergeConfig} = require('@react-native/metro-config');  
  
/**  
 * Metro configuration  
 * https://metrobundler.dev/docs/configuration  
 *  
 * @type {import('metro-config').MetroConfig}  
 */  
const config = {};  
  
module.exports = mergeConfig(getDefaultConfig(__dirname), config);  

```

Metro options you wish to customize can be done so within the `config` object.

### Advanced: Using a config function[​](#advanced-using-a-config-function "Direct link to Advanced: Using a config function")

Exporting a config function is an opt-in to managing the final config yourself — **Metro will not apply any internal defaults**. This pattern can be useful when needing to read the base default config object from Metro or to set options dynamically.

info

**From `@react-native/metro-config` 0.72.1**, it is no longer necessary to use a config function to access the complete default config. See the **Tip** section below.

js

```
const {getDefaultConfig, mergeConfig} = require('@react-native/metro-config');  
  
module.exports = function (baseConfig) {  
  const defaultConfig = mergeConfig(baseConfig, getDefaultConfig(__dirname));  
  const {resolver: {assetExts, sourceExts}} = defaultConfig;  
  
  return mergeConfig(  
    defaultConfig,  
    {  
      resolver: {  
        assetExts: assetExts.filter(ext => ext !== 'svg'),  
        sourceExts: [...sourceExts, 'svg'],  
      },  
    },  
  );  
};  

```

tip

Using a config function is for advanced use cases. A simpler method than the above, e.g. for customising `sourceExts`, would be to read these defaults from `@react-native/metro-config`.

**Alternative**

js

```
const defaultConfig = getDefaultConfig(__dirname);  
  
const config = {  
  resolver: {  
    sourceExts: [...defaultConfig.resolver.sourceExts, 'svg'],  
  },  
};  
  
module.exports = mergeConfig(defaultConfig, config);  

```

**However!**, we recommend copying and editing when overriding these config values — placing the source of truth in your config file.

✅ **Recommended**

js

```
const config = {  
  resolver: {  
    sourceExts: ['js', 'ts', 'tsx', 'svg'],  
  },  
};  

```

Learn more about Metro[​](#learn-more-about-metro "Direct link to Learn more about Metro")
------------------------------------------------------------------------------------------

* [Metro website](https://metrobundler.dev/)
* [Video: "Metro & React Native DevX" talk at App.js 2023](https://www.youtube.com/watch?v=c9D4pg0y9cI)

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/metro.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/metro.md)

Last updated on **Apr 14, 2025**

[Previous

Fast Refresh](/docs/fast-refresh)[Next

Using Libraries](/docs/libraries)

* [Configuring Metro](#configuring-metro)
  + [Advanced: Using a config function](#advanced-using-a-config-function)* [Learn more about Metro](#learn-more-about-metro)

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