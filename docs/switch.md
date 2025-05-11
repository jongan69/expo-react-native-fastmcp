Switch · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/switch)

* [Next](/docs/next/switch)* [0.79](/docs/switch)* [0.78](/docs/0.78/switch)* [0.77](/docs/0.77/switch)* [0.76](/docs/0.76/switch)* [0.75](/docs/0.75/switch)* [0.74](/docs/0.74/switch)* [0.73](/docs/0.73/switch)* [0.72](/docs/0.72/switch)* [0.71](/docs/0.71/switch)* [0.70](/docs/0.70/switch)* [All versions](/versions)

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

Switch
======

Renders a boolean input.

This is a controlled component that requires an `onValueChange` callback that updates the `value` prop in order for the component to reflect user actions. If the `value` prop is not updated, the component will continue to render the supplied `value` prop instead of the expected result of any user actions.

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

### `disabled`[​](#disabled "Direct link to disabled")

If true the user won't be able to toggle the switch.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | bool `false` | | | |

---

### `ios_backgroundColor` iOS [​](#ios_backgroundcolor-ios "Direct link to ios_backgroundcolor-ios")

On iOS, custom color for the background. This background color can be seen either when the switch value is `false` or when the switch is disabled (and the switch is translucent).

|  |  |
| --- | --- |
| Type|  | | --- | | [color](/docs/colors) | |

---

### `onChange`[​](#onchange "Direct link to onchange")

Invoked when the user tries to change the value of the switch. Receives the change event as an argument. If you want to only receive the new value, use `onValueChange` instead.

|  |  |
| --- | --- |
| Type|  | | --- | | function | |

---

### `onValueChange`[​](#onvaluechange "Direct link to onvaluechange")

Invoked when the user tries to change the value of the switch. Receives the new value as an argument. If you want to instead receive an event, use `onChange`.

|  |  |
| --- | --- |
| Type|  | | --- | | function | |

---

### `thumbColor`[​](#thumbcolor "Direct link to thumbcolor")

Color of the foreground switch grip. If this is set on iOS, the switch grip will lose its drop shadow.

|  |  |
| --- | --- |
| Type|  | | --- | | [color](/docs/colors) | |

---

### `trackColor`[​](#trackcolor "Direct link to trackcolor")

Custom colors for the switch track.

*iOS*: When the switch value is `false`, the track shrinks into the border. If you want to change the color of the background exposed by the shrunken track, use [`ios_backgroundColor`](/docs/switch#ios_backgroundColor).

|  |  |
| --- | --- |
| Type|  | | --- | | `object: {false: color, true: color}` | |

---

### `value`[​](#value "Direct link to value")

The value of the switch. If true the switch will be turned on. Default value is false.

|  |  |
| --- | --- |
| Type|  | | --- | | bool | |

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/switch.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/switch.md)

Last updated on **Apr 14, 2025**

[Previous

StatusBar](/docs/statusbar)[Next

Text](/docs/text)

* [Example](#example)* [Props](#props)
    + [View Props](#view-props)+ [`disabled`](#disabled)+ [`ios_backgroundColor`

          iOS](#ios_backgroundcolor-ios)+ [`onChange`](#onchange)+ [`onValueChange`](#onvaluechange)+ [`thumbColor`](#thumbcolor)+ [`trackColor`](#trackcolor)+ [`value`](#value)

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