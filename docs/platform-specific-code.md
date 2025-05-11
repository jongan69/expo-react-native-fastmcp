Platform-Specific Code · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/platform-specific-code)

* [Next](/docs/next/platform-specific-code)* [0.79](/docs/platform-specific-code)* [0.78](/docs/0.78/platform-specific-code)* [0.77](/docs/0.77/platform-specific-code)* [0.76](/docs/0.76/platform-specific-code)* [0.75](/docs/0.75/platform-specific-code)* [0.74](/docs/0.74/platform-specific-code)* [0.73](/docs/0.73/platform-specific-code)* [0.72](/docs/0.72/platform-specific-code)* [0.71](/docs/0.71/platform-specific-code)* [0.70](/docs/0.70/platform-specific-code)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [The Basics](/docs/getting-started)

  + [Introduction](/docs/getting-started)+ [Core Components and Native Components](/docs/intro-react-native-components)+ [React Fundamentals](/docs/intro-react)+ [Handling Text Input](/docs/handling-text-input)+ [Using a ScrollView](/docs/using-a-scrollview)+ [Using List Views](/docs/using-a-listview)+ [Troubleshooting](/docs/troubleshooting)+ [Platform-Specific Code](/docs/platform-specific-code)+ [More Resources](/docs/more-resources)* [Environment setup](/docs/environment-setup)

    * [Workflow](/docs/running-on-device)

      * [UI & Interaction](/docs/style)

        * [Debugging](/docs/debugging)

          * [Testing](/docs/testing-overview)

            * [Performance](/docs/performance)

              * [JavaScript Runtime](/docs/javascript-environment)

                * [Codegen](/docs/the-new-architecture/what-is-codegen)

                  * [Native Development](/docs/native-platform)

                    * [Android and iOS guides](/docs/headless-js-android)

                      * [Legacy Architecture](/docs/legacy/native-modules-intro)

On this page

Platform-Specific Code
======================

When building a cross-platform app, you'll want to re-use as much code as possible. Scenarios may arise where it makes sense for the code to be different, for example you may want to implement separate visual components for Android and iOS.

React Native provides two ways to organize your code and separate it by platform:

* Using the [`Platform` module](/docs/platform-specific-code#platform-module).
* Using [platform-specific file extensions](/docs/platform-specific-code#platform-specific-extensions).

Certain components may have properties that work on one platform only. All of these props are annotated with `@platform` and have a small badge next to them on the website.

Platform module[​](#platform-module "Direct link to Platform module")
---------------------------------------------------------------------

React Native provides a module that detects the platform in which the app is running. You can use the detection logic to implement platform-specific code. Use this option when only small parts of a component are platform-specific.

tsx

```
import {Platform, StyleSheet} from 'react-native';  
  
const styles = StyleSheet.create({  
  height: Platform.OS === 'ios' ? 200 : 100,  
});  

```

`Platform.OS` will be `ios` when running on iOS and `android` when running on Android.

There is also a `Platform.select` method available that, given an object where keys can be one of `'ios' | 'android' | 'native' | 'default'`, returns the most fitting value for the platform you are currently running on. That is, if you're running on a phone, `ios` and `android` keys will take preference. If those are not specified, `native` key will be used and then the `default` key.

tsx

```
import {Platform, StyleSheet} from 'react-native';  
  
const styles = StyleSheet.create({  
  container: {  
    flex: 1,  
    ...Platform.select({  
      ios: {  
        backgroundColor: 'red',  
      },  
      android: {  
        backgroundColor: 'green',  
      },  
      default: {  
        // other platforms, web for example  
        backgroundColor: 'blue',  
      },  
    }),  
  },  
});  

```

This will result in a container having `flex: 1` on all platforms, a red background color on iOS, a green background color on Android, and a blue background color on other platforms.

Since it accepts `any` value, you can also use it to return platform-specific components, like below:

tsx

```
const Component = Platform.select({  
  ios: () => require('ComponentIOS'),  
  android: () => require('ComponentAndroid'),  
})();  
  
<Component />;  

```

tsx

```
const Component = Platform.select({  
  native: () => require('ComponentForNative'),  
  default: () => require('ComponentForWeb'),  
})();  
  
<Component />;  

```

### Detecting the Android version Android [​](#detecting-the-android-version-android "Direct link to detecting-the-android-version-android")

On Android, the `Platform` module can also be used to detect the version of the Android Platform in which the app is running:

tsx

```
import {Platform} from 'react-native';  
  
if (Platform.Version === 25) {  
  console.log('Running on Nougat!');  
}  

```

**Note**: `Version` is set to the Android API version not the Android OS version. To find a mapping please refer to [Android Version History](https://en.wikipedia.org/wiki/Android_version_history#Overview).

### Detecting the iOS version iOS [​](#detecting-the-ios-version-ios "Direct link to detecting-the-ios-version-ios")

On iOS, the `Version` is a result of `-[UIDevice systemVersion]`, which is a string with the current version of the operating system. An example of the system version is "10.3". For example, to detect the major version number on iOS:

tsx

```
import {Platform} from 'react-native';  
  
const majorVersionIOS = parseInt(Platform.Version, 10);  
if (majorVersionIOS <= 9) {  
  console.log('Work around a change in behavior');  
}  

```

Platform-specific extensions[​](#platform-specific-extensions "Direct link to Platform-specific extensions")
------------------------------------------------------------------------------------------------------------

When your platform-specific code is more complex, you should consider splitting the code out into separate files. React Native will detect when a file has a `.ios.` or `.android.` extension and load the relevant platform file when required from other components.

For example, say you have the following files in your project:

shell

```
BigButton.ios.js  
BigButton.android.js  

```

You can then import the component as follows:

tsx

```
import BigButton from './BigButton';  

```

React Native will automatically pick up the right file based on the running platform.

Native-specific extensions (i.e. sharing code with NodeJS and Web)[​](#native-specific-extensions-ie-sharing-code-with-nodejs-and-web "Direct link to Native-specific extensions (i.e. sharing code with NodeJS and Web)")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can also use the `.native.js` extension when a module needs to be shared between NodeJS/Web and React Native but it has no Android/iOS differences. This is especially useful for projects that have common code shared among React Native and ReactJS.

For example, say you have the following files in your project:

shell

```
Container.js # picked up by webpack, Rollup or any other Web bundler  
Container.native.js # picked up by the React Native bundler for both Android and iOS (Metro)  

```

You can still import it without the `.native` extension, as follows:

tsx

```
import Container from './Container';  

```

**Pro tip:** Configure your Web bundler to ignore `.native.js` extensions in order to avoid having unused code in your production bundle, thus reducing the final bundle size.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/platform-specific-code.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/platform-specific-code.md)

Last updated on **Apr 14, 2025**

[Previous

Troubleshooting](/docs/troubleshooting)[Next

More Resources](/docs/more-resources)

* [Platform module](#platform-module)
  + [Detecting the Android version

    Android](#detecting-the-android-version-android)+ [Detecting the iOS version

      iOS](#detecting-the-ios-version-ios)* [Platform-specific extensions](#platform-specific-extensions)* [Native-specific extensions (i.e. sharing code with NodeJS and Web)](#native-specific-extensions-ie-sharing-code-with-nodejs-and-web)

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