🚧 DatePickerIOS · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/datepickerios)

* [Next](/docs/next/datepickerios)* [0.79](/docs/datepickerios)* [0.78](/docs/0.78/datepickerios)* [0.77](/docs/0.77/datepickerios)* [0.76](/docs/0.76/datepickerios)* [0.75](/docs/0.75/datepickerios)* [0.74](/docs/0.74/datepickerios)* [0.73](/docs/0.73/datepickerios)* [0.72](/docs/0.72/datepickerios)* [0.71](/docs/0.71/datepickerios)* [0.70](/docs/0.70/datepickerios)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

On this page

🚧 DatePickerIOS
===============

> **Removed.** Use one of the [community packages](https://reactnative.directory/?search=datepicker) instead.

Use `DatePickerIOS` to render a date/time picker (selector) on iOS. This is a controlled component, so you must hook in to the `onDateChange` callback and update the `date` prop in order for the component to update, otherwise the user's change will be reverted immediately to reflect `props.date` as the source of truth.

### Example[​](#example "Direct link to Example")

---

Reference
=========

Props[​](#props "Direct link to Props")
---------------------------------------

Inherits [View Props](/docs/view#props).

### `date`[​](#date "Direct link to date")

The currently selected date.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | Date Yes | | | |

---

### `onChange`[​](#onchange "Direct link to onchange")

Date change handler.

This is called when the user changes the date or time in the UI. The first and only argument is an Event. For getting the date the picker was changed to, use onDateChange instead.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | function No | | | |

---

### `onDateChange`[​](#ondatechange "Direct link to ondatechange")

Date change handler.

This is called when the user changes the date or time in the UI. The first and only argument is a Date object representing the new date and time.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | function Yes | | | |

---

### `maximumDate`[​](#maximumdate "Direct link to maximumdate")

Maximum date.

Restricts the range of possible date/time values.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | Date No | | | |

Example with `maximumDate` set to December 31, 2017:

![](/docs/assets/DatePickerIOS/maximumDate.gif)


---

### `minimumDate`[​](#minimumdate "Direct link to minimumdate")

Minimum date.

Restricts the range of possible date/time values.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | Date No | | | |

See [`maximumDate`](#maximumdate) for an example image.

---

### `minuteInterval`[​](#minuteinterval "Direct link to minuteinterval")

The interval at which minutes can be selected.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | enum(1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30) No | | | |

Example with `minuteInterval` set to `10`:

![](/docs/assets/DatePickerIOS/minuteInterval.png)


---

### `mode`[​](#mode "Direct link to mode")

The date picker mode.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | enum('date', 'time', 'datetime', 'countdown') No | | | |

Example with `mode` set to `date`, `time`, and `datetime`: ![](/assets/images/mode-089618b034a4d64bad0b39c4be929f4a.png)

---

### `locale`[​](#locale "Direct link to locale")

The locale for the date picker. Value needs to be a [Locale ID](https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/BPInternational/LanguageandLocaleIDs/LanguageandLocaleIDs.html).

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | String No | | | |

---

### `timeZoneOffsetInMinutes`[​](#timezoneoffsetinminutes "Direct link to timezoneoffsetinminutes")

Timezone offset in minutes.

By default, the date picker will use the device's timezone. With this parameter, it is possible to force a certain timezone offset. For instance, to show times in Pacific Standard Time, pass -7 \* 60.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number No | | | |

---

### `initialDate`[​](#initialdate "Direct link to initialdate")

Provides an initial value that will change when the user starts selecting a date. It is useful for use-cases where you do not want to deal with listening to events and updating the date prop to keep the controlled state in sync. The controlled state has known bugs which causes it to go out of sync with native. The initialDate prop is intended to allow you to have native be source of truth.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | Date No | | | |

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/datepickerios.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/datepickerios.md)

Last updated on **Apr 14, 2025**

* [Example](#example)* [Props](#props)
    + [`date`](#date)+ [`onChange`](#onchange)+ [`onDateChange`](#ondatechange)+ [`maximumDate`](#maximumdate)+ [`minimumDate`](#minimumdate)+ [`minuteInterval`](#minuteinterval)+ [`mode`](#mode)+ [`locale`](#locale)+ [`timeZoneOffsetInMinutes`](#timezoneoffsetinminutes)+ [`initialDate`](#initialdate)

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