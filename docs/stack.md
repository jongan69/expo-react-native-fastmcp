Stack - Expo Documentation

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

Stack
=====

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/advanced/stack.mdx)

Learn how to use the Stack navigator in Expo Router.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/advanced/stack.mdx)

---

[![Using a Stack Navigator with Expo Router](https://i3.ytimg.com/vi/izZv6a99Roo/maxresdefault.jpg)

Using a Stack Navigator with Expo Router

Navigate between screens, pass params between screens, create dynamic routes, and configure the screen titles and animations.](https://www.youtube.com/watch?v=izZv6a99Roo)

A stack navigator is the foundational way of navigating between routes in an app. On Android, a stacked route animates on top of the current screen. On iOS, a stacked route animates from the right. Expo Router provides a `Stack` navigation component that creates a navigation stack and allows you to add new routes in your app.

This guide provides information on how you can create a `Stack` navigator in your project and customize an individual route's options and header.

Get started
-----------

You can use file-based routing to create a stack navigator. Here's an example file structure:

`app`

â`_layout.tsx`

â`index.tsx`

â`details.tsx`

This file structure produces a layout where the `index` route is the first route in the stack, and the `details` route is pushed on top of the `index` route when navigated.

You can use the app/\_layout.tsx file to define your app's `Stack` navigator with these two routes:

app/\_layout.tsx

Copy

```
import { Stack } from 'expo-router';

export default function Layout() {
  return <Stack />;
}

```

Screen options and header configuration
---------------------------------------

### Statically configure route options

You can use the `<Stack.Screen name={routeName} />` component in the layout component route to statically configure a route's options. This is also useful for [tabs](/router/advanced/tabs) or [drawers](/router/advanced/drawer) as they need an icon defined ahead of time.

app/\_layout.tsx

Copy

```
import { Stack } from 'expo-router';

export default function Layout() {
  return (
    <Stack
      screenOptions={{
        headerStyle: {
          backgroundColor: '#f4511e',
        },
        headerTintColor: '#fff',
        headerTitleStyle: {
          fontWeight: 'bold',
        },
      }}>
      {/* Optionally configure static options outside the route.*/}
      <Stack.Screen name="home" options={{}} />
    </Stack>
  );
}

```

As an alternative to the `<Stack.Screen>` component, you can use [`navigation.setOptions()`](https://reactnavigation.org/docs/navigation-object/#setoptions) to configure a route's options from within the route's component file.

app/index.tsx

Copy

```
import { Stack, useNavigation } from 'expo-router';
import { Text, View } from 'react-native';
import { useEffect } from 'react';

export default function Home() {
  const navigation = useNavigation();

  useEffect(() => {
    navigation.setOptions({ headerShown: false });
  }, [navigation]);

  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Home Screen</Text>
    </View>
  );
}

```

### Configure header bar

You can configure the header bar for all routes in a `Stack` navigator by using the `screenOptions` prop. This is useful for setting a common header style across all routes.

app/\_layout.tsx

Copy

```
import { Stack } from 'expo-router';

export default function Layout() {
  return (
    <Stack
      screenOptions={{
        headerStyle: {
          backgroundColor: '#f4511e',
        },
        headerTintColor: '#fff',
        headerTitleStyle: {
          fontWeight: 'bold',
        },
      }}
    />
  );
}

```

To configure the header bar dynamically for an individual route, use that navigator's `<Stack.Screen>` component in the routes's file. This is useful for interactions that change the UI.

app/index.tsx

Copy

```
import { Link, Stack } from 'expo-router';
import { Image, Text, View, StyleSheet } from 'react-native';

function LogoTitle() {
  return (
    <Image style={styles.image} source={{ uri: 'https://reactnative.dev/img/tiny_logo.png' }} />
  );
}

export default function Home() {
  return (
    <View style={styles.container}>
      <Stack.Screen
        options={{
          title: 'My home',
          headerStyle: { backgroundColor: '#f4511e' },
          headerTintColor: '#fff',
          headerTitleStyle: {
            fontWeight: 'bold',
          },

          headerTitle: props => <LogoTitle {...props} />,
        }}
      />
      <Text>Home Screen</Text>
      <Link href={{ pathname: 'details', params: { name: 'Bacon' } }}>Go to Details</Link>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  image: {
    width: 50,
    height: 50,
  },
});

```

### Set screen options dynamically

To configure a route's option dynamically, you can always use the `<Stack.Screen>` component in that route's file.

As an alternative, you can also use the [imperative API's `router.setParams()`](/versions/latest/sdk/router#router) function to configure the route dynamically.

app/details.tsx

Copy

```
import { Stack, useLocalSearchParams, useRouter } from 'expo-router';
import { View, Text, StyleSheet } from 'react-native';

export default function Details() {
  const router = useRouter();
  const params = useLocalSearchParams();

  return (
    <View style={styles.container}>
      <Stack.Screen
        options={{
          title: params.name,
        }}
      />
      <Text
        onPress={() => {
          router.setParams({ name: 'Updated' });
        }}>
        Update the title
      </Text>
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

### Header buttons

You can add buttons to the header by using the `headerLeft` and `headerRight` options. These options accept a React component that renders in the header.

app/index.tsx

Copy

```
import { Stack } from 'expo-router';
import { Button, Text, Image, StyleSheet } from 'react-native';
import { useState } from 'react';

function LogoTitle() {
  return (
    <Image style={styles.image} source={{ uri: 'https://reactnative.dev/img/tiny_logo.png' }} />
  );
}

export default function Home() {
  const [count, setCount] = useState(0);

  return (
    <>
      <Stack.Screen
        options={{
          headerTitle: props => <LogoTitle {...props} />,
          headerRight: () => <Button onPress={() => setCount(c => c + 1)} title="Update count" />,
        }}
      />
      <Text>Count: {count}</Text>
    </>
  );
}

const styles = StyleSheet.create({
  image: {
    width: 50,
    height: 50,
  },
});

```

Custom push behavior
--------------------

By default, the `Stack` navigator removes duplicate screens when pushing a route that is already in the stack. For example, if you push the same screen twice, the second push will be ignored. You can change this push behavior by providing a custom `getId()` function to the `<Stack.Screen>`.

For example, the `index` route in the following layout structure shows a list of different user profiles in the app. Let's make the `[details]` route a [dynamic route](/router/basics/notation#square-brackets) so that the app user can navigate to see a profile's details.

`app`

â`_layout.tsx`

â`index.tsx`

â`[details].tsx``matches dynamic paths like '/details1'`

The `Stack` navigator will push a new screen every time the app user navigates to a different profile but will fail. If you provide a `getId()` function that returns a new ID every time, the `Stack` will push a new screen every time the app user navigates to a profile.

You can use the `<Stack.Screen name="[profile]" getId={}>` component in the layout component route to modify the push behavior:

app/\_layout.tsx

Copy

```
import { Stack } from 'expo-router';

export default function Layout() {
  return (
    <Stack>
      <Stack.Screen
        name="[profile]"
        getId={
          ({ params }) => String(Date.now())
        }
      />
    </Stack>
  );
}

```

Removing stack screens
----------------------

There are different actions you can use to dismiss and remove one or many routes from a stack.

### `dismiss` action

Dismisses the last screen in the closest stack. If the current screen is the only route in the stack, it will dismiss the entire stack.

You can optionally pass a positive number to dismiss up to that specified number of screens.

Dismiss is different from `back` as it targets the closest stack and not the current navigator. If you have nested navigators, calling `dismiss` will take you back multiple screens.

app/settings.tsx

Copy

```
import { Button, View } from 'react-native';
import { useRouter } from 'expo-router';

export default function Settings() {
  const router = useRouter();

  const handleDismiss = (count: number) => {
    router.dismiss(count)
  };

  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Button title="Go to first screen" onPress={() => handleDismiss(3)} />
    </View>
  );
}

```

### `dismissTo` action

> `dismissTo` was added in Expo Router `4.0.8`. It operates similarly to the `navigation` function in Expo Router v3.

Dismisses screens in the current `<Stack />` until the specified `Href` is reached. If the `Href` is absent in the history, a `push` action will be performed instead.

For example, consider the history of `/one`, `/two`, `/three` routes, where `/three` is the current route. The action `router.dismissTo('/one')` will cause the history to go back twice, while `router.dismissTo('/four')` will `push` the history forward to the `/four` route.

app/settings.tsx

Copy

```
import { Button, View, Text } from 'react-native';
import { useRouter } from 'expo-router';

export default function Settings() {
  const router = useRouter();

  const handleDismissAll = () => {
    router.dismissTo('/')
  };

  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Button title="Go to first screen" onPress={handleDismissAll} />
    </View>
  );
}

```

### `dismissAll` action

To return to the first screen in the closest stack. This is similar to [`popToTop`](https://reactnavigation.org/docs/stack-actions/#poptotop) stack action.

For example, the `home` route is the first screen, and the `settings` is the last. To go from `settings` to `home` route you'll have to go back to `details`. However, using the `dismissAll` action, you can go from `settings` to `home` and dismiss any screen in between.

app/settings.tsx

Copy

```
import { Button, View, Text } from 'react-native';
import { useRouter } from 'expo-router';

export default function Settings() {
  const router = useRouter();

  const handleDismissAll = () => {
    router.dismissAll()
  };

  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Button title="Go to first screen" onPress={handleDismissAll} />
    </View>
  );
}

```

### `canDismiss` action

To check if it is possible to dismiss the current screen. Returns `true` if the router is within a stack with more than one screen in the stack's history.

app/settings.tsx

Copy

```
import { Button, View } from 'react-native';
import { useRouter } from 'expo-router';

export default function Settings() {
  const router = useRouter();

  const handleDismiss = (count: number) => {
    if (router.canDismiss()) {
      router.dismiss(count)
    }
  };

  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Button title="Maybe dismiss" onPress={() => handleDismiss()} />
    </View>
  );
}

