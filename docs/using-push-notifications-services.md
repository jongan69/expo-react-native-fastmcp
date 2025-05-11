Using push notifications - Expo Documentation

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

Using push notifications
========================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/using-push-notifications-services.mdx)

Learn about push notification services that are compatible with Expo and React Native apps.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/using-push-notifications-services.mdx)

---

Expo apps can work with any notification service or any of the notification capabilities offered by the Android and iOS operating systems. Even if a package doesn't yet exist for a feature, native code can be written to access it via the [Expo Modules API](/modules/overview), and native project configurations can be automated using [config plugins](/config-plugins/introduction). The following options provide purpose-built Expo integrations, including config plugins where necessary, for implementing push notifications in your app:

> The [`expo-notifications`](/versions/latest/sdk/notifications) library is designed and tested to work with Expo's push notification service and notifications sent directly from FCM and APNS. Some advanced features may not be compatible with third-party providers, as they often have their own native and React Native SDKs optimized for their services.

Expo push notifications
-----------------------

[Expo Notifications](/versions/latest/sdk/notifications) provides a unified API for handling push notifications across Android and iOS. It integrates seamlessly with your Expo account and is free to use.

### Key capabilities

* Fully compatible with the [`expo-notifications`](/versions/latest/sdk/notifications) library
* Includes an Expo Dashboard to track notification delivery to FCM and APNs
* Supports testing notifications with the [Expo Notifications Tool](https://expo.dev/notifications)

### Considerations and limitations

* iOS Notification Service Extension for adding additional content to notifications, such as images, is not formally included, but you can add it using a config plugin with custom native code and configuration ([example](https://github.com/expo/expo/pull/36202)).
* Volumes are limited to 600 notifications per second per project.

For implementation details, see the following guides:

[Expo push notifications overview

Learn more about Expo push notifications.](/push-notifications/overview)
[Expo Notifications server-side SDK options

Learn more about sending push notifications using a server.](/push-notifications/sending-notifications#send-push-notifications-using-a-servers)

OneSignal
---------

[OneSignal](https://onesignal.com/) is a customer engagement platform that provides push notifications, in-app messaging, SMS, and email services for web and mobile apps. OneSignal supports rich media in notifications and engagement analytics. It includes an [Expo config plugin](https://github.com/OneSignal/onesignal-expo-plugin) for direct integration into your Expo project.

[OneSignal Expo SDK Setup

Follow this guide for a step-by-step setup on how to integrate OneSignal in your Expo project.](https://documentation.onesignal.com/docs/react-native-expo-sdk-setup)

Braze
-----

[Braze](https://www.braze.com/) is a customer engagement platform that delivers personalized, cross-channel messaging through push notifications, in-app messaging, email, SMS, and web. Braze supports rich notification content, push notification campaigns, and support for resending notifications after failed deliveries on Android. It provides a [React Native SDK](https://github.com/braze-inc/braze-react-native-sdk) and a [config plugin](https://github.com/braze-inc/braze-expo-plugin/tree/main). Check out the [Expo example app](https://github.com/braze-inc/braze-expo-plugin/tree/main/example) for more details.

[Braze Expo Setup

Follow this guide for a step-by-step setup on how to integrate Braze in your Expo project.](https://www.braze.com/docs/developer_guide/platforms/react_native/sdk_integration)

Customer.io
-----------

[Customer.io](http://Customer.io) is a customer engagement platform that allows you to design powerful automated workflows utilizing push notifications, in-app messaging, email, SMS capabilities, and more. Its visual workflow builder allows you to automate complex, data-driven campaigns across multiple channels. Customer.io supports device-side metrics collection that can be used to customize push notifications tailored to user behaviors and preferences. Customer.io provides an [Expo plugin](https://github.com/customerio/customerio-expo-plugin) for direct integration with your Expo project and documentation for using Customer.io push notifications alongside other providers.

[Customer.io Expo Quick Start Guide

Follow this guide for a step-by-step setup on how to integrate Customer.io in your Expo project.](https://docs.customer.io/sdk/expo/quick-start-guide/)

CleverTap
---------

[CleverTap](https://clevertap.com/) is an all-in-one customer engagement platform that helps you deliver personalized, real-time, omnichannel messaging across push notifications, in-app messages, email, and more. It offers advanced segmentation, analytics, and campaign automation â built to scale with your business. The [CleverTap React Native SDK](https://developer.clevertap.com/docs/react-native) and [Expo config plugin](https://github.com/CleverTap/clevertap-expo-plugin) make it easy to integrate CleverTap into your Expo projects. The config plugin handles all the native module setup during the prebuild process, allowing you to configure CleverTap through your app config without having to manually modify native code. For more information, check out the [CleverTap Example Plugin](https://github.com/CleverTap/clevertap-expo-plugin/tree/main/CTExample).

[CleverTap Expo Plugin Docs

Follow this guide to set up CleverTap in your Expo or React Native project.](https://developer.clevertap.com/docs/clevertap-expo-plugin)

Send notifications directly via FCM and APNs
--------------------------------------------

You may choose to send directly to platform push API's from your backend. In this case, you can still use [`expo-notifications`](/versions/latest/sdk/notifications) to retrieve the native push token and configure notifications separately for each platform.

Although the client-side code remains cross-platform with [`expo-notifications`](/versions/latest/sdk/notifications), you will need to implement server-side logic to interact with the [FCM](https://firebase.google.com/docs/cloud-messaging) and [APNs](https://developer.apple.com/documentation/usernotifications) APIs individually.

React Native Firebase messaging
-------------------------------

[React Native Firebase](https://rnfirebase.io/) provides a messaging module that lets you use [Firebase Cloud Messaging (FCM)](https://firebase.google.com/docs/cloud-messaging) as a unified push notification service for both Android and iOS. While FCM is often associated with Android notifications, it also supports iOS by routing messages through Apple Push Notification service (APNs) behind the scenes.

This approach differs from using FCM solely for Android notifications. Instead, Firebase's cross-platform SDK handles notifications for both platforms through a single service.

> Even though FCM handles notifications for both platforms, iOS notifications still go through APNs. Firebase automatically manages this routing. Learn more in the [React Native Firebase messaging documentation](https://rnfirebase.io/messaging/usage).

Tips and important considerations
---------------------------------

* Avoid mixing client-side implementations: Different notification services may have conflicting client-side implementations. Use a consistent approach to prevent potential issues.
* Web notifications: Expo notifications do not support web notifications. However, some third-party solutions may offer this capability. Consider your app's requirements when choosing a service.
* Token management: Track both Expo push tokens and native device tokens in your database. This provides flexibility for future integrations, especially with marketing tools that send notifications directly via FCM or APNs.

[Previous (More - Integrations)

Using In-app purchase](/guides/in-app-purchases)[Next (More - Troubleshooting)

Overview](/troubleshooting/overview)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/using-push-notifications-services.mdx)
* Last updated on May 09, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Expo push notifications](/guides/using-push-notifications-services/#expo-push-notifications)[Key capabilities](/guides/using-push-notifications-services/#key-capabilities)[Considerations and limitations](/guides/using-push-notifications-services/#considerations-and-limitations)[OneSignal](/guides/using-push-notifications-services/#onesignal)[Braze](/guides/using-push-notifications-services/#braze)[Customer.io](/guides/using-push-notifications-services/#customerio)[CleverTap](/guides/using-push-notifications-services/#clevertap)[Send notifications directly via FCM and APNs](/guides/using-push-notifications-services/#send-notifications-directly-via-fcm-and-apns)[React Native Firebase messaging](/guides/using-push-notifications-services/#react-native-firebase-messaging)[Tips and important considerations](/guides/using-push-notifications-services/#tips-and-important-considerations)