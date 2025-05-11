Measuring the Layout · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/the-new-architecture/layout-measurements)

* [Next](/docs/next/the-new-architecture/layout-measurements)* [0.79](/docs/the-new-architecture/layout-measurements)* [0.78](/docs/0.78/the-new-architecture/layout-measurements)* [0.77](/docs/0.77/the-new-architecture/layout-measurements)* [0.76](/docs/0.76/the-new-architecture/layout-measurements)* [0.75](/docs/0.75/getting-started)* [0.74](/docs/0.74/getting-started)* [0.73](/docs/0.73/getting-started)* [0.72](/docs/0.72/getting-started)* [0.71](/docs/0.71/getting-started)* [0.70](/docs/0.70/getting-started)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

On this page

Measuring the Layout
====================

Sometimes, you need to measure the current layout to apply some changes to the overall layout or to make decisions and call some specific logic.

React Native provides some native methods to know what are the measurements of the views.

The best way to invoke those methods is in a `useLayoutEffect` hook: this will give you the most recent values for those measurements and it will let you apply changes in the same frame when the measurements are computed.

Typical code will look like this:

tsx

```
function AComponent(children) {  
  const targetRef = React.useRef(null)  
  
  useLayoutEffect(() => {  
    targetRef.current?.measure((x, y, width, height, pageX, pageY) => {  
      //do something with the measurements  
    });  
  }, [ /* add dependencies here */]);  
  
  return (  
    <View ref={targetRef}>  
     {children}  
    <View />  
  );  
}  

```

note

The methods described here are available on most of the default components provided by React Native. However, they are *not* available on composite components that aren't directly backed by a native view. This will generally include most components that you define in your own app.

measure(callback)[​](#measurecallback "Direct link to measure(callback)")
-------------------------------------------------------------------------

Determines the location on screen (`x` and `y`), `width`, and `height` in the viewport of the given view. Returns the values via an async callback. If successful, the callback will be called with the following arguments:

* `x`: the `x` coordinate of the origin (top-left corner) of the measured view in the viewport.
* `y`: the `y` coordinate of the origin (top-left corner) of the measured view in the viewport.
* `width`: the `width` of the view.
* `height`: the `height` of the view.
* `pageX`: the `x` coordinate of the view in the viewport (typically the whole screen).
* `pageY`: the `y` coordinate of the view in the viewport (typically the whole screen).

Also the `width` and `height` returned by `measure()` are the `width` and `height` of the component in the viewport.

measureInWindow(callback)[​](#measureinwindowcallback "Direct link to measureInWindow(callback)")
-------------------------------------------------------------------------------------------------

Determines the location (`x` and `y`) of the given view in the window and returns the values via an async callback. If the React root view is embedded in another native view, this will give you the absolute coordinates. If successful, the callback will be called with the following arguments:

* `x`: the `x` coordinate of the view in the current window.
* `y`: the `y` coordinate of the view in the current window.
* `width`: the `width` of the view.
* `height`: the `height` of the view.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/the-new-architecture/layout-measurements.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/the-new-architecture/layout-measurements.md)

Last updated on **Apr 14, 2025**

* [measure(callback)](#measurecallback)* [measureInWindow(callback)](#measureinwindowcallback)

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