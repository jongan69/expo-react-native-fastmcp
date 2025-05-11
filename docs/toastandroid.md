ToastAndroid · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/toastandroid)

* [Next](/docs/next/toastandroid)* [0.79](/docs/toastandroid)* [0.78](/docs/0.78/toastandroid)* [0.77](/docs/0.77/toastandroid)* [0.76](/docs/0.76/toastandroid)* [0.75](/docs/0.75/toastandroid)* [0.74](/docs/0.74/toastandroid)* [0.73](/docs/0.73/toastandroid)* [0.72](/docs/0.72/toastandroid)* [0.71](/docs/0.71/toastandroid)* [0.70](/docs/0.70/toastandroid)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [APIs](/docs/accessibilityinfo)

  + [AccessibilityInfo](/docs/accessibilityinfo)+ [Alert](/docs/alert)+ [Animated](/docs/animated)+ [Animated.Value](/docs/animatedvalue)+ [Animated.ValueXY](/docs/animatedvaluexy)+ [Appearance](/docs/appearance)+ [AppRegistry](/docs/appregistry)+ [AppState](/docs/appstate)+ [DevSettings](/docs/devsettings)+ [Dimensions](/docs/dimensions)+ [Easing](/docs/easing)+ [InteractionManager](/docs/interactionmanager)+ [Keyboard](/docs/keyboard)+ [LayoutAnimation](/docs/layoutanimation)+ [Linking](/docs/linking)+ [PanResponder](/docs/panresponder)+ [PixelRatio](/docs/pixelratio)+ [Platform](/docs/platform)+ [PlatformColor](/docs/platformcolor)+ [RootTag](/docs/roottag)+ [Share](/docs/share)+ [StyleSheet](/docs/stylesheet)+ [Systrace](/docs/systrace)+ [Transforms](/docs/transforms)+ [Vibration](/docs/vibration)+ [Hooks](/docs/usecolorscheme)

                                                      - [useColorScheme](/docs/usecolorscheme)- [useWindowDimensions](/docs/usewindowdimensions)+ [Android APIs](/docs/backhandler)

                                                        - [BackHandler](/docs/backhandler)- [PermissionsAndroid](/docs/permissionsandroid)- [ToastAndroid](/docs/toastandroid)+ [iOS APIs](/docs/actionsheetios)

                                                          - [ActionSheetIOS](/docs/actionsheetios)- [DynamicColorIOS](/docs/dynamiccolorios)- [Settings](/docs/settings)

On this page

ToastAndroid
============

React Native's ToastAndroid API exposes the Android platform's ToastAndroid module as a JS module. It provides the method `show(message, duration)` which takes the following parameters:

* *message* A string with the text to toast
* *duration* The duration of the toast—either `ToastAndroid.SHORT` or `ToastAndroid.LONG`

You can alternatively use `showWithGravity(message, duration, gravity)` to specify where the toast appears in the screen's layout. May be `ToastAndroid.TOP`, `ToastAndroid.BOTTOM` or `ToastAndroid.CENTER`.

The `showWithGravityAndOffset(message, duration, gravity, xOffset, yOffset)` method adds the ability to specify an offset with in pixels.

> Starting with Android 11 (API level 30), setting the gravity has no effect on text toasts. Read about the changes [here](https://developer.android.com/about/versions/11/behavior-changes-11#text-toast-api-changes).

---

Reference
=========

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### `show()`[​](#show "Direct link to show")

tsx

```
static show(message: string, duration: number);  

```

---

### `showWithGravity()`[​](#showwithgravity "Direct link to showwithgravity")

This property will only work on Android API 29 and below. For similar functionality on higher Android APIs, consider using snackbar or notification.

tsx

```
static showWithGravity(message: string, duration: number, gravity: number);  

```

---

### `showWithGravityAndOffset()`[​](#showwithgravityandoffset "Direct link to showwithgravityandoffset")

This property will only work on Android API 29 and below. For similar functionality on higher Android APIs, consider using snackbar or notification.

tsx

```
static showWithGravityAndOffset(  
  message: string,  
  duration: number,  
  gravity: number,  
  xOffset: number,  
  yOffset: number,  
);  

```

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### `SHORT`[​](#short "Direct link to short")

Indicates the duration on the screen.

tsx

```
static SHORT: number;  

```

---

### `LONG`[​](#long "Direct link to long")

Indicates the duration on the screen.

tsx

```
static LONG: number;  

```

---

### `TOP`[​](#top "Direct link to top")

Indicates the position on the screen.

tsx

```
static TOP: number;  

```

---

### `BOTTOM`[​](#bottom "Direct link to bottom")

Indicates the position on the screen.

tsx

```
static BOTTOM: number;  

```

---

### `CENTER`[​](#center "Direct link to center")

Indicates the position on the screen.

tsx

```
static CENTER: number;  

```

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/toastandroid.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/toastandroid.md)

Last updated on **Apr 14, 2025**

[Previous

PermissionsAndroid](/docs/permissionsandroid)[Next

ActionSheetIOS](/docs/actionsheetios)

* [Methods](#methods)
  + [`show()`](#show)+ [`showWithGravity()`](#showwithgravity)+ [`showWithGravityAndOffset()`](#showwithgravityandoffset)* [Properties](#properties)
    + [`SHORT`](#short)+ [`LONG`](#long)+ [`TOP`](#top)+ [`BOTTOM`](#bottom)+ [`CENTER`](#center)

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