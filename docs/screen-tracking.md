Screen tracking for analytics - Expo Documentation

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

[Error handling](/router/error-handling)[URL parameters](/router/reference/url-parameters)[Redirects](/router/reference/redirects)[Static Rendering](/router/reference/static-rendering)[Async routes](/router/reference/async-routes)[API Routes](/router/reference/api-routes)[Sitemap](/router/reference/sitemap)[Typed routes](/router/reference/typed-routes)[Screen tracking for analytics](/router/reference/screen-tracking)[Top-level src directory](/router/reference/src-directory)[Testing](/router/reference/testing)[Troubleshooting](/router/reference/troubleshooting)

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

Screen tracking for analytics
=============================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/reference/screen-tracking.mdx)

Learn how to enable screen tracking for analytic when using Expo Router.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/reference/screen-tracking.mdx)

---

Unlike React Navigation, Expo Router always has access to a URL. This means screen tracking is as easy as the web.

1. Create a higher-order component that observes the currently selected URL
2. Track the URL in your analytics provider

`app`

â`_layout.tsx`

app/\_layout.tsx

Copy

```
import { useEffect } from 'react';
import { usePathname, useGlobalSearchParams, Slot } from 'expo-router';

export default function Layout() {
  const pathname = usePathname();
  const params = useGlobalSearchParams();

  // Track the location in your analytics provider here.
  useEffect(() => {
    analytics.track({ pathname, params });
  }, [pathname, params]);

  // Export all the children routes in the most basic way.
  return <Slot />;
}

```

Now when the user changes routes, the analytics provider will be notified.

Migrating from React Navigation
-------------------------------

React Navigation's [screen tracking guide](https://reactnavigation.org/docs/screen-tracking/) cannot make the same assumptions about the navigation state that Expo Router can. As a result, the implementation requires the use of `onReady` and `onStateChange` callbacks. Avoid using these methods if possible as the root `<NavigationContainer />` is not directly exposed and allows cascading in Expo Router.

[Previous (Expo Router - Reference)

Typed routes](/router/reference/typed-routes)[Next (Expo Router - Reference)

Top-level src directory](/router/reference/src-directory)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/reference/screen-tracking.mdx)
* Last updated on July 10, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).