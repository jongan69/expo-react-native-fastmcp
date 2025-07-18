Expo push notifications setup - Expo Documentation

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

Expo push notifications setup
=============================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/push-notifications/push-notifications-setup.mdx)

Learn how to set up push notifications, get credentials for development and production, and send a testing push notification.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/push-notifications/push-notifications-setup.mdx)

---

To utilize Expo push notification service, you must configure your app by installing a set of libraries, implement functions to handle notifications, and set up credentials for Android and iOS.

Complete the steps outlined in this guide or follow the more detailed video below. At the end, you'll be able to send a push notification and receive it on a device.

[![Expo Notifications with EAS | Complete Guide](https://i3.ytimg.com/vi/BCCjGtKtBjE/maxresdefault.jpg)

Expo Notifications with EAS | Complete Guide

Learn how to set up push notifications in an Expo project. This video covers configuring Firebase for FCM v1 on Android, setting up Android and iOS credentials on EAS, building with EAS Build, and testing with Expo Notifications tool.](https://www.youtube.com/watch?v=BCCjGtKtBjE)
  

To get the client-side ready for push notifications, the following things are required:

* The user's permission to send them push notifications.
* The app's [`ExpoPushToken`](/versions/latest/sdk/notifications#expopushtoken).

  
Do you want to use FCM / APNs directly, instead of the Expo push notification service?

If you need finer-grained control over your notifications, communicating directly with FCM and APNs may be necessary. Expo does not lock you into using Expo Application Services, and the `expo-notifications` API is push-service agnostic. Learn how to ["Send notifications with FCM and APNs"](/push-notifications/sending-notifications-custom).

Prerequisites
-------------

> Important: Push notifications are not supported on Android Emulators and iOS Simulators. A real device is required.

The following steps described in this guide use [EAS Build](/build/introduction). This is the easiest way to set up notifications since your EAS project will also contain the [notification credentials](/push-notifications/push-notifications-setup#get-credentials-for-development-builds). However, you can use the `expo-notifications` library without EAS Build by building [your project locally](/guides/local-app-development).

1

Install libraries
-----------------

Run the following command to install the `expo-notifications`, `expo-device` and `expo-constants` libraries:

Terminal

Copy

`-Â``npx expo install expo-notifications expo-device expo-constants`

* [`expo-notifications`](/versions/latest/sdk/notifications) library is used to request a user's permission and to obtain the `ExpoPushToken` for sending push notifications.
* [`expo-device`](/versions/latest/sdk/device) is used to check whether the app is running on a physical device.
* [`expo-constants`](/versions/latest/sdk/constants) is used to get the `projectId` value from the app config.

2

Add a minimal working example
-----------------------------

The code below shows a working example of how to register for, send, and receive push notifications in a React Native app. Copy and paste it into your project:

App.tsx

Copy

```
import { useState, useEffect, useRef } from 'react';
import { Text, View, Button, Platform } from 'react-native';
import * as Device from 'expo-device';
import * as Notifications from 'expo-notifications';
import Constants from 'expo-constants';

Notifications.setNotificationHandler({
  handleNotification: async () => ({
    shouldPlaySound: true,
    shouldSetBadge: true,
    shouldShowBanner: true,
    shouldShowList: true,
  }),
});

async function sendPushNotification(expoPushToken: string) {
  const message = {
    to: expoPushToken,
    sound: 'default',
    title: 'Original Title',
    body: 'And here is the body!',
    data: { someData: 'goes here' },
  };

  await fetch('https://exp.host/--/api/v2/push/send', {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Accept-encoding': 'gzip, deflate',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(message),
  });
}

function handleRegistrationError(errorMessage: string) {
  alert(errorMessage);
  throw new Error(errorMessage);
}

async function registerForPushNotificationsAsync() {
  if (Platform.OS === 'android') {
    Notifications.setNotificationChannelAsync('default', {
      name: 'default',
      importance: Notifications.AndroidImportance.MAX,
      vibrationPattern: [0, 250, 250, 250],
      lightColor: '#FF231F7C',
    });
  }

  if (Device.isDevice) {
    const { status: existingStatus } = await Notifications.getPermissionsAsync();
    let finalStatus = existingStatus;
    if (existingStatus !== 'granted') {
      const { status } = await Notifications.requestPermissionsAsync();
      finalStatus = status;
    }
    if (finalStatus !== 'granted') {
      handleRegistrationError('Permission not granted to get push token for push notification!');
      return;
    }
    const projectId =
      Constants?.expoConfig?.extra?.eas?.projectId ?? Constants?.easConfig?.projectId;
    if (!projectId) {
      handleRegistrationError('Project ID not found');
    }
    try {
      const pushTokenString = (
        await Notifications.getExpoPushTokenAsync({
          projectId,
        })
      ).data;
      console.log(pushTokenString);
      return pushTokenString;
    } catch (e: unknown) {
      handleRegistrationError(`${e}`);
    }
  } else {
    handleRegistrationError('Must use physical device for push notifications');
  }
}

export default function App() {
  const [expoPushToken, setExpoPushToken] = useState('');
  const [notification, setNotification] = useState<Notifications.Notification | undefined>(
    undefined
  );

  useEffect(() => {
    registerForPushNotificationsAsync()
      .then(token => setExpoPushToken(token ?? ''))
      .catch((error: any) => setExpoPushToken(`${error}`));

    const notificationListener = Notifications.addNotificationReceivedListener(notification => {
      setNotification(notification);
    });

    const responseListener = Notifications.addNotificationResponseReceivedListener(response => {
      console.log(response);
    });

    return () => {
      notificationListener.remove();
      responseListener.remove();
    };
  }, []);

  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'space-around' }}>
      <Text>Your Expo push token: {expoPushToken}</Text>
      <View style={{ alignItems: 'center', justifyContent: 'center' }}>
        <Text>Title: {notification && notification.request.content.title} </Text>
        <Text>Body: {notification && notification.request.content.body}</Text>
        <Text>Data: {notification && JSON.stringify(notification.request.content.data)}</Text>
      </View>
      <Button
        title="Press to Send Notification"
        onPress={async () => {
          await sendPushNotification(expoPushToken);
        }}
      />
    </View>
  );
}

```

### Configure `projectId`

Using the previous example, when you are registering for push notifications, you need to use [`projectId`](/versions/latest/sdk/constants#easconfig). This property is used to attribute Expo push token to the specific project. For projects using EAS, the `projectId` property represents the Universally Unique Identifier (UUID) of that project.

`projectId` is set automatically when you create a development build. However, we recommend setting it manually in your project's code. To do so, you can use [`expo-constants`](/versions/latest/sdk/constants) to get the `projectId` value from the app config.

```
const projectId = Constants?.expoConfig?.extra?.eas?.projectId ?? Constants?.easConfig?.projectId;
const pushTokenString = (await Notifications.getExpoPushTokenAsync({ projectId })).data;

```

One advantage of attributing the Expo push token to your project's ID is that it doesn't change when a project is transferred between different accounts or the existing account gets renamed.

3

Get credentials for development builds
--------------------------------------

For Android and iOS, there are different requirements to set up your credentials.

Android

iOS

For Android, you need to configure Firebase Cloud Messaging (FCM) to get credentials and set up your Expo project.

Follow the steps in [Add Android FCM V1 credentials](/push-notifications/fcm-credentials) to set up your credentials.

> A paid Apple Developer Account is required to generate credentials.

For iOS, make sure you have [registered your iOS device](/develop/development-builds/create-a-build#create-a-development-build-for-the-device) on which you want to test before running the `eas build` command for the first time.

If you create a development build for the first time, you'll be asked to enable push notifications. Answer yes to the following questions when prompted by the EAS CLI:

* Setup Push Notifications for your project
* Generating a new Apple Push Notifications service key

  
> If you are not using EAS Build, run `eas credentials` manually.

4

Build the app
-------------

Terminal

Copy

`-Â``eas build`

5

Test using the push notifications tool
--------------------------------------

After creating and installing the development build, you can use [Expo push notifications tool](https://expo.dev/notifications) to quickly send a test notification to your device.

1. Start the development server for your project:

   Terminal

   Copy

   `-Â``npx expo start`
2. Open the development build on your device.
3. After the `ExpoPushToken` is generated, enter the value in the Expo push notifications tool with other details (for example, a message title and body).
4. Click on the Send a Notification button.

   ![Expo push notifications tool overview.](/static/images/notifications/push-notifications-tool-overview.png)

After sending the notification from the tool, you should see the notification on your device. Below is an example of an Android device receiving a push notification.

![An Android device receiving a push notification.](/static/images/notifications/notification-on-android.png)

[Previous (Push notifications)

About notification types](/push-notifications/what-you-need-to-know)[Next (Push notifications)

Send notifications with the Expo Push Service](/push-notifications/sending-notifications)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/push-notifications/push-notifications-setup.mdx)
* Last updated on May 08, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Prerequisites](/push-notifications/push-notifications-setup/#prerequisites)[Install libraries](/push-notifications/push-notifications-setup/#install-libraries)[Add a minimal working example](/push-notifications/push-notifications-setup/#add-a-minimal-working-example)[Configure projectId](/push-notifications/push-notifications-setup/#configure-projectid)[Get credentials for development builds](/push-notifications/push-notifications-setup/#get-credentials-for-development-builds)[Build the app](/push-notifications/push-notifications-setup/#build-the-app)[Test using the push notifications tool](/push-notifications/push-notifications-setup/#test-using-the-push-notifications-tool)