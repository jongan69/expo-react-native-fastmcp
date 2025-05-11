Systrace · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/systrace)

* [Next](/docs/next/systrace)* [0.79](/docs/systrace)* [0.78](/docs/0.78/systrace)* [0.77](/docs/0.77/systrace)* [0.76](/docs/0.76/systrace)* [0.75](/docs/0.75/systrace)* [0.74](/docs/0.74/systrace)* [0.73](/docs/0.73/systrace)* [0.72](/docs/0.72/systrace)* [0.71](/docs/0.71/systrace)* [0.70](/docs/0.70/systrace)* [All versions](/versions)

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

Systrace
========

`Systrace` is a standard Android marker-based profiling tool (and is installed when you install the Android platform-tools package). Profiled code blocks are surrounded by start/end markers which are then visualized in a colorful chart format. Both the Android SDK and React Native framework provide standard markers that you can visualize.

Example[​](#example "Direct link to Example")
---------------------------------------------

`Systrace` allows you to mark JavaScript (JS) events with a tag and an integer value. Capture the non-Timed JS events in EasyProfiler.

---

Reference
=========

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### `isEnabled()`[​](#isenabled "Direct link to isenabled")

tsx

```
static isEnabled(): boolean;  

```

---

### `beginEvent()`[​](#beginevent "Direct link to beginevent")

tsx

```
static beginEvent(eventName: string | (() => string), args?: EventArgs);  

```

beginEvent/endEvent for starting and then ending a profile within the same call stack frame.

---

### `endEvent()`[​](#endevent "Direct link to endevent")

tsx

```
static endEvent(args?: EventArgs);  

```

---

### `beginAsyncEvent()`[​](#beginasyncevent "Direct link to beginasyncevent")

tsx

```
static beginAsyncEvent(  
  eventName: string | (() => string),  
  args?: EventArgs,  
): number;  

```

beginAsyncEvent/endAsyncEvent for starting and then ending a profile where the end can either occur on another thread or out of the current stack frame, eg await the returned cookie variable should be used as input into the endAsyncEvent call to end the profile.

---

### `endAsyncEvent()`[​](#endasyncevent "Direct link to endasyncevent")

tsx

```
static endAsyncEvent(  
  eventName: EventName,  
  cookie: number,  
  args?: EventArgs,  
);  

```

---

### `counterEvent()`[​](#counterevent "Direct link to counterevent")

tsx

```
static counterEvent(eventName: string | (() => string), value: number);  

```

Register the value to the profileName on the systrace timeline.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/systrace.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/systrace.md)

Last updated on **Apr 14, 2025**

[Previous

StyleSheet](/docs/stylesheet)[Next

Transforms](/docs/transforms)

* [Example](#example)* [Methods](#methods)
    + [`isEnabled()`](#isenabled)+ [`beginEvent()`](#beginevent)+ [`endEvent()`](#endevent)+ [`beginAsyncEvent()`](#beginasyncevent)+ [`endAsyncEvent()`](#endasyncevent)+ [`counterEvent()`](#counterevent)

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