DynamicColorIOS · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/dynamiccolorios)

* [Next](/docs/next/dynamiccolorios)* [0.79](/docs/dynamiccolorios)* [0.78](/docs/0.78/dynamiccolorios)* [0.77](/docs/0.77/dynamiccolorios)* [0.76](/docs/0.76/dynamiccolorios)* [0.75](/docs/0.75/dynamiccolorios)* [0.74](/docs/0.74/dynamiccolorios)* [0.73](/docs/0.73/dynamiccolorios)* [0.72](/docs/0.72/dynamiccolorios)* [0.71](/docs/0.71/dynamiccolorios)* [0.70](/docs/0.70/dynamiccolorios)* [All versions](/versions)

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

DynamicColorIOS
===============

The `DynamicColorIOS` function is a platform color type specific to iOS.

tsx

```
DynamicColorIOS({  
  light: color,  
  dark: color,  
  highContrastLight: color, // (optional) will fallback to "light" if not provided  
  highContrastDark: color, // (optional) will fallback to "dark" if not provided  
});  

```

`DynamicColorIOS` takes a single argument as an object with two mandatory keys: `dark` and `light`, and two optional keys `highContrastLight` and `highContrastDark`. These correspond to the colors you want to use for "light mode" and "dark mode" on iOS, and when high contrast accessibility mode is enabled, high contrast version of them.

At runtime, the system will choose which of the colors to display depending on the current system appearance and accessibility settings. Dynamic colors are useful for branding colors or other app specific colors that still respond automatically to system setting changes.

#### Developer notes[​](#developer-notes "Direct link to Developer notes")

* iOS* Web

> If you’re familiar with `@media (prefers-color-scheme: dark)` in CSS, this is similar! Only instead of defining all the colors in a media query, you define which color to use under what circumstances right there where you're using it. Neat!

> The `DynamicColorIOS` function is similar to the iOS native methods [`UIColor colorWithDynamicProvider:`](https://developer.apple.com/documentation/uikit/uicolor/3238040-colorwithdynamicprovider)

Example[​](#example "Direct link to Example")
---------------------------------------------

tsx

```
import {DynamicColorIOS} from 'react-native';  
  
const customDynamicTextColor = DynamicColorIOS({  
  dark: 'lightskyblue',  
  light: 'midnightblue',  
});  
  
const customContrastDynamicTextColor = DynamicColorIOS({  
  dark: 'darkgray',  
  light: 'lightgray',  
  highContrastDark: 'black',  
  highContrastLight: 'white',  
});  

```

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/dynamiccolorios.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/dynamiccolorios.md)

Last updated on **Apr 14, 2025**

[Previous

ActionSheetIOS](/docs/actionsheetios)[Next

Settings](/docs/settings)

* [Example](#example)

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