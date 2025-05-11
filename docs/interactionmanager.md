InteractionManager · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/interactionmanager)

* [Next](/docs/next/interactionmanager)* [0.79](/docs/interactionmanager)* [0.78](/docs/0.78/interactionmanager)* [0.77](/docs/0.77/interactionmanager)* [0.76](/docs/0.76/interactionmanager)* [0.75](/docs/0.75/interactionmanager)* [0.74](/docs/0.74/interactionmanager)* [0.73](/docs/0.73/interactionmanager)* [0.72](/docs/0.72/interactionmanager)* [0.71](/docs/0.71/interactionmanager)* [0.70](/docs/0.70/interactionmanager)* [All versions](/versions)

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

InteractionManager
==================

InteractionManager allows long-running work to be scheduled after any interactions/animations have completed. In particular, this allows JavaScript animations to run smoothly.

Applications can schedule tasks to run after interactions with the following:

tsx

```
InteractionManager.runAfterInteractions(() => {  
  // ...long-running synchronous task...  
});  

```

Compare this to other scheduling alternatives:

* `requestAnimationFrame()` for code that animates a view over time.
* `setImmediate/setTimeout()` run code later, note this may delay animations.
* `runAfterInteractions()` run code later, without delaying active animations.

The touch handling system considers one or more active touches to be an 'interaction' and will delay `runAfterInteractions()` callbacks until all touches have ended or been cancelled.

InteractionManager also allows applications to register animations by creating an interaction 'handle' on animation start, and clearing it upon completion:

tsx

```
const handle = InteractionManager.createInteractionHandle();  
// run animation... (`runAfterInteractions` tasks are queued)  
// later, on animation completion:  
InteractionManager.clearInteractionHandle(handle);  
// queued tasks run if all handles were cleared  

```

`runAfterInteractions` takes either a plain callback function, or a `PromiseTask` object with a `gen` method that returns a `Promise`. If a `PromiseTask` is supplied, then it is fully resolved (including asynchronous dependencies that also schedule more tasks via `runAfterInteractions`) before starting on the next task that might have been queued up synchronously earlier.

By default, queued tasks are executed together in a loop in one `setImmediate` batch. If `setDeadline` is called with a positive number, then tasks will only be executed until the deadline (in terms of js event loop run time) approaches, at which point execution will yield via setTimeout, allowing events such as touches to start interactions and block queued tasks from executing, making apps more responsive.

---

Example[​](#example "Direct link to Example")
---------------------------------------------

### Basic[​](#basic "Direct link to Basic")

* TypeScript* JavaScript

### Advanced[​](#advanced "Direct link to Advanced")

* TypeScript* JavaScript

Reference
=========

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### `runAfterInteractions()`[​](#runafterinteractions "Direct link to runafterinteractions")

tsx

```
static runAfterInteractions(task?: (() => any) | SimpleTask | PromiseTask);  

```

Schedule a function to run after all interactions have completed. Returns a cancellable "promise".

---

### `createInteractionHandle()`[​](#createinteractionhandle "Direct link to createinteractionhandle")

tsx

```
static createInteractionHandle(): Handle;  

```

Notify manager that an interaction has started.

---

### `clearInteractionHandle()`[​](#clearinteractionhandle "Direct link to clearinteractionhandle")

tsx

```
static clearInteractionHandle(handle: Handle);  

```

Notify manager that an interaction has completed.

---

### `setDeadline()`[​](#setdeadline "Direct link to setdeadline")

tsx

```
static setDeadline(deadline: number);  

```

A positive number will use setTimeout to schedule any tasks after the eventLoopRunningTime hits the deadline value, otherwise all tasks will be executed in one setImmediate batch (default).

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/interactionmanager.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/interactionmanager.md)

Last updated on **Apr 14, 2025**

[Previous

Easing](/docs/easing)[Next

Keyboard](/docs/keyboard)

* [Example](#example)
  + [Basic](#basic)+ [Advanced](#advanced)* [Methods](#methods)
    + [`runAfterInteractions()`](#runafterinteractions)+ [`createInteractionHandle()`](#createinteractionhandle)+ [`clearInteractionHandle()`](#clearinteractionhandle)+ [`setDeadline()`](#setdeadline)

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