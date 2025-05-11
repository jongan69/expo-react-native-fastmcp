Speeding Up CI Builds · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.73](/docs/0.73/speeding-ci-builds)

* [Next](/docs/next/getting-started)* [0.79](/docs/getting-started)* [0.78](/docs/0.78/getting-started)* [0.77](/docs/0.77/getting-started)* [0.76](/docs/0.76/getting-started)* [0.75](/docs/0.75/getting-started)* [0.74](/docs/0.74/getting-started)* [0.73](/docs/0.73/speeding-ci-builds)* [0.72](/docs/0.72/speeding-ci-builds)* [0.71](/docs/0.71/getting-started)* [0.70](/docs/0.70/getting-started)* [All versions](/versions)

[Development](#)

* [Guides](/docs/0.73/getting-started)* [Components](/docs/0.73/components-and-apis)* [APIs](/docs/0.73/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [The Basics](/docs/0.73/getting-started)

  * [Environment setup](/docs/0.73/environment-setup)

    * [Workflow](/docs/0.73/running-on-device)

      * [UI & Interaction](/docs/0.73/style)

        * [Debugging](/docs/0.73/debugging)

          * [Testing](/docs/0.73/testing-overview)

            * [Performance](/docs/0.73/performance)

              + [Performance Overview](/docs/0.73/performance)+ [Speeding up your Build phase](/docs/0.73/build-speed)+ [Speeding Up CI Builds](/docs/0.73/speeding-ci-builds)+ [Optimizing Flatlist Configuration](/docs/0.73/optimizing-flatlist-configuration)+ [RAM Bundles and Inline Requires](/docs/0.73/ram-bundles-inline-requires)+ [Profiling](/docs/0.73/profiling)+ [Profiling with Hermes](/docs/0.73/profile-hermes)* [JavaScript Runtime](/docs/0.73/javascript-environment)

                * [Native Modules](/docs/0.73/native-modules-intro)

                  * [Native Components](/docs/0.73/native-components-android)

                    * [Android and iOS guides](/docs/0.73/headless-js-android)

                      * [Experimental](/docs/0.73/the-new-architecture/landing-page)

This is documentation for React Native **0.73**, which is no longer in active development.

For up-to-date documentation, see the **[latest version](/docs/getting-started)** (0.79).

Version: 0.73

On this page

Speeding Up CI Builds
=====================

You or your company may have set up a Continuous Integration (CI) environment to test your React Native application.

A fast CI service is important for 2 reasons:

* The more time CI machines are running, the more they cost.
* The longer the CI jobs take to run, the longer the development loop.

It is therefore important to try and minimize the time the CI environment spends building React Native.

Disable Flipper for iOS[​](#disable-flipper-for-ios "Direct link to Disable Flipper for iOS")
---------------------------------------------------------------------------------------------

[Flipper](https://github.com/facebook/flipper) is a debugging tool shipped by default with React Native, to help developers debug and profile their React Native applications. However, Flipper is not required in CI: it is very unlikely that you or one of your collegue would have to debug the app built in the CI environment.

For iOS apps, Flipper is built every time the React Native framework is built and it may require some time to build, and this is time you can save.

Starting from React Native 0.71, we introduced a new flag in the template's Podfile: the [`NO_FLIPPER` flag](https://github.com/facebook/react-native/blob/main/packages/react-native/template/ios/Podfile#L20).

By default, the `NO_FLIPPER` flag is not set, therefore Flipper will be included by default in your app.

You can specify `NO_FLIPPER=1` when installing your iOS pods, to instruct React Native not to install Flipper. Typically, the command would look like this:

shell

```
# from the root folder of the react native project  
NO_FLIPPER=1 bundle exec pod install --project-directory=ios  

```

Add this command in your CI environment to skip the installation of Flipper dependencies and thus saving time and money.

### Handle Transitive Dependencies[​](#handle-transitive-dependencies "Direct link to Handle Transitive Dependencies")

Your app may be using some libraries which depends on the Flipper pods. If that's your case, disabling flipper with the `NO_FLIPPER` flag may not be enough: your app may fail to build in this case.

The proper way to handle this case is to add a custom configuration for react native, instructing the app to properly install the transitive dependency. To achieve that:

1. If you don't have it already, create a new file called `react-native.config.js`.
2. Exclude explicitly the transitive dependency from the `dependency` when the flag is turned on.

For example, the `react-native-flipper` library is an additional library that depends on Flipper. If your app uses that, you need to exclude it from the dependencies. Your `react-native.config.js` would look like this:

react-native.config.js

```
module.exports = {  
  // other fields  
  dependency: {  
    ...(process.env.NO_FLIPPER  
      ? {'react-native-flipper': {platforms: {ios: null}}}  
      : {}),  
  },  
};  

```

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/speeding-ci-builds.md)[Edit page for 0.73 release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.73/speeding-ci-builds.md)

Last updated on **Dec 8, 2023**

[Previous

Speeding up your Build phase](/docs/0.73/build-speed)[Next

Optimizing Flatlist Configuration](/docs/0.73/optimizing-flatlist-configuration)

* [Disable Flipper for iOS](#disable-flipper-for-ios)
  + [Handle Transitive Dependencies](#handle-transitive-dependencies)

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