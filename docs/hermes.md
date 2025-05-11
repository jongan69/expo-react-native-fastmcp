Using Hermes · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/hermes)

* [Next](/docs/next/hermes)* [0.79](/docs/hermes)* [0.78](/docs/0.78/hermes)* [0.77](/docs/0.77/hermes)* [0.76](/docs/0.76/hermes)* [0.75](/docs/0.75/hermes)* [0.74](/docs/0.74/hermes)* [0.73](/docs/0.73/hermes)* [0.72](/docs/0.72/hermes)* [0.71](/docs/0.71/hermes)* [0.70](/docs/0.70/hermes)* [All versions](/versions)

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

                + [JavaScript Environment](/docs/javascript-environment)+ [Timers](/docs/timers)+ [Using Hermes](/docs/hermes)* [Codegen](/docs/the-new-architecture/what-is-codegen)

                  * [Native Development](/docs/native-platform)

                    * [Android and iOS guides](/docs/headless-js-android)

                      * [Legacy Architecture](/docs/legacy/native-modules-intro)

On this page

Using Hermes
============

[![](/docs/assets/HermesLogo.svg)](https://hermesengine.dev)

[Hermes](https://hermesengine.dev) is an open-source JavaScript engine optimized for React Native. For many apps, using Hermes will result in improved start-up time, decreased memory usage, and smaller app size when compared to JavaScriptCore.
Hermes is used by default by React Native and no additional configuration is required to enable it.

Bundled Hermes[​](#bundled-hermes "Direct link to Bundled Hermes")
------------------------------------------------------------------

React Native comes with a **bundled version** of Hermes.
We are building a version of Hermes for you whenever we release a new version of React Native. This will make sure you're consuming a version of Hermes which is fully compatible with the version of React Native you're using.

This change is fully transparent to users of React Native. You can still disable Hermes using the command described in this page.
You can [read more about the technical implementation on this page](/architecture/bundled-hermes).

Confirming Hermes is in use[​](#confirming-hermes-is-in-use "Direct link to Confirming Hermes is in use")
---------------------------------------------------------------------------------------------------------

If you've recently created a new app from scratch, you should see if Hermes is enabled in the welcome view:

![Where to find JS engine status in AwesomeProject](/assets/images/HermesApp-ae778d80caa321ba00b558b025dc9805.jpg)

A `HermesInternal` global variable will be available in JavaScript that can be used to verify that Hermes is in use:

jsx

```
const isHermes = () => !!global.HermesInternal;  

```

caution

If you are using a non-standard way of loading the JS bundle, it is possible that the `HermesInternal` variable is available but you aren't using the highly optimised pre-compiled bytecode.
Confirm that you are using the `.hbc` file and also benchmark the before/after as detailed below.

To see the benefits of Hermes, try making a release build/deployment of your app to compare. For example; from the root of your project:

* Android* iOS

* npm* Yarn

shell

```
npm run android -- --mode="release"  

```

shell

```
yarn android --mode release  

```

* npm* Yarn

shell

```
npm run ios -- --mode="Release"  

```

shell

```
yarn ios --mode Release  

```

This will compile JavaScript to Hermes Bytecode during build time which will improve your app's startup speed on device.

Switching back to JavaScriptCore[​](#switching-back-to-javascriptcore "Direct link to Switching back to JavaScriptCore")
------------------------------------------------------------------------------------------------------------------------

React Native also supports using JavaScriptCore as the [JavaScript engine](/docs/javascript-environment). Follow these instructions to opt-out of Hermes.

### Android[​](#android "Direct link to Android")

Edit your `android/gradle.properties` file and flip `hermesEnabled` back to false:

diff

```
# Use this property to enable or disable the Hermes JS engine.  
# If set to false, you will be using JSC instead.  
hermesEnabled=false  

```

### iOS[​](#ios "Direct link to iOS")

Edit your `ios/Podfile` file and make the change illustrated below:

diff

```
   use_react_native!(  
     :path => config[:reactNativePath],  
+    :hermes_enabled => false,  
     # An absolute path to your application root.  
     :app_path => "#{Pod::Config.instance.installation_root}/.."  
   )  

```

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/hermes.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/hermes.md)

Last updated on **Apr 14, 2025**

[Previous

Timers](/docs/timers)[Next

What is Codegen?](/docs/the-new-architecture/what-is-codegen)

* [Bundled Hermes](#bundled-hermes)* [Confirming Hermes is in use](#confirming-hermes-is-in-use)* [Switching back to JavaScriptCore](#switching-back-to-javascriptcore)
      + [Android](#android)+ [iOS](#ios)

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