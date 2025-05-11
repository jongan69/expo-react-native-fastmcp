Using Google authentication - Expo Documentation

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

Using Google authentication
===========================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/google-authentication.mdx)

A guide on using @react-native-google-signin/google-signin library to integrate Google authentication in your Expo project.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/google-authentication.mdx)

---

The [`@react-native-google-signin/google-signin`](https://github.com/react-native-google-signin/google-signin) library provides a way integrate Google authentication in your Expo app. It also provides native sign-in buttons and supports authenticating the user as well as obtaining their authorization to use Google APIs. You can use the library in your project by adding the [config plugin](/config-plugins/introduction) in the [app config](/versions/latest/config/app).

This guide provides information on how to configure the library for your project.

Prerequisites
-------------

The `@react-native-google-signin/google-signin` library can't be used in the Expo Go app because it requires custom native code. Learn more about [adding custom native code to your app](/workflow/customizing).

Installation
------------

See `@react-native-google-signin/google-signin` documentation for instructions on how to install and configure the library:

[React Native Google Sign In: Expo installation instructions](https://react-native-google-signin.github.io/docs/setting-up/expo)

Configure Google project for Android and iOS
--------------------------------------------

Below are instructions on how to configure your Google project for Android and iOS.

### Upload app to Google Play Store

We recommend uploading the app to the Google Play Store if your app intends to run in production. You can submit your app to the stores for testing even if your project is still in development. This allows you to test Google Sign In when your app is signed by EAS for testing, and when it is signed by [Google Play App Signing](https://support.google.com/googleplay/android-developer/answer/9842756?hl=en) for store deployment. To learn more about the app submission process, see the guides below in the order they are specified:

[Create your first EAS Build](/build/setup)
[Build your project for app stores](/deploy/build-project)
[Manually upload Android app for the first time](https://expo.fyi/first-android-submission)

### Configure your Firebase or Google Cloud Console project

> Refer to the [library's documentation](https://react-native-google-signin.github.io/docs/setting-up/get-config-file) for a more in-depth configuration guide.

For Android, once you have uploaded your app, you need to provide the SHA-1 certificate fingerprint values when asked while configuring the project in Firebase or Google Cloud Console. There are two types of values that you can provide:

* Fingerprint of the .apk you built (on your machine or using EAS Build). You can find the SHA-1 certificate fingerprint in the Google Play Console under Release > Setup > App Integrity > Upload key certificate.
* Fingerprint(s) of a production app downloaded from the play store. You can find the SHA-1 certificate fingerprint(s) in the Google Play Console under Release > Setup > App Integrity > App signing key certificate.

### With Firebase

For more instructions on how to configure your project for Android and iOS with Firebase:

[Firebase](https://react-native-google-signin.github.io/docs/setting-up/expo#expo-and-firebase-authentication)

#### Upload google-services.json and GoogleService-Info.plist to EAS

If you use the Firebase method for Android and iOS (as shared in sections above), you'll need to make sure google-services.json and GoogleService-Info.plist are available in EAS for building the app. You can check them into your repository because the files should not contain sensitive values, or you can treat the files as secrets, add them to .gitignore and use the guide below to make them available in EAS.

[Upload a secret file to EAS and use in the app config](/eas/environment-variables?redirected#use-environment-variables-with-eas-build)

### With Google Cloud Console

This is an alternate method to configure a Google project when you are not using [Firebase](/guides/google-authentication#with-firebase).

For more instructions on how to configure your Google project Android and iOS with Google Cloud Console:

[Expo without Firebase](https://react-native-google-signin.github.io/docs/setting-up/expo#expo-without-firebase)

[Previous (More - Integrations)

Using Firebase](/guides/using-firebase)[Next (More - Integrations)

Using ESLint and Prettier](/guides/using-eslint)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/google-authentication.mdx)
* Last updated on April 28, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Prerequisites](/guides/google-authentication/#prerequisites)[Installation](/guides/google-authentication/#installation)[Configure Google project for Android and iOS](/guides/google-authentication/#configure-google-project-for-android-and-ios)[Upload app to Google Play Store](/guides/google-authentication/#upload-app-to-google-play-store)[Configure your Firebase or Google Cloud Console project](/guides/google-authentication/#configure-your-firebase-or-google-cloud-console-project)[With Firebase](/guides/google-authentication/#with-firebase)[With Google Cloud Console](/guides/google-authentication/#with-google-cloud-console)