Expo Vector Icons - Expo Documentation

[Docs](/)

[Blog](https://expo.dev/blog)[Changelog](https://expo.dev/changelog)[Star Us on GitHub](https://github.com/expo/expo)

Search

[Home](/)[Guides](/guides/overview)[EAS](/eas)[Reference](/versions/latest)[Learn](/tutorial/overview)

[Overview](/guides/overview)

Development process

[Develop an app with Expo](/workflow/overview)[Configure with app config](/workflow/configuration)[Continuous Native Generation](/workflow/continuous-native-generation)[Using libraries](/workflow/using-libraries)[Privacy manifests](/guides/apple-privacy)[Permissions](/guides/permissions)[Environment variables](/guides/environment-variables)

Linking

Write native code

Compile locally

Web

Bundling

Existing React Native apps

Existing native apps

Reference

Expo Router

[Introduction](/router/introduction)[Installation](/router/installation)

Router 101

Navigation patterns

Advanced

Reference

Migration

Expo Modules API

[Overview](/modules/overview)[Get started](/modules/get-started)

Tutorials

Reference

Push notifications

[Overview](/push-notifications/overview)[About notification types](/push-notifications/what-you-need-to-know)[Expo push notifications setup](/push-notifications/push-notifications-setup)[Send notifications with the Expo Push Service](/push-notifications/sending-notifications)[Handle incoming notifications](/push-notifications/receiving-notifications)

Reference

More

[Upgrade Expo SDK](/workflow/upgrading-expo-sdk-walkthrough)

Assorted

[Authentication with OAuth or OpenID providers](/guides/authentication)[Using Hermes](/guides/using-hermes)[iOS Developer Mode](/guides/ios-developer-mode)[Expo Vector Icons](/guides/icons)[Localization](/guides/localization)[Configure JS engines](/guides/configuring-js-engines)[Using Bun](/guides/using-bun)[Edit rich text](/guides/editing-richtext)[App store assets](/guides/store-assets)[Local-first](/guides/local-first)[Keyboard handling](/guides/keyboard-handling)

Integrations

Troubleshooting

Regulatory compliance

[Data and Privacy protection](/regulatory-compliance/data-and-privacy-protection)[GDPR compliance](/regulatory-compliance/gdpr)[HIPAA compliance](/regulatory-compliance/hipaa)[Privacy Shield](/regulatory-compliance/privacy-shield)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Expo Vector Icons
=================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/icons.mdx)

Learn how to use various types of icons in your Expo app, including react native vector icons, custom icon fonts, icon images, and icon buttons.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/icons.mdx)

---

