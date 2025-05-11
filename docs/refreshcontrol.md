RefreshControl · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/refreshcontrol)

* [Next](/docs/next/refreshcontrol)* [0.79](/docs/refreshcontrol)* [0.78](/docs/0.78/refreshcontrol)* [0.77](/docs/0.77/refreshcontrol)* [0.76](/docs/0.76/refreshcontrol)* [0.75](/docs/0.75/refreshcontrol)* [0.74](/docs/0.74/refreshcontrol)* [0.73](/docs/0.73/refreshcontrol)* [0.72](/docs/0.72/refreshcontrol)* [0.71](/docs/0.71/refreshcontrol)* [0.70](/docs/0.70/refreshcontrol)* [All versions](/versions)

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

RefreshControl
==============

This component is used inside a ScrollView or ListView to add pull to refresh functionality. When the ScrollView is at `scrollY: 0`, swiping down triggers an `onRefresh` event.

Example[​](#example "Direct link to Example")
---------------------------------------------

> Note: `refreshing` is a controlled prop, this is why it needs to be set to `true` in the `onRefresh` function otherwise the refresh indicator will stop immediately.

---

Reference
=========

Props[​](#props "Direct link to Props")
---------------------------------------

### [View Props](/docs/view#props)[​](#view-props "Direct link to view-props")

Inherits [View Props](/docs/view#props).

---

### Required **`refreshing`**[​](#requiredrefreshing "Direct link to requiredrefreshing")

Whether the view should be indicating an active refresh.

|  |  |
| --- | --- |
| Type|  | | --- | | boolean | |

---

### `colors` Android [​](#colors-android "Direct link to colors-android")

The colors (at least one) that will be used to draw the refresh indicator.

|  |  |
| --- | --- |
| Type|  | | --- | | array of [colors](/docs/colors) | |

---

### `enabled` Android [​](#enabled-android "Direct link to enabled-android")

Whether the pull to refresh functionality is enabled.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | boolean `true` | | | |

---

### `onRefresh`[​](#onrefresh "Direct link to onrefresh")

Called when the view starts refreshing.

|  |  |
| --- | --- |
| Type|  | | --- | | function | |

---

### `progressBackgroundColor` Android [​](#progressbackgroundcolor-android "Direct link to progressbackgroundcolor-android")

The background color of the refresh indicator.

|  |  |
| --- | --- |
| Type|  | | --- | | [color](/docs/colors) | |

---

### `progressViewOffset`[​](#progressviewoffset "Direct link to progressviewoffset")

Progress view top offset.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | number `0` | | | |

---

### `size` Android [​](#size-android "Direct link to size-android")

Size of the refresh indicator.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | enum(`'default'`, `'large'`) `'default'` | | | |

---

### `tintColor` iOS [​](#tintcolor-ios "Direct link to tintcolor-ios")

The color of the refresh indicator.

|  |  |
| --- | --- |
| Type|  | | --- | | [color](/docs/colors) | |

---

### `title` iOS [​](#title-ios "Direct link to title-ios")

The title displayed under the refresh indicator.

|  |  |
| --- | --- |
| Type|  | | --- | | string | |

---

### `titleColor` iOS [​](#titlecolor-ios "Direct link to titlecolor-ios")

The color of the refresh indicator title.

|  |  |
| --- | --- |
| Type|  | | --- | | [color](/docs/colors) | |

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/refreshcontrol.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/refreshcontrol.md)

Last updated on **Apr 14, 2025**

[Previous

Pressable](/docs/pressable)[Next

ScrollView](/docs/scrollview)

* [Example](#example)* [Props](#props)
    + [View Props](#view-props)+ [Required

        **`refreshing`**](#requiredrefreshing)+ [`colors`

          Android](#colors-android)+ [`enabled`

            Android](#enabled-android)+ [`onRefresh`](#onrefresh)+ [`progressBackgroundColor`

                Android](#progressbackgroundcolor-android)+ [`progressViewOffset`](#progressviewoffset)+ [`size`

                    Android](#size-android)+ [`tintColor`

                      iOS](#tintcolor-ios)+ [`title`

                        iOS](#title-ios)+ [`titleColor`

                          iOS](#titlecolor-ios)

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