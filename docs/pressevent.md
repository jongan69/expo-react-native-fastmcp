PressEvent Object Type · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/pressevent)

* [Next](/docs/next/pressevent)* [0.79](/docs/pressevent)* [0.78](/docs/0.78/pressevent)* [0.77](/docs/0.77/pressevent)* [0.76](/docs/0.76/pressevent)* [0.75](/docs/0.75/pressevent)* [0.74](/docs/0.74/pressevent)* [0.73](/docs/0.73/pressevent)* [0.72](/docs/0.72/pressevent)* [0.71](/docs/0.71/pressevent)* [0.70](/docs/0.70/pressevent)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [Core Components](/docs/components-and-apis)

  * [Props](/docs/image-style-props)

    * [Object Types](/docs/boxshadowvalue)

      + [BoxShadowValue Object Type](/docs/boxshadowvalue)+ [DropShadowValue Object Type](/docs/dropshadowvalue)+ [LayoutEvent Object Type](/docs/layoutevent)+ [PressEvent Object Type](/docs/pressevent)+ [React Node Object Type](/docs/react-node)+ [Rect Object Type](/docs/rect)+ [ViewToken Object Type](/docs/viewtoken)

On this page

PressEvent Object Type
======================

`PressEvent` object is returned in the callback as a result of user press interaction, for example `onPress` in [Button](/docs/button) component.

Example[​](#example "Direct link to Example")
---------------------------------------------

js

```
{  
    changedTouches: [PressEvent],  
    identifier: 1,  
    locationX: 8,  
    locationY: 4.5,  
    pageX: 24,  
    pageY: 49.5,  
    target: 1127,  
    timestamp: 85131876.58868201,  
    touches: []  
}  

```

Keys and values[​](#keys-and-values "Direct link to Keys and values")
---------------------------------------------------------------------

### `changedTouches`[​](#changedtouches "Direct link to changedtouches")

Array of all PressEvents that have changed since the last event.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Optional|  |  | | --- | --- | | array of PressEvents No | | | |

### `force` iOS [​](#force-ios "Direct link to force-ios")

Amount of force used during the 3D Touch press. Returns the float value in range from `0.0` to `1.0`.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Optional|  |  | | --- | --- | | number Yes | | | |

### `identifier`[​](#identifier "Direct link to identifier")

Unique numeric identifier assigned to the event.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Optional|  |  | | --- | --- | | number No | | | |

### `locationX`[​](#locationx "Direct link to locationx")

Touch origin X coordinate inside touchable area (relative to the element).

|  |  |  |  |
| --- | --- | --- | --- |
| Type Optional|  |  | | --- | --- | | number No | | | |

### `locationY`[​](#locationy "Direct link to locationy")

Touch origin Y coordinate inside touchable area (relative to the element).

|  |  |  |  |
| --- | --- | --- | --- |
| Type Optional|  |  | | --- | --- | | number No | | | |

### `pageX`[​](#pagex "Direct link to pagex")

Touch origin X coordinate on the screen (relative to the root view).

|  |  |  |  |
| --- | --- | --- | --- |
| Type Optional|  |  | | --- | --- | | number No | | | |

### `pageY`[​](#pagey "Direct link to pagey")

Touch origin Y coordinate on the screen (relative to the root view).

|  |  |  |  |
| --- | --- | --- | --- |
| Type Optional|  |  | | --- | --- | | number No | | | |

### `target`[​](#target "Direct link to target")

The node id of the element receiving the PressEvent.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Optional|  |  | | --- | --- | | number, `null`, `undefined` No | | | |

### `timestamp`[​](#timestamp "Direct link to timestamp")

Timestamp value when a PressEvent occurred. Value is represented in milliseconds.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Optional|  |  | | --- | --- | | number No | | | |

### `touches`[​](#touches "Direct link to touches")

Array of all current PressEvents on the screen.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Optional|  |  | | --- | --- | | array of PressEvents No | | | |

Used by[​](#used-by "Direct link to Used by")
---------------------------------------------

* [`Button`](/docs/button)
* [`PanResponder`](/docs/panresponder)
* [`Pressable`](/docs/pressable)
* [`ScrollView`](/docs/scrollview)
* [`Text`](/docs/text)
* [`TextInput`](/docs/textinput)
* [`TouchableHighlight`](/docs/touchablenativefeedback)
* [`TouchableOpacity`](/docs/touchablewithoutfeedback)
* [`TouchableNativeFeedback`](/docs/touchablenativefeedback)
* [`TouchableWithoutFeedback`](/docs/touchablewithoutfeedback)
* [`View`](/docs/view)

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/pressevent.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/pressevent.md)

Last updated on **Apr 14, 2025**

[Previous

LayoutEvent Object Type](/docs/layoutevent)[Next

React Node Object Type](/docs/react-node)

* [Example](#example)* [Keys and values](#keys-and-values)
    + [`changedTouches`](#changedtouches)+ [`force`

        iOS](#force-ios)+ [`identifier`](#identifier)+ [`locationX`](#locationx)+ [`locationY`](#locationy)+ [`pageX`](#pagex)+ [`pageY`](#pagey)+ [`target`](#target)+ [`timestamp`](#timestamp)+ [`touches`](#touches)* [Used by](#used-by)

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