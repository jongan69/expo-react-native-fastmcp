DrawerLayoutAndroid · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/drawerlayoutandroid)

* [Next](/docs/next/drawerlayoutandroid)* [0.79](/docs/drawerlayoutandroid)* [0.78](/docs/0.78/drawerlayoutandroid)* [0.77](/docs/0.77/drawerlayoutandroid)* [0.76](/docs/0.76/drawerlayoutandroid)* [0.75](/docs/0.75/drawerlayoutandroid)* [0.74](/docs/0.74/drawerlayoutandroid)* [0.73](/docs/0.73/drawerlayoutandroid)* [0.72](/docs/0.72/drawerlayoutandroid)* [0.71](/docs/0.71/drawerlayoutandroid)* [0.70](/docs/0.70/drawerlayoutandroid)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [Core Components](/docs/components-and-apis)

  + [Core Components and APIs](/docs/components-and-apis)+ [ActivityIndicator](/docs/activityindicator)+ [Button](/docs/button)+ [FlatList](/docs/flatlist)+ [Image](/docs/image)+ [ImageBackground](/docs/imagebackground)+ [KeyboardAvoidingView](/docs/keyboardavoidingview)+ [Modal](/docs/modal)+ [Pressable](/docs/pressable)+ [RefreshControl](/docs/refreshcontrol)+ [ScrollView](/docs/scrollview)+ [SectionList](/docs/sectionlist)+ [StatusBar](/docs/statusbar)+ [Switch](/docs/switch)+ [Text](/docs/text)+ [TextInput](/docs/textinput)+ [TouchableHighlight](/docs/touchablehighlight)+ [TouchableOpacity](/docs/touchableopacity)+ [TouchableWithoutFeedback](/docs/touchablewithoutfeedback)+ [View](/docs/view)+ [VirtualizedList](/docs/virtualizedlist)+ [Android Components](/docs/drawerlayoutandroid)

                                              - [DrawerLayoutAndroid](/docs/drawerlayoutandroid)- [TouchableNativeFeedback](/docs/touchablenativefeedback)+ [iOS Components](/docs/inputaccessoryview)

                                                - [InputAccessoryView](/docs/inputaccessoryview)- [SafeAreaView](/docs/safeareaview)* [Props](/docs/image-style-props)

    * [Object Types](/docs/boxshadowvalue)

On this page

DrawerLayoutAndroid
===================

React component that wraps the platform `DrawerLayout` (Android only). The Drawer (typically used for navigation) is rendered with `renderNavigationView` and direct children are the main view (where your content goes). The navigation view is initially not visible on the screen, but can be pulled in from the side of the window specified by the `drawerPosition` prop and its width can be set by the `drawerWidth` prop.

Example[​](#example "Direct link to Example")
---------------------------------------------

* TypeScript* JavaScript

---

Reference
=========

Props[​](#props "Direct link to Props")
---------------------------------------

### [View Props](/docs/view#props)[​](#view-props "Direct link to view-props")

Inherits [View Props](/docs/view#props).

---

### `drawerBackgroundColor`[​](#drawerbackgroundcolor "Direct link to drawerbackgroundcolor")

Specifies the background color of the drawer. The default value is `white`. If you want to set the opacity of the drawer, use rgba. Example:

tsx

```
return (  
  <DrawerLayoutAndroid drawerBackgroundColor="rgba(0,0,0,0.5)" />  
);  

```

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | [color](/docs/colors) No | | | |

---

### `drawerLockMode`[​](#drawerlockmode "Direct link to drawerlockmode")

Specifies the lock mode of the drawer. The drawer can be locked in 3 states:

* unlocked (default), meaning that the drawer will respond (open/close) to touch gestures.
* locked-closed, meaning that the drawer will stay closed and not respond to gestures.
* locked-open, meaning that the drawer will stay opened and not respond to gestures. The drawer may still be opened and closed programmatically (`openDrawer`/`closeDrawer`).

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | enum('unlocked', 'locked-closed', 'locked-open') No | | | |

---

### `drawerPosition`[​](#drawerposition "Direct link to drawerposition")

Specifies the side of the screen from which the drawer will slide in. By default it is set to `left`.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | enum('left', 'right') No | | | |

---

### `drawerWidth`[​](#drawerwidth "Direct link to drawerwidth")

Specifies the width of the drawer, more precisely the width of the view that be pulled in from the edge of the window.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number No | | | |

---

### `keyboardDismissMode`[​](#keyboarddismissmode "Direct link to keyboarddismissmode")

Determines whether the keyboard gets dismissed in response to a drag.

* 'none' (the default), drags do not dismiss the keyboard.
* 'on-drag', the keyboard is dismissed when a drag begins.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | enum('none', 'on-drag') No | | | |

---

### `onDrawerClose`[​](#ondrawerclose "Direct link to ondrawerclose")

Function called whenever the navigation view has been closed.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | function No | | | |

---

### `onDrawerOpen`[​](#ondraweropen "Direct link to ondraweropen")

Function called whenever the navigation view has been opened.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | function No | | | |

---

### `onDrawerSlide`[​](#ondrawerslide "Direct link to ondrawerslide")

Function called whenever there is an interaction with the navigation view.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | function No | | | |

---

### `onDrawerStateChanged`[​](#ondrawerstatechanged "Direct link to ondrawerstatechanged")

Function called when the drawer state has changed. The drawer can be in 3 states:

* idle, meaning there is no interaction with the navigation view happening at the time
* dragging, meaning there is currently an interaction with the navigation view
* settling, meaning that there was an interaction with the navigation view, and the navigation view is now finishing its closing or opening animation

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | function No | | | |

---

### `renderNavigationView`[​](#rendernavigationview "Direct link to rendernavigationview")

The navigation view that will be rendered to the side of the screen and can be pulled in.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | function Yes | | | |

---

### `statusBarBackgroundColor`[​](#statusbarbackgroundcolor "Direct link to statusbarbackgroundcolor")

Make the drawer take the entire screen and draw the background of the status bar to allow it to open over the status bar. It will only have an effect on API 21+.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | [color](/docs/colors) No | | | |

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### `closeDrawer()`[​](#closedrawer "Direct link to closedrawer")

tsx

```
closeDrawer();  

```

Closes the drawer.

---

### `openDrawer()`[​](#opendrawer "Direct link to opendrawer")

tsx

```
openDrawer();  

```

Opens the drawer.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/drawerlayoutandroid.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/drawerlayoutandroid.md)

Last updated on **Apr 14, 2025**

[Previous

VirtualizedList](/docs/virtualizedlist)[Next

TouchableNativeFeedback](/docs/touchablenativefeedback)

* [Example](#example)* [Props](#props)
    + [View Props](#view-props)+ [`drawerBackgroundColor`](#drawerbackgroundcolor)+ [`drawerLockMode`](#drawerlockmode)+ [`drawerPosition`](#drawerposition)+ [`drawerWidth`](#drawerwidth)+ [`keyboardDismissMode`](#keyboarddismissmode)+ [`onDrawerClose`](#ondrawerclose)+ [`onDrawerOpen`](#ondraweropen)+ [`onDrawerSlide`](#ondrawerslide)+ [`onDrawerStateChanged`](#ondrawerstatechanged)+ [`renderNavigationView`](#rendernavigationview)+ [`statusBarBackgroundColor`](#statusbarbackgroundcolor)* [Methods](#methods)
      + [`closeDrawer()`](#closedrawer)+ [`openDrawer()`](#opendrawer)

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