StyleSheet · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/stylesheet)

* [Next](/docs/next/stylesheet)* [0.79](/docs/stylesheet)* [0.78](/docs/0.78/stylesheet)* [0.77](/docs/0.77/stylesheet)* [0.76](/docs/0.76/stylesheet)* [0.75](/docs/0.75/stylesheet)* [0.74](/docs/0.74/stylesheet)* [0.73](/docs/0.73/stylesheet)* [0.72](/docs/0.72/stylesheet)* [0.71](/docs/0.71/stylesheet)* [0.70](/docs/0.70/stylesheet)* [All versions](/versions)

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

StyleSheet
==========

A StyleSheet is an abstraction similar to CSS StyleSheets.

Code quality tips:

* By moving styles away from the render function, you're making the code easier to understand.
* Naming the styles is a good way to add meaning to the low level components in the render function, and encourage reuse.
* In most IDEs, using `StyleSheet.create()` will offer static type checking and suggestions to help you write valid styles.

---

Reference
=========

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### `compose()`[​](#compose "Direct link to compose")

tsx

```
static compose(style1: Object, style2: Object): Object | Object[];  

```

Combines two styles such that `style2` will override any styles in `style1`. If either style is falsy, the other one is returned without allocating an array, saving allocations and maintaining reference equality for PureComponent checks.

---

### `create()`[​](#create "Direct link to create")

tsx

```
static create(styles: Object extends Record<string, ViewStyle | ImageStyle | TextStyle>): Object;  

```

An identity function for creating styles. The main practical benefit of creating styles inside `StyleSheet.create()` is static type checking against native style properties.

---

### `flatten()`[​](#flatten "Direct link to flatten")

tsx

```
static flatten(style: Array<Object extends Record<string, ViewStyle | ImageStyle | TextStyle>>): Object;  

```

Flattens an array of style objects, into one aggregated style object.

---

### `setStyleAttributePreprocessor()`[​](#setstyleattributepreprocessor "Direct link to setstyleattributepreprocessor")

> **WARNING: EXPERIMENTAL.** Breaking changes will probably happen a lot and will not be reliably announced. The whole thing might be deleted, who knows? Use at your own risk.

tsx

```
static setStyleAttributePreprocessor(  
  property: string,  
  process: (propValue: any) => any,  
);  

```

Sets a function to use to pre-process a style property value. This is used internally to process color and transform values. You should not use this unless you really know what you are doing and have exhausted other options.

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

---

### `absoluteFill`[​](#absolutefill "Direct link to absolutefill")

A very common pattern is to create overlays with position absolute and zero positioning (`position: 'absolute', left: 0, right: 0, top: 0, bottom: 0`), so `absoluteFill` can be used for convenience and to reduce duplication of these repeated styles. If you want, absoluteFill can be used to create a customized entry in a StyleSheet, e.g.:

---

### `absoluteFillObject`[​](#absolutefillobject "Direct link to absolutefillobject")

Sometimes you may want `absoluteFill` but with a couple tweaks - `absoluteFillObject` can be used to create a customized entry in a `StyleSheet`, e.g.:

---

### `hairlineWidth`[​](#hairlinewidth "Direct link to hairlinewidth")

This is defined as the width of a thin line on the platform. It can be used as the thickness of a border or division between two elements. Example:

This constant will always be a round number of pixels (so a line defined by it can look crisp) and will try to match the standard width of a thin line on the underlying platform. However, you should not rely on it being a constant size, because on different platforms and screen densities its value may be calculated differently.

A line with hairline width may not be visible if your simulator is downscaled.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/stylesheet.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/stylesheet.md)

Last updated on **Apr 14, 2025**

[Previous

Share](/docs/share)[Next

Systrace](/docs/systrace)

* [Methods](#methods)
  + [`compose()`](#compose)+ [`create()`](#create)+ [`flatten()`](#flatten)+ [`setStyleAttributePreprocessor()`](#setstyleattributepreprocessor)* [Properties](#properties)
    + [`absoluteFill`](#absolutefill)+ [`absoluteFillObject`](#absolutefillobject)+ [`hairlineWidth`](#hairlinewidth)

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