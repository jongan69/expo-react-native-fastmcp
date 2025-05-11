TouchableNativeFeedback · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/touchablenativefeedback)

* [Next](/docs/next/touchablenativefeedback)* [0.79](/docs/touchablenativefeedback)* [0.78](/docs/0.78/touchablenativefeedback)* [0.77](/docs/0.77/touchablenativefeedback)* [0.76](/docs/0.76/touchablenativefeedback)* [0.75](/docs/0.75/touchablenativefeedback)* [0.74](/docs/0.74/touchablenativefeedback)* [0.73](/docs/0.73/touchablenativefeedback)* [0.72](/docs/0.72/touchablenativefeedback)* [0.71](/docs/0.71/touchablenativefeedback)* [0.70](/docs/0.70/touchablenativefeedback)* [All versions](/versions)

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

TouchableNativeFeedback
=======================

> If you're looking for a more extensive and future-proof way to handle touch-based input, check out the [Pressable](/docs/pressable) API.

A wrapper for making views respond properly to touches (Android only). On Android this component uses native state drawable to display touch feedback.

At the moment it only supports having a single View instance as a child node, as it's implemented by replacing that View with another instance of RCTView node with some additional properties set.

Background drawable of native feedback touchable can be customized with `background` property.

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

### `background`[​](#background "Direct link to background")

Determines the type of background drawable that's going to be used to display feedback. It takes an object with `type` property and extra data depending on the `type`. It's recommended to use one of the static methods to generate that dictionary.

|  |  |
| --- | --- |
| Type|  | | --- | | backgroundPropType | |

---

### `useForeground`[​](#useforeground "Direct link to useforeground")

Set to true to add the ripple effect to the foreground of the view, instead of the background. This is useful if one of your child views has a background of its own, or you're e.g. displaying images, and you don't want the ripple to be covered by them.

Check TouchableNativeFeedback.canUseNativeForeground() first, as this is only available on Android 6.0 and above. If you try to use this on older versions you will get a warning and fallback to background.

|  |  |
| --- | --- |
| Type|  | | --- | | bool | |

---

### `hasTVPreferredFocus` Android [​](#hastvpreferredfocus-android "Direct link to hastvpreferredfocus-android")

TV preferred focus (see documentation for the View component).

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

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### `SelectableBackground()`[​](#selectablebackground "Direct link to selectablebackground")

tsx

```
static SelectableBackground(  
  rippleRadius: number | null,  
): ThemeAttributeBackgroundPropType;  

```

Creates an object that represents android theme's default background for selectable elements (`?android:attr/selectableItemBackground`). `rippleRadius` parameter controls the radius of the ripple effect.

---

### `SelectableBackgroundBorderless()`[​](#selectablebackgroundborderless "Direct link to selectablebackgroundborderless")

tsx

```
static SelectableBackgroundBorderless(  
  rippleRadius: number | null,  
): ThemeAttributeBackgroundPropType;  

```

Creates an object that represent android theme's default background for borderless selectable elements (`?android:attr/selectableItemBackgroundBorderless`). Available on android API level 21+. `rippleRadius` parameter controls the radius of the ripple effect.

---

### `Ripple()`[​](#ripple "Direct link to ripple")

tsx

```
static Ripple(  
  color: ColorValue,  
  borderless: boolean,  
  rippleRadius?: number | null,  
): RippleBackgroundPropType;  

```

Creates an object that represents ripple drawable with specified color (as a string). If property `borderless` evaluates to true the ripple will render outside of the view bounds (see native actionbar buttons as an example of that behavior). This background type is available on Android API level 21+.

**Parameters:**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | color string Yes The ripple color|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | borderless boolean Yes If the ripple can render outside its bounds|  |  |  |  | | --- | --- | --- | --- | | rippleRadius ?number No controls the radius of the ripple effect | | | | | | | | | | | | | | | |

---

### `canUseNativeForeground()`[​](#canusenativeforeground "Direct link to canusenativeforeground")

tsx

```
static canUseNativeForeground(): boolean;  

```

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/touchablenativefeedback.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/touchablenativefeedback.md)

Last updated on **Apr 14, 2025**

[Previous

DrawerLayoutAndroid](/docs/drawerlayoutandroid)[Next

InputAccessoryView](/docs/inputaccessoryview)

* [Example](#example)* [Props](#props)
    + [TouchableWithoutFeedback Props](#touchablewithoutfeedback-props)+ [`background`](#background)+ [`useForeground`](#useforeground)+ [`hasTVPreferredFocus`

            Android](#hastvpreferredfocus-android)+ [`nextFocusDown`

              Android](#nextfocusdown-android)+ [`nextFocusForward`

                Android](#nextfocusforward-android)+ [`nextFocusLeft`

                  Android](#nextfocusleft-android)+ [`nextFocusRight`

                    Android](#nextfocusright-android)+ [`nextFocusUp`

                      Android](#nextfocusup-android)* [Methods](#methods)
      + [`SelectableBackground()`](#selectablebackground)+ [`SelectableBackgroundBorderless()`](#selectablebackgroundborderless)+ [`Ripple()`](#ripple)+ [`canUseNativeForeground()`](#canusenativeforeground)

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