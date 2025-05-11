DevSettings · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/devsettings)

* [Next](/docs/next/devsettings)* [0.79](/docs/devsettings)* [0.78](/docs/0.78/devsettings)* [0.77](/docs/0.77/devsettings)* [0.76](/docs/0.76/devsettings)* [0.75](/docs/0.75/devsettings)* [0.74](/docs/0.74/devsettings)* [0.73](/docs/0.73/devsettings)* [0.72](/docs/0.72/devsettings)* [0.71](/docs/0.71/devsettings)* [0.70](/docs/0.70/devsettings)* [All versions](/versions)

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

DevSettings
===========

The `DevSettings` module exposes methods for customizing settings for developers in development.

---

Reference
=========

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### `addMenuItem()`[​](#addmenuitem "Direct link to addmenuitem")

tsx

```
static addMenuItem(title: string, handler: () => any);  

```

Add a custom menu item to the Dev Menu.

**Parameters:**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Name Type|  |  |  |  | | --- | --- | --- | --- | | title Required  string|  |  | | --- | --- | | handler Required  function | | | | | |

**Example:**

tsx

```
DevSettings.addMenuItem('Show Secret Dev Screen', () => {  
  Alert.alert('Showing secret dev screen!');  
});  

```

---

### `reload()`[​](#reload "Direct link to reload")

tsx

```
static reload(reason?: string): void;  

```

Reload the application. Can be invoked directly or on user interaction.

**Example:**

tsx

```
<Button title="Reload" onPress={() => DevSettings.reload()} />  

```

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/devsettings.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/devsettings.md)

Last updated on **Apr 14, 2025**

[Previous

AppState](/docs/appstate)[Next

Dimensions](/docs/dimensions)

* [Methods](#methods)
  + [`addMenuItem()`](#addmenuitem)+ [`reload()`](#reload)

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