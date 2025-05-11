Error handling - Expo Documentation

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

Error handling
==============

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/error-handling.mdx)

Learn how to handle unmatched routes and errors in your app when using Expo Router.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/error-handling.mdx)

---

This guide specifies how to handle unmatched routes and errors in your app when using Expo Router.

Unmatched routes
----------------

![An example of unmatched routes displayed on all platforms.](/static/images/expo-router/unmatched.png)

Native apps don't have a server so there are technically no 404s. However, if you're implementing a router universally, then it makes sense to handle missing routes. This is done automatically for each app, but you can also customize it.

app/+not-found.tsx

Copy

```
import { Unmatched } from 'expo-router';
export default Unmatched;

```

This will render the default `Unmatched`. You can export any component you want to render instead. We recommend having a link to `/` so users can navigate back to the home screen.

### Route priority

On web, files are served in the following order:

1. Static files in the public directory.
2. Standard and dynamic routes in the app directory.
3. [API routes](/router/reference/api-routes) in the app directory.
4. Not-found routes will be served last with a 404 status code.

Error handling
--------------

Expo Router enables fine-tuned error handling to enable a more opinionated data-loading strategy in the future.

![Using ErrorBoundary in Expo Router to catch errors in a route component.](/static/images/expo-router/error-boundaries.png)

You can export a nested [`ErrorBoundary`](/versions/latest/sdk/router#errorboundary) component from any route to intercept and format component-level errors using [React Error Boundaries](https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary):

app/home.tsx

Copy

```
import { View, Text } from 'react-native';
import { type ErrorBoundaryProps } from 'expo-router';

export function ErrorBoundary({ error, retry }: ErrorBoundaryProps) {
  return (
    <View style={{ flex: 1, backgroundColor: "red" }}>
      <Text>{error.message}</Text>
      <Text onPress={retry}>Try Again?</Text>
    </View>
  );
}

export default function Page() { ... }

```

When you export an `ErrorBoundary` the route will be wrapped with a React Error Boundary effectively:

Virtual

Copy

```
function Route({ ErrorBoundary, Component }) {
  return (
    <Try catch={ErrorBoundary}>
      <Component />
    </Try>
  );
}

```

When `ErrorBoundary` is not present, the error will be thrown to the nearest parent's `ErrorBoundary` and accepts [`error`](/versions/latest/sdk/router#error) and [`retry`](/versions/latest/sdk/router#retry) props.

### Work in progress

React Native LogBox needs to be presented less aggressively to develop with errors. Currently, it shows for `console.error` and `console.warn`. However, it should ideally only show for uncaught errors.

[Previous (Expo Router - Advanced)

Custom tabs](/router/advanced/custom-tabs)[Next (Expo Router - Reference)

URL parameters](/router/reference/url-parameters)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/error-handling.mdx)
* Last updated on March 24, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Unmatched routes](/router/error-handling/#unmatched-routes)[Route priority](/router/error-handling/#route-priority)[Error handling](/router/error-handling/#error-handling)[Work in progress](/router/error-handling/#work-in-progress)