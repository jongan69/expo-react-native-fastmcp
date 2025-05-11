TouchableHighlight · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/touchablehighlight)

* [Next](/docs/next/touchablehighlight)* [0.79](/docs/touchablehighlight)* [0.78](/docs/0.78/touchablehighlight)* [0.77](/docs/0.77/touchablehighlight)* [0.76](/docs/0.76/touchablehighlight)* [0.75](/docs/0.75/touchablehighlight)* [0.74](/docs/0.74/touchablehighlight)* [0.73](/docs/0.73/touchablehighlight)* [0.72](/docs/0.72/touchablehighlight)* [0.71](/docs/0.71/touchablehighlight)* [0.70](/docs/0.70/touchablehighlight)* [All versions](/versions)

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

TouchableHighlight
==================

> If you're looking for a more extensive and future-proof way to handle touch-based input, check out the [Pressable](/docs/pressable) API.

A wrapper for making views respond properly to touches. On press down, the opacity of the wrapped view is decreased, which allows the underlay color to show through, darkening or tinting the view.

The underlay comes from wrapping the child in a new View, which can affect layout, and sometimes cause unwanted visual artifacts if not used correctly, for example if the backgroundColor of the wrapped view isn't explicitly set to an opaque color.

TouchableHighlight must have one child (not zero or more than one). If you wish to have several child components, wrap them in a View.

tsx

```
function MyComponent(props: MyComponentProps) {  
  return (  
    <View {...props} style={{flex: 1, backgroundColor: '#fff'}}>  
      <Text>My Component</Text>  
    </View>  
  );  
}  
  
<TouchableHighlight  
  activeOpacity={0.6}  
  underlayColor="#DDDDDD"  
  onPress={() => alert('Pressed!')}>  
  <MyComponent />  
</TouchableHighlight>;  

```

Example[​](#example "Direct link to Example")
---------------------------------------------

---

Reference
=========

Props[​](#props "Direct link to Props")
---------------------------------------

### [TouchableWithoutFeedback Props](/docs/touchablewithoutfeedback#props)[​](#touchablewithoutfeedback-props "Direct link to touchablewithoutfeedback-props")

Inherits [TouchableWithoutFeedback Props](/docs/touchablewithoutfeedback#props).

---

### `activeOpacity`[​](#activeopacity "Direct link to activeopacity")

Determines what the opacity of the wrapped view should be when touch is active. The value should be between 0 and 1. Defaults to 0.85. Requires `underlayColor` to be set.

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

---

### `onHideUnderlay`[​](#onhideunderlay "Direct link to onhideunderlay")

Called immediately after the underlay is hidden.

|  |  |
| --- | --- |
| Type|  | | --- | | function | |

---

### `onShowUnderlay`[​](#onshowunderlay "Direct link to onshowunderlay")

Called immediately after the underlay is shown.

|  |  |
| --- | --- |
| Type|  | | --- | | function | |

---

### `style`[​](#style "Direct link to style")

|  |  |
| --- | --- |
| Type|  | | --- | | View.style | |

---

### `underlayColor`[​](#underlaycolor "Direct link to underlaycolor")

The color of the underlay that will show through when the touch is active.

|  |  |
| --- | --- |
| Type|  | | --- | | [color](/docs/colors) | |

---

### `hasTVPreferredFocus` iOS [​](#hastvpreferredfocus-ios "Direct link to hastvpreferredfocus-ios")

*(Apple TV only)* TV preferred focus (see documentation for the View component).

|  |  |
| --- | --- |
| Type|  | | --- | | bool | |

---

### `nextFocusDown` Android [​](#nextfocusdown-android "Direct link to nextfocusdown-android")

TV next focus down (see documentation for the View component).

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

---

### `nextFocusForward` Android [​](#nextfocusforward-android "Direct link to nextfocusforward-android")

TV next focus forward (see documentation for the View component).

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

---

### `nextFocusLeft` Android [​](#nextfocusleft-android "Direct link to nextfocusleft-android")

TV next focus left (see documentation for the View component).

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

---

### `nextFocusRight` Android [​](#nextfocusright-android "Direct link to nextfocusright-android")

TV next focus right (see documentation for the View component).

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

---

### `nextFocusUp` Android [​](#nextfocusup-android "Direct link to nextfocusup-android")

TV next focus up (see documentation for the View component).

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

---

### `testOnly_pressed`[​](#testonly_pressed "Direct link to testonly_pressed")

Handy for snapshot tests.

|  |  |
| --- | --- |
| Type|  | | --- | | bool | |

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/touchablehighlight.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/touchablehighlight.md)

Last updated on **Apr 14, 2025**

[Previous

TextInput](/docs/textinput)[Next

TouchableOpacity](/docs/touchableopacity)

* [Example](#example)* [Props](#props)
    + [TouchableWithoutFeedback Props](#touchablewithoutfeedback-props)+ [`activeOpacity`](#activeopacity)+ [`onHideUnderlay`](#onhideunderlay)+ [`onShowUnderlay`](#onshowunderlay)+ [`style`](#style)+ [`underlayColor`](#underlaycolor)+ [`hasTVPreferredFocus`

                  iOS](#hastvpreferredfocus-ios)+ [`nextFocusDown`

                    Android](#nextfocusdown-android)+ [`nextFocusForward`

                      Android](#nextfocusforward-android)+ [`nextFocusLeft`

                        Android](#nextfocusleft-android)+ [`nextFocusRight`

                          Android](#nextfocusright-android)+ [`nextFocusUp`

                            Android](#nextfocusup-android)+ [`testOnly_pressed`](#testonly_pressed)

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