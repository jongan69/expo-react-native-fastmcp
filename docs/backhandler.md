BackHandler · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/backhandler)

* [Next](/docs/next/backhandler)* [0.79](/docs/backhandler)* [0.78](/docs/0.78/backhandler)* [0.77](/docs/0.77/backhandler)* [0.76](/docs/0.76/backhandler)* [0.75](/docs/0.75/backhandler)* [0.74](/docs/0.74/backhandler)* [0.73](/docs/0.73/backhandler)* [0.72](/docs/0.72/backhandler)* [0.71](/docs/0.71/backhandler)* [0.70](/docs/0.70/backhandler)* [All versions](/versions)

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

BackHandler
===========

The Backhandler API detects hardware button presses for back navigation, lets you register event listeners for the system's back action, and lets you control how your application responds. It is Android-only.

The event subscriptions are called in reverse order (i.e. the last registered subscription is called first).

* **If one subscription returns true,** then subscriptions registered earlier will not be called.
* **If no subscription returns true or none are registered,** it programmatically invokes the default back button functionality to exit the app.

> **Warning for modal users:** If your app shows an opened `Modal`, `BackHandler` will not publish any events ([see `Modal` docs](/docs/modal#onrequestclose)).

Pattern[​](#pattern "Direct link to Pattern")
---------------------------------------------

tsx

```
const subscription = BackHandler.addEventListener(  
  'hardwareBackPress',  
  function () {  
    /**  
     * this.onMainScreen and this.goBack are just examples,  
     * you need to use your own implementation here.  
     *  
     * Typically you would use the navigator here to go to the last state.  
     */  
  
    if (!this.onMainScreen()) {  
      this.goBack();  
      /**  
       * When true is returned the event will not be bubbled up  
       * & no other back action will execute  
       */  
      return true;  
    }  
    /**  
     * Returning false will let the event to bubble up & let other event listeners  
     * or the system's default back action to be executed.  
     */  
    return false;  
  },  
);  
  
// Unsubscribe the listener on unmount  
subscription.remove();  

```

Example[​](#example "Direct link to Example")
---------------------------------------------

The following example implements a scenario where you confirm if the user wants to exit the app:

`BackHandler.addEventListener` creates an event listener & returns a `NativeEventSubscription` object which should be cleared using `NativeEventSubscription.remove` method.

Usage with React Navigation[​](#usage-with-react-navigation "Direct link to Usage with React Navigation")
---------------------------------------------------------------------------------------------------------

If you are using React Navigation to navigate across different screens, you can follow their guide on [Custom Android back button behaviour](https://reactnavigation.org/docs/custom-android-back-button-handling/)

Backhandler hook[​](#backhandler-hook "Direct link to Backhandler hook")
------------------------------------------------------------------------

[React Native Hooks](https://github.com/react-native-community/hooks#usebackhandler) has a nice `useBackHandler` hook which will simplify the process of setting up event listeners.

---

Reference
=========

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### `addEventListener()`[​](#addeventlistener "Direct link to addeventlistener")

tsx

```
static addEventListener(  
  eventName: BackPressEventName,  
  handler: () => boolean | null | undefined,  
): NativeEventSubscription;  

```

---

### `exitApp()`[​](#exitapp "Direct link to exitapp")

tsx

```
static exitApp();  

```

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/backhandler.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/backhandler.md)

Last updated on **Apr 14, 2025**

[Previous

useWindowDimensions](/docs/usewindowdimensions)[Next

PermissionsAndroid](/docs/permissionsandroid)

* [Pattern](#pattern)* [Example](#example)* [Usage with React Navigation](#usage-with-react-navigation)* [Backhandler hook](#backhandler-hook)* [Methods](#methods)
          + [`addEventListener()`](#addeventlistener)+ [`exitApp()`](#exitapp)

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