Learn the Basics · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/tutorial)

* [Next](/docs/next/tutorial)* [0.79](/docs/tutorial)* [0.78](/docs/0.78/tutorial)* [0.77](/docs/0.77/tutorial)* [0.76](/docs/0.76/tutorial)* [0.75](/docs/0.75/tutorial)* [0.74](/docs/0.74/tutorial)* [0.73](/docs/0.73/tutorial)* [0.72](/docs/0.72/tutorial)* [0.71](/docs/0.71/tutorial)* [0.70](/docs/0.70/tutorial)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

On this page

Learn the Basics
================

React Native is like React, but it uses native components instead of web components as building blocks. So to understand the basic structure of a React Native app, you need to understand some of the basic React concepts, like JSX, components, `state`, and `props`. If you already know React, you still need to learn some React Native specific stuff, like the native components. This tutorial is aimed at all audiences, whether you have React experience or not.

Let's do this thing.

Hello World[​](#hello-world "Direct link to Hello World")
---------------------------------------------------------

In accordance with the ancient traditions of our people, we must first build an app that does nothing except say "Hello, world!". Here it is:

If you are feeling curious, you can play around with sample code directly in the web simulators. You can also paste it into your `App.js` file to create a real app on your local machine.

What's going on here?[​](#whats-going-on-here "Direct link to What's going on here?")
-------------------------------------------------------------------------------------

1. First of all, we need to import `React` to be able to use `JSX`, which will then be transformed to the native components of each platform.
2. On line 2, we import the `Text` and `View` components from `react-native`

Then we define the `HelloWorldApp` function, which is a [functional component](https://reactjs.org/docs/components-and-props.html#function-and-class-components) and behaves in the same way as in React for the web. This function returns a `View` component with some styles and a`Text` as its child.

The `Text` component allows us to render a text, while the `View` component renders a container. This container has several styles applied, let's analyze what each one is doing.

The first style that we find is `flex: 1`, the [`flex`](/docs/layout-props#flex) prop will define how your items are going to "fill" over the available space along your main axis. Since we only have one container, it will take all the available space of the parent component. In this case, it is the only component, so it will take all the available screen space.

The following style is [`justifyContent`](/docs/layout-props#justifycontent): "center". This aligns children of a container in the center of the container's main axis. Finally, we have [`alignItems`](/docs/layout-props#alignitems): "center", which aligns children of a container in the center of the container's cross axis.

Some of the things in here might not look like JavaScript to you. Don't panic. *This is the future*.

First of all, ES2015 (also known as ES6) is a set of improvements to JavaScript that is now part of the official standard, but not yet supported by all browsers, so often it isn't used yet in web development. React Native ships with ES2015 support, so you can use this stuff without worrying about compatibility. `import`, `export`, `const` and `from` in the example above are all ES2015 features. If you aren't familiar with ES2015, you can probably pick it up by reading through sample code like this tutorial has. If you want, [this page](https://babeljs.io/learn-es2015/) has a good overview of ES2015 features.

The other unusual thing in this code example is `<View><Text>Hello world!</Text></View>`. This is JSX - a syntax for embedding XML within JavaScript. Many frameworks use a specialized templating language which lets you embed code inside markup language. In React, this is reversed. JSX lets you write your markup language inside code. It looks like HTML on the web, except instead of web things like `<div>` or `<span>`, you use React components. In this case, `<Text>` is a [Core Component](/docs/intro-react-native-components) that displays some text and `View` is like the `<div>` or `<span>`.

Components[​](#components "Direct link to Components")
------------------------------------------------------

So this code is defining `HelloWorldApp`, a new `Component`. When you're building a React Native app, you'll be making new components a lot. Anything you see on the screen is some sort of component.

Props[​](#props "Direct link to Props")
---------------------------------------

Most components can be customized when they are created, with different parameters. These creation parameters are called props.

Your own components can also use `props`. This lets you make a single component that is used in many different places in your app, with slightly different properties in each place. Refer to `props.YOUR_PROP_NAME` in your functional components or `this.props.YOUR_PROP_NAME` in your class components. Here's an example:

* TypeScript* JavaScript

Using `name` as a prop lets us customize the `Greeting` component, so we can reuse that component for each of our greetings. This example also uses the `Greeting` component in JSX. The power to do this is what makes React so cool.

The other new thing going on here is the [`View`](/docs/view) component. A [`View`](/docs/view) is useful as a container for other components, to help control style and layout.

With `props` and the basic [`Text`](/docs/text), [`Image`](/docs/image), and [`View`](/docs/view) components, you can build a wide variety of static screens. To learn how to make your app change over time, you need to [learn about State](#state).

State[​](#state "Direct link to State")
---------------------------------------

Unlike props [that are read-only](https://reactjs.org/docs/components-and-props.html#props-are-read-only) and should not be modified, the `state` allows React components to change their output over time in response to user actions, network responses and anything else.

#### What's the difference between state and props in React?[​](#whats-the-difference-between-state-and-props-in-react "Direct link to What's the difference between state and props in React?")

In a React component, the props are the variables that we pass from a parent component to a child component. Similarly, the state are also variables, with the difference that they are not passed as parameters, but rather that the component initializes and manages them internally.

#### Are there differences between React and React Native to handle the state?[​](#are-there-differences-between-react-and-react-native-to-handle-the-state "Direct link to Are there differences between React and React Native to handle the state?")

tsx

```
// ReactJS Counter Example using Hooks!  
  
import React, {useState} from 'react';  
  
  
  
const App = () => {  
  const [count, setCount] = useState(0);  
  
  return (  
    <div className="container">  
      <p>You clicked {count} times</p>  
      <button  
        onClick={() => setCount(count + 1)}>  
        Click me!  
      </button>  
    </div>  
  );  
};  
  
  
// CSS  
.container {  
  display: flex;  
  justify-content: center;  
  align-items: center;  
}  
  

```

tsx

```
// React Native Counter Example using Hooks!  
  
import React, {useState} from 'react';  
import {View, Text, Button, StyleSheet} from 'react-native';  
  
const App = () => {  
  const [count, setCount] = useState(0);  
  
  return (  
    <View style={styles.container}>  
      <Text>You clicked {count} times</Text>  
      <Button  
        onPress={() => setCount(count + 1)}  
        title="Click me!"  
      />  
    </View>  
  );  
};  
  
// React Native Styles  
const styles = StyleSheet.create({  
  container: {  
    flex: 1,  
    justifyContent: 'center',  
    alignItems: 'center',  
  },  
});  

```

As shown above, there is no difference in handling the `state` between [React](https://reactjs.org/docs/state-and-lifecycle.html) and `React Native`. You can use the state of your components both in classes and in functional components using [hooks](https://reactjs.org/docs/hooks-intro.html)!

In the following example we will show the same above counter example using classes.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/tutorial.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/tutorial.md)

Last updated on **Apr 14, 2025**

* [Hello World](#hello-world)* [What's going on here?](#whats-going-on-here)* [Components](#components)* [Props](#props)* [State](#state)

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