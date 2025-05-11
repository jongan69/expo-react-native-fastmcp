Alert · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/alert)

* [Next](/docs/next/alert)* [0.79](/docs/alert)* [0.78](/docs/0.78/alert)* [0.77](/docs/0.77/alert)* [0.76](/docs/0.76/alert)* [0.75](/docs/0.75/alert)* [0.74](/docs/0.74/alert)* [0.73](/docs/0.73/alert)* [0.72](/docs/0.72/alert)* [0.71](/docs/0.71/alert)* [0.70](/docs/0.70/alert)* [All versions](/versions)

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

Alert
=====

Launches an alert dialog with the specified title and message.

Optionally provide a list of buttons. Tapping any button will fire the respective onPress callback and dismiss the alert. By default, the only button will be an 'OK' button.

This is an API that works both on Android and iOS and can show static alerts. Alert that prompts the user to enter some information is available on iOS only.

Example[​](#example "Direct link to Example")
---------------------------------------------

iOS[​](#ios "Direct link to iOS")
---------------------------------

On iOS you can specify any number of buttons. Each button can optionally specify a style or be emphasized, available options are represented by the [AlertButtonStyle](#alertbuttonstyle-ios) enum and the `isPreferred` field on [AlertButton](/docs/alert#alertbutton).

Android[​](#android "Direct link to Android")
---------------------------------------------

On Android at most three buttons can be specified. Android has a concept of a neutral, negative and a positive button:

* If you specify one button, it will be the 'positive' one (such as 'OK')
* Two buttons mean 'negative', 'positive' (such as 'Cancel', 'OK')
* Three buttons mean 'neutral', 'negative', 'positive' (such as 'Later', 'Cancel', 'OK')

Alerts on Android can be dismissed by tapping outside of the alert box. It is disabled by default and can be enabled by providing an optional [AlertOptions](/docs/alert#alertoptions) parameter with the cancelable property set to `true` i.e.  
`{cancelable: true}`.

The cancel event can be handled by providing an `onDismiss` callback property inside the `options` parameter.

### Example Android [​](#example-android "Direct link to example-android")

---

Reference
=========

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### `alert()`[​](#alert "Direct link to alert")

tsx

```
static alert (  
  title: string,  
  message?: string,  
  buttons?: AlertButton[],  
  options?: AlertOptions,  
);  

```

**Parameters:**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Description|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | title Required  string The dialog's title. Passing `null` or empty string will hide the title.| message string An optional message that appears below the dialog's title.|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | buttons [AlertButton](/docs/alert#alertbutton)[] An optional array containing buttons configuration.|  |  |  | | --- | --- | --- | | options [AlertOptions](/docs/alert#alertoptions) An optional Alert configuration. | | | | | | | | | | | | | | |

---

### `prompt()` iOS [​](#prompt-ios "Direct link to prompt-ios")

tsx

```
static prompt: (  
  title: string,  
  message?: string,  
  callbackOrButtons?: ((text: string) => void) | AlertButton[],  
  type?: AlertType,  
  defaultValue?: string,  
  keyboardType?: string,  
);  

```

Create and display a prompt to enter some text in form of Alert.

**Parameters:**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Description|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | title Required  string The dialog's title.|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | message string An optional message that appears above the text input.|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | callbackOrButtons function  ---  [AlertButton](/docs/alert#alertButton)[] If passed a function, it will be called with the prompt's value `(text: string) => void`, when the user taps 'OK'.  ---  If passed an array, buttons will be configured based on the array content.| type [AlertType](/docs/alert#alerttype-ios) This configures the text input.|  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | defaultValue string The default text in text input.|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | keyboardType string The keyboard type of first text field (if exists). One of TextInput [keyboardTypes](/docs/textinput#keyboardtype).| options [AlertOptions](/docs/alert#alertoptions) An optional Alert configuration. | | | | | | | | | | | | | | | | | | | | | | | |

---

Type Definitions[​](#type-definitions "Direct link to Type Definitions")
------------------------------------------------------------------------

### AlertButtonStyle iOS [​](#alertbuttonstyle-ios "Direct link to alertbuttonstyle-ios")

An iOS Alert button style.

|  |  |
| --- | --- |
| Type|  | | --- | | enum | |

**Constants:**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Value Description|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | `'default'` Default button style.|  |  |  |  | | --- | --- | --- | --- | | `'cancel'` Cancel button style.|  |  | | --- | --- | | `'destructive'` Destructive button style. | | | | | | | |

---

### AlertType iOS [​](#alerttype-ios "Direct link to alerttype-ios")

An iOS Alert type.

|  |  |
| --- | --- |
| Type|  | | --- | | enum | |

**Constants:**

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Value Description|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | `'default'` Default alert with no inputs|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | `'plain-text'` Plain text input alert|  |  |  |  | | --- | --- | --- | --- | | `'secure-text'` Secure text input alert|  |  | | --- | --- | | `'login-password'` Login and password alert | | | | | | | | | |

---

### AlertButton[​](#alertbutton "Direct link to AlertButton")

An object describing the configuration of a button in the alert.

|  |  |
| --- | --- |
| Type|  | | --- | | array of objects | |

**Objects properties:**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Description|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | text string Button label.|  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | onPress function Callback function when button is pressed.|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | style iOS  [AlertButtonStyle](/docs/alert#alertbuttonstyle-ios) Button style, on Android this property will be ignored.|  |  |  | | --- | --- | --- | | isPreferred iOS  boolean Whether button should be emphasized, on Android this property will be ignored. | | | | | | | | | | | | | | |

---

### AlertOptions[​](#alertoptions "Direct link to AlertOptions")

|  |  |
| --- | --- |
| Type|  | | --- | | object | |

**Properties:**

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Description|  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | cancelable Android  boolean Defines if alert can be dismissed by tapping outside of the alert box.|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | userInterfaceStyle iOS  string The interface style used for the alert, can be set to `light` or `dark`, otherwise the default system style will be used.| onDismiss Android  function Callback function fired when alert has been dismissed. | | | | | | | | | | | |

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/alert.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/alert.md)

Last updated on **Apr 14, 2025**

[Previous

AccessibilityInfo](/docs/accessibilityinfo)[Next

Animated](/docs/animated)

* [Example](#example)* [iOS](#ios)* [Android](#android)
      + [Example

        Android](#example-android)* [Methods](#methods)
        + [`alert()`](#alert)+ [`prompt()`

            iOS](#prompt-ios)* [Type Definitions](#type-definitions)
          + [AlertButtonStyle

            iOS](#alertbuttonstyle-ios)+ [AlertType

              iOS](#alerttype-ios)+ [AlertButton](#alertbutton)+ [AlertOptions](#alertoptions)

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