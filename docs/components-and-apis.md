Core Components and APIs · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/components-and-apis)

* [Next](/docs/next/components-and-apis)* [0.79](/docs/components-and-apis)* [0.78](/docs/0.78/components-and-apis)* [0.77](/docs/0.77/components-and-apis)* [0.76](/docs/0.76/components-and-apis)* [0.75](/docs/0.75/components-and-apis)* [0.74](/docs/0.74/components-and-apis)* [0.73](/docs/0.73/components-and-apis)* [0.72](/docs/0.72/components-and-apis)* [0.71](/docs/0.71/components-and-apis)* [0.70](/docs/0.70/components-and-apis)* [All versions](/versions)

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

Core Components and APIs
========================

React Native provides a number of built-in [Core Components](/docs/intro-react-native-components) ready for you to use in your app. You can find them all in the left sidebar (or menu above, if you are on a narrow screen). If you're not sure where to get started, take a look at the following categories:

* [Basic Components](/docs/components-and-apis#basic-components)
* [User Interface](/docs/components-and-apis#user-interface)
* [List Views](/docs/components-and-apis#list-views)
* [Android-specific](/docs/components-and-apis#android-components-and-apis)
* [iOS-specific](/docs/components-and-apis#ios-components-and-apis)
* [Others](/docs/components-and-apis#others)

You're not limited to the components and APIs bundled with React Native. React Native has a community of thousands of developers. If you're looking for a library that does something specific, please refer to [this guide about finding libraries](/docs/libraries#finding-libraries).

Basic Components[​](#basic-components "Direct link to Basic Components")
------------------------------------------------------------------------

Most apps will end up using one or more of these basic components.

[### View

The most fundamental component for building a UI.](./view)

[### Text

A component for displaying text.](./text)

[### Image

A component for displaying images.](./image)

[### TextInput

A component for inputting text into the app via a keyboard.](./textinput)

[### ScrollView

Provides a scrolling container that can host multiple components and views.](./scrollview)

[### StyleSheet

Provides an abstraction layer similar to CSS stylesheets.](./stylesheet)

User Interface[​](#user-interface "Direct link to User Interface")
------------------------------------------------------------------

These common user interface controls will render on any platform.

[### Button

A basic button component for handling touches that should render nicely on any platform.](./button)

[### Switch

Renders a boolean input.](./switch)

List Views[​](#list-views "Direct link to List Views")
------------------------------------------------------

Unlike the more generic [`ScrollView`](/docs/scrollview), the following list view components only render elements that are currently showing on the screen. This makes them a performant choice for displaying long lists of data.

[### FlatList

A component for rendering performant scrollable lists.](./flatlist)

[### SectionList

Like `FlatList`, but for sectioned lists.](./sectionlist)

Android Components and APIs[​](#android-components-and-apis "Direct link to Android Components and APIs")
---------------------------------------------------------------------------------------------------------

Many of the following components provide wrappers for commonly used Android classes.

[### BackHandler

Detect hardware button presses for back navigation.](./backhandler)

[### DrawerLayoutAndroid

Renders a `DrawerLayout` on Android.](./drawerlayoutandroid)

[### PermissionsAndroid

Provides access to the permissions model introduced in Android M.](./permissionsandroid)

[### ToastAndroid

Create an Android Toast alert.](./toastandroid)

iOS Components and APIs[​](#ios-components-and-apis "Direct link to iOS Components and APIs")
---------------------------------------------------------------------------------------------

Many of the following components provide wrappers for commonly used UIKit classes.

[### ActionSheetIOS

API to display an iOS action sheet or share sheet.](./actionsheetios)

Others[​](#others "Direct link to Others")
------------------------------------------

These components may be useful for certain applications. For an exhaustive list of components and APIs, check out the sidebar to the left (or menu above, if you are on a narrow screen).

[### ActivityIndicator

Displays a circular loading indicator.](./activityindicator)

[### Alert

Launches an alert dialog with the specified title and message.](./alert)

[### Animated

A library for creating fluid, powerful animations that are easy to build and maintain.](./animated)

[### Dimensions

Provides an interface for getting device dimensions.](./dimensions)

[### KeyboardAvoidingView

Provides a view that moves out of the way of the virtual keyboard automatically.](./keyboardavoidingview)

[### Linking

Provides a general interface to interact with both incoming and outgoing app links.](./linking)

[### Modal

Provides a simple way to present content above an enclosing view.](./modal)

[### PixelRatio

Provides access to the device pixel density.](./pixelratio)

[### RefreshControl

This component is used inside a `ScrollView` to add pull to refresh functionality.](./refreshcontrol)

[### StatusBar

Component to control the app status bar.](./statusbar)

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/components-and-apis.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/components-and-apis.md)

Last updated on **Apr 14, 2025**

[Next

ActivityIndicator](/docs/activityindicator)

* [Basic Components](#basic-components)* [User Interface](#user-interface)* [List Views](#list-views)* [Android Components and APIs](#android-components-and-apis)* [iOS Components and APIs](#ios-components-and-apis)* [Others](#others)

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