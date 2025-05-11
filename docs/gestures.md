Add gestures - Expo Documentation

[Docs](/)

[Blog](https://expo.dev/blog)[Changelog](https://expo.dev/changelog)[Star Us on GitHub](https://github.com/expo/expo)

Search

[Home](/)[Guides](/guides/overview)[EAS](/eas)[Reference](/versions/latest)[Learn](/tutorial/overview)

[Overview](/tutorial/overview)

Expo tutorial

0 of 9

[Introduction](/tutorial/introduction)[Create your first app](/tutorial/create-your-first-app)[Add navigation](/tutorial/add-navigation)[Build a screen](/tutorial/build-a-screen)[Use an image picker](/tutorial/image-picker)[Create a modal](/tutorial/create-a-modal)[Add gestures](/tutorial/gestures)[Take a screenshot](/tutorial/screenshot)[Handle platform differences](/tutorial/platform-differences)[Configure status bar, splash screen and app icon](/tutorial/configuration)[Learning resources](/tutorial/follow-up)

EAS tutorial

0 of 11

[Introduction](/tutorial/eas/introduction)[Configure development build](/tutorial/eas/configure-development-build)[Android development build](/tutorial/eas/android-development-build)[iOS development build for simulators](/tutorial/eas/ios-development-build-for-simulators)[iOS development build for devices](/tutorial/eas/ios-development-build-for-devices)[Multiple app variants](/tutorial/eas/multiple-app-variants)[Internal distribution build](/tutorial/eas/internal-distribution-builds)[Manage app versions](/tutorial/eas/manage-app-versions)[Android production build](/tutorial/eas/android-production-build)[iOS production build](/tutorial/eas/ios-production-build)[Share previews](/tutorial/eas/team-development)[Builds from GitHub](/tutorial/eas/using-github)[Next steps](/tutorial/eas/next-steps)

More

[Additional resources](/additional-resources)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Add gestures
============

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/tutorial/gestures.mdx)

In this tutorial, learn how to implement gestures from React Native Gesture Handler and Reanimated libraries.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/tutorial/gestures.mdx)

---

