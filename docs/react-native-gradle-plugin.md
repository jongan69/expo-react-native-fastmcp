React Native Gradle Plugin · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/react-native-gradle-plugin)

* [Next](/docs/next/react-native-gradle-plugin)* [0.79](/docs/react-native-gradle-plugin)* [0.78](/docs/0.78/react-native-gradle-plugin)* [0.77](/docs/0.77/react-native-gradle-plugin)* [0.76](/docs/0.76/react-native-gradle-plugin)* [0.75](/docs/0.75/react-native-gradle-plugin)* [0.74](/docs/0.74/react-native-gradle-plugin)* [0.73](/docs/0.73/react-native-gradle-plugin)* [0.72](/docs/0.72/react-native-gradle-plugin)* [0.71](/docs/0.71/react-native-gradle-plugin)* [0.70](/docs/0.70/getting-started)* [All versions](/versions)

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

                      + Android

                        - [Headless JS](/docs/headless-js-android)- [Publishing to Google Play Store](/docs/signed-apk-android)- [Communication between native and React Native](/docs/communication-android)- [React Native Gradle Plugin](/docs/react-native-gradle-plugin)+ iOS

                          - [Linking Libraries](/docs/linking-libraries-ios)- [Running On Simulator](/docs/running-on-simulator-ios)- [Communication between native and React Native](/docs/communication-ios)- [App Extensions](/docs/app-extensions)- [Publishing to Apple App Store](/docs/publishing-to-app-store)* [Legacy Architecture](/docs/legacy/native-modules-intro)

On this page

React Native Gradle Plugin
==========================

This guide describes how to configure the **React Native Gradle Plugin** (often referred as RNGP), when building your React Native application for Android.

