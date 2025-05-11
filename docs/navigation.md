Navigating Between Screens · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/navigation)

* [Next](/docs/next/navigation)* [0.79](/docs/navigation)* [0.78](/docs/0.78/navigation)* [0.77](/docs/0.77/navigation)* [0.76](/docs/0.76/navigation)* [0.75](/docs/0.75/navigation)* [0.74](/docs/0.74/navigation)* [0.73](/docs/0.73/navigation)* [0.72](/docs/0.72/navigation)* [0.71](/docs/0.71/navigation)* [0.70](/docs/0.70/navigation)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [The Basics](/docs/getting-started)

  * [Environment setup](/docs/environment-setup)

    * [Workflow](/docs/running-on-device)

      * [UI & Interaction](/docs/style)

        + [Style](/docs/style)+ [Height and Width](/docs/height-and-width)+ [Layout with Flexbox](/docs/flexbox)+ [Images](/docs/images)+ [Color Reference](/docs/colors)+ Interaction

                    - [Handling Touches](/docs/handling-touches)- [Navigating Between Screens](/docs/navigation)- [Animations](/docs/animations)- [Gesture Responder System](/docs/gesture-responder-system)+ Connectivity

                      - [Networking](/docs/network)- [Security](/docs/security)+ Inclusion

                        - [Accessibility](/docs/accessibility)* [Debugging](/docs/debugging)

          * [Testing](/docs/testing-overview)

            * [Performance](/docs/performance)

              * [JavaScript Runtime](/docs/javascript-environment)

                * [Codegen](/docs/the-new-architecture/what-is-codegen)

                  * [Native Development](/docs/native-platform)

                    * [Android and iOS guides](/docs/headless-js-android)

                      * [Legacy Architecture](/docs/legacy/native-modules-intro)

On this page

Navigating Between Screens
==========================

Mobile apps are rarely made up of a single screen. Managing the presentation of, and transition between, multiple screens is typically handled by what is known as a navigator.

This guide covers the various navigation components available in React Native. If you are getting started with navigation, you will probably want to use [React Navigation](/docs/navigation#react-navigation). React Navigation provides a straightforward navigation solution, with the ability to present common stack navigation and tabbed navigation patterns on both Android and iOS.

If you're integrating React Native into an app that already manages navigation natively, or looking for an alternative to React Navigation, the following library provides native navigation on both platforms: [react-native-navigation](https://github.com/wix/react-native-navigation).

React Navigation[​](#react-navigation "Direct link to React Navigation")
------------------------------------------------------------------------

The community solution to navigation is a standalone library that allows developers to set up the screens of an app with a few lines of code.

### Installation and setup[​](#installation-and-setup "Direct link to Installation and setup")

First, you need to install them in your project:

shell

```
npm install @react-navigation/native @react-navigation/native-stack  

```

Next, install the required peer dependencies. You need to run different commands depending on whether your project is an Expo managed project or a bare React Native project.

* If you have an Expo managed project, install the dependencies with `expo`:

  shell

  ```
  npx expo install react-native-screens react-native-safe-area-context  

  ```
* If you have a bare React Native project, install the dependencies with `npm`:

  shell

  ```
  npm install react-native-screens react-native-safe-area-context  

  ```

  For iOS with bare React Native project, make sure you have [CocoaPods](https://cocoapods.org/) installed. Then install the pods to complete the installation:

  shell

  ```
  cd ios  
  pod install  
  cd ..  

  ```

note

You might get warnings related to peer dependencies after installation. They are usually caused by incorrect version ranges specified in some packages. You can safely ignore most warnings as long as your app builds.

Now, you need to wrap the whole app in `NavigationContainer`. Usually you'd do this in your entry file, such as `index.js` or `App.js`:

tsx

```
import * as React from 'react';  
import {NavigationContainer} from '@react-navigation/native';  
  
const App = () => {  
  return (  
    <NavigationContainer>  
      {/* Rest of your app code */}  
    </NavigationContainer>  
  );  
};  
  
export default App;  

```

Now you are ready to build and run your app on the device/simulator.

### Usage[​](#usage "Direct link to Usage")

Now you can create an app with a home screen and a profile screen:

tsx

```
import * as React from 'react';  
import {NavigationContainer} from '@react-navigation/native';  
import {createNativeStackNavigator} from '@react-navigation/native-stack';  
  
const Stack = createNativeStackNavigator();  
  
const MyStack = () => {  
  return (  
    <NavigationContainer>  
      <Stack.Navigator>  
        <Stack.Screen  
          name="Home"  
          component={HomeScreen}  
          options={{title: 'Welcome'}}  
        />  
        <Stack.Screen name="Profile" component={ProfileScreen} />  
      </Stack.Navigator>  
    </NavigationContainer>  
  );  
};  

```

In this example, there are 2 screens (`Home` and `Profile`) defined using the `Stack.Screen` component. Similarly, you can define as many screens as you like.

You can set options such as the screen title for each screen in the `options` prop of `Stack.Screen`.

Each screen takes a `component` prop that is a React component. Those components receive a prop called `navigation` which has various methods to link to other screens. For example, you can use `navigation.navigate` to go to the `Profile` screen:

tsx

```
const HomeScreen = ({navigation}) => {  
  return (  
    <Button  
      title="Go to Jane's profile"  
      onPress={() =>  
        navigation.navigate('Profile', {name: 'Jane'})  
      }  
    />  
  );  
};  
const ProfileScreen = ({navigation, route}) => {  
  return <Text>This is {route.params.name}'s profile</Text>;  
};  

```

This `native-stack` navigator uses the native APIs: `UINavigationController` on iOS and `Fragment` on Android so that navigation built with `createNativeStackNavigator` will behave the same and have the same performance characteristics as apps built natively on top of those APIs.

React Navigation also has packages for different kind of navigators such as tabs and drawer. You can use them to implement various patterns in your app.

For a complete intro to React Navigation, follow the [React Navigation Getting Started Guide](https://reactnavigation.org/docs/getting-started).

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/navigation.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/navigation.md)

Last updated on **Apr 14, 2025**

[Previous

Handling Touches](/docs/handling-touches)[Next

Animations](/docs/animations)

* [React Navigation](#react-navigation)
  + [Installation and setup](#installation-and-setup)+ [Usage](#usage)

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