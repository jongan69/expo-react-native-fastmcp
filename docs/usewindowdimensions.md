useWindowDimensions · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/usewindowdimensions)

* [Next](/docs/next/usewindowdimensions)* [0.79](/docs/usewindowdimensions)* [0.78](/docs/0.78/usewindowdimensions)* [0.77](/docs/0.77/usewindowdimensions)* [0.76](/docs/0.76/usewindowdimensions)* [0.75](/docs/0.75/usewindowdimensions)* [0.74](/docs/0.74/usewindowdimensions)* [0.73](/docs/0.73/usewindowdimensions)* [0.72](/docs/0.72/usewindowdimensions)* [0.71](/docs/0.71/usewindowdimensions)* [0.70](/docs/0.70/usewindowdimensions)* [All versions](/versions)

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

useWindowDimensions
===================

tsx

```
import {useWindowDimensions} from 'react-native';  

```

`useWindowDimensions` automatically updates all of its values when screen size or font scale changes. You can get your application window's width and height like so:

tsx

```
const {height, width} = useWindowDimensions();  

```

Example[​](#example "Direct link to Example")
---------------------------------------------

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### `fontScale`[​](#fontscale "Direct link to fontscale")

tsx

```
useWindowDimensions().fontScale;  

```

The scale of the font currently used. Some operating systems allow users to scale their font sizes larger or smaller for reading comfort. This property will let you know what is in effect.

---

### `height`[​](#height "Direct link to height")

tsx

```
useWindowDimensions().height;  

```

The height in pixels of the window or screen your app occupies.

---

### `scale`[​](#scale "Direct link to scale")

tsx

```
useWindowDimensions().scale;  

```

The pixel ratio of the device your app is running on. The values can be:

* `1` which indicates that one point equals one pixel (usually PPI/DPI of 96, 76 on some platforms).
* `2` or `3` which indicates a Retina or high DPI display.

---

### `width`[​](#width "Direct link to width")

tsx

```
useWindowDimensions().width;  

```

The width in pixels of the window or screen your app occupies.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/usewindowdimensions.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/usewindowdimensions.md)

Last updated on **Apr 14, 2025**

[Previous

useColorScheme](/docs/usecolorscheme)[Next

BackHandler](/docs/backhandler)

* [Example](#example)* [Properties](#properties)
    + [`fontScale`](#fontscale)+ [`height`](#height)+ [`scale`](#scale)+ [`width`](#width)

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