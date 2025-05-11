PanResponder · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/panresponder)

* [Next](/docs/next/panresponder)* [0.79](/docs/panresponder)* [0.78](/docs/0.78/panresponder)* [0.77](/docs/0.77/panresponder)* [0.76](/docs/0.76/panresponder)* [0.75](/docs/0.75/panresponder)* [0.74](/docs/0.74/panresponder)* [0.73](/docs/0.73/panresponder)* [0.72](/docs/0.72/panresponder)* [0.71](/docs/0.71/panresponder)* [0.70](/docs/0.70/panresponder)* [All versions](/versions)

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

PanResponder
============

`PanResponder` reconciles several touches into a single gesture. It makes single-touch gestures resilient to extra touches, and can be used to recognize basic multi-touch gestures.

By default, `PanResponder` holds an `InteractionManager` handle to block long-running JS events from interrupting active gestures.

It provides a predictable wrapper of the responder handlers provided by the [gesture responder system](/docs/gesture-responder-system). For each handler, it provides a new `gestureState` object alongside the native event object:

```
onPanResponderMove: (event, gestureState) => {}  

```

A native event is a synthetic touch event with form of [PressEvent](/docs/pressevent).

A `gestureState` object has the following:

* `stateID` - ID of the gestureState- persisted as long as there's at least one touch on screen
* `moveX` - the latest screen coordinates of the recently-moved touch
* `moveY` - the latest screen coordinates of the recently-moved touch
* `x0` - the screen coordinates of the responder grant
* `y0` - the screen coordinates of the responder grant
* `dx` - accumulated distance of the gesture since the touch started
* `dy` - accumulated distance of the gesture since the touch started
* `vx` - current velocity of the gesture
* `vy` - current velocity of the gesture
* `numberActiveTouches` - Number of touches currently on screen

Usage Pattern[​](#usage-pattern "Direct link to Usage Pattern")
---------------------------------------------------------------

tsx

```
const ExampleComponent = () => {  
  const panResponder = React.useRef(  
    PanResponder.create({  
      // Ask to be the responder:  
      onStartShouldSetPanResponder: (evt, gestureState) => true,  
      onStartShouldSetPanResponderCapture: (evt, gestureState) =>  
        true,  
      onMoveShouldSetPanResponder: (evt, gestureState) => true,  
      onMoveShouldSetPanResponderCapture: (evt, gestureState) =>  
        true,  
  
      onPanResponderGrant: (evt, gestureState) => {  
        // The gesture has started. Show visual feedback so the user knows  
        // what is happening!  
        // gestureState.d{x,y} will be set to zero now  
      },  
      onPanResponderMove: (evt, gestureState) => {  
        // The most recent move distance is gestureState.move{X,Y}  
        // The accumulated gesture distance since becoming responder is  
        // gestureState.d{x,y}  
      },  
      onPanResponderTerminationRequest: (evt, gestureState) =>  
        true,  
      onPanResponderRelease: (evt, gestureState) => {  
        // The user has released all touches while this view is the  
        // responder. This typically means a gesture has succeeded  
      },  
      onPanResponderTerminate: (evt, gestureState) => {  
        // Another component has become the responder, so this gesture  
        // should be cancelled  
      },  
      onShouldBlockNativeResponder: (evt, gestureState) => {  
        // Returns whether this component should block native components from becoming the JS  
        // responder. Returns true by default. Is currently only supported on android.  
        return true;  
      },  
    }),  
  ).current;  
  
  return <View {...panResponder.panHandlers} />;  
};  

```

Example[​](#example "Direct link to Example")
---------------------------------------------

`PanResponder` works with `Animated` API to help build complex gestures in the UI. The following example contains an animated `View` component which can be dragged freely across the screen

Try the [PanResponder example in RNTester](https://github.com/facebook/react-native/blob/main/packages/rn-tester/js/examples/PanResponder/PanResponderExample.js).

---

Reference
=========

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### `create()`[​](#create "Direct link to create")

tsx

```
static create(config: PanResponderCallbacks): PanResponderInstance;  

```

**Parameters:**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Name Type Description|  |  |  | | --- | --- | --- | | config Required  object Refer below | | | | | |

The `config` object provides enhanced versions of all of the responder callbacks that provide not only the [`PressEvent`](/docs/pressevent), but also the `PanResponder` gesture state, by replacing the word `Responder` with `PanResponder` in each of the typical `onResponder*` callbacks. For example, the `config` object would look like:

* `onMoveShouldSetPanResponder: (e, gestureState) => {...}`
* `onMoveShouldSetPanResponderCapture: (e, gestureState) => {...}`
* `onStartShouldSetPanResponder: (e, gestureState) => {...}`
* `onStartShouldSetPanResponderCapture: (e, gestureState) => {...}`
* `onPanResponderReject: (e, gestureState) => {...}`
* `onPanResponderGrant: (e, gestureState) => {...}`
* `onPanResponderStart: (e, gestureState) => {...}`
* `onPanResponderEnd: (e, gestureState) => {...}`
* `onPanResponderRelease: (e, gestureState) => {...}`
* `onPanResponderMove: (e, gestureState) => {...}`
* `onPanResponderTerminate: (e, gestureState) => {...}`
* `onPanResponderTerminationRequest: (e, gestureState) => {...}`
* `onShouldBlockNativeResponder: (e, gestureState) => {...}`

In general, for events that have capture equivalents, we update the gestureState once in the capture phase and can use it in the bubble phase as well.

Be careful with `onStartShould*` callbacks. They only reflect updated `gestureState` for start/end events that bubble/capture to the Node. Once the node is the responder, you can rely on every start/end event being processed by the gesture and `gestureState` being updated accordingly. (numberActiveTouches) may not be totally accurate unless you are the responder.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/panresponder.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/panresponder.md)

Last updated on **Apr 14, 2025**

[Previous

Linking](/docs/linking)[Next

PixelRatio](/docs/pixelratio)

* [Usage Pattern](#usage-pattern)* [Example](#example)* [Methods](#methods)
      + [`create()`](#create)

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