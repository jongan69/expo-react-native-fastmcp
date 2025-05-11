Sitemap - Expo Documentation

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

Sitemap
=======

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/reference/sitemap.mdx)

Learn how to use the sitemap to debug your app with Expo Router.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/reference/sitemap.mdx)

---

On native, you can use the [`uri-scheme`](https://www.npmjs.com/package/uri-scheme) CLI to test opening native links on a device.

For example, if you want to launch the Expo Go app on iOS to the `/form-sheet` route, run:

Terminal

Copy

`-Â``npx uri-scheme open exp://192.168.87.39:19000/--/form-sheet --ios`

> Replace `192.168.87.39:19000` with the IP address shown when running `npx expo start`.

You can also search for links directly in a browser like Safari or Chrome to test deep linking on physical devices. Learn more about [testing deep links](https://reactnavigation.org/docs/deep-linking).

Sitemap
-------

![Directory structure](/static/images/expo-router/directory.png)

Expo Router currently injects a /\_sitemap automatically that provides a list of all routes in the app. This is useful for debugging.

In SDK 52 and above, the sitemap can be removed by adding `sitemap: false` to the `expo-router` config plugin in the app config:

app.json

Copy

```
{
  "plugins": [
    [
      "expo-router",
      {
        "sitemap": false
      }
    ]
  ]
}

```

In SDK 51 and below, the sitemap can be removed by creating an empty \_sitemap file inside the app directory:

app/\_sitemap.tsx

Copy

```
export default function Sitemap() {
  return null;
}

```

[Previous (Expo Router - Reference)

API Routes](/router/reference/api-routes)[Next (Expo Router - Reference)

Typed routes](/router/reference/typed-routes)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/reference/sitemap.mdx)
* Last updated on April 28, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).