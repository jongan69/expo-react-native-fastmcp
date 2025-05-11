Other Debugging Methods · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/other-debugging-methods)

* [Next](/docs/next/other-debugging-methods)* [0.79](/docs/other-debugging-methods)* [0.78](/docs/0.78/other-debugging-methods)* [0.77](/docs/0.77/other-debugging-methods)* [0.76](/docs/0.76/other-debugging-methods)* [0.75](/docs/0.75/other-debugging-methods)* [0.74](/docs/0.74/other-debugging-methods)* [0.73](/docs/0.73/other-debugging-methods)* [0.72](/docs/0.72/getting-started)* [0.71](/docs/0.71/getting-started)* [0.70](/docs/0.70/getting-started)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [The Basics](/docs/getting-started)

  * [Environment setup](/docs/environment-setup)

    * [Workflow](/docs/running-on-device)

      * [UI & Interaction](/docs/style)

        * [Debugging](/docs/debugging)

          + [Debugging Basics](/docs/debugging)+ [React Native DevTools](/docs/react-native-devtools)+ [Debugging Native Code](/docs/debugging-native-code)+ [Debugging Release Builds](/docs/debugging-release-builds)+ [Other Debugging Methods](/docs/other-debugging-methods)* [Testing](/docs/testing-overview)

            * [Performance](/docs/performance)

              * [JavaScript Runtime](/docs/javascript-environment)

                * [Codegen](/docs/the-new-architecture/what-is-codegen)

                  * [Native Development](/docs/native-platform)

                    * [Android and iOS guides](/docs/headless-js-android)

                      * [Legacy Architecture](/docs/legacy/native-modules-intro)

On this page

Other Debugging Methods
=======================

This page covers how to use legacy JavaScript debugging methods. If you are getting started with a new React Native or Expo app, we recommend using [React Native DevTools](/docs/react-native-devtools).

Safari Developer Tools (direct JSC debugging)[​](#safari-developer-tools-direct-jsc-debugging "Direct link to Safari Developer Tools (direct JSC debugging)")
-------------------------------------------------------------------------------------------------------------------------------------------------------------

You can use Safari to debug the iOS version of your app when using [JavaScriptCore](https://trac.webkit.org/wiki/JavaScriptCore) (JSC) as your app's runtime.

1. **Physical devices only**: Open the Settings app, and navigate to Safari > Advanced, and make sure "Web Inspector" is turned on.
2. On your Mac, open Safari and enable the Develop menu. This can be found under Safari > Settings..., then the Advanced tab, then selecting "Show features for web developers".
3. Find your device under the Develop menu, and select the "JSContext" item from the submenu. This will open Safari's Web Inspector, which includes Console and Sources panels similar to Chrome DevTools.

![Opening Safari Web Inspector](/assets/images/debugging-safari-developer-tools-a67219e1ea0f852bbb150c988b00c3cf.jpg)

tip

While source maps may not be enabled by default, you can follow [this guide](https://blog.nparashuram.com/2019/10/debugging-react-native-ios-apps-with.html) or [video](https://www.youtube.com/watch?v=GrGqIIz51k4) to enable them and set break points at the right places in the source code.

tip

Every time the app is reloaded, a new JSContext is created. Choosing "Automatically Show Web Inspectors for JSContexts" saves you from having to select the latest JSContext manually.

Remote JavaScript Debugging (removed)[​](#remote-javascript-debugging-removed "Direct link to Remote JavaScript Debugging (removed)")
-------------------------------------------------------------------------------------------------------------------------------------

Important

Remote JavaScript Debugging has been removed as of React Native 0.79. See the original [deprecation announcement](https://github.com/react-native-community/discussions-and-proposals/discussions/734).

If you are on an older version of React Native, please go to the docs [for your version](/versions).

![The remote debugger window in Chrome](/assets/images/debugging-chrome-remote-debugger-09207af31fea81d1d97a81a0d96774ba.jpg)

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/other-debugging-methods.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/other-debugging-methods.md)

Last updated on **Apr 14, 2025**

[Previous

Debugging Release Builds](/docs/debugging-release-builds)[Next

Testing](/docs/testing-overview)

* [Safari Developer Tools (direct JSC debugging)](#safari-developer-tools-direct-jsc-debugging)* [Remote JavaScript Debugging (removed)](#remote-javascript-debugging-removed)

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