Obtain Google Service Account Keys using FCM V1 - Expo Documentation

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

Obtain Google Service Account Keys using FCM V1
===============================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/push-notifications/fcm-credentials.mdx)

Learn how to create or use a Google Service Account Key for sending Android Notifications using FCM.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/push-notifications/fcm-credentials.mdx)

---

Create a new Google Service Account Key
---------------------------------------

Here are the steps to configure a new Google Service Account Key in EAS for sending Android Notifications using FCM V1.

1

Create a new Firebase project for your app in the [Firebase Console](https://console.firebase.google.com). If you already have a Firebase project for your app, continue to the next step.

![Create a project in the Firebase Console](/static/images/creating-google-service-account/fcm-v1/new-service-account/01-new-firebase-project.png)

2

In the Firebase console, open Project settings > [Service accounts](https://console.firebase.google.com/project/_/settings/serviceaccounts/adminsdk) for your project.

![Service accounts settings tab in Firebase console](/static/images/creating-google-service-account/fcm-v1/new-service-account/02-manage-service-accounts.png)

3

Click Generate New Private Key, then confirm by clicking Generate Key. Securely store the JSON file containing the private key.

![Generate a new private key in the Firebase Console](/static/images/creating-google-service-account/fcm-v1/new-service-account/03-generate-key.png)

4

Upload the JSON file to EAS and configure it for sending Android notifications. This can be done using EAS CLI or in [Expo dashboard](https://expo.dev).

EAS CLI

expo.dev

* Run `eas credentials`
* Select `Android` > `production` > `Google Service Account`
* Select `Manage your Google Service Account Key for Push Notifications (FCM V1)`
* Select `Set up a Google Service Account Key for Push Notifications (FCM V1)` > `Upload a new service account key`
* If you've previously stored the JSON file in your project directory, the EAS CLI automatically detects the file and prompts you to select it. Press `Y` to continue.

> Note: Add the JSON file to your version source control's ignore file (for example, .gitignore) to avoid committing it to your repository since it contains sensitive data.

* Under Project > Configuration, click [Credentials](https://expo.dev/accounts/%5Baccount%5D/projects/%5Bproject%5D/credentials) in the navigation menu
* For Android, click Add Application Identifier or select an existing Application identifier
* Under Service Credentials > FCM V1 service account key, click Add a service account key

![Project credentials page on expo.dev](/static/images/creating-google-service-account/fcm-v1/new-service-account/04-upload-credential-1.png)

* Under Upload new key, upload your JSON credential and click Save

![Save the service account key file to the project](/static/images/creating-google-service-account/fcm-v1/new-service-account/04-upload-credential-2.png)

5

Configure the google-services.json file in your project. Download it from the Firebase Console and place it at the root of your project directory.

Note: You can skip this step if google-services.json has already been set up.

![Download google-services.json from Firebase Cloud Console](/static/images/creating-google-service-account/fcm-v1/new-service-account/05-setup-google-services-json.png)

In app.json, add [`expo.android.googleServicesFile`](/versions/latest/config/app#googleservicesfile) with its value as the path of the google-services.json.

app.json

Copy

```
{
  "expo": {
  %%placeholder-start%%...%%placeholder-end%%
  "android": {
    %%placeholder-start%%...%%placeholder-end%%
    "googleServicesFile": "./path/to/google-services.json"
  }
}

```

6

You're all set! You can now send notifications to Android devices via Expo Push Notifications using the FCM V1 protocol.

![Service account key successfully uploaded](/static/images/creating-google-service-account/fcm-v1/new-service-account/06-upload-credential-complete.png)

Use an existing Google Service Account Key
------------------------------------------

1

Open the [IAM Admin page](https://console.cloud.google.com/iam-admin/iam?authuser=0) in Google Cloud Console. In the Permissions tab, locate the Principal you intend to modify and click the pencil icon for Edit Principal.

![Edit Principal in IAM Admin page in Google Cloud Console](/static/images/creating-google-service-account/fcm-v1/existing-service-account/01-iam-admin-page.png)

2

Click Add Role and select the Firebase Messaging API Admin role from the dropdown. Click Save.

![Assign roles](/static/images/creating-google-service-account/fcm-v1/existing-service-account/02-add-role-1.png)![Select the Firebase Messaging API Admin role](/static/images/creating-google-service-account/fcm-v1/existing-service-account/02-add-role-2.png)![Save the role assignment](/static/images/creating-google-service-account/fcm-v1/existing-service-account/02-add-role-3.png)

3

You have to specify to EAS which JSON credential file to use for sending FCM V1 notifications, using EAS CLI or in [Expo dashboard](https://expo.dev). You can upload a new JSON file or select a previously uploaded file.

EAS CLI

expo.dev

* Run `eas credentials`
* Select `Android` > `production` > `Google Service Account`
* Select `Manage your Google Service Account Key for Push Notifications (FCM V1)`
* Select `Set up a Google Service Account Key for Push Notifications (FCM V1)` > `Upload a new service account key`
* The EAS CLI automatically detects the file on your local machine and prompts you to select it. Press `Y` to continue.

> Note: Add the JSON file to your version source control's ignore file (for example, .gitignore) to avoid committing it to your repository since it contains sensitive data.

* Under Project > Configuration, click [Credentials](https://expo.dev/accounts/%5Baccount%5D/projects/%5Bproject%5D/credentials) in the navigation menu
* For Android, click Add Application Identifier or select an existing Application identifier
* Under Service Credentials > FCM V1 service account key, click Add a service account key

![Project credentials page on expo.dev](/static/images/creating-google-service-account/fcm-v1/new-service-account/04-upload-credential-1.png)

* Under Upload new key, upload your JSON credential and click Save

![Save the service account key file to the project](/static/images/creating-google-service-account/fcm-v1/new-service-account/04-upload-credential-2.png)

4

Configure the google-services.json file in your project. Download it from the Firebase Console and place it at the root of your project directory. If you're using version control, add it to your ignore file (for example, .gitignore) as it contains sensitive data.

Note: You can skip this step if google-services.json has already been set up.

![Download google-services.json from Firebase Cloud Console](/static/images/creating-google-service-account/fcm-v1/existing-service-account/04-setup-google-services-json.png)

In app.json, add [`expo.android.googleServicesFile`](/versions/latest/config/app#googleservicesfile) with its value as the path of the google-services.json.

app.json

Copy

```
{
  "expo": {
    %%placeholder-start%%...%%placeholder-end%%
    "android": {
      %%placeholder-start%%...%%placeholder-end%% "googleServicesFile": "./path/to/google-services.json"
    }
  }
}

```

5

You're all set! You can now send notifications to Android devices via Expo Push Notifications using the FCM V1 protocol.

![Service account key successfully uploaded](/static/images/creating-google-service-account/fcm-v1/new-service-account/06-upload-credential-complete.png)

[Previous (Push notifications)

Handle incoming notifications](/push-notifications/receiving-notifications)[Next (Push notifications - Reference)

Send notifications with FCM and APNs](/push-notifications/sending-notifications-custom)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/push-notifications/fcm-credentials.mdx)
* Last updated on January 11, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Create a new Google Service Account Key](/push-notifications/fcm-credentials/#create-a-new-google-service-account-key)[Use an existing Google Service Account Key](/push-notifications/fcm-credentials/#use-an-existing-google-service-account-key)