Not every app needs to use emojis for icons. You can use a popular icon set through an icon font such as FontAwesome, Glyphicons, or Ionicons, or choose PNGs from [The Noun Project](https://thenounproject.com/). This guide explains various ways to use icons in your Expo app.

`@expo/vector-icons`
--------------------

The `@expo/vector-icons` library is installed by default on the template project using `npx create-expo-app` and is part of the `expo` package. It is built on top of [`react-native-vector-icons`](https://github.com/oblador/react-native-vector-icons) and uses a similar API. It includes popular icon sets you can browse at [icons.expo.fyi](https://icons.expo.fyi).

The component loads the `Ionicons` font and renders a checkmark icon in the following example:

Vector icons

Copy

Open in Snack

```
import { View, StyleSheet } from 'react-native';
import Ionicons from '@expo/vector-icons/Ionicons';

export default function App() {
  return (
    <View style={styles.container}>
      <Ionicons name="checkmark-circle" size={32} color="green" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

```

> As with [any custom font](/develop/user-interface/fonts#use-a-local-font-file) in Expo, you can preload icon fonts before rendering your app. The font object is available as a static property on the font component. So, in the case above, it is `Ionicons.font`, which evaluates to `{ionicons: require('path/to/ionicons.ttf')}`.

Custom icon fonts
-----------------

To use a custom icon font, first import it into your project. Only after the font has loaded, can you create an Icon set. [Learn more about loading custom fonts](/develop/user-interface/fonts#handle-expovector-icons-initial-load).

`@expo/vector-icons` exposes three methods to help you create an icon set:

### `createIconSet`

The `createIconSet` method returns a custom font based on the `glyphMap` where the key is the icon name and the value is either a UTF-8 character or its character code.

In the example below, the `glyphMap` object is defined and then passed as the first argument to the `createIconSet` method. The second argument `fontFamily` is the name of the font (not the filename). Optionally, you can pass the third argument for Android support, which is the custom font file name.

createIconSet example

Copy

```
import createIconSet from '@expo/vector-icons/createIconSet';

const glyphMap = { 'icon-name': 1234, test: 'â' };
const CustomIcon = createIconSet(glyphMap, 'fontFamily', 'custom-icon-font.ttf');

export default function CustomIconExample() {
  return <CustomIcon name="icon-name" size={32} color="red" />;
}

```

### `createIconSetFromIcoMoon`

The `createIconSetFromIcoMoon` method is used to create a custom font based on an [IcoMoon](https://icomoon.io/) config file. You have to save the selection.json and .ttf in your project, preferably in the assets directory, and then load the font using either `useFonts` hook or `Font.loadAsync` method from `expo-font`.

See the example below that uses the `useFonts` hook to load the font:

Icomoon Icons

Copy

Open in Snack

```
import React from 'react';
import { View, StyleSheet } from 'react-native';
import { useFonts } from 'expo-font';
import createIconSetFromIcoMoon from '@expo/vector-icons/createIconSetFromIcoMoon';

const Icon = createIconSetFromIcoMoon(
  require('./assets/icomoon/selection.json'),
  'IcoMoon',
  'icomoon.ttf'
);

export default function App() {
  const [fontsLoaded] = useFonts({
    IcoMoon: require('./assets/icomoon/icomoon.ttf'),
  });

  if (!fontsLoaded) {
    return null;
  }

  return (
    <View style={styles.container}>
      <Icon name="pacman" size={50} color="red" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

```

### `createIconSetFromFontello`

The `createIconSetFromFontello` method is used to create a custom font based on a [Fontello](http://fontello.com/) config file. You have to save the config.json and .ttf somewhere convenient in your project, preferably in the assets directory, and then load the font using either `useFonts` hook or `Font.loadAsync` method from `expo-font`.

It follows a similar configuration as `createIconSetFromIcoMoon` as shown in the example:

Fontello Icons

Copy

```
// Import the createIconSetFromFontello method
import createIconSetFromFontello from '@expo/vector-icons/createIconSetFromFontello';

// Import the config file
import fontelloConfig from './config.json';

// Both the font name and files exported from Fontello are most likely called "fontello".
// Ensure this is the `fontname.ttf` and not the file path.
const Icon = createIconSetFromFontello(fontelloConfig, 'fontello', 'fontello.ttf');

```

Icon images
-----------

You can use the `Image` component from [Expo Image](/versions/latest/sdk/image) or React Native to display an icon. The `source` prop takes the relative path to refer to the image.

Expo Image

React Native Image

Usage with Expo Image

Copy

Open in Snack

```
import { Image } from 'expo-image';
import { View, StyleSheet } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <Image source={require('./assets/images/slack-icon.png')} style={{ width: 50, height: 50 }} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

```

Usage with React Native Image

Copy

Open in Snack

```
import { Image, View, StyleSheet } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <Image source={require('./assets/images/slack-icon.png')} style={{ width: 50, height: 50 }} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

```

You can also provide different versions of your icon at various pixel densities. The `Image` component takes care of using the image with appropriate pixel density automatically. For example, if the image has variants such as `icon@2x.png` and `icon@3x.png`, the `@2x` suffix is served for a device's screen density for older devices such as iPhone 8 and the `@3x` suffix is served for a device's screen density on newer devices such as iPhone 13. [Learn more about serving different densities in React Native documentation](https://reactnative.dev/docs/images#static-image-resources).

Button component
----------------

You can create an Icon Button using the `Font.Button` syntax where the `Font` is the icon set that you import from `@expo/vector-icons`.

In the example below, a login button uses the `FontAwesome` icon set. Notice that the `FontAwesome.Button` component accepts props to handle action when a button is pressed and can wrap the text of the button.

Icon Button Component

Copy

Open in Snack

```
import React from 'react';
import { View, StyleSheet } from 'react-native';
import FontAwesome from '@expo/vector-icons/FontAwesome';

export default function App() {
  const loginWithFacebook = () => {
    console.log('Button pressed');
  };

  return (
    <View style={styles.container}>
      <FontAwesome.Button name="facebook" backgroundColor="#3b5998" onPress={loginWithFacebook}>
        Login with Facebook
      </FontAwesome.Button>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

```

### Properties

Any [`Text`](http://reactnative.dev/docs/text), [`TouchableHighlight`](http://reactnative.dev/docs/touchablehighlight), or [`TouchableWithoutFeedback`](http://reactnative.dev/docs/touchablewithoutfeedback) property in addition to these:

| Prop | Description | Default |
| --- | --- | --- |
| `color` | Text and icon color, use `iconStyle` or nest a `Text` component if you need different colors. | `white` |
| `size` | Icon size. | `20` |
| `iconStyle` | Styles applied to the icon only, good for setting margins or a different color. *Note: use `iconStyle` for margins or expect unstable behaviour.* | `{marginRight: 10}` |
| `backgroundColor` | Background color of the button. | `#007AFF` |
| `borderRadius` | Border radius of the button, set to `0` to disable. | `5` |
| `onPress` | A function called when the button is pressed. | *None* |

[Previous (More - Assorted)

iOS Developer Mode](/guides/ios-developer-mode)[Next (More - Assorted)

Localization](/guides/localization)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/icons.mdx)
* Last updated on December 18, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[@expo/vector-icons](/guides/icons/#expovector-icons)[Custom icon fonts](/guides/icons/#custom-icon-fonts)[createIconSet](/guides/icons/#createiconset)[createIconSetFromIcoMoon](/guides/icons/#createiconsetfromicomoon)[createIconSetFromFontello](/guides/icons/#createiconsetfromfontello)[Icon images](/guides/icons/#icon-images)[Button component](/guides/icons/#button-component)[Properties](/guides/icons/#properties)