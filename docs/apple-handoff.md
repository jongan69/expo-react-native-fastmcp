Apple Handoff - Expo Documentation

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

Apple Handoff
=============

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/advanced/apple-handoff.mdx)

Learn how to seamlessly continue app navigation across Apple devices with Expo Router and Apple Handoff.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/advanced/apple-handoff.mdx)

---

Apple Handoff is a feature that enables users to continue browsing your app or website on another device. Expo Router automates all of the runtime routing for this feature. However, the one-time configuration must be set up manually.

In Expo Router, the underlying iOS API (`NSUserActivity`) requires a `webpageUrl` which the OS recommends as the current URL for switching to your app. The `expo-router/head` component has an optional native module that can automatically set the `webpageUrl` to the currently focused route in Expo Router.

#### Platform Compatibility

| Android Device | Android Emulator | iOS Device | iOS Simulator | Web |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

Setup
-----

The following restrictions and considerations are important:

* Handoff is Apple-only.
* Handoff can not be used in the Expo Go app as it requires build-time configuration.
* Handoff requires [universal links](/linking/into-your-app) to be configured, at least on iOS, and contain the `activitycontinuation` object.
* Handoff requires the `expo-router/head` component to be used on each page that you want to support, or in the root layout if you want all pages to be continuous.

To ensure that the public/.well-known/apple-app-site-association file is configured correctly, it must include the `activitycontinuation` key with an `apps` array that contains your app's bundle ID and Team ID formatted as `<APPLE_TEAM_ID>.<IOS_BUNDLE_ID>`. For example, `QQ57RJ5UTD.app.expo.acme` where `QQ57RJ5UTD` is the Team ID and `app.expo.acme` is the bundle identifier.

public/.well-known/apple-app-site-association

Copy

```
{
  "applinks": {
    "details": [
      {
        "appIDs": ["<APPLE_TEAM_ID>.<IOS_BUNDLE_ID>"],
        "components": [
          {
            "/": "*",
            "comment": "Matches all routes"
          }
        ]
      }
    ]
  },
  "activitycontinuation": {
    "apps": ["<APPLE_TEAM_ID>.<IOS_BUNDLE_ID>"]
  },
  "webcredentials": {
    "apps": ["<APPLE_TEAM_ID>.<IOS_BUNDLE_ID>"]
  }
}

```

> The `webcredentials` object is optional but recommended.

You can use the following command to generate the apple-app-site-association file based on your [app config](/versions/latest/config/app):

Terminal

Copy

`-Â``npx setup-safari`

See [Test the deep link](/linking/into-your-app#test-the-deep-link) guide to test handoff in development.

### Expo Head setup

Ensure you set the Handoff origin in your `app.config.tsx` file using the `expo-router` config plugin. This is the URL that will be used for the `webpageUrl` when the user switches to your app.

app.config.tsx

Copy

```
// Be sure to change this to be unique to your project.
process.env.EXPO_TUNNEL_SUBDOMAIN = 'bacon-router-sandbox';

const ngrokUrl = `${process.env.EXPO_TUNNEL_SUBDOMAIN}.ngrok.io`;

/** @type {import('expo/config').ExpoConfig} */
module.exports = {
  // ...
  ios: {
    associatedDomains: [
      `applinks:${ngrokUrl}`,
      `activitycontinuation:${ngrokUrl}`,
      `webcredentials:${ngrokUrl}`,
      // Add additional production-URLs here.
      // `applinks:example.com`,
      // `activitycontinuation:example.com`,
      // `webcredentials:example.com`,
    ],
  },

  plugins: [
    [
      'expo-router',
      {
        // Note: The URL must start with "https://" in "headOrigin"
        headOrigin:
          process.env.NODE_ENV === 'development'
            ? `https://${ngrokUrl}`
            : 'https://my-website-example.com',
      },
    ],
  ],
};

```

> Do not use the development-only `?mode=developer` suffix when testing handoff to native.

After configuring the app config, regenerate your native project with the following command:

Terminal

Copy

`-Â``npx expo prebuild -p ios`

In development, you must start the website before installing the app on your device. This is because when you install the app, the OS will trigger Apple's servers to ping your website for the .well-known/apple-app-site-association file. If the website is not running, the OS will not be able to find the file and handoff will not work. If this happens, rebuild the native app with `npx expo run:ios -d`.

Usage
-----

In any route that you want to support handoff, use the `Head` component from `expo-router/head`:

app/index.tsx

Copy

```
import Head from 'expo-router/head';
import { Text } from 'react-native';

export default function App() {
  return (
    <>
      <Head>
        <meta property="expo:handoff" content="true" />
      </Head>
      <Text>Hello World</Text>
    </>
  );
}

```

### Meta tags

The `expo-router/head` component supports the following meta tags:

| Meta tags | Description |
| --- | --- |
| `expo:handoff` | Set to `true` to enable handoff for the current route. Defaults to `false`. (iOS only) |
| `og:title` and `<title>` | Set the title for the `NSUserActivity` this is unused with handoff. |
| `og:description` | Set the description for the `NSUserActivity` this is unused with handoff. |
| `og:url` | Set the URL that should be opened when the user switches to your app. Defaults to the current URL in-app with `headOrigin` prop in the `expo-router` config plugin, as the baseURL. Passing a relative path will append the `headOrigin` to the path. |

You may want to switch the values between platforms, for that you can use Platform.select:

app/index.tsx

Copy

```
import Head from 'expo-router/head';

export default function App() {
  return (
    <Head>
      <meta
        property="og:url"
        content={Platform.select({ web: 'https://expo.dev', default: null })}
      />
    </Head>
  );
}

```

Debugging
---------

Ensure your Apple devices have [Handoff enabled](https://support.apple.com/en-us/HT209455). You can test this by following the steps below but substituting your app with Safari.

1. Open your native application on your device.
2. Navigate to a route in the app that supports handoff which is rendering the `<Head />` element from Expo Router.
3. To switch to your Mac and click the app's Handoff icon in the Dock.
4. To switch to your iPhone or iPad, open the App Switcher, and tap the app banner at the bottom of the screen.

If you only see the Safari icon in your iPhone's App Switcher, then handoff is not working.

Troubleshooting
---------------

You can test the Apple App Site Association file (public/.well-known/apple-app-site-association) by using a validator such as, [AASA Validator](https://branch.io/resources/aasa-validator/).

If you're having issues, the best thing you can do is enable the most aggressive handoff settings in your app. This ensures that any possible route is linkable. You can do this by making sure that public/.well-known/apple-app-site-association file matches all routes:

public/.well-known/apple-app-site-association

Copy

```
{
  "applinks": {
    "details": [
      {
        "appIDs": ["<APPLE_TEAM_ID>.<IOS_BUNDLE_ID>"],
        "components": [
          {
            "/": "*",
            "comment": "Matches all routes"
          }
        ]
      }
    ]
  }
}

```

In the application, ensure you are not rendering the `<Head />` element conditionally (for example, in an `if/else` block), it must be rendered on every page that you want to support handoff. We recommend adding it to the [Root Layout](/router/basics/layout#root-layout) component to ensure every route is linkable while debugging.

Ensure you can access the Ngrok URL (for example, via the browser), before installing the app on your device. If you can't access the URL, the OS will not be able to find the file and handoff will not work.

`npx expo run:ios` and Xcode will both codesign your app when associated domains is set up, this is required for handoff and universal links to work.

Handoff between your Mac and iPhone/iPad is not supported in the Expo Go app. You must build and install your app on your device.

If you see the Safari icon in the App Switcher on your iPhone, then it means handoff is not working.

* Ensure you are not using the `?mode=developer` suffix when testing handoff to native.
* Also be sure you're not using the local development server URL. For example, `http://localhost:8081` as this cannot be used as a valid app site association link, open the running Ngrok URL in your browser to test.
* Ensure your public/.well-known/apple-app-site-association file contains the `activitycontinuation` field.
* We've observed that in iOS 16.3.1 and macOS 13.0 (Ventura), bundle identifiers starting with `app.` and `io.` will sometimes not trigger the native app to show up in the iOS task switcher. Use `com.` as the first part of your bundle identifier.

Your public/.well-known/apple-app-site-association must be served from a secure URL (HTTPS). If you are using a development tunnel, you must use the `EXPO_TUNNEL_SUBDOMAIN` environment variable to configure the subdomain for your development tunnel. The tunnel is required for testing in development because you need SSL to use universal links, Expo CLI provides built-in support for this by running `npx expo start --tunnel`.

Check your ios/project/project.entitlements file, under the `com.apple.developer.associated-domains` key. This should contain the same domains as your web server/website. The URL cannot contain a protocol (`https://`) or additional pathname, query parameters, or fragments.

### Still stuck

> This is an important but very difficult feature to set up. Expo Router automates many of the moving parts, Expo CLI automates much of the configuration and hosting. However, hardware settings can still be misconfigured.

If all else fails, you can try to debug the issue by following the steps in the [Apple Docs](https://developer.apple.com/documentation/foundation/task_management/implementing_handoff_in_your_app). Note that:

* "Representing user activities as instances of `NSUserActivity`." is performed by the Expo Head native module.
* "Updating the activity instances as the user performs actions in your app." is performed by mounting/rendering the `<Head />` component with the meta tag `<meta property="expo:handoff" content="true" />` inside.
* "Receiving activities from Handoff in your app on other devices." is performed by an [App Delegate Subscriber](/modules/appdelegate-subscribers) in the Expo Head native module. It is used to redirect you to the correct route when you handoff to your native app.

Known issues
------------

Handoff from web to native does not support client-side routing. This means the URL presented in the App Switcher will be the URL of the page you were on when you clicked the link, or reloaded the page. It is a limitation of the web platform and not something that can be fixed by Expo Router.

[Previous (Expo Router - Advanced)

Settings](/router/advanced/router-settings)[Next (Expo Router - Advanced)

Custom tabs](/router/advanced/custom-tabs)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/advanced/apple-handoff.mdx)
* Last updated on April 03, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Setup](/router/advanced/apple-handoff/#setup)[Expo Head setup](/router/advanced/apple-handoff/#expo-head-setup)[Usage](/router/advanced/apple-handoff/#usage)[Meta tags](/router/advanced/apple-handoff/#meta-tags)[Debugging](/router/advanced/apple-handoff/#debugging)[Troubleshooting](/router/advanced/apple-handoff/#troubleshooting)[Still stuck](/router/advanced/apple-handoff/#still-stuck)[Known issues](/router/advanced/apple-handoff/#known-issues)