```

Relation with Native Stack Navigator
------------------------------------

The `Stack` navigator in Expo Router wraps the [Native Stack Navigator](https://reactnavigation.org/docs/native-stack-navigator) from React Navigation. Options available in the Native Stack Navigator are all available in the `Stack` navigator in Expo Router.

### JavaScript stack with @react-navigation/stack

You can also use the JavaScript-powered `@react-navigation/stack` library to create a custom layout component by wrapping this library with the `withLayoutContext`.

In the following example, `JsStack` component is defined using `@react-navigation/stack` library:

layouts/js-stack.tsx

Copy

```
import { ParamListBase, StackNavigationState } from '@react-navigation/native';
import {
  createStackNavigator,
  StackNavigationEventMap,
  StackNavigationOptions,
} from '@react-navigation/stack';
import { withLayoutContext } from 'expo-router';

const { Navigator } = createStackNavigator();

export const JsStack = withLayoutContext<
  StackNavigationOptions,
  typeof Navigator,
  StackNavigationState<ParamListBase>,
  StackNavigationEventMap
>(Navigator);

```

After defining the `JsStack` component, you can use it in your app:

app/\_layout.tsx

Copy

```
import { JsStack } from '../layouts/js-stack';

export default function Layout() {
  return (
    <JsStack
      screenOptions={
        {
          %%placeholder-start%%... %%placeholder-end%%
        }
      }
    />
  );
}

