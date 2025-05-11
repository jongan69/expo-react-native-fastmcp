Common navigation patterns - Expo Documentation

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

Common navigation patterns
==========================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/basics/common-navigation-patterns.mdx)

Apply Expo Router basics to real-life navigation patterns you could use in your app.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/basics/common-navigation-patterns.mdx)

---

Now that you know the basics of how files and directories are named and arranged in Expo Router, let's apply that knowledge, looking at some real-life navigation patterns you might use in your app.

Stacks inside tabs: nested navigators
-------------------------------------

If the typical starting point for your app is a set of tabs, but one or more tabs may have more than one screen associated with it, nesting a stack navigator inside of a tab is often the way to go. This pattern often results in intuitive URLs and scales well to desktop web apps, where the primary tabs are often always visible.

Consider the following navigation tree:

`app`

â`(tabs)`

ââ`_layout.tsx`

ââ`index.tsx``single page tab`

ââ`feed`

âââ`_layout.tsx``tab with a stack inside`

âââ`index.tsx`

âââ`[postId].tsx`

ââ`settings.tsx``single page tab`

In the app/(tabs)/\_layout.tsx file, return a `Tabs` component:

app/(tabs)/\_layout.tsx

Copy

```
import { Tabs } from 'expo-router';

export default function TabLayout() {
  return (
    <Tabs screenOptions={{ headerShown: false }}>
      <Tabs.Screen name="index" options={{ title: 'Home' }} />
      <Tabs.Screen name="feed" options={{ title: 'Feed' }} />
      <Tabs.Screen name="settings" options={{ title: 'Settings' }} />
    </Tabs>
  );
}

```

In the app/(tabs)/feed/\_layout.tsx file, return a `Stack` component:

app/(tabs)/feed/\_layout.tsx

Copy

```
import { Stack } from 'expo-router';

export const unstable_settings = {
  initialRouteName: 'index',
};

export default function FeedLayout() {
  return <Stack />;
}

```

Now, within the app/(tabs)/feed directory, you can have `Link` components that point to different posts (for example, `/feed/123`). Those links will push the `feed/[postId]` route onto the stack, leaving the tab navigator visible.

You can also navigate from any other tab to a post in the feed tab with the same URL. Use `withAnchor` in conjunction with `initialRouteName` to ensure that the `feed/index` route is always the first screen in the stack:

app/(tabs)/feed/index.tsx

Copy

```
<Link href="/feed/123" withAnchor>
  Go to post
</Link>

```

You can also nest tabs inside of an outer stack navigator. That is often more useful for displaying modals over the tabs.

[Nested navigators

Learn more about how to use nested navigators in your Expo Router app.](/router/advanced/nesting-navigators)

One screen, two tabs: sharing routes
------------------------------------

Route groups can be used to share a single screen between two different tabs. Consider a navigation tree that has a Feed tab and a Search tab, and they both share pages for viewing a user profile:

`app`

â`(tabs)`

ââ`_layout.tsx`

ââ`(feed)`

âââ`index.tsx``default route`

ââ`(search)`

âââ`search.tsx`

ââ`(feed,search)`

âââ`_layout.tsx``layout shared between the two tabs`

âââ`users`

ââââ`[username].tsx``shared user profile page`

Each of the tabs is put in a group so you can define a third directory that shares routes between two groups (app/(tabs)/(feed,search)/). Even with the extra layer, app/(tabs)/(feed)/index.tsx is still the nearest index, so it will be the default route.

app/(tabs)/\_layout.tsx

Copy

```
import { Tabs } from 'expo-router';

export default function TabLayout() {
  return (
    <Tabs>
      <Tabs.Screen name="(feed)" options={{ title: 'Feed' }} />
      <Tabs.Screen name="(search)" options={{ title: 'Search' }} />
    </Tabs>
  );
}

```

Both the `(feed)` and `(search)` route groups contain stacks, so they can also share a single layout:

app/(tabs)/(feed,search)/\_layout.tsx

Copy

```
import { Stack } from 'expo-router';

export default function SharedLayout() {
  return <Stack />;
}

```

It's also possible for shared groups to only contain the shared pages, with each distinct group having its own layout file.

Now, both tabs can navigate to `/users/evanbacon` and see the same user profile page.

