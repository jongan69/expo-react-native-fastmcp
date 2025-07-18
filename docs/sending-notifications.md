Send notifications with the Expo Push Service - Expo Documentation

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

Send notifications with the Expo Push Service
=============================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/push-notifications/sending-notifications.mdx)

Learn how to call Expo Push Service API to send push notifications from your server.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/push-notifications/sending-notifications.mdx)

---

The [`expo-notifications`](/versions/latest/sdk/notifications) library provides all the client-side functionality for push notifications. Expo also handles sending push notifications off to FCM and APNs which then send them to particular devices. All you need to do is send a request to Expo Push API with the `ExpoPushToken` you obtain with [`getExpoPushTokenAsync`](/versions/latest/sdk/notifications#getexpopushtokenasyncoptions).

> If you'd rather build a server that communicates with APNs and FCM directly, see [Send notifications with FCM and APNs](/push-notifications/sending-notifications-custom). It's more complex than using Expo Push Service, but allows finer-grained control, and full access to all FCM and APNs features.

![Diagram explaining sending a push from your server to device](/static/images/sending-notification.png)

Send push notifications using a server
--------------------------------------

After you setup your push notification credentials and add logic to get the `ExpoPushToken`, you can send it to the Expo API using an HTTPS POST request. You can do this by setting up a server with a database (or you can also write a command line tool to send them or send them straight from your app).

The Expo team and community have taken care of creating back-ends for you in a few different languages:

| SDKs | Back-end | Maintained by |
| --- | --- | --- |
| [expo-server-sdk-node](https://github.com/expo/expo-server-sdk-node) | Node.js | Expo team |
| [expo-server-sdk-python](https://github.com/expo/expo-server-sdk-python) | Python | Community |
| [expo-server-sdk-ruby](https://github.com/expo/expo-server-sdk-ruby) | Ruby | Community |
| [expo-push-notification-client-rust](https://github.com/katayama8000/expo-push-notification-client-rust) | Rust | Community |
| [expo-notifier](https://github.com/symfony/expo-notifier) | Symfony | Symfony |
| [exponent-server-sdk-php](https://github.com/Alymosul/exponent-server-sdk-php) | PHP | Community |
| [expo-server-sdk-php](https://github.com/ctwillie/expo-server-sdk-php) | PHP | Community |
| [exponent-server-sdk-golang](https://github.com/oliveroneill/exponent-server-sdk-golang) | Golang | Community |
| [exponent](https://github.com/9ssi7/exponent) | Golang | Community |
| [exponent-server-sdk-elixir](https://github.com/rdrop/exponent-server-sdk-elixir) | Elixir | Community |
| [expo-server-sdk-dotnet](https://github.com/glyphard/expo-server-sdk-dotnet) | dotnet | Community |
| [expo-server-sdk-java](https://github.com/hlspablo/expo-server-sdk-java) | Java | Community |
| [laravel-expo-notifier](https://github.com/YieldStudio/laravel-expo-notifier) | Laravel | Community |

Each of the example servers above is a wrapper around Expo Push Service API.

Implement push notifications reliably
-------------------------------------

Push Notifications travel through several systems from your server to recipient devices. Notifications are delivered most of the time. However, occasionally there are issues with systems along the way and the network connections between them. Handling errors helps push notifications to arrive at their destinations more reliably.

### Limit concurrent connections

When sending a large number of push notifications at once, limit the number of your concurrent connections. The [Node SDK](https://github.com/expo/expo-server-sdk-node) implements this for you and opens a maximum of six concurrent connections. This smooths out your peak load and helps the Expo push notification service receive push notification requests successfully.

### Retry on failure

The first step in sending push notifications is to deliver them to the Expo push notification service, which internally adds them to a queue for delivery to Google (FCM v1) and Apple (APNs). This first step can fail for several reasons:

* network issues between your server and the Expo push notification service
* an outage or degraded availability of the Expo notification service
* misconfigured push credentials
* an invalid notification payload

Some of these failures are temporary. For example, if the Expo push notification service is down or unreachable and you get a network error - a HTTP 429 error (Too Many Requests), or a HTTP 5xx error (Server Errors) - use [exponential backoff](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/) to wait a few seconds before retrying. If the first retry attempt is unsuccessful, wait for longer (follow exponential backoff) and retry again. This lets the temporarily unavailable service recover before you retry.

Other failures will not resolve themselves. For example, if your push notification payload is malformed, you may get an HTTP 400 response explaining the issue with the payload. You will also get an error if there are no push credentials for your project or if you send push notifications for different projects in the same request.

### Check push receipts for errors

The Expo push notification service responds with [push tickets](/push-notifications/sending-notifications#push-tickets) upon successfully receiving notifications. A push ticket indicates that Expo has received your notification payload but may still need to send it. Each push ticket contains a ticket ID, which you later use to look up a [push receipt](/push-notifications/sending-notifications#push-receipts). A push receipt is available after Expo has tried to deliver the notification to FCM or APNs. It tells you whether delivery to the push notification provider was successful.

You must check your push receipts. If there is an issue delivering push notifications, the push receipts are the best way to get information about the underlying cause. For example, the receipts may indicate a problem with FCMs or APNs, the Expo push notification service, or your notification payload.

Push receipts may also tell you if a recipient device has unsubscribed from notifications (for example, by revoking notification permissions or uninstalling your app) if APNs or FCM responds with that information. The push receipt will contain a `details` â `error` field set to `DeviceNotRegistered`. In this scenario, stop sending notifications to this device's push token until it re-registers with your server, so your app remains a good citizen. The `DeviceNotRegistered` error appears in push receipts only when Google or Apple deems the device to be unregistered. It takes an undefined amount of time and is often impossible to test by uninstalling your app and sending a push notification shortly after.

We recommend checking push receipts 15 minutes after sending your push notifications. While push receipts are often available much sooner, a 15-minute window gives the Expo push notification service a comfortable amount of time to make the receipts available to you. If after 15 minutes there is no push receipt, this likely indicates an error with the Expo push notification service. Lastly, push receipts are cleared after 24 hours.

### SLAs

The Expo push notification service does not have an SLA and the FCM and APNs services also may have occasional outages. By following the guidance above, you can make your application robust against temporary service interruptions.

HTTP/2 API
----------

Instead of using one of the libraries listed earlier, you may want to send requests directly to our HTTP/2 API (this API currently does not require any authentication).

To do so, send a POST request to `https://exp.host/--/api/v2/push/send` with the following HTTP headers:

```
host: exp.host
accept: application/json
accept-encoding: gzip, deflate
content-type: application/json

```

This is a "hello world" push notification using cURL that you can send using your terminal (replace the placeholder push token with your own):

```
curl -H "Content-Type: application/json" -X POST "https://exp.host/--/api/v2/push/send" -d '{
  "to": "ExponentPushToken[xxxxxxxxxxxxxxxxxxxxxx]",
  "title":"hello",
  "body": "world"
}'

```

The request body must be JSON. It may either be a single [message object](/push-notifications/sending-notifications#message-request-format) (as shown in the example above) or an array of up to 100 message objects, as long as they are all for the same project as shown below. We recommend using an array when you want to send multiple messages to efficiently minimize the number of requests you need to make to Expo servers. Here's an example request body that sends four messages:

```
[
  {
    "to": "ExponentPushToken[xxxxxxxxxxxxxxxxxxxxxx]",
    "sound": "default",
    "body": "Hello world!"
  },
  {
    "to": "ExponentPushToken[yyyyyyyyyyyyyyyyyyyyyy]",
    "badge": 1,
    "body": "You've got mail"
  },
  {
    "to": [
      "ExponentPushToken[zzzzzzzzzzzzzzzzzzzzzz]",
      "ExponentPushToken[aaaaaaaaaaaaaaaaaaaaaa]"
    ],
    "body": "Breaking news!"
  }
]

```

The Expo Push Service also optionally accepts gzip-compressed request bodies. This can greatly reduce the amount of upload bandwidth needed to send large numbers of notifications. The [Node Expo Server SDK](https://github.com/expo/expo-server-sdk-node) automatically gzips requests for you and automatically throttles your requests to smooth out the load, so we highly recommend it.

### Push tickets

The requests above will respond with a JSON object with two optional fields, `data` and `errors`. `data` will contain an array of [push tickets](/push-notifications/sending-notifications#push-ticket-format) in the same order in which the messages were sent (or one push ticket object, if you send a single message to a single recipient). Each ticket includes a `status` field indicating whether Expo successfully received the notification and, if successful, an `id` field that can be used to retrieve a push receipt later.

> A status of `ok` along with a receipt ID means that the message was received by Expo's servers, not that it was received by the user (for that you will need to check the [push receipt](/push-notifications/sending-notifications#push-receipts)).

Continuing the above example, this is what a successful response body looks like:

```
{
  "data": [
    { "status": "ok", "id": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX" },
    { "status": "ok", "id": "YYYYYYYY-YYYY-YYYY-YYYY-YYYYYYYYYYYY" },
    { "status": "ok", "id": "ZZZZZZZZ-ZZZZ-ZZZZ-ZZZZ-ZZZZZZZZZZZZ" },
    { "status": "ok", "id": "AAAAAAAA-AAAA-AAAA-AAAA-AAAAAAAAAAAA" }
  ]
}

```

If there were errors with individual messages, but not the entire request, the bad messages' corresponding push tickets will have a status of `error`, and fields that describe the error as shown below:

```
{
  "data": [
    {
      "status": "error",
      "message": "\"ExponentPushToken[xxxxxxxxxxxxxxxxxxxxxx]\" is not a registered push notification recipient",
      "details": {
        "error": "DeviceNotRegistered"
      }
    },
    {
      "status": "ok",
      "id": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
    }
  ]
}

```

If the entire request failed, the HTTP status code is 4xx or 5xx and the `errors` field will be an array of error objects (usually just one). Otherwise, the HTTP status code will be 200 and your messages will be on their way to the Android and iOS push notification services.

### Push receipts

After receiving a batch of notifications, Expo enqueues each notification to deliver to the Android and iOS push notification services (FCM and APNs, respectively). Most notifications are typically delivered within a few seconds. However, sometimes it may take longer to deliver notifications, particularly if the Android or iOS push notification services take longer than usual to receive and deliver notifications or if Expo's Push Service infrastructure is under high load.

Once Expo delivers a notification to the Android or iOS push notification service, Expo creates a [push receipt](/push-notifications/sending-notifications#push-receipt-response-format) that indicates whether the Android or iOS push notification service successfully received the notification. If there was an error in delivering the notification, perhaps due to faulty credentials or service downtime, the push receipt will contain more information regarding that error.

To fetch the push receipts, send a POST request to `https://exp.host/--/api/v2/push/getReceipts`. The [request body](/push-notifications/sending-notifications#push-receipt-request-format) must be a JSON object with a field name `ids` that is an array of ticket ID strings:

```
curl -H "Content-Type: application/json" -X POST "https://exp.host/--/api/v2/push/getReceipts" -d '{
  "ids": [
    "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
    "YYYYYYYY-YYYY-YYYY-YYYY-YYYYYYYYYYYY",
    "ZZZZZZZZ-ZZZZ-ZZZZ-ZZZZ-ZZZZZZZZZZZZ"
  ]
}'

```

The [response body](/push-notifications/sending-notifications#push-receipt-response-format) for push receipts is very similar to that of push tickets; it is a JSON object with two optional fields, `data` and `errors`. `data` contains a mapping of receipt IDs to receipts. Receipts include a `status` field, and two optional `message` and `details` fields (in the case where `"status": "error"`). If there is no push receipt for a requested receipt ID, the mapping won't contain that ID. This is what a successful response to the above request looks like:

```
{
  "data": {
    "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX": { "status": "ok" },
    "ZZZZZZZZ-ZZZZ-ZZZZ-ZZZZ-ZZZZZZZZZZZZ": { "status": "ok" }
    // When there is no receipt with a given ID (YYYYYYYY-YYYY-YYYY-YYYY-YYYYYYYYYYYY in this
    // example), the ID is omitted from the response.
  }
}

```

You must check each push receipt, since it may contain information about errors you need to resolve. For example, if a device is no longer eligible to receive notifications, Apple's documentation asks that you stop sending notifications to that device. The push receipts contain information about these errors.

> Even if a receipt's `status` says `ok`, this doesn't guarantee that the device has received the message; "ok" in a push receipt means that the Android (FCM) or iOS (APNs) push notification service successfully received the notification. If the recipient device is turned off, for example, the iOS or Android push notification service will try to deliver the message but the device won't necessarily receive it.

If the entire request failed, the HTTP status code will be 4xx or 5xx and the `errors` field will be an array of error objects (usually just one). Otherwise, the HTTP status code will be 200 and your messages will be on their way to your users' devices.

Errors
------

Expo provides details regarding any errors that occur during this entire process. We'll cover some of the most common errors below so that you can implement logic to handle them automatically on your server.

If for whatever reason, Expo couldn't deliver the message to the Android or iOS push notification service, the push receipt's details may also include service-specific information. This is useful mostly for debugging and reporting possible bugs to Expo.

### Individual errors

Inside both push tickets and push receipts, look for a `details` object with an `error` field. If present, it may be one of the following values, and you should handle these errors like so:

### Push ticket errors

* `DeviceNotRegistered`: The device cannot receive push notifications anymore and you should stop sending messages to the corresponding Expo push token.

### Push receipt errors

* `DeviceNotRegistered`: The device cannot receive push notifications anymore and you should stop sending messages to the corresponding Expo push token.
* `MessageTooBig`: The total notification payload was too large. On Android and iOS, the total payload must be at most 4096 bytes.
* `MessageRateExceeded`: You are sending messages too frequently to the given device. Implement exponential backoff and slowly retry sending messages.
* `MismatchSenderId`: This indicates that there is an issue with your FCM push credentials. There are two pieces to FCM push credentials: your FCM server key, and your google-services.json file. Both must be associated with the same sender ID. You can find your sender ID in the [same place you find your server key](/push-notifications/push-notifications-setup#upload-server-credentials). Check that the server key from your project's Expo dashboard under Credentials > Application Identifier > FCM Server Key and that the sender ID from your project's google-services.json > `project_number` is the same as shown in the Firebase console under Project Settings > Cloud Messaging tab > Cloud Messaging API (Legacy).
* `InvalidCredentials`: Your push notification credentials for your standalone app are invalid (for example, you may have revoked them).

  + Android: Make sure that you have correctly uploaded the server key from the Firebase Console as specified in [uploading FCM V1 server credentials](/push-notifications/fcm-credentials).
  + iOS: Run `eas credentials` and follow the prompts to regenerate new push notification credentials. If you revoke an APN key, all apps that rely on that key will no longer be able to send or receive push notifications until you upload a new key to replace it. Uploading a new APN key will not change your users' Expo Push Tokens. Sometimes, these errors will contain further details claiming an `InvalidProviderToken` error. This is actually tied to both your APN key and your provisioning profile. To resolve this error, you should rebuild the app and regenerate a new push key and provisioning profile.

> For a better understanding of iOS credentials, including push notification credentials, read our [App Signing docs](/app-signing/app-credentials#ios).

### Request errors

If there's an error with the entire request for either push tickets or push receipts, the `errors` object might have one of the following values, and you should handle these errors:

* `TOO_MANY_REQUESTS`: You are exceeding the request limit of 600 notifications per second per project. We recommend implementing rate-limiting in your server to prevent sending more than 600 notifications per second (note that if you use [expo-server-sdk-node](https://github.com/expo/expo-server-sdk-node), this is already implemented along with exponential backoffs for retries).
* `PUSH_TOO_MANY_EXPERIENCE_IDS`: You are trying to send push notifications to different Expo experiences, for example, `@username/projectAAA` and `@username/projectBBB`. Check the `details` field for a mapping of experience names to their associated push tokens from the request, and remove any from another experience.
* `PUSH_TOO_MANY_NOTIFICATIONS`: You are trying to send more than 100 push notifications in one request. Make sure you are only sending 100 (or fewer) notifications in each request.
* `PUSH_TOO_MANY_RECEIPTS`: You are trying to get more than 1000 push receipts in one request. Make sure you are only sending an array of 1000 (or fewer) ticket ID strings to get your push receipts.

Additional security
-------------------

You can require any push requests to be sent with a valid [access token](/accounts/programmatic-access) before we will deliver them to your users. You can enable this enhanced push security from your [Expo Dashboard](https://expo.dev/settings/access-tokens).

By default, you can send a notification to your users by sending their Expo Push Token and any text or additional data needed for the message. This is easy to set up, but if the tokens are leaked, a malicious user would be able to impersonate your server and send their message to your users. We have never had an instance of this report. However, to follow best security practices, we offer the use of an access token alongside the push token as an additional layer of security.

If you're using the [`expo-server-sdk-node`](https://github.com/expo/expo-server-sdk-node#usage), upgrade to at least `v3.6.0` and pass your `accessToken` as an option in the constructor. Otherwise, pass in the header `'Authorization': 'Bearer ${accessToken}'` with any requests to our push API.

Any requests sent *without* a valid access token *after* you enable push security will result in an error with code: `UNAUTHORIZED`.

Formats
-------

### Message request format

Each message must be a JSON object with the given fields (only the `to` field is required):

| Field | Platform | Type | Description |
| --- | --- | --- | --- |
| `to` | Android and iOS | `string | string[]` | An Expo push token or an array of Expo push tokens specifying the recipient(s) of this message. |
| `_contentAvailable` | iOS Only | `boolean | undefined` | When this is set to true, the notification will cause the iOS app to start in the background to run a [background task](/versions/latest/sdk/notifications#background-notifications). Your app needs to be [configured](/versions/unversioned/sdk/notifications#background-notification-configuration) to support this. |
| `data` | Android and iOS | `Object` | A JSON object delivered to your app. It may be up to about 4KiB; the total notification payload sent to Apple and Google must be at most 4KiB or else you will get a "Message Too Big" error. |
| `title` | Android and iOS | `string` | The title to display in the notification. Often displayed above the notification body. Maps to [`AndroidNotification.title`](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#AndroidNotification) and [`aps.alert.title`](https://developer.apple.com/documentation/usernotifications/generating-a-remote-notification#Payload-key-reference). |
| `body` | Android and iOS | `string` | The message to display in the notification. Maps to [`AndroidNotification.body`](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#AndroidNotification) and [`aps.alert.body`](https://developer.apple.com/documentation/usernotifications/generating-a-remote-notification#Payload-key-reference). |
| `ttl` | Android and iOS | `number` | Time to Live: the number of seconds for which the message may be kept around for redelivery if it hasn't been delivered yet. Defaults to `undefined` to use the respective defaults of each provider (1 month for Android/FCM as well as iOS/APNs). |
| `expiration` | Android and iOS | `number` | Timestamp since the Unix epoch specifying when the message expires. Same effect as `ttl` (`ttl` takes precedence over `expiration`). |
| `priority` | Android and iOS | `'default' | 'normal' | 'high'` | The delivery priority of the message. Specify `default` or omit this field to use the default priority on each platform ("normal" on Android and "high" on iOS). |
| `subtitle` | iOS Only | `string` | The subtitle to display in the notification below the title. Maps to [`aps.alert.subtitle`](https://developer.apple.com/documentation/usernotifications/generating-a-remote-notification#Payload-key-reference). |
| `sound` | iOS Only | `string | null` | Play a sound when the recipient receives this notification. Specify `default` to play the device's default notification sound, or omit this field to play no sound. Custom sounds need to be [configured](/versions/unversioned/sdk/notifications#configurable-properties) via the config plugin and then specified including the file extension. Example: `bells_sound.wav`. |
| `badge` | iOS Only | `number` | Number to display in the badge on the app icon. Specify zero to clear the badge. |
| `interruptionLevel` | iOS Only | `'active' | 'critical' | 'passive' | 'time-sensitive'` | The importance and delivery timing of a notification. The string values correspond to the [`UNNotificationInterruptionLevel`](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel) enumeration cases. |
| `channelId` | Android Only | `string` | ID of the Notification Channel through which to display this notification. If an ID is specified but the corresponding channel does not exist on the device (that has not yet been created by your app), the notification will not be displayed to the user. |
| `icon` | Android Only | `string` | The notification's icon. Name of an Android drawable resource (example: `myicon`). Defaults to the icon specified in the [config plugin](/versions/latest/sdk/notifications#configurable-properties). |
| `richContent` | Android and iOS | `Object` | Currently supports setting a notification image. Provide an object with key `image` and value of type `string`, which is the image URL. Android will show the image out of the box. On iOS, you need to add a Notification Service Extension target to your app. See [this example](https://github.com/expo/expo/pull/36202) on how to do that. |
| `categoryId` | Android and iOS | `string` | ID of the notification category that this notification is associated with. [Find out more about notification categories here](/versions/latest/sdk/notifications#manage-notification-categories-interactive-notifications). |
| `mutableContent` | iOS Only | `boolean` | Specifies whether this notification can be [intercepted by the client app](https://developer.apple.com/documentation/usernotifications/modifying_content_in_newly_delivered_notifications?language=objc). Defaults to `false`. |

Note on `ttl`: On Android, we make our best effort to deliver messages with zero TTL immediately and do not throttle them. However, setting TTL to a low value (for example, zero) can prevent normal-priority notifications from ever reaching Android devices that are in doze mode. To guarantee that a notification is delivered, TTL must be long enough for the device to wake from doze mode. This field takes precedence over `expiration` when both are specified.

Note on `priority`: On Android, normal-priority messages won't open network connections on sleeping devices and their delivery may be delayed to conserve the battery. High-priority messages are more likely to be delivered immediately and may wake sleeping devices to open network connections, consuming energy. On iOS, normal-priority messages are sent at a time that takes into account power considerations for the device and may be grouped and delivered in bursts. They are throttled and may not be delivered by Apple. High-priority messages are usually sent immediately. Normal priority corresponds to APNs priority level 5 and high priority to 10.

Note on `channelId`: If left null, a "Default" channel is used, and Expo creates the channel on the device if it does not yet exist. However, use caution, as the "Default" channel is user-facing and you may not be able to fully delete it.

### Push ticket format

```
{
  "data": [
    {
      "status": "error" | "ok",
      "id": string, // this is the Receipt ID
      // if status === "error"
      "message": string,
      "details": JSON
    },
    ...
  ],
  // only populated if there was an error with the entire request
  "errors": [{
    "code": string,
    "message": string
  }]
}

```

### Push receipt request format

```
{
  "ids": string[]
}

```

### Push receipt response format

```
{
  "data": {
    Receipt ID: {
      "status": "error" | "ok",
      // if status === "error"
      "message": string,
      "details": JSON
    },
    ...
  },
  // only populated if there was an error with the entire request
  "errors": [{
    "code": string,
    "message": string
  }]
}

```

Delivery guarantees
-------------------

Expo makes a best effort to deliver notifications to the push notification services operated by Google and Apple. Expo's infrastructure is designed for at least one attempt at delivery to the underlying push notification services. It is more likely for a notification to be delivered to Google or Apple more than once rather than not at all; however, both these results are uncommon.

After a notification has been handed off to an underlying push notification service, Expo creates a "push receipt" that records whether the handoff was successful. A push receipt denotes whether the underlying push notification service received the notification.

Finally, the push notification services from Google and Apple follow their own policies to deliver the notifications to the device.

[Previous (Push notifications)

Expo push notifications setup](/push-notifications/push-notifications-setup)[Next (Push notifications)

Handle incoming notifications](/push-notifications/receiving-notifications)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/push-notifications/sending-notifications.mdx)
* Last updated on May 07, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Send push notifications using a server](/push-notifications/sending-notifications/#send-push-notifications-using-a-server)[Implement push notifications reliably](/push-notifications/sending-notifications/#implement-push-notifications-reliably)[Limit concurrent connections](/push-notifications/sending-notifications/#limit-concurrent-connections)[Retry on failure](/push-notifications/sending-notifications/#retry-on-failure)[Check push receipts for errors](/push-notifications/sending-notifications/#check-push-receipts-for-errors)[SLAs](/push-notifications/sending-notifications/#slas)[HTTP/2 API](/push-notifications/sending-notifications/#http2-api)[Push tickets](/push-notifications/sending-notifications/#push-tickets)[Push receipts](/push-notifications/sending-notifications/#push-receipts)[Errors](/push-notifications/sending-notifications/#errors)[Individual errors](/push-notifications/sending-notifications/#individual-errors)[Push ticket errors](/push-notifications/sending-notifications/#push-ticket-errors)[Push receipt errors](/push-notifications/sending-notifications/#push-receipt-errors)[Request errors](/push-notifications/sending-notifications/#request-errors)[Additional security](/push-notifications/sending-notifications/#additional-security)[Formats](/push-notifications/sending-notifications/#formats)[Message request format](/push-notifications/sending-notifications/#message-request-format)[Push ticket format](/push-notifications/sending-notifications/#push-ticket-format)[Push receipt request format](/push-notifications/sending-notifications/#push-receipt-request-format)[Push receipt response format](/push-notifications/sending-notifications/#push-receipt-response-format)[Delivery guarantees](/push-notifications/sending-notifications/#delivery-guarantees)