Router settings - Expo Documentation

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

[Platform-specific Modules](/router/advanced/platform-specific-modules)[Customizing links](/router/advanced/native-intent)[Settings](/router/advanced/router-settings)[Apple Handoff](/router/advanced/apple-handoff)[Custom tabs](/router/advanced/custom-tabs)

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

Router settings
===============

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/advanced/router-settings.mdx)

Learn how to configure layouts with static properties in Expo Router.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/advanced/router-settings.mdx)

---

> Warning: `unstable_settings` currently do not work with [async routes](/router/reference/async-routes) (development-only). This is why the feature is designated *unstable*.

### `initialRouteName`

When deep linking to a route, you may want to provide a user with a "back" button. The `initialRouteName` sets the default screen of the stack and should match a valid filename (without the extension).

`app`

â`_layout.tsx`

â`index.tsx`

â`other.tsx`

app/\_layout.tsx

Copy

```
import { Stack } from 'expo-router';

export const unstable_settings = {
  // Ensure any route can link back to `/`
  initialRouteName: 'index',
};

export default function Layout() {
  return <Stack />;
}

```

Now deep linking directly to `/other` or reloading the page will continue to show the back arrow.

When using [array syntax](/router/advanced/shared-routes#arrays) `(foo,bar)` you can specify the name of a group in the `unstable_settings` object to target a particular segment.

other.tsx

Copy

```
export const unstable_settings = {
  // Used for `(foo)`
  initialRouteName: 'first',
  // Used for `(bar)`
  bar: {
    initialRouteName: 'second',
  },
};

```

The `initialRouteName` is only used when deep-linking to a route. During app navigation, the route you are navigating to will be the initial route. You can disable this behavior using the `initial` prop on the `<Link />` component or by passing the option to the imperative APIs.

```
// If this navigates to a new _layout, don't override the initial route
<Link href="/route" initial={false} />;

router.push('/route', { overrideInitialScreen: false });

```

[Previous (Expo Router - Advanced)

Customizing links](/router/advanced/native-intent)[Next (Expo Router - Advanced)

Apple Handoff](/router/advanced/apple-handoff)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/advanced/router-settings.mdx)
* Last updated on April 03, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).