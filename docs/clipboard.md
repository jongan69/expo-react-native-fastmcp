🚧 Clipboard · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/clipboard)

* [Next](/docs/next/clipboard)* [0.79](/docs/clipboard)* [0.78](/docs/0.78/clipboard)* [0.77](/docs/0.77/clipboard)* [0.76](/docs/0.76/clipboard)* [0.75](/docs/0.75/clipboard)* [0.74](/docs/0.74/clipboard)* [0.73](/docs/0.73/clipboard)* [0.72](/docs/0.72/clipboard)* [0.71](/docs/0.71/clipboard)* [0.70](/docs/0.70/clipboard)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

On this page

🚧 Clipboard
===========

> **Removed.** Use one of the [community packages](https://reactnative.directory/?search=clipboard) instead.

`Clipboard` gives you an interface for setting and getting content from Clipboard on both Android and iOS

---

Example[​](#example "Direct link to Example")
---------------------------------------------

Reference
=========

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### `getString()`[​](#getstring "Direct link to getstring")

jsx

```
static getString()  

```

Get content of string type, this method returns a `Promise`, so you can use following code to get clipboard content

jsx

```
async _getContent() {  
  const content = await Clipboard.getString();  
}  

```

---

### `setString()`[​](#setstring "Direct link to setstring")

jsx

```
static setString(content)  

```

Set content of string type. You can use following code to set clipboard content

jsx

```
_setContent() {  
  Clipboard.setString('hello world');  
}  

```

**Parameters:**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  | | --- | --- | --- | --- | | content string Yes The content to be stored in the clipboard | | | | | | | |

*Notice*

Be careful when you're trying to copy to clipboard any data except `string` and `number`, some data need additional stringification. For example, if you will try to copy array - Android will raise an exception, but iOS will not.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/clipboard.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/clipboard.md)

Last updated on **Apr 14, 2025**

* [Example](#example)* [Methods](#methods)
    + [`getString()`](#getstring)+ [`setString()`](#setstring)

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