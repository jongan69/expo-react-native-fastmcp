Communication between native and React Native · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/communication-android)

* [Next](/docs/next/communication-android)* [0.79](/docs/communication-android)* [0.78](/docs/0.78/communication-android)* [0.77](/docs/0.77/communication-android)* [0.76](/docs/0.76/communication-android)* [0.75](/docs/0.75/communication-android)* [0.74](/docs/0.74/communication-android)* [0.73](/docs/0.73/communication-android)* [0.72](/docs/0.72/communication-android)* [0.71](/docs/0.71/communication-android)* [0.70](/docs/0.70/communication-android)* [All versions](/versions)

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

                * [Codegen](/docs/the-new-architecture/what-is-codegen)

                  * [Native Development](/docs/native-platform)

                    * [Android and iOS guides](/docs/headless-js-android)

                      + Android

                        - [Headless JS](/docs/headless-js-android)- [Publishing to Google Play Store](/docs/signed-apk-android)- [Communication between native and React Native](/docs/communication-android)- [React Native Gradle Plugin](/docs/react-native-gradle-plugin)+ iOS

                          - [Linking Libraries](/docs/linking-libraries-ios)- [Running On Simulator](/docs/running-on-simulator-ios)- [Communication between native and React Native](/docs/communication-ios)- [App Extensions](/docs/app-extensions)- [Publishing to Apple App Store](/docs/publishing-to-app-store)* [Legacy Architecture](/docs/legacy/native-modules-intro)

On this page

Communication between native and React Native
=============================================

In [Integrating with Existing Apps guide](/docs/integration-with-existing-apps) and [Native UI Components guide](/docs/legacy/native-components-android) we learn how to embed React Native in a native component and vice versa. When we mix native and React Native components, we'll eventually find a need to communicate between these two worlds. Some ways to achieve that have been already mentioned in other guides. This article summarizes available techniques.

