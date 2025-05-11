Animation - Expo Documentation

[Docs](/)

[Blog](https://expo.dev/blog)[Changelog](https://expo.dev/changelog)[Star Us on GitHub](https://github.com/expo/expo)

Search

[Home](/)[Guides](/guides/overview)[EAS](/eas)[Reference](/versions/latest)[Learn](/tutorial/overview)

Get started

[Introduction](/get-started/introduction)[Create a project](/get-started/create-a-project)[Set up your environment](/get-started/set-up-your-environment)[Start developing](/get-started/start-developing)[Next steps](/get-started/next-steps)

Develop

[Tools for development](/develop/tools)

Navigation

User interface

[Splash screen and app icon](/develop/user-interface/splash-screen-and-app-icon)[Safe areas](/develop/user-interface/safe-areas)[System bars](/develop/user-interface/system-bars)[Fonts](/develop/user-interface/fonts)[Assets](/develop/user-interface/assets)[Color themes](/develop/user-interface/color-themes)[Animation](/develop/user-interface/animation)[Store data](/develop/user-interface/store-data)[Next steps](/develop/user-interface/next-steps)

Development builds

Config plugins

Debugging

[Authentication](/develop/authentication)[Unit testing](/develop/unit-testing)

Review

[Distributing apps for review](/review/overview)[Share previews with your team](/review/share-previews-with-your-team)[Open updates with Orbit](/review/with-orbit)

Deploy

[Build project for app stores](/deploy/build-project)[Submit to app stores](/deploy/submit-to-app-stores)[App stores metadata](/deploy/app-stores-metadata)[Send over-the-air updates](/deploy/send-over-the-air-updates)[Deploy web apps](/deploy/web)

Monitor

[Monitoring services](/monitoring/services)

More

[Core concepts](/core-concepts)[FAQ](/faq)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Animation
=========

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/user-interface/animation.mdx)

Learn how to integrate React Native animations and use it in your Expo project.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/user-interface/animation.mdx)

---

Animations are a great way to enhance and provide a better user experience. In your Expo projects, you can use the [Animated API](https://reactnative.dev/docs/next/animations) from React Native. However, if you want to use more advanced animations with better performance, you can use the [`react-native-reanimated`](https://docs.swmansion.com/react-native-reanimated/) library. It provides an API that simplifies the process of creating smooth, powerful, and maintainable animations.

Installation
------------

You can skip installing `react-native-reanimated` if you have created a project using [the default template](/get-started/create-a-project). This library is already installed. Otherwise, install it by running the following command:

Terminal

Copy

`-Â``npx expo install react-native-reanimated`

Usage
-----

### Minimal example

The following example shows how to use the `react-native-reanimated` library to create a simple animation. For more information on the API and advanced usage, see [`react-native-reanimated` documentation](https://docs.swmansion.com/react-native-reanimated/docs/fundamentals/your-first-animation).

Using react-native-reanimated

Copy

Open in Snack

```
import Animated, {
  useSharedValue,
  withTiming,
  useAnimatedStyle,
  Easing,
} from 'react-native-reanimated';
import { View, Button, StyleSheet } from 'react-native';

export default function AnimatedStyleUpdateExample() {
  const randomWidth = useSharedValue(10);

  const config = {
    duration: 500,
    easing: Easing.bezier(0.5, 0.01, 0, 1),
  };

  const style = useAnimatedStyle(() => {
    return {
      width: withTiming(randomWidth.value, config),
    };
  });

  return (
    <View style={styles.container}>
      <Animated.View style={[styles.box, style]} />
      <Button
        title="toggle"
        onPress={() => {
          randomWidth.value = Math.random() * 350;
        }}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  box: {
    width: 100,
    height: 80,
    backgroundColor: 'black',
    margin: 30,
  },
});

```

Other animation libraries
-------------------------

You can use other animation packages such as [Moti](https://moti.fyi/) in your Expo project. It works on Android, iOS, and web.

[Previous (Develop - User interface)

Color themes](/develop/user-interface/color-themes)[Next (Develop - User interface)

Store data](/develop/user-interface/store-data)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/user-interface/animation.mdx)
* Last updated on December 18, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Installation](/develop/user-interface/animation/#installation)[Usage](/develop/user-interface/animation/#usage)[Minimal example](/develop/user-interface/animation/#minimal-example)[Other animation libraries](/develop/user-interface/animation/#other-animation-libraries)