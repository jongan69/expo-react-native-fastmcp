Text Style Props · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/text-style-props)

* [Next](/docs/next/text-style-props)* [0.79](/docs/text-style-props)* [0.78](/docs/0.78/text-style-props)* [0.77](/docs/0.77/text-style-props)* [0.76](/docs/0.76/text-style-props)* [0.75](/docs/0.75/text-style-props)* [0.74](/docs/0.74/text-style-props)* [0.73](/docs/0.73/text-style-props)* [0.72](/docs/0.72/text-style-props)* [0.71](/docs/0.71/text-style-props)* [0.70](/docs/0.70/text-style-props)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [Core Components](/docs/components-and-apis)

  * [Props](/docs/image-style-props)

    + [Image Style Props](/docs/image-style-props)+ [Layout Props](/docs/layout-props)+ [Shadow Props](/docs/shadow-props)+ [Text Style Props](/docs/text-style-props)+ [View Style Props](/docs/view-style-props)* [Object Types](/docs/boxshadowvalue)

On this page

Text Style Props
================

### Example[​](#example "Direct link to Example")

* TypeScript* JavaScript

Reference
=========

Props[​](#props "Direct link to Props")
---------------------------------------

### `color`[​](#color "Direct link to color")

|  |  |
| --- | --- |
| Type|  | | --- | | [color](/docs/colors) | |

---

### `fontFamily`[​](#fontfamily "Direct link to fontfamily")

|  |  |
| --- | --- |
| Type|  | | --- | | string | |

---

### `fontSize`[​](#fontsize "Direct link to fontsize")

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

---

### `fontStyle`[​](#fontstyle "Direct link to fontstyle")

|  |  |
| --- | --- |
| Type|  | | --- | | enum(`'normal'`, `'italic'`) | |

---

### `fontWeight`[​](#fontweight "Direct link to fontweight")

Specifies font weight. The values `'normal'` and `'bold'` are supported for most fonts. Not all fonts have a variant for each of the numeric values, in that case the closest one is chosen.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | enum(`'normal'`, `'bold'`, `'100'`, `'200'`, `'300'`, `'400'`, `'500'`, `'600'`, `'700'`, `'800'`, `'900'`) or number `'normal'` | | | |

---

### `includeFontPadding` Android [​](#includefontpadding-android "Direct link to includefontpadding-android")

Set to `false` to remove extra font padding intended to make space for certain ascenders / descenders. With some fonts, this padding can make text look slightly misaligned when centered vertically. For best results also set `textAlignVertical` to `center`.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | bool `true` | | | |

---

### `fontVariant`[​](#fontvariant "Direct link to fontvariant")

Allows you to set all the font variants for a font. Can be set by using an array of enums or a space-separated string e.g. `'small-caps common-ligatures'`.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | array of enum(`'small-caps'`, `'oldstyle-nums'`, `'lining-nums'`, `'tabular-nums'`, `'proportional-nums'`) or string `[]` | | | |

---

### `letterSpacing`[​](#letterspacing "Direct link to letterspacing")

Increase or decrease the spacing between characters. By default there is no extra letter spacing.

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

---

### `lineHeight`[​](#lineheight "Direct link to lineheight")

Numeric value that controls the vertical spacing between lines of text within a text element. It specifies the distance between the baselines of consecutive lines of text.

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

---

### `textAlign`[​](#textalign "Direct link to textalign")

Specifies text alignment. On Android, the value 'justify' is only supported on Oreo (8.0) or above (API level >= 26). The value will fallback to `left` on lower Android versions.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | enum(`'auto'`, `'left'`, `'right'`, `'center'`, `'justify'`) `'auto'` | | | |

---

### `textAlignVertical` Android [​](#textalignvertical-android "Direct link to textalignvertical-android")

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | enum(`'auto'`, `'top'`, `'bottom'`, `'center'`) `'auto'` | | | |

---

### `textDecorationColor` iOS [​](#textdecorationcolor-ios "Direct link to textdecorationcolor-ios")

|  |  |
| --- | --- |
| Type|  | | --- | | [color](/docs/colors) | |

---

### `textDecorationLine`[​](#textdecorationline "Direct link to textdecorationline")

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | enum(`'none'`, `'underline'`, `'line-through'`, `'underline line-through'`) `'none'` | | | |

---

### `textDecorationStyle` iOS [​](#textdecorationstyle-ios "Direct link to textdecorationstyle-ios")

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | enum(`'solid'`, `'double'`, `'dotted'`, `'dashed'`) `'solid'` | | | |

---

### `textShadowColor`[​](#textshadowcolor "Direct link to textshadowcolor")

|  |  |
| --- | --- |
| Type|  | | --- | | [color](/docs/colors) | |

---

### `textShadowOffset`[​](#textshadowoffset "Direct link to textshadowoffset")

|  |  |
| --- | --- |
| Type|  | | --- | | object: `{width?: number, height?: number}` | |

---

### `textShadowRadius`[​](#textshadowradius "Direct link to textshadowradius")

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

---

### `textTransform`[​](#texttransform "Direct link to texttransform")

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | enum(`'none'`, `'uppercase'`, `'lowercase'`, `'capitalize'`) `'none'` | | | |

---

### `verticalAlign` Android [​](#verticalalign-android "Direct link to verticalalign-android")

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | enum(`'auto'`, `'top'`, `'bottom'`, `'middle'`) `'auto'` | | | |

---

### `writingDirection` iOS [​](#writingdirection-ios "Direct link to writingdirection-ios")

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | enum(`'auto'`, `'ltr'`, `'rtl'`) `'auto'` | | | |

---

### `userSelect`[​](#userselect "Direct link to userselect")

It allows the user to select text and to use the native copy and paste functionality. Has precedence over the `selectable` prop.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | enum(`'auto'`, `'text'`, `'none'`, `'contain'`, `'all'`) `none` | | | |

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/text-style-props.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/text-style-props.md)

Last updated on **Apr 14, 2025**

[Previous

Shadow Props](/docs/shadow-props)[Next

View Style Props](/docs/view-style-props)

* [Example](#example)* [Props](#props)
    + [`color`](#color)+ [`fontFamily`](#fontfamily)+ [`fontSize`](#fontsize)+ [`fontStyle`](#fontstyle)+ [`fontWeight`](#fontweight)+ [`includeFontPadding`

                Android](#includefontpadding-android)+ [`fontVariant`](#fontvariant)+ [`letterSpacing`](#letterspacing)+ [`lineHeight`](#lineheight)+ [`textAlign`](#textalign)+ [`textAlignVertical`

                          Android](#textalignvertical-android)+ [`textDecorationColor`

                            iOS](#textdecorationcolor-ios)+ [`textDecorationLine`](#textdecorationline)+ [`textDecorationStyle`

                                iOS](#textdecorationstyle-ios)+ [`textShadowColor`](#textshadowcolor)+ [`textShadowOffset`](#textshadowoffset)+ [`textShadowRadius`](#textshadowradius)+ [`textTransform`](#texttransform)+ [`verticalAlign`

                                          Android](#verticalalign-android)+ [`writingDirection`

                                            iOS](#writingdirection-ios)+ [`userSelect`](#userselect)

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