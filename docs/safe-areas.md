Safe areas - Expo Documentation

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

Safe areas
==========

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/user-interface/safe-areas.mdx)

Learn how to add safe areas for screen components inside your Expo project.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/user-interface/safe-areas.mdx)

---

Creating a safe area ensures your app screen's content is positioned correctly. This means it doesn't get overlapped by notches, status bars, home indicators, and other interface elements that are part of the device's physical hardware or are controlled by the operating system. When the content gets overlapped, it gets concealed by these interface elements.

Here's an example of an app screen's content getting concealed by the status bar on Android. On iOS, the same content is concealed by rounded corners, notch, and the status bar.

![Without defining a safe area, the content can be obscured by the device's interface elements.](/static/images/safe-area/without-safe-area.png)

Use `react-native-safe-area-context` library
--------------------------------------------

[`react-native-safe-area-context`](https://github.com/th3rdwave/react-native-safe-area-context) provides a flexible API for handling Android and iOS device's safe area insets. It also provides a `SafeAreaView` component that you can use instead of a [`<View>`](https://reactnative.dev/docs/view) to account for safe areas automatically in your screen components.

Using the library, the result of the previous example changes as it displays the content inside a safe area, as shown below:

![On using react-native-safe-area-context, the content is positioned within the safe area.](/static/images/safe-area/with-safe-area.png)

### Installation

You can skip installing `react-native-safe-area-context` if you have created a project using [the default template](/get-started/create-a-project). This library is installed as peer dependency for Expo Router library. Otherwise, install it by running the following command:

Terminal

Copy

`-Â``npx expo install react-native-safe-area-context`

### Usage

You can directly use [`SafeAreaView`](https://github.com/th3rdwave/react-native-safe-area-context#safeareaview) to wrap the content of your screen's component. It is a regular `<View>` with the safe area insets applied as extra padding or margin.

app/index.tsx

Copy

```
import { Text } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';

export default function HomeScreen() {
  return (
    <SafeAreaView style={{ flex: 1 }}>
      <Text>Content is in safe area.</Text>
    </SafeAreaView>
  );
}

```

Using a different Expo template and don't have Expo Router installed?

Import and add [`SafeAreaProvider`](https://github.com/th3rdwave/react-native-safe-area-context#safeareaprovider) to the root component file (such as App.tsx) before using `SafeAreaView` in your screen component.

App.tsx

Copy

```
import { SafeAreaProvider } from 'react-native-safe-area-context';

export default function App() {
  return (
    return <SafeAreaProvider>...</SafeAreaProvider>;
  );
}

```

Alternate: `useSafeAreaInsets` hook
-----------------------------------

Alternate to `SafeAreaView`, you can use [`useSafeAreaInsets`](https://github.com/th3rdwave/react-native-safe-area-context#usesafeareainsets) hook in your screen component. It provides direct access to the safe area insets, allowing you to apply padding for each edge of the `<View>` using an inset from this hook.

The example below uses the `useSafeAreaInsets` hook. It applies top padding to a `<View>` using `insets.top`.

app/index.tsx

Copy

```
import { Text, View } from 'react-native';
import { useSafeAreaInsets } from 'react-native-safe-area-context';

export default function HomeScreen() {
  const insets = useSafeAreaInsets();

  return (
    <View style={{ flex: 1, paddingTop: insets.top }}>
      <Text>Content is in safe area.</Text>
    </View>
  );
}

```

The hook provides the insets in the following object:

```
{
  top: number,
  right: number,
  bottom: number,
  left: number
}

```

Additional information
----------------------

### Minimal example

Below is a minimal working example that uses the `useSafeAreaInsets` hook to apply top padding to a view.

Using react-native-safe-area-context

Copy

Open in Snack

```
import { Text, View } from 'react-native';
import { SafeAreaProvider, useSafeAreaInsets } from 'react-native-safe-area-context';

function HomeScreen() {
  const insets = useSafeAreaInsets();
  return (
    <View style={{ flex: 1, paddingTop: insets.top }}>
      <Text style={{ fontSize: 28 }}>Content is in safe area.</Text>
    </View>
  );
}

export default function App() {
  return (
    <SafeAreaProvider>
      <HomeScreen />
    </SafeAreaProvider>
  );
}

```

### Usage with React Navigation

By default, React Navigation supports safe areas and uses `react-native-safe-area-context` as a peer dependency. For more information, see the [React Navigation documentation](https://reactnavigation.org/docs/handling-safe-area/).

### Usage with web

If you are targeting the web, set up `SafeAreaProvider` as described in the [usage section](/develop/user-interface/safe-areas#usage). If you are doing server-side rendering (SSR), see the [Web SSR section](https://github.com/th3rdwave/react-native-safe-area-context#web-ssr) in the library's documentation.

[Previous (Develop - User interface)

Splash screen and app icon](/develop/user-interface/splash-screen-and-app-icon)[Next (Develop - User interface)

System bars](/develop/user-interface/system-bars)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/user-interface/safe-areas.mdx)
* Last updated on July 25, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Use react-native-safe-area-context library](/develop/user-interface/safe-areas/#use-react-native-safe-area-context-library)[Installation](/develop/user-interface/safe-areas/#installation)[Usage](/develop/user-interface/safe-areas/#usage)[Alternate: useSafeAreaInsets hook](/develop/user-interface/safe-areas/#alternate-usesafeareainsets-hook)[Additional information](/develop/user-interface/safe-areas/#additional-information)[Minimal example](/develop/user-interface/safe-areas/#minimal-example)[Usage with React Navigation](/develop/user-interface/safe-areas/#usage-with-react-navigation)[Usage with web](/develop/user-interface/safe-areas/#usage-with-web)