Timers · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/timers)

* [Next](/docs/next/timers)* [0.79](/docs/timers)* [0.78](/docs/0.78/timers)* [0.77](/docs/0.77/timers)* [0.76](/docs/0.76/timers)* [0.75](/docs/0.75/timers)* [0.74](/docs/0.74/timers)* [0.73](/docs/0.73/timers)* [0.72](/docs/0.72/timers)* [0.71](/docs/0.71/timers)* [0.70](/docs/0.70/timers)* [All versions](/versions)

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

              * [JavaScript Runtime](/docs/javascript-environment)

                + [JavaScript Environment](/docs/javascript-environment)+ [Timers](/docs/timers)+ [Using Hermes](/docs/hermes)* [Codegen](/docs/the-new-architecture/what-is-codegen)

                  * [Native Development](/docs/native-platform)

                    * [Android and iOS guides](/docs/headless-js-android)

                      * [Legacy Architecture](/docs/legacy/native-modules-intro)

On this page

Timers
======

Timers are an important part of an application and React Native implements the [browser timers](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Timeouts_and_intervals).

Timers[​](#timers "Direct link to Timers")
------------------------------------------

* setTimeout, clearTimeout
* setInterval, clearInterval
* setImmediate, clearImmediate
* requestAnimationFrame, cancelAnimationFrame

`requestAnimationFrame(fn)` is not the same as `setTimeout(fn, 0)` - the former will fire after all the frames have flushed, whereas the latter will fire as quickly as possible (over 1000x per second on a iPhone 5S).

`setImmediate` is executed at the end of the current JavaScript execution block, right before sending the batched response back to native. Note that if you call `setImmediate` within a `setImmediate` callback, it will be executed right away, it won't yield back to native in between.

The `Promise` implementation uses `setImmediate` as its asynchronicity implementation.

note

When debugging on Android, if the times between the debugger and device have drifted; things such as animation, event behavior, etc., might not work properly or the results may not be accurate.
Please correct this by running `adb shell "date `date +%m%d%H%M%Y.%S%3N`"` on your debugger machine. Root access is required for the use in real device.

InteractionManager[​](#interactionmanager "Direct link to InteractionManager")
------------------------------------------------------------------------------

One reason why well-built native apps feel so smooth is by avoiding expensive operations during interactions and animations. In React Native, we currently have a limitation that there is only a single JS execution thread, but you can use `InteractionManager` to make sure long-running work is scheduled to start after any interactions/animations have completed.

Applications can schedule tasks to run after interactions with the following:

tsx

```
InteractionManager.runAfterInteractions(() => {  
  // ...long-running synchronous task...  
});  

```

Compare this to other scheduling alternatives:

* requestAnimationFrame(): for code that animates a view over time.
* setImmediate/setTimeout/setInterval(): run code later, note this may delay animations.
* runAfterInteractions(): run code later, without delaying active animations.

The touch handling system considers one or more active touches to be an 'interaction' and will delay `runAfterInteractions()` callbacks until all touches have ended or been cancelled.

InteractionManager also allows applications to register animations by creating an interaction 'handle' on animation start, and clearing it upon completion:

tsx

```
const handle = InteractionManager.createInteractionHandle();  
// run animation... (`runAfterInteractions` tasks are queued)  
// later, on animation completion:  
InteractionManager.clearInteractionHandle(handle);  
// queued tasks run if all handles were cleared  

```

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/timers.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/timers.md)

Last updated on **Apr 14, 2025**

[Previous

JavaScript Environment](/docs/javascript-environment)[Next

Using Hermes](/docs/hermes)

* [Timers](#timers)* [InteractionManager](#interactionmanager)

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