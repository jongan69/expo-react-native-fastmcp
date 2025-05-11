AccessibilityInfo · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/accessibilityinfo)

* [Next](/docs/next/accessibilityinfo)* [0.79](/docs/accessibilityinfo)* [0.78](/docs/0.78/accessibilityinfo)* [0.77](/docs/0.77/accessibilityinfo)* [0.76](/docs/0.76/accessibilityinfo)* [0.75](/docs/0.75/accessibilityinfo)* [0.74](/docs/0.74/accessibilityinfo)* [0.73](/docs/0.73/accessibilityinfo)* [0.72](/docs/0.72/accessibilityinfo)* [0.71](/docs/0.71/accessibilityinfo)* [0.70](/docs/0.70/accessibilityinfo)* [All versions](/versions)

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

AccessibilityInfo
=================

Sometimes it's useful to know whether or not the device has a screen reader that is currently active. The `AccessibilityInfo` API is designed for this purpose. You can use it to query the current state of the screen reader as well as to register to be notified when the state of the screen reader changes.

Example[​](#example "Direct link to Example")
---------------------------------------------

---

Reference
=========

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### `addEventListener()`[​](#addeventlistener "Direct link to addeventlistener")

tsx

```
static addEventListener(  
  eventName: AccessibilityChangeEventName | AccessibilityAnnouncementEventName,  
  handler: (  
    event: AccessibilityChangeEvent | AccessibilityAnnouncementFinishedEvent,  
  ) => void,  
): EmitterSubscription;  

```

Add an event handler. Supported events:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Event name Description|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `accessibilityServiceChanged`  Android  Fires when some services such as TalkBack, other Android assistive technologies, and third-party accessibility services are enabled. The argument to the event handler is a boolean. The boolean is `true` when a some accessibility services is enabled and `false` otherwise.| `announcementFinished`  iOS  Fires when the screen reader has finished making an announcement. The argument to the event handler is a dictionary with these keys:  * `announcement`: The string announced by the screen reader.* `success`: A boolean indicating whether the announcement was successfully made.  | `boldTextChanged`  iOS  Fires when the state of the bold text toggle changes. The argument to the event handler is a boolean. The boolean is `true` when bold text is enabled and `false` otherwise.| `grayscaleChanged`  iOS  Fires when the state of the gray scale toggle changes. The argument to the event handler is a boolean. The boolean is `true` when a gray scale is enabled and `false` otherwise.| `invertColorsChanged`  iOS  Fires when the state of the invert colors toggle changes. The argument to the event handler is a boolean. The boolean is `true` when invert colors is enabled and `false` otherwise.| `reduceMotionChanged` Fires when the state of the reduce motion toggle changes. The argument to the event handler is a boolean. The boolean is `true` when a reduce motion is enabled (or when "Transition Animation Scale" in "Developer options" is "Animation off") and `false` otherwise.| `reduceTransparencyChanged`  iOS  Fires when the state of the reduce transparency toggle changes. The argument to the event handler is a boolean. The boolean is `true` when reduce transparency is enabled and `false` otherwise.| `screenReaderChanged` Fires when the state of the screen reader changes. The argument to the event handler is a boolean. The boolean is `true` when a screen reader is enabled and `false` otherwise. | | | | | | | | | | | | | | | | | |

---

### `announceForAccessibility()`[​](#announceforaccessibility "Direct link to announceforaccessibility")

tsx

```
static announceForAccessibility(announcement: string);  

```

Post a string to be announced by the screen reader.

---

### `announceForAccessibilityWithOptions()`[​](#announceforaccessibilitywithoptions "Direct link to announceforaccessibilitywithoptions")

tsx

```
static announceForAccessibilityWithOptions(  
  announcement: string,  
  options: options: {queue?: boolean},  
);  

```

Post a string to be announced by the screen reader with modification options. By default announcements will interrupt any existing speech, but on iOS they can be queued behind existing speech by setting `queue` to `true` in the options object.

**Parameters:**

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Description|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | announcement Required  string The string to be announced|  |  |  | | --- | --- | --- | | options Required  object `queue` - queue the announcement behind existing speech iOS | | | | | | | | |

---

### `getRecommendedTimeoutMillis()` Android [​](#getrecommendedtimeoutmillis-android "Direct link to getrecommendedtimeoutmillis-android")

tsx

```
static getRecommendedTimeoutMillis(originalTimeout: number): Promise<number>;  

```

Gets the timeout in millisecond that the user needs.
This value is set in "Time to take action (Accessibility timeout)" of "Accessibility" settings.

**Parameters:**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Name Type Description|  |  |  | | --- | --- | --- | | originalTimeout Required  number The timeout to return if "Accessibility timeout" is not set. Specify in milliseconds. | | | | | |

---

### `isAccessibilityServiceEnabled()` Android [​](#isaccessibilityserviceenabled-android "Direct link to isaccessibilityserviceenabled-android")

tsx

```
static isAccessibilityServiceEnabled(): Promise<boolean>;  

```

Check whether any accessibility service is enabled. This includes TalkBack but also any third-party accessibility app that may be installed. To only check whether TalkBack is enabled, use [isScreenReaderEnabled](#isscreenreaderenabled). Returns a promise which resolves to a boolean. The result is `true` when some accessibility services is enabled and `false` otherwise.

> **Note**: Please use [isScreenReaderEnabled](#isscreenreaderenabled) if you only want to check the status of TalkBack.

---

### `isBoldTextEnabled()` iOS [​](#isboldtextenabled-ios "Direct link to isboldtextenabled-ios")

tsx

```
static isBoldTextEnabled(): Promise<boolean>:  

```

Query whether a bold text is currently enabled. Returns a promise which resolves to a boolean. The result is `true` when bold text is enabled and `false` otherwise.

---

### `isGrayscaleEnabled()` iOS [​](#isgrayscaleenabled-ios "Direct link to isgrayscaleenabled-ios")

tsx

```
static isGrayscaleEnabled(): Promise<boolean>;  

```

Query whether grayscale is currently enabled. Returns a promise which resolves to a boolean. The result is `true` when grayscale is enabled and `false` otherwise.

---

### `isInvertColorsEnabled()` iOS [​](#isinvertcolorsenabled-ios "Direct link to isinvertcolorsenabled-ios")

tsx

```
static isInvertColorsEnabled(): Promise<boolean>;  

```

Query whether invert colors is currently enabled. Returns a promise which resolves to a boolean. The result is `true` when invert colors is enabled and `false` otherwise.

---

### `isReduceMotionEnabled()`[​](#isreducemotionenabled "Direct link to isreducemotionenabled")

tsx

```
static isReduceMotionEnabled(): Promise<boolean>;  

```

Query whether reduce motion is currently enabled. Returns a promise which resolves to a boolean. The result is `true` when reduce motion is enabled and `false` otherwise.

---

### `isReduceTransparencyEnabled()` iOS [​](#isreducetransparencyenabled-ios "Direct link to isreducetransparencyenabled-ios")

tsx

```
static isReduceTransparencyEnabled(): Promise<boolean>;  

```

Query whether reduce transparency is currently enabled. Returns a promise which resolves to a boolean. The result is `true` when a reduce transparency is enabled and `false` otherwise.

---

### `isScreenReaderEnabled()`[​](#isscreenreaderenabled "Direct link to isscreenreaderenabled")

tsx

```
static isScreenReaderEnabled(): Promise<boolean>;  

```

Query whether a screen reader is currently enabled. Returns a promise which resolves to a boolean. The result is `true` when a screen reader is enabled and `false` otherwise.

---

### `prefersCrossFadeTransitions()` iOS [​](#preferscrossfadetransitions-ios "Direct link to preferscrossfadetransitions-ios")

tsx

```
static prefersCrossFadeTransitions(): Promise<boolean>;  

```

Query whether reduce motion and prefer cross-fade transitions settings are currently enabled. Returns a promise which resolves to a boolean. The result is `true` when prefer cross-fade transitions is enabled and `false` otherwise.

---

### `setAccessibilityFocus()`[​](#setaccessibilityfocus "Direct link to setaccessibilityfocus")

tsx

```
static setAccessibilityFocus(reactTag: number);  

```

Set accessibility focus to a React component.

On Android, this calls `UIManager.sendAccessibilityEvent` method with passed `reactTag` and `UIManager.AccessibilityEventTypes.typeViewFocused` arguments.

> **Note**: Make sure that any `View` you want to receive the accessibility focus has `accessible={true}`.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/accessibilityinfo.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/accessibilityinfo.md)

Last updated on **Apr 14, 2025**

[Next

Alert](/docs/alert)

* [Example](#example)* [Methods](#methods)
    + [`addEventListener()`](#addeventlistener)+ [`announceForAccessibility()`](#announceforaccessibility)+ [`announceForAccessibilityWithOptions()`](#announceforaccessibilitywithoptions)+ [`getRecommendedTimeoutMillis()`

            Android](#getrecommendedtimeoutmillis-android)+ [`isAccessibilityServiceEnabled()`

              Android](#isaccessibilityserviceenabled-android)+ [`isBoldTextEnabled()`

                iOS](#isboldtextenabled-ios)+ [`isGrayscaleEnabled()`

                  iOS](#isgrayscaleenabled-ios)+ [`isInvertColorsEnabled()`

                    iOS](#isinvertcolorsenabled-ios)+ [`isReduceMotionEnabled()`](#isreducemotionenabled)+ [`isReduceTransparencyEnabled()`

                        iOS](#isreducetransparencyenabled-ios)+ [`isScreenReaderEnabled()`](#isscreenreaderenabled)+ [`prefersCrossFadeTransitions()`

                            iOS](#preferscrossfadetransitions-ios)+ [`setAccessibilityFocus()`](#setaccessibilityfocus)

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