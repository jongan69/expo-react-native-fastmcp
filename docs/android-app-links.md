Android App Links - Expo Documentation

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

Android App Links
=================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/linking/android-app-links.mdx)

Learn how to configure Android App Links to open your Expo app from a standard web URL.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/linking/android-app-links.mdx)

---

To configure Android App Links for your app, you need to:

* Add `intentFilters` and set `autoVerify` to true in your project's app config
* Set up two-way association to verify your website and native app

[![Watch: Set up Android App Links with Expo Router](https://i3.ytimg.com/vi/kNbEEYlFIPs/maxresdefault.jpg)

Watch: Set up Android App Links with Expo Router](https://www.youtube.com/watch?v=kNbEEYlFIPs&t=399)

Add `intentFilters` to the app config
-------------------------------------

Configure your app config by adding the `android.intentFilters` property and setting the `autoVerify` attribute to `true`. Specifying `autoVerify` is required for Android App Links to work correctly.

The following example shows a basic configuration that enables your app to appear in the standard Android dialog as an option for handling any links to the `webapp.io` domain. It also uses the regular `https` scheme since [Android App Links](/linking/overview#android-app-links) are different from [standard deep links](/linking/into-other-apps).

app.json

Copy

```
{
  "expo": {
    "android": {
      "intentFilters": [
        {
          "action": "VIEW",
          "autoVerify": true,
          "data": [
            {
              "scheme": "https",
              "host": "*.webapp.io",
              "pathPrefix": "/records"
            }
          ],
          "category": ["BROWSABLE", "DEFAULT"]
        }
      ]
    }
  }
}

```

Set up two-way association
--------------------------

To setup two-way association between the website and Android app, you will need the following:

* Website verification: This requires creating a assetlinks.json file inside the /.well-known directory and hosting it on the target website. This file is used to verify that the app opened from a given link is the correct app.
* Native app verification: This requires some form of code signing that references the target website domain (URL).

### Create assetlinks.json file

1

Create an assetlinks.json file for the website verification (also known as [digital asset links](https://developers.google.com/digital-asset-links/v1/getting-started) file) at /.well-known/assetlinks.json. This file is used to verify that the app opened for a given link.

If you're using Expo Router to build your website (or any other modern React framework such as Remix, Next.js, and so on), create assetlinks.json at public/.well-known/assetlinks.json. For legacy Expo webpack projects, create the file at web/.well-known/assetlinks.json.

2

Get the value of `package_name` from your app config, under `android.package`.

3

Get the value of `sha256_cert_fingerprints` from your app's signing certificate. If you're using [EAS Build](/build/setup) to build your Android app, after creating a build:

* Run `eas credentials -p android` command, and select the build profile to get its fingerprint value.
* Copy the fingerprint value listed under `SHA256 Fingerprint`.

Alternate method to obtain the SHA256 certificate fingerprint from Google Play Console

If you're not using EAS to manage code signing, you can find the sha256\_cert\_fingerprints by building and submitting your app manually to the [Google Play Console](https://play.google.com/console/):

* Inside the Google Play Console's dashboard, go to Release > Setup > App Signing.
* Find the correct Digital Asset Links JSON snippet for your app.
* Copy the value looks like `14:6D:E9:83...` and paste it into your public/.well-known/assetlinks.json file under `sha256_cert_fingerprints`.

4

Add `package_name` and `sha256_cert_fingerprints` to the assetlinks.json file:

public/.well-known/assetlinks.json

Copy

```
[
  {
    "relation": ["delegate_permission/common.handle_all_urls"],
    "target": {
      "namespace": "android_app",
      "package_name": "com.example",
      "sha256_cert_fingerprints": [
        // Supports multiple fingerprints for different apps and keys
        "14:6D:E9:83:51:7F:66:01:84:93:4F:2F:5E:E0:8F:3A:D6:F4:CA:41:1A:CF:45:BF:8D:10:76:76:CD"
      ]
    }
  }
]

```

> You can add multiple fingerprints to the `sha256_cert_fingerprints` array to support different variants of your app. For more information, see [Android's documentation on how to declare website associations](https://developer.android.com/training/app-links/verify-android-applinks#web-assoc).

### Host assetlinks.json file

Host the assetlinks.json file using a web server with your domain. This file must be served with the content-type `application/json` and accessible over an HTTPS connection. Verify that your browser can access this file by typing the complete URL in the address bar.

### Native app verification

Install the app on an Android device to trigger the [Android app verification](https://developer.android.com/training/app-links/verify-android-applinks#web-assoc) process.

Once you have your app opened, see [Handle links into your app](/linking/into-your-app#handle-urls) for more information on how to handle inbound links and show the user the content they requested.

Debugging
---------

The Expo CLI enables you to test Android App Links without deploying a website. Utilizing the [`--tunnel`](/more/expo-cli#tunneling) functionality, you can forward your dev server to a publicly available HTTPS URL.

1

Set the environment variable `EXPO_TUNNEL_SUBDOMAIN=my-custom-domain` where `my-custom-domain` is a unique string that you use during development. This ensures that your tunnel URL is consistent across dev server restarts.

2

Add `intentFilters` to your app config as [described above](/linking/android-app-links#add-intentfilters-to-the-app-config). Replace the `host` value with a Ngrok URL: `my-custom-domain.ngrok.io`.

3

Start your dev server with the `--tunnel` flag:

Terminal

Copy

`-Â``npx expo start --tunnel`

4

Compile the development build on your device:

Terminal

Copy

`-Â``npx expo run:android`

5

Use the following `adb` command to start the intent activity and open the link on your app or type the custom domain link in your device's web browser.

Terminal

Copy

`-Â``adb shell am start -a android.intent.action.VIEW -c android.intent.category.BROWSABLE -d "https://my-custom-domain.ngrok.io/" <your-package-name>`

Troubleshooting
---------------

Here are some common tips to help you troubleshoot when implementing Android App Links:

* Ensure your website is served over HTTPS and with the content-type `application/json`
* [Verify Android app links](https://developer.android.com/training/app-links/verify-android-applinks)
* Android verification may take 20 seconds or longer to take effect, so be sure to wait until it is completed.
* If you update your web files, rebuild the native app to trigger a server update on the vendor side (Google)

[Previous (Development process - Linking)

Into your app](/linking/into-your-app)[Next (Development process - Linking)

iOS Universal Links](/linking/ios-universal-links)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/linking/android-app-links.mdx)
* Last updated on February 05, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Add intentFilters to the app config](/linking/android-app-links/#add-intentfilters-to-the-app-config)[Set up two-way association](/linking/android-app-links/#set-up-two-way-association)[Create assetlinks.json file](/linking/android-app-links/#create-assetlinksjson-file)[Host assetlinks.json file](/linking/android-app-links/#host-assetlinksjson-file)[Native app verification](/linking/android-app-links/#native-app-verification)[Debugging](/linking/android-app-links/#debugging)[Troubleshooting](/linking/android-app-links/#troubleshooting)