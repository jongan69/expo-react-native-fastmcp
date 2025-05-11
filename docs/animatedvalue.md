Animated.Value · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/animatedvalue)

* [Next](/docs/next/animatedvalue)* [0.79](/docs/animatedvalue)* [0.78](/docs/0.78/animatedvalue)* [0.77](/docs/0.77/animatedvalue)* [0.76](/docs/0.76/animatedvalue)* [0.75](/docs/0.75/animatedvalue)* [0.74](/docs/0.74/animatedvalue)* [0.73](/docs/0.73/animatedvalue)* [0.72](/docs/0.72/animatedvalue)* [0.71](/docs/0.71/animatedvalue)* [0.70](/docs/0.70/animatedvalue)* [All versions](/versions)

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

Animated.Value
==============

Standard value for driving animations. One `Animated.Value` can drive multiple properties in a synchronized fashion, but can only be driven by one mechanism at a time. Using a new mechanism (e.g. starting a new animation, or calling `setValue`) will stop any previous ones.

Typically initialized with `useAnimatedValue(0);` or `new Animated.Value(0);` in class components.

---

Reference
=========

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### `setValue()`[​](#setvalue "Direct link to setvalue")

tsx

```
setValue(value: number);  

```

Directly set the value. This will stop any animations running on the value and update all the bound properties.

**Parameters:**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  | | --- | --- | --- | --- | | value number Yes Value | | | | | | | |

---

### `setOffset()`[​](#setoffset "Direct link to setoffset")

tsx

```
setOffset(offset: number);  

```

Sets an offset that is applied on top of whatever value is set, whether via `setValue`, an animation, or `Animated.event`. Useful for compensating things like the start of a pan gesture.

**Parameters:**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  | | --- | --- | --- | --- | | offset number Yes Offset value | | | | | | | |

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
addListener(callback: (state: {value: number}) => void): string;  

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
stopAnimation(callback?: (value: number) => void);  

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
resetAnimation(callback?: (value: number) => void);  

```

Stops any animation and resets the value to its original.

**Parameters:**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  | | --- | --- | --- | --- | | callback function No A function that will receive the original value. | | | | | | | |

---

### `interpolate()`[​](#interpolate "Direct link to interpolate")

tsx

```
interpolate(config: InterpolationConfigType);  

```

Interpolates the value before updating the property, e.g. mapping 0-1 to 0-10.

See `AnimatedInterpolation.js`

**Parameters:**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  | | --- | --- | --- | --- | | config object Yes See below. | | | | | | | |

The `config` object is composed of the following keys:

* `inputRange`: an array of numbers
* `outputRange`: an array of numbers or strings
* `easing` (optional): a function that returns a number, given an input number
* `extrapolate` (optional): a string such as 'extend', 'identity', or 'clamp'
* `extrapolateLeft` (optional): a string such as 'extend', 'identity', or 'clamp'
* `extrapolateRight` (optional): a string such as 'extend', 'identity', or 'clamp'

---

### `animate()`[​](#animate "Direct link to animate")

tsx

```
animate(animation, callback);  

```

Typically only used internally, but could be used by a custom Animation class.

**Parameters:**

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | animation Animation Yes See `Animation.js`.| callback function Yes Callback function. | | | | | | | | | | | |

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/animatedvalue.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/animatedvalue.md)

Last updated on **Apr 14, 2025**

[Previous

Animated](/docs/animated)[Next

Animated.ValueXY](/docs/animatedvaluexy)

* [Methods](#methods)
  + [`setValue()`](#setvalue)+ [`setOffset()`](#setoffset)+ [`flattenOffset()`](#flattenoffset)+ [`extractOffset()`](#extractoffset)+ [`addListener()`](#addlistener)+ [`removeListener()`](#removelistener)+ [`removeAllListeners()`](#removealllisteners)+ [`stopAnimation()`](#stopanimation)+ [`resetAnimation()`](#resetanimation)+ [`interpolate()`](#interpolate)+ [`animate()`](#animate)

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