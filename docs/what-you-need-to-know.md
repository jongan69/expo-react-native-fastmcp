What you need to know about notifications - Expo Documentation

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

Troubleshooting

Regulatory compliance

[Data and Privacy protection](/regulatory-compliance/data-and-privacy-protection)[GDPR compliance](/regulatory-compliance/gdpr)[HIPAA compliance](/regulatory-compliance/hipaa)[Privacy Shield](/regulatory-compliance/privacy-shield)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

What you need to know about notifications
=========================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/push-notifications/what-you-need-to-know.mdx)

Learn about notification types and their behavior before you get started.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/push-notifications/what-you-need-to-know.mdx)

---

Notifications are alerts that inform users of new information or events, even when the app isn't actively in use. They have a large surface area and differences across platforms can make implementing notifications intimidating.

Whether you are starting with notifications or have existing knowledge, this document explains the different types of notification and their behaviors.

Expo's notification support builds on top of the native functionality provided by Android and iOS. The same concepts and behaviors from native platforms apply to Expo apps. If you are unsure about a specific notification feature, see each platform's [official documentation](/push-notifications/what-you-need-to-know#external-references).

Remote and Local notifications
------------------------------

1. Push Notifications: (also known as "remote notifications") Notifications that are sent to a user's device from a remote server.
2. Local Notifications: (also known as "in-app notifications") Notifications that are created and displayed from within the app. Since many of the APIs that create these notifications will create them at a particular time, these may also sometimes be called "scheduled notifications".

`expo-notifications` supports both push and local notifications. You must use a [development build](/develop/development-builds/introduction) to use push notifications since the capability is not built into Expo Go.

See [in-app notifications](/versions/latest/sdk/notifications#present-a-local-in-app-notification-to-the-user) on how to create and display a local notification. The rest of this guide focuses on push notifications.

Push Notification delivery
--------------------------

When a push notification arrives to your app, its behavior depends on the app's state and the type of notification. Let's clarify the terminology:

### Application states

* Foreground: The app is actively running in the foreground. Its interface is currently being displayed on the screen.
* Background: The app is running in the background, "minimized". Its interface is not currently being displayed on the screen.
* Terminated: The app was "killed", usually by a swipe-away gesture in the app switcher. On Android, if the user force-stops the app from device settings, it must be manually reopened for notifications to start working (this is a limitation of Android).

### Push Notification behaviors

For any kind of notification, when the app is in the foreground, the app is in control of how an incoming notification is handled. The app may present it directly, show some custom in-app UI, or even ignore it (this is controlled by [`NotificationHandler`](/versions/latest/sdk/notifications#setnotificationhandlerhandler)). When the app is not in the foreground, the behavior depends on the type of notification.

The table below summarizes what happens when a push notification is delivered to the device:

| Notification Type | App in Foreground | App in Background | App Terminated |
| --- | --- | --- | --- |
| [Notification Message](/push-notifications/what-you-need-to-know#notification-message) and [Notification Message with data payload](/push-notifications/what-you-need-to-know#notification-message-with-data-payload) | delivery runs [`NotificationReceivedListener`](/versions/latest/sdk/notifications#addnotificationreceivedlistenerlistener) and [JS task](/versions/latest/sdk/notifications#registertaskasynctaskname) | OS shows notification | OS shows notification |
| [Headless Background Notification](/push-notifications/what-you-need-to-know#headless-background-notifications) | delivery runs [`NotificationReceivedListener`](/versions/latest/sdk/notifications#addnotificationreceivedlistenerlistener) and [JS task](/versions/latest/sdk/notifications#registertaskasynctaskname) | delivery runs [JS task](/versions/latest/sdk/notifications#registertaskasynctaskname) | delivery runs [JS task](/versions/latest/sdk/notifications#registertaskasynctaskname) |

For the cases when the user interacts with the notification (for example, by pressing an action button), the following handlers are made available to you.

| App state | iOS Listener(s) triggered | Android Listener(s) triggered |
| --- | --- | --- |
| Foreground | `NotificationResponseReceivedListener` | `NotificationResponseReceivedListener` |
| Background | `NotificationResponseReceivedListener` | `NotificationResponseReceivedListener` and [JS task](/versions/latest/sdk/notifications#registertaskasynctaskname) |
| Terminated | `NotificationResponseReceivedListener` | [JS task](/versions/latest/sdk/notifications#registertaskasynctaskname) |

In the table above, whenever `NotificationResponseReceivedListener` is triggered, also `useLastNotificationResponse` return value would change.

> When the app is not running or killed and is started by tapping on a notification, the `NotificationResponseReceivedListener` should be registered early (module top-level) to be triggered on iOS. For action buttons that bring the app to the foreground, we recommend to capture the response using `useLastNotificationResponse` or `getLastNotificationResponseAsync` after the app starts.

Push Notification types
-----------------------

### Notification Message

A Notification Message is a notification that specifies presentational information, such as a title or body text.

* On Android, this corresponds to a push notification request that contains [`AndroidNotification`](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#AndroidNotification)
* On iOS, this corresponds to a push notification request that contains [`aps.alert` dictionary](https://developer.apple.com/documentation/usernotifications/generating-a-remote-notification#Create-the-JSON-payload) and the `apns-push-type` header set to `alert`.

When you use the Expo Push Service, and specify `title`, `subtitle`, `body`, `icon`, or `channelId`, the resulting push notification request is a Notification Message.

The typical use case for a Notification Message is to have it presented to the user immediately without any extra processing being done.

### Notification Message with data payload

This is an Android-only term ([see the official docs](https://firebase.google.com/docs/cloud-messaging/concept-options#data_messages)) where a push notification request contains both `data` field and a `notification` field.

On iOS, extra data may be part of a regular Notification Message request. Apple doesn't distinguish between Notification Message which does and does not carry data.

### Headless Background Notifications

Headless Notification is a remote notification that doesn't directly specify presentational information such as the title or body text. With the exception below\*, headless notifications are not presented to users. Instead, they carry data (JSON) which is processed by a JavaScript task defined in your app via [`registerTaskAsync`](/versions/latest/sdk/notifications#registertaskasynctaskname). The task may perform arbitrary logic. For example, write to `AsyncStorage`, make an api request, or present a local notification whose content is taken from the push notification's data.

> We use the term "Headless Background Notification" to refer to the [Data Message](https://firebase.google.com/docs/cloud-messaging/concept-options#data_messages) on Android and the [background notification](https://developer.apple.com/documentation/usernotifications/pushing-background-updates-to-your-app#Create-a-background-notification) on iOS. Their key similarities are that both of these notification types allow sending only JSON data, and background processing by the app.

Headless Background Notifications have the ability to run custom JavaScript in response to a notification *even when the app is terminated*. This is powerful but comes with a limitation: even when the notification is delivered to the device, the OS does not guarantee its delivery to your app. This may happen due to a variety of reasons, such as when [Doze mode](https://developer.android.com/training/monitoring-device-state/doze-standby) is enabled on Android, or when you send too many background notifications â Apple recommends not to [send more than two or three per hour](https://developer.apple.com/documentation/usernotifications/pushing-background-updates-to-your-app#overview).

When you use the Expo Push Service, and specify only `data` and `_contentAvailable: true` (and other non-interactive fields such as `ttl`), the resulting push notification request produces a Headless Background Notification.

> To use Headless Background Notifications on iOS, you have to [configure](/versions/latest/sdk/notifications#background-notification-configuration) them first.

The rule of thumb is to prefer a regular Notification Message if you don't require running JavaScript in the background.

\* The exception is when you specify `title` or `message` inside of [`data`](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#AndroidConfig). In that case, `expo-notifications` package automatically presents the headless notification on Android, but not on iOS. We plan to make this behavior more consistent across platforms in a future release.

### Data-only notifications

Android has a concept of [Data Messages](https://firebase.google.com/docs/cloud-messaging/concept-options#data_messages). iOS does not have exactly the same concept, but a close equivalent is [Headless Background Notifications](/push-notifications/what-you-need-to-know#headless-background-notifications).

You may also come across the term "silent notification", which is yet another name for notifications that don't present anything to the user â we describe these as [Headless Background Notifications](/push-notifications/what-you-need-to-know#headless-background-notifications).

External references
-------------------

This is a non-exhaustive list of official resources for push notifications on Android and iOS:

* [Android - About FCM messages](https://firebase.google.com/docs/cloud-messaging/concept-options)
* [iOS - Generating a remote notification](https://developer.apple.com/documentation/usernotifications/generating-a-remote-notification)
* [iOS - Pushing background updates to your app](https://developer.apple.com/documentation/usernotifications/pushing-background-updates-to-your-app)

[Previous (Push notifications)

Overview](/push-notifications/overview)[Next (Push notifications)

Expo push notifications setup](/push-notifications/push-notifications-setup)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/push-notifications/what-you-need-to-know.mdx)
* Last updated on May 06, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Remote and Local notifications](/push-notifications/what-you-need-to-know/#remote-and-local-notifications)[Push Notification delivery](/push-notifications/what-you-need-to-know/#push-notification-delivery)[Application states](/push-notifications/what-you-need-to-know/#application-states)[Push Notification behaviors](/push-notifications/what-you-need-to-know/#push-notification-behaviors)[Push Notification types](/push-notifications/what-you-need-to-know/#push-notification-types)[Notification Message](/push-notifications/what-you-need-to-know/#notification-message)[Notification Message with data payload](/push-notifications/what-you-need-to-know/#notification-message-with-data-payload)[Headless Background Notifications](/push-notifications/what-you-need-to-know/#headless-background-notifications)[Data-only notifications](/push-notifications/what-you-need-to-know/#data-only-notifications)[External references](/push-notifications/what-you-need-to-know/#external-references)