When you're already focused on a tab and navigating to a user, you will stay in that current tab's group. But when deep-linking directly to a user profile page from outside the app, Expo Router has to pick one of the two groups, so it will pick the first group alphabetically. Therefore, deep-linking to `/users/evanbacon` will show the user profile in the Feed tab.

[Shared routes

Learn more about how distinct routes can share the same URL in Expo Router.](/router/advanced/shared-routes)

Authenticated users only protecting routes
------------------------------------------

If you have a set of routes that should only be accessible to authenticated users, you can embed those routes in a group whose layout redirects users to a login page if they are not authenticated.

Here's what that looks like:

`app`

â`_layout.tsx`

â`login.tsx``routes users back to /(logged-in) after authentication`

â`(logged-in)`

ââ`_layout.tsx``includes redirect for unauthenticated users`

ââ`(tabs)`

âââ`_layout.tsx`

âââ`index.tsx``default route for app`

âââ`feed.tsx`

ââ`modal.tsx`

By default, the app will go to the nearest index, app/(logged-in)/(tabs)/index.tsx. However, a route group's layout file will be rendered before the enclosed route is. So, if the user is not authenticated, at this point, you can redirect the user to the login page:

app/(logged-in)/\_layout.tsx

Copy

```
import { Redirect, Stack } from 'expo-router';

export default function AuthLayout() {
  const isAuthenticated = /* check for valid auth token/session */

  if (!isAuthenticated) {
    return <Redirect href="/login" />;
  }

  return <Stack />;
}

```

Further, if a user tries to navigate to a deep link that's inside the `(logged-in)` group, they will also be redirected to the login page. Every layout on the way to the route you're navigating to is first rendered before the route itself.

The data source for checking authentication status could be React context, a state library, or a third-party auth framework. In the case of a reactive data source like context, not only will this redirect an unauthenticated user when first entering the app, but it will also redirect them if their session becomes invalid while using the app, as this layout component will re-render at that time.

In the app/login.tsx file, attempt to reroute the user to the `/(logged-in)` route after successful authentication:

app/login.tsx

Copy

```
import { Button } from 'react-native';
import { useRouter } from 'expo-router';

export default function Login() {
  const router = useRouter();

  return (
    <View>
      {/* login form */}
      <Button
        title="Login"
        onPress={() => {
          /* authenticate user */
          router.replace('/(logged-in)');
        }}
      />
    </View>
  );
}

```

This will cause app/(logged-in)/\_layout.tsx to re-render again. This time, the authentication check will pass, and the app will proceed to the default route.

[Expo Router authentication

Follow an in-depth guide for implementing authentication using protected routes.](/router/advanced/authentication)

Sometimes the best route isn't a route at all
---------------------------------------------

Separating your navigation states into distinct routes is meant to serve you and your app. Sometimes the best pattern for the job will not involve navigating to another route at all. Since layout files are just React components, you can use them to display all sorts of UI around, besides, or instead of a navigator.

Thinking back to authentication, the protected route setup works great if the user should simply not be able to visit certain pages without logging in. But what about when unauthenticated users can browse an app in read-only mode? In that case, you might want to show a login modal over the app, rather than redirecting the user to a login page:

app/(logged-in)/\_layout.tsx

Copy

```
import { SafeAreaView, Modal } from 'react-native';
import { Stack } from 'expo-router';

export default function Layout() {
  const isAuthenticated = /* check for valid auth token / session */

  return (
    <SafeAreaView>
      <Stack />
      <Modal visible={!isAuthenticated}>{/* login UX */}</Modal>
    </SafeAreaView>
  );
}

```

[Modals in Expo Router

Learn multiple patterns for displaying modals in Expo Router, including using a modal inside of a layout file.](/router/advanced/modals)

[Previous (Expo Router - Router 101)

Navigation](/router/basics/navigation)[Next (Expo Router - Navigation patterns)

Stack](/router/advanced/stack)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/basics/common-navigation-patterns.mdx)
* Last updated on May 07, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Stacks inside tabs: nested navigators](/router/basics/common-navigation-patterns/#stacks-inside-tabs-nested-navigators)[One screen, two tabs: sharing routes](/router/basics/common-navigation-patterns/#one-screen-two-tabs-sharing-routes)[Authenticated users only protecting routes](/router/basics/common-navigation-patterns/#authenticated-users-only-protecting-routes)[Sometimes the best route isn't a route at all](/router/basics/common-navigation-patterns/#sometimes-the-best-route-isnt-a-route-at-all)