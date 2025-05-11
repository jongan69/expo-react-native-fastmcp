Threading Model · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [Architecture](/architecture/overview)

  + [Architecture Overview](/architecture/overview)+ [About the New Architecture](/architecture/landing-page)+ Rendering

        - [Fabric](/architecture/fabric-renderer)- [Render, Commit, and Mount](/architecture/render-pipeline)- [Cross Platform Implementation](/architecture/xplat-implementation)- [View Flattening](/architecture/view-flattening)- [Threading Model](/architecture/threading-model)+ Build Tools

          - [Bundled Hermes](/architecture/bundled-hermes)+ [Glossary](/architecture/glossary)

On this page

Threading Model
===============

caution

This document refers to the [New Architecture](/architecture/fabric-renderer), that is in active roll-out.

#### The React Native renderer distributes the work of the [render pipeline](/architecture/render-pipeline) across multiple threads.[​](#the-react-native-renderer-distributes-the-work-of-the-render-pipeline-across-multiple-threads "Direct link to the-react-native-renderer-distributes-the-work-of-the-render-pipeline-across-multiple-threads")

Here we define the threading model and provide some examples to illustrate thread usage of the render pipeline.

React Native renderer is designed to be thread safe. At a high level thread safety is guaranteed by using immutable data structures in the internals of the framework (enforced by C++ “const correctness” feature). This means that every update in React creates or clones new objects in the renderer instead of updating data structures. This allows the framework to expose thread safe and synchronous APIs to React.

The renderer uses two different threads:

* **UI thread** (often called main): The only thread that can manipulate host views.
* **JavaScript thread**: This is where React’s render phase, as well as layout, are executed.

Let’s review the supported scenarios of execution for each phase:

![Threading model symbols](/docs/assets/Architecture/threading-model/symbols.png)

Render Scenarios[​](#render-scenarios "Direct link to Render Scenarios")
------------------------------------------------------------------------

### Render in a JS Thread[​](#render-in-a-js-thread "Direct link to Render in a JS Thread")

This is the most common scenario where most of the render pipeline happens on JavaScript thread.

![Threading model use case one](/docs/assets/Architecture/threading-model/case-1.jpg)


---

### Render in the UI Thread[​](#render-in-the-ui-thread "Direct link to Render in the UI Thread")

When there is a high priority event on the UI Thread, the renderer is able to execute all the render pipeline synchronously on the UI thread.

![Threading model use case two](/docs/assets/Architecture/threading-model/case-2.jpg)


---

### Default or continuous event interruption[​](#default-or-continuous-event-interruption "Direct link to Default or continuous event interruption")

This scenario shows the interruption of the render phase by a low priority event in the UI thread. React and the React Native renderer are able to interrupt the render phase and merge its state with a low priority event that is executed on the UI thread. In this case the render process continues executing in the JS thread.

![Threading model use case three](/docs/assets/Architecture/threading-model/case-3.jpg)


---

### Discrete event interruption[​](#discrete-event-interruption "Direct link to Discrete event interruption")

The render phase is interruptible. This scenario shows the interruption of the render phase by a high priority event in the UI thread. React and the renderer are able to interrupt the render phase and merge its state with a high priority event that was executed on the UI thread. The render phase executes synchronously on the UI thread.

![Threading model use case four](/docs/assets/Architecture/threading-model/case-4.jpg)


---

### C++ State update[​](#c-state-update "Direct link to C++ State update")

Update originating on UI thread and skips rendering phase. See [React Native Renderer State Updates](/architecture/render-pipeline#react-native-renderer-state-updates) for more details.

![Threading model use case six](/docs/assets/Architecture/threading-model/case-6.jpg)

[Edit this page](https://github.com/facebook/react-native-website/edit/main/docs/threading-model.md)

Last updated on **Nov 8, 2023**

[Previous

View Flattening](/architecture/view-flattening)[Next

Bundled Hermes](/architecture/bundled-hermes)

* [Render Scenarios](#render-scenarios)
  + [Render in a JS Thread](#render-in-a-js-thread)+ [Render in the UI Thread](#render-in-the-ui-thread)+ [Default or continuous event interruption](#default-or-continuous-event-interruption)+ [Discrete event interruption](#discrete-event-interruption)+ [C++ State update](#c-state-update)

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