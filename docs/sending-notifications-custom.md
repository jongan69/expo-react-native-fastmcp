Send notifications with FCM and APNs - Expo Documentation

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

Send notifications with FCM and APNs
====================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/push-notifications/sending-notifications-custom.mdx)

Learn how to send notifications with FCM and APNs.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/push-notifications/sending-notifications-custom.mdx)

---

You may need finer-grained control over your notifications, in which case communicating directly with FCM and APNs may be necessary. The Expo platform does not lock you into using Expo Application Services, and the `expo-notifications` API is push-service agnostic.

> Note: This guide does not aim to be a comprehensive resource for sending notifications via FCM or APNs. We recommend you read the official documentation to make sure you're following the latest instructions.

Obtaining a device token for FCM or APNs
----------------------------------------

When using Expo notification service, you use the `ExpoPushToken` obtained with [`getExpoPushTokenAsync`](/versions/latest/sdk/notifications#getexpopushtokenasyncoptions-expotokenoptions-expopushtoken).

If you instead want to send notifications via FCM or APNs, you need to obtain the native device token with [`getDevicePushTokenAsync`](/versions/latest/sdk/notifications#getdevicepushtokenasync-devicepushtoken).

```
import * as Notifications from 'expo-notifications';
...
- const token = (await Notifications.getExpoPushTokenAsync()).data;
+ const token = (await Notifications.getDevicePushTokenAsync()).data;
// send token to your server

```

FCMv1 server
------------

This guide is based on [Firebase official documentation](https://firebase.google.com/docs/cloud-messaging/server).

Communicating with FCM is done by sending a POST request. However, before sending or receiving any notifications, you'll need to follow the steps to [configure FCM](/push-notifications/fcm-credentials) and get your `FCM-SERVER-KEY`.

### Getting an authentication token

FCM requires an Oauth 2.0 access token, which must be obtained via one of the methods described in ["Update authorization of send requests"](https://firebase.google.com/docs/cloud-messaging/migrate-v1#update-authorization-of-send-requests).

For testing purposes, you can use the Google Auth Library and your private key file obtained above, to obtain a short lived token for a single notification, as in this Node example adapted from Firebase documentation:

```
import { JWT } from 'google-auth-library';

function getAccessTokenAsync(
  key: string // Contents of your FCM private key file
) {
  return new Promise(function (resolve, reject) {
    const jwtClient = new JWT(
      key.client_email,
      null,
      key.private_key,
      ['https://www.googleapis.com/auth/cloud-platform'],
      null
    );
    jwtClient.authorize(function (err, tokens) {
      if (err) {
        reject(err);
        return;
      }
      resolve(tokens.access_token);
    });
  });
}

```

### Sending the notification

The example code below calls `getAccessTokenAsync()` above to get the Oauth 2.0 token, then constructs and sends the notification POST request. Note that unlike FCM legacy protocol, the endpoint for the request includes the name of your Firebase project.

```
// FCM_SERVER_KEY: Environment variable with the path to your FCM private key file
// FCM_PROJECT_NAME: Your Firebase project name
// FCM_DEVICE_TOKEN: The client's device token (see above in this document)

async function sendFCMv1Notification() {
  const key = require(process.env.FCM_SERVER_KEY);
  const firebaseAccessToken = await getAccessTokenAsync(key);
  const deviceToken = process.env.FCM_DEVICE_TOKEN;

  const messageBody = {
    message: {
      token: deviceToken,
      data: {
        channelId: 'default',
        message: 'Testing',
        title: `This is an FCM notification message`,
        body: JSON.stringify({ title: 'bodyTitle', body: 'bodyBody' }),
        scopeKey: '@yourExpoUsername/yourProjectSlug',
        experienceId: '@yourExpoUsername/yourProjectSlug',
      },
    },
  };

  const response = await fetch(
    `https://fcm.googleapis.com/v1/projects/${process.env.FCM_PROJECT_NAME}/messages:send`,
    {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${firebaseAccessToken}`,
        Accept: 'application/json',
        'Accept-encoding': 'gzip, deflate',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(messageBody),
    }
  );

  const readResponse = (response: Response) => response.json();
  const json = await readResponse(response);

  console.log(`Response JSON: ${JSON.stringify(json, null, 2)}`);
}

```

The `experienceId` and `scopeKey` fields are only applicable when using Expo Go (from SDK 53, push notifications support is removed from Expo Go). Otherwise, your notifications will not go through to your app. FCM has a list of supported fields in the [notification payload](https://firebase.google.com/docs/cloud-messaging/http-server-ref#notification-payload-support), and you can see which ones are supported by `expo-notifications` on Android by looking at the [FirebaseRemoteMessage](/versions/latest/sdk/notifications#firebaseremotemessage).

FCM also provides some [server-side libraries in a few different languages](https://firebase.google.com/docs/cloud-messaging/send-message#node.js) you can use instead of raw `fetch` requests.

### How to find FCM server key

Your FCM server key can be found by making sure you've followed the [configuration steps](/push-notifications/push-notifications-setup#android), and instead of uploading your FCM key to Expo, you would use that key directly in your server (as the `FCM-SERVER-KEY` in the previous example).

APNs server
-----------

> This documentation is based on [Apple's documentation](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html), and this section covers the basics to get you started.

Communicating with APNs is a little more complicated than with FCM. Some libraries wrap all of this functionality into one or two function calls such as [`node-apn`](https://github.com/node-apn/node-apn). However, in the examples below, a minimum set of libraries are used.

### Authorization

Initially, before sending requests to APNS, you need permission to send notifications to your app. This is granted via a JSON web token which is generated using iOS developer credentials:

* APN key (`.p8` file) associated with your app
* Key ID of the above `.p8` file
* Your Apple Team ID

```
const jwt = require("jsonwebtoken");
const authorizationToken = jwt.sign(
  {
    iss: "YOUR-APPLE-TEAM-ID"
    iat: Math.round(new Date().getTime() / 1000),
  },
  fs.readFileSync("./path/to/appName_apns_key.p8", "utf8"),
  {
    header: {
      alg: "ES256",
      kid: "YOUR-P8-KEY-ID",
    },
  }
);

```

### HTTP/2 connection

After getting the `authorizationToken`, you can open up an HTTP/2 connection to Apple's servers. In development, send requests to `api.sandbox.push.apple.com`. In production, send requests to `api.push.apple.com`.

Here's how to construct the request:

```
const http2 = require('http2');

const client = http2.connect(
  IS_PRODUCTION ? 'https://api.push.apple.com' : 'https://api.sandbox.push.apple.com'
);

const request = client.request({
  ':method': 'POST',
  ':scheme': 'https',
  'apns-topic': 'YOUR-BUNDLE-IDENTIFIER',
  ':path': '/3/device/' + nativeDeviceToken, // This is the native device token you grabbed client-side
  authorization: `bearer ${authorizationToken}`, // This is the JSON web token generated in the "Authorization" step
});
request.setEncoding('utf8');

request.write(
  JSON.stringify({
    aps: {
      alert: {
        title: "ð§ You've got mail!",
        body: 'Hello world! ð',
      },
    },
    experienceId: '@yourExpoUsername/yourProjectSlug', // Required when testing in the Expo Go app
    scopeKey: '@yourExpoUsername/yourProjectSlug', // Required when testing in the Expo Go app
  })
);
request.end();

```

> This example is minimal and includes no error handling and connection pooling. For testing purposes, you can refer to [`sendNotificationToAPNS`](https://github.com/expo/expo/blob/main/docs/public/static/examples/sendNotificationToAPNS.js) example code.

APNs provide their full list of supported fields in the [notification payload](https://developer.apple.com/documentation/usernotifications/generating-a-remote-notification#Payload-key-reference).

[Previous (Push notifications - Reference)

Add Android FCM V1 credentials](/push-notifications/fcm-credentials)[Next (Push notifications - Reference)

Troubleshooting and FAQ](/push-notifications/faq)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/push-notifications/sending-notifications-custom.mdx)
* Last updated on March 12, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Obtaining a device token for FCM or APNs](/push-notifications/sending-notifications-custom/#obtaining-a-device-token-for-fcm-or-apns)[FCMv1 server](/push-notifications/sending-notifications-custom/#fcmv1-server)[Getting an authentication token](/push-notifications/sending-notifications-custom/#getting-an-authentication-token)[Sending the notification](/push-notifications/sending-notifications-custom/#sending-the-notification)[How to find FCM server key](/push-notifications/sending-notifications-custom/#how-to-find-fcm-server-key)[APNs server](/push-notifications/sending-notifications-custom/#apns-server)[Authorization](/push-notifications/sending-notifications-custom/#authorization)[HTTP/2 connection](/push-notifications/sending-notifications-custom/#http2-connection)