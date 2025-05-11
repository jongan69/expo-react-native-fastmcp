🚧 ImagePickerIOS · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/imagepickerios)

* [Next](/docs/next/imagepickerios)* [0.79](/docs/imagepickerios)* [0.78](/docs/0.78/imagepickerios)* [0.77](/docs/0.77/imagepickerios)* [0.76](/docs/0.76/imagepickerios)* [0.75](/docs/0.75/imagepickerios)* [0.74](/docs/0.74/imagepickerios)* [0.73](/docs/0.73/imagepickerios)* [0.72](/docs/0.72/imagepickerios)* [0.71](/docs/0.71/imagepickerios)* [0.70](/docs/0.70/imagepickerios)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

On this page

🚧 ImagePickerIOS
================

> **Removed.** Use one of the [community packages](https://reactnative.directory/?search=image+picker) instead.

---

Reference
=========

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### `canRecordVideos()`[​](#canrecordvideos "Direct link to canrecordvideos")

jsx

```
static canRecordVideos(callback)  

```

---

### `canUseCamera()`[​](#canusecamera "Direct link to canusecamera")

jsx

```
static canUseCamera(callback)  

```

---

### `openCameraDialog()`[​](#opencameradialog "Direct link to opencameradialog")

jsx

```
static openCameraDialog(config, successCallback, cancelCallback)  

```

**Parameters:**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | config object No See below.|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | successCallback function No See below.|  |  |  |  | | --- | --- | --- | --- | | cancelCallback function No See below. | | | | | | | | | | | | | | | |

`config` is an object containing:

* `videoMode` : An optional boolean value that defaults to false.

`successCallback` is an optional callback function that's invoked when the select dialog is opened successfully. It will include the following data:

* `[string, number, number]`

`cancelCallback` is an optional callback function that's invoked when the camera dialog is canceled.

---

### `openSelectDialog()`[​](#openselectdialog "Direct link to openselectdialog")

jsx

```
static openSelectDialog(config, successCallback, cancelCallback)  

```

**Parameters:**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | config object No See below.|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | successCallback function No See below.|  |  |  |  | | --- | --- | --- | --- | | cancelCallback function No See below. | | | | | | | | | | | | | | | |

`config` is an object containing:

* `showImages` : An optional boolean value that defaults to false.
* `showVideos`: An optional boolean value that defaults to false.

`successCallback` is an optional callback function that's invoked when the select dialog is opened successfully. It will include the following data:

* `[string, number, number]`

`cancelCallback` is an optional callback function that's invoked when the select dialog is canceled.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/imagepickerios.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/imagepickerios.md)

Last updated on **Apr 14, 2025**

* [Methods](#methods)
  + [`canRecordVideos()`](#canrecordvideos)+ [`canUseCamera()`](#canusecamera)+ [`openCameraDialog()`](#opencameradialog)+ [`openSelectDialog()`](#openselectdialog)

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