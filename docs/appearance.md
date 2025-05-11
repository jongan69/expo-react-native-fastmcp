Appearance · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/appearance)

* [Next](/docs/next/appearance)* [0.79](/docs/appearance)* [0.78](/docs/0.78/appearance)* [0.77](/docs/0.77/appearance)* [0.76](/docs/0.76/appearance)* [0.75](/docs/0.75/appearance)* [0.74](/docs/0.74/appearance)* [0.73](/docs/0.73/appearance)* [0.72](/docs/0.72/appearance)* [0.71](/docs/0.71/appearance)* [0.70](/docs/0.70/appearance)* [All versions](/versions)

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

Appearance
==========

tsx

```
import {Appearance} from 'react-native';  

```

The `Appearance` module exposes information about the user's appearance preferences, such as their preferred color scheme (light or dark).

#### Developer notes[​](#developer-notes "Direct link to Developer notes")

* Android* iOS* Web

> The `Appearance` API is inspired by the [Media Queries draft](https://drafts.csswg.org/mediaqueries-5/) from the W3C. The color scheme preference is modeled after the [`prefers-color-scheme` CSS media feature](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme).

> The color scheme preference will map to the user's Light or [Dark theme](https://developer.android.com/guide/topics/ui/look-and-feel/darktheme) preference on Android 10 (API level 29) devices and higher.

> The color scheme preference will map to the user's Light or [Dark Mode](https://developer.apple.com/design/human-interface-guidelines/ios/visual-design/dark-mode/) preference on iOS 13 devices and higher.

> Note: When taking a screenshot, by default, the color scheme may flicker between light and dark mode. It happens because the iOS takes snapshots on both color schemes and updating the user interface with color scheme is asynchronous.

Example[​](#example "Direct link to Example")
---------------------------------------------

You can use the `Appearance` module to determine if the user prefers a dark color scheme:

tsx

```
const colorScheme = Appearance.getColorScheme();  
if (colorScheme === 'dark') {  
  // Use dark color scheme  
}  

```

Although the color scheme is available immediately, this may change (e.g. scheduled color scheme change at sunrise or sunset). Any rendering logic or styles that depend on the user preferred color scheme should try to call this function on every render, rather than caching the value. For example, you may use the [`useColorScheme`](/docs/usecolorscheme) React hook as it provides and subscribes to color scheme updates, or you may use inline styles rather than setting a value in a `StyleSheet`.

---

Reference
=========

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### `getColorScheme()`[​](#getcolorscheme "Direct link to getcolorscheme")

tsx

```
static getColorScheme(): 'light' | 'dark' | null;  

```

Indicates the current user preferred color scheme. The value may be updated later, either through direct user action (e.g. theme selection in device settings or application-level selected user interface style via `setColorScheme`) or on a schedule (e.g. light and dark themes that follow the day/night cycle).

Supported color schemes:

* `light`: The user prefers a light color theme.
* `dark`: The user prefers a dark color theme.
* null: The user has not indicated a preferred color theme.

See also: `useColorScheme` hook.

> Note: `getColorScheme()` will always return `light` when debugging with Chrome.

---

### `setColorScheme()`[​](#setcolorscheme "Direct link to setcolorscheme")

tsx

```
static setColorScheme('light' | 'dark' | null): void;  

```

Force the application to always adopt a light or dark interface style. The default value is `null` which causes the application to inherit the system's interface style. If you assign a different value, the new style applies to the application and all native elements within the application (Alerts, Pickers etc).

Supported color schemes:

* `light`: Apply light user interface style.
* `dark`: Apply dark user interface style.
* null: Follow the system's interface style.

> Note: The change will not affect the system's selected interface style or any style set in other applications.

---

### `addChangeListener()`[​](#addchangelistener "Direct link to addchangelistener")

tsx

```
static addChangeListener(  
  listener: (preferences: {colorScheme: 'light' | 'dark' | null}) => void,  
): NativeEventSubscription;  

```

Add an event handler that is fired when appearance preferences change.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/appearance.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/appearance.md)

Last updated on **Apr 14, 2025**

[Previous

Animated.ValueXY](/docs/animatedvaluexy)[Next

AppRegistry](/docs/appregistry)

* [Example](#example)* [Methods](#methods)
    + [`getColorScheme()`](#getcolorscheme)+ [`setColorScheme()`](#setcolorscheme)+ [`addChangeListener()`](#addchangelistener)

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