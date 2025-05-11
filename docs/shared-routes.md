Shared routes - Expo Documentation

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

Shared routes
=============

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/advanced/shared-routes.mdx)

Learn how to define shared routes or use arrays to use the same route multiple times with different layouts using Expo Router.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/advanced/shared-routes.mdx)

---

To match the same URL with different layouts, use [groups](/router/basics/notation#parentheses) with overlapping child routes. This pattern is very common in native apps. For example, in the X app, a profile can be viewed in every tab (such as home, search, and profile). However, there is only one URL that is required to access this route.

In the example below, app/\_layout.tsx is the tab bar and each route has its own header. The app/(profile)/[user].tsx route is shared between each tab.

`app`

â`_layout.tsx`

â`(home)`

ââ`_layout.tsx`

ââ`[user].tsx`

â`(search)`

ââ`_layout.tsx`

ââ`[user].tsx`

â`(profile)`

ââ`_layout.tsx`

ââ`[user].tsx`

> When reloading the page, the first alphabetical match is rendered.

Shared routes can be navigated directly by including the group name in the route. For example, `/(search)/baconbrix` navigates to `/baconbrix` in the "search" layout.

Arrays
------

> Array syntax is an advanced concept that is unique to native app development.

Instead of defining the same route multiple times with different layouts, use the array syntax `(,)` to duplicate the children of a group. For example, `app/(home,search)/[user].tsx` â creates `app/(home)/[user].tsx` and `app/(search)/[user].tsx` in memory.

To distinguish between the two routes use a layout's `segment` prop:

app/(home,search)/\_layout.tsx

Copy

```
export default function DynamicLayout({ segment }) {
  if (segment === '(search)') {
    return <SearchStack />;
  }

  return <Stack />;
}

```

To enable the array syntax, specify the [`initialRouteName`](/router/advanced/router-settings#initialroutename) for each group using `unstable_settings` object in the dynamic layout:

app/(home,search)/\_layout.tsx

Copy

```
export const unstable_settings = {
  initialRouteName: 'home',
  search: {
    initialRouteName: 'search',
  },
};

export default function DynamicLayout({ segment }) {
  %%placeholder-start%% ... %%placeholder-end%%
}

```

In the above example, the `home` route is the default route for the `home` group and the app. The `search` route is the default route for the `search` group.

Key points
----------

* You can only provide groups for the current navigator.
* When using the array syntax, if there are two groups (for example, `(one)/(two)`), only the last group's segment is used for matching the route.
* If there are at least two group `initialRouteNames`, but a default `initialRouteName` is not provided, the first group's `initialRouteName` is used.

[Previous (Expo Router - Navigation patterns)

Modals](/router/advanced/modals)[Next (Expo Router - Navigation patterns)

Protected routes](/router/advanced/protected)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/advanced/shared-routes.mdx)
* Last updated on April 03, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Arrays](/router/advanced/shared-routes/#arrays)[Key points](/router/advanced/shared-routes/#key-points)