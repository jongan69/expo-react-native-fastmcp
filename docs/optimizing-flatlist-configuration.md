Optimizing Flatlist Configuration · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/optimizing-flatlist-configuration)

* [Next](/docs/next/optimizing-flatlist-configuration)* [0.79](/docs/optimizing-flatlist-configuration)* [0.78](/docs/0.78/optimizing-flatlist-configuration)* [0.77](/docs/0.77/optimizing-flatlist-configuration)* [0.76](/docs/0.76/optimizing-flatlist-configuration)* [0.75](/docs/0.75/optimizing-flatlist-configuration)* [0.74](/docs/0.74/optimizing-flatlist-configuration)* [0.73](/docs/0.73/optimizing-flatlist-configuration)* [0.72](/docs/0.72/optimizing-flatlist-configuration)* [0.71](/docs/0.71/optimizing-flatlist-configuration)* [0.70](/docs/0.70/optimizing-flatlist-configuration)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [The Basics](/docs/getting-started)

  * [Environment setup](/docs/environment-setup)

    * [Workflow](/docs/running-on-device)

      * [UI & Interaction](/docs/style)

        * [Debugging](/docs/debugging)

          * [Testing](/docs/testing-overview)

            * [Performance](/docs/performance)

              + [Performance Overview](/docs/performance)+ [Speeding up your Build phase](/docs/build-speed)+ [Optimizing Flatlist Configuration](/docs/optimizing-flatlist-configuration)+ [Optimizing JavaScript loading](/docs/optimizing-javascript-loading)+ [Profiling](/docs/profiling)* [JavaScript Runtime](/docs/javascript-environment)

                * [Codegen](/docs/the-new-architecture/what-is-codegen)

                  * [Native Development](/docs/native-platform)

                    * [Android and iOS guides](/docs/headless-js-android)

                      * [Legacy Architecture](/docs/legacy/native-modules-intro)

On this page

Optimizing Flatlist Configuration
=================================

