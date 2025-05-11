TouchableOpacity · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/touchableopacity)

* [Next](/docs/next/touchableopacity)* [0.79](/docs/touchableopacity)* [0.78](/docs/0.78/touchableopacity)* [0.77](/docs/0.77/touchableopacity)* [0.76](/docs/0.76/touchableopacity)* [0.75](/docs/0.75/touchableopacity)* [0.74](/docs/0.74/touchableopacity)* [0.73](/docs/0.73/touchableopacity)* [0.72](/docs/0.72/touchableopacity)* [0.71](/docs/0.71/touchableopacity)* [0.70](/docs/0.70/touchableopacity)* [All versions](/versions)

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

TouchableOpacity
================

> If you're looking for a more extensive and future-proof way to handle touch-based input, check out the [Pressable](/docs/pressable) API.

A wrapper for making views respond properly to touches. On press down, the opacity of the wrapped view is decreased, dimming it.

Opacity is controlled by wrapping the children in an `Animated.View`, which is added to the view hierarchy. Be aware that this can affect layout.

Example[​](#example "Direct link to Example")
---------------------------------------------

---

Reference
=========

Props[​](#props "Direct link to Props")
---------------------------------------

### [TouchableWithoutFeedback Props](/docs/touchablewithoutfeedback#props)[​](#touchablewithoutfeedback-props "Direct link to touchablewithoutfeedback-props")

Inherits [TouchableWithoutFeedback Props](/docs/touchablewithoutfeedback#props).

---

### `style`[​](#style "Direct link to style")

|  |  |
| --- | --- |
| Type|  | | --- | | [View.style](/docs/view-style-props) | |

---

### `activeOpacity`[​](#activeopacity "Direct link to activeopacity")

Determines what the opacity of the wrapped view should be when touch is active. Defaults to `0.2`.

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

---

### `hasTVPreferredFocus` iOS [​](#hastvpreferredfocus-ios "Direct link to hastvpreferredfocus-ios")

*(Apple TV only)* TV preferred focus (see documentation for the View component).

|  |  |
| --- | --- |
| Type|  | | --- | | bool | |

---

### `nextFocusDown` Android [​](#nextfocusdown-android "Direct link to nextfocusdown-android")

TV next focus down (see documentation for the View component).

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

---

### `nextFocusForward` Android [​](#nextfocusforward-android "Direct link to nextfocusforward-android")

TV next focus forward (see documentation for the View component).

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

---

### `nextFocusLeft` Android [​](#nextfocusleft-android "Direct link to nextfocusleft-android")

TV next focus left (see documentation for the View component).

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

---

### `nextFocusRight` Android [​](#nextfocusright-android "Direct link to nextfocusright-android")

TV next focus right (see documentation for the View component).

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

---

### `nextFocusUp` Android [​](#nextfocusup-android "Direct link to nextfocusup-android")

TV next focus up (see documentation for the View component).

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/touchableopacity.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/touchableopacity.md)

Last updated on **Apr 14, 2025**

[Previous

TouchableHighlight](/docs/touchablehighlight)[Next

TouchableWithoutFeedback](/docs/touchablewithoutfeedback)

* [Example](#example)* [Props](#props)
    + [TouchableWithoutFeedback Props](#touchablewithoutfeedback-props)+ [`style`](#style)+ [`activeOpacity`](#activeopacity)+ [`hasTVPreferredFocus`

            iOS](#hastvpreferredfocus-ios)+ [`nextFocusDown`

              Android](#nextfocusdown-android)+ [`nextFocusForward`

                Android](#nextfocusforward-android)+ [`nextFocusLeft`

                  Android](#nextfocusleft-android)+ [`nextFocusRight`

                    Android](#nextfocusright-android)+ [`nextFocusUp`

                      Android](#nextfocusup-android)

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