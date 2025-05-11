Build a screen - Expo Documentation

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

Build a screen
==============

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/tutorial/build-a-screen.mdx)

In this tutorial, learn how to use components such as React Native's Pressable and Expo Image to build a screen.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/tutorial/build-a-screen.mdx)

---

In this chapter, we'll create the first screen of the StickerSmash app.

![Initial layout.](/static/images/tutorial/initial-layout.png)

The screen above displays an image and two buttons. The app user can select an image using one of the two buttons. The first button allows the user to select an image from their device. The second button allows the user to continue with a default image provided by the app.

Once the user selects an image, they can add a sticker to it. So, let's start creating this screen.

[![Watch: Building a screen in your universal Expo app](https://i3.ytimg.com/vi/3rcOP8xDwTQ/maxresdefault.jpg)

Watch: Building a screen in your universal Expo app](https://www.youtube.com/watch?v=3rcOP8xDwTQ)


---

1

Break down the screen
---------------------

Before we build this screen by writing code, let's break it down into some essential elements.

![Break down of initial layout.](/static/images/tutorial/breakdown-of-layout.png)

There are two essential elements:

* There is a large image displayed at the center of the screen
* There are two buttons in the bottom half of the screen

The first button contains multiple components. The parent element provides a yellow border, and contains an icon and text components inside a row.

![Break down of the button component with row.](/static/images/tutorial/breakdown-of-buttons.png)

Now that we've broken down the UI into smaller chunks, we're ready to start coding.

2

Display the image
-----------------

We'll use `expo-image` library to display the image in the app. It provides a cross-platform `<Image>` component to load and render an image.

Stop the development server by pressing `Ctrl` + `c` in the terminal. Then, install the `expo-image` library:

Terminal

Copy

`-Â``npx expo install expo-image`

The [`npx expo install`](/more/expo-cli#installation) command will install the library and add it to the project's dependencies in package.json.

The Image component takes the source of an image as its value. The source can be either a [static asset](https://reactnative.dev/docs/images#static-image-resources) or a URL. For example, the source required from assets/images directory is static. It can also come from [Network](https://reactnative.dev/docs/images#network-images) as a `uri` property.

![Background image that we are going to use as a placeholder for the tutorial.](/static/images/tutorial/background-image.png)

To use the Image component in app/(tabs)/index.tsx file:

1. Import `Image` from the `expo-image` library.
2. Create a `PlaceholderImage` variable to use assets/images/background-image.png file as the `source` prop on the `Image` component.

app/(tabs)/index.tsx

Copy

```
import { View, StyleSheet } from 'react-native';
import { Image } from 'expo-image';

const PlaceholderImage = require('@/assets/images/background-image.png');

export default function Index() {
  return (
    <View style={styles.container}>
      <View style={styles.imageContainer}>
        <Image source={PlaceholderImage} style={styles.image} />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#25292e',
    alignItems: 'center',
  },
  imageContainer: {
    flex: 1,
  },
  image: {
    width: 320,
    height: 440,
    borderRadius: 18,
  },
});

```

3

Divide components into files
----------------------------

Let's divide the code into multiple files as we add more components to this screen. Throughout this tutorial, we'll use the components directory to create custom components.

1. Create a top-level components directory, and inside it, create the ImageViewer.tsx file.
2. Move the code to display the image in this file along with the `image` styles.

components/ImageViewer.tsx

Copy

```
import { StyleSheet } from 'react-native';
import { Image, type ImageSource } from 'expo-image';

type Props = {
  imgSource: ImageSource;
};

export default function ImageViewer({ imgSource }: Props) {
  return <Image source={imgSource} style={styles.image} />;
}

const styles = StyleSheet.create({
  image: {
    width: 320,
    height: 440,
    borderRadius: 18,
  },
});

```

> Since ImageViewer is a custom component, we are placing it in a separate directory instead of the app directory. Every file inside app directory is either a layout file or a route file. For more information, see [Non-navigation components live outside of app directory](/router/basics/core-concepts#5-non-navigation-components-live-outside-of-app-directory).

Import `ImageViewer` and use it in the app/(tabs)/index.tsx:

app/(tabs)/index.tsx

Copy

```
import { StyleSheet, View } from 'react-native';

import ImageViewer from '@/components/ImageViewer';

const PlaceholderImage = require('@/assets/images/background-image.png');

export default function Index() {
  return (
    <View style={styles.container}>
      <View style={styles.imageContainer}>
        <ImageViewer imgSource={PlaceholderImage} />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#25292e',
    alignItems: 'center',
  },
  imageContainer: {
    flex: 1,
  },
});

```

What is the `@` in import statement?

The `@` symbol is a custom [path alias](/guides/typescript#path-aliases-optional) for importing custom components and other modules instead of relative paths. Expo CLI automatically configures it in tsconfig.json.

4

Create buttons using Pressable
------------------------------

React Native includes a few different components for handling touch events, but [`<Pressable>`](https://reactnative.dev/docs/pressable) is recommended for its flexibility. It can detect single taps, long presses, trigger separate events when the button is pushed in and released, and more.

In the design, there are two buttons we need to create. Each has a different style and label. Let's start by creating a reusable component for these buttons. Create a Button.tsx file inside the components directory with the following code:

components/Button.tsx

Copy

```
import { StyleSheet, View, Pressable, Text } from 'react-native';

type Props = {
  label: string;
};

export default function Button({ label }: Props) {
  return (
    <View style={styles.buttonContainer}>
      <Pressable style={styles.button} onPress={() => alert('You pressed a button.')}>
        <Text style={styles.buttonLabel}>{label}</Text>
      </Pressable>
    </View>
  );
}

const styles = StyleSheet.create({
  buttonContainer: {
    width: 320,
    height: 68,
    marginHorizontal: 20,
    alignItems: 'center',
    justifyContent: 'center',
    padding: 3,
  },
  button: {
    borderRadius: 10,
    width: '100%',
    height: '100%',
    alignItems: 'center',
    justifyContent: 'center',
    flexDirection: 'row',
  },
  buttonLabel: {
    color: '#fff',
    fontSize: 16,
  },
});

```

The app displays an alert when the user taps any of the buttons on the screen. It happens because `<Pressable>` calls `alert()` on its `onPress` prop. Let's import this component into app/(tabs)/index.tsx file and add styles for the `<View>` that encapsulates these buttons:

app/(tabs)/index.tsx

Copy

```
import { View, StyleSheet } from 'react-native';

import Button from '@/components/Button';
import ImageViewer from '@/components/ImageViewer';

const PlaceholderImage = require("@/assets/images/background-image.png");

export default function Index() {
  return (
    <View style={styles.container}>
      <View style={styles.imageContainer}>
        <ImageViewer imgSource={PlaceholderImage} />
      </View>
      <View style={styles.footerContainer}>
        <Button label="Choose a photo" />
        <Button label="Use this photo" />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#25292e',
    alignItems: 'center',
  },
  imageContainer: {
    flex: 1,
    paddingTop: 28,
  },
  footerContainer: {
    flex: 1 / 3,
    alignItems: 'center',
  },
});

```

Let's take a look at our app on Android, iOS and the web:

![Initial layout.](/static/images/tutorial/buttons-created.png)

The second button with the label "Use this photo" resembles the actual button from the design. However, the first button needs more styling to match the design.

5

Enhance the reusable button component
-------------------------------------

The "Choose a photo" button requires different styling than the "Use this photo" button, so we will add a new button theme prop that will allow us to apply a `primary` theme. This button also has an icon before the label. We will use an icon from the `@expo/vector-icons` library.

To load and display the icon on the button, let's use `FontAwesome` from the library. Modify components/Button.tsx to add the following code snippet:

components/Button.tsx

Copy

```
import { StyleSheet, View, Pressable, Text } from 'react-native';
import FontAwesome from '@expo/vector-icons/FontAwesome';

type Props = {
  label: string;
  theme?: 'primary';
};

export default function Button({ label, theme }: Props) {
  if (theme === 'primary') {
    return (
      <View
        style={[
          styles.buttonContainer,
          { borderWidth: 4, borderColor: '#ffd33d', borderRadius: 18 },
        ]}>
        <Pressable
          style={[styles.button, { backgroundColor: '#fff' }]}
          onPress={() => alert('You pressed a button.')}>
          <FontAwesome name="picture-o" size={18} color="#25292e" style={styles.buttonIcon} />
          <Text style={[styles.buttonLabel, { color: '#25292e' }]}>{label}</Text>
        </Pressable>
      </View>
    );
  }

  return (
    <View style={styles.buttonContainer}>
      <Pressable style={styles.button} onPress={() => alert('You pressed a button.')}>
        <Text style={styles.buttonLabel}>{label}</Text>
      </Pressable>
    </View>
  );
}

const styles = StyleSheet.create({
  buttonContainer: {
    width: 320,
    height: 68,
    marginHorizontal: 20,
    alignItems: 'center',
    justifyContent: 'center',
    padding: 3,
  },
  button: {
    borderRadius: 10,
    width: '100%',
    height: '100%',
    alignItems: 'center',
    justifyContent: 'center',
    flexDirection: 'row',
  },
  buttonIcon: {
    paddingRight: 8,
  },
  buttonLabel: {
    color: '#fff',
    fontSize: 16,
  },
});

```

Let's learn what the above code does:

* The primary theme button uses inline styles, which overrides the styles defined in `StyleSheet.create()` with an object directly passed in the `style` prop.
* The `<Pressable>` component in the primary theme uses a `backgroundColor` property with a value `#fff` to set the button's background to white. If we add this property to the `styles.button`, the background color value will be set for both the primary theme and the unstyled one.
* Inline styles use JavaScript and override the default styles for a specific value.

Now, modify the app/(tabs)/index.tsx file to use the `theme="primary"` prop on the first button.

app/(tabs)/index.tsx

Copy

```
import { View, StyleSheet } from 'react-native';

import Button from '@/components/Button';
import ImageViewer from '@/components/ImageViewer';

const PlaceholderImage = require('@/assets/images/background-image.png');

export default function Index() {
  return (
    <View style={styles.container}>
      <View style={styles.imageContainer}>
        <ImageViewer imgSource={PlaceholderImage} />
      </View>
      <View style={styles.footerContainer}>
        <Button theme="primary" label="Choose a photo" />
        <Button label="Use this photo" />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#25292e',
    alignItems: 'center',
  },
  imageContainer: {
    flex: 1,
  },
  footerContainer: {
    flex: 1 / 3,
    alignItems: 'center',
  },
});

```

Let's take a look at our app on Android, iOS and the web:

Summary
-------

Chapter 3: Build a screen

We've successfully implemented the initial design to start building our app's first screen.

Mark this chapter as read

In the next chapter, we'll add the functionality to pick an image from the device's media library.

[Next: Use an image picker](/tutorial/image-picker)

[Previous (Expo tutorial)

Add navigation](/tutorial/add-navigation)[Next (Expo tutorial)

Use an image picker](/tutorial/image-picker)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/tutorial/build-a-screen.mdx)

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Break down the screen](/tutorial/build-a-screen/#break-down-the-screen)[Display the image](/tutorial/build-a-screen/#display-the-image)[Divide components into files](/tutorial/build-a-screen/#divide-components-into-files)[Create buttons using Pressable](/tutorial/build-a-screen/#create-buttons-using-pressable)[Enhance the reusable button component](/tutorial/build-a-screen/#enhance-the-reusable-button-component)[Summary](/tutorial/build-a-screen/#summary)