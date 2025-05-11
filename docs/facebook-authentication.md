Using Facebook authentication - Expo Documentation

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

Using Facebook authentication
=============================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/facebook-authentication.mdx)

A guide on using react-native-fbsdk-next library to integrate Facebook authentication in your Expo project.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/facebook-authentication.mdx)

---

The [`react-native-fbsdk-next`](https://github.com/thebergamo/react-native-fbsdk-next/) library provides a wrapper around Facebook's Android and iOS SDKs. It allows integrating Facebook authentication into your Expo project and provide access to native components.

This guide provides additional information on configuring the library with Expo for Android.

Prerequisites
-------------

The `react-native-fbsdk-next` library can't be used in the Expo Go app because it requires custom native code. Learn more about [adding custom native code to your app](/workflow/customizing).

Installation
------------

See `react-native-fbsdk-next` documentation for instructions on how to install and configure the library:

[React Native FBSDK Next: Expo installation instructions](https://github.com/thebergamo/react-native-fbsdk-next/#expo-installation)

Configuration for Android
-------------------------

Adding Android as a platform in your Facebook project requires you to have your app approved by Google Play Store so that it has a valid Play Store URL, and the [`package`](/versions/latest/config/app#package) name associated with your app. Otherwise, you'll run into the following error:

![Facebook project not recognizing unpublished Android app's package that doesn't have a valid Google Play Store URL.](/static/images/guides/android-package-error.png)

See the following guides for more information on how to build your project for app stores:

[Build your project for app stores](/deploy/build-project)
[Manually upload Android app for the first time](https://expo.fyi/first-android-submission)

Once you have uploaded the app to the Play Store you can submit your app review. When it is approved the Facebook project will be able to access it at a Play Store URL.

After that, go to your Facebook project's Settings > Basic and add the Android platform. You'll need to provide the Key hash, Package name and Class name.

![Required fields to add Android platform in the Facebook project.](/static/images/guides/android-required-fields.png)

* To add Key hash, go to your Play Store Console to obtain the SHA-1 certificate fingerprint from Release > Setup > App Integrity > App signing key certificate. Then, [convert the value of the Hex value of the certificate to Base64](https://base64.guru/converter/encode/hex) and add it under the Android > Key hashes in your Facebook project.
* You can find the Package name in your [app config](/versions/latest/config/app) under the [`android.package`](/versions/latest/config/app#package) field.
* The Class name is `MainActivity` by default, and you can use `package.MainActivity` where `package` is the `android.package` in your project's app config. For example, `com.myapp.example.MainActivity`, where `com.myapp.example` is the `package` name of your app.
* Then, click Save changes to save the configuration.

Now, you can use your Facebook project for development or release builds and production apps.

[Previous (More - Integrations)

Using Analytics](/guides/using-analytics)[Next (More - Integrations)

Using Supabase](/guides/using-supabase)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/facebook-authentication.mdx)
* Last updated on December 18, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Prerequisites](/guides/facebook-authentication/#prerequisites)[Installation](/guides/facebook-authentication/#installation)[Configuration for Android](/guides/facebook-authentication/#configuration-for-android)