🚧 SegmentedControlIOS · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/segmentedcontrolios)

* [Next](/docs/next/segmentedcontrolios)* [0.79](/docs/segmentedcontrolios)* [0.78](/docs/0.78/segmentedcontrolios)* [0.77](/docs/0.77/segmentedcontrolios)* [0.76](/docs/0.76/segmentedcontrolios)* [0.75](/docs/0.75/segmentedcontrolios)* [0.74](/docs/0.74/segmentedcontrolios)* [0.73](/docs/0.73/segmentedcontrolios)* [0.72](/docs/0.72/segmentedcontrolios)* [0.71](/docs/0.71/segmentedcontrolios)* [0.70](/docs/0.70/segmentedcontrolios)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

On this page

🚧 SegmentedControlIOS
=====================

> **Removed from React Native.** Use one of the [community packages](https://reactnative.directory/?search=segmentedcontrol) instead.

Uses `SegmentedControlIOS` to render a UISegmentedControl iOS.

#### Programmatically changing selected index[​](#programmatically-changing-selected-index "Direct link to Programmatically changing selected index")

The selected index can be changed on the fly by assigning the selectedIndex prop to a state variable, then changing that variable. Note that the state variable would need to be updated as the user selects a value and changes the index, as shown in the example below.

Example[​](#example "Direct link to Example")
---------------------------------------------

---

Reference
=========

Props[​](#props "Direct link to Props")
---------------------------------------

Inherits [View Props](/docs/view#props).

### `enabled`[​](#enabled "Direct link to enabled")

If false the user won't be able to interact with the control. Default value is true.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | bool No | | | |

---

### `momentary`[​](#momentary "Direct link to momentary")

If true, then selecting a segment won't persist visually. The `onValueChange` callback will still work as expected.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | bool No | | | |

---

### `onChange`[​](#onchange "Direct link to onchange")

Callback that is called when the user taps a segment; passes the event as an argument

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | function No | | | |

---

### `onValueChange`[​](#onvaluechange "Direct link to onvaluechange")

Callback that is called when the user taps a segment; passes the segment's value as an argument

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | function No | | | |

---

### `selectedIndex`[​](#selectedindex "Direct link to selectedindex")

The index in `props.values` of the segment to be (pre)selected.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number No | | | |

---

### `tintColor`[​](#tintcolor "Direct link to tintcolor")

> **Note:** `tintColor` is not supported on the iOS 13+.

Accent color of the control.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | string No | | | |

---

### `values`[​](#values "Direct link to values")

The labels for the control's segment buttons, in order.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | array of string No | | | |

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/segmentedcontrolios.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/segmentedcontrolios.md)

Last updated on **Apr 14, 2025**

* [Example](#example)* [Props](#props)
    + [`enabled`](#enabled)+ [`momentary`](#momentary)+ [`onChange`](#onchange)+ [`onValueChange`](#onvaluechange)+ [`selectedIndex`](#selectedindex)+ [`tintColor`](#tintcolor)+ [`values`](#values)

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