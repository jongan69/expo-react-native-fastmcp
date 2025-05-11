Animated.ValueXY · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/animatedvaluexy)

* [Next](/docs/next/animatedvaluexy)* [0.79](/docs/animatedvaluexy)* [0.78](/docs/0.78/animatedvaluexy)* [0.77](/docs/0.77/animatedvaluexy)* [0.76](/docs/0.76/animatedvaluexy)* [0.75](/docs/0.75/animatedvaluexy)* [0.74](/docs/0.74/animatedvaluexy)* [0.73](/docs/0.73/animatedvaluexy)* [0.72](/docs/0.72/animatedvaluexy)* [0.71](/docs/0.71/animatedvaluexy)* [0.70](/docs/0.70/animatedvaluexy)* [All versions](/versions)

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

Animated.ValueXY
================

2D Value for driving 2D animations, such as pan gestures. Almost identical API to normal [`Animated.Value`](/docs/animatedvalue), but multiplexed. Contains two regular `Animated.Value`s under the hood.

Example[​](#example "Direct link to Example")
---------------------------------------------

---

Reference
=========

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### `setValue()`[​](#setvalue "Direct link to setvalue")

tsx

```
setValue(value: {x: number; y: number});  

```

Directly set the value. This will stop any animations running on the value and update all the bound properties.

**Parameters:**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  | | --- | --- | --- | --- | | value `{x: number; y: number}` Yes Value | | | | | | | |

---

### `setOffset()`[​](#setoffset "Direct link to setoffset")

tsx

```
setOffset(offset: {x: number; y: number});  

```

Sets an offset that is applied on top of whatever value is set, whether via `setValue`, an animation, or `Animated.event`. Useful for compensating things like the start of a pan gesture.

**Parameters:**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  | | --- | --- | --- | --- | | offset `{x: number; y: number}` Yes Offset value | | | | | | | |

---

### `flattenOffset()`[​](#flattenoffset "Direct link to flattenoffset")

tsx

```
flattenOffset();  

```

Merges the offset value into the base value and resets the offset to zero. The final output of the value is unchanged.

---

### `extractOffset()`[​](#extractoffset "Direct link to extractoffset")

tsx

```
extractOffset();  

```

Sets the offset value to the base value, and resets the base value to zero. The final output of the value is unchanged.

---

### `addListener()`[​](#addlistener "Direct link to addlistener")

tsx

```
addListener(callback: (value: {x: number; y: number}) => void);  

```

Adds an asynchronous listener to the value so you can observe updates from animations. This is useful because there is no way to synchronously read the value because it might be driven natively.

Returns a string that serves as an identifier for the listener.

**Parameters:**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  | | --- | --- | --- | --- | | callback function Yes The callback function which will receive an object with a `value` key set to the new value. | | | | | | | |

---

### `removeListener()`[​](#removelistener "Direct link to removelistener")

tsx

```
removeListener(id: string);  

```

Unregister a listener. The `id` param shall match the identifier previously returned by `addListener()`.

**Parameters:**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  | | --- | --- | --- | --- | | id string Yes Id for the listener being removed. | | | | | | | |

---

### `removeAllListeners()`[​](#removealllisteners "Direct link to removealllisteners")

tsx

```
removeAllListeners();  

```

Remove all registered listeners.

---

### `stopAnimation()`[​](#stopanimation "Direct link to stopanimation")

tsx

```
stopAnimation(callback?: (value: {x: number; y: number}) => void);  

```

Stops any running animation or tracking. `callback` is invoked with the final value after stopping the animation, which is useful for updating state to match the animation position with layout.

**Parameters:**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  | | --- | --- | --- | --- | | callback function No A function that will receive the final value. | | | | | | | |

---

### `resetAnimation()`[​](#resetanimation "Direct link to resetanimation")

tsx

```
resetAnimation(callback?: (value: {x: number; y: number}) => void);  

```

Stops any animation and resets the value to its original.

**Parameters:**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  | | --- | --- | --- | --- | | callback function No A function that will receive the original value. | | | | | | | |

---

### `getLayout()`[​](#getlayout "Direct link to getlayout")

tsx

```
getLayout(): {left: Animated.Value, top: Animated.Value};  

```

Converts `{x, y}` into `{left, top}` for use in style, e.g.

tsx

```
style={this.state.anim.getLayout()}  

```

---

### `getTranslateTransform()`[​](#gettranslatetransform "Direct link to gettranslatetransform")

tsx

```
getTranslateTransform(): [  
  {translateX: Animated.Value},  
  {translateY: Animated.Value},  
];  

```

Converts `{x, y}` into a useable translation transform, e.g.

tsx

```
style={{  
  transform: this.state.anim.getTranslateTransform()  
}}  

```

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/animatedvaluexy.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/animatedvaluexy.md)

Last updated on **Apr 14, 2025**

[Previous

Animated.Value](/docs/animatedvalue)[Next

Appearance](/docs/appearance)

* [Example](#example)* [Methods](#methods)
    + [`setValue()`](#setvalue)+ [`setOffset()`](#setoffset)+ [`flattenOffset()`](#flattenoffset)+ [`extractOffset()`](#extractoffset)+ [`addListener()`](#addlistener)+ [`removeListener()`](#removelistener)+ [`removeAllListeners()`](#removealllisteners)+ [`stopAnimation()`](#stopanimation)+ [`resetAnimation()`](#resetanimation)+ [`getLayout()`](#getlayout)+ [`getTranslateTransform()`](#gettranslatetransform)

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