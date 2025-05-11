Share · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/share)

* [Next](/docs/next/share)* [0.79](/docs/share)* [0.78](/docs/0.78/share)* [0.77](/docs/0.77/share)* [0.76](/docs/0.76/share)* [0.75](/docs/0.75/share)* [0.74](/docs/0.74/share)* [0.73](/docs/0.73/share)* [0.72](/docs/0.72/share)* [0.71](/docs/0.71/share)* [0.70](/docs/0.70/share)* [All versions](/versions)

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

Share
=====

Example[​](#example "Direct link to Example")
---------------------------------------------

* TypeScript* JavaScript

Reference
=========

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### `share()`[​](#share "Direct link to share")

tsx

```
static share(content: ShareContent, options?: ShareOptions);  

```

Open a dialog to share text content.

In iOS, returns a Promise which will be invoked with an object containing `action` and `activityType`. If the user dismissed the dialog, the Promise will still be resolved with action being `Share.dismissedAction` and all the other keys being undefined. Note that some share options will not appear or work on the iOS simulator.

In Android, returns a Promise which will always be resolved with action being `Share.sharedAction`.

**Properties:**

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Description|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | content Required  object `message` - a message to share `url` - a URL to share iOS  `title` - title of the message Android   ---  At least one of `url` and `message` is required.| options object `dialogTitle` Android  `excludedActivityTypes` iOS  `subject` - a subject to share via email iOS  `tintColor` iOS  `anchor` - the node to which the action sheet should be anchored (used for iPad) iOS | | | | | | | | |

---

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### `sharedAction`[​](#sharedaction "Direct link to sharedaction")

tsx

```
static sharedAction: 'sharedAction';  

```

The content was successfully shared.

---

### `dismissedAction` iOS [​](#dismissedaction-ios "Direct link to dismissedaction-ios")

tsx

```
static dismissedAction: 'dismissedAction';  

```

The dialog has been dismissed.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/share.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/share.md)

Last updated on **Apr 14, 2025**

[Previous

RootTag](/docs/roottag)[Next

StyleSheet](/docs/stylesheet)

* [Example](#example)* [Methods](#methods)
    + [`share()`](#share)* [Properties](#properties)
      + [`sharedAction`](#sharedaction)+ [`dismissedAction`

          iOS](#dismissedaction-ios)

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