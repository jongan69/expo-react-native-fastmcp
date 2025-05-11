Tabs - Expo Documentation

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

Tabs
====

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/advanced/tabs.mdx)

Learn how to use the Tabs layout in Expo Router.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/advanced/tabs.mdx)

---

[![Using a Tab Navigator with Expo Router](https://i3.ytimg.com/vi/BElPB4Ai3j0/maxresdefault.jpg)

Using a Tab Navigator with Expo Router

Configure the tab icons, nest navigators, and manage navigation history.](https://www.youtube.com/watch?v=BElPB4Ai3j0)

Tabs are a common way to navigate between different sections of an app. Expo Router provides a tabs layout to help you create a tab bar at the bottom of your app. The fastest way to get started is to use a template. See the [quick start installation](/router/installation#quick-start) to get started.

Continue reading to add tabs to an existing project or to customize your app's tabs.

Get started
-----------

You can use file-based routing to create a tabs layout. Here's an example file structure:

`app`

â`_layout.tsx`

â`(tabs)`

ââ`_layout.tsx`

ââ`index.tsx`

ââ`settings.tsx`

This file structure produces a layout with a tab bar at the bottom of the screen. The tab bar will have two tabs: Home and Settings:

![A screenshot of a tab bar with two tabs: Home and Settings.](/static/images/expo-router/tabs.png)

You can use the app/\_layout.tsx file to define your app's root layout:

app/\_layout.tsx

Copy

```
import { Stack } from 'expo-router';

export default function Layout() {
  return (
    <Stack>
      <Stack.Screen name="(tabs)" options={{ headerShown: false }} />
    </Stack>
  );
}

```

The (tabs) directory is a special directory name that tells Expo Router to use the `Tabs` layout.

From the file structure, the (tabs) directory has three files. The first is (tabs)/\_layout.tsx. This file is the main layout file for the tab bar and each tab. Inside it, you can control how the tab bar and each tab button look and behave.

app/(tabs)/\_layout.tsx

Copy

```
import FontAwesome from '@expo/vector-icons/FontAwesome';
import { Tabs } from 'expo-router';

export default function TabLayout() {
  return (
    <Tabs screenOptions={{ tabBarActiveTintColor: 'blue' }}>
      <Tabs.Screen
        name="index"
        options={{
          title: 'Home',
          tabBarIcon: ({ color }) => <FontAwesome size={28} name="home" color={color} />,
        }}
      />
      <Tabs.Screen
        name="settings"
        options={{
          title: 'Settings',
          tabBarIcon: ({ color }) => <FontAwesome size={28} name="cog" color={color} />,
        }}
      />
    </Tabs>
  );
}

```

Finally, you have the two tab files that make up the content of the tabs: app/(tabs)/index.tsx and app/(tabs)/settings.tsx.

app/(tabs)/index.tsx & app/(tabs)/settings.tsx

Copy

```
import { View, Text, StyleSheet } from 'react-native';

export default function Tab() {
  return (
    <View style={styles.container}>
      <Text>Tab [Home|Settings]</Text>
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

The tab file named index.tsx is the default tab when the app loads. The second tab file settings.tsx shows how you can add more tabs to the tab bar.

Screen options
--------------

The tabs layout wraps the [Bottom Tabs Navigator](https://reactnavigation.org/docs/bottom-tab-navigator) from React Navigation. You can use the [options presented in the React Navigation documentation](https://reactnavigation.org/docs/bottom-tab-navigator/#options) to customize the tab bar or each tab.

Advanced
--------

### Hiding a tab

Sometimes you want a route to exist but not show up in the tab bar. You can pass `href: null` to disable the button:

app/(tabs)/\_layout.tsx

Copy

```
import { Tabs } from 'expo-router';

export default function TabLayout() {
  return (
    <Tabs>
      <Tabs.Screen
        name="index"
        options={{
          href: null,
        }}
      />
    </Tabs>
  );
}

```

### Dynamic routes

You can use a dynamic route in a tab bar. For example, you have a `[user]` tab that shows a user's profile. You can use the `href` option to link to a specific user's profile.

app/(tabs)/\_layout.tsx

Copy

```
import { Tabs } from 'expo-router';

export default function TabLayout() {
  return (
    <Tabs>
      <Tabs.Screen
        {/* Name of the dynamic route.*/}
        name="[user]"
        options={{
          {/* Ensure the tab always links to the same href.*/}
          href: '/evanbacon',
          {/* OR you can use the href object.*/}
          href: {
            pathname: '/[user]',
            params: {
              user: 'evanbacon',
            },
          },
        }}
      />
    </Tabs>
  );
}

```

> Note: When adding a dynamic route in your tab layout, ensure that the dynamic route defined is unique. You cannot have two screens for the same dynamic route. For example, you cannot have two `[user]` tabs. If you need to have multiple dynamic routes, create a custom navigator.

[Previous (Expo Router - Navigation patterns)

Stack](/router/advanced/stack)[Next (Expo Router - Navigation patterns)

Drawer](/router/advanced/drawer)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/advanced/tabs.mdx)
* Last updated on May 01, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Get started](/router/advanced/tabs/#get-started)[Screen options](/router/advanced/tabs/#screen-options)[Advanced](/router/advanced/tabs/#advanced)[Hiding a tab](/router/advanced/tabs/#hiding-a-tab)[Dynamic routes](/router/advanced/tabs/#dynamic-routes)