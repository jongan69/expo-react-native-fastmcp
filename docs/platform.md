Platform · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/platform)

* [Next](/docs/next/platform)* [0.79](/docs/platform)* [0.78](/docs/0.78/platform)* [0.77](/docs/0.77/platform)* [0.76](/docs/0.76/platform)* [0.75](/docs/0.75/platform)* [0.74](/docs/0.74/platform)* [0.73](/docs/0.73/platform)* [0.72](/docs/0.72/platform)* [0.71](/docs/0.71/platform)* [0.70](/docs/0.70/platform)* [All versions](/versions)

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

Platform
========

Example[​](#example "Direct link to Example")
---------------------------------------------

---

Reference
=========

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### `constants`[​](#constants "Direct link to constants")

tsx

```
static constants: PlatformConstants;  

```

Returns an object which contains all available common and specific constants related to the platform.

**Properties:**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name  Type Optional Description|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | isTesting boolean No |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | reactNativeVersion object No Information about React Native version. Keys are `major`, `minor`, `patch` with optional `prerelease` and values are `number`s.| Version Android  number No OS version constant specific to Android.|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Release Android  string No |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Serial Android  string No Hardware serial number of an Android device.|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Fingerprint Android  string No A string that uniquely identifies the build.|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Model Android  string No The end-user-visible name for the Android device.|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Brand Android  string No The consumer-visible brand with which the product/hardware will be associated.|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Manufacturer Android  string No The manufacturer of the Android device.|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | ServerHost Android  string Yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | uiMode Android  string No Possible values are: `'car'`, `'desk'`, `'normal'`,`'tv'`, `'watch'` and `'unknown'`. Read more about [Android ModeType](https://developer.android.com/reference/android/app/UiModeManager.html).| forceTouchAvailable iOS  boolean No Indicate the availability of 3D Touch on a device.|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | interfaceIdiom iOS  string No The interface type for the device. Read more about [UIUserInterfaceIdiom](https://developer.apple.com/documentation/uikit/uiuserinterfaceidiom).| osVersion iOS  string No OS version constant specific to iOS.|  |  |  |  | | --- | --- | --- | --- | | systemName iOS  string No OS name constant specific to iOS. | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

---

### `isPad` iOS [​](#ispad-ios "Direct link to ispad-ios")

tsx

```
static isPad: boolean;  

```

Returns a boolean which defines if device is an iPad.

|  |  |
| --- | --- |
| Type|  | | --- | | boolean | |

---

### `isTV`[​](#istv "Direct link to istv")

tsx

```
static isTV: boolean;  

```

Returns a boolean which defines if device is a TV.

|  |  |
| --- | --- |
| Type|  | | --- | | boolean | |

---

### `isVision`[​](#isvision "Direct link to isvision")

tsx

```
static isVision: boolean;  

```

Returns a boolean which defines if device is an Apple Vision. *If you are using [Apple Vision Pro (Designed for iPad)](https://developer.apple.com/documentation/visionos/checking-whether-your-app-is-compatible-with-visionos) `isVision` will be `false` but `isPad` will be `true`*

|  |  |
| --- | --- |
| Type|  | | --- | | boolean | |

---

### `isTesting`[​](#istesting "Direct link to istesting")

tsx

```
static isTesting: boolean;  

```

Returns a boolean which defines if application is running in Developer Mode with testing flag set.

|  |  |
| --- | --- |
| Type|  | | --- | | boolean | |

---

### `OS`[​](#os "Direct link to os")

tsx

```
static OS: 'android' | 'ios';  

```

Returns string value representing the current OS.

|  |  |
| --- | --- |
| Type|  | | --- | | enum(`'android'`, `'ios'`) | |

---

### `Version`[​](#version "Direct link to version")

tsx

```
static Version: 'number' | 'string';  

```

Returns the version of the OS.

|  |  |
| --- | --- |
| Type|  | | --- | | number Android   ---  string iOS | |

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### `select()`[​](#select "Direct link to select")

tsx

```
static select(config: Record<string, T>): T;  

```

Returns the most fitting value for the platform you are currently running on.

#### Parameters:[​](#parameters "Direct link to Parameters:")

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  | | --- | --- | --- | --- | | config object Yes See config description below. | | | | | | | |

Select method returns the most fitting value for the platform you are currently running on. That is, if you're running on a phone, `android` and `ios` keys will take preference. If those are not specified, `native` key will be used and then the `default` key.

The `config` parameter is an object with the following keys:

* `android` (any)
* `ios` (any)
* `native` (any)
* `default` (any)

**Example usage:**

tsx

```
import {Platform, StyleSheet} from 'react-native';  
  
const styles = StyleSheet.create({  
  container: {  
    flex: 1,  
    ...Platform.select({  
      android: {  
        backgroundColor: 'green',  
      },  
      ios: {  
        backgroundColor: 'red',  
      },  
      default: {  
        // other platforms, web for example  
        backgroundColor: 'blue',  
      },  
    }),  
  },  
});  

```

This will result in a container having `flex: 1` on all platforms, a green background color on Android, a red background color on iOS, and a blue background color on other platforms.

Since the value of the corresponding platform key can be of type `any`, [`select`](/docs/platform#select) method can also be used to return platform-specific components, like below:

tsx

```
const Component = Platform.select({  
  ios: () => require('ComponentIOS'),  
  android: () => require('ComponentAndroid'),  
})();  
  
<Component />;  

```

tsx

```
const Component = Platform.select({  
  native: () => require('ComponentForNative'),  
  default: () => require('ComponentForWeb'),  
})();  
  
<Component />;  

```

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/platform.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/platform.md)

Last updated on **Apr 14, 2025**

[Previous

PixelRatio](/docs/pixelratio)[Next

PlatformColor](/docs/platformcolor)

* [Example](#example)* [Properties](#properties)
    + [`constants`](#constants)+ [`isPad`

        iOS](#ispad-ios)+ [`isTV`](#istv)+ [`isVision`](#isvision)+ [`isTesting`](#istesting)+ [`OS`](#os)+ [`Version`](#version)* [Methods](#methods)
      + [`select()`](#select)

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