```

For more information on available options, see [`@react-navigation/stack` documentation](https://reactnavigation.org/docs/stack-navigator).

More
----

[Native Stack Navigator options

For a list of all options available in the stack layout, see React Navigation's documentation.](https://reactnavigation.org/docs/native-stack-navigator#options)

[Previous (Expo Router - Router 101)

Common patterns](/router/basics/common-navigation-patterns)[Next (Expo Router - Navigation patterns)

Tabs](/router/advanced/tabs)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/advanced/stack.mdx)
* Last updated on May 01, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Get started](/router/advanced/stack/#get-started)[Screen options and header configuration](/router/advanced/stack/#screen-options-and-header-configuration)[Statically configure route options](/router/advanced/stack/#statically-configure-route-options)[Configure header bar](/router/advanced/stack/#configure-header-bar)[Set screen options dynamically](/router/advanced/stack/#set-screen-options-dynamically)[Header buttons](/router/advanced/stack/#header-buttons)[Custom push behavior](/router/advanced/stack/#custom-push-behavior)[Removing stack screens](/router/advanced/stack/#removing-stack-screens)[dismiss action](/router/advanced/stack/#dismiss-action)[dismissTo action](/router/advanced/stack/#dismissto-action)[dismissAll action](/router/advanced/stack/#dismissall-action)[canDismiss action](/router/advanced/stack/#candismiss-action)[Relation with Native Stack Navigator](/router/advanced/stack/#relation-with-native-stack-navigator)[JavaScript stack with @react-navigation/stack](/router/advanced/stack/#javascript-stack-with-react-navigationstack)[More](/router/advanced/stack/#more)