View Flattening · React Native

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

View Flattening
===============

caution

This document refers to the [New Architecture](/architecture/fabric-renderer), that is in active roll-out.

#### View Flattening is an optimization by the React Native renderer to avoid deep layout trees.[​](#view-flattening-is-an-optimization-by-the-react-native-renderer-to-avoid-deep-layout-trees "Direct link to View Flattening is an optimization by the React Native renderer to avoid deep layout trees.")

The React API is designed to be declarative and reusable through composition. This provides a great model for intuitive development. However, in implementation, these qualities of the API lead to the creation of deep [React Element Trees](/architecture/glossary#react-element-tree-and-react-element), where a large majority of React Element Nodes only affect the layout of a View and don’t render anything on the screen. We call these types of nodes **“Layout-Only”** Nodes.

Conceptually, each of the Nodes of the React Element Tree have a 1:1 relationship with a view on the screen, therefore rendering a deep React Element Tree that is composed by a large amount of “Layout-Only” Node leads to poor performance during rendering.

Here is a common use case that is affected by the cost of "Layout Only" views.

Imagine you want to render an image and a title that is handled by the `TitleComponent`, and you include this component as a child of the `ContainerComponent` that has some margin styles. After decomposing the components, the React code would look like this:

jsx

```
function MyComponent() {  
  return (  
    <View>                          // ReactAppComponent  
      <View style={{margin: 10}} /> // ContainerComponent  
        <View style={{margin: 10}}> // TitleComponent  
          <Image {...} />  
          <Text {...}>This is a title</Text>  
        </View>  
      </View>  
    </View>  
  );  
}  

```

As part of the render process, React Native will produce the following trees:

![Diagram one](/assets/images/diagram-one-3f2f9d7a2fa9d97b6b86fa3bd9b886d1.png)

Note that the Views (2) and (3) are “Layout Only” views, because they are rendered on the screen but they only render a `margin` of `10 px` on top of their children.

To improve the performance of these types of React Element Trees, the renderer implements a View Flattening mechanism that merges or flattens these types of Nodes, reducing the depth of the [host view](/architecture/glossary#host-view-tree-and-host-view) hierarchy that is rendered on the screen. This algorithm takes into consideration props like: `margin`, `padding`, `backgroundColor`, `opacity`, etc.

The View Flattening algorithm is integrated by design as part of the diffing stage of the renderer, which means that we don’t use extra CPU cycles to optimize the React Element Tree flattening these types of views. As the rest of the core, the View flattening algorithm is implemented in C++ and its benefits are shared by default on all supported platforms.

In the case of the previous example, the Views (2) and (3) would be flattened as part of the “diffing algorithm” and as a result their styles will be merged into the View (1):

![Diagram two](/assets/images/diagram-two-b87959980d29e4a303465a3d0ac82c73.png)

It is important to note that this optimization allows the renderer to avoid the creation and render of two host views. From the user’s perspective there are no visible changes on the screen.

[Edit this page](https://github.com/facebook/react-native-website/edit/main/docs/view-flattening.md)

Last updated on **Mar 10, 2022**

[Previous

Cross Platform Implementation](/architecture/xplat-implementation)[Next

Threading Model](/architecture/threading-model)

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