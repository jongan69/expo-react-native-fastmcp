LayoutEvent Object Type · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/layoutevent)

* [Next](/docs/next/layoutevent)* [0.79](/docs/layoutevent)* [0.78](/docs/0.78/layoutevent)* [0.77](/docs/0.77/layoutevent)* [0.76](/docs/0.76/layoutevent)* [0.75](/docs/0.75/layoutevent)* [0.74](/docs/0.74/layoutevent)* [0.73](/docs/0.73/layoutevent)* [0.72](/docs/0.72/layoutevent)* [0.71](/docs/0.71/layoutevent)* [0.70](/docs/0.70/layoutevent)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [Core Components](/docs/components-and-apis)

  * [Props](/docs/image-style-props)

    * [Object Types](/docs/boxshadowvalue)

      + [BoxShadowValue Object Type](/docs/boxshadowvalue)+ [DropShadowValue Object Type](/docs/dropshadowvalue)+ [LayoutEvent Object Type](/docs/layoutevent)+ [PressEvent Object Type](/docs/pressevent)+ [React Node Object Type](/docs/react-node)+ [Rect Object Type](/docs/rect)+ [ViewToken Object Type](/docs/viewtoken)

On this page

LayoutEvent Object Type
=======================

`LayoutEvent` object is returned in the callback as a result of component layout change, for example `onLayout` in [View](/docs/view) component.

Example[​](#example "Direct link to Example")
---------------------------------------------

js

```
{  
    layout: {  
        width: 520,  
        height: 70.5,  
        x: 0,  
        y: 42.5  
    },  
    target: 1127  
}  

```

Keys and values[​](#keys-and-values "Direct link to Keys and values")
---------------------------------------------------------------------

### `height`[​](#height "Direct link to height")

Height of the component after the layout changes.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Optional|  |  | | --- | --- | | number No | | | |

### `width`[​](#width "Direct link to width")

Width of the component after the layout changes.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Optional|  |  | | --- | --- | | number No | | | |

### `x`[​](#x "Direct link to x")

Component X coordinate inside the parent component.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Optional|  |  | | --- | --- | | number No | | | |

### `y`[​](#y "Direct link to y")

Component Y coordinate inside the parent component.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Optional|  |  | | --- | --- | | number No | | | |

### `target`[​](#target "Direct link to target")

The node id of the element receiving the PressEvent.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Optional|  |  | | --- | --- | | number, `null`, `undefined` No | | | |

Used by[​](#used-by "Direct link to Used by")
---------------------------------------------

* [`Image`](/docs/image)
* [`Pressable`](/docs/pressable)
* [`ScrollView`](/docs/scrollview)
* [`Text`](/docs/text)
* [`TextInput`](/docs/textinput)
* [`TouchableWithoutFeedback`](/docs/touchablewithoutfeedback)
* [`View`](/docs/view)

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/layoutevent.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/layoutevent.md)

Last updated on **Apr 14, 2025**

[Previous

DropShadowValue Object Type](/docs/dropshadowvalue)[Next

PressEvent Object Type](/docs/pressevent)

* [Example](#example)* [Keys and values](#keys-and-values)
    + [`height`](#height)+ [`width`](#width)+ [`x`](#x)+ [`y`](#y)+ [`target`](#target)* [Used by](#used-by)

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