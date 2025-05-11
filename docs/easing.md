Easing · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/easing)

* [Next](/docs/next/easing)* [0.79](/docs/easing)* [0.78](/docs/0.78/easing)* [0.77](/docs/0.77/easing)* [0.76](/docs/0.76/easing)* [0.75](/docs/0.75/easing)* [0.74](/docs/0.74/easing)* [0.73](/docs/0.73/easing)* [0.72](/docs/0.72/easing)* [0.71](/docs/0.71/easing)* [0.70](/docs/0.70/easing)* [All versions](/versions)

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

Easing
======

The `Easing` module implements common easing functions. This module is used by [`Animated.timing()`](/docs/animated#timing) to convey physically believable motion in animations.

You can find a visualization of some common easing functions at <https://easings.net/>

### Predefined animations[​](#predefined-animations "Direct link to Predefined animations")

The `Easing` module provides several predefined animations through the following methods:

* [`back`](/docs/easing#back) provides a basic animation where the object goes slightly back before moving forward
* [`bounce`](/docs/easing#bounce) provides a bouncing animation
* [`ease`](/docs/easing#ease) provides a basic inertial animation
* [`elastic`](/docs/easing#elastic) provides a basic spring interaction

### Standard functions[​](#standard-functions "Direct link to Standard functions")

Three standard easing functions are provided:

* [`linear`](/docs/easing#linear)
* [`quad`](/docs/easing#quad)
* [`cubic`](/docs/easing#cubic)

The [`poly`](/docs/easing#poly) function can be used to implement quartic, quintic, and other higher power functions.

### Additional functions[​](#additional-functions "Direct link to Additional functions")

Additional mathematical functions are provided by the following methods:

* [`bezier`](/docs/easing#bezier) provides a cubic bezier curve
* [`circle`](/docs/easing#circle) provides a circular function
* [`sin`](/docs/easing#sin) provides a sinusoidal function
* [`exp`](/docs/easing#exp) provides an exponential function

The following helpers are used to modify other easing functions.

* [`in`](/docs/easing#in) runs an easing function forwards
* [`inOut`](/docs/easing#inout) makes any easing function symmetrical
* [`out`](/docs/easing#out) runs an easing function backwards

Example[​](#example "Direct link to Example")
---------------------------------------------

* TypeScript* JavaScript

---

Reference
=========

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### `step0()`[​](#step0 "Direct link to step0")

tsx

```
static step0(n: number);  

```

A stepping function, returns 1 for any positive value of `n`.

---

### `step1()`[​](#step1 "Direct link to step1")

tsx

```
static step1(n: number);  

```

A stepping function, returns 1 if `n` is greater than or equal to 1.

---

### `linear()`[​](#linear "Direct link to linear")

tsx

```
static linear(t: number);  

```

A linear function, `f(t) = t`. Position correlates to elapsed time one to one.

<https://cubic-bezier.com/#0,0,1,1>

---

### `ease()`[​](#ease "Direct link to ease")

tsx

```
static ease(t: number);  

```

A basic inertial interaction, similar to an object slowly accelerating to speed.

<https://cubic-bezier.com/#.42,0,1,1>

---

### `quad()`[​](#quad "Direct link to quad")

tsx

```
static quad(t: number);  

```

A quadratic function, `f(t) = t * t`. Position equals the square of elapsed time.

<https://easings.net/#easeInQuad>

---

### `cubic()`[​](#cubic "Direct link to cubic")

tsx

```
static cubic(t: number);  

```

A cubic function, `f(t) = t * t * t`. Position equals the cube of elapsed time.

<https://easings.net/#easeInCubic>

---

### `poly()`[​](#poly "Direct link to poly")

tsx

```
static poly(n: number);  

```

A power function. Position is equal to the Nth power of elapsed time.

n = 4: <https://easings.net/#easeInQuart> n = 5: <https://easings.net/#easeInQuint>

---

### `sin()`[​](#sin "Direct link to sin")

tsx

```
static sin(t: number);  

```

A sinusoidal function.

<https://easings.net/#easeInSine>

---

### `circle()`[​](#circle "Direct link to circle")

tsx

```
static circle(t: number);  

```

A circular function.

<https://easings.net/#easeInCirc>

---

### `exp()`[​](#exp "Direct link to exp")

tsx

```
static exp(t: number);  

```

An exponential function.

<https://easings.net/#easeInExpo>

---

### `elastic()`[​](#elastic "Direct link to elastic")

tsx

```
static elastic(bounciness: number);  

```

A basic elastic interaction, similar to a spring oscillating back and forth.

Default bounciness is 1, which overshoots a little bit once. 0 bounciness doesn't overshoot at all, and bounciness of N > 1 will overshoot about N times.

<https://easings.net/#easeInElastic>

---

### `back()`[​](#back "Direct link to back")

tsx

```
static back(s)  

```

Use with `Animated.parallel()` to create a basic effect where the object animates back slightly as the animation starts.

---

### `bounce()`[​](#bounce "Direct link to bounce")

tsx

```
static bounce(t: number);  

```

Provides a basic bouncing effect.

<https://easings.net/#easeInBounce>

---

### `bezier()`[​](#bezier "Direct link to bezier")

tsx

```
static bezier(x1: number, y1: number, x2: number, y2: number);  

```

Provides a cubic bezier curve, equivalent to CSS Transitions' `transition-timing-function`.

A useful tool to visualize cubic bezier curves can be found at <https://cubic-bezier.com/>

---

### `in()`[​](#in "Direct link to in")

tsx

```
static in(easing: number);  

```

Runs an easing function forwards.

---

### `out()`[​](#out "Direct link to out")

tsx

```
static out(easing: number);  

```

Runs an easing function backwards.

---

### `inOut()`[​](#inout "Direct link to inout")

tsx

```
static inOut(easing: number);  

```

Makes any easing function symmetrical. The easing function will run forwards for half of the duration, then backwards for the rest of the duration.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/easing.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/easing.md)

Last updated on **Apr 14, 2025**

[Previous

Dimensions](/docs/dimensions)[Next

InteractionManager](/docs/interactionmanager)

* [Predefined animations](#predefined-animations)* [Standard functions](#standard-functions)* [Additional functions](#additional-functions)* [Example](#example)* [Methods](#methods)
          + [`step0()`](#step0)+ [`step1()`](#step1)+ [`linear()`](#linear)+ [`ease()`](#ease)+ [`quad()`](#quad)+ [`cubic()`](#cubic)+ [`poly()`](#poly)+ [`sin()`](#sin)+ [`circle()`](#circle)+ [`exp()`](#exp)+ [`elastic()`](#elastic)+ [`back()`](#back)+ [`bounce()`](#bounce)+ [`bezier()`](#bezier)+ [`in()`](#in)+ [`out()`](#out)+ [`inOut()`](#inout)

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