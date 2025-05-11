AppState · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/appstate)

* [Next](/docs/next/appstate)* [0.79](/docs/appstate)* [0.78](/docs/0.78/appstate)* [0.77](/docs/0.77/appstate)* [0.76](/docs/0.76/appstate)* [0.75](/docs/0.75/appstate)* [0.74](/docs/0.74/appstate)* [0.73](/docs/0.73/appstate)* [0.72](/docs/0.72/appstate)* [0.71](/docs/0.71/appstate)* [0.70](/docs/0.70/appstate)* [All versions](/versions)

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

AppState
========

`AppState` can tell you if the app is in the foreground or background, and notify you when the state changes.

AppState is frequently used to determine the intent and proper behavior when handling push notifications.

### App States[​](#app-states "Direct link to App States")

* `active` - The app is running in the foreground
* `background` - The app is running in the background. The user is either:
  + in another app
  + on the home screen
  + [Android] on another `Activity` (even if it was launched by your app)
* [iOS] `inactive` - This is a state that occurs when transitioning between foreground & background, and during periods of inactivity such as entering the multitasking view, opening the Notification Center or in the event of an incoming call.

For more information, see [Apple's documentation](https://developer.apple.com/documentation/uikit/app_and_scenes/managing_your_app_s_life_cycle)

Basic Usage[​](#basic-usage "Direct link to Basic Usage")
---------------------------------------------------------

To see the current state, you can check `AppState.currentState`, which will be kept up-to-date. However, `currentState` will be null at launch while `AppState` retrieves it over the bridge.

This example will only ever appear to say "Current state is: active" because the app is only visible to the user when in the `active` state, and the null state will happen only momentarily. If you want to experiment with the code we recommend to use your own device instead of embedded preview.

---

Reference
=========

Events[​](#events "Direct link to Events")
------------------------------------------

### `change`[​](#change "Direct link to change")

This event is received when the app state has changed. The listener is called with one of [the current app state values](/docs/appstate#app-states).

### `memoryWarning`[​](#memorywarning "Direct link to memorywarning")

This event is used in the need of throwing memory warning or releasing it.

### `focus` Android [​](#focus-android "Direct link to focus-android")

Received when the app gains focus (the user is interacting with the app).

### `blur` Android [​](#blur-android "Direct link to blur-android")

Received when the user is not actively interacting with the app. Useful in situations when the user pulls down the [notification drawer](https://developer.android.com/guide/topics/ui/notifiers/notifications#bar-and-drawer). `AppState` won't change but the `blur` event will get fired.

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### `addEventListener()`[​](#addeventlistener "Direct link to addeventlistener")

tsx

```
static addEventListener(  
  type: AppStateEvent,  
  listener: (state: AppStateStatus) => void,  
): NativeEventSubscription;  

```

Sets up a function that will be called whenever the specified event type on AppState occurs. Valid values for `eventType` are
[listed above](#events). Returns the `EventSubscription`.

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### `currentState`[​](#currentstate "Direct link to currentstate")

tsx

```
static currentState: AppStateStatus;  

```

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/appstate.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/appstate.md)

Last updated on **Apr 14, 2025**

[Previous

AppRegistry](/docs/appregistry)[Next

DevSettings](/docs/devsettings)

* [App States](#app-states)* [Basic Usage](#basic-usage)* [Events](#events)
      + [`change`](#change)+ [`memoryWarning`](#memorywarning)+ [`focus`

            Android](#focus-android)+ [`blur`

              Android](#blur-android)* [Methods](#methods)
        + [`addEventListener()`](#addeventlistener)* [Properties](#properties)
          + [`currentState`](#currentstate)

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