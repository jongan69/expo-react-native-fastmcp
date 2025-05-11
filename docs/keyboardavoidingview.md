KeyboardAvoidingView · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/keyboardavoidingview)

* [Next](/docs/next/keyboardavoidingview)* [0.79](/docs/keyboardavoidingview)* [0.78](/docs/0.78/keyboardavoidingview)* [0.77](/docs/0.77/keyboardavoidingview)* [0.76](/docs/0.76/keyboardavoidingview)* [0.75](/docs/0.75/keyboardavoidingview)* [0.74](/docs/0.74/keyboardavoidingview)* [0.73](/docs/0.73/keyboardavoidingview)* [0.72](/docs/0.72/keyboardavoidingview)* [0.71](/docs/0.71/keyboardavoidingview)* [0.70](/docs/0.70/keyboardavoidingview)* [All versions](/versions)

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

KeyboardAvoidingView
====================

This component will automatically adjust its height, position, or bottom padding based on the keyboard height to remain visible while the virtual keyboard is displayed.

Example[​](#example "Direct link to Example")
---------------------------------------------

---

Reference
=========

Props[​](#props "Direct link to Props")
---------------------------------------

### [View Props](/docs/view#props)[​](#view-props "Direct link to view-props")

Inherits [View Props](/docs/view#props).

---

### `behavior`[​](#behavior "Direct link to behavior")

Specify how to react to the presence of the keyboard.

> Android and iOS both interact with this prop differently. On both iOS and Android, setting `behavior` is recommended.

|  |  |
| --- | --- |
| Type|  | | --- | | enum(`'height'`, `'position'`, `'padding'`) | |

---

### `contentContainerStyle`[​](#contentcontainerstyle "Direct link to contentcontainerstyle")

The style of the content container (View) when behavior is `'position'`.

|  |  |
| --- | --- |
| Type|  | | --- | | [View Style](/docs/view-style-props) | |

---

### `enabled`[​](#enabled "Direct link to enabled")

Enabled or disabled KeyboardAvoidingView.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | boolean `true` | | | |

---

### `keyboardVerticalOffset`[​](#keyboardverticaloffset "Direct link to keyboardverticaloffset")

This is the distance between the top of the user screen and the react native view, may be non-zero in some use cases.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | number `0` | | | |

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/keyboardavoidingview.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/keyboardavoidingview.md)

Last updated on **Apr 14, 2025**

[Previous

ImageBackground](/docs/imagebackground)[Next

Modal](/docs/modal)

* [Example](#example)* [Props](#props)
    + [View Props](#view-props)+ [`behavior`](#behavior)+ [`contentContainerStyle`](#contentcontainerstyle)+ [`enabled`](#enabled)+ [`keyboardVerticalOffset`](#keyboardverticaloffset)

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