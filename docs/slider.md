🚧 Slider · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.75](/docs/0.75/slider)

* [Next](/docs/next/getting-started)* [0.79](/docs/getting-started)* [0.78](/docs/0.78/getting-started)* [0.77](/docs/0.77/getting-started)* [0.76](/docs/0.76/getting-started)* [0.75](/docs/0.75/slider)* [0.74](/docs/0.74/slider)* [0.73](/docs/0.73/slider)* [0.72](/docs/0.72/slider)* [0.71](/docs/0.71/slider)* [0.70](/docs/0.70/slider)* [All versions](/versions)

[Development](#)

* [Guides](/docs/0.75/getting-started)* [Components](/docs/0.75/components-and-apis)* [APIs](/docs/0.75/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

This is documentation for React Native **0.75**, which is no longer in active development.

For up-to-date documentation, see the **[latest version](/docs/getting-started)** (0.79).

Version: 0.75

On this page

🚧 Slider
========

> **Deprecated.** Use one of the [community packages](https://reactnative.directory/?search=slider) instead.

A component used to select a single value from a range of values.

---

Reference
=========

Props[​](#props "Direct link to Props")
---------------------------------------

Inherits [View Props](/docs/0.75/view#props).

### `style`[​](#style "Direct link to style")

Used to style and layout the `Slider`. See `StyleSheet.js` and `ViewStylePropTypes.js` for more info.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | View.style No | | | |

---

### `disabled`[​](#disabled "Direct link to disabled")

If true the user won't be able to move the slider. Default value is false.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | bool No | | | |

---

### `maximumValue`[​](#maximumvalue "Direct link to maximumvalue")

Initial maximum value of the slider. Default value is 1.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number No | | | |

---

### `minimumTrackTintColor`[​](#minimumtracktintcolor "Direct link to minimumtracktintcolor")

The color used for the track to the left of the button. Overrides the default blue gradient image on iOS.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | [color](/docs/0.75/colors) No | | | |

---

### `minimumValue`[​](#minimumvalue "Direct link to minimumvalue")

Initial minimum value of the slider. Default value is 0.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number No | | | |

---

### `onSlidingComplete`[​](#onslidingcomplete "Direct link to onslidingcomplete")

Callback that is called when the user releases the slider, regardless if the value has changed. The current value is passed as an argument to the callback handler.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | function No | | | |

---

### `onValueChange`[​](#onvaluechange "Direct link to onvaluechange")

Callback continuously called while the user is dragging the slider.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | function No | | | |

---

### `step`[​](#step "Direct link to step")

Step value of the slider. The value should be between 0 and (maximumValue - minimumValue). Default value is 0.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number No | | | |

---

### `maximumTrackTintColor`[​](#maximumtracktintcolor "Direct link to maximumtracktintcolor")

The color used for the track to the right of the button. Overrides the default gray gradient image on iOS.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | [color](/docs/0.75/colors) No | | | |

---

### `testID`[​](#testid "Direct link to testid")

Used to locate this view in UI automation tests.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | string No | | | |

---

### `value`[​](#value "Direct link to value")

Initial value of the slider. The value should be between minimumValue and maximumValue, which default to 0 and 1 respectively. Default value is 0.

*This is not a controlled component*, you don't need to update the value during dragging.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number No | | | |

---

### `thumbTintColor`[​](#thumbtintcolor "Direct link to thumbtintcolor")

The color used to tint the default thumb images on iOS, or the color of the foreground switch grip on Android.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | [color](/docs/0.75/colors) No | | | |

---

### `maximumTrackImage`[​](#maximumtrackimage "Direct link to maximumtrackimage")

Assigns a maximum track image. Only static images are supported. The leftmost pixel of the image will be stretched to fill the track.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Type Required Platform|  |  |  | | --- | --- | --- | | Image.propTypes.source No iOS | | | | | |

---

### `minimumTrackImage`[​](#minimumtrackimage "Direct link to minimumtrackimage")

Assigns a minimum track image. Only static images are supported. The rightmost pixel of the image will be stretched to fill the track.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Type Required Platform|  |  |  | | --- | --- | --- | | Image.propTypes.source No iOS | | | | | |

---

### `thumbImage`[​](#thumbimage "Direct link to thumbimage")

Sets an image for the thumb. Only static images are supported.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Type Required Platform|  |  |  | | --- | --- | --- | | Image.propTypes.source No iOS | | | | | |

---

### `trackImage`[​](#trackimage "Direct link to trackimage")

Assigns a single image for the track. Only static images are supported. The center pixel of the image will be stretched to fill the track.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Type Required Platform|  |  |  | | --- | --- | --- | | Image.propTypes.source No iOS | | | | | |

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/slider.md)[Edit page for 0.75 release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.75/slider.md)

Last updated on **Aug 15, 2024**

* [Props](#props)
  + [`style`](#style)+ [`disabled`](#disabled)+ [`maximumValue`](#maximumvalue)+ [`minimumTrackTintColor`](#minimumtracktintcolor)+ [`minimumValue`](#minimumvalue)+ [`onSlidingComplete`](#onslidingcomplete)+ [`onValueChange`](#onvaluechange)+ [`step`](#step)+ [`maximumTrackTintColor`](#maximumtracktintcolor)+ [`testID`](#testid)+ [`value`](#value)+ [`thumbTintColor`](#thumbtintcolor)+ [`maximumTrackImage`](#maximumtrackimage)+ [`minimumTrackImage`](#minimumtrackimage)+ [`thumbImage`](#thumbimage)+ [`trackImage`](#trackimage)

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