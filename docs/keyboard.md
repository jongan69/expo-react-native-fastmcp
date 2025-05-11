Keyboard · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/keyboard)

* [Next](/docs/next/keyboard)* [0.79](/docs/keyboard)* [0.78](/docs/0.78/keyboard)* [0.77](/docs/0.77/keyboard)* [0.76](/docs/0.76/keyboard)* [0.75](/docs/0.75/keyboard)* [0.74](/docs/0.74/keyboard)* [0.73](/docs/0.73/keyboard)* [0.72](/docs/0.72/keyboard)* [0.71](/docs/0.71/keyboard)* [0.70](/docs/0.70/keyboard)* [All versions](/versions)

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

Keyboard
========

`Keyboard` module to control keyboard events.

### Usage[​](#usage "Direct link to Usage")

The Keyboard module allows you to listen for native events and react to them, as well as make changes to the keyboard, like dismissing it.

---

Reference
=========

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### `addListener()`[​](#addlistener "Direct link to addlistener")

tsx

```
static addListener: (  
  eventType: KeyboardEventName,  
  listener: KeyboardEventListener,  
) => EmitterSubscription;  

```

The `addListener` function connects a JavaScript function to an identified native keyboard notification event.

This function then returns the reference to the listener.

**Parameters:**

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Description|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | eventName Required  string The string that identifies the event you're listening for. See the list below.|  |  |  | | --- | --- | --- | | callback Required  function The function to be called when the event fires | | | | | | | | |

**`eventName`**

This can be any of the following:

* `keyboardWillShow`
* `keyboardDidShow`
* `keyboardWillHide`
* `keyboardDidHide`
* `keyboardWillChangeFrame`
* `keyboardDidChangeFrame`

> Note that only `keyboardDidShow` and `keyboardDidHide` events are available on Android. The events will not be fired when using Android 10 and under if your activity has `android:windowSoftInputMode` set to `adjustNothing`.

---

### `dismiss()`[​](#dismiss "Direct link to dismiss")

tsx

```
static dismiss();  

```

Dismisses the active keyboard and removes focus.

---

### `scheduleLayoutAnimation`[​](#schedulelayoutanimation "Direct link to schedulelayoutanimation")

tsx

```
static scheduleLayoutAnimation(event: KeyboardEvent);  

```

Useful for syncing TextInput (or other keyboard accessory view) size of position changes with keyboard movements.

---

### `isVisible()`[​](#isvisible "Direct link to isvisible")

tsx

```
static isVisible(): boolean;  

```

Whether the keyboard is last known to be visible.

---

### `metrics()`[​](#metrics "Direct link to metrics")

tsx

```
static metrics(): KeyboardMetrics | undefined;  

```

Return the metrics of the soft-keyboard if visible.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/keyboard.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/keyboard.md)

Last updated on **Apr 14, 2025**

[Previous

InteractionManager](/docs/interactionmanager)[Next

LayoutAnimation](/docs/layoutanimation)

* [Usage](#usage)* [Methods](#methods)
    + [`addListener()`](#addlistener)+ [`dismiss()`](#dismiss)+ [`scheduleLayoutAnimation`](#schedulelayoutanimation)+ [`isVisible()`](#isvisible)+ [`metrics()`](#metrics)

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