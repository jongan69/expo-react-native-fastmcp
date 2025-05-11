About the New Architecture · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.75](/docs/0.75/the-new-architecture/landing-page)

* [Next](/docs/next/getting-started)* [0.79](/docs/getting-started)* [0.78](/docs/0.78/getting-started)* [0.77](/docs/0.77/getting-started)* [0.76](/docs/0.76/getting-started)* [0.75](/docs/0.75/the-new-architecture/landing-page)* [0.74](/docs/0.74/the-new-architecture/landing-page)* [0.73](/docs/0.73/the-new-architecture/landing-page)* [0.72](/docs/0.72/the-new-architecture/landing-page)* [0.71](/docs/0.71/the-new-architecture/landing-page)* [0.70](/docs/0.70/the-new-architecture/landing-page)* [All versions](/versions)

[Development](#)

* [Guides](/docs/0.75/getting-started)* [Components](/docs/0.75/components-and-apis)* [APIs](/docs/0.75/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [The Basics](/docs/0.75/getting-started)

  * [Environment setup](/docs/0.75/environment-setup)

    * [Workflow](/docs/0.75/running-on-device)

      * [UI & Interaction](/docs/0.75/style)

        * [Debugging](/docs/0.75/debugging)

          * [Testing](/docs/0.75/testing-overview)

            * [Performance](/docs/0.75/performance)

              * [JavaScript Runtime](/docs/0.75/javascript-environment)

                * [Native Modules](/docs/0.75/native-modules-intro)

                  * [Native Components](/docs/0.75/native-components-android)

                    * [Android and iOS guides](/docs/0.75/headless-js-android)

                      * [New Architecture](/docs/0.75/the-new-architecture/landing-page)

                        + [About the New Architecture](/docs/0.75/the-new-architecture/landing-page)

This is documentation for React Native **0.75**, which is no longer in active development.

For up-to-date documentation, see the **[latest version](/docs/getting-started)** (0.79).

Version: 0.75

On this page

About the New Architecture
==========================

info

If you are looking for the New Architecture guides, they have moved to the [working group](https://github.com/reactwg/react-native-new-architecture#guides).

Since 2018, the React Native team has been redesigning the core internals of React Native to enable developers to create higher-quality experiences. As of 2024, this version of React Native has been proven at scale and powers production apps by Meta.

The term *New Architecture* refers to both the new framework architecture and the work to bring it to open source.

The New Architecture has been available for experimental opt-in as of [React Native 0.68](/blog/2022/03/30/version-068#opting-in-to-the-new-architecture) with continued improvements in every subsequent release. The team is now working to make this the default experience for the React Native open source ecosystem.

Why a New Architecture?[​](#why-a-new-architecture "Direct link to Why a New Architecture?")
--------------------------------------------------------------------------------------------

After many years of building with React Native, the team identified a set of limitations that prevented developers from crafting certain experiences with a high polish. These limitations were fundamental to the existing design of the framework, so the New Architecture started as an investment in the future of React Native.

The New Architecture unlocks capabilities and improvements that were impossible in the legacy architecture.

### Synchronous Layout and Effects[​](#synchronous-layout-and-effects "Direct link to Synchronous Layout and Effects")

Building adaptive UI experiences often requires measuring the size and position of your views and adjusting layout.

Today, you would use the [`onLayout`](/docs/view#onlayout) event to get the layout information of a view and make any adjustments. However, state updates within the `onLayout` callback may apply after painting the previous render. This means that users may see intermediate states or visual jumps between rendering the initial layout and responding to layout measurements.

With the New Architecture, we can avoid this issue entirely with synchronous access to layout information and properly scheduled updates such that no intermediate state is visible to users.

Example: Rendering a Tooltip

Measuring and placing a tooltip above a view allows us to showcase what synchronous rendering unlocks. The tooltip needs to know the position of its target view to determine where it should render.

In the current architecture, we use `onLayout` to get the measurements of the view and then update the positioning of the tooltip based on where the view is.

jsx

```
function ViewWithTooltip() {  
  // ...  
  
  // We get the layout information and pass to ToolTip to position itself  
  const onLayout = React.useCallback(event => {  
    targetRef.current?.measureInWindow((x, y, width, height) => {  
      // This state update is not guaranteed to run in the same commit  
      // This results in a visual "jump" as the ToolTip repositions itself  
      setTargetRect({x, y, width, height});  
    });  
  }, []);  
  
  return (  
    <>  
      <View ref={targetRef} onLayout={onLayout}>  
        <Text>Some content that renders a tooltip above</Text>  
      </View>  
      <Tooltip targetRect={targetRect} />  
    </>  
  );  
}  

```

With the New Architecture, we can use [`useLayoutEffect`](https://react.dev/reference/react/useLayoutEffect) to synchronously measure and apply layout updates in a single commit, avoiding the visual "jump".

jsx

```
function ViewWithTooltip() {  
  // ...  
  
  useLayoutEffect(() => {  
    // The measurement and state update for `targetRect` happens in a single commit  
    // allowing ToolTip to position itself without intermediate paints  
    targetRef.current?.measureInWindow((x, y, width, height) => {  
      setTargetRect({x, y, width, height});  
    });  
  }, [setTargetRect]);  
  
  return (  
    <>  
      <View ref={targetRef}>  
        <Text>Some content that renders a tooltip above</Text>  
      </View>  
      <Tooltip targetRect={targetRect} />  
    </>  
  );  
}  

```

![A view that is moving to the corners of the viewport and center with a tooltip rendered either above or below it. The tooltip is rendered after a short delay after the view moves](/img/new-architecture/async-on-layout.gif)

Asynchronous measurement and render of the ToolTip. [See code](https://gist.github.com/lunaleaps/eabd653d9864082ac1d3772dac217ab9).

![A view that is moving to the corners of the viewport and center with a tooltip rendered either above or below it. The view and tooltip move in unison.](/img/new-architecture/sync-use-layout-effect.gif)

Synchronous measurement and render of the ToolTip. [See code](https://gist.github.com/lunaleaps/148756563999c83220887757f2e549a3).

### Support for Concurrent Renderer and Features[​](#support-for-concurrent-renderer-and-features "Direct link to Support for Concurrent Renderer and Features")

The New Architecture supports concurrent rendering and features that have shipped in [React 18](https://react.dev/blog/2022/03/29/react-v18) and beyond. You can now use features like Suspense for data-fetching, Transitions, and other new React APIs in your React Native code, further conforming codebases and concepts between web and native React development.

The concurrent renderer also brings out-of-the-box improvements like automatic batching, which reduces re-renders in React.

Example: Automatic Batching

With the New Architecture, you'll get automatic batching with the React 18 renderer.

In this example, a slider specifies how many tiles to render. Dragging the slider from 0 to 1000 will fire off a quick succession of state updates and re-renders.

In comparing the renderers for the [same code](https://gist.github.com/lunaleaps/79bb6f263404b12ba57db78e5f6f28b2), you can visually notice the renderer provides a smoother UI, with less intermediate UI updates. State updates from native event handlers, like this native Slider component, are now batched.

![A video demonstrating an app rendering many views according to a slider input. The slider value is adjusted from 0 to 1000 and the UI slowly catches up to rendering 1000 views.](/img/new-architecture/legacy-renderer.gif)

Rendering frequent state updates with legacy renderer.

![A video demonstrating an app rendering many views according to a slider input. The slider value is adjusted from 0 to 1000 and the UI resolves to 1000 views faster than the previous example, without as many intermediate states.](/img/new-architecture/react18-renderer.gif)

Rendering frequent state updates with React 18 renderer.

New concurrent features, like [Transitions](https://react.dev/reference/react/useTransition), give you the power to express the priority of UI updates. Marking an update as lower priority tells React it can "interrupt" rendering the update to handle higher priority updates to ensure a responsive user experience where it matters.

Example: Using `startTransition`

We can build on the previous example to showcase how transitions can interrupt in-progress rendering to handle a newer state update.

We wrap the tile number state update with `startTransition` to indicate that rendering the tiles can be interrupted. `startTransition` also provides a `isPending` flag to tell us when the transition is complete.

jsx

```
function TileSlider({value, onValueChange}) {  
  const [isPending, startTransition] = useTransition();  
  
  return (  
    <>  
      <View>  
        <Text>  
          Render {value} Tiles  
        </Text>  
        <ActivityIndicator animating={isPending} />  
      </View>  
      <Slider  
        value={1}  
        minimumValue={1}  
        maximumValue={1000}  
        step={1}  
        onValueChange={newValue => {  
          startTransition(() => {  
            onValueChange(newValue);  
          });  
        }}  
      />  
    </>  
  );  
}  
  
function ManyTiles() {  
  const [value, setValue] = useState(1);  
  const tiles = generateTileViews(value);  
  return (  
      <TileSlider onValueChange={setValue} value={value} />  
      <View>  
        {tiles}  
      </View>  
  )  
}  

```

You'll notice that with the frequent updates in a transition, React renders fewer intermediate states because it bails out of rendering the state as soon as it becomes stale. In comparison, without transitions, more intermediate states are rendered. Both examples still use automatic batching. Still, transitions give even more power to developers to batch in-progress renders.

![A video demonstrating an app rendering many views (tiles) according to a slider input. The views are rendered in batches as the slider is quickly adjusted from 0 to 1000. There are less batch renders in comparison to the next video.](/img/new-architecture/with-transitions.gif)

Rendering tiles with transitions to interrupt in-progress renders of stale state. [See code](https://gist.github.com/lunaleaps/eac391bf3fe4c85953cefeb74031bab0/revisions).

![A video demonstrating an app rendering many views (tiles) according to a slider input. The views are rendered in batches as the slider is quickly adjusted from 0 to 1000.](/img/new-architecture/without-transitions.gif)

Rendering tiles without marking it as a transition. [See code](https://gist.github.com/lunaleaps/eac391bf3fe4c85953cefeb74031bab0/revisions).

### Fast JavaScript/Native Interfacing[​](#fast-javascriptnative-interfacing "Direct link to Fast JavaScript/Native Interfacing")

The New Architecture removes the [asynchronous bridge](https://reactnative.dev/blog/2018/06/14/state-of-react-native-2018#architecture) between JavaScript and native and replaces it with JavaScript Interface (JSI). JSI is an interface that allows JavaScript to hold a reference to a C++ object and vice-versa. With a memory reference, you can directly invoke methods without serialization costs.

JSI enables [VisionCamera](https://github.com/mrousavy/react-native-vision-camera), a popular camera library for React Native, to process frames in real time. Typical frame buffers are 10 MB, which amounts to roughly 1 GB of data per second, depending on the frame rate. In comparison with the serialization costs of the bridge, JSI handles that amount of interfacing data with ease. JSI can expose other complex instance-based types such as databases, images, audio samples, etc.

JSI adoption in the New Architecture removes this class of serialization work from all native-JavaScript interop. This includes initializing and re-rendering native core components like `View` and `Text`. You can read more about our [investigation in rendering performance](https://github.com/reactwg/react-native-new-architecture/discussions/123) in the New Architecture and the improved benchmarks we measured.

### Learn more[​](#learn-more "Direct link to Learn more")

To achieve this, the New Architecture had to refactor multiple parts of the React Native infrastructure. To learn more about the refactor and other benefits it brings, check out the [documentation](https://github.com/reactwg/react-native-new-architecture) in the New Architecture working group.

What can I expect from enabling the New Architecture?[​](#what-can-i-expect-from-enabling-the-new-architecture "Direct link to What can I expect from enabling the New Architecture?")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

While the New Architecture enables these features and improvements, enabling the New Architecture for your app or library may not immediately improve the performance or user experience.

For example, your code may need refactoring to leverage new capabilities like synchronous layout effects or concurrent features. Although JSI will minimize the overhead between JavaScript and native memory, data serialization may not have been a bottleneck for your app's performance.

Enabling the New Architecture in your app or library is opting into the future of React Native.

The team is actively researching and developing new capabilities the New Architecture unlocks. For example, web alignment is an active area of exploration at Meta that will ship to the React Native open source ecosystem.

* [Updates to the event loop model](https://github.com/react-native-community/discussions-and-proposals/blob/main/proposals/0744-well-defined-event-loop.md)
* [Node and layout APIs](https://github.com/react-native-community/discussions-and-proposals/blob/main/proposals/0607-dom-traversal-and-layout-apis.md)
* [Styling and layout conformance](https://github.com/facebook/yoga/releases/tag/v2.0.0)

You can follow along and contribute in our dedicated [discussions & proposals](https://github.com/react-native-community/discussions-and-proposals/discussions/651) repository.

Should I use the New Architecture today?[​](#should-i-use-the-new-architecture-today "Direct link to Should I use the New Architecture today?")
-----------------------------------------------------------------------------------------------------------------------------------------------

At [React Conf 2024](https://youtu.be/Q5SMmKb7qVI?feature=shared&t=1219), we announced that the React Native [New Architecture is now in Beta](https://github.com/reactwg/react-native-new-architecture/discussions/189).

We believe that the New Architecture is very close to be used in production.

Our guidance is as follows:

* For most production apps, we do *not* recommend enabling the New Architecture today. Waiting for the official release will offer the best experience.
* However, we do advise for you to plan for the migration and to start trying it out.
* If you maintain a React Native library, we recommend enabling it and verifying your use cases are covered. You can find the [instructions here](https://github.com/reactwg/react-native-new-architecture#guides).

### Enable the New Architecture[​](#enable-the-new-architecture "Direct link to Enable the New Architecture")

If you are interested in dogfooding the New Architecture experience, you can find [instructions](https://github.com/reactwg/react-native-new-architecture/blob/main/docs/enable-apps.md) in our dedicated working group. The [New Architecture working group](https://github.com/reactwg/react-native-new-architecture) is a dedicated space for support and coordination for New Architecture adoption and where the team posts regular updates.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/the-new-architecture/landing-page.md)[Edit page for 0.75 release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.75/the-new-architecture/landing-page.md)

Last updated on **Aug 15, 2024**

[Previous

Publishing to Apple App Store](/docs/0.75/publishing-to-app-store)

* [Why a New Architecture?](#why-a-new-architecture)
  + [Synchronous Layout and Effects](#synchronous-layout-and-effects)+ [Support for Concurrent Renderer and Features](#support-for-concurrent-renderer-and-features)+ [Fast JavaScript/Native Interfacing](#fast-javascriptnative-interfacing)+ [Learn more](#learn-more)* [What can I expect from enabling the New Architecture?](#what-can-i-expect-from-enabling-the-new-architecture)* [Should I use the New Architecture today?](#should-i-use-the-new-architecture-today)
      + [Enable the New Architecture](#enable-the-new-architecture)

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