Animated · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/animated)

* [Next](/docs/next/animated)* [0.79](/docs/animated)* [0.78](/docs/0.78/animated)* [0.77](/docs/0.77/animated)* [0.76](/docs/0.76/animated)* [0.75](/docs/0.75/animated)* [0.74](/docs/0.74/animated)* [0.73](/docs/0.73/animated)* [0.72](/docs/0.72/animated)* [0.71](/docs/0.71/animated)* [0.70](/docs/0.70/animated)* [All versions](/versions)

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

Animated
========

The `Animated` library is designed to make animations fluid, powerful, and painless to build and maintain. `Animated` focuses on declarative relationships between inputs and outputs, configurable transforms in between, and `start`/`stop` methods to control time-based animation execution.

The core workflow for creating an animation is to create an `Animated.Value`, hook it up to one or more style attributes of an animated component, and then drive updates via animations using `Animated.timing()`.

> Don't modify the animated value directly. You can use the [`useRef` Hook](https://reactjs.org/docs/hooks-reference.html#useref) to return a mutable ref object. This ref object's `current` property is initialized as the given argument and persists throughout the component lifecycle.

Example[​](#example "Direct link to Example")
---------------------------------------------

The following example contains a `View` which will fade in and fade out based on the animated value `fadeAnim`

Refer to the [Animations](/docs/animations#animated-api) guide to see additional examples of `Animated` in action.

Overview[​](#overview "Direct link to Overview")
------------------------------------------------

There are two value types you can use with `Animated`:

* [`Animated.Value()`](/docs/animated#value) for single values
* [`Animated.ValueXY()`](/docs/animated#valuexy) for vectors

`Animated.Value` can bind to style properties or other props, and can be interpolated as well. A single `Animated.Value` can drive any number of properties.

### Configuring animations[​](#configuring-animations "Direct link to Configuring animations")

`Animated` provides three types of animation types. Each animation type provides a particular animation curve that controls how your values animate from their initial value to the final value:

* [`Animated.decay()`](/docs/animated#decay) starts with an initial velocity and gradually slows to a stop.
* [`Animated.spring()`](/docs/animated#spring) provides a basic spring physics model.
* [`Animated.timing()`](/docs/animated#timing) animates a value over time using [easing functions](/docs/easing).

In most cases, you will be using `timing()`. By default, it uses a symmetric easeInOut curve that conveys the gradual acceleration of an object to full speed and concludes by gradually decelerating to a stop.

### Working with animations[​](#working-with-animations "Direct link to Working with animations")

Animations are started by calling `start()` on your animation. `start()` takes a completion callback that will be called when the animation is done. If the animation finished running normally, the completion callback will be invoked with `{finished: true}`. If the animation is done because `stop()` was called on it before it could finish (e.g. because it was interrupted by a gesture or another animation), then it will receive `{finished: false}`.

tsx

```
Animated.timing({}).start(({finished}) => {  
  /* completion callback */  
});  

```

### Using the native driver[​](#using-the-native-driver "Direct link to Using the native driver")

By using the native driver, we send everything about the animation to native before starting the animation, allowing native code to perform the animation on the UI thread without having to go through the bridge on every frame. Once the animation has started, the JS thread can be blocked without affecting the animation.

You can use the native driver by specifying `useNativeDriver: true` in your animation configuration. See the [Animations](/docs/animations#using-the-native-driver) guide to learn more.

### Animatable components[​](#animatable-components "Direct link to Animatable components")

Only animatable components can be animated. These unique components do the magic of binding the animated values to the properties, and do targeted native updates to avoid the cost of the React render and reconciliation process on every frame. They also handle cleanup on unmount so they are safe by default.

* [`createAnimatedComponent()`](/docs/animated#createanimatedcomponent) can be used to make a component animatable.

`Animated` exports the following animatable components using the above wrapper:

* `Animated.Image`
* `Animated.ScrollView`
* `Animated.Text`
* `Animated.View`
* `Animated.FlatList`
* `Animated.SectionList`

### Composing animations[​](#composing-animations "Direct link to Composing animations")

Animations can also be combined in complex ways using composition functions:

* [`Animated.delay()`](/docs/animated#delay) starts an animation after a given delay.
* [`Animated.parallel()`](/docs/animated#parallel) starts a number of animations at the same time.
* [`Animated.sequence()`](/docs/animated#sequence) starts the animations in order, waiting for each to complete before starting the next.
* [`Animated.stagger()`](/docs/animated#stagger) starts animations in order and in parallel, but with successive delays.

Animations can also be chained together by setting the `toValue` of one animation to be another `Animated.Value`. See [Tracking dynamic values](/docs/animations#tracking-dynamic-values) in the Animations guide.

By default, if one animation is stopped or interrupted, then all other animations in the group are also stopped.

### Combining animated values[​](#combining-animated-values "Direct link to Combining animated values")

You can combine two animated values via addition, subtraction, multiplication, division, or modulo to make a new animated value:

* [`Animated.add()`](/docs/animated#add)
* [`Animated.subtract()`](/docs/animated#subtract)
* [`Animated.divide()`](/docs/animated#divide)
* [`Animated.modulo()`](/docs/animated#modulo)
* [`Animated.multiply()`](/docs/animated#multiply)

### Interpolation[​](#interpolation "Direct link to Interpolation")

The `interpolate()` function allows input ranges to map to different output ranges. By default, it will extrapolate the curve beyond the ranges given, but you can also have it clamp the output value. It uses linear interpolation by default but also supports easing functions.

* [`interpolate()`](/docs/animatedvalue#interpolate)

Read more about interpolation in the [Animation](/docs/animations#interpolation) guide.

### Handling gestures and other events[​](#handling-gestures-and-other-events "Direct link to Handling gestures and other events")

Gestures, like panning or scrolling, and other events can map directly to animated values using `Animated.event()`. This is done with a structured map syntax so that values can be extracted from complex event objects. The first level is an array to allow mapping across multiple args, and that array contains nested objects.

* [`Animated.event()`](/docs/animated#event)

For example, when working with horizontal scrolling gestures, you would do the following in order to map `event.nativeEvent.contentOffset.x` to `scrollX` (an `Animated.Value`):

tsx

```
 onScroll={Animated.event(  
   // scrollX = e.nativeEvent.contentOffset.x  
   [{nativeEvent: {  
        contentOffset: {  
          x: scrollX  
        }  
      }  
    }]  
 )}  

```

---

Reference
=========

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

When the given value is a ValueXY instead of a Value, each config option may be a vector of the form `{x: ..., y: ...}` instead of a scalar.

### `decay()`[​](#decay "Direct link to decay")

tsx

```
static decay(value, config): CompositeAnimation;  

```

Animates a value from an initial velocity to zero based on a decay coefficient.

Config is an object that may have the following options:

* `velocity`: Initial velocity. Required.
* `deceleration`: Rate of decay. Default 0.997.
* `isInteraction`: Whether or not this animation creates an "interaction handle" on the `InteractionManager`. Default true.
* `useNativeDriver`: Uses the native driver when true. Required.

---

### `timing()`[​](#timing "Direct link to timing")

tsx

```
static timing(value, config): CompositeAnimation;  

```

Animates a value along a timed easing curve. The [`Easing`](/docs/easing) module has tons of predefined curves, or you can use your own function.

Config is an object that may have the following options:

* `duration`: Length of animation (milliseconds). Default 500.
* `easing`: Easing function to define curve. Default is `Easing.inOut(Easing.ease)`.
* `delay`: Start the animation after delay (milliseconds). Default 0.
* `isInteraction`: Whether or not this animation creates an "interaction handle" on the `InteractionManager`. Default true.
* `useNativeDriver`: Uses the native driver when true. Required.

---

### `spring()`[​](#spring "Direct link to spring")

tsx

```
static spring(value, config): CompositeAnimation;  

```

Animates a value according to an analytical spring model based on [damped harmonic oscillation](https://en.wikipedia.org/wiki/Harmonic_oscillator#Damped_harmonic_oscillator). Tracks velocity state to create fluid motions as the `toValue` updates, and can be chained together.

Config is an object that may have the following options.

Note that you can only define one of bounciness/speed, tension/friction, or stiffness/damping/mass, but not more than one:

The friction/tension or bounciness/speed options match the spring model in [`Facebook Pop`](https://github.com/facebook/pop), [Rebound](https://github.com/facebookarchive/rebound), and [Origami](https://origami.design/).

* `friction`: Controls "bounciness"/overshoot. Default 7.
* `tension`: Controls speed. Default 40.
* `speed`: Controls speed of the animation. Default 12.
* `bounciness`: Controls bounciness. Default 8.

Specifying stiffness/damping/mass as parameters makes `Animated.spring` use an analytical spring model based on the motion equations of a [damped harmonic oscillator](https://en.wikipedia.org/wiki/Harmonic_oscillator#Damped_harmonic_oscillator). This behavior is slightly more precise and faithful to the physics behind spring dynamics, and closely mimics the implementation in iOS's CASpringAnimation.

* `stiffness`: The spring stiffness coefficient. Default 100.
* `damping`: Defines how the spring’s motion should be damped due to the forces of friction. Default 10.
* `mass`: The mass of the object attached to the end of the spring. Default 1.

Other configuration options are as follows:

* `velocity`: The initial velocity of the object attached to the spring. Default 0 (object is at rest).
* `overshootClamping`: Boolean indicating whether the spring should be clamped and not bounce. Default false.
* `restDisplacementThreshold`: The threshold of displacement from rest below which the spring should be considered at rest. Default 0.001.
* `restSpeedThreshold`: The speed at which the spring should be considered at rest in pixels per second. Default 0.001.
* `delay`: Start the animation after delay (milliseconds). Default 0.
* `isInteraction`: Whether or not this animation creates an "interaction handle" on the `InteractionManager`. Default true.
* `useNativeDriver`: Uses the native driver when true. Required.

---

### `add()`[​](#add "Direct link to add")

tsx

```
static add(a: Animated, b: Animated): AnimatedAddition;  

```

Creates a new Animated value composed from two Animated values added together.

---

### `subtract()`[​](#subtract "Direct link to subtract")

tsx

```
static subtract(a: Animated, b: Animated): AnimatedSubtraction;  

```

Creates a new Animated value composed by subtracting the second Animated value from the first Animated value.

---

### `divide()`[​](#divide "Direct link to divide")

tsx

```
static divide(a: Animated, b: Animated): AnimatedDivision;  

```

Creates a new Animated value composed by dividing the first Animated value by the second Animated value.

---

### `multiply()`[​](#multiply "Direct link to multiply")

tsx

```
static multiply(a: Animated, b: Animated): AnimatedMultiplication;  

```

Creates a new Animated value composed from two Animated values multiplied together.

---

### `modulo()`[​](#modulo "Direct link to modulo")

tsx

```
static modulo(a: Animated, modulus: number): AnimatedModulo;  

```

Creates a new Animated value that is the (non-negative) modulo of the provided Animated value

---

### `diffClamp()`[​](#diffclamp "Direct link to diffclamp")

tsx

```
static diffClamp(a: Animated, min: number, max: number): AnimatedDiffClamp;  

```

Create a new Animated value that is limited between 2 values. It uses the difference between the last value so even if the value is far from the bounds it will start changing when the value starts getting closer again. (`value = clamp(value + diff, min, max)`).

This is useful with scroll events, for example, to show the navbar when scrolling up and to hide it when scrolling down.

---

### `delay()`[​](#delay "Direct link to delay")

tsx

```
static delay(time: number): CompositeAnimation;  

```

Starts an animation after the given delay.

---

### `sequence()`[​](#sequence "Direct link to sequence")

tsx

```
static sequence(animations: CompositeAnimation[]): CompositeAnimation;  

```

Starts an array of animations in order, waiting for each to complete before starting the next. If the current running animation is stopped, no following animations will be started.

---

### `parallel()`[​](#parallel "Direct link to parallel")

tsx

```
static parallel(  
  animations: CompositeAnimation[],  
  config?: ParallelConfig  
): CompositeAnimation;  

```

Starts an array of animations all at the same time. By default, if one of the animations is stopped, they will all be stopped. You can override this with the `stopTogether` flag.

---

### `stagger()`[​](#stagger "Direct link to stagger")

tsx

```
static stagger(  
  time: number,  
  animations: CompositeAnimation[]  
): CompositeAnimation;  

```

Array of animations may run in parallel (overlap), but are started in sequence with successive delays. Nice for doing trailing effects.

---

### `loop()`[​](#loop "Direct link to loop")

tsx

```
static loop(  
  animation: CompositeAnimation[],  
  config?: LoopAnimationConfig  
): CompositeAnimation;  

```

Loops a given animation continuously, so that each time it reaches the end, it resets and begins again from the start. Will loop without blocking the JS thread if the child animation is set to `useNativeDriver: true`. In addition, loops can prevent `VirtualizedList`-based components from rendering more rows while the animation is running. You can pass `isInteraction: false` in the child animation config to fix this.

Config is an object that may have the following options:

* `iterations`: Number of times the animation should loop. Default `-1` (infinite).

---

### `event()`[​](#event "Direct link to event")

tsx

```
static event(  
  argMapping: Mapping[],  
  config?: EventConfig  
): (...args: any[]) => void;  

```

Takes an array of mappings and extracts values from each arg accordingly, then calls `setValue` on the mapped outputs. e.g.

tsx

```
onScroll={Animated.event(  
  [{nativeEvent: {contentOffset: {x: this._scrollX}}}],  
  {listener: (event: ScrollEvent) => console.log(event)}, // Optional async listener  
)}  
 ...  
onPanResponderMove: Animated.event(  
  [  
    null, // raw event arg ignored  
    {dx: this._panX},  
  ], // gestureState arg  
  {  
    listener: (  
      event: GestureResponderEvent,  
      gestureState: PanResponderGestureState  
    ) => console.log(event, gestureState),  
  } // Optional async listener  
);  

```

Config is an object that may have the following options:

* `listener`: Optional async listener.
* `useNativeDriver`: Uses the native driver when true. Required.

---

### `forkEvent()`[​](#forkevent "Direct link to forkevent")

jsx

```
static forkEvent(event: AnimatedEvent, listener: Function): AnimatedEvent;  

```

Advanced imperative API for snooping on animated events that are passed in through props. It permits to add a new javascript listener to an existing `AnimatedEvent`. If `animatedEvent` is a javascript listener, it will merge the 2 listeners into a single one, and if `animatedEvent` is null/undefined, it will assign the javascript listener directly. Use values directly where possible.

---

### `unforkEvent()`[​](#unforkevent "Direct link to unforkevent")

jsx

```
static unforkEvent(event: AnimatedEvent, listener: Function);  

```

---

### `start()`[​](#start "Direct link to start")

tsx

```
static start(callback?: (result: {finished: boolean}) => void);  

```

Animations are started by calling start() on your animation. start() takes a completion callback that will be called when the animation is done or when the animation is done because stop() was called on it before it could finish.

**Parameters:**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  | | --- | --- | --- | --- | | callback `(result: {finished: boolean}) => void` No Function that will be called after the animation finished running normally or when the animation is done because stop() was called on it before it could finish | | | | | | | |

Start example with callback:

tsx

```
Animated.timing({}).start(({finished}) => {  
  /* completion callback */  
});  

```

---

### `stop()`[​](#stop "Direct link to stop")

tsx

```
static stop();  

```

Stops any running animation.

---

### `reset()`[​](#reset "Direct link to reset")

tsx

```
static reset();  

```

Stops any running animation and resets the value to its original.

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### `Value`[​](#value "Direct link to value")

Standard value class for driving animations. Typically initialized with `useAnimatedValue(0);` or `new Animated.Value(0);` in class components.

You can read more about `Animated.Value` API on the separate [page](/docs/animatedvalue).

---

### `ValueXY`[​](#valuexy "Direct link to valuexy")

2D value class for driving 2D animations, such as pan gestures.

You can read more about `Animated.ValueXY` API on the separate [page](/docs/animatedvaluexy).

---

### `Interpolation`[​](#interpolation-1 "Direct link to interpolation-1")

Exported to use the Interpolation type in flow.

---

### `Node`[​](#node "Direct link to node")

Exported for ease of type checking. All animated values derive from this class.

---

### `createAnimatedComponent`[​](#createanimatedcomponent "Direct link to createanimatedcomponent")

Make any React component Animatable. Used to create `Animated.View`, etc.

---

### `attachNativeEvent`[​](#attachnativeevent "Direct link to attachnativeevent")

Imperative API to attach an animated value to an event on a view. Prefer using `Animated.event` with `useNativeDriver: true` if possible.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/animated.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/animated.md)

Last updated on **Apr 14, 2025**

[Previous

Alert](/docs/alert)[Next

Animated.Value](/docs/animatedvalue)

* [Example](#example)* [Overview](#overview)
    + [Configuring animations](#configuring-animations)+ [Working with animations](#working-with-animations)+ [Using the native driver](#using-the-native-driver)+ [Animatable components](#animatable-components)+ [Composing animations](#composing-animations)+ [Combining animated values](#combining-animated-values)+ [Interpolation](#interpolation)+ [Handling gestures and other events](#handling-gestures-and-other-events)* [Methods](#methods)
      + [`decay()`](#decay)+ [`timing()`](#timing)+ [`spring()`](#spring)+ [`add()`](#add)+ [`subtract()`](#subtract)+ [`divide()`](#divide)+ [`multiply()`](#multiply)+ [`modulo()`](#modulo)+ [`diffClamp()`](#diffclamp)+ [`delay()`](#delay)+ [`sequence()`](#sequence)+ [`parallel()`](#parallel)+ [`stagger()`](#stagger)+ [`loop()`](#loop)+ [`event()`](#event)+ [`forkEvent()`](#forkevent)+ [`unforkEvent()`](#unforkevent)+ [`start()`](#start)+ [`stop()`](#stop)+ [`reset()`](#reset)* [Properties](#properties)
        + [`Value`](#value)+ [`ValueXY`](#valuexy)+ [`Interpolation`](#interpolation-1)+ [`Node`](#node)+ [`createAnimatedComponent`](#createanimatedcomponent)+ [`attachNativeEvent`](#attachnativeevent)

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