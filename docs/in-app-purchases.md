Using In-app purchase - Expo Documentation

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

[Using Analytics](/guides/using-analytics)[Using Facebook authentication](/guides/facebook-authentication)[Using Supabase](/guides/using-supabase)[Using Firebase](/guides/using-firebase)[Using Google authentication](/guides/google-authentication)[Using ESLint and Prettier](/guides/using-eslint)[Using Next.js](/guides/using-nextjs)[Using LogRocket](/guides/using-logrocket)[Using Sentry](/guides/using-sentry)[Using BugSnag](/guides/using-bugsnag)[Using Vexo](/guides/using-vexo)[Build apps for TV](/guides/building-for-tv)[Using TypeScript](/guides/typescript)[Using In-app purchase](/guides/in-app-purchases)[Using push notifications](/guides/using-push-notifications-services)

Troubleshooting

Regulatory compliance

[Data and Privacy protection](/regulatory-compliance/data-and-privacy-protection)[GDPR compliance](/regulatory-compliance/gdpr)[HIPAA compliance](/regulatory-compliance/hipaa)[Privacy Shield](/regulatory-compliance/privacy-shield)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Using In-app purchase
=====================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/in-app-purchases.mdx)

Learn about how to use in-app purchases in your Expo app.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/in-app-purchases.mdx)

---

In-app purchases (IAP) are transactions within a mobile or desktop application where users can buy digital goods or additional features. This guide provides a list of popular libraries and tutorials for implementing IAP in your Expo app.

> In-app purchase libraries require configuring custom native code. Native code is not configurable when using Expo Go. Instead, create a [development build](/develop/development-builds/introduction), which allows using a native library in your project.

Tutorial
--------

[Expo In-App Purchase Tutorial

The getting started guide for in-app purchases and subscriptions with `react-native-purchases` library and RevenueCat.](https://www.revenuecat.com/blog/engineering/expo-in-app-purchase-tutorial/)

Libraries
---------

The following libraries provide robust support for in-app purchase functionality and out-of-the-box compatibility with Expo apps using [CNG](/workflow/continuous-native-generation) and [Config Plugins](/config-plugins/introduction) for seamless integration in your app.

[`react-native-purchases`

An open-source framework that provides a wrapper around Google Play Billing and StoreKit APIs, and integration with RevenueCat services supporting in-app purchases. It enables product management, analytics, and simplified workflows for in-app purchase requirements that may extend beyond your client code, such as validating purchases on an app's backend.](https://github.com/RevenueCat/react-native-purchases)
[`react-native-iap`

A React Native library providing an interface to the client-side native in-app purchase API's for Android (both Play Store and Amazon) and iOS.](https://github.com/dooboolab-community/react-native-iap)

[Previous (More - Integrations)

Using TypeScript](/guides/typescript)[Next (More - Integrations)

Using push notifications](/guides/using-push-notifications-services)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/in-app-purchases.mdx)
* Last updated on May 01, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).