Gestures are a great way to provide an intuitive user experience in an app. The [React Native Gesture Handler](https://docs.swmansion.com/react-native-gesture-handler/docs/) library provides built-in native components that can handle gestures. It recognizes pan, tap, rotation, and other gestures using the platform's native touch handling system. In this chapter, we'll add two different gestures using this library:

* Double tap to scale the size of the emoji sticker and reduce the scale when double tapped again.
* Pan to move the emoji sticker around the screen so that the user can place the sticker anywhere on the image.

We'll also use the [Reanimated](https://docs.swmansion.com/react-native-reanimated/docs/fundamentals/handling-gestures/) library to animate between gesture states.

[![Watch: Adding gestures to your universal Expo app](https://i3.ytimg.com/vi/0q48LLvTGDU/maxresdefault.jpg)

Watch: Adding gestures to your universal Expo app](https://www.youtube.com/watch?v=0q48LLvTGDU)


---

1

Add GestureHandlerRootView
--------------------------

To get gesture interactions to work in the app, we'll render `<GestureHandlerRootView>` from `react-native-gesture-handler` at the top of `Index` component. Replace the root level `<View>` component in the app/(tabs)/index.tsx with `<GestureHandlerRootView>`.

app/(tabs)/index.tsx

Copy

```
// ... rest of the import statements remain same
import { GestureHandlerRootView } from 'react-native-gesture-handler';

export default function Index() {
  return (
    <GestureHandlerRootView style={styles.container}>
      {/* ...rest of the code remains */}
    </GestureHandlerRootView>
  )
}

```

2

Use animated components
-----------------------

An `Animated` component looks at the `style` prop of the component and determines which values to animate and apply updates to create an animation. Reanimated exports animated components such as `<Animated.View>`, `<Animated.Text>`, or `<Animated.ScrollView>`. We will apply animations to the `<Animated.Image>` component to make a double tap gesture work.

1. Open the EmojiSticker.tsx file in the components directory. Inside it, import `Animated` from the `react-native-reanimated` library to use animated components.
2. Replace the `Image` component with `<Animated.Image>`.

components/EmojiSticker.tsx

Copy

```
import { View } from 'react-native';
import Animated from 'react-native-reanimated';
import { type ImageSource } from 'expo-image';

type Props = {
  imageSize: number;
  stickerSource: ImageSource;
};

export default function EmojiSticker({ imageSize, stickerSource }: Props) {
  return (
    <View style={{ top: -350 }}>
      <Animated.Image
        source={stickerSource}
        resizeMode="contain"
        style={{ width: imageSize, height: imageSize }}
      />
    </View>
  );
}

```

> For a complete reference of the animated component API, see [React Native Reanimated](https://docs.swmansion.com/react-native-reanimated/docs/core/createAnimatedComponent) documentation.

3

Add a tap gesture
-----------------

React Native Gesture Handler allows us to add behavior when it detects touch input, like a double tap event.

In the EmojiSticker.tsx file:

1. Import `Gesture` and `GestureDetector` from `react-native-gesture-handler`.
2. To recognize the tap on the sticker, import `useAnimatedStyle`, `useSharedValue`, and `withSpring` from `react-native-reanimated` to animate the style of the `<Animated.Image>`.
3. Inside the `EmojiSticker` component, create a reference called `scaleImage` using the `useSharedValue()` hook. It will take the value of `imageSize` as its initial value.

components/EmojiSticker.tsx

Copy

```
// ...rest of the import statements remain same
import { Gesture, GestureDetector } from 'react-native-gesture-handler';
import Animated, { useAnimatedStyle, useSharedValue, withSpring } from 'react-native-reanimated';

export default function EmojiSticker({ imageSize, stickerSource }: Props) {
  const scaleImage = useSharedValue(imageSize);

  return (
    // ...rest of the code remains same
  )
}

```

Creating a shared value using the `useSharedValue()` hook has many advantages. It helps to mutate data and runs animations based on the current value. We can access and modify the shared value using the `.value` property. We'll create a `doubleTap` object to scale the initial value and use `Gesture.Tap()` to animate the transition while scaling the sticker image. To determine the number of taps required, we'll add `numberOfTaps()`.

Create the following object in the `EmojiSticker` component:

components/EmojiSticker.tsx

Copy

```
const doubleTap = Gesture.Tap()
  .numberOfTaps(2)
  .onStart(() => {
    if (scaleImage.value !== imageSize * 2) {
      scaleImage.value = scaleImage.value * 2;
    } else {
      scaleImage.value = Math.round(scaleImage.value / 2);
    }
  });

```

To animate the transition, let's use a spring-based animation. This will make it feel alive because it's based on the real-world physics of a spring. We will use the `withSpring()` function provided by `react-native-reanimated`.

On the sticker image, we'll use the `useAnimatedStyle()` hook to create a style object. This will help us to update styles using shared values when the animation happens. We'll also scale the size of the image by manipulating the `width` and `height` properties. The initial values of these properties are set to `imageSize`.

Create an `imageStyle` variable and add it to the `EmojiSticker` component:

components/EmojiSticker.tsx

Copy

```
const imageStyle = useAnimatedStyle(() => {
  return {
    width: withSpring(scaleImage.value),
    height: withSpring(scaleImage.value),
  };
});

```

Next, wrap the `<Animated.Image>` component with the `<GestureDetector>` and modify the `style` prop on the `<Animated.Image>` to pass the `imageStyle`.

components/EmojiSticker.tsx

Copy

```
import { View } from 'react-native';
import { Gesture, GestureDetector } from 'react-native-gesture-handler';
import Animated, { useAnimatedStyle, useSharedValue, withSpring } from 'react-native-reanimated';
import { type ImageSource } from 'expo-image';

type Props = {
  imageSize: number;
  stickerSource: ImageSource;
};

export default function EmojiSticker({ imageSize, stickerSource }: Props) {
  const scaleImage = useSharedValue(imageSize);

  const doubleTap = Gesture.Tap()
    .numberOfTaps(2)
    .onStart(() => {
      if (scaleImage.value !== imageSize * 2) {
        scaleImage.value = scaleImage.value * 2;
      } else {
        scaleImage.value = Math.round(scaleImage.value / 2);
      }
    });

  const imageStyle = useAnimatedStyle(() => {
    return {
      width: withSpring(scaleImage.value),
      height: withSpring(scaleImage.value),
    };
  });

  return (
    <View style={{ top: -350 }}>
      <GestureDetector gesture={doubleTap}>
        <Animated.Image
          source={stickerSource}
          resizeMode="contain"
          style={[imageStyle, { width: imageSize, height: imageSize }]}
        />
      </GestureDetector>
    </View>
  );
}

```

In the above snippet, the `gesture` prop takes the value of the `doubleTap` to trigger a gesture when a user double-taps the sticker image.

Let's take a look at our app on Android, iOS and the web:

> For a complete reference of the tap gesture API, see the [React Native Gesture Handler](https://docs.swmansion.com/react-native-gesture-handler/docs/gestures/tap-gesture) documentation.

4

Add a pan gesture
-----------------

To recognize a dragging gesture on the sticker and to track its movement, we'll use a pan gesture. In the components/EmojiSticker.tsx:

1. Create two new shared values: `translateX` and `translateY`.
2. Replace the `<View>` with the `<Animated.View>` component.

components/EmojiSticker.tsx

Copy

```
export default function EmojiSticker({ imageSize, stickerSource }: Props) {
  const scaleImage = useSharedValue(imageSize);
  const translateX = useSharedValue(0);
  const translateY = useSharedValue(0);
  // ...rest of the code remains same

  return (
    <Animated.View style={{ top: -350 }}>
      <GestureDetector gesture={doubleTap}>
        {/* ...rest of the code remains same */}
      </GestureDetector>
    </Animated.View>
  );
}

```

Let's learn what the above code does:

* The translation values defined will move the sticker around the screen. Since the sticker moves along both axes, we need to track the X and Y values.
* In the `useSharedValue()` hooks, we have set both translation variables to have an initial position of `0`. This is the sticker's initial position and a starting point. This value sets the sticker's initial position when the gesture starts.

In the previous step, we triggered the `onStart()` callback for the tap gesture chained to the `Gesture.Tap()` method. For the pan gesture, specify an `onChange()` callback, which runs when the gesture is active and moving.

1. Create a `drag` object to handle the pan gesture. The `onChange()` callback accepts `event` as a parameter. `changeX` and `changeY` properties hold the change in position since the last event. and update the values stored in `translateX` and `translateY`.
2. Define the `containerStyle` object using the `useAnimatedStyle()` hook. It will return an array of transforms. For the `<Animated.View>` component, we need to set the `transform` property to the `translateX` and `translateY` values. This will change the sticker's position when the gesture is active.

components/EmojiSticker.tsx

Copy

```
const drag = Gesture.Pan().onChange(event => {
  translateX.value += event.changeX;
  translateY.value += event.changeY;
});

const containerStyle = useAnimatedStyle(() => {
  return {
    transform: [
      {
        translateX: translateX.value,
      },
      {
        translateY: translateY.value,
      },
    ],
  };
});

```

Next, inside the JSX code:

1. Update the `<EmojiSticker>` component so that the `<GestureDetector>` component becomes the top-level component.
2. Add the `containerStyle` on the `<Animated.View>` component to apply the transform styles.

components/EmojiSticker.tsx

Copy

```
import { Gesture, GestureDetector } from 'react-native-gesture-handler';
import Animated, { useAnimatedStyle, useSharedValue, withSpring } from 'react-native-reanimated';
import { type ImageSource } from 'expo-image';

type Props = {
  imageSize: number;
  stickerSource: ImageSource;
};

export default function EmojiSticker({ imageSize, stickerSource }: Props) {
  const scaleImage = useSharedValue(imageSize);
  const translateX = useSharedValue(0);
  const translateY = useSharedValue(0);

  const doubleTap = Gesture.Tap()
    .numberOfTaps(2)
    .onStart(() => {
      if (scaleImage.value !== imageSize * 2) {
        scaleImage.value = scaleImage.value * 2;
      } else {
        scaleImage.value = Math.round(scaleImage.value / 2);
      }
    });

  const imageStyle = useAnimatedStyle(() => {
    return {
      width: withSpring(scaleImage.value),
      height: withSpring(scaleImage.value),
    };
  });

  const drag = Gesture.Pan().onChange(event => {
    translateX.value += event.changeX;
    translateY.value += event.changeY;
  });

  const containerStyle = useAnimatedStyle(() => {
    return {
      transform: [
        {
          translateX: translateX.value,
        },
        {
          translateY: translateY.value,
        },
      ],
    };
  });

  return (
    <GestureDetector gesture={drag}>
      <Animated.View style={[containerStyle, { top: -350 }]}>
        <GestureDetector gesture={doubleTap}>
          <Animated.Image
            source={stickerSource}
            resizeMode="contain"
            style={[imageStyle, { width: imageSize, height: imageSize }]}
          />
        </GestureDetector>
      </Animated.View>
    </GestureDetector>
  );
}

```

Let's take a look at our app on Android, iOS and the web:

Summary
-------

Chapter 6: Add gestures

We've successfully implemented pan and tap gestures.

Mark this chapter as read

In the next chapter, we'll learn how to take a screenshot of the image and the sticker, and save it on the device's library.

[Next: Take a screenshot](/tutorial/screenshot)

[Previous (Expo tutorial)

Create a modal](/tutorial/create-a-modal)[Next (Expo tutorial)

Take a screenshot](/tutorial/screenshot)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/tutorial/gestures.mdx)

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Add GestureHandlerRootView](/tutorial/gestures/#add-gesturehandlerrootview)[Use animated components](/tutorial/gestures/#use-animated-components)[Add a tap gesture](/tutorial/gestures/#add-a-tap-gesture)[Add a pan gesture](/tutorial/gestures/#add-a-pan-gesture)[Summary](/tutorial/gestures/#summary)