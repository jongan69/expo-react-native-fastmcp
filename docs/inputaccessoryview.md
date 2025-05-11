InputAccessoryView · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/inputaccessoryview)

* [Next](/docs/next/inputaccessoryview)* [0.79](/docs/inputaccessoryview)* [0.78](/docs/0.78/inputaccessoryview)* [0.77](/docs/0.77/inputaccessoryview)* [0.76](/docs/0.76/inputaccessoryview)* [0.75](/docs/0.75/inputaccessoryview)* [0.74](/docs/0.74/inputaccessoryview)* [0.73](/docs/0.73/inputaccessoryview)* [0.72](/docs/0.72/inputaccessoryview)* [0.71](/docs/0.71/inputaccessoryview)* [0.70](/docs/0.70/inputaccessoryview)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [Core Components](/docs/components-and-apis)

  + [Core Components and APIs](/docs/components-and-apis)+ [ActivityIndicator](/docs/activityindicator)+ [Button](/docs/button)+ [FlatList](/docs/flatlist)+ [Image](/docs/image)+ [ImageBackground](/docs/imagebackground)+ [KeyboardAvoidingView](/docs/keyboardavoidingview)+ [Modal](/docs/modal)+ [Pressable](/docs/pressable)+ [RefreshControl](/docs/refreshcontrol)+ [ScrollView](/docs/scrollview)+ [SectionList](/docs/sectionlist)+ [StatusBar](/docs/statusbar)+ [Switch](/docs/switch)+ [Text](/docs/text)+ [TextInput](/docs/textinput)+ [TouchableHighlight](/docs/touchablehighlight)+ [TouchableOpacity](/docs/touchableopacity)+ [TouchableWithoutFeedback](/docs/touchablewithoutfeedback)+ [View](/docs/view)+ [VirtualizedList](/docs/virtualizedlist)+ [Android Components](/docs/drawerlayoutandroid)

                                              - [DrawerLayoutAndroid](/docs/drawerlayoutandroid)- [TouchableNativeFeedback](/docs/touchablenativefeedback)+ [iOS Components](/docs/inputaccessoryview)

                                                - [InputAccessoryView](/docs/inputaccessoryview)- [SafeAreaView](/docs/safeareaview)* [Props](/docs/image-style-props)

    * [Object Types](/docs/boxshadowvalue)

On this page

InputAccessoryView
==================

A component which enables customization of the keyboard input accessory view on iOS. The input accessory view is displayed above the keyboard whenever a `TextInput` has focus. This component can be used to create custom toolbars.

To use this component wrap your custom toolbar with the InputAccessoryView component, and set a `nativeID`. Then, pass that `nativeID` as the `inputAccessoryViewID` of whatever `TextInput` you desire. A basic example:

This component can also be used to create sticky text inputs (text inputs which are anchored to the top of the keyboard). To do this, wrap a `TextInput` with the `InputAccessoryView` component, and don't set a `nativeID`. For an example, look at [InputAccessoryViewExample.js](https://github.com/facebook/react-native/blob/main/packages/rn-tester/js/examples/InputAccessoryView/InputAccessoryViewExample.js).

---

Reference
=========

Props[​](#props "Direct link to Props")
---------------------------------------

### `backgroundColor`[​](#backgroundcolor "Direct link to backgroundcolor")

|  |  |
| --- | --- |
| Type|  | | --- | | [color](/docs/colors) | |

---

### `nativeID`[​](#nativeid "Direct link to nativeid")

An ID which is used to associate this `InputAccessoryView` to specified TextInput(s).

|  |  |
| --- | --- |
| Type|  | | --- | | string | |

---

### `style`[​](#style "Direct link to style")

|  |  |
| --- | --- |
| Type|  | | --- | | [View Style](/docs/view-style-props) | |

Known issues
============

* [react-native#18997](https://github.com/facebook/react-native/issues/18997): Doesn't support multiline `TextInput`
* [react-native#20157](https://github.com/facebook/react-native/issues/20157): Can't use with a bottom tab bar

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/inputaccessoryview.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/inputaccessoryview.md)

Last updated on **Apr 14, 2025**

[Previous

TouchableNativeFeedback](/docs/touchablenativefeedback)[Next

SafeAreaView](/docs/safeareaview)

* [Props](#props)
  + [`backgroundColor`](#backgroundcolor)+ [`nativeID`](#nativeid)+ [`style`](#style)

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