File-based routing - Expo Documentation

[Docs](/)

[Blog](https://expo.dev/blog)[Changelog](https://expo.dev/changelog)[Star Us on GitHub](https://github.com/expo/expo)

Search

[Home](/)[Guides](/guides/overview)[EAS](/eas)[Reference](/versions/latest)[Learn](/tutorial/overview)

Get started

[Introduction](/get-started/introduction)[Create a project](/get-started/create-a-project)[Set up your environment](/get-started/set-up-your-environment)[Start developing](/get-started/start-developing)[Next steps](/get-started/next-steps)

Develop

[Tools for development](/develop/tools)

Navigation

[File-based routing](/develop/file-based-routing)[Dynamic routes](/develop/dynamic-routes)[Next steps](/develop/next-steps)

User interface

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

File-based routing
==================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/file-based-routing.mdx)

Learn about Expo Router which is a file-based routing system and how to use it in your project.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/file-based-routing.mdx)

---

This guide provides basic conventions and guidance for Expo Router and navigation patterns (stack and tabs). To follow along, you can [create a project by using the default template](/get-started/create-a-project) or install [Expo Router library manually](/router/installation#manual-installation) in your existing project.

What is Expo Router?
--------------------

Expo Router is a routing framework for React Native and web applications. It allows you to manage navigation between screens in your app and use the same components on multiple platforms (Android, iOS and web). It uses a file-based method to determine routes inside your app. It also provides native navigation and is built on top of [React Navigation](https://reactnavigation.org/).

app directory
-------------

The app is a special directory. Any file you add to this directory becomes a route inside the native app and reflects the same URL for that route on the web.

Create a route
--------------

In the app directory, a route is created by adding a file or a nested directory that includes index.tsx file.

For example, to create an initial route of your app, you can add index.tsx to the app directory with the following code:

app/index.tsx

Copy

```
import { View, Text, StyleSheet } from 'react-native';

export default function HomeScreen() {
  return (
    <View style={styles.container}>
      <Text>Home</Text>
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

The app/index.tsx file will match the `/` route and after creating this file the app directory structure is:

`app`

â`index.tsx``matches '/'`

### File name conventions

Files named index match the parent directory and do not add a path segment. For example, if you expand the app's file structure by adding app/settings/index.tsx, it will match the `/settings` route.

`app`

â`index.tsx``matches '/'`

â`settings`

ââ`index.tsx``matches '/settings'`

> Note: A route file is defined by exporting a React component as the default value. The file must use either `.js`, `.jsx`, `.ts`, or `.tsx` extension.

\_layout file
-------------

Layout files in a directory are used to define shared UI elements such as headers, tab bars so that they persist between different routes.

Any time you create a new project, by default the app directory will contain a root layout file (app/\_layout).

`app`

â`index.tsx``matches '/'`

â`_layout``Root layout`

### Root layout

Traditionally, React Native projects are structured with a single root component (defined as App.js or index.js). Similarly, the first layout file (\_layout.tsx) inside the app directory is considered to be the single root component.

Between multiple routes, a Root layout file in Expo Router is used to share UI between multiple routes such as injecting global providers, themes, styles, delay splash screen rendering until assets and fonts are loaded, or defining your app's root navigation structure.

For example, the following code exports a default React component called `RootLayout`:

app/\_layout.tsx

Copy

```
export default function RootLayout() {
  return (
	  %%placeholder-start%%... %%placeholder-end%%
  )
}

```

> With Expo Router, any React providers defined inside app/\_layout.tsx are accessible by any route in your app. To improve performance and cause fewer renders, try to reduce the scope of your providers to only the routes that need them.

Stack navigator
---------------

A stack navigator is a pattern to navigate between different routes in an app. It allows transitioning between screens and managing the navigation history. It is conceptually similar to how a web browser handles the navigation state.

For example, if you want to add a new route `/details`, create details.tsx file. This will allow the app user to navigate from the `/` route to `/details`:

app/details.tsx

Copy

```
import { View, Text, StyleSheet } from 'react-native';

export default function DetailsScreen() {
  return (
    <View style={styles.container}>
      <Text>Details</Text>
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

After creating this route file, the current file structure looks like:

`app`

â`index.tsx``matches '/'`

â`details.tsx``matches '/details'`

â`_layout``Root layout`

To allow navigation between two routes (`/` and `/details`), update the Root layout file and add a `Stack` component to it:

app/\_layout.tsx

Copy

```
import { Stack } from 'expo-router';

export default function RootLayout() {
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
      <Stack.Screen name="index" />
      <Stack.Screen name="details" />
    </Stack>
  );
}

```

`<Stack.Screen name={routeName} />` component in the layout file allows defining routes in a stack.

> Note: The `screenOptions` in the above example allows configuring options for all the routes inside a stack. See [Statically configure route options](/router/advanced/stack#statically-configure-route-options) for more information.

Navigating between routes
-------------------------

Expo Router uses a built-in component called `Link` to move between routes in an app. This is conceptually similar to how web works with the `<a>` tag and the `href` attribute.

You can use it by importing it from Expo Router library and then passing the `href` prop with the route to navigate as the value of the prop. For example, to navigate from `/` to `/details`, add a `Link` component in the index.tsx file:

app/index.tsx

Copy

```
import { Link } from 'expo-router';
import { View, Text, StyleSheet } from 'react-native';

export default function HomeScreen() {
  return (
    <View style={styles.container}>
      <Text>Home</Text>
      <Link href="/details">View details</Link>
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

### How does `Link` work?

`Link` wraps the children in a `<Text>` by default. You can customize to use a different button component.

Use the `Link` component to wrap the custom button component and the `asChild` prop which forwards all props to the first child of the `Link` component. For more information on the `Link` component's props, see [Navigate between pages](/router/navigating-pages).

Groups
------

A group is created to organize similar routes or a section of the app. Each group has a layout file, and the grouped directory requires a name inside parentheses `(group)`.

For example, you have the `/` and `/details` routes which can be grouped inside app/(home) directory. This updates the file structure to:

`app`

â`_layout.tsx``Root layout`

â`(home)`

ââ`index.tsx``matches '/'`

ââ`details.tsx``matches '/details'`

ââ`_layout.tsx``Home layout`

You also need to add (home)/\_layout.tsx which is used to define the `Stack` navigator for `/` and `/details` routes.

app/(home)/\_layout.tsx

Copy

```
import { Stack } from 'expo-router';

export default function HomeLayout() {
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
      <Stack.Screen name="index" />
      <Stack.Screen name="details" />
    </Stack>
  );
}

```

The Root layout file also changes and now includes the (home) group which further uses (home)/index as the initial route of the app.

app/\_layout.tsx

Copy

```
import { Stack } from 'expo-router';

export default function RootLayout() {
  return (
    <Stack>
      <Stack.Screen name="(home)" />
    </Stack>
  );
}

```

> Note: In the above example, the screen options are moved to (home)/\_layout.tsx file. This means if you add any route to the Stack navigator inside the Root layout, it will not use the same screen options as the routes inside the Home layout.

Tab navigator
-------------

A tab navigator is a common pattern to navigate between different sections of an app using a tab bar. Expo Router provides a `Tabs` navigation component.

For example, in the current file structure, you have two different sections: Home (`/` and `/details` routes) and Settings (`/settings` route). Adding a special directory (tabs), you can move the existing Home route files inside it and create a settings.tsx.

`app`

â`_layout.tsx``Root layout`

â`(tabs)`

ââ`_layout.tsx``Tab layout`

ââ`(home)`

âââ`index.tsx``matches '/'`

âââ`details.tsx``matches '/details'`

âââ`_layout.tsx``Home layout`

ââ`settings.tsx``matches '/settings'`

Any file or directory inside (tabs) becomes a route in the tab navigator. To switch between different routes using the tab bar, you need to create a layout file inside this directory (tabs)/\_layout and export a `TabLayout` component:

app/(tabs)/\_layout.tsx

Copy

```
import { Tabs } from 'expo-router';

export default function TabLayout() {
  return (
    <Tabs>
      <Tabs.Screen name="(home)" />
      <Tabs.Screen name="settings" />
    </Tabs>
  );
}

```

> Note: In `TabLayout`, the existing Stack navigator for `(home)` is now nested.

To make this work, update the app/\_layout.tsx file by adding (tabs) as the first route.

app/\_layout.tsx

Copy

```
import { Stack } from 'expo-router';

export default function RootLayout() {
  return (
    <Stack>
      <Stack.Screen name="(tabs)" />
    </Stack>
  );
}

```

Not found routes
----------------

Expo Router provides a special file +not-found.tsx which is used to handle routes that are 404s. This route file matches all unmatched routes from a nested level.

Create this file in the app directory:

+not-found.tsx

Copy

```
import { Link, Stack } from 'expo-router';
import { View, StyleSheet } from 'react-native';

export default function NotFoundScreen() {
  return (
    <>
      <Stack.Screen options={{ title: "Oops! This screen doesn't exist." }} />
      <View style={styles.container}>
        <Link href="/">Go to home screen</Link>
      </View>
    </>
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

[Previous (Develop)

Tools for development](/develop/tools)[Next (Develop - Navigation)

Dynamic routes](/develop/dynamic-routes)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/file-based-routing.mdx)
* Last updated on June 08, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[What is Expo Router?](/develop/file-based-routing/#what-is-expo-router)[app directory](/develop/file-based-routing/#app-directory)[Create a route](/develop/file-based-routing/#create-a-route)[File name conventions](/develop/file-based-routing/#file-name-conventions)[\_layout file](/develop/file-based-routing/#_layout-file)[Root layout](/develop/file-based-routing/#root-layout)[Stack navigator](/develop/file-based-routing/#stack-navigator)[Navigating between routes](/develop/file-based-routing/#navigating-between-routes)[How does Link work?](/develop/file-based-routing/#how-does-link-work)[Groups](/develop/file-based-routing/#groups)[Tab navigator](/develop/file-based-routing/#tab-navigator)[Not found routes](/develop/file-based-routing/#not-found-routes)