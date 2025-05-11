Improving User Experience · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/improvingux)

* [Next](/docs/next/improvingux)* [0.79](/docs/improvingux)* [0.78](/docs/0.78/improvingux)* [0.77](/docs/0.77/improvingux)* [0.76](/docs/0.76/improvingux)* [0.75](/docs/0.75/improvingux)* [0.74](/docs/0.74/improvingux)* [0.73](/docs/0.73/improvingux)* [0.72](/docs/0.72/improvingux)* [0.71](/docs/0.71/improvingux)* [0.70](/docs/0.70/improvingux)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

On this page

Improving User Experience
=========================

Configure text inputs[​](#configure-text-inputs "Direct link to Configure text inputs")
---------------------------------------------------------------------------------------

Entering text on touch phone is a challenge - small screen, software keyboard. But based on what kind of data you need, you can make it easier by properly configuring the text inputs:

* Focus the first field automatically
* Use placeholder text as an example of expected data format
* Enable or disable autocapitalization and autocorrect
* Choose keyboard type (e.g. email, numeric)
* Make sure the return button focuses the next field or submits the form

Check out [`TextInput` docs](/docs/textinput) for more configuration options.

* TypeScript* JavaScript

Manage layout when keyboard is visible[​](#manage-layout-when-keyboard-is-visible "Direct link to Manage layout when keyboard is visible")
------------------------------------------------------------------------------------------------------------------------------------------

Software keyboard takes almost half of the screen. If you have interactive elements that can get covered by the keyboard, make sure they are still accessible by using the [`KeyboardAvoidingView` component](/docs/keyboardavoidingview).

* TypeScript* JavaScript

Make tappable areas larger[​](#make-tappable-areas-larger "Direct link to Make tappable areas larger")
------------------------------------------------------------------------------------------------------

On mobile phones it's hard to be very precise when pressing buttons. Make sure all interactive elements are 44x44 or larger. One way to do this is to leave enough space for the element, `padding`, `minWidth` and `minHeight` style values can be useful for that. Alternatively, you can use [`hitSlop` prop](/docs/touchablewithoutfeedback#hitslop) to increase interactive area without affecting the layout. Here's a demo:

Use Android Ripple[​](#use-android-ripple "Direct link to Use Android Ripple")
------------------------------------------------------------------------------

Android API 21+ uses the material design ripple to provide user with feedback when they touch an interactable area on the screen. React Native exposes this through the [`TouchableNativeFeedback` component](/docs/touchablenativefeedback). Using this touchable effect instead of opacity or highlight will often make your app feel much more fitting on the platform. That said, you need to be careful when using it because it doesn't work on iOS or on Android API < 21, so you will need to fallback to using one of the other Touchable components on iOS. You can use a library like [react-native-platform-touchable](https://github.com/react-community/react-native-platform-touchable) to handle the platform differences for you.

Screen orientation lock[​](#screen-orientation-lock "Direct link to Screen orientation lock")
---------------------------------------------------------------------------------------------

Multiple screen orientations should work fine by default unless you're using `Dimensions` API and don't handle orientation changes. If you don't want to support multiple screen orientations, you can lock the screen orientation to either portrait or landscape.

On iOS, in the General tab and Deployment Info section of Xcode enable the Device Orientation you want to support (ensure you have selected iPhone from the Devices menu when making the changes). For Android, open the AndroidManifest.xml file and within the activity element add `'android:screenOrientation="portrait"'` to lock to portrait or `'android:screenOrientation="landscape"'` to lock to landscape.

Learn more
==========

[Material Design](https://material.io/) and [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines) are great resources for learning more about designing for mobile platforms.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/improvingux.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/improvingux.md)

Last updated on **Apr 14, 2025**

* [Configure text inputs](#configure-text-inputs)* [Manage layout when keyboard is visible](#manage-layout-when-keyboard-is-visible)* [Make tappable areas larger](#make-tappable-areas-larger)* [Use Android Ripple](#use-android-ripple)* [Screen orientation lock](#screen-orientation-lock)

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