Core concepts of file-based routing - Expo Documentation

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

Core concepts of file-based routing
===================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/basics/core-concepts.mdx)

Learn the ground rules of Expo Router and how it relates to the rest of your code.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/basics/core-concepts.mdx)

---

Before diving into how to construct your app's navigation tree with Expo Router, let's first understand the core concepts that make up the foundation of file-based routing in Expo Router, and how an Expo Router project might differ in structure from other React Native projects.

The rules of Expo Router
------------------------

### 1. All screens/pages are files inside of app directory

All navigation routes in your app are defined by the files and sub-directories inside the app directory. Every file inside the app directory has a default export that defines a distinct page in your app (except for the special \_layout files).

Accordingly, directories inside app define groups of related screens together as stacks, tabs, or in other arrangements.

### 2. All pages have a URL

All pages have a URL path that matches the file's location in the app directory, which can be used to navigate to that page in the address bar on the web, or as an app-specific deep link in a native mobile app. This is what is meant by Expo Router supporting "universal deep-linking". All pages in your app can be navigated to with a URL, regardless of the platform.

### 3. First index.tsx is the initial route

With Expo Router, you do not define an initial route or first screen in code. Rather, when you open your app, Expo Router will look for the first index.tsx file matching the `/` URL. This could be an app/index.tsx file, but it doesn't have to be. If the user should start by default in a deeper part of your navigation tree, you can use a [route group](/router/basics/notation#parentheses) (a directory where the name is surrounded in parenthesis), and that will not count as part of the URL. If you want your first screen to be a group of tabs, you might put all of the tab pages inside the app/(tabs) directory and define the default tab as index.tsx. With this arrangement, the `/` URL will take the user directly to app/(tabs)/index.tsx file.

### 4. Root \_layout.tsx replaces App.jsx/tsx

Every project should have a \_layout.tsx file directly inside the app directory. This file is rendered before any other route in your app and is where you would put the initialization code that may have previously gone inside an App.jsx file, such as loading fonts or interacting with the splash screen.

### 5. Non-navigation components live outside of app directory

In Expo Router, the app directory is exclusively for defining your app's routes. Other parts of your app, like components, hooks, utilities, and so on, should be placed in other top-level directories. If you put a non-route inside of the app directory, Expo Router will attempt to treat it like a route.

Alternatively, you can create a [top-level src directory](/router/reference/src-directory) and put your routes inside the src/app directory, with non-route components going in folders like src/components, src/utils, and so on. This is the only other directory structure that Expo Router will recognize.

### 6. It's still React Navigation under the hood

While this may sound quite a bit different from React Navigation, Expo Router is actually built on top of React Navigation. You can think of Expo Router as an Expo CLI optimization that translates your file structure into React Navigation components that you previously defined in your own code.

This also means that you can often refer to React Navigation documentation for how to style or configure navigation, as the default stack and tab navigators use the exact same options.

The rules of Expo Router applied
--------------------------------

Let's apply these foundational rules of Expo Router to quickly identify key elements of the following project file structure:

`app`

â`index.tsx`

â`home.tsx`

â`_layout.tsx`

â`profile`

ââ`friends.tsx`

`components`

â`TextField.tsx`

â`Toolbar.tsx`

* app/index.tsx is the initial route, and will appear first when you open the app or navigate to your web app's root URL.
* app/home.tsx is a page with the route `/home`, so you can navigate to it with a URL like `yourapp.com/home` in the browser, or `myapp://home` in a native app.
* app/\_layout.tsx is the root layout. Any initialization code you may have previously put in App.jsx should go here.
* app/profile/friends.tsx is a page with the route `/profile/friends`.
* TextField.tsx and Toolbar.tsx are not in the app directory, so they will not be considered pages. They will not have a URL, and they cannot be the target of a navigation action. However, they can be used as components in the pages inside of the app directory.

[Previous (Expo Router)

Installation](/router/installation)[Next (Expo Router - Router 101)

Router notation](/router/basics/notation)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/basics/core-concepts.mdx)
* Last updated on April 07, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[The rules of Expo Router](/router/basics/core-concepts/#the-rules-of-expo-router)[1. All screens/pages are files inside of app directory](/router/basics/core-concepts/#1-all-screenspages-are-files-inside-of-app-directory)[2. All pages have a URL](/router/basics/core-concepts/#2-all-pages-have-a-url)[3. First index.tsx is the initial route](/router/basics/core-concepts/#3-first-indextsx-is-the-initial-route)[4. Root \_layout.tsx replaces App.jsx/tsx](/router/basics/core-concepts/#4-root-_layouttsx-replaces-appjsxtsx)[5. Non-navigation components live outside of app directory](/router/basics/core-concepts/#5-non-navigation-components-live-outside-of-app-directory)[6. It's still React Navigation under the hood](/router/basics/core-concepts/#6-its-still-react-navigation-under-the-hood)[The rules of Expo Router applied](/router/basics/core-concepts/#the-rules-of-expo-router-applied)