Modals - Expo Documentation

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

[Stack](/router/advanced/stack)[Tabs](/router/advanced/tabs)[Drawer](/router/advanced/drawer)[Authentication](/router/advanced/authentication)[Nesting navigators](/router/advanced/nesting-navigators)[Modals](/router/advanced/modals)[Shared routes](/router/advanced/shared-routes)[Protected routes](/router/advanced/protected)

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

Integrations

Troubleshooting

Regulatory compliance

[Data and Privacy protection](/regulatory-compliance/data-and-privacy-protection)[GDPR compliance](/regulatory-compliance/gdpr)[HIPAA compliance](/regulatory-compliance/hipaa)[Privacy Shield](/regulatory-compliance/privacy-shield)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Modals
======

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/advanced/modals.mdx)

Learn how to use modals in Expo Router.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/advanced/modals.mdx)

---

[![Using Modals with Expo Router](https://i3.ytimg.com/vi/gNzuJVRmyDk/maxresdefault.jpg)

Using Modals with Expo Router

Learn about the different ways to display content over the rest of your app.](https://www.youtube.com/watch?v=gNzuJVRmyDk)

Modals are a common user interface pattern in mobile apps. They are used to present content on top of the existing screen and is used for different purposes, such as displaying confirmation alerts or standalone forms. You can create modals in your app using the following methods:

* Use React Native's [`Modal`](https://reactnative.dev/docs/modal) component.
* Use Expo Router's special file-based syntax to create a modal screen within the app's navigation system.

Each approach has its specific use case. Understanding when to use each method is important for creating a positive user experience.

React Native's Modal component
------------------------------

The `Modal` component is part of React Native's core API. Common use cases include:

* Standalone interactions, such as self-contained tasks that don't need to be part of the navigation system.
* Temporary alerts or confirmation dialogs that are ideal for quick interactions.

Below is an example of a custom `Modal` component that overlays the current screen on different platforms:

For most use cases, you can use the `Modal` component and customize it according to your app's user interface requirements. For details on how to use the `Modal` component and its props, see the [React Native documentation](https://reactnative.dev/docs/modal).

Modal screen using Expo Router
------------------------------

A modal screen is a file created inside the app directory and is used as a route within the existing stack. It is used for complex interactions that need to be part of the navigation system, such as multi-step forms where you can link to a specific screen after the process completes.

Below is an example of how a modal screen works on different platforms:

### Usage

To implement a modal route, create a screen called modal.tsx inside the app directory. Here's an example file structure:

`app`

â`_layout.tsx`

â`index.tsx`

â`modal.tsx`

The above file structure produces a layout where the `index` is the first route in the stack. Inside the root layout file (app/\_layout.tsx), you can add the `modal` route in the stack. To present it as a modal, set the `presentation` option to `modal` on the route.

app/\_layout.tsx

Copy

```
import { Stack } from 'expo-router';

export default function Layout() {
  return (
    <Stack>
      <Stack.Screen name="index" />
      <Stack.Screen
        name="modal"
        options={{
          presentation: 'modal',
        }}
      />
    </Stack>
  );
}

```

You can use the `Link` component to navigate to the modal screen from the index.tsx file.

app/index.tsx

Copy

```
import { Link } from 'expo-router';
import { StyleSheet, Text, View } from 'react-native';

export default function Home() {
  return (
    <View style={styles.container}>
      <Text>Home screen</Text>
      <Link href="/modal" style={styles.link}>
        Open modal
      </Link>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  link: {
    paddingTop: 20,
    fontSize: 20,
  },
});

```

The modal.tsx presents the contents of the modal.

app/modal.tsx

Copy

```
import { StyleSheet, Text, View } from 'react-native';

export default function Modal() {
  return (
    <View style={styles.container}>
      <Text>Modal screen</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
});

```

### Modal presentation and dismiss behavior

A modal loses its previous context when it is the current screen in the navigator and is presented as a standalone screen. Its presentation and dismissal behavior are different on each platform:

* On Android, the modal slides on top of the current screen. To dismiss it, use the back button to navigate back to the previous screen.
* On iOS, the modal slides from the bottom of the current screen. To dismiss it, swipe it down from the top.
* On web, the modal is presented as a separate route, and the dismiss behavior has to be provided manually using [`router.canGoBack()`](/router/navigating-pages#imperative-navigation). Here's an example of how to dismiss the modal:

app/modal.tsx

Copy

```
import { Link, router} from 'expo-router';
import { StyleSheet, Text, View } from 'react-native';

export default function Modal() {
  const isPresented = router.canGoBack();

  return (
    <View style={styles.container}>
      <Text>Modal screen</Text>
      {isPresented && <Link href="../">Dismiss modal</Link>}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
});

```

### Change status bar appearance on iOS

By default on iOS, the modal has a dark background which hides the status bar. To change the status bar appearance, you can use the `Platform` API to check if the current platform is iOS and then use the [`StatusBar`](/versions/latest/sdk/status-bar) component to change the appearance inside the modal.tsx file.

app/modal.tsx

Copy

```
import { StyleSheet, Text, View, Platform } from 'react-native';
import { StatusBar } from 'expo-status-bar';

export default function Modal() {
  return (
    <View style={styles.container}>
      <Text>Modal screen</Text>
      <StatusBar style={Platform.OS === 'ios' ? 'light' : 'auto'} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
});

```

Web modals implementation
-------------------------

The video above demonstrates a modal window that appears over the main content of the web page. The background dims to draw focus to the modal, which contains information for the user. This is typical behavior for web modals, where users can interact with the modal or close it to return to the main page.

You can achieve the above web modal behavior by using the [`transparentModal`](https://reactnavigation.org/docs/stack-navigator/#transparent-modals) presentation mode, styling the overlay and modal content, and utilizing [`react-native-reanimated`](/versions/latest/sdk/reanimated#installation) to animate the modal's presentation.

Modify your project's root layout (app/\_layout.tsx) to add an `options` object to the modal route:

app/\_layout.tsx

Copy

```
import { Stack } from 'expo-router';

export const unstable_settings = {
  initialRouteName: 'index',
};

export default function Layout() {
  return (
    <Stack>
      <Stack.Screen name="index" />
      <Stack.Screen
        name="modal"
        options={{
          presentation: 'transparentModal',
          animation: 'fade',
          headerShown: false,
        }}
      />
    </Stack>
  );
}

```

> `unstable_settings` currently works only with `Stack` navigators.

The above example sets the `index` screen as the [`initialRouteName`](/router/advanced/router-settings#initialroutename) using [`unstable_settings`](/router/advanced/router-settings). This ensures that the transparent modal is always rendered on top of the current screen, even when users navigate to the modal screen via a direct link.

Style the overlay and modal content in modal.tsx as shown below:

app/modal.tsx

Copy

```
import { Link } from 'expo-router';
import { Pressable, StyleSheet, Text } from 'react-native';
import Animated, { FadeIn, SlideInDown } from 'react-native-reanimated';

export default function Modal() {
  return (
    <Animated.View
      entering={FadeIn}
      style={{
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#00000040',
      }}
    >
      {/* Dismiss modal when pressing outside */}
      <Link href={'/'} asChild>
        <Pressable style={StyleSheet.absoluteFill} />
      </Link>
      <Animated.View
        entering={SlideInDown}
        style={{
          width: '90%',
          height: '80%',
          alignItems: 'center',
          justifyContent: 'center',
          backgroundColor: 'white',
        }}
      >
        <Text style={{ fontWeight: 'bold', marginBottom: 10 }}>Modal Screen</Text>
        <Link href="/">
          <Text>â Go back</Text>
        </Link>
      </Animated.View>
    </Animated.View>
  );
}

```

Feel free to customize the modal animations and styles to your liking.

Additional information
----------------------

### Presentation options

There are different options to present a modal screen using the `presentation` option on Android and iOS.

| Option | Description |
| --- | --- |
| `card` | The new screen will be pushed onto a stack. The default animation on Android will vary depending on the OS version and theme. On iOS, it will slide from the side. |
| `modal` | The new screen will be presented modally, allowing for a nested stack to be rendered inside the screen. |
| `transparentModal` | The new screen will be presented modally, with the previous screen remaining visible. This allows the content below to still be seen if the screen has a translucent background. |
| `containedModal` | On Android, fallbacks to `modal`. On iOS, uses [`UIModalPresentationCurrentContext`](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle/uimodalpresentationcurrentcontext) modal style. |
| `containedTransparentModal` | On Android, fallbacks to `transparentModal`. On iOS, uses [`UIModalPresentationOverCurrentContext`](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle/uimodalpresentationovercurrentcontext) modal style. |
| `fullScreenModal` | On Android, fallbacks to `modal`. On iOS, uses [`UIModalPresentationFullScreen`](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle/uimodalpresentationfullscreen) modal style. |
| `formSheet` | On Android, fallbacks to `modal`. On iOS, uses [`UIModalPresentationFormSheet`](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle/uimodalpresentationformsheet) modal style. |

[Previous (Expo Router - Navigation patterns)

Nesting navigators](/router/advanced/nesting-navigators)[Next (Expo Router - Navigation patterns)

Shared routes](/router/advanced/shared-routes)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/advanced/modals.mdx)
* Last updated on April 17, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[React Native's Modal component](/router/advanced/modals/#react-natives-modal-component)[Modal screen using Expo Router](/router/advanced/modals/#modal-screen-using-expo-router)[Usage](/router/advanced/modals/#usage)[Modal presentation and dismiss behavior](/router/advanced/modals/#modal-presentation-and-dismiss-behavior)[Change status bar appearance on iOS](/router/advanced/modals/#change-status-bar-appearance-on-ios)[Web modals implementation](/router/advanced/modals/#web-modals-implementation)[Additional information](/router/advanced/modals/#additional-information)[Presentation options](/router/advanced/modals/#presentation-options)