Async routes - Expo Documentation

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

Async routes
============

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/reference/async-routes.mdx)

Learn how to speed up development with async bundling in Expo Router.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/reference/async-routes.mdx)

---

> Async routes is an experimental feature.

Expo Router can automatically split your JavaScript bundle based on the route files using [React Suspense](https://react.dev/reference/react/Suspense). This enables faster development as only the routes you navigate to will be bundled or loaded into memory. This can also be useful for reducing the initial bundle size for your application.

Apps using the Hermes Engine will not benefit as much from bundle splitting as the bytecode is already memory mapped ahead of time. However, it will improve your over-the-air updates, React Server Components, and web support.

> When bundling for production on native platforms, all suspense boundaries will be disabled and there will be no loading states.

How it works
------------

All Routes are wrapped inside a suspense boundary and are loaded asynchronously. This means that the first time you navigate to a route, it will take a little longer to load. However, once it is loaded, it will be cached and subsequent visits will be instant.

Loading errors are handled in the parent route, via the [`ErrorBoundary`](/router/error-handling#errorboundary) export.

Async routes cannot be statically analyzed during development, so all files will be treated as routes even if they don't export a default component. After the component is bundled and loaded, any invalid route will use a fallback warning screen.

For those familiar with advanced bundling techniques, the async routes feature is composed of [React Suspense](https://react.dev/docs/concurrent-mode-suspense), [route-based bundle splitting](https://legacy.reactjs.org/docs/code-splitting.html#route-based-code-splitting) and [lazy bundling](https://github.com/react-native-community/discussions-and-proposals/blob/main/proposals/0605-lazy-bundling.md) (in development).

Setup
-----

Enable the feature by setting the `asyncRoutes` option in the Expo Router config plugin of your [app config](/versions/latest/config/app):

> Set `asyncRoutes` to `true` to enable production bundle splitting.

app.json

Copy

```
{
  "expo": {
    "plugins": [
      [
        "expo-router",
        {
          "origin": "https://acme.com",
          "asyncRoutes": {
            "web": true,
            "default": "development"
          }
        }
      ]
    ]
  }
}

```

You can set platform-specific settings (`default`, `android`, `ios` or `web`) for `asyncRoutes` using an object:

app.json

Copy

```
{
  "expo": {
    "plugins": [
      [
        "expo-router",
        {
          "origin": "https://acme.com",
          "asyncRoutes": {
            "web": true,
            "android": false,
            "default": "development"
          }
        }
      ]
    ]
  }
}

```

Then, when you are about to start your project, you can use the `--clear` flag to clear the Metro cache. This will ensure that the routes are loaded asynchronously:

Terminal

`-Â``npx expo start --clear`

  
`# Or when exporting`

`-Â``npx expo export --clear`

Static rendering
----------------

Static rendering is supported in production web apps by rendering all Suspense boundaries synchronously in Node.js, then linking all of async chunks together in the HTML based on all the selected routes for a given HTML file. This ensures you don't encounter a waterfall of loading states on server navigations. Subsequent navigations will recursively load any missing chunks.

To ensure a consistent first render, all layout routes leading up to the leaf route for a URL will be included in the initial server response.

All initial routes, defined with `unstable_settings = { initialRouteName: '...' }` will be included in the initial HTML file as they are required for the first render. For example, if the server request is for a modal, the screen rendered under the modal will also be included to ensure the modal is rendered correctly.

Caveats
-------

Async Routes represents an early preview of how we plan to support [React Server Components](https://react.dev/blog/2023/03/22/react-labs-what-we-have-been-working-on-march-2023#react-server-components) in the future. As such, there are some caveats to be aware of:

* Async Routes do not support native production apps yet.
* In development, the runtime JavaScript is lazily bundled so you may encounter cases where the HTML doesn't match the available JavaScript.
* The loading state cannot be customized at this time.

[Previous (Expo Router - Reference)

Static Rendering](/router/reference/static-rendering)[Next (Expo Router - Reference)

API Routes](/router/reference/api-routes)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/reference/async-routes.mdx)
* Last updated on May 07, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[How it works](/router/reference/async-routes/#how-it-works)[Setup](/router/reference/async-routes/#setup)[Static rendering](/router/reference/async-routes/#static-rendering)[Caveats](/router/reference/async-routes/#caveats)