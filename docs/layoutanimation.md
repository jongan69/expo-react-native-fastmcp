LayoutAnimation · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/layoutanimation)

* [Next](/docs/next/layoutanimation)* [0.79](/docs/layoutanimation)* [0.78](/docs/0.78/layoutanimation)* [0.77](/docs/0.77/layoutanimation)* [0.76](/docs/0.76/layoutanimation)* [0.75](/docs/0.75/layoutanimation)* [0.74](/docs/0.74/layoutanimation)* [0.73](/docs/0.73/layoutanimation)* [0.72](/docs/0.72/layoutanimation)* [0.71](/docs/0.71/layoutanimation)* [0.70](/docs/0.70/layoutanimation)* [All versions](/versions)

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

LayoutAnimation
===============

Automatically animates views to their new positions when the next layout happens.

A common way to use this API is to call it before updating the state hook in functional components and calling `setState` in class components.

Note that in order to get this to work on **Android** you need to set the following flags via `UIManager`:

js

```
if (Platform.OS === 'android') {  
  if (UIManager.setLayoutAnimationEnabledExperimental) {  
    UIManager.setLayoutAnimationEnabledExperimental(true);  
  }  
}  

```

Example[​](#example "Direct link to Example")
---------------------------------------------

---

Reference
=========

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### `configureNext()`[​](#configurenext "Direct link to configurenext")

tsx

```
static configureNext(  
  config: LayoutAnimationConfig,  
  onAnimationDidEnd?: () => void,  
  onAnimationDidFail?: () => void,  
);  

```

Schedules an animation to happen on the next layout.

#### Parameters:[​](#parameters "Direct link to Parameters:")

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | config object Yes See config description below.|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | onAnimationDidEnd function No Called when the animation finished.|  |  |  |  | | --- | --- | --- | --- | | onAnimationDidFail function No Called when the animation failed. | | | | | | | | | | | | | | | |

The `config` parameter is an object with the keys below. [`create`](/docs/layoutanimation#create) returns a valid object for `config`, and the [`Presets`](/docs/layoutanimation#presets) objects can also all be passed as the `config`.

* `duration` in milliseconds
* `create`, optional config for animating in new views
* `update`, optional config for animating views that have been updated
* `delete`, optional config for animating views as they are removed

The config that's passed to `create`, `update`, or `delete` has the following keys:

* `type`, the [animation type](/docs/layoutanimation#types) to use
* `property`, the [layout property](/docs/layoutanimation#properties) to animate (optional, but recommended for `create` and `delete`)
* `springDamping` (number, optional and only for use with `type: Type.spring`)
* `initialVelocity` (number, optional)
* `delay` (number, optional)
* `duration` (number, optional)

---

### `create()`[​](#create "Direct link to create")

tsx

```
static create(duration, type, creationProp)  

```

Helper that creates an object (with `create`, `update`, and `delete` fields) to pass into [`configureNext`](/docs/layoutanimation#configurenext). The `type` parameter is an [animation type](/docs/layoutanimation#types), and the `creationProp` parameter is a [layout property](/docs/layoutanimation#properties).

**Example:**

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### Types[​](#types "Direct link to Types")

An enumeration of animation types to be used in the [`create`](/docs/layoutanimation#create) method, or in the `create`/`update`/`delete` configs for [`configureNext`](/docs/layoutanimation#configurenext). (example usage: `LayoutAnimation.Types.easeIn`)

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Types|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | spring|  |  |  |  |  | | --- | --- | --- | --- | --- | | linear|  |  |  |  | | --- | --- | --- | --- | | easeInEaseOut|  |  |  | | --- | --- | --- | | easeIn|  |  | | --- | --- | | easeOut|  | | --- | | keyboard | | | | | | |

---

### Properties[​](#properties-1 "Direct link to Properties")

An enumeration of layout properties to be animated to be used in the [`create`](/docs/layoutanimation#create) method, or in the `create`/`update`/`delete` configs for [`configureNext`](/docs/layoutanimation#configurenext). (example usage: `LayoutAnimation.Properties.opacity`)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Properties|  |  |  |  | | --- | --- | --- | --- | | opacity|  |  |  | | --- | --- | --- | | scaleX|  |  | | --- | --- | | scaleY|  | | --- | | scaleXY | | | | |

---

### Presets[​](#presets "Direct link to Presets")

A set of predefined animation configs to pass into [`configureNext`](/docs/layoutanimation#configurenext).

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Presets Value|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | easeInEaseOut `create(300, 'easeInEaseOut', 'opacity')`| linear `create(500, 'linear', 'opacity')`| spring `{duration: 700, create: {type: 'linear', property: 'opacity'}, update: {type: 'spring', springDamping: 0.4}, delete: {type: 'linear', property: 'opacity'} }` | | | | | | | |

---

### `easeInEaseOut`[​](#easeineaseout "Direct link to easeineaseout")

Calls `configureNext()` with `Presets.easeInEaseOut`.

---

### `linear`[​](#linear "Direct link to linear")

Calls `configureNext()` with `Presets.linear`.

---

### `spring`[​](#spring "Direct link to spring")

Calls `configureNext()` with `Presets.spring`.

**Example:**

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/layoutanimation.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/layoutanimation.md)

Last updated on **Apr 14, 2025**

[Previous

Keyboard](/docs/keyboard)[Next

Linking](/docs/linking)

* [Example](#example)* [Methods](#methods)
    + [`configureNext()`](#configurenext)+ [`create()`](#create)* [Properties](#properties)
      + [Types](#types)+ [Properties](#properties-1)+ [Presets](#presets)+ [`easeInEaseOut`](#easeineaseout)+ [`linear`](#linear)+ [`spring`](#spring)

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