Using the plugin[​](#using-the-plugin "Direct link to Using the plugin")
------------------------------------------------------------------------

The React Native Gradle Plugin is distributed as a separate NPM package which is installed automatically with `react-native`.

The plugin is **already configured** for new projects created using `npx react-native init`. You don't need to do any extra steps to install it if you created your app with this command.

If you're integrating React Native into an existing project, please refer to [the corresponding page](/docs/next/integration-with-existing-apps#configuring-gradle): it contains specific instructions on how to install the plugin.

Configuring the plugin[​](#configuring-the-plugin "Direct link to Configuring the plugin")
------------------------------------------------------------------------------------------

By default, the plugin will work **out of the box** with sensible defaults. You should refer to this guide and customize the behavior only if you need it.

To configure the plugin you can modify the `react` block, inside your `android/app/build.gradle`:

groovy

```
apply plugin: "com.facebook.react"  
  
/**  
 * This is the configuration block to customize your React Native Android app.  
 * By default you don't need to apply any configuration, just uncomment the lines you need.  
 */  
react {  
  // Custom configuration goes here.  
}  

```

Each configuration key is described below:

### `root`[​](#root "Direct link to root")

This is the root folder of your React Native project, i.e. where the `package.json` file lives. Default is `..`. You can customize it as follows:

groovy

```
root = file("../")  

```

### `reactNativeDir`[​](#reactnativedir "Direct link to reactnativedir")

This is the folder where the `react-native` package lives. Default is `../node_modules/react-native`.
If you're in a monorepo or using a different package manager, you can use adjust `reactNativeDir` to your setup.

You can customize it as follows:

groovy

```
reactNativeDir = file("../node_modules/react-native")  

```

### `codegenDir`[​](#codegendir "Direct link to codegendir")

This is the folder where the `react-native-codegen` package lives. Default is `../node_modules/react-native-codegen`.
If you're in a monorepo or using a different package manager, you can adjust `codegenDir` to your setup.

You can customize it as follows:

groovy

```
codegenDir = file("../node_modules/@react-native/codegen")  

```

### `cliFile`[​](#clifile "Direct link to clifile")

This is the entrypoint file for the React Native CLI. Default is `../node_modules/react-native/cli.js`.
The entrypoint file is needed as the plugin needs to invoke the CLI for bundling and creating your app.

If you're in a monorepo or using a different package manager, you can adjust `cliFile` to your setup.
You can customize it as follows:

groovy

```
cliFile = file("../node_modules/react-native/cli.js")  

```

### `debuggableVariants`[​](#debuggablevariants "Direct link to debuggablevariants")

This is the list of variants that are debuggable (see [using variants](#using-variants) for more context on variants).

By default the plugin is considering as `debuggableVariants` only `debug`, while `release` is not. If you have other
variants (like `staging`, `lite`, etc.) you'll need to adjust this accordingly.

Variants that are listed as `debuggableVariants` will not come with a shipped bundle, so you'll need Metro to run them.

You can customize it as follows:

groovy

```
debuggableVariants = ["liteDebug", "prodDebug"]  

```

### `nodeExecutableAndArgs`[​](#nodeexecutableandargs "Direct link to nodeexecutableandargs")

This is the list of node command and arguments that should be invoked for all the scripts. By default is `[node]` but can be customized to add extra flags as follows:

groovy

```
nodeExecutableAndArgs = ["node"]  

```

### `bundleCommand`[​](#bundlecommand "Direct link to bundlecommand")

This is the name of the `bundle` command to be invoked when creating the bundle for your app. That's useful if you're using [RAM Bundles](https://reactnative.dev/docs/0.74/ram-bundles-inline-requires). By default is `bundle` but can be customized to add extra flags as follows:

groovy

```
bundleCommand = "ram-bundle"  

```

### `bundleConfig`[​](#bundleconfig "Direct link to bundleconfig")

This is the path to a configuration file that will be passed to `bundle --config <file>` if provided. Default is empty (no config file will be probided). More information on bundling config files can be found [on the CLI documentation](https://github.com/react-native-community/cli/blob/main/docs/commands.md#bundle). Can be customized as follow:

groovy

```
bundleConfig = file(../rn-cli.config.js)  

```

### `bundleAssetName`[​](#bundleassetname "Direct link to bundleassetname")

This is the name of the bundle file that should be generated. Default is `index.android.bundle`. Can be customized as follow:

groovy

```
bundleAssetName = "MyApplication.android.bundle"  

```

### `entryFile`[​](#entryfile "Direct link to entryfile")

The entry file used for bundle generation. The default is to search for `index.android.js` or `index.js`. Can be customized as follow:

groovy

```
entryFile = file("../js/MyApplication.android.js")  

```

### `extraPackagerArgs`[​](#extrapackagerargs "Direct link to extrapackagerargs")

A list of extra flags that will be passed to the `bundle` command. The list of available flags is in [the CLI documentation](https://github.com/react-native-community/cli/blob/main/docs/commands.md#bundle). Default is empty. Can be customized as follows:

groovy

```
extraPackagerArgs = []  

```

### `hermesCommand`[​](#hermescommand "Direct link to hermescommand")

The path to the `hermesc` command (the Hermes Compiler). React Native comes with a version of the Hermes compiler bundled with it, so you generally won't be needing to customize this. The plugin will use the correct compiler for your system by default.

### `hermesFlags`[​](#hermesflags "Direct link to hermesflags")

The list of flags to pass to `hermesc`. By default is `["-O", "-output-source-map"]`. You can customize it as follows

groovy

```
hermesFlags = ["-O", "-output-source-map"]  

```

### `enableBundleCompression`[​](#enablebundlecompression "Direct link to enablebundlecompression")

Whether the Bundle Asset should be compressed when packaged into a `.apk`, or not.

Disabling compression for the `.bundle` allows it to be directly memory-mapped to RAM, hence improving startup time - at the cost of a larger resulting app size on disk. Please note that the `.apk` download size will be mostly unaffected as the `.apk` files are compressed before downloading

By default this is disabled, and you should not turn it on, unless you're really concerned about disk space for your application.

Using Flavors & Build Variants[​](#using-flavors--build-variants "Direct link to Using Flavors & Build Variants")
-----------------------------------------------------------------------------------------------------------------

When building Android apps, you might want to use [custom flavors](https://developer.android.com/studio/build/build-variants#product-flavors) to have different versions of your app starting from the same project.

Please refer to the [official Android guide](https://developer.android.com/studio/build/build-variants) to configure custom build types (like `staging`) or custom flavors (like `full`, `lite`, etc.).
By default new apps are created with two build types (`debug` and `release`) and no custom flavors.

The combination of all the build types and all the flavors generates a set of **build variants**. For instance for `debug`/`staging`/`release` build types and `full`/`lite` you will have 6 build variants: `fullDebug`, `fullStaging`, `fullRelease` and so on.

If you're using custom variants beyond `debug` and `release`, you need to instruct the React Native Gradle Plugin specifying which of your variants are **debuggable** using the [`debuggableVariants`](#debuggablevariants) configuration as follows:

diff

```
apply plugin: "com.facebook.react"  
  
react {  
+ debuggableVariants = ["fullStaging", "fullDebug"]  
}  

```

This is necessary because the plugin will skip the JS bundling for all the `debuggableVariants`: you'll need Metro to run them. For example, if you list `fullStaging` in the `debuggableVariants`, you won't be able to publish it to a store as it will be missing the bundle.

What is the plugin doing under the hood?[​](#what-is-the-plugin-doing-under-the-hood "Direct link to What is the plugin doing under the hood?")
-----------------------------------------------------------------------------------------------------------------------------------------------

The React Native Gradle Plugin is responsible for configuring your Application build to ship React Native applications to production.
The plugin is also used inside 3rd party libraries, to run the [Codegen](https://github.com/reactwg/react-native-new-architecture/blob/main/docs/codegen.md) used for the New Architecture.

Here is a summary of the plugin responsibilities:

* Add a `createBundle<Variant>JsAndAssets` task for every non debuggable variant, that is responsible of invoking the `bundle`, `hermesc` and `compose-source-map` commands.
* Setting up the proper version of the `com.facebook.react:react-android` and `com.facebook.react:hermes-android` dependency, reading the React Native version from the `package.json` of `react-native`.
* Setting up the proper Maven repositories (Maven Central, Google Maven Repo, JSC local Maven repo, etc.) needed to consume all the necessary Maven Dependencies.
* Setting up the NDK to let you build apps that are using the New Architecture.
* Setting up the `buildConfigFields` so that you can know at runtime if Hermes or the New Architecture are enabled.
* Setting up the Metro DevServer Port as an Android resource so the app knows on which port to connect.
* Invoking the [React Native Codegen](https://github.com/reactwg/react-native-new-architecture/blob/main/docs/codegen.md) if a library or app is using the Codegen for the New Architecture.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/react-native-gradle-plugin.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/react-native-gradle-plugin.md)

Last updated on **Apr 14, 2025**

[Previous

Communication between native and React Native](/docs/communication-android)[Next

Linking Libraries](/docs/linking-libraries-ios)

* [Using the plugin](#using-the-plugin)* [Configuring the plugin](#configuring-the-plugin)
    + [`root`](#root)+ [`reactNativeDir`](#reactnativedir)+ [`codegenDir`](#codegendir)+ [`cliFile`](#clifile)+ [`debuggableVariants`](#debuggablevariants)+ [`nodeExecutableAndArgs`](#nodeexecutableandargs)+ [`bundleCommand`](#bundlecommand)+ [`bundleConfig`](#bundleconfig)+ [`bundleAssetName`](#bundleassetname)+ [`entryFile`](#entryfile)+ [`extraPackagerArgs`](#extrapackagerargs)+ [`hermesCommand`](#hermescommand)+ [`hermesFlags`](#hermesflags)+ [`enableBundleCompression`](#enablebundlecompression)* [Using Flavors & Build Variants](#using-flavors--build-variants)* [What is the plugin doing under the hood?](#what-is-the-plugin-doing-under-the-hood)

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