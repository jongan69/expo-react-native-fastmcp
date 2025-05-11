ViewToken Object Type · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/viewtoken)

* [Next](/docs/next/viewtoken)* [0.79](/docs/viewtoken)* [0.78](/docs/0.78/viewtoken)* [0.77](/docs/0.77/viewtoken)* [0.76](/docs/0.76/viewtoken)* [0.75](/docs/0.75/viewtoken)* [0.74](/docs/0.74/viewtoken)* [0.73](/docs/0.73/viewtoken)* [0.72](/docs/0.72/viewtoken)* [0.71](/docs/0.71/viewtoken)* [0.70](/docs/0.70/viewtoken)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [Core Components](/docs/components-and-apis)

  * [Props](/docs/image-style-props)

    * [Object Types](/docs/boxshadowvalue)

      + [BoxShadowValue Object Type](/docs/boxshadowvalue)+ [DropShadowValue Object Type](/docs/dropshadowvalue)+ [LayoutEvent Object Type](/docs/layoutevent)+ [PressEvent Object Type](/docs/pressevent)+ [React Node Object Type](/docs/react-node)+ [Rect Object Type](/docs/rect)+ [ViewToken Object Type](/docs/viewtoken)

On this page

ViewToken Object Type
=====================

`ViewToken` object is returned as one of the properties in the `onViewableItemsChanged` callback (for example, in the [FlatList](/docs/flatlist) component). It is exported by [`ViewabilityHelper.js`](https://github.com/facebook/react-native/blob/main/packages/react-native/Libraries/Lists/ViewabilityHelper.js).

Example[​](#example "Direct link to Example")
---------------------------------------------

js

```
{  
  item: {key: "key-12"},  
  key: "key-12",  
  index: 11,  
  isViewable: true  
}  

```

Keys and values[​](#keys-and-values "Direct link to Keys and values")
---------------------------------------------------------------------

### `index`[​](#index "Direct link to index")

Unique numeric identifier assigned to the data element.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Optional|  |  | | --- | --- | | number Yes | | | |

### `isViewable`[​](#isviewable "Direct link to isviewable")

Specifies if at least some part of list element is visible in the viewport.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Optional|  |  | | --- | --- | | boolean No | | | |

### `item`[​](#item "Direct link to item")

Item data

|  |  |  |  |
| --- | --- | --- | --- |
| Type Optional|  |  | | --- | --- | | any No | | | |

### `key`[​](#key "Direct link to key")

Key identifier assigned to the data element extracted to the top level.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Optional|  |  | | --- | --- | | string No | | | |

### `section`[​](#section "Direct link to section")

Item section data when used with `SectionList`.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Optional|  |  | | --- | --- | | any Yes | | | |

Used by[​](#used-by "Direct link to Used by")
---------------------------------------------

* [`FlatList`](/docs/flatlist)
* [`SectionList`](/docs/sectionlist)
* [`VirtualizedList`](/docs/virtualizedlist)

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/viewtoken.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/viewtoken.md)

Last updated on **Apr 14, 2025**

[Previous

Rect Object Type](/docs/rect)

* [Example](#example)* [Keys and values](#keys-and-values)
    + [`index`](#index)+ [`isViewable`](#isviewable)+ [`item`](#item)+ [`key`](#key)+ [`section`](#section)* [Used by](#used-by)

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