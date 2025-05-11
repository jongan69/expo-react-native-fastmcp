Linking into your app - Expo Documentation

[Docs](/)

[Blog](https://expo.dev/blog)[Changelog](https://expo.dev/changelog)[Star Us on GitHub](https://github.com/expo/expo)

Search

[Home](/)[Guides](/guides/overview)[EAS](/eas)[Reference](/versions/latest)[Learn](/tutorial/overview)

[Overview](/guides/overview)

Development process

[Develop an app with Expo](/workflow/overview)[Configure with app config](/workflow/configuration)[Continuous Native Generation](/workflow/continuous-native-generation)[Using libraries](/workflow/using-libraries)[Privacy manifests](/guides/apple-privacy)[Permissions](/guides/permissions)[Environment variables](/guides/environment-variables)

Linking

[Overview](/linking/overview)[Into other apps](/linking/into-other-apps)[Into your app](/linking/into-your-app)[Android App Links](/linking/android-app-links)[iOS Universal Links](/linking/ios-universal-links)

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

Linking into your app
=====================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/linking/into-your-app.mdx)

Learn how to handle an incoming URL in your React Native and Expo app by creating a deep link.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/linking/into-your-app.mdx)

---

This guide provides steps to configure standard deep links in your project by adding a custom scheme.

> For most apps, you probably want to set up [Android App/iOS Universal Links](/linking/overview#universal-linking) instead of the deep links described in this guide or set up both.

Add a custom scheme in app config
---------------------------------

To provide a link to your app, add a custom string to the [`scheme`](/versions/latest/config/app#scheme) property in the [app config](/workflow/configuration):

app.json

Copy

```
{
  "expo": {
    "scheme": "myapp"
  }
}

```

After adding a custom scheme to your app, you need to [create a new development build](/develop/development-builds/create-a-build). Once the app is installed on a device, you can open links within your app using `myapp://`.

If the custom scheme is not defined, the app will use `android.package` and `ios.bundleIdentifier` as the default schemes in both development and production builds. This is because [Expo Prebuild](/workflow/prebuild) automatically adds these properties as custom schemes for Android and iOS.

Test the deep link
------------------

You can test a link that opens your app using [`npx uri-scheme`](https://github.com/expo/expo/tree/main/packages/uri-scheme#readme), which is a command-line utility for interacting and testing URI schemes.

For example, if your app has a `/details` screen that you want to open when a user taps on a link (either through another app or a web browser), you can test this behavior by running the following command:

Terminal

`# If you have `android.package` or `ios.bundleIdentifier` defined in your app.json`

`-Â``npx uri-scheme open com.example.app://somepath/details --android`

  
`# If you have a `scheme` defined in your app.json`

`-Â``npx uri-scheme open myapp://somepath/details --ios`

Running the above command:

* Opens your app's `/details` screen
* The `android` or `ios` options specify that the link should be opened on Android or iOS
* Alternatively, you can try opening the link by clicking a link like `<a href="scheme://">Click me</a>` in the device's web browser. Note that entering the link in the address bar may not work as expected, and you can use [universal linking](/linking/overview#universal-linking) to implement that ability.

Test a link using Expo Go

By default, [Expo Go](https://expo.dev/go) uses the `exp://` scheme. If you link to `exp://` without specifying a URL address afterward, it will open the app to the home screen. In development, your app's complete URL looks like `exp://127.0.0.1:8081`.

To open the `/details` screen while testing on Expo Go, you can use `npx uri-scheme`:

Terminal

Copy

`-Â``npx uri-scheme open exp://127.0.0.1:8081/--/somepath/into/app?hello=world --ios`

In Expo Go, `/--/` is added to the URL when a path is specified. This indicates to Expo Go that the substring after it corresponds to the deep link path and is not part of the path to the app itself.

By default, `exp://` is replaced with `http://` when opening a URL in Expo Go. You can also use `exps://` to open `https://` URLs. However, `exps://` does not currently support loading sites with insecure TLS certificates.

Handle URLs
-----------

> If you are using [Expo Router](/linking/overview#use-expo-router-to-handle-deep-linking), you can ignore this section.

You can observe links that launch your app using the [`Linking.useURL()`](/versions/latest/sdk/linking#useurl) hook from [`expo-linking`](/versions/latest/sdk/linking).

index.tsx

Copy

```
import * as Linking from 'expo-linking';

export default function Home() {
  const url = Linking.useURL();

  return <Text>URL: {url}</Text>;
}

```

The `Linking.useURL()` hook works behind the scenes by following these imperative methods:

* The link that launched the app is initially returned using [`Linking.getInitialURL()`](/versions/latest/sdk/linking#linkinggetinitialurl)
* Any new links triggered while the app is already open are observed with [`Linking.addEventListener('url', callback)`](/versions/latest/sdk/linking#linkingaddeventlistenertype-handler)

Parse URLs
----------

You can use the [`Linking.parse()`](/versions/latest/sdk/linking#linkingparseurl) method to parse the path, hostname, and query parameters from a URL. This method extracts deep linking information and considers nonstandard implementations.

index.tsx

Copy

```
import * as Linking from 'expo-linking';

export default function Home() {
  const url = Linking.useURL();

  if (url) {
    const { hostname, path, queryParams } = Linking.parse(url);

    console.log(
      `Linked to app with hostname: ${hostname}, path: ${path} and data: ${JSON.stringify(
        queryParams
      )}`
    );
  }

  return (
    %%placeholder-start%%Your React component here. %%placeholder-end%%
  )
}

```

Limitations
-----------

If a user does not have your app installed, deep links to your app will not work. Attribution services like [Branch](https://www.branch.io/deep-linking/) offer solutions for conditionally linking to your app or web page.

Android App/iOS Universal Links is another solution you can use to handle such cases. This type of linking allows your app to open when a user clicks follows an HTTP(S) link pointing to your web domain. If the user doesn't have your app installed, the link takes them to your website. For more details, see [universal linking](/linking/overview#universal-linking).

[Previous (Development process - Linking)

Into other apps](/linking/into-other-apps)[Next (Development process - Linking)

Android App Links](/linking/android-app-links)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/linking/into-your-app.mdx)
* Last updated on February 11, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Add a custom scheme in app config](/linking/into-your-app/#add-a-custom-scheme-in-app-config)[Test the deep link](/linking/into-your-app/#test-the-deep-link)[Handle URLs](/linking/into-your-app/#handle-urls)[Parse URLs](/linking/into-your-app/#parse-urls)[Limitations](/linking/into-your-app/#limitations)