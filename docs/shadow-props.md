Shadow Props · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/shadow-props)

* [Next](/docs/next/shadow-props)* [0.79](/docs/shadow-props)* [0.78](/docs/0.78/shadow-props)* [0.77](/docs/0.77/shadow-props)* [0.76](/docs/0.76/shadow-props)* [0.75](/docs/0.75/shadow-props)* [0.74](/docs/0.74/shadow-props)* [0.73](/docs/0.73/shadow-props)* [0.72](/docs/0.72/shadow-props)* [0.71](/docs/0.71/shadow-props)* [0.70](/docs/0.70/shadow-props)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [Core Components](/docs/components-and-apis)

  * [Props](/docs/image-style-props)

    + [Image Style Props](/docs/image-style-props)+ [Layout Props](/docs/layout-props)+ [Shadow Props](/docs/shadow-props)+ [Text Style Props](/docs/text-style-props)+ [View Style Props](/docs/view-style-props)* [Object Types](/docs/boxshadowvalue)

On this page

Shadow Props
============

* TypeScript* JavaScript

---

Reference
=========

There are 3 sets of shadow APIs in React Native:

* `boxShadow`: A View style prop and a spec-compliant implementation of the [web style prop of the same name](https://developer.mozilla.org/en-US/docs/Web/CSS/box-shadow).
* `dropShadow`: A specific filter function available as part of the [`filter`](/docs/view-style-props#filter) View style prop.
* Various `shadow` props (`shadowColor`, `shadowOffset`, `shadowOpacity`, `shadowRadius`): These map directly to their native counterparts exposed by the platform-level APIs.

The difference between `dropShadow` and `boxShadow` are as follows:

* `dropShadow` exists as part of `filter`, whereas `boxShadow` is a standalone style prop.
* `dropShadow` is an alpha mask, so only pixels with a positive alpha value will "cast" a shadow. `boxShadow` will cast around the border box of the element no matter it's contents (unless it is inset).
* `dropShadow` is only available on Android, `boxShadow` is available on iOS and Android.
* `dropShadow` cannot be inset like `boxShadow`.
* `dropShadow` does not have the `spreadDistance` argument like `boxShadow`.

Both `boxShadow` and `dropShadow` are generally more capable than the `shadow` props. The `shadow` props, however, map to native platform-level APIs, so if you only need a straightforward shadow these props are recommended. Note that only `shadowColor` works on both Android and iOS, all other `shadow` props only work on iOS.

Props[​](#props "Direct link to Props")
---------------------------------------

### `boxShadow`[​](#boxshadow "Direct link to boxshadow")

See [View Style Props](/docs/view-style-props#boxshadow) for documentation.

### `dropShadow` Android [​](#dropshadow-android "Direct link to dropshadow-android")

See [View Style Props](/docs/view-style-props#filter) for documentation.

### `shadowColor`[​](#shadowcolor "Direct link to shadowcolor")

Sets the drop shadow color.

This property will only work on Android API 28 and above. For similar functionality on lower Android APIs, use the [`elevation` property](/docs/view-style-props#elevation-android).

|  |  |
| --- | --- |
| Type|  | | --- | | [color](/docs/colors) | |

---

### `shadowOffset` iOS [​](#shadowoffset-ios "Direct link to shadowoffset-ios")

Sets the drop shadow offset.

|  |  |
| --- | --- |
| Type|  | | --- | | object: `{width: number,height: number}` | |

---

### `shadowOpacity` iOS [​](#shadowopacity-ios "Direct link to shadowopacity-ios")

Sets the drop shadow opacity (multiplied by the color's alpha component).

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

---

### `shadowRadius` iOS [​](#shadowradius-ios "Direct link to shadowradius-ios")

Sets the drop shadow blur radius.

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/shadow-props.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/shadow-props.md)

Last updated on **Apr 14, 2025**

[Previous

Layout Props](/docs/layout-props)[Next

Text Style Props](/docs/text-style-props)

* [Props](#props)
  + [`boxShadow`](#boxshadow)+ [`dropShadow`

      Android](#dropshadow-android)+ [`shadowColor`](#shadowcolor)+ [`shadowOffset`

          iOS](#shadowoffset-ios)+ [`shadowOpacity`

            iOS](#shadowopacity-ios)+ [`shadowRadius`

              iOS](#shadowradius-ios)

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