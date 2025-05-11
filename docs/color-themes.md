Color themes - Expo Documentation

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

Color themes
============

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/user-interface/color-themes.mdx)

Learn how to support light and dark modes in your app.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/user-interface/color-themes.mdx)

---

It's common for apps to support light and dark color schemes. Here is an example of how supporting both modes looks in an Expo project:

Configuration
-------------

> For Android and iOS projects, additional configuration is required to support switching between light and dark mode. For web, no additional configuration is required.

To configure supported appearance styles, you can use the [`userInterfaceStyle`](/versions/latest/config/app#userinterfacestyle) property in your project's [app config](/versions/latest/config/app). By default, this property is set to `automatic` when you create a new project with the [default template](/get-started/create-a-project).

Here is an example configuration:

app.json

Copy

```
{
  "expo": {
    "userInterfaceStyle": "automatic"
  }
}

```

You can also configure `userInterfaceStyle` property for a specific platforms by setting either [`android.userInterfaceStyle`](/versions/latest/config/app#userinterfacestyle-2) or [`ios.userInterfaceStyle`](/versions/latest/config/app#userinterfacestyle-1) to the preferred value.

> The app will default to the `light` style if this property is absent.

When you are creating a development build, you have to install [`expo-system-ui`](/versions/latest/sdk/system-ui#installation) to support the appearance styles for Android. Otherwise, the `userInterfaceStyle` property is ignored.

Terminal

Copy

`-Â``npx expo install expo-system-ui`

If the project is misconfigured and doesn't have `expo-system-ui` installed, the following warning will be shown in the terminal:

Terminal

Copy

`Â» android: userInterfaceStyle: Install expo-system-ui in your project to enable this feature.`

You can also use the following command to check if the project is misconfigured:

Terminal

Copy

`-Â``npx expo config --type introspect`

Using bare React Native app?

#### Android

Ensure that the `uiMode` flag is present on your `MainActivity` (and any other activities where this behavior is desired) in AndroidManifest.xml:

```
<activity android:configChanges="keyboard|keyboardHidden|orientation|screenSize|uiMode">

```

Implement the `onConfigurationChanged` method in MainActivity.java:

```
import android.content.Intent;
import android.content.res.Configuration;
public class MainActivity extends ReactActivity {
  %%placeholder-start%%... %%placeholder-end%%

  @Override
  public void onConfigurationChanged(Configuration newConfig) {
    super.onConfigurationChanged(newConfig);
    Intent intent = new Intent("onConfigurationChanged");
    intent.putExtra("newConfig", newConfig);
    sendBroadcast(intent);
  }
  %%placeholder-start%%... %%placeholder-end%%
}

```

#### iOS

You can configure supported styles with the [`UIUserInterfaceStyle`](https://developer.apple.com/documentation/bundleresources/information_property_list/uiuserinterfacestyle) key in your app Info.plist. Use `Automatic` to support both light and dark modes.

### Supported appearance styles

The `userInterfaceStyle` property supports the following values:

* `automatic`: Follow system appearance settings and notify about any change the user makes.
* `light`: Restrict the app to support light theme only.
* `dark`: Restrict the app to support dark theme only.

Detect the color scheme
-----------------------

To detect the color scheme in your project, use `Appearance` or `useColorScheme` from `react-native`:

app/index.tsx

Copy

```
import { Appearance, useColorScheme } from 'react-native';

```

Then, you can use `useColorScheme()` hook as shown below:

app/index.tsx

Copy

```
function MyComponent() {
  let colorScheme = useColorScheme();

  if (colorScheme === 'dark') {
    // render some dark thing
  } else {
    // render some light thing
  }
}

```

In some cases, you will find it helpful to get the current color scheme imperatively with [`Appearance.getColorScheme()` or listen to changes with `Appearance.addChangeListener()`](https://reactnative.dev/docs/appearance).

Additional information
----------------------

### Minimal example

useColorScheme example

Copy

Open in Snack

```
import { Text, StyleSheet, View, useColorScheme } from 'react-native';
import { StatusBar } from 'expo-status-bar';

export default function App() {
  const colorScheme = useColorScheme();

  const themeTextStyle = colorScheme === 'light' ? styles.lightThemeText : styles.darkThemeText;
  const themeContainerStyle =
    colorScheme === 'light' ? styles.lightContainer : styles.darkContainer;

  return (
    <View style={[styles.container, themeContainerStyle]}>
      <Text style={[styles.text, themeTextStyle]}>Color scheme: {colorScheme}</Text>
      <StatusBar />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  text: {
    fontSize: 20,
  },
  lightContainer: {
    backgroundColor: '#d0d0c0',
  },
  darkContainer: {
    backgroundColor: '#242c40',
  },
  lightThemeText: {
    color: '#242c40',
  },
  darkThemeText: {
    color: '#d0d0c0',
  },
});

```

### Tips

While you are developing your project, you can change your simulator's or device's appearance by using the following shortcuts:

* If using an Android Emulator, you can run `adb shell "cmd uimode night yes"` to enable dark mode, and `adb shell "cmd uimode night no"` to disable dark mode.
* If using a physical Android device or an Android Emulator, you can toggle the system dark mode setting in the device's settings.
* If working with an iOS emulator locally, you can use the `Cmd â` + `Shift` + `a` shortcut to toggle between light and dark modes.

[Previous (Develop - User interface)

Assets](/develop/user-interface/assets)[Next (Develop - User interface)

Animation](/develop/user-interface/animation)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/user-interface/color-themes.mdx)
* Last updated on July 24, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Configuration](/develop/user-interface/color-themes/#configuration)[Supported appearance styles](/develop/user-interface/color-themes/#supported-appearance-styles)[Detect the color scheme](/develop/user-interface/color-themes/#detect-the-color-scheme)[Additional information](/develop/user-interface/color-themes/#additional-information)[Minimal example](/develop/user-interface/color-themes/#minimal-example)[Tips](/develop/user-interface/color-themes/#tips)