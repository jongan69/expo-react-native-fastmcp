RootTag · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/roottag)

* [Next](/docs/next/roottag)* [0.79](/docs/roottag)* [0.78](/docs/0.78/roottag)* [0.77](/docs/0.77/roottag)* [0.76](/docs/0.76/roottag)* [0.75](/docs/0.75/roottag)* [0.74](/docs/0.74/roottag)* [0.73](/docs/0.73/roottag)* [0.72](/docs/0.72/roottag)* [0.71](/docs/0.71/roottag)* [0.70](/docs/0.70/roottag)* [All versions](/versions)

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

RootTag
=======

`RootTag` is an opaque identifier assigned to the native root view of your React Native surface — i.e. the `ReactRootView` or `RCTRootView` instance for Android or iOS respectively. In short, it is a surface identifier.

When to use a RootTag?[​](#when-to-use-a-roottag "Direct link to When to use a RootTag?")
-----------------------------------------------------------------------------------------

For most React Native developers, you likely won’t need to deal with `RootTag`s.

`RootTag`s are useful for when an app renders **multiple React Native root views** and you need to handle native API calls differently depending on the surface. An example of this is when an app is using native navigation and each screen is a separate React Native root view.

In native navigation, every React Native root view is rendered in a platform’s navigation view (e.g., `Activity` for Android, `UINavigationViewController` for iOS). By this, you are able to leverage the navigation paradigms of the platform such as native look and feel and navigation transitions. The functionality to interact with the native navigation APIs can be exposed to React Native via a [native module](https://reactnative.dev/docs/next/native-modules-intro).

For example, to update the title bar of a screen, you would call the navigation module’s API `setTitle("Updated Title")`, but it would need to know which screen in the stack to update. A `RootTag` is necessary here to identify the root view and its hosting container.

Another use case for `RootTag` is when your app needs to attribute a certain JavaScript call to native based on its originating root view. A `RootTag` is necessary to differentiate the source of the call from different surfaces.

How to access the RootTag... if you need it[​](#how-to-access-the-roottag-if-you-need-it "Direct link to How to access the RootTag... if you need it")
------------------------------------------------------------------------------------------------------------------------------------------------------

In versions 0.65 and below, RootTag is accessed via a [legacy context](https://github.com/facebook/react-native/blob/v0.64.1/Libraries/ReactNative/AppContainer.js#L56). To prepare React Native for Concurrent features coming in React 18 and beyond, we are migrating to the latest [Context API](https://reactjs.org/docs/context.html#api) via `RootTagContext` in 0.66. Version 0.65 supports both the legacy context and the recommended `RootTagContext` to allow developers time to migrate their call-sites. See the breaking changes summary.

How to access `RootTag` via the `RootTagContext`.

js

```
import {RootTagContext} from 'react-native';  
import NativeAnalytics from 'native-analytics';  
import NativeNavigation from 'native-navigation';  
  
function ScreenA() {  
  const rootTag = useContext(RootTagContext);  
  
  const updateTitle = title => {  
    NativeNavigation.setTitle(rootTag, title);  
  };  
  
  const handleOneEvent = () => {  
    NativeAnalytics.logEvent(rootTag, 'one_event');  
  };  
  
  // ...  
}  
  
class ScreenB extends React.Component {  
  static contextType: typeof RootTagContext = RootTagContext;  
  
  updateTitle(title) {  
    NativeNavigation.setTitle(this.context, title);  
  }  
  
  handleOneEvent() {  
    NativeAnalytics.logEvent(this.context, 'one_event');  
  }  
  
  // ...  
}  

```

Learn more about the Context API for [classes](https://reactjs.org/docs/context.html#classcontexttype) and [hooks](https://reactjs.org/docs/hooks-reference.html#usecontext) from the React docs.

### Breaking Change in 0.65[​](#breaking-change-in-065 "Direct link to Breaking Change in 0.65")

`RootTagContext` was formerly named `unstable_RootTagContext` and changed to `RootTagContext` in 0.65. Please update any usages of `unstable_RootTagContext` in your codebase.

### Breaking Change in 0.66[​](#breaking-change-in-066 "Direct link to Breaking Change in 0.66")

The legacy context access to `RootTag` will be removed and replaced by `RootTagContext`. Beginning in 0.65, we encourage developers to proactively migrate `RootTag` accesses to `RootTagContext`.

Future Plans[​](#future-plans "Direct link to Future Plans")
------------------------------------------------------------

With the new React Native architecture progressing, there will be future iterations to `RootTag`, with the intention to keep the `RootTag` type opaque and prevent thrash in React Native codebases. Please do not rely on the fact that RootTag currently aliases to a number! If your app relies on RootTags, keep an eye on our version change logs, which you can find [here](https://github.com/facebook/react-native/blob/main/CHANGELOG.md).

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/roottag.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/roottag.md)

Last updated on **Apr 14, 2025**

[Previous

PlatformColor](/docs/platformcolor)[Next

Share](/docs/share)

* [When to use a RootTag?](#when-to-use-a-roottag)* [How to access the RootTag... if you need it](#how-to-access-the-roottag-if-you-need-it)
    + [Breaking Change in 0.65](#breaking-change-in-065)+ [Breaking Change in 0.66](#breaking-change-in-066)* [Future Plans](#future-plans)

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