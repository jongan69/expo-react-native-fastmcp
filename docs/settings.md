Settings · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/settings)

* [Next](/docs/next/settings)* [0.79](/docs/settings)* [0.78](/docs/0.78/settings)* [0.77](/docs/0.77/settings)* [0.76](/docs/0.76/settings)* [0.75](/docs/0.75/settings)* [0.74](/docs/0.74/settings)* [0.73](/docs/0.73/settings)* [0.72](/docs/0.72/settings)* [0.71](/docs/0.71/settings)* [0.70](/docs/0.70/settings)* [All versions](/versions)

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

Settings
========

`Settings` serves as a wrapper for [`NSUserDefaults`](https://developer.apple.com/documentation/foundation/nsuserdefaults), a persistent key-value store available only on iOS.

Example[​](#example "Direct link to Example")
---------------------------------------------

---

Reference
=========

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### `clearWatch()`[​](#clearwatch "Direct link to clearwatch")

tsx

```
static clearWatch(watchId: number);  

```

`watchId` is the number returned by `watchKeys()` when the subscription was originally configured.

---

### `get()`[​](#get "Direct link to get")

tsx

```
static get(key: string): any;  

```

Get the current value for a given `key` in `NSUserDefaults`.

---

### `set()`[​](#set "Direct link to set")

tsx

```
static set(settings: Record<string, any>);  

```

Set one or more values in `NSUserDefaults`.

---

### `watchKeys()`[​](#watchkeys "Direct link to watchkeys")

tsx

```
static watchKeys(keys: string | array<string>, callback: () => void): number;  

```

Subscribe to be notified when the value for any of the keys specified by the `keys` parameter has been changed in `NSUserDefaults`. Returns a `watchId` number that may be used with `clearWatch()` to unsubscribe.

> **Note:** `watchKeys()` by design ignores internal `set()` calls and fires callback only on changes preformed outside of React Native code.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/settings.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/settings.md)

Last updated on **Apr 14, 2025**

[Previous

DynamicColorIOS](/docs/dynamiccolorios)

* [Example](#example)* [Methods](#methods)
    + [`clearWatch()`](#clearwatch)+ [`get()`](#get)+ [`set()`](#set)+ [`watchKeys()`](#watchkeys)

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