Terms[​](#terms "Direct link to Terms")
---------------------------------------

* **VirtualizedList:** The component behind `FlatList` (React Native's implementation of the [`Virtual List`](https://bvaughn.github.io/react-virtualized/#/components/List) concept.)
* **Memory consumption:** How much information about your list is being stored in memory, which could lead to an app crash.
* **Responsiveness:** Application ability to respond to interactions. Low responsiveness, for instance, is when you touch on a component and it waits a bit to respond, instead of responding immediately as expected.
* **Blank areas:** When `VirtualizedList` can't render your items fast enough, you may enter a part of your list with non-rendered components that appear as blank space.
* **Viewport:** The visible area of content that is rendered to pixels.
* **Window:** The area in which items should be mounted, which is generally much larger than the viewport.

Props[​](#props "Direct link to Props")
---------------------------------------

Here are a list of props that can help to improve `FlatList` performance:

### removeClippedSubviews[​](#removeclippedsubviews "Direct link to removeClippedSubviews")

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | Boolean False | | | |

If `true`, views that are outside of the viewport are detached from the native view hierarchy.

**Pros:** This reduces time spent on the main thread, and thus reduces the risk of dropped frames, by excluding views outside of the viewport from the native rendering and drawing traversals.

**Cons:** Be aware that this implementation can have bugs, such as missing content (mainly observed on iOS), especially if you are doing complex things with transforms and/or absolute positioning. Also note this does not save significant memory because the views are not deallocated, only detached.

### maxToRenderPerBatch[​](#maxtorenderperbatch "Direct link to maxToRenderPerBatch")

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | Number 10 | | | |

It is a `VirtualizedList` prop that can be passed through `FlatList`. This controls the amount of items rendered per batch, which is the next chunk of items rendered on every scroll.

**Pros:** Setting a bigger number means less visual blank areas when scrolling (increases the fill rate).

**Cons:** More items per batch means longer periods of JavaScript execution potentially blocking other event processing, like presses, hurting responsiveness.

### updateCellsBatchingPeriod[​](#updatecellsbatchingperiod "Direct link to updateCellsBatchingPeriod")

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | Number 50 | | | |

While `maxToRenderPerBatch` tells the amount of items rendered per batch, setting `updateCellsBatchingPeriod` tells your `VirtualizedList` the delay in milliseconds between batch renders (how frequently your component will be rendering the windowed items).

**Pros:** Combining this prop with `maxToRenderPerBatch` gives you the power to, for example, render more items in a less frequent batch, or less items in a more frequent batch.

**Cons:** Less frequent batches may cause blank areas, More frequent batches may cause responsiveness issues.

### initialNumToRender[​](#initialnumtorender "Direct link to initialNumToRender")

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | Number 10 | | | |

The initial amount of items to render.

**Pros:** Define precise number of items that would cover the screen for every device. This can be a big performance boost for the initial render.

**Cons:** Setting a low `initialNumToRender` may cause blank areas, especially if it's too small to cover the viewport on initial render.

### windowSize[​](#windowsize "Direct link to windowSize")

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | Number 21 | | | |

The number passed here is a measurement unit where 1 is equivalent to your viewport height. The default value is 21 (10 viewports above, 10 below, and one in between).

**Pros:** Bigger `windowSize` will result in less chance of seeing blank space while scrolling. On the other hand, smaller `windowSize` will result in fewer items mounted simultaneously, saving memory.

**Cons:** For a bigger `windowSize`, you will have more memory consumption. For a lower `windowSize`, you will have a bigger chance of seeing blank areas.

List items[​](#list-items "Direct link to List items")
------------------------------------------------------

Below are some tips about list item components. They are the core of your list, so they need to be fast.

### Use basic components[​](#use-basic-components "Direct link to Use basic components")

The more complex your components are, the slower they will render. Try to avoid a lot of logic and nesting in your list items. If you are reusing this list item component a lot in your app, create a component only for your big lists and make them with as little logic and nesting as possible.

### Use light components[​](#use-light-components "Direct link to Use light components")

The heavier your components are, the slower they render. Avoid heavy images (use a cropped version or thumbnail for list items, as small as possible). Talk to your design team, use as little effects and interactions and information as possible in your list. Show them in your item's detail.

### Use `memo()`[​](#use-memo "Direct link to use-memo")

`React.memo()` creates a memoized component that will be re-rendered only when the props passed to the component change. We can use this function to optimize the components in the FlatList.

tsx

```
import React, {memo} from 'react';  
import {View, Text} from 'react-native';  
  
const MyListItem = memo(  
  ({title}: {title: string}) => (  
    <View>  
      <Text>{title}</Text>  
    </View>  
  ),  
  (prevProps, nextProps) => {  
    return prevProps.title === nextProps.title;  
  },  
);  
  
export default MyListItem;  

```

In this example, we have determined that MyListItem should be re-rendered only when the title changes. We passed the comparison function as the second argument to React.memo() so that the component is re-rendered only when the specified prop is changed. If the comparison function returns true, the component will not be re-rendered.

### Use cached optimized images[​](#use-cached-optimized-images "Direct link to Use cached optimized images")

You can use the community packages (such as [react-native-fast-image](https://github.com/DylanVann/react-native-fast-image) from [@DylanVann](https://github.com/DylanVann)) for more performant images. Every image in your list is a `new Image()` instance. The faster it reaches the `loaded` hook, the faster your JavaScript thread will be free again.

### Use getItemLayout[​](#use-getitemlayout "Direct link to Use getItemLayout")

If all your list item components have the same height (or width, for a horizontal list), providing the [getItemLayout](/docs/flatlist#getitemlayout) prop removes the need for your `FlatList` to manage async layout calculations. This is a very desirable optimization technique.

If your components have dynamic size and you really need performance, consider asking your design team if they may think of a redesign in order to perform better.

### Use keyExtractor or key[​](#use-keyextractor-or-key "Direct link to Use keyExtractor or key")

You can set the [`keyExtractor`](/docs/flatlist#keyextractor) to your `FlatList` component. This prop is used for caching and as the React `key` to track item re-ordering.

You can also use a `key` prop in your item component.

### Avoid anonymous function on renderItem[​](#avoid-anonymous-function-on-renderitem "Direct link to Avoid anonymous function on renderItem")

For functional components, move the `renderItem` function outside of the returned JSX. Also, ensure that it is wrapped in a `useCallback` hook to prevent it from being recreated each render.

For class components, move the `renderItem` function outside of the render function, so it won't recreate itself each time the render function is called.

tsx

```
const renderItem = useCallback(({item}) => (  
   <View key={item.key}>  
      <Text>{item.title}</Text>  
   </View>  
 ), []);  
  
return (  
  // ...  
  
  <FlatList data={items} renderItem={renderItem} />;  
  // ...  
);  

```

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/optimizing-flatlist-configuration.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/optimizing-flatlist-configuration.md)

Last updated on **Apr 14, 2025**

[Previous

Speeding up your Build phase](/docs/build-speed)[Next

Optimizing JavaScript loading](/docs/optimizing-javascript-loading)

* [Terms](#terms)* [Props](#props)
    + [removeClippedSubviews](#removeclippedsubviews)+ [maxToRenderPerBatch](#maxtorenderperbatch)+ [updateCellsBatchingPeriod](#updatecellsbatchingperiod)+ [initialNumToRender](#initialnumtorender)+ [windowSize](#windowsize)* [List items](#list-items)
      + [Use basic components](#use-basic-components)+ [Use light components](#use-light-components)+ [Use `memo()`](#use-memo)+ [Use cached optimized images](#use-cached-optimized-images)+ [Use getItemLayout](#use-getitemlayout)+ [Use keyExtractor or key](#use-keyextractor-or-key)+ [Avoid anonymous function on renderItem](#avoid-anonymous-function-on-renderitem)

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