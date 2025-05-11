🚧 TimePickerAndroid · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/timepickerandroid)

* [Next](/docs/next/timepickerandroid)* [0.79](/docs/timepickerandroid)* [0.78](/docs/0.78/timepickerandroid)* [0.77](/docs/0.77/timepickerandroid)* [0.76](/docs/0.76/timepickerandroid)* [0.75](/docs/0.75/timepickerandroid)* [0.74](/docs/0.74/timepickerandroid)* [0.73](/docs/0.73/timepickerandroid)* [0.72](/docs/0.72/timepickerandroid)* [0.71](/docs/0.71/timepickerandroid)* [0.70](/docs/0.70/timepickerandroid)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

On this page

🚧 TimePickerAndroid
===================

> **Removed.** Use one of the [community packages](https://reactnative.directory/?search=timepicker) instead.

Opens the standard Android time picker dialog.

### Example[​](#example "Direct link to Example")

jsx

```
try {  
  const {action, hour, minute} = await TimePickerAndroid.open({  
    hour: 14,  
    minute: 0,  
    is24Hour: false, // Will display '2 PM'  
  });  
  if (action !== TimePickerAndroid.dismissedAction) {  
    // Selected hour (0-23), minute (0-59)  
  }  
} catch ({code, message}) {  
  console.warn('Cannot open time picker', message);  
}  

```

---

Reference
=========

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### `open()`[​](#open "Direct link to open")

jsx

```
static open(options)  

```

Opens the standard Android time picker dialog.

The available keys for the `options` object are:

* `hour` (0-23) - the hour to show, defaults to the current time
* `minute` (0-59) - the minute to show, defaults to the current time
* `is24Hour` (boolean) - If `true`, the picker uses the 24-hour format. If `false`, the picker shows an AM/PM chooser. If undefined, the default for the current locale is used.
* `mode` (`enum('clock', 'spinner', 'default')`) - set the time picker mode
  + 'clock': Show a time picker in clock mode.
  + 'spinner': Show a time picker in spinner mode.
  + 'default': Show a default time picker based on Android versions.

Returns a Promise which will be invoked an object containing `action`, `hour` (0-23), `minute` (0-59) if the user picked a time. If the user dismissed the dialog, the Promise will still be resolved with action being `TimePickerAndroid.dismissedAction` and all the other keys being undefined. **Always** check whether the `action` before reading the values.

---

### `timeSetAction()`[​](#timesetaction "Direct link to timesetaction")

jsx

```
static timeSetAction()  

```

A time has been selected.

---

### `dismissedAction()`[​](#dismissedaction "Direct link to dismissedaction")

jsx

```
static dismissedAction()  

```

The dialog has been dismissed.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/timepickerandroid.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/timepickerandroid.md)

Last updated on **Apr 14, 2025**

* [Example](#example)* [Methods](#methods)
    + [`open()`](#open)+ [`timeSetAction()`](#timesetaction)+ [`dismissedAction()`](#dismissedaction)

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