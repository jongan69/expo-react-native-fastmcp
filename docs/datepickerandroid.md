🚧 DatePickerAndroid · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/datepickerandroid)

* [Next](/docs/next/datepickerandroid)* [0.79](/docs/datepickerandroid)* [0.78](/docs/0.78/datepickerandroid)* [0.77](/docs/0.77/datepickerandroid)* [0.76](/docs/0.76/datepickerandroid)* [0.75](/docs/0.75/datepickerandroid)* [0.74](/docs/0.74/datepickerandroid)* [0.73](/docs/0.73/datepickerandroid)* [0.72](/docs/0.72/datepickerandroid)* [0.71](/docs/0.71/datepickerandroid)* [0.70](/docs/0.70/datepickerandroid)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

On this page

🚧 DatePickerAndroid
===================

> **Removed.** Use one of the [community packages](https://reactnative.directory/?search=datepicker) instead.

Opens the standard Android date picker dialog.

### Example[​](#example "Direct link to Example")

jsx

```
try {  
  const {action, year, month, day} = await DatePickerAndroid.open(  
    {  
      // Use `new Date()` for current date.  
      // May 25 2020. Month 0 is January.  
      date: new Date(2020, 4, 25),  
    },  
  );  
  if (action !== DatePickerAndroid.dismissedAction) {  
    // Selected year, month (0-11), day  
  }  
} catch ({code, message}) {  
  console.warn('Cannot open date picker', message);  
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

Opens the standard Android date picker dialog.

The available keys for the `options` object are:

* `date` (`Date` object or timestamp in milliseconds) - date to show by default
* `minDate` (`Date` or timestamp in milliseconds) - minimum date that can be selected
* `maxDate` (`Date` object or timestamp in milliseconds) - maximum date that can be selected
* `mode` (`enum('calendar', 'spinner', 'default')`) - To set the date-picker mode to calendar/spinner/default
  + 'calendar': Show a date picker in calendar mode.
  + 'spinner': Show a date picker in spinner mode.
  + 'default': Show a default native date picker(spinner/calendar) based on android versions.

Returns a Promise which will be invoked an object containing `action`, `year`, `month` (0-11), `day` if the user picked a date. If the user dismissed the dialog, the Promise will still be resolved with action being `DatePickerAndroid.dismissedAction` and all the other keys being undefined. **Always** check whether the `action` is equal to `DatePickerAndroid.dateSetAction` before reading the values.

Note the native date picker dialog has some UI glitches on Android 4 and lower when using the `minDate` and `maxDate` options.

---

### `dateSetAction()`[​](#datesetaction "Direct link to datesetaction")

jsx

```
static dateSetAction()  

```

A date has been selected.

---

### `dismissedAction()`[​](#dismissedaction "Direct link to dismissedaction")

jsx

```
static dismissedAction()  

```

The dialog has been dismissed.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/datepickerandroid.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/datepickerandroid.md)

Last updated on **Apr 14, 2025**

* [Example](#example)* [Methods](#methods)
    + [`open()`](#open)+ [`dateSetAction()`](#datesetaction)+ [`dismissedAction()`](#dismissedaction)

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