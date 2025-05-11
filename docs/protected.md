Protected routes - Expo Documentation

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

Protected routes
================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/advanced/protected.mdx)

Learn how to make screens inaccessible to client-side navigation.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/advanced/protected.mdx)

---

> Protected routes are available in SDK 53 and above.

Protected screens allow you to prevent users from accessing certain routes using client-side navigation. If a user tries to navigate to a protected screen, or if a screen becomes protected while it is active, they will be redirected to the anchor route (usually the index screen) or the first available screen in the stack.

`app`

â`_layout.tsx`

â`index.tsx`

â`about.tsx`

â`login.tsx``Should only be available while not authenticated`

â`private`

ââ`_layout.tsx``Should only be available while authenticated`

ââ`index.tsx`

ââ`page.tsx`

app/\_layout.tsx

Copy

```
export { Stack } from 'expo-router';

const isLoggedIn = false;

export function AppLayout() {
  return (
    <Stack>
      <Stack.Protected guard={!isLoggedIn}>
        <Stack.Screen name="login" />
      </Stack.Protected>

      <Stack.Protected guard={isLoggedIn}>
        <Stack.Screen name="private" />
      </Stack.Protected>
      {/* Expo Router includes all routes by default. Adding Stack.Protected creates exceptions for these screens. */}
    </Stack>
  );
}

```

In this example, the `/private` route is inaccessible because the `guard` is false. When a user attempts to access `/private`, they are redirected to the anchor route, which is the index screen.

Additionally, if the user is on `/private/page` and the `guard` condition changes to false, they will be redirected automatically.

When a screen's guard is changed from true to false, all it's history entries will be removed from the navigation history.

Multiple protected screens
--------------------------

In Expo Router, a screen can only exist in one active route group at a time.

You should only declare a screen only once, in the most appropriate group or stack. If a screen's availability depends on logic, wrap it in a conditional group instead of duplicating the screen.

app/\_layout.tsx

Copy

```
export { Stack } from 'expo-router';

const isLoggedIn = true;
const isAdmin = true;

export function AppLayout() {
  return (
    <Stack>
      <Stack.Protected guard={true}>
        <Stack.Screen name="profile" />
      </Stack.Protected>
      <Stack.Screen name="profile" /> // â Not allowed: duplicate screen
    </Stack>
  );
}

```

Nesting protected screens
-------------------------

Protected screens can be nested to define hierarchical access control logic.

app/\_layout.tsx

Copy

```
export { Stack } from 'expo-router';

const isLoggedIn = true;
const isAdmin = true;

export function AppLayout() {
  return (
    <Stack>
      <Stack.Protected guard={isLoggedIn}>
        <Stack.Protected guard={isAdmin}>
          <Stack.Screen name="protected" />
        </Stack.Protected>

        <Stack.Screen name="about" />
      </Stack.Protected>
    </Stack>
  );
}

```

In this case:

* `/private` is only protected if the user is logged in and is an admin.
* `/about` is protected to any logged-in user.

Falling back to a specific screen
---------------------------------

You can configure the navigator to fall back to a specific screen if access is denied.

`app`

â`_layout.tsx`

â`index.tsx`

â`about.tsx`

â`login.tsx`

â`private`

ââ`_layout.tsx`

ââ`index.tsx`

ââ`page.tsx`

app/\_layout.tsx

Copy

```
export { Stack } from 'expo-router';

const isLoggedIn = false;

export function AppLayout() {
  return (
    <Stack>
      <Stack.Protected guard={isLoggedIn}>
        <Stack.Screen name="index" />
        <Stack.Screen name="private" />
      </Stack.Protected>

      <Stack.Screen name="login" />
    </Stack>
  );
}

```

Here, because the index screen is protected and the protected is false, the router redirects to the first available screen â login.

Static rendering considerations
-------------------------------

Protected screens are evaluated on the client side only. During static site generation, no HTML files are created for protected routes. However, if users know the URLs of these routes, they can still request the corresponding HTML or JavaScript files directly. Protected screens are not a replacement for server-side authentication or access control.

[Previous (Expo Router - Navigation patterns)

Shared routes](/router/advanced/shared-routes)[Next (Expo Router - Advanced)

Platform-specific Modules](/router/advanced/platform-specific-modules)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/advanced/protected.mdx)
* Last updated on May 07, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Multiple protected screens](/router/advanced/protected/#multiple-protected-screens)[Nesting protected screens](/router/advanced/protected/#nesting-protected-screens)[Falling back to a specific screen](/router/advanced/protected/#falling-back-to-a-specific-screen)[Static rendering considerations](/router/advanced/protected/#static-rendering-considerations)