Introduction[​](#introduction "Direct link to Introduction")
------------------------------------------------------------

React Native is inspired by React, so the basic idea of the information flow is similar. The flow in React is one-directional. We maintain a hierarchy of components, in which each component depends only on its parent and its own internal state. We do this with properties: data is passed from a parent to its children in a top-down manner. If an ancestor component relies on the state of its descendant, one should pass down a callback to be used by the descendant to update the ancestor.

The same concept applies to React Native. As long as we are building our application purely within the framework, we can drive our app with properties and callbacks. But, when we mix React Native and native components, we need some specific, cross-language mechanisms that would allow us to pass information between them.

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

Properties are the most straightforward way of cross-component communication. So we need a way to pass properties both from native to React Native, and from React Native to native.

### Passing properties from native to React Native[​](#passing-properties-from-native-to-react-native "Direct link to Passing properties from native to React Native")

You can pass properties down to the React Native app by providing a custom implementation of `ReactActivityDelegate` in your main activity. This implementation should override `getLaunchOptions` to return a `Bundle` with the desired properties.

* Java* Kotlin

java

```
public class MainActivity extends ReactActivity {  
  @Override  
  protected ReactActivityDelegate createReactActivityDelegate() {  
    return new ReactActivityDelegate(this, getMainComponentName()) {  
      @Override  
      protected Bundle getLaunchOptions() {  
        Bundle initialProperties = new Bundle();  
        ArrayList<String> imageList = new ArrayList<String>(Arrays.asList(  
                "https://dummyimage.com/600x400/ffffff/000000.png",  
                "https://dummyimage.com/600x400/000000/ffffff.png"  
        ));  
        initialProperties.putStringArrayList("images", imageList);  
        return initialProperties;  
      }  
    };  
  }  
}  

```

kotlin

```
class MainActivity : ReactActivity() {  
    override fun createReactActivityDelegate(): ReactActivityDelegate {  
        return object : ReactActivityDelegate(this, mainComponentName) {  
            override fun getLaunchOptions(): Bundle {  
                val imageList = arrayListOf("https://dummyimage.com/600x400/ffffff/000000.png", "https://dummyimage.com/600x400/000000/ffffff.png")  
                val initialProperties = Bundle().apply { putStringArrayList("images", imageList) }  
                return initialProperties  
            }  
        }  
    }  
}  

```

tsx

```
import React from 'react';  
import {View, Image} from 'react-native';  
  
export default class ImageBrowserApp extends React.Component {  
  renderImage(imgURI) {  
    return <Image source={{uri: imgURI}} />;  
  }  
  render() {  
    return <View>{this.props.images.map(this.renderImage)}</View>;  
  }  
}  

```

`ReactRootView` provides a read-write property `appProperties`. After `appProperties` is set, the React Native app is re-rendered with new properties. The update is only performed when the new updated properties differ from the previous ones.

* Java* Kotlin

java

```
Bundle updatedProps = mReactRootView.getAppProperties();  
ArrayList<String> imageList = new ArrayList<String>(Arrays.asList(  
        "https://dummyimage.com/600x400/ff0000/000000.png",  
        "https://dummyimage.com/600x400/ffffff/ff0000.png"  
));  
updatedProps.putStringArrayList("images", imageList);  
  
mReactRootView.setAppProperties(updatedProps);  

```

kotlin

```
var updatedProps: Bundle = reactRootView.getAppProperties()  
var imageList = arrayListOf("https://dummyimage.com/600x400/ff0000/000000.png", "https://dummyimage.com/600x400/ffffff/ff0000.png")  

```

It is fine to update properties anytime. However, updates have to be performed on the main thread. You use the getter on any thread.

There is no way to update only a few properties at a time. We suggest that you build it into your own wrapper instead.

> ***Note:*** Currently, JS function `componentWillUpdateProps` of the top level RN component will not be called after a prop update. However, you can access the new props in `componentDidMount` function.

### Passing properties from React Native to native[​](#passing-properties-from-react-native-to-native "Direct link to Passing properties from React Native to native")

The problem exposing properties of native components is covered in detail in [this article](/docs/legacy/native-components-android#3-expose-view-property-setters-using-reactprop-or-reactpropgroup-annotation). In short, properties that are to be reflected in JavaScript needs to be exposed as setter method annotated with `@ReactProp`, then use them in React Native as if the component was an ordinary React Native component.

### Limits of properties[​](#limits-of-properties "Direct link to Limits of properties")

The main drawback of cross-language properties is that they do not support callbacks, which would allow us to handle bottom-up data bindings. Imagine you have a small RN view that you want to be removed from the native parent view as a result of a JS action. There is no way to do that with props, as the information would need to go bottom-up.

Although we have a flavor of cross-language callbacks ([described here](/docs/legacy/native-modules-android#callbacks)), these callbacks are not always the thing we need. The main problem is that they are not intended to be passed as properties. Rather, this mechanism allows us to trigger a native action from JS, and handle the result of that action in JS.

Other ways of cross-language interaction (events and native modules)[​](#other-ways-of-cross-language-interaction-events-and-native-modules "Direct link to Other ways of cross-language interaction (events and native modules)")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

As stated in the previous chapter, using properties comes with some limitations. Sometimes properties are not enough to drive the logic of our app and we need a solution that gives more flexibility. This chapter covers other communication techniques available in React Native. They can be used for internal communication (between JS and native layers in RN) as well as for external communication (between RN and the 'pure native' part of your app).

React Native enables you to perform cross-language function calls. You can execute custom native code from JS and vice versa. Unfortunately, depending on the side we are working on, we achieve the same goal in different ways. For native - we use events mechanism to schedule an execution of a handler function in JS, while for React Native we directly call methods exported by native modules.

### Calling React Native functions from native (events)[​](#calling-react-native-functions-from-native-events "Direct link to Calling React Native functions from native (events)")

Events are described in detail in [this article](/docs/legacy/native-components-android#events). Note that using events gives us no guarantees about execution time, as the event is handled on a separate thread.

Events are powerful, because they allow us to change React Native components without needing a reference to them. However, there are some pitfalls that you can fall into while using them:

* As events can be sent from anywhere, they can introduce spaghetti-style dependencies into your project.
* Events share namespace, which means that you may encounter some name collisions. Collisions will not be detected statically, which makes them hard to debug.
* If you use several instances of the same React Native component and you want to distinguish them from the perspective of your event, you'll likely need to introduce identifiers and pass them along with events (you can use the native view's `reactTag` as an identifier).

### Calling native functions from React Native (native modules)[​](#calling-native-functions-from-react-native-native-modules "Direct link to Calling native functions from React Native (native modules)")

Native modules are Java/Kotlin classes that are available in JS. Typically one instance of each module is created per JS bridge. They can export arbitrary functions and constants to React Native. They have been covered in detail in [this article](/docs/legacy/native-modules-android).

> ***Warning***: All native modules share the same namespace. Watch out for name collisions when creating new ones.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/communication-android.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/communication-android.md)

Last updated on **Apr 14, 2025**

[Previous

Publishing to Google Play Store](/docs/signed-apk-android)[Next

React Native Gradle Plugin](/docs/react-native-gradle-plugin)

* [Introduction](#introduction)* [Properties](#properties)
    + [Passing properties from native to React Native](#passing-properties-from-native-to-react-native)+ [Passing properties from React Native to native](#passing-properties-from-react-native-to-native)+ [Limits of properties](#limits-of-properties)* [Other ways of cross-language interaction (events and native modules)](#other-ways-of-cross-language-interaction-events-and-native-modules)
      + [Calling React Native functions from native (events)](#calling-react-native-functions-from-native-events)+ [Calling native functions from React Native (native modules)](#calling-native-functions-from-react-native-native-modules)

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