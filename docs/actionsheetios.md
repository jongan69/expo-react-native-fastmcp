ActionSheetIOS · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/actionsheetios)

* [Next](/docs/next/actionsheetios)* [0.79](/docs/actionsheetios)* [0.78](/docs/0.78/actionsheetios)* [0.77](/docs/0.77/actionsheetios)* [0.76](/docs/0.76/actionsheetios)* [0.75](/docs/0.75/actionsheetios)* [0.74](/docs/0.74/actionsheetios)* [0.73](/docs/0.73/actionsheetios)* [0.72](/docs/0.72/actionsheetios)* [0.71](/docs/0.71/actionsheetios)* [0.70](/docs/0.70/actionsheetios)* [All versions](/versions)

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

ActionSheetIOS
==============

Displays native to iOS [Action Sheet](https://developer.apple.com/design/human-interface-guidelines/ios/views/action-sheets/) component.

Example[​](#example "Direct link to Example")
---------------------------------------------

Reference
=========

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### `showActionSheetWithOptions()`[​](#showactionsheetwithoptions "Direct link to showactionsheetwithoptions")

tsx

```
static showActionSheetWithOptions: (  
  options: ActionSheetIOSOptions,  
  callback: (buttonIndex: number) => void,  
);  

```

Display an iOS action sheet. The `options` object must contain one or more of:

* `options` (array of strings) - a list of button titles (required)
* `cancelButtonIndex` (int) - index of cancel button in `options`
* `cancelButtonTintColor` (string) - the [color](/docs/colors) used for the change the text color of the cancel button
* `destructiveButtonIndex` (int or array of ints) - indices of destructive buttons in `options`
* `title` (string) - a title to show above the action sheet
* `message` (string) - a message to show below the title
* `anchor` (number) - the node to which the action sheet should be anchored (used for iPad)
* `tintColor` (string) - the [color](/docs/colors) used for non-destructive button titles
* `disabledButtonIndices` (array of numbers) - a list of button indices which should be disabled
* `userInterfaceStyle` (string) - the interface style used for the action sheet, can be set to `light` or `dark`, otherwise the default system style will be used

The 'callback' function takes one parameter, the zero-based index of the selected item.

Minimal example:

tsx

```
ActionSheetIOS.showActionSheetWithOptions(  
  {  
    options: ['Cancel', 'Remove'],  
    destructiveButtonIndex: 1,  
    cancelButtonIndex: 0,  
  },  
  buttonIndex => {  
    if (buttonIndex === 1) {  
      /* destructive action */  
    }  
  },  
);  

```

---

### `dismissActionSheet()`[​](#dismissactionsheet "Direct link to dismissactionsheet")

tsx

```
static dismissActionSheet();  

```

Dismisses the most upper iOS action sheet presented, if no action sheet is present a warning is displayed.

---

### `showShareActionSheetWithOptions()`[​](#showshareactionsheetwithoptions "Direct link to showshareactionsheetwithoptions")

tsx

```
static showShareActionSheetWithOptions: (  
  options: ShareActionSheetIOSOptions,  
  failureCallback: (error: Error) => void,  
  successCallback: (success: boolean, method: string) => void,  
);  

```

Display the iOS share sheet. The `options` object should contain one or both of `message` and `url` and can additionally have a `subject` or `excludedActivityTypes`:

* `url` (string) - a URL to share
* `message` (string) - a message to share
* `subject` (string) - a subject for the message
* `excludedActivityTypes` (array) - the activities to exclude from the ActionSheet

> **Note:** If `url` points to a local file, or is a base64-encoded uri, the file it points to will be loaded and shared directly. In this way, you can share images, videos, PDF files, etc. If `url` points to a remote file or address it must conform to URL format as described in [RFC 2396](https://www.ietf.org/rfc/rfc2396.txt). For example, a web URL without a proper protocol (HTTP/HTTPS) will not be shared.

The 'failureCallback' function takes one parameter, an error object. The only property defined on this object is an optional `stack` property of type `string`.

The 'successCallback' function takes two parameters:

* a boolean value signifying success or failure
* a string that, in the case of success, indicates the method of sharing

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/actionsheetios.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/actionsheetios.md)

Last updated on **Apr 14, 2025**

[Previous

ToastAndroid](/docs/toastandroid)[Next

DynamicColorIOS](/docs/dynamiccolorios)

* [Example](#example)* [Methods](#methods)
    + [`showActionSheetWithOptions()`](#showactionsheetwithoptions)+ [`dismissActionSheet()`](#dismissactionsheet)+ [`showShareActionSheetWithOptions()`](#showshareactionsheetwithoptions)

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