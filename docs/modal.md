Modal · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/modal)

* [Next](/docs/next/modal)* [0.79](/docs/modal)* [0.78](/docs/0.78/modal)* [0.77](/docs/0.77/modal)* [0.76](/docs/0.76/modal)* [0.75](/docs/0.75/modal)* [0.74](/docs/0.74/modal)* [0.73](/docs/0.73/modal)* [0.72](/docs/0.72/modal)* [0.71](/docs/0.71/modal)* [0.70](/docs/0.70/modal)* [All versions](/versions)

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

Modal
=====

The Modal component is a basic way to present content above an enclosing view.

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

### `animated`[​](#animated "Direct link to animated")

> **Deprecated.** Use the [`animationType`](/docs/modal#animationtype) prop instead.

---

### `animationType`[​](#animationtype "Direct link to animationtype")

The `animationType` prop controls how the modal animates.

Possible values:

* `slide` slides in from the bottom
* `fade` fades into view
* `none` appears without an animation

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | enum(`'none'`, `'slide'`, `'fade'`) `none` | | | |

---

### `backdropColor`[​](#backdropcolor "Direct link to backdropcolor")

The `backdropColor` of the modal (or background color of the modal's container.) Defaults to `white` if not provided and transparent is `false`. Ignored if `transparent` is `true`.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | [color](/docs/colors) white | | | |

---

### `hardwareAccelerated` Android [​](#hardwareaccelerated-android "Direct link to hardwareaccelerated-android")

The `hardwareAccelerated` prop controls whether to force hardware acceleration for the underlying window.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | bool `false` | | | |

---

### `navigationBarTranslucent` Android [​](#navigationbartranslucent-android "Direct link to navigationbartranslucent-android")

The `navigationBarTranslucent` prop determines whether your modal should go under the system navigation bar. However, `statusBarTranslucent` also needs to be set to `true` to make navigation bar translucent.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | bool `false` | | | |

---

### `onDismiss` iOS [​](#ondismiss-ios "Direct link to ondismiss-ios")

The `onDismiss` prop allows passing a function that will be called once the modal has been dismissed.

|  |  |
| --- | --- |
| Type|  | | --- | | function | |

---

### `onOrientationChange` iOS [​](#onorientationchange-ios "Direct link to onorientationchange-ios")

The `onOrientationChange` callback is called when the orientation changes while the modal is being displayed. The orientation provided is only 'portrait' or 'landscape'. This callback is also called on initial render, regardless of the current orientation.

|  |  |
| --- | --- |
| Type|  | | --- | | function | |

---

### `onRequestClose`[​](#onrequestclose "Direct link to onrequestclose")

The `onRequestClose` callback is called when the user taps the hardware back button on Android or the menu button on Apple TV. Because of this required prop, be aware that `BackHandler` events will not be emitted as long as the modal is open.
On iOS, this callback is called when a Modal is being dismissed using a drag gesture when `presentationStyle` is `pageSheet or formSheet`

|  |  |
| --- | --- |
| Type|  | | --- | | function Required  Android  TV   ---  function iOS | |

---

### `onShow`[​](#onshow "Direct link to onshow")

The `onShow` prop allows passing a function that will be called once the modal has been shown.

|  |  |
| --- | --- |
| Type|  | | --- | | function | |

---

### `presentationStyle` iOS [​](#presentationstyle-ios "Direct link to presentationstyle-ios")

The `presentationStyle` prop controls how the modal appears (generally on larger devices such as iPad or plus-sized iPhones). See <https://developer.apple.com/reference/uikit/uimodalpresentationstyle> for details.

Possible values:

* `fullScreen` covers the screen completely
* `pageSheet` covers portrait-width view centered (only on larger devices)
* `formSheet` covers narrow-width view centered (only on larger devices)
* `overFullScreen` covers the screen completely, but allows transparency

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | enum(`'fullScreen'`, `'pageSheet'`, `'formSheet'`, `'overFullScreen'`) `fullScreen` if `transparent={false}`  ---  `overFullScreen` if `transparent={true}` | | | |

---

### `statusBarTranslucent` Android [​](#statusbartranslucent-android "Direct link to statusbartranslucent-android")

The `statusBarTranslucent` prop determines whether your modal should go under the system statusbar.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | bool `false` | | | |

---

### `supportedOrientations` iOS [​](#supportedorientations-ios "Direct link to supportedorientations-ios")

The `supportedOrientations` prop allows the modal to be rotated to any of the specified orientations. On iOS, the modal is still restricted by what's specified in your app's Info.plist's UISupportedInterfaceOrientations field.

> When using `presentationStyle` of `pageSheet` or `formSheet`, this property will be ignored by iOS.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | array of enums(`'portrait'`, `'portrait-upside-down'`, `'landscape'`, `'landscape-left'`, `'landscape-right'`) `['portrait']` | | | |

---

### `transparent`[​](#transparent "Direct link to transparent")

The `transparent` prop determines whether your modal will fill the entire view. Setting this to `true` will render the modal over a transparent background.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | bool `false` | | | |

---

### `visible`[​](#visible "Direct link to visible")

The `visible` prop determines whether your modal is visible.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | bool `true` | | | |

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/modal.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/modal.md)

Last updated on **Apr 14, 2025**

[Previous

KeyboardAvoidingView](/docs/keyboardavoidingview)[Next

Pressable](/docs/pressable)

* [Example](#example)* [Props](#props)
    + [View Props](#view-props)+ [`animated`](#animated)+ [`animationType`](#animationtype)+ [`backdropColor`](#backdropcolor)+ [`hardwareAccelerated`

              Android](#hardwareaccelerated-android)+ [`navigationBarTranslucent`

                Android](#navigationbartranslucent-android)+ [`onDismiss`

                  iOS](#ondismiss-ios)+ [`onOrientationChange`

                    iOS](#onorientationchange-ios)+ [`onRequestClose`](#onrequestclose)+ [`onShow`](#onshow)+ [`presentationStyle`

                          iOS](#presentationstyle-ios)+ [`statusBarTranslucent`

                            Android](#statusbartranslucent-android)+ [`supportedOrientations`

                              iOS](#supportedorientations-ios)+ [`transparent`](#transparent)+ [`visible`](#visible)

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