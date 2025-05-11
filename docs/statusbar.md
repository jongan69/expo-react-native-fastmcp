StatusBar · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/statusbar)

* [Next](/docs/next/statusbar)* [0.79](/docs/statusbar)* [0.78](/docs/0.78/statusbar)* [0.77](/docs/0.77/statusbar)* [0.76](/docs/0.76/statusbar)* [0.75](/docs/0.75/statusbar)* [0.74](/docs/0.74/statusbar)* [0.73](/docs/0.73/statusbar)* [0.72](/docs/0.72/statusbar)* [0.71](/docs/0.71/statusbar)* [0.70](/docs/0.70/statusbar)* [All versions](/versions)

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

StatusBar
=========

Component to control the app's status bar. The status bar is the zone, typically at the top of the screen, that displays the current time, Wi-Fi and cellular network information, battery level and/or other status icons.

### Usage with Navigator[​](#usage-with-navigator "Direct link to Usage with Navigator")

It is possible to have multiple `StatusBar` components mounted at the same time. The props will be merged in the order the `StatusBar` components were mounted.

* TypeScript* JavaScript

### Imperative API[​](#imperative-api "Direct link to Imperative API")

For cases where using a component is not ideal, there is also an imperative API exposed as static functions on the component. It is however not recommended to use the static API and the component for the same prop because any value set by the static API will get overridden by the one set by the component in the next render.

---

Reference
=========

Constants[​](#constants "Direct link to Constants")
---------------------------------------------------

### `currentHeight` Android [​](#currentheight-android "Direct link to currentheight-android")

The height of the status bar, which includes the notch height, if present.

---

Props[​](#props "Direct link to Props")
---------------------------------------

### `animated`[​](#animated "Direct link to animated")

If the transition between status bar property changes should be animated. Supported for `backgroundColor`, `barStyle` and `hidden` properties.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Type Required Default|  |  |  | | --- | --- | --- | | boolean No `false` | | | | | |

---

### `backgroundColor` Android [​](#backgroundcolor-android "Direct link to backgroundcolor-android")

The background color of the status bar.

warning

Due to edge-to-edge enforcement introduced in Android 15, setting background color of the status bar is deprecated in API level 35.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Type Required Default|  |  |  | | --- | --- | --- | | [color](/docs/colors) No default system StatusBar background color, or `'black'` if not defined | | | | | |

---

### `barStyle`[​](#barstyle "Direct link to barstyle")

Sets the color of the status bar text.

On Android, this will only have an impact on API versions 23 and above.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Type Required Default|  |  |  | | --- | --- | --- | | [StatusBarStyle](/docs/statusbar#statusbarstyle) No `'default'` | | | | | |

---

### `hidden`[​](#hidden "Direct link to hidden")

If the status bar is hidden.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Type Required Default|  |  |  | | --- | --- | --- | | boolean No `false` | | | | | |

---

### `networkActivityIndicatorVisible` iOS [​](#networkactivityindicatorvisible-ios "Direct link to networkactivityindicatorvisible-ios")

If the network activity indicator should be visible.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | boolean `false` | | | |

---

### `showHideTransition` iOS [​](#showhidetransition-ios "Direct link to showhidetransition-ios")

The transition effect when showing and hiding the status bar using the `hidden` prop.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | [StatusBarAnimation](/docs/statusbar#statusbaranimation) `'fade'` | | | |

---

### `translucent` Android [​](#translucent-android "Direct link to translucent-android")

If the status bar is translucent. When translucent is set to `true`, the app will draw under the status bar. This is useful when using a semi transparent status bar color.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | boolean `false` | | | |

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### `popStackEntry()`[​](#popstackentry "Direct link to popstackentry")

tsx

```
static popStackEntry(entry: StatusBarProps);  

```

Get and remove the last StatusBar entry from the stack.

**Parameters:**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Name Type Description|  |  |  | | --- | --- | --- | | entry Required  any Entry returned from `pushStackEntry`. | | | | | |

---

### `pushStackEntry()`[​](#pushstackentry "Direct link to pushstackentry")

tsx

```
static pushStackEntry(props: StatusBarProps): StatusBarProps;  

```

Push a StatusBar entry onto the stack. The return value should be passed to `popStackEntry` when complete.

**Parameters:**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Name Type Description|  |  |  | | --- | --- | --- | | props Required  any Object containing the StatusBar props to use in the stack entry. | | | | | |

---

### `replaceStackEntry()`[​](#replacestackentry "Direct link to replacestackentry")

tsx

```
static replaceStackEntry(  
  entry: StatusBarProps,  
  props: StatusBarProps  
): StatusBarProps;  

```

Replace an existing StatusBar stack entry with new props.

**Parameters:**

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Description|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | entry Required  any Entry returned from `pushStackEntry` to replace.| props Required  any Object containing the StatusBar props to use in the replacement stack entry. | | | | | | | | |

---

### `setBackgroundColor()` Android [​](#setbackgroundcolor-android "Direct link to setbackgroundcolor-android")

tsx

```
static setBackgroundColor(color: ColorValue, animated?: boolean);  

```

Set the background color for the status bar.

warning

Due to edge-to-edge enforcement introduced in Android 15, setting background color of the status bar is deprecated in API level 35.

**Parameters:**

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Description|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | color Required  string Background color.|  |  |  | | --- | --- | --- | | animated boolean Animate the style change. | | | | | | | | |

---

### `setBarStyle()`[​](#setbarstyle "Direct link to setbarstyle")

tsx

```
static setBarStyle(style: StatusBarStyle, animated?: boolean);  

```

Set the status bar style.

**Parameters:**

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Description|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | style Required  [StatusBarStyle](/docs/statusbar#statusbarstyle) Status bar style to set.|  |  |  | | --- | --- | --- | | animated boolean Animate the style change. | | | | | | | | |

---

### `setHidden()`[​](#sethidden "Direct link to sethidden")

tsx

```
static setHidden(hidden: boolean, animation?: StatusBarAnimation);  

```

Show or hide the status bar.

**Parameters:**

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Description|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | hidden Required  boolean Hide the status bar.|  |  |  | | --- | --- | --- | | animation iOS  [StatusBarAnimation](/docs/statusbar#statusbaranimation) Animation when changing the status bar hidden property. | | | | | | | | |

---

### `setNetworkActivityIndicatorVisible()` iOS [​](#setnetworkactivityindicatorvisible-ios "Direct link to setnetworkactivityindicatorvisible-ios")

tsx

```
static setNetworkActivityIndicatorVisible(visible: boolean);  

```

Control the visibility of the network activity indicator.

**Parameters:**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Name Type Description|  |  |  | | --- | --- | --- | | visible Required  boolean Show the indicator. | | | | | |

---

### `setTranslucent()` Android [​](#settranslucent-android "Direct link to settranslucent-android")

tsx

```
static setTranslucent(translucent: boolean);  

```

Control the translucency of the status bar.

**Parameters:**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Name Type Description|  |  |  | | --- | --- | --- | | translucent Required  boolean Set as translucent. | | | | | |

Type Definitions[​](#type-definitions "Direct link to Type Definitions")
------------------------------------------------------------------------

### StatusBarAnimation[​](#statusbaranimation "Direct link to StatusBarAnimation")

Status bar animation type for transitions on the iOS.

|  |  |
| --- | --- |
| Type|  | | --- | | enum | |

**Constants:**

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Value Type Description|  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `'fade'` string Fade animation|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | `'slide'` string Slide animation|  |  |  | | --- | --- | --- | | `'none'` string No animation | | | | | | | | | | | |

---

### StatusBarStyle[​](#statusbarstyle "Direct link to StatusBarStyle")

Status bar style type.

|  |  |
| --- | --- |
| Type|  | | --- | | enum | |

**Constants:**

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Value Type Description|  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `'default'` string Default status bar style (dark for iOS, light for Android)|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | `'light-content'` string White texts and icons|  |  |  | | --- | --- | --- | | `'dark-content'` string Dark texts and icons (requires API>=23 on Android) | | | | | | | | | | | |

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/statusbar.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/statusbar.md)

Last updated on **Apr 14, 2025**

[Previous

SectionList](/docs/sectionlist)[Next

Switch](/docs/switch)

* [Usage with Navigator](#usage-with-navigator)* [Imperative API](#imperative-api)* [Constants](#constants)
      + [`currentHeight`

        Android](#currentheight-android)* [Props](#props)
        + [`animated`](#animated)+ [`backgroundColor`

            Android](#backgroundcolor-android)+ [`barStyle`](#barstyle)+ [`hidden`](#hidden)+ [`networkActivityIndicatorVisible`

                  iOS](#networkactivityindicatorvisible-ios)+ [`showHideTransition`

                    iOS](#showhidetransition-ios)+ [`translucent`

                      Android](#translucent-android)* [Methods](#methods)
          + [`popStackEntry()`](#popstackentry)+ [`pushStackEntry()`](#pushstackentry)+ [`replaceStackEntry()`](#replacestackentry)+ [`setBackgroundColor()`

                  Android](#setbackgroundcolor-android)+ [`setBarStyle()`](#setbarstyle)+ [`setHidden()`](#sethidden)+ [`setNetworkActivityIndicatorVisible()`

                        iOS](#setnetworkactivityindicatorvisible-ios)+ [`setTranslucent()`

                          Android](#settranslucent-android)* [Type Definitions](#type-definitions)
            + [StatusBarAnimation](#statusbaranimation)+ [StatusBarStyle](#statusbarstyle)

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