iOS Universal Links - Expo Documentation

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

iOS Universal Links
===================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/linking/ios-universal-links.mdx)

Learn how to configure iOS Universal Links to open your Expo app from a standard web URL.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/linking/ios-universal-links.mdx)

---

To configure iOS Universal Links for your app, you need to set up the two-way association to verify your website and native app.

[![Watch: Set up iOS Universal Links with Expo Router](https://i3.ytimg.com/vi/kNbEEYlFIPs/maxresdefault.jpg)

Watch: Set up iOS Universal Links with Expo Router](https://www.youtube.com/watch?v=kNbEEYlFIPs&t=68)

Set up two-way association
--------------------------

To setup two-way association between the website and app for iOS, you need to perform the following steps:

* Website verification: This requires creating a apple-app-site-association (AASA) file inside the /.well-known directory and hosting it on the target website. This file is used to verify that the app opened from a given link is the correct app.
* Native app verification: This requires some form of code signing that references the target website domain (URL).

### Create AASA file

Create an apple-app-site-association file for the website verification inside the /.well-known directory. This file specifies your Apple Developer Team ID, bundle identifier, and a list of supported paths to redirect to the native app.

> You can run the experimental CLI command `npx setup-safari` inside your project to automatically register a bundle identifier to your Apple account, assign entitlements to the ID, and create an iTunes app entry in the store. The local setup will be printed and you can skip most the following. This is the easiest way to get started with universal links on iOS.

If you're using Expo Router to build your website (or any other modern React framework such as Remix, Next.js, and so on), create the AASA file at public/.well-known/apple-app-site-association. For legacy Expo webpack projects, create the file at web/.well-known/apple-app-site-association.

public/.well-known/apple-app-site-association

Copy

```
{
  // This section enables Universal Links
  "applinks": {
    "apps": [],
    "details": [
      {
        // Syntax: "<APPLE_TEAM_ID>.<BUNDLE_ID>"
        "appID": "QQ57RJ5UTD.com.example.myapp",
        // All paths that should support redirecting.
        "paths": ["/records/*"]
      }
    ]
  },
  // This section enables Apple Handoff
  "activitycontinuation": {
    "apps": ["<APPLE_TEAM_ID>.<BUNDLE_ID>"]
  },
  // This section enable Shared Web Credentials
  "webcredentials": {
    "apps": ["<APPLE_TEAM_ID>.<BUNDLE_ID>"]
  }
}

```

In the above example:

* Any links to `https://www.myapp.io/records/*` (with wildcard matching for the record ID) should be opened directly by the app with a matching bundle identifier on an iOS device. It is a combination of the [Apple Team ID](https://expo.fyi/apple-team) and the bundle identifier.
* The `*` wildcard does not match domain or path separators (periods and slashes).
* The `activitycontinuation` and `webcredentials` objects are optional, but recommended.

> See [Apple's documentation](https://developer.apple.com/library/archive/documentation/General/Conceptual/AppSearch/UniversalLinks.html) for further details on the format of the AASA. Branch provides an [AASA validator](https://branch.io/resources/aasa-validator/) which can help you confirm that your AASA is correctly deployed and has a valid format.

### Supporting `details` format

The [`details` format is supported](https://developer.apple.com/documentation/xcode/supporting-associated-domains) as of iOS 13. It allows you to specify:

* `appIDs` instead of `appID`: Makes it easier to associate multiple apps with the same configuration
* An array of `components`: Allows you to specify fragments, exclude specific paths, and add comments

An example AASA JSON from Apple's documentation

public/.well-known/apple-app-site-association

Copy

```
{
  "applinks": {
    "details": [
      {
        "appIDs": ["ABCDE12345.com.example.app", "ABCDE12345.com.example.app2"],
        "components": [
          {
            "#": "no_universal_links",
            "exclude": true,
            "comment": "Matches any URL whose fragment equals no_universal_links and instructs the system not to open it as a universal link"
          },
          {
            "/": "/buy/*",
            "comment": "Matches any URL whose path starts with /buy/"
          },
          {
            "/": "/help/website/*",
            "exclude": true,
            "comment": "Matches any URL whose path starts with /help/website/ and instructs the system not to open it as a universal link"
          },
          {
            "/": "/help/*",
            "?": {
              "articleNumber": "????"
            },
            "comment": "Matches any URL whose path starts with /help/ and which has a query item with name 'articleNumber' and a value of exactly 4 characters"
          }
        ]
      }
    ]
  }
}

```

To support all iOS versions, you can provide both the above formats in your `details` key, but we recommend placing the configuration for more recent iOS versions first.

### Host AASA file

Host the apple-app-site-association file using a web server with your domain. This file must be served over an HTTPS connection. Verify that your browser can access this file.

After you have setup the AASA file, deploy your website to a server that supports HTTPS (most modern web hosts).

### Native app configuration

After deploying your apple-app-site-association (AASA) file, configure your app to use your associated domain by adding [`ios.associatedDomains`](/versions/latest/config/app#associateddomains) to your [app config](/workflow/configuration). Make sure to follow [Apple's specified format](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_developer_associated-domains) and not include the protocol (`https`) in your URL. This is a common mistake that will result in the universal links not working.

For example, if an associated website is `https://expo.dev/`, the `applinks` is:

app.json

Copy

```
{
  "expo": {
    "ios": {
      "associatedDomains": ["applinks:expo.dev"]
    }
  }
}

```

Build your iOS app with [EAS Build](/build/setup) which ensures that the entitlement is registered with Apple automatically.

Manual native configuration

If you're not using EAS or [Continuous Native Generation](/workflow/continuous-native-generation) (`npx expo prebuild`), you have to [manually configure](/build-reference/ios-capabilities#manual-setup) the Associated Domains capability for your bundle identifier.

If you enable through the [Apple Developer Console](/build-reference/ios-capabilities#apple-developer-console), then make sure to add the following entitlements in your ios/[app]/[app].entitlements file:

```
<key>com.apple.developer.associated-domains</key>
<array>
  <string>applinks:expo.dev</string>
</array>

```

### Native app verification

Install the app on your iOS device to trigger the verification process. A link to your website on your mobile device should open your app. If it doesn't, re-check the previous steps to ensure that your AASA is valid, the path specified in the AASA, and you have correctly configured your App ID in the [Apple Developer Console](https://developer.apple.com/account/resources/identifiers/list).

Once you have your app opened, see [Handle links into your app](/linking/into-your-app#handle-urls) for more information on how to handle inbound links and show the user the content they requested.

> iOS downloads your AASA when your app is first installed or when updates are installed from the App Store. The operating system does not refresh frequently after that. If you want to change the paths in your AASA for a production app, you will need to issue a full update via the App Store so that all of your users' apps re-fetch your AASA and recognize the new paths.

Apple Smart Banner
------------------

If a user doesn't have your app installed, they'll be directed to the website. You can use the [Apple Smart Banner](https://developer.apple.com/documentation/webkit/promoting_apps_with_smart_app_banners) to show a banner at the top of the page that prompts the user to install the app. The banner will only show up if the user is on a mobile device and doesn't have the app installed.

To enable the banner, add the following meta tag to the `<head>` of your website, replacing `<ITUNES_ID>` with your app's iTunes ID:

```
<meta name="apple-itunes-app" content="app-id=<ITUNES_ID>" />

```

If you're having trouble setting up the banner, run the following command to automatically generate the meta tag for your project:

Terminal

Copy

`-Â``npx setup-safari`

### Add the meta tag to your statically rendered website

If you're building a [statically rendered website with Expo Router](/router/reference/static-rendering), then add the HTML tag to the `<head>` component in your [app/+html.js file](/router/reference/static-rendering#root-html).

app/+html.tsx

Copy

```
import { type PropsWithChildren } from 'react';

export default function Root({ children }: PropsWithChildren) {
  return (
    <html lang="en">
      <head>
        <meta charSet="utf-8" />
        <meta httpEquiv="X-UA-Compatible" content="IE=edge" />
        <meta name="apple-itunes-app" content="app-id=<ITUNES_ID>" />
        {/* Other head elements... */}
      </head>
      <body>{children}</body>
    </html>
  );
}

```

Debugging
---------

Expo CLI enables you to test iOS Universal Links without deploying a website. Utilizing the [`--tunnel`](/more/expo-cli#tunneling) functionality, you can forward your dev server to a publicly available HTTPS URL.

1

Set the environment variable `EXPO_TUNNEL_SUBDOMAIN=my-custom-domain` where `my-custom-domain` is a unique string that you use during development. This ensures that your tunnel URL is consistent across dev server restarts.

2

Add `associatedDomains` to your app config as [described above](/linking/ios-universal-links#native-app-configuration). Replace the domain value with a Ngrok URL: `my-custom-domain.ngrok.io`.

3

Start your dev server with the `--tunnel` flag:

Terminal

Copy

`-Â``npx expo start --tunnel`

4

Compile the development build on your device:

Terminal

Copy

`-Â``npx expo run:ios`

You can now type your custom domain link in your device's web browser to open your app.

Troubleshooting
---------------

Here are some common tips to help you troubleshoot when implementing iOS Universal Links:

* Read Apple's official documentation on [debugging universal links](https://developer.apple.com/documentation/technotes/tn3155-debugging-universal-links)
* Ensure your apple app site association file is valid by using a [validator tool](https://branch.io/resources/aasa-validator/).
* The uncompressed `apple-app-site-association` file cannot be [larger than 128kb](https://developer.apple.com/library/archive/documentation/General/Conceptual/AppSearch/UniversalLinks.html).
* Ensure your website is served over HTTPS.
* If you update your web files, rebuild the native app to trigger a server update on the vendor side (Apple).

[Previous (Development process - Linking)

Android App Links](/linking/android-app-links)[Next (Development process - Write native code)

Add custom native code](/workflow/customizing)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/linking/ios-universal-links.mdx)
* Last updated on February 05, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Set up two-way association](/linking/ios-universal-links/#set-up-two-way-association)[Create AASA file](/linking/ios-universal-links/#create-aasa-file)[Supporting details format](/linking/ios-universal-links/#supporting-details-format)[Host AASA file](/linking/ios-universal-links/#host-aasa-file)[Native app configuration](/linking/ios-universal-links/#native-app-configuration)[Native app verification](/linking/ios-universal-links/#native-app-verification)[Apple Smart Banner](/linking/ios-universal-links/#apple-smart-banner)[Add the meta tag to your statically rendered website](/linking/ios-universal-links/#add-the-meta-tag-to-your-statically-rendered-website)[Debugging](/linking/ios-universal-links/#debugging)[Troubleshooting](/linking/ios-universal-links/#troubleshooting)