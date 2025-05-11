BoxShadowValue Object Type · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/boxshadowvalue)

* [Next](/docs/next/boxshadowvalue)* [0.79](/docs/boxshadowvalue)* [0.78](/docs/0.78/boxshadowvalue)* [0.77](/docs/0.77/boxshadowvalue)* [0.76](/docs/0.76/boxshadowvalue)* [0.75](/docs/0.75/getting-started)* [0.74](/docs/0.74/getting-started)* [0.73](/docs/0.73/getting-started)* [0.72](/docs/0.72/getting-started)* [0.71](/docs/0.71/getting-started)* [0.70](/docs/0.70/getting-started)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [Core Components](/docs/components-and-apis)

  * [Props](/docs/image-style-props)

    * [Object Types](/docs/boxshadowvalue)

      + [BoxShadowValue Object Type](/docs/boxshadowvalue)+ [DropShadowValue Object Type](/docs/dropshadowvalue)+ [LayoutEvent Object Type](/docs/layoutevent)+ [PressEvent Object Type](/docs/pressevent)+ [React Node Object Type](/docs/react-node)+ [Rect Object Type](/docs/rect)+ [ViewToken Object Type](/docs/viewtoken)

On this page

BoxShadowValue Object Type
==========================

The `BoxShadowValue` object is taken by the [`boxShadow`](/docs/view-style-props#boxshadow) style prop. It is comprised of 2-4 lengths, an optional color, and an optional `inset` boolean. These values collectively define the box shadow's color, position, size, and blurriness.

Example[​](#example "Direct link to Example")
---------------------------------------------

js

```
{  
  offsetX: 10,  
  offsetY: -3,  
  blurRadius: '15px',  
  spreadDistance: '10px',  
  color: 'red',  
  inset: true,  
}  

```

Keys and values[​](#keys-and-values "Direct link to Keys and values")
---------------------------------------------------------------------

### `offsetX`[​](#offsetx "Direct link to offsetx")

The offset on the x-axis. This can be positive or negative. A positive value indicates right and negative indicates left.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Optional|  |  | | --- | --- | | number | string No | | | |

### `offsetY`[​](#offsety "Direct link to offsety")

The offset on the y-axis. This can be positive or negative. A positive value indicates up and negative indicates down.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Optional|  |  | | --- | --- | | number | string No | | | |

### `blurRadius`[​](#blurradius "Direct link to blurradius")

Represents the radius used in the [Guassian blur](https://en.wikipedia.org/wiki/Gaussian_blur) algorithm. The larger the value the blurrier the shadow is. Only non-negative values are valid. The default is 0.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Optional|  |  | | --- | --- | | numer | string Yes | | | |

### `spreadDistance`[​](#spreaddistance "Direct link to spreaddistance")

How much larger or smaller the shadow grows or shrinks. A positive value will grow the shadow, a negative value will shrink the shadow.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Optional|  |  | | --- | --- | | numer | string Yes | | | |

### `color`[​](#color "Direct link to color")

The color of the shadow. The default is `black`.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Optional|  |  | | --- | --- | | [color](/docs/colors) Yes | | | |

### `inset`[​](#inset "Direct link to inset")

Whether the shadow is inset or not. Inset shadows will appear around the inside of the element's border box as opposed to the outside.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Optional|  |  | | --- | --- | | boolean Yes | | | |

Used by[​](#used-by "Direct link to Used by")
---------------------------------------------

* [`boxShadow`](/docs/view-style-props#boxshadow)

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/boxshadowvalue.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/boxshadowvalue.md)

Last updated on **Apr 14, 2025**

[Previous

View Style Props](/docs/view-style-props)[Next

DropShadowValue Object Type](/docs/dropshadowvalue)

* [Example](#example)* [Keys and values](#keys-and-values)
    + [`offsetX`](#offsetx)+ [`offsetY`](#offsety)+ [`blurRadius`](#blurradius)+ [`spreadDistance`](#spreaddistance)+ [`color`](#color)+ [`inset`](#inset)* [Used by](#used-by)

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