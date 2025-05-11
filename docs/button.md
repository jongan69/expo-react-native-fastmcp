Button · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/button)

* [Next](/docs/next/button)* [0.79](/docs/button)* [0.78](/docs/0.78/button)* [0.77](/docs/0.77/button)* [0.76](/docs/0.76/button)* [0.75](/docs/0.75/button)* [0.74](/docs/0.74/button)* [0.73](/docs/0.73/button)* [0.72](/docs/0.72/button)* [0.71](/docs/0.71/button)* [0.70](/docs/0.70/button)* [All versions](/versions)

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

Button
======

A basic button component that should render nicely on any platform. Supports a minimal level of customization.

If this button doesn't look right for your app, you can build your own button using [Pressable](/docs/pressable). For inspiration, look at the [source code for the Button component](https://github.com/facebook/react-native/blob/main/packages/react-native/Libraries/Components/Button.js).

tsx

```
<Button  
  onPress={onPressLearnMore}  
  title="Learn More"  
  color="#841584"  
  accessibilityLabel="Learn more about this purple button"  
/>  

```

Example[​](#example "Direct link to Example")
---------------------------------------------

---

Reference
=========

Props[​](#props "Direct link to Props")
---------------------------------------

### Required **`onPress`**[​](#requiredonpress "Direct link to requiredonpress")

Handler to be called when the user taps the button.

|  |  |
| --- | --- |
| Type|  | | --- | | `({nativeEvent: PressEvent})` | |

---

### Required **`title`**[​](#requiredtitle "Direct link to requiredtitle")

Text to display inside the button. On Android the given title will be converted to the uppercased form.

|  |  |
| --- | --- |
| Type|  | | --- | | string | |

---

### `accessibilityLabel`[​](#accessibilitylabel "Direct link to accessibilitylabel")

Text to display for blindness accessibility features.

|  |  |
| --- | --- |
| Type|  | | --- | | string | |

---

### `accessibilityLanguage` iOS [​](#accessibilitylanguage-ios "Direct link to accessibilitylanguage-ios")

A value indicating which language should be used by the screen reader when the user interacts with the element. It should follow the [BCP 47 specification](https://www.rfc-editor.org/info/bcp47).

See the [iOS `accessibilityLanguage` doc](https://developer.apple.com/documentation/objectivec/nsobject/1615192-accessibilitylanguage) for more information.

|  |  |
| --- | --- |
| Type|  | | --- | | string | |

---

### `accessibilityActions`[​](#accessibilityactions "Direct link to accessibilityactions")

Accessibility actions allow an assistive technology to programmatically invoke the actions of a component. The `accessibilityActions` property should contain a list of action objects. Each action object should contain the field name and label.

See the [Accessibility guide](/docs/accessibility#accessibility-actions) for more information.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | array No | | | |

---

### `onAccessibilityAction`[​](#onaccessibilityaction "Direct link to onaccessibilityaction")

Invoked when the user performs the accessibility actions. The only argument to this function is an event containing the name of the action to perform.

See the [Accessibility guide](/docs/accessibility#accessibility-actions) for more information.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | function No | | | |

---

### `color`[​](#color "Direct link to color")

Color of the text (iOS), or background color of the button (Android).

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | [color](/docs/colors) `'#2196F3'` Android   ---   `'#007AFF'` iOS | | | |

---

### `disabled`[​](#disabled "Direct link to disabled")

If `true`, disable all interactions for this component.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | bool `false` | | | |

---

### `hasTVPreferredFocus` TV [​](#hastvpreferredfocus-tv "Direct link to hastvpreferredfocus-tv")

TV preferred focus.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | bool `false` | | | |

---

### `nextFocusDown` Android TV [​](#nextfocusdown-androidtv "Direct link to nextfocusdown-androidtv")

Designates the next view to receive focus when the user navigates down. See the [Android documentation](https://developer.android.com/reference/android/view/View.html#attr_android:nextFocusDown).

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

---

### `nextFocusForward` Android TV [​](#nextfocusforward-androidtv "Direct link to nextfocusforward-androidtv")

Designates the next view to receive focus when the user navigates forward. See the [Android documentation](https://developer.android.com/reference/android/view/View.html#attr_android:nextFocusForward).

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

---

### `nextFocusLeft` Android TV [​](#nextfocusleft-androidtv "Direct link to nextfocusleft-androidtv")

Designates the next view to receive focus when the user navigates left. See the [Android documentation](https://developer.android.com/reference/android/view/View.html#attr_android:nextFocusLeft).

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

---

### `nextFocusRight` Android TV [​](#nextfocusright-androidtv "Direct link to nextfocusright-androidtv")

Designates the next view to receive focus when the user navigates right. See the [Android documentation](https://developer.android.com/reference/android/view/View.html#attr_android:nextFocusRight).

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

---

### `nextFocusUp` Android TV [​](#nextfocusup-androidtv "Direct link to nextfocusup-androidtv")

Designates the next view to receive focus when the user navigates up. See the [Android documentation](https://developer.android.com/reference/android/view/View.html#attr_android:nextFocusUp).

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

---

### `testID`[​](#testid "Direct link to testid")

Used to locate this view in end-to-end tests.

|  |  |
| --- | --- |
| Type|  | | --- | | string | |

---

### `touchSoundDisabled` Android [​](#touchsounddisabled-android "Direct link to touchsounddisabled-android")

If `true`, doesn't play system sound on touch.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | boolean `false` | | | |

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/button.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/button.md)

Last updated on **Apr 14, 2025**

[Previous

ActivityIndicator](/docs/activityindicator)[Next

FlatList](/docs/flatlist)

* [Example](#example)* [Props](#props)
    + [Required

      **`onPress`**](#requiredonpress)+ [Required

        **`title`**](#requiredtitle)+ [`accessibilityLabel`](#accessibilitylabel)+ [`accessibilityLanguage`

            iOS](#accessibilitylanguage-ios)+ [`accessibilityActions`](#accessibilityactions)+ [`onAccessibilityAction`](#onaccessibilityaction)+ [`color`](#color)+ [`disabled`](#disabled)+ [`hasTVPreferredFocus`

                      TV](#hastvpreferredfocus-tv)+ [`nextFocusDown`

                        Android

                        TV](#nextfocusdown-androidtv)+ [`nextFocusForward`

                          Android

                          TV](#nextfocusforward-androidtv)+ [`nextFocusLeft`

                            Android

                            TV](#nextfocusleft-androidtv)+ [`nextFocusRight`

                              Android

                              TV](#nextfocusright-androidtv)+ [`nextFocusUp`

                                Android

                                TV](#nextfocusup-androidtv)+ [`testID`](#testid)+ [`touchSoundDisabled`

                                    Android](#touchsounddisabled-android)

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