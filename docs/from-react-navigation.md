Migrate from React Navigation - Expo Documentation

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

[React Navigation](/router/migrate/from-react-navigation)[Expo Webpack](/router/migrate/from-expo-webpack)

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

Migrate from React Navigation
=============================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/migrate/from-react-navigation.mdx)

Learn how to migrate a project using React Navigation to Expo Router.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/migrate/from-react-navigation.mdx)

---

Both React Navigation and Expo Router are Expo frameworks for routing and navigation. Expo Router is a wrapper around React Navigation and many of the concepts are the same.

Pitch
-----

Along with all the benefits of React Navigation, Expo Router enables automatic deep linking, [type safety](/router/reference/typed-routes), [deferred bundling](/router/reference/async-routes), [static rendering on web](/router/reference/static-rendering), and more.

Anti-pitch
----------

If your app uses a custom `getPathFromState` or `getStateFromPath` component, it may not be a good fit for Expo Router. If you're using these functions to support [shared routes](/router/advanced/shared-routes) then you should be fine as Expo Router has built-in support for this.

Recommendations
---------------

We recommend making the following modifications to your codebase before beginning the migration:

* Split React Navigation screen components into individual files. For example, if you have `<Stack.Screen component={HomeScreen} />`, then ensure the `HomeScreen` component is in its own file.
* Convert the project to [TypeScript](/guides/typescript#migrating-existing-javascript-project). This will make it easier to spot errors that may occur during the migration.
* Convert relative imports to [typed aliases](/guides/typescript#path-aliases-optional). For example, `../../components/button.tsx` to `@/components/button` before starting the migration. This makes it easier to move screens around the filesystem without having to update the relative paths.
* Migrate away from `resetRoot`. This is used to "restart" the app while running. This is generally considered bad practice, and you should restructure your app's navigation so this never needs to happen.
* Rename the initial route to `index`. Expo Router considers the route that is opened on launch to match `/`, React Navigation users will generally use something such as "Home" for the initial route.

### Refactor search parameters

Refactor screens to [use serializable top-level query parameters](https://reactnavigation.org/docs/params/#what-should-be-in-params). We recommend this in React Navigation as well.

In Expo Router, search parameters can only serialize top-level values such as `number`, `boolean`, and `string`. React Navigation doesn't have the same restrictions, so users can sometimes pass invalid parameters like Functions, Objects, Maps, and so on.

If your code has something similar to the below:

```
import { useNavigation } from '@react-navigation/native';

const navigation = useNavigation();

navigation.push('Followers', {
  onPress: profile => {
    navigation.push('User', { profile });
  },
});

```

Consider restructuring so the function can be accessed from the "followers" screen. In this case, you can access the router and push directly from the "followers" screen.

### Eagerly load UI

It's common in React Native apps to `return null` from the root component while assets and fonts are loading. This is bad practice and generally unsupported in Expo Router. If you absolutely must defer rendering, then ensure you don't attempt to navigate to any screens.

Historically this pattern exists because React Native will throw errors if you use custom fonts that haven't loaded yet. We changed this upstream in React Native 0.72 (SDK 49) so the default behavior is to swap the default font when the custom font loads. If you'd like to hide individual text elements until a font has finished loading, write a wrapper `<Text>`, which returns null until the font has loaded.

On web, returning `null` from the root will cause [static rendering](/router/reference/static-rendering) to skip all of the children, resulting in no searchable content. This can be tested by using "View Page Source" in Chrome, or by disabling JavaScript and reloading the page.

Migration
---------

### Delete unused or managed code

Expo Router automatically adds `react-native-safe-area-context` support.

```
- import { SafeAreaProvider } from 'react-native-safe-area-context';

export default function App() {
  return (
-    <SafeAreaProvider>
      <MyApp />
-    </SafeAreaProvider>
  )
}

```

Expo Router does not add `react-native-gesture-handler` (as of v3), so you'll have to add this yourself if you are using Gesture Handler or `<Drawer />` layout. Avoid using this package on web since it adds a lot of JavaScript that is often unused.

### Copy screens to the app directory

Create an app directory at the root of your repo, or in a root src directory.

Layout the structure of your app by creating files according to the [application of Expo Router rules](/router/basics/core-concepts#the-rules-of-expo-router-applied). Kebab-case and lowercase letters are considered best practice for route filenames.

Replace navigators with directories, for example:

React Navigation

Copy

```
function HomeTabs() {
  return (
    <Tab.Navigator>
      <Tab.Screen name="Home" component={Home} />
      <Tab.Screen name="Feed" component={Feed} />
    </Tab.Navigator>
  );
}

function App() {
  return (
    // NavigationContainer is managed by Expo Router.
    <NavigationContainer
      linking={
        {
          // ...linking configuration
        }
      }
    >
      <Stack.Navigator>
        <Stack.Screen name="Settings" component={Settings} />
        <Stack.Screen name="Profile" component={Profile} />
        <Stack.Screen
          name="Home"
          component={HomeTabs}
          options={{
            title: 'Home Screen',
          }}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

```

Expo Router:

* Rename the "main" route from Home to index to ensure it matches the `/` path.
* Convert names to lowercase.
* Move all the screens to the appropriate file locations inside the app directory. This may take some experimenting.

`app`

â`_layout.js`

â`(home)`

ââ`_layout.js`

ââ`index.js`

ââ`feed.js`

â`profile.js`

â`settings.js`

app/\_layout.js

Copy

```
import { Stack } from 'expo-router';

export default function RootLayout() {
  return (
    <Stack>
      <Stack.Screen
        name="(home)"
        options={
          {
            title: 'Home Screen',
          }
        }
      />
    </Stack>
  );
}

```

The tab navigator will be moved to a subdirectory.

app/(home)/\_layout.js

Copy

```
import { Tabs } from 'expo-router';

export default function HomeLayout() {
  return <Tabs />;
}

```

### Use Expo Router hooks

React Navigation v6 and lower will pass the props `{ navigation, route }` to every screen. This pattern is going away in React Navigation, and we never introduced it to the Expo Router.

Instead, migrate `navigation` to the `useRouter` hook.

```
+ import { useRouter } from 'expo-router';

export default function Page({
-  navigation
}) {
-  navigation.push('User', { user: 'bacon' });

+  const router = useRouter();
+  router.push('/users/bacon');
}

```

Similarly, migrate from the `route` prop to the [`useLocalSearchParams`](/router/reference/hooks#uselocalsearchparams) hook.

```
+ import { useLocalSearchParams } from 'expo-router';

export default function Page({
-  route
}) {
-  const user = route?.params?.user;

+  const { user } = useLocalSearchParams();
}

```

To access the [`navigation.navigate`](https://reactnavigation.org/docs/navigation-object/#navigate), import the `navigation` prop from [`useNavigation`](/router/reference/hooks#usenavigation) hook.

```
+ import { useNavigation } from 'expo-router';

export default function Page({
+  const navigation = useNavigation();

  return (
    <Button onPress={navigation.navigate('screenName')}>
  )
})

```

### Migrate the Link component

React Navigation and Expo Router both provide Link components. However, Expo's Link component uses `href` instead of [`to`](https://reactnavigation.org/docs/use-link-props/#to).

```
// React Navigation
<Link to="Settings" />

// Expo Router
<Link href="/settings" />

```

React Navigation users will often create a custom Link component with the `useLinkProps` hook to control the child component. This isn't necessary in Expo Router, instead, use the `asChild` prop.

### Share screens across navigators

It's common for React Navigation apps to reuse a set of routes across multiple navigators. This is generally used with tabs to ensure each tab can push any screen.

In Expo Router, you can either migrate to [shared routes](/router/advanced/shared-routes) or create multiple files and re-export the same component from them.

When you use groups or shared routes, you can navigate to specific tabs by using the fully qualified route name, for example, `/(home)/settings` instead of `/settings`.

### Migrate screen tracking events

You may have your screen tracking setup according to our [React Navigation screen tracking guide](https://reactnavigation.org/docs/screen-tracking/), update it according to the [Expo Router screen tracking guide](/router/reference/screen-tracking).

### Use platform-specific components for screens

Refer to the [platform-specific modules](/router/advanced/platform-specific-modules) guide for info on switching UI based on the platform.

### Replace the `NavigationContainer`

The global React Navigation [`<NavigationContainer />`](https://reactnavigation.org/docs/navigation-container/) is completely managed in Expo Router. Expo Router provides systems for achieving the same functionality as the `NavigationContainer` without needing to use it directly.

API substitutions

### Ref

The `NavigationContainer` ref should not be accessed directly. Use the following methods instead.

#### `resetRootâ`

Navigate to the initial route of the application. For example, if your app starts at `/` (recommended), then you can replace the current route with `/` using this method.

```
import { useRouter } from 'expo-router';

function Example() {
  const router = useRouter();

  return (
    <Text
      onPress={() => {
        // Go to the initial route of the application.
        router.replace('/');
      }}>
      Reset App
    </Text>
  );
}

```

#### `getRootState`

Use `useRootNavigationState()`.

#### `getCurrentRoute`

Unlike React Navigation, Expo Router can reliably represent any route with a string. Use the [`usePathname()`](/router/reference/hooks#usepathname) or [`useSegments()`](/router/reference/hooks#usesegments) hooks to identify the current route.

#### `getCurrentOptions`

Use the [`useLocalSearchParams()`](/router/reference/hooks#uselocalsearchparams) hook to get the current route's query parameters.

#### `addListener`

The following events can be migrated:

#### `state`

Use the [`usePathname()`](/router/reference/hooks#usepathname) or [`useSegments()`](/router/reference/hooks#usesegments) hooks to identify the current route. Use in conjunction with `useEffect(() => {}, [...])` to observe changes.

#### `options`

Use the [`useLocalSearchParams()`](/router/reference/hooks#uselocalsearchparams) hook to get the current route's query parameters. Use in conjunction with `useEffect(() => {}, [...])` to observe changes.

### props

Migrate the following `<NavigationContainer />` props:

#### `initialState`

In Expo Router, you can rehydrate your application state from a route string (for example, `/user/evanbacon`). Use [redirects](/router/reference/redirects) to handle initial states. See [shared routes](/router/advanced/shared-routes) for advanced redirects.

Avoid using this pattern in favor of deep linking (for example, a user opens your app to `/profile` rather than from the home screen) as it is most analogous to the web. If an app crashes due to a particular screen, it's best to avoid automatically navigating back to that exact screen when the app starts as it may require reinstalling the app to fix.

#### `onStateChange`

Use the [`usePathname()`](/router/reference/hooks#usepathname), [`useSegments()`](/router/reference/hooks#usesegments), and [`useGlobalSearchParams()`](/router/reference/hooks#useglobalsearchparams) hooks to identify the current route state. Use in conjunction with `useEffect(() => {}, [...])` to observe changes.

* If you're attempting to track screen changes, follow the [Screen Tracking guide](/router/reference/screen-tracking).
* React Navigation recommends avoiding [`onStateChange`](https://reactnavigation.org/docs/navigation-container/#onstatechange).

#### `onReady`

In React Navigation, [`onReady`](https://reactnavigation.org/docs/navigation-container/#onready) is most often used to determine when the splash screen should hide or when to track screens using analytics. Expo Router has special handling for both of these use cases. Assume the navigation is always ready for navigation events in the Expo Router.

* See the [Screen Tracking guide](/router/reference/screen-tracking) for info on migrating analytics from React Navigation.
* See the [Splash Screen feature](/develop/user-interface/splash-screen-and-app-icon) for info on handling the splash screen.

#### `onUnhandledAction`

Actions are always handled in Expo Router. Use [dynamic routes](/router/basics/notation#square-brackets) and [404 screens](/router/error-handling#unmatched-routes) in favor of [`onUnhandledAction`](https://reactnavigation.org/docs/navigation-container/#onunhandledaction).

#### `linking`

The [`linking`](https://reactnavigation.org/docs/navigation-container/#linking) prop is automatically constructed based on the files to the app directory.

#### `fallback`

The [`fallback`](https://reactnavigation.org/docs/navigation-container/#fallback) prop is automatically handled by Expo Router. Learn more in the [Splash Screen](/versions/latest/sdk/splash-screen) reference.

#### `theme`

In React Navigation, you set the theme for the entire app using the [`<NavigationContainer />`](https://reactnavigation.org/docs/navigation-container/#theme) component. Expo Router manages the root container for you, so instead you should set the theme using the `ThemeProvider` directly.

app/\_layout.tsx

Copy

```
import { ThemeProvider, DarkTheme, DefaultTheme, useTheme } from '@react-navigation/native';
import { Slot } from 'expo-router';

export default function RootLayout() {
  return (
    <ThemeProvider value={DarkTheme}>
      <Slot />
    </ThemeProvider>
  );
}

```

You can use this technique at any layer of the app to set the theme for a specific layout. The current theme can be accessed with the `useTheme` hook from `@react-navigation/native`.

#### `children`

The `children` prop is automatically populated based on the files in the app directory and the currently open URL.

#### `independent`

Expo Router does not support [`independent`](https://reactnavigation.org/docs/navigation-container/#independent) containers. This is because the router is responsible for managing the single `<NavigationContainer />`. Any additional containers will not be automatically managed by Expo Router.

#### `documentTitle`

Use the [Head component](/router/reference/static-rendering#meta-tags) to set the webpage title.

#### `ref`

Use the `useNavigationContainerRef()` hook instead.

### Rewrite custom navigators

If your project has a custom navigator, you can rewrite this or port it to Expo Router.

To port, simply use the `withLayoutContext` function:

```
import { createCustomNavigator } from './my-navigator';

export const CustomNavigator = withLayoutContext(createCustomNavigator().Navigator);

```

To rewrite, use the `Navigator` component, which wraps the [`useNavigationBuilder`](https://reactnavigation.org/docs/custom-navigators#usenavigationbuilder) hook from React Navigation.

The return value of `useNavigationBuilder` can be accessed with the `Navigator.useContext()` hook from inside the `<Navigator />` component. Properties can be passed to `useNavigationBuilder` using the props of the `<Navigator />` component, this includes `initialRouteName`, `screenOptions`, `router`.

All of the `children` of a `<Navigator />` component will be rendered as-is.

* `Navigator.useContext`: Access the React Navigation `state`, `navigation`, `descriptors`, and `router` for the custom navigator.
* `Navigator.Slot`: A React component used to render the currently selected route. This component can only be rendered inside a `<Navigator />` component.

#### Example

Custom layouts have an internal context that is ignored when using the `<Slot />` component without a `<Navigator />` component wrapping it.

```
import { View } from 'react-native';
import { TabRouter } from '@react-navigation/native';

import { Navigator, usePathname, Slot, Link } from 'expo-router';

export default function App() {
  return (
    <Navigator router={TabRouter}>
      <Header />
      <Slot />
    </Navigator>
  );
}

function Header() {;
  const pathname = usePathname();

  return (
    <View>
      <Link href="/">Home</Link>
      <Link
        href="/profile"
        style={[pathname === '/profile' && { color: 'blue' }]}>
        Profile
      </Link>
      <Link href="/settings">Settings</Link>
    </View>
  );
}

```

### Use Expo Router's Splash Screen wrapper

Expo Router wraps `expo-splash-screen` and adds special handling to ensure it's hidden after the navigation mounts, and whenever an unexpected error is caught. Simply migrate from importing `expo-splash-screen` to importing `SplashScreen` from `expo-router`.

### Navigation state observation

If you're observing the navigation state directly, migrate to the [`usePathname`](/router/reference/hooks#usepathname), [`useSegments`](/router/reference/hooks#usesegments), and [`useGlobalSearchParams`](/router/reference/hooks#useglobalsearchparams) hooks.

### Pass params to nested screens

Instead of using the [nested screen navigation events](https://reactnavigation.org/docs/params/#passing-params-to-nested-navigators), use a qualified href:

```
// React Navigation
navigation.navigate('Account', {
  screen: 'Settings',
  params: { user: 'jane' },
});

// Expo Router
router.push({ pathname: '/account/settings', params: { user: 'jane' } });

```

### Set initial routes for deep linking and server navigation

In React Navigation, you can use the `initialRouteName` property of the linking configuration. In Expo Router, use [layout settings](/router/advanced/router-settings).

### Reset navigation state

You can use the [`reset`](https://reactnavigation.org/docs/navigation-actions/#reset) action from the React Navigation library to reset the navigation state. It is dispatched using the [`useNavigation`](/router/reference/hooks#usenavigation) hook from Expo Router to access the `navigation` prop.

In the below example, the `navigation` prop is accessible from the `useNavigation` hook and the `CommonActions.reset` action from `@react-navigation/native`. The object specified in the `reset` action replaces the existing navigation state with the new one.

app/screen.js

Copy

```
import { useNavigation } from 'expo-router'
import { CommonActions } from '@react-navigation/native'

export default function Screen() {
  const navigation = useNavigation();

  const handleResetAction = () => {
    navigation.dispatch(CommonActions.reset({
      routes: [{key: "(tabs)", name: "(tabs)"}]
    }))
  }

  return (
    <>
      {/* ...rest of the code */}
      <Button title='Reset' onPress={handleResetAction} />
    </>
  );
}

```

### Migrate TypeScript types

Expo Router can automatically generate [statically typed routes](/router/reference/typed-routes), this will ensure you can only navigate to valid routes.

Additional information
----------------------

### React Navigation themes

React Navigation navigators `<Stack>`, `<Drawer>`, and `<Tabs>` use a shared appearance provider. In React Navigation, you set the theme for the entire app using the `<NavigationContainer />` component. Expo Router manages the root container so that you can set the theme using the `ThemeProvider` directly.

app/\_layout.tsx

Copy

```
import { ThemeProvider, DarkTheme, DefaultTheme, useTheme } from '@react-navigation/native';
import { Slot } from 'expo-router';

export default function RootLayout() {
  return (
    <ThemeProvider value={DarkTheme}>
      <Slot />
    </ThemeProvider>
  );
}

```

You can use this technique at any layer of the app to set the theme for a specific layout. The current theme can be accessed via `useTheme` hook from `@react-navigation/native`.

### React Navigation Elements

The [`@react-navigation/elements`](https://reactnavigation.org/docs/elements/) library provides a set of UI elements and helpers that can be used to build a navigation UI. These components are designed to be composable and customizable. You can reuse the default functionality from the library or build your navigator's UI on top of it.

To use it with Expo Router, you need to install the library:

npm

Yarn

Terminal

Copy

`-Â``npm install @react-navigation/elements`

Terminal

Copy

`-Â``yarn add @react-navigation/elements`

To learn more about the components and utilities the library provides, see [Elements library](https://reactnavigation.org/docs/elements/) documentation.

[Previous (Expo Router - Reference)

Troubleshooting](/router/reference/troubleshooting)[Next (Expo Router - Migration)

Expo Webpack](/router/migrate/from-expo-webpack)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/migrate/from-react-navigation.mdx)
* Last updated on April 29, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Pitch](/router/migrate/from-react-navigation/#pitch)[Anti-pitch](/router/migrate/from-react-navigation/#anti-pitch)[Recommendations](/router/migrate/from-react-navigation/#recommendations)[Refactor search parameters](/router/migrate/from-react-navigation/#refactor-search-parameters)[Eagerly load UI](/router/migrate/from-react-navigation/#eagerly-load-ui)[Migration](/router/migrate/from-react-navigation/#migration)[Delete unused or managed code](/router/migrate/from-react-navigation/#delete-unused-or-managed-code)[Copy screens to the app directory](/router/migrate/from-react-navigation/#copy-screens-to-the-app-directory)[Use Expo Router hooks](/router/migrate/from-react-navigation/#use-expo-router-hooks)[Migrate the Link component](/router/migrate/from-react-navigation/#migrate-the-link-component)[Share screens across navigators](/router/migrate/from-react-navigation/#share-screens-across-navigators)[Migrate screen tracking events](/router/migrate/from-react-navigation/#migrate-screen-tracking-events)[Use platform-specific components for screens](/router/migrate/from-react-navigation/#use-platform-specific-components-for-screens)[Replace the NavigationContainer](/router/migrate/from-react-navigation/#replace-the-navigationcontainer)[Ref](/router/migrate/from-react-navigation/#ref)[props](/router/migrate/from-react-navigation/#props)[Rewrite custom navigators](/router/migrate/from-react-navigation/#rewrite-custom-navigators)[Use Expo Router's Splash Screen wrapper](/router/migrate/from-react-navigation/#use-expo-routers-splash-screen-wrapper)[Navigation state observation](/router/migrate/from-react-navigation/#navigation-state-observation)[Pass params to nested screens](/router/migrate/from-react-navigation/#pass-params-to-nested-screens)[Set initial routes for deep linking and server navigation](/router/migrate/from-react-navigation/#set-initial-routes-for-deep-linking-and-server-navigation)[Reset navigation state](/router/migrate/from-react-navigation/#reset-navigation-state)[Migrate TypeScript types](/router/migrate/from-react-navigation/#migrate-typescript-types)[Additional information](/router/migrate/from-react-navigation/#additional-information)[React Navigation themes](/router/migrate/from-react-navigation/#react-navigation-themes)[React Navigation Elements](/router/migrate/from-react-navigation/#react-navigation-elements)