Expo Router notation - Expo Documentation

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

Expo Router notation
====================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/basics/notation.mdx)

Learn how to use special filenames and notation to expressively define your app's navigation tree within your project's file structure.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/basics/notation.mdx)

---

When you look inside the app directory in a typical Expo Router project, you'll see a lot more than some simple file and directory names. What do the parentheses and brackets mean? Let's learn the significance of file-based routing notation and how it allows you to define complex navigation patterns.

Types of route notation
-----------------------

### Simple names/no notation

`app`

â`home.tsx`

â`feed`

ââ`favorites.tsx`

Regular file and directory names without any notation signify *static routes*. Their URL matches exactly as they appear in your file tree. So, a file named favorites.tsx inside the feed directory will have a URL of `/feed/favorites`.

### Square brackets

`app`

â`[userName].tsx`

â`products`

ââ`[productId]`

âââ`index.tsx`

If you see square brackets in a file or directory name, you are looking at a *dynamic route*. The name of the route includes a parameter that can be used when rendering the page. The parameter could be either in a directory name or a file name. For example, a file named [userName].tsx will match `/evanbacon`, `/expo`, or another username. Then, you can access that parameter with the `useLocalSearchParams` hook inside the page, using that to load the data for that specific user.

### Parentheses

`app`

â`(tabs)`

ââ`index.tsx`

ââ`settings.tsx`

A directory with its name surrounded in parentheses indicates a *route group*. These directories are useful for grouping routes together without affecting the URL. For example, a file named app/(tabs)/settings.tsx will have `/settings` for its URL, even though it is not directly in the app directory.

Route groups can be useful for simple organization purposes, but often become more important for defining complex relationships between routes.

### index.tsx files

`app`

â`(tabs)`

ââ`index.tsx`

â`profile`

ââ`index.tsx`

Just like on the web, an index.tsx file indicates the default route for a directory. For example, a file named profile/index.tsx will match `/profile`. A file named (tabs)/index.tsx will match `/`, effectively becoming the default route for your entire app.

### \_layout.tsx files

`app`

â`_layout.tsx`

â`(tabs)`

ââ`_layout.tsx`

â`feed`

ââ`_layout.tsx`

\_layout.tsx files are special files that are not pages themselves but define how groups of routes inside a directory relate to each other. If a directory of routes is arranged as a stack or tabs, the layout route is where you would define that relationship by using a stack navigator or tab navigator component.

Layout routes are rendered before the actual page routes inside their directory. This means that the \_layout.tsx directly inside the app directory is rendered before anything else in the app, and is where you would put the initialization code that may have previously gone inside an App.jsx file.

### Plus sign

`app`

â`+not-found.tsx`

â`+native-intent.tsx`

Routes starting with a `+` have special significance to Expo Router, and are used for specific purposes. One example is [`+not-found`](/router/error-handling#unmatched-routes), which catches any requests that don't match a route in your app. [`+html`](/router/reference/static-rendering#root-html) is used to customize the HTML boilerplate used by your app on web. [`+native-intent`](/router/advanced/native-intent) is used to handle deep links into your app that don't match a specific route, such as links generated by third party services.

Route notation applied
----------------------

Consider the following project file structure to identify the different types of routes represented:

`app`

â`(tabs)`

ââ`_layout.tsx`

ââ`index.tsx`

ââ`feed.tsx`

ââ`profile.tsx`

â`_layout.tsx`

â`users`

ââ`[userId].tsx`

â`+not-found.tsx`

â`about.tsx`

* app/about.tsx is a static route that matches `/about`.
* app/users/[userId].tsx is a dynamic route that matches `/users/123`, `/users/456`, and so on.
* app/(tabs) is a route group. It will not factor into the URL, so `/feed` will match app/(tabs)/feed.tsx.
* app/(tabs)/index.tsx is the default route for the (tabs) directory, so it will be the initially-focused tab, and will match the `/` URL.
* app/(tabs)/\_layout.tsx is a layout file defining how the three pages inside app/(tabs)/ relate to each other. If you use a tab navigator component inside of this file, then those screens will be arranged as tabs.
* app/\_layout.tsx is the root layout file, and is rendered before any other route in the app.
* +not-found.tsx is a special route that will be displayed if the user navigates to a route that doesn't exist in your app.

[Previous (Expo Router - Router 101)

Core concepts](/router/basics/core-concepts)[Next (Expo Router - Router 101)

Layout](/router/basics/layout)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/basics/notation.mdx)
* Last updated on May 05, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Types of route notation](/router/basics/notation/#types-of-route-notation)[Simple names/no notation](/router/basics/notation/#simple-namesno-notation)[Square brackets](/router/basics/notation/#square-brackets)[Parentheses](/router/basics/notation/#parentheses)[index.tsx files](/router/basics/notation/#indextsx-files)[\_layout.tsx files](/router/basics/notation/#_layouttsx-files)[Plus sign](/router/basics/notation/#plus-sign)[Route notation applied](/router/basics/notation/#route-notation-applied)