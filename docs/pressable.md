Pressable · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/pressable)

* [Next](/docs/next/pressable)* [0.79](/docs/pressable)* [0.78](/docs/0.78/pressable)* [0.77](/docs/0.77/pressable)* [0.76](/docs/0.76/pressable)* [0.75](/docs/0.75/pressable)* [0.74](/docs/0.74/pressable)* [0.73](/docs/0.73/pressable)* [0.72](/docs/0.72/pressable)* [0.71](/docs/0.71/pressable)* [0.70](/docs/0.70/pressable)* [All versions](/versions)

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

Pressable
=========

Pressable is a Core Component wrapper that can detect various stages of press interactions on any of its defined children.

tsx

```
<Pressable onPress={onPressFunction}>  
  <Text>I'm pressable!</Text>  
</Pressable>  

```

How it works[​](#how-it-works "Direct link to How it works")
------------------------------------------------------------

On an element wrapped by `Pressable`:

* [`onPressIn`](#onpressin) is called when a press is activated.
* [`onPressOut`](#onpressout) is called when the press gesture is deactivated.

After pressing [`onPressIn`](#onpressin), one of two things will happen:

1. The person will remove their finger, triggering [`onPressOut`](#onpressout) followed by [`onPress`](#onpress).
2. If the person leaves their finger longer than 500 milliseconds before removing it, [`onLongPress`](#onlongpress) is triggered. ([`onPressOut`](#onpressout) will still fire when they remove their finger.)

![Diagram of the onPress events in sequence.](/docs/assets/d_pressable_pressing.svg)

Fingers are not the most precise instruments, and it is common for users to accidentally activate the wrong element or miss the activation area. To help, `Pressable` has an optional `HitRect` you can use to define how far a touch can register away from the wrapped element. Presses can start anywhere within a `HitRect`.

`PressRect` allows presses to move beyond the element and its `HitRect` while maintaining activation and being eligible for a "press"—think of sliding your finger slowly away from a button you're pressing down on.

> The touch area never extends past the parent view bounds and the Z-index of sibling views always takes precedence if a touch hits two overlapping views.

![Diagram of HitRect and PressRect and how they work.](/docs/assets/d_pressable_anatomy.svg)

You can set `HitRect` with `hitSlop` and set `PressRect` with `pressRetentionOffset`.

> `Pressable` uses React Native's `Pressability` API. For more information around the state machine flow of Pressability and how it works, check out the implementation for [Pressability](https://github.com/facebook/react-native/blob/main/packages/react-native/Libraries/Pressability/Pressability.js#L350).

Example[​](#example "Direct link to Example")
---------------------------------------------

Props[​](#props "Direct link to Props")
---------------------------------------

### `android_disableSound` Android [​](#android_disablesound-android "Direct link to android_disablesound-android")

If true, doesn't play Android system sound on press.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | boolean `false` | | | |

### `android_ripple` Android [​](#android_ripple-android "Direct link to android_ripple-android")

Enables the Android ripple effect and configures its properties.

|  |  |
| --- | --- |
| Type|  | | --- | | [RippleConfig](/docs/pressable#rippleconfig) | |

### `children`[​](#children "Direct link to children")

Either children or a function that receives a boolean reflecting whether the component is currently pressed.

|  |  |
| --- | --- |
| Type|  | | --- | | [React Node](/docs/react-node) | |

### `unstable_pressDelay`[​](#unstable_pressdelay "Direct link to unstable_pressdelay")

Duration (in milliseconds) to wait after press down before calling `onPressIn`.

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

### `delayLongPress`[​](#delaylongpress "Direct link to delaylongpress")

Duration (in milliseconds) from `onPressIn` before `onLongPress` is called.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | number `500` | | | |

### `disabled`[​](#disabled "Direct link to disabled")

Whether the press behavior is disabled.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | boolean `false` | | | |

### `hitSlop`[​](#hitslop "Direct link to hitslop")

Sets additional distance outside of element in which a press can be detected.

|  |  |
| --- | --- |
| Type|  | | --- | | [Rect](/docs/rect) or number | |

### `onHoverIn`[​](#onhoverin "Direct link to onhoverin")

Called when the hover is activated to provide visual feedback.

|  |  |
| --- | --- |
| Type|  | | --- | | `({ nativeEvent: MouseEvent }) => void` | |

### `onHoverOut`[​](#onhoverout "Direct link to onhoverout")

Called when the hover is deactivated to undo visual feedback.

|  |  |
| --- | --- |
| Type|  | | --- | | `({ nativeEvent: MouseEvent }) => void` | |

### `onLongPress`[​](#onlongpress "Direct link to onlongpress")

Called if the time after `onPressIn` lasts longer than 500 milliseconds. This time period can be customized with [`delayLongPress`](#delaylongpress).

|  |  |
| --- | --- |
| Type|  | | --- | | `({nativeEvent: PressEvent}) => void` | |

### `onPress`[​](#onpress "Direct link to onpress")

Called after `onPressOut`.

|  |  |
| --- | --- |
| Type|  | | --- | | `({nativeEvent: PressEvent}) => void` | |

### `onPressIn`[​](#onpressin "Direct link to onpressin")

Called immediately when a touch is engaged, before `onPressOut` and `onPress`.

|  |  |
| --- | --- |
| Type|  | | --- | | `({nativeEvent: PressEvent}) => void` | |

### `onPressOut`[​](#onpressout "Direct link to onpressout")

Called when a touch is released.

|  |  |
| --- | --- |
| Type|  | | --- | | `({nativeEvent: PressEvent}) => void` | |

### `pressRetentionOffset`[​](#pressretentionoffset "Direct link to pressretentionoffset")

Additional distance outside of this view in which a touch is considered a press before `onPressOut` is triggered.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | [Rect](/docs/rect) or number `{bottom: 30, left: 20, right: 20, top: 20}` | | | |

### `style`[​](#style "Direct link to style")

Either view styles or a function that receives a boolean reflecting whether the component is currently pressed and returns view styles.

|  |  |
| --- | --- |
| Type|  | | --- | | [View Style](/docs/view-style-props) or `({ pressed: boolean }) => View Style` | |

### `testOnly_pressed`[​](#testonly_pressed "Direct link to testonly_pressed")

Used only for documentation or testing (e.g. snapshot testing).

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | boolean `false` | | | |

Type Definitions[​](#type-definitions "Direct link to Type Definitions")
------------------------------------------------------------------------

### RippleConfig[​](#rippleconfig "Direct link to RippleConfig")

Ripple effect configuration for the `android_ripple` property.

|  |  |
| --- | --- |
| Type|  | | --- | | object | |

**Properties:**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | color [color](/docs/colors) No Defines the color of the ripple effect.|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | borderless boolean No Defines if ripple effect should not include border.|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | radius number No Defines the radius of the ripple effect.|  |  |  |  | | --- | --- | --- | --- | | foreground boolean No Set to true to add the ripple effect to the foreground of the view, instead of the background. This is useful if one of your child views has a background of its own, or you're e.g. displaying images, and you don't want the ripple to be covered by them. | | | | | | | | | | | | | | | | | | | |

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/pressable.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/pressable.md)

Last updated on **Apr 14, 2025**

[Previous

Modal](/docs/modal)[Next

RefreshControl](/docs/refreshcontrol)

* [How it works](#how-it-works)* [Example](#example)* [Props](#props)
      + [`android_disableSound`

        Android](#android_disablesound-android)+ [`android_ripple`

          Android](#android_ripple-android)+ [`children`](#children)+ [`unstable_pressDelay`](#unstable_pressdelay)+ [`delayLongPress`](#delaylongpress)+ [`disabled`](#disabled)+ [`hitSlop`](#hitslop)+ [`onHoverIn`](#onhoverin)+ [`onHoverOut`](#onhoverout)+ [`onLongPress`](#onlongpress)+ [`onPress`](#onpress)+ [`onPressIn`](#onpressin)+ [`onPressOut`](#onpressout)+ [`pressRetentionOffset`](#pressretentionoffset)+ [`style`](#style)+ [`testOnly_pressed`](#testonly_pressed)* [Type Definitions](#type-definitions)
        + [RippleConfig](#rippleconfig)

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