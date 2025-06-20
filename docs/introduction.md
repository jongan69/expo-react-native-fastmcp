Introduction to Expo Router - Expo Documentation

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

Introduction to Expo Router
===========================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/introduction.mdx)

Expo Router is an open-source routing library for Universal React Native applications built with Expo.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/introduction.mdx)

---

Expo Router is a file-based router for React Native and web applications. It allows you to manage navigation between screens in your app, allowing users to move seamlessly between different parts of your app's UI, using the same components on multiple platforms (Android, iOS, and web).

It brings the best file-system routing concepts from the web to a universal application â allowing your routing to work across every platform. When a file is added to the app directory, the file automatically becomes a route in your navigation.

Features
--------

* Native: Built on top of our powerful [React Navigation suite](https://reactnavigation.org/), Expo Router navigation is truly native and platform-optimized by default.
* Shareable: Every screen in your app is automatically deep linkable. Making any route in your app shareable with links.
* Offline-first: Apps are cached and run offline-first, with automatic updates when you publish a new version. Handles all incoming native URLs without a network connection or server.
* Optimized: Routes are automatically optimized with lazy-evaluation in production, and deferred bundling in development.
* Iteration: Universal Fast Refresh across Android, iOS, and web, along with artifact memoization in the bundler to keep you moving fast at scale.
* Universal: Android, iOS, and web share a unified navigation structure, with the ability to drop-down to platform-specific APIs at the route level.
* Discoverable: Expo Router enables build-time static rendering on web, and universal linking to native. Meaning your app content can be indexed by search engines.

### Using a different navigation library

You can use any other navigation library, like [React Navigation](https://reactnavigation.org/docs/getting-started#installation), in your Expo project. However, if you are building a new app, we recommend using Expo Router for all the features described above. With other navigation libraries, you might have to implement your own strategies for some of these features, such as shareable links or handling web and native navigation in the same project.

If you are looking to use [React Native Navigation by Wix](https://github.com/wix/react-native-navigation), it is not available in Expo Go and is not yet compatible with `expo-dev-client`. We recommend using [`createNativeStackNavigator`](https://reactnavigation.org/docs/native-stack-navigator) from React Navigation to use Android and iOS native navigation APIs.

Common questions
----------------

Expo Router versus Expo versus React Native CLI

Historically, React Native has been non prescriptive about how apps should be built which is similar to using React without a modern web framework. Expo Router is an opinionated framework for React Native, similar to how Remix and Next.js are opinionated frameworks for web-only React.

Expo Router is designed to bring the best architectural patterns to everyone, to ensure React Native is leveraged to its fullest. For example, Expo Router's [Async Routes](/router/reference/async-routes) feature enables lazy bundling for everyone. Previously, lazy bundling was only used at Meta to build the Facebook app.

Can I use Expo Router in my existing React Native app?

Yes, Expo Router is the framework for universal React Native apps. Due to the deep connection between the router and the bundler, Expo Router is only available in Expo CLI projects with Metro. Luckily, you can [use Expo CLI in any React Native project](/bare/using-expo-cli) too!

What are the benefits of file-based routing?

* The file system is a well-known and well-understood concept. The simpler mental model makes it easier to educate new team members and scale your application.
* The fastest way to onboard new users is by having them open a universal link that opens the app or website to the correct screen depending on if they have the app installed or not. This technique is so advanced that it's usually only available to large companies that can afford to make and maintain the parity between platforms. But with Expo's file-based routing, you can have this feature out of the box!
* Refactoring is easier to do because you can move files around without having to update any imports or routing components.
* Expo Router has the ability to statically type routes automatically. This ensures you can only link to valid routes and that you can't link to a route that doesn't exist. Typed Routes also improve refactoring as you'll get type errors if links are broken.
* Async Routes (bundle splitting) improve development speed, especially in larger projects. They also make upgrades easier as errors are isolated to a single route, meaning you can incrementally update or refactor your app page-by-page rather than all at once (traditional React Native).
* Deep links always work, for every page. This makes it possible to share links to any content in the app, which is great for promoting your app, collecting bug reports, E2E testing, automating screenshots, and so on.
* Expo Head uses automatic links to enable deep-native integration. Features like Quick Notes, Handoff, Siri context, and universal links only require configuration setup, no code changes. This enables perfect vertical integration with the entire ecosystem of smart devices that a user has, leading to the types of user experiences that are only possible with universal apps (web â native).
* Expo Router has the ability to statically render each page automatically on the web, enabling real SEO and full discoverability of your app's content. This is only possible because of the file-based convention.
* Expo CLI can infer a lot of information about your application when it follows a known convention. For example, we could implement automatic bundle splitting per route, or automatically generate a sitemap for your website. This is impossible when your app only has a single entry point.
* Re-engagement features like notifications and home screen widgets are easier to integrate as you can simply intercept the launch and deep link, with query parameters, anywhere in the app.
* Like on the web, analytics and error reporting can easily be configured to automatically include the route name, which is useful for debugging and understanding user behavior.

Why should I use Expo Router over React Navigation?

Expo Router and React Navigation are both libraries from the Expo team. We built Expo Router on top of React Navigation to enable the benefits of file-based routing. Expo Router is a superset of React Navigation, meaning you can use any React Navigation components and APIs with Expo Router.

If file-based routing isn't right for your project, you can drop down to React Navigation and set up routes, types, and links manually.

How do I server-render my Expo Router website?

Basic static rendering (SSG) is supported in Expo Router. Server-side rendering currently requires custom infrastructure to set up.

Next steps
----------

[Quick start

Learn how to quickly get started using Expo Router.](/router/installation#quick-start)
[Manual installation

Detailed instructions on how to get started and add Expo Router to your existing app.](/router/installation#manual-installation)
[Example app

See the source code for the example app on GitHub.](https://github.com/expo/expo/tree/main/templates/expo-template-tabs)

[Previous (Development process - Reference)

React Compiler](/guides/react-compiler)[Next (Expo Router)

Installation](/router/installation)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/introduction.mdx)
* Last updated on December 18, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).