Top-level src directory - Expo Documentation

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

Top-level src directory
=======================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/reference/src-directory.mdx)

Learn how to use a top-level src directory in your Expo Router project.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/reference/src-directory.mdx)

---

As your project grows, it can be helpful to move all the directories containing application code into a single src directory. Expo Router supports this out of the box.

`src`

â`app`

ââ`_layout.tsx`

ââ`index.tsx`

â`components`

ââ`button.tsx`

`package.json`

Simply move your app directory to src/app and restart the development server.

Terminal

`-Â``npx expo start`

  
`# Or export for production`

`-Â``npx expo export`

Notes:

* The config files (app.config.tsx, app.json, package.json, metro.config.js, tsconfig.json) should remain in the root directory.
* The src/app directory takes higher precedence than the root app directory. Only the src/app directory will be used if you have both.
* The public directory should remain in the root directory.
* Static rendering will automatically use the src/app directory if it exists.
* You may consider updating any [type aliases](/guides/typescript#path-aliases) to point to the src directory instead of the root directory.

Custom directory
----------------

> Changing the default root directory is highly discouraged. We will not accept bug reports regarding projects with custom root directories.

You can dangerously customize the root directory using the Expo Router Config Plugin. The following will change the root directory to src/routes, relative to the project root.

app.json

Copy

```
{
  "plugins": [
    [
      "expo-router",
      {
        "root": "./src/routes"
      }
    ]
  ]
}

```

This may lead to unexpected behavior. Many tools assume the root directory to be either app or src/app. Only tools in the exact version of Expo CLI will respect the config plugin.

[Previous (Expo Router - Reference)

Screen tracking for analytics](/router/reference/screen-tracking)[Next (Expo Router - Reference)

Testing](/router/reference/testing)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/reference/src-directory.mdx)
* Last updated on April 28, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).