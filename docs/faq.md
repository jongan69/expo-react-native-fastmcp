Push notifications troubleshooting and FAQ - Expo Documentation

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

[Add Android FCM V1 credentials](/push-notifications/fcm-credentials)[Send notifications with FCM and APNs](/push-notifications/sending-notifications-custom)[Troubleshooting and FAQ](/push-notifications/faq)

More

[Upgrade Expo SDK](/workflow/upgrading-expo-sdk-walkthrough)

Assorted

Integrations

Troubleshooting

Regulatory compliance

[Data and Privacy protection](/regulatory-compliance/data-and-privacy-protection)[GDPR compliance](/regulatory-compliance/gdpr)[HIPAA compliance](/regulatory-compliance/hipaa)[Privacy Shield](/regulatory-compliance/privacy-shield)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Push notifications troubleshooting and FAQ
==========================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/push-notifications/faq.mdx)

A collection of common questions about Expo push notification service.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/push-notifications/faq.mdx)

---

A collection of common issues and FAQs when setting up push notifications with the `expo-notifications` library and Expo push notification service.

Expo push notification service FAQ
----------------------------------

### Cost of the push notification service

There is no cost associated with sending notifications through Expo push notification service.

### Limit of sending notifications

There is a limit of 600 notifications per second per project that can be sent. If you exceed this rate, subsequent requests will fail until the rate falls below 600 per second again.

For best results, we recommend you add throttling (which is handled automatically in the [`expo-server-sdk-node`](https://github.com/expo/expo-server-sdk-node)) and retry logic to your server.

### Using Expo push notification service is not mandatory

You can use any push notification service for Expo projects. The [`getDevicePushTokenAsync` method from `expo-notifications`](/versions/latest/sdk/notifications#getdevicepushtokenasync-devicepushtoken) allows you to get the native device push token, which you can then use with other services, or even [send your notifications directly through FCM and APNs](/push-notifications/sending-notifications-custom).

### Connections to notification service are encrypted

Expo's connections to Apple and Google are encrypted and use HTTPS.

### Contents of the notification are not stored

Expo doesn't store the contents of push notifications any longer than it takes to deliver them to the push notification services operated by Google and Apple. Notifications are stored only in memory and in message queues, not in databases.

### Contents of the notifications may be seen by Expo staff

If the Expo team is actively debugging the push notifications service, we may see notification contents (for example, at a breakpoint) but Expo cannot see push notification contents otherwise.

### Delivery guarantees

Expo makes the best effort to deliver notifications to the push notification services operated by Google and Apple. Expo's infrastructure is designed for at-least-once delivery to the underlying push notification services. In some cases, a notification may be delivered to Google or Apple more than once or not at all, although these cases are rare.

After a notification has been handed off to an underlying push notification service, Expo creates a "push receipt" that records whether the handoff was successful. A push receipt denotes whether the underlying push notification service received the notification.

Finally, the push notification services from Google and Apple follow their policies to deliver the notification to the device.

### When and why does the `ExpoPushToken` change

The `ExpoPushToken` remains the same across app upgrades. On Android, reinstalling the app may result in the token changing. On iOS, the token also remains the same even after uninstalling the app and reinstalling it.

It also changes if you change your [`applicationId`](/versions/latest/sdk/application#applicationapplicationid) or `experienceId` (usually `@expoUsername/projectSlug`).

The `ExpoPushToken` never expires. However, if one of your users uninstalls the app, you'll receive a `DeviceNotRegistered` error back from Expo's servers. This means you should stop sending notifications to this token.

Push notifications troubleshooting
----------------------------------

### Notifications aren't working

Push notifications have a lot of moving parts, so this can be due to a wide variety of reasons. To narrow things down, check the [push ticket](/push-notifications/sending-notifications#push-tickets) and [push receipt](/push-notifications/sending-notifications#push-receipts) for error messages.

You can also narrow things even further by testing [local notifications](/versions/latest/sdk/notifications#schedulenotificationasyncnotificationrequest-notificationrequestinput-promisestring) in your app. This ensures all of your client-side logic is correct, and narrow things down to the server side or app credentials.

See here for some quick terminal commands you can use to get the push receipt

1. Send a notification:

```
curl -H "Content-Type: application/json" -X POST "https://exp.host/--/api/v2/push/send" -d '{
  "to": "ExponentPushToken[xxxxxxxxxxxxxxxxxxxxxx]",
  "title":"hello",
  "body": "world"
}'

```

2. Use the resulting ticket `id` to request the push receipt:

```
curl -H "Content-Type: application/json" -X POST "https://exp.host/--/api/v2/push/getReceipts" -d '{
  "ids": [
    "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
  ]
}'

```

### Notifications work in development, but not in release mode

This indicates that you have either misconfigured your credentials or didn't configure them at all in your production app. Expo Go uses Expo's credentials, which allows working on notifications in development.

When you build your app for the app stores, you need to generate and use your own credentials. On Android, follow [this guide](/push-notifications/fcm-credentials). On iOS, this is handled by your [push key](/app-signing/app-credentials#push-notification-keys) (revoking the push key associated with your app results in your notifications failing to be delivered. To fix that, add a new push key with `eas credentials`).

For more information, see [app signing](/app-signing/app-credentials).

### Notifications occasionally stop coming through on Android

This is likely due to the `priority` level of the notifications you're sending. You can learn more about [Android priority](https://firebase.google.com/docs/cloud-messaging/http-server-ref#downstream-http-messages-json). [Expo accepts four priorities](/push-notifications/sending-notifications#message-request-format):

* `default`: manually mapped to the default priority documented by Apple and Google
* `high`: mapped to the high priority level documented by Apple and Google
* `normal`: mapped to the normal priority level documented by Apple and Google
* (priority omitted): treated exactly as if `default` were specified

Setting the priority to `high` gives your notification the greatest likelihood that Android will display the notification.

### Handle expired push notification credentials

When your push notification credentials have expired, run `eas credentials`, choose iOS and a build profile, then remove your push notification key and generate a new one.

### No valid aps-environment entitlement string found error for iOS

This error occurs if you haven't set up a push notification key for your iOS project. To check, go to the [Project Credentials page](https://expo.dev/accounts/%5Baccount%5D/projects/%5Bproject%5D/credentials/ios).

To generate a new push notification key, trigger a new build by running:

Terminal

Copy

`eas build --profile [profile] --platform ios`

For a visual guide, see the [Expo Notifications with EAS video](https://youtu.be/BCCjGtKtBjE?t=2123).

### Error message when sending a notification

Check the `details` property of the returned push ticket or receipt for more information. [Read this](/push-notifications/sending-notifications#errors) for common error code responses and their associated solutions.

### Fetching a push token takes a long time on iOS

`getDevicePushTokenAsync` and `getExpoPushTokenAsync` can sometimes take a long time to resolve on iOS. This is outside of `expo-notifications`'s control, as stated in Apple's [Troubleshooting Push Notifications](https://developer.apple.com/library/archive/technotes/tn2265/_index.html) technical note:

> This is not necessarily an error condition. The system may not have Internet connectivity at all because it is out of range of any cell towers or Wi-Fi access points, or it may be in airplane mode. Instead of treating this as an error, your app should continue normally, disabling only that functionality that relies on push notifications.

Here are some ways our community members have resolved this issue:

Read the Apple's Technical Note on troubleshooting push notifications

Read Apple's [Technical Note on troubleshooting push notifications](https://developer.apple.com/library/archive/technotes/tn2265/_index.html)! This is the single most reliable source of information on this problem. To help you grasp what they're suggesting:

* Make sure the device has a reliable connection to the Internet (try turning off Wi-Fi or switching to another network, and disabling the firewall block on port 5223, as suggested in [this SO answer](https://stackoverflow.com/a/34332047/1123156)).
* Bare React Native apps must [manually enable the Push Notifications capability](/build-reference/ios-capabilities#manual-setup). If you have trouble setting this up, refer to [this Stack Overflow answer](https://stackoverflow.com/a/10791240/1123156). You may also want to try to debug this even further by logging persistent connection debug information as outlined by [this Stack Overflow answer](https://stackoverflow.com/a/8036052/1123156).

Try again in a little while

* APNS servers near the device may be down as indicated by [this forum thread](https://developer.apple.com/forums/thread/52224). Take a walk and try again later!
* Try again in a few days as suggested by [this GitHub comment](https://github.com/expo/expo/issues/10369#issuecomment-717872956).

Disable network sharing on your device

You may need to disable network sharing as this may impact the registration as suggested by [this Stack Overflow answer](https://stackoverflow.com/a/59156989/1123156).

Restart your device

If you just changed the APNS servers where the app should be registering (by installing a TestFlight build over an Xcode build on the same device) you may need to restart your device as suggested by [this Stack Overflow answer](https://stackoverflow.com/a/59864028/1123156).

Setup your device with a SIM card

If the device you're experiencing this on hasn't been setup with a SIM card it looks like configuring it may help mitigate this bug as suggested by [this Stack Overflow answer](https://stackoverflow.com/a/19432504/1123156).

Miscellaneous
-------------

### Sending notifications directly through FCM and APNs

If you are not using [Expo push notification service](/push-notifications/sending-notifications) and instead, would like to communicate with Google and Apple directly, see [Send notifications with FCM and APNs](/push-notifications/sending-notifications-custom).

### Notification icon on Android is a grey or white square

This indicates an issue with the image asset you're providing. The image should be all white with a transparent background (this is required and enforced by Google, not Expo). For more information, see [this article](https://clevertap.com/blog/fixing-notification-icon-for-android-lollipop-and-above/).

[Previous (Push notifications - Reference)

Send notifications with FCM and APNs](/push-notifications/sending-notifications-custom)[Next (More)

Upgrade Expo SDK](/workflow/upgrading-expo-sdk-walkthrough)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/push-notifications/faq.mdx)
* Last updated on May 05, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Expo push notification service FAQ](/push-notifications/faq/#expo-push-notification-service-faq)[Cost of the push notification service](/push-notifications/faq/#cost-of-the-push-notification-service)[Limit of sending notifications](/push-notifications/faq/#limit-of-sending-notifications)[Using Expo push notification service is not mandatory](/push-notifications/faq/#using-expo-push-notification-service-is-not-mandatory)[Connections to notification service are encrypted](/push-notifications/faq/#connections-to-notification-service-are-encrypted)[Contents of the notification are not stored](/push-notifications/faq/#contents-of-the-notification-are-not-stored)[Contents of the notifications may be seen by Expo staff](/push-notifications/faq/#contents-of-the-notifications-may-be-seen-by-expo-staff)[Delivery guarantees](/push-notifications/faq/#delivery-guarantees)[When and why does the ExpoPushToken change](/push-notifications/faq/#when-and-why-does-the-expopushtoken-change)[Push notifications troubleshooting](/push-notifications/faq/#push-notifications-troubleshooting)[Notifications aren't working](/push-notifications/faq/#notifications-arent-working)[Notifications work in development, but not in release mode](/push-notifications/faq/#notifications-work-in-development-but-not-in-release-mode)[Notifications occasionally stop coming through on Android](/push-notifications/faq/#notifications-occasionally-stop-coming-through-on-android)[Handle expired push notification credentials](/push-notifications/faq/#handle-expired-push-notification-credentials)[No valid aps-environment entitlement string found error for iOS](/push-notifications/faq/#no-valid-aps-environment-entitlement-string-found-error-for-ios)[Error message when sending a notification](/push-notifications/faq/#error-message-when-sending-a-notification)[Fetching a push token takes a long time on iOS](/push-notifications/faq/#fetching-a-push-token-takes-a-long-time-on-ios)[Miscellaneous](/push-notifications/faq/#miscellaneous)[Sending notifications directly through FCM and APNs](/push-notifications/faq/#sending-notifications-directly-through-fcm-and-apns)[Notification icon on Android is a grey or white square](/push-notifications/faq/#notification-icon-on-android-is-a-grey-or-white-square)