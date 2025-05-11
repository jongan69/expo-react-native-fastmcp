Navigation layouts in Expo Router - Expo Documentation

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

[Core concepts](/router/basics/core-concepts)[Router notation](/router/basics/notation)[Layout](/router/basics/layout)[Navigation](/router/basics/navigation)[Common patterns](/router/basics/common-navigation-patterns)

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

Integrations

Troubleshooting

Regulatory compliance

[Data and Privacy protection](/regulatory-compliance/data-and-privacy-protection)[GDPR compliance](/regulatory-compliance/gdpr)[HIPAA compliance](/regulatory-compliance/hipaa)[Privacy Shield](/regulatory-compliance/privacy-shield)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Navigation layouts in Expo Router
=================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/basics/layout.mdx)

Learn how to construct different relationships between pages by using directories and layout files.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/basics/layout.mdx)

---

[![Introduction to Expo Router Layout Files](https://i3.ytimg.com/vi/Yh6Qlg2CYwQ/maxresdefault.jpg)

Introduction to Expo Router Layout Files

What are layout files, how to navigate between screens, and block access using redirects.](https://www.youtube.com/watch?v=Yh6Qlg2CYwQ)

Each directory within the app directory (including app itself) can define a layout in the form of a \_layout.tsx file inside that directory. This file defines how all the pages within that directory are arranged. This is where you would define a stack navigator, tab navigator, drawer navigator, or any other layout that you want to use for the pages in that directory. The layout file exports a default component that is rendered before whatever page you are navigating to within that directory.

Let's look at a few common layout scenarios.

Root layout
-----------

Virtually every app will have a \_layout.tsx file directly inside the app directory. This is the root layout and represents the entry point for your navigation. In addition to describing the top-level navigator for your app, this file is where you would put initialization code that may have previously gone inside an App.jsx file, such as loading fonts, interacting with the splash screen, or adding context providers.

Here's an example root layout:

app/\_layout.tsx

Copy

```
import { useFonts } from 'expo-font';
import { Stack } from 'expo-router';
import * as SplashScreen from 'expo-splash-screen';
import { useEffect } from 'react';

SplashScreen.preventAutoHideAsync();

export default function RootLayout() {
  const [loaded] = useFonts({
    SpaceMono: require('../assets/fonts/SpaceMono-Regular.ttf'),
  });

  useEffect(() => {
    if (loaded) {
      SplashScreen.hideAsync();
    }
  }, [loaded]);

  if (!loaded) {
    return null;
  }

  return <Stack />;
}

```

The above example shows the splash screen initially and then renders a stack navigator once the fonts are loaded, which will cause your app to proceed to the initial route.

Stacks
------

You can implement a stack navigator in your root layout, as shown above, or in any other layout file inside a directory. Let's suppose you have a file structure with a stack inside of a directory:

`app`

â`products`

ââ`_layout.tsx`

ââ`index.tsx`

ââ`[productId].tsx`

ââ`accessories`

âââ`index.tsx`

If you want everything inside of the app/products directory to be arranged in a stack relationship, inside the \_layout.tsx file, return a `Stack` component:

app/products/\_layout.tsx

Copy

```
import { Stack } from 'expo-router';

export default function StackLayout() {
  return <Stack />;
}

```

When you navigate to `/products`, it will first go to the default route, which is products/index.tsx. If you navigate to `/products/123`, then that page will be pushed onto the stack. By default, the stack will render a back button in the header that will pop the current page off the stack, returning the user to the previous page. Even when a page isn't visible, if it is still pushed onto the stack, it is still being rendered.

The `Stack` component implements [React Navigation's native stack](https://reactnavigation.org/docs/native-stack-navigator/) and can use the same screen options. However, you do not have to define the pages specifically inside the navigator. The files inside the directory will be automatically treated as eligible routes in the stack. However, if you want to define screen options, you can add a `Stack.Screen` component inside the `Stack` component. The `name` prop should match the route name, but you do not need to supply a `component` prop; Expo Router will map this automatically:

app/products/\_layout.tsx

Copy

```
import { Stack } from 'expo-router';

export default function StackLayout() {
  return (
    <Stack>
      <Stack.Screen name="[productId]" options={{ headerShown: false }} />
    </Stack>
  );
}

```

While it is possible to nest navigators, be sure to only do so when it is truly needed. In the above example, if you want to push products/accessories/index.tsx onto the stack, it's not necessary to have an additional \_layout.tsx in the accessories directory with a `Stack` navigator. That would define another stack inside the first one. It is fine to add directories that only affect the URL, otherwise, use the same navigator as the parent directory.

Tabs
----

Much like a stack, you can implement a tab navigator in your layout file, and all the routes directly inside that directory will be treated as tabs. Consider the following file structure:

`app`

â`(tabs)`

ââ`_layout.tsx`

ââ`index.tsx`

ââ`feed.tsx`

ââ`profile.tsx`

In the \_layout.tsx file, return a `Tabs` component:

app/(tabs)/\_layout.tsx

Copy

```
import { Tabs } from 'expo-router';
import MaterialIcons from '@expo/vector-icons/MaterialIcons';

export default function TabLayout() {
  return (
    <Tabs>
      <Tabs.Screen
        name="index"
        options={{
          title: 'Home',
          tabBarIcon: ({ color }) => <MaterialIcons size={28} name="house.fill" color={color} />,
        }}
      />
      <!-- Add more tabs here -->
    </Tabs>
  );
}

```

This will cause the index.tsx, feed.tsx, and profile.tsx files to appear together in the same bottom tabs navigator. This `Tabs` component uses [React Navigation's native bottom tabs](https://reactnavigation.org/docs/bottom-tab-navigator/) and supports the same options.

In the case of `Tabs`, you will likely want to define the tabs in the navigator, as this influences the order in which tabs appear, the title, and the icon inside the tab. The index route will be the default selected tab.

Slot
----

In some cases, you may want a layout without a navigator. This is helpful for adding a header or footer around the current route, or for displaying a modal over any route inside a directory. In this case, you can use the `Slot` component, which serves as a placeholder for the current child route.

Consider the following file structure:

`app`

â`social`

ââ`_layout.tsx`

ââ`index.tsx`

ââ`feed.tsx`

ââ`profile.tsx`

For example, you may want to wrap any route inside the social directory with a header and footer, but you want navigating between the pages to simply replace the current page rather than pushing new pages onto a stack, which can then later be popped off with a "back" navigation action. In the \_layout.tsx file, return a `Slot` component surrounded by your header and footer:

app/social/\_layout.tsx

Copy

```
import { Slot } from 'expo-router';

export default function Layout() {
  return (
    <>
      <Header />
      <Slot />
      <Footer />
    </>
  );
}

```

Other layouts
-------------

These are just a few examples of common layouts to give you an idea of how it works. There's much more you can do with layout:

* Implement a [Drawer navigator](/router/advanced/drawer)
* Replace the default tabs with [fully customized tabs](/router/advanced/custom-tabs)
* Use a [modal](/router/advanced/modals) to display a page with transparency, such that the parent navigator is still visible underneath
* [Adapt any navigator that is compatible with React Navigation](/versions/latest/sdk/router#withlayoutcontextnav-processor), including top tabs, bottom sheets, and more

[Previous (Expo Router - Router 101)

Router notation](/router/basics/notation)[Next (Expo Router - Router 101)

Navigation](/router/basics/navigation)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/basics/layout.mdx)
* Last updated on April 24, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Root layout](/router/basics/layout/#root-layout)[Stacks](/router/basics/layout/#stacks)[Tabs](/router/basics/layout/#tabs)[Slot](/router/basics/layout/#slot)[Other layouts](/router/basics/layout/#other-layouts)