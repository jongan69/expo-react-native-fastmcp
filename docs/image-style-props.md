Image Style Props · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/image-style-props)

* [Next](/docs/next/image-style-props)* [0.79](/docs/image-style-props)* [0.78](/docs/0.78/image-style-props)* [0.77](/docs/0.77/image-style-props)* [0.76](/docs/0.76/image-style-props)* [0.75](/docs/0.75/image-style-props)* [0.74](/docs/0.74/image-style-props)* [0.73](/docs/0.73/image-style-props)* [0.72](/docs/0.72/image-style-props)* [0.71](/docs/0.71/image-style-props)* [0.70](/docs/0.70/image-style-props)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [Core Components](/docs/components-and-apis)

  * [Props](/docs/image-style-props)

    + [Image Style Props](/docs/image-style-props)+ [Layout Props](/docs/layout-props)+ [Shadow Props](/docs/shadow-props)+ [Text Style Props](/docs/text-style-props)+ [View Style Props](/docs/view-style-props)* [Object Types](/docs/boxshadowvalue)

On this page

Image Style Props
=================

Examples[​](#examples "Direct link to Examples")
------------------------------------------------

### Image Resize Mode[​](#image-resize-mode "Direct link to Image Resize Mode")

### Image Border[​](#image-border "Direct link to Image Border")

### Image Border Radius[​](#image-border-radius "Direct link to Image Border Radius")

### Image Tint[​](#image-tint "Direct link to Image Tint")

Reference
=========

Props[​](#props "Direct link to Props")
---------------------------------------

### `backfaceVisibility`[​](#backfacevisibility "Direct link to backfacevisibility")

The property defines whether or not the back face of a rotated image should be visible.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | enum(`'visible'`, `'hidden'`) `'visible'` | | | |

---

### `backgroundColor`[​](#backgroundcolor "Direct link to backgroundcolor")

|  |  |
| --- | --- |
| Type|  | | --- | | [color](/docs/colors) | |

---

### `borderBottomLeftRadius`[​](#borderbottomleftradius "Direct link to borderbottomleftradius")

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

---

### `borderBottomRightRadius`[​](#borderbottomrightradius "Direct link to borderbottomrightradius")

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

---

### `borderColor`[​](#bordercolor "Direct link to bordercolor")

|  |  |
| --- | --- |
| Type|  | | --- | | [color](/docs/colors) | |

---

### `borderRadius`[​](#borderradius "Direct link to borderradius")

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

---

### `borderTopLeftRadius`[​](#bordertopleftradius "Direct link to bordertopleftradius")

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

---

### `borderTopRightRadius`[​](#bordertoprightradius "Direct link to bordertoprightradius")

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

---

### `borderWidth`[​](#borderwidth "Direct link to borderwidth")

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

---

### `opacity`[​](#opacity "Direct link to opacity")

Set an opacity value for the image. The number should be in the range from `0.0` to `1.0`.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | number `1.0` | | | |

---

### `overflow`[​](#overflow "Direct link to overflow")

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | enum(`'visible'`, `'hidden'`) `'visible'` | | | |

---

### `overlayColor` Android [​](#overlaycolor-android "Direct link to overlaycolor-android")

When the image has rounded corners, specifying an overlayColor will cause the remaining space in the corners to be filled with a solid color. This is useful in cases which are not supported by the Android implementation of rounded corners:

* Certain resize modes, such as `'contain'`
* Animated GIFs

A typical way to use this prop is with images displayed on a solid background and setting the `overlayColor` to the same color as the background.

For details of how this works under the hood, see [Fresco documentation](https://frescolib.org/docs/rounded-corners-and-circles.html).

|  |  |
| --- | --- |
| Type|  | | --- | | string | |

---

### `resizeMode`[​](#resizemode "Direct link to resizemode")

Determines how to resize the image when the frame doesn't match the raw image dimensions. Defaults to `cover`.

* `cover`: Scale the image uniformly (maintain the image's aspect ratio) so that:

  + Both dimensions (width and height) of the image will be equal to or larger than the corresponding dimension of the view (minus padding)
  + At least one dimension of the scaled image will be equal to the corresponding dimension of the view (minus padding)
* `contain`: Scale the image uniformly (maintain the image's aspect ratio) so that both dimensions (width and height) of the image will be equal to or less than the corresponding dimension of the view (minus padding).
* `stretch`: Scale width and height independently, This may change the aspect ratio of the src.
* `repeat`: Repeat the image to cover the frame of the view. The image will keep its size and aspect ratio, unless it is larger than the view, in which case it will be scaled down uniformly so that it is contained in the view.
* `center`: Center the image in the view along both dimensions. If the image is larger than the view, scale it down uniformly so that it is contained in the view.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | enum(`'cover'`, `'contain'`, `'stretch'`, `'repeat'`, `'center'`) `'cover'` | | | |

---

### `objectFit`[​](#objectfit "Direct link to objectfit")

Determines how to resize the image when the frame doesn't match the raw image dimensions.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | enum(`'cover'`, `'contain'`, `'fill'`, `'scale-down'`) `'cover'` | | | |

---

### `tintColor`[​](#tintcolor "Direct link to tintcolor")

Changes the color of all the non-transparent pixels to the tintColor.

|  |  |
| --- | --- |
| Type|  | | --- | | [color](/docs/colors) | |

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/image-style-props.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/image-style-props.md)

Last updated on **Apr 14, 2025**

[Previous

SafeAreaView](/docs/safeareaview)[Next

Layout Props](/docs/layout-props)

* [Examples](#examples)
  + [Image Resize Mode](#image-resize-mode)+ [Image Border](#image-border)+ [Image Border Radius](#image-border-radius)+ [Image Tint](#image-tint)* [Props](#props)
    + [`backfaceVisibility`](#backfacevisibility)+ [`backgroundColor`](#backgroundcolor)+ [`borderBottomLeftRadius`](#borderbottomleftradius)+ [`borderBottomRightRadius`](#borderbottomrightradius)+ [`borderColor`](#bordercolor)+ [`borderRadius`](#borderradius)+ [`borderTopLeftRadius`](#bordertopleftradius)+ [`borderTopRightRadius`](#bordertoprightradius)+ [`borderWidth`](#borderwidth)+ [`opacity`](#opacity)+ [`overflow`](#overflow)+ [`overlayColor`

                            Android](#overlaycolor-android)+ [`resizeMode`](#resizemode)+ [`objectFit`](#objectfit)+ [`tintColor`](#tintcolor)

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