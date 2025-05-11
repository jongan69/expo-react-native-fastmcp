Dimensions · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/dimensions)

* [Next](/docs/next/dimensions)* [0.79](/docs/dimensions)* [0.78](/docs/0.78/dimensions)* [0.77](/docs/0.77/dimensions)* [0.76](/docs/0.76/dimensions)* [0.75](/docs/0.75/dimensions)* [0.74](/docs/0.74/dimensions)* [0.73](/docs/0.73/dimensions)* [0.72](/docs/0.72/dimensions)* [0.71](/docs/0.71/dimensions)* [0.70](/docs/0.70/dimensions)* [All versions](/versions)

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

Dimensions
==========

> [`useWindowDimensions`](/docs/usewindowdimensions) is the preferred API for React components. Unlike `Dimensions`, it updates as the window's dimensions update. This works nicely with the React paradigm.

tsx

```
import {Dimensions} from 'react-native';  

```

You can get the application window's width and height using the following code:

tsx

```
const windowWidth = Dimensions.get('window').width;  
const windowHeight = Dimensions.get('window').height;  

```

> Although dimensions are available immediately, they may change (e.g due to device rotation, foldable devices etc) so any rendering logic or styles that depend on these constants should try to call this function on every render, rather than caching the value (for example, using inline styles rather than setting a value in a `StyleSheet`).

If you are targeting foldable devices or devices which can change the screen size or app window size, you can use the event listener available in the Dimensions module as shown in the below example.

Example[​](#example "Direct link to Example")
---------------------------------------------

Reference
=========

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### `addEventListener()`[​](#addeventlistener "Direct link to addeventlistener")

tsx

```
static addEventListener(  
  type: 'change',  
  handler: ({  
    window,  
    screen,  
  }: DimensionsValue) => void,  
): EmitterSubscription;  

```

Add an event handler. Supported events:

* `change`: Fires when a property within the `Dimensions` object changes. The argument to the event handler is a [`DimensionsValue`](#dimensionsvalue) type object.

---

### `get()`[​](#get "Direct link to get")

tsx

```
static get(dim: 'window' | 'screen'): ScaledSize;  

```

Initial dimensions are set before `runApplication` is called so they should be available before any other require's are run, but may be updated later.

Example: `const {height, width} = Dimensions.get('window');`

**Parameters:**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Name Type Description|  |  |  | | --- | --- | --- | | dim Required  string Name of dimension as defined when calling `set`. Returns value for the dimension. | | | | | |

> For Android the `window` dimension will exclude the size used by the `status bar` (if not translucent) and `bottom navigation bar`

---

Type Definitions[​](#type-definitions "Direct link to Type Definitions")
------------------------------------------------------------------------

### DimensionsValue[​](#dimensionsvalue "Direct link to DimensionsValue")

**Properties:**

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Description|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | window [ScaledSize](/docs/dimensions#scaledsize) Size of the visible Application window.|  |  |  | | --- | --- | --- | | screen [ScaledSize](/docs/dimensions#scaledsize) Size of the device's screen. | | | | | | | | |

### ScaledSize[​](#scaledsize "Direct link to ScaledSize")

|  |  |
| --- | --- |
| Type|  | | --- | | object | |

**Properties:**

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | width number|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | height number|  |  |  |  | | --- | --- | --- | --- | | scale number|  |  | | --- | --- | | fontScale number | | | | | | | | | |

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/dimensions.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/dimensions.md)

Last updated on **Apr 14, 2025**

[Previous

DevSettings](/docs/devsettings)[Next

Easing](/docs/easing)

* [Example](#example)* [Methods](#methods)
    + [`addEventListener()`](#addeventlistener)+ [`get()`](#get)* [Type Definitions](#type-definitions)
      + [DimensionsValue](#dimensionsvalue)+ [ScaledSize](#scaledsize)

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