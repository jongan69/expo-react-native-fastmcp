App credentials - Expo Documentation

[Docs](/)

[Blog](https://expo.dev/blog)[Changelog](https://expo.dev/changelog)[Star Us on GitHub](https://github.com/expo/expo)

Search

[Home](/)[Guides](/guides/overview)[EAS](/eas)[Reference](/versions/latest)[Learn](/tutorial/overview)

[Introduction](/eas)[Configuration with eas.json](/eas/json)[Environment variables](/eas/environment-variables)

EAS Workflows

[Get started](/eas/workflows/get-started)[Example CI/CD workflows](/eas/workflows/examples)[Syntax for EAS Workflows](/eas/workflows/syntax)[Automating EAS CLI commands](/eas/workflows/automating-eas-cli)

Reference

EAS Build

[Introduction](/build/introduction)[Create your first build](/build/setup)[Configure with eas.json](/build/eas-json)[Internal distribution](/build/internal-distribution)[Automate submissions](/build/automate-submissions)[Using EAS Update](/build/updates)[Trigger builds from CI](/build/building-on-ci)[Trigger builds from GitHub App](/build/building-from-github)[Expo Orbit](/build/orbit)

App signing

[App credentials](/app-signing/app-credentials)[Automatically managed credentials](/app-signing/managed-credentials)[Local credentials](/app-signing/local-credentials)[Existing credentials](/app-signing/existing-credentials)[Sync credentials between remote and local sources](/app-signing/syncing-credentials)[Security](/app-signing/security)[Apple Developer Program roles and permissions](/app-signing/apple-developer-program-roles-and-permissions)

Custom builds

Reference

EAS Hosting

[Introduction](/eas/hosting/introduction)[Get started](/eas/hosting/get-started)[Deployments and aliases](/eas/hosting/deployments-and-aliases)[Environment variables](/eas/hosting/environment-variables)[Custom domain](/eas/hosting/custom-domain)[Monitoring API routes](/eas/hosting/api-routes)[Workflows](/eas/hosting/workflows)

Reference

EAS Submit

[Introduction](/submit/introduction)[Submit to the Google Play Store](/submit/android)[Submit to the Apple App Store](/submit/ios)[Configure with eas.json](/submit/eas-json)

EAS Update

[Introduction](/eas-update/introduction)[Get started](/eas-update/getting-started)

Preview

Deployment

Concepts

Troubleshooting

Reference

EAS Metadata

[Introduction](/eas/metadata)[Get started](/eas/metadata/getting-started)

Reference

EAS Insights

[Introduction](/eas-insights/introduction)

Distribution

[Overview](/distribution/introduction)[App stores best practices](/distribution/app-stores)[App transfers](/distribution/app-transfers)[Understanding app size](/distribution/app-size)

Reference

[Webhooks](/eas/webhooks)

Expo accounts

Billing

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

App credentials
===============

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/app-signing/app-credentials.mdx)

Learn about what app credentials Android and iOS require.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/app-signing/app-credentials.mdx)

---

Expo automates the process of signing your app for Android and iOS, but in both cases, you can choose to provide your overrides. [EAS Build](/build/introduction) can generate signed or unsigned applications, but to distribute your application through the stores, it must be a signed application.

On this page, you'll learn about the credentials that each platform requires. If you're curious about how we store your credentials on our end, take a look at our [security documentation](/app-signing/security).

Android
-------

Google requires all Android apps to be digitally signed with a certificate before they are installed on a device or updated. Usually,
a private key and its public certificate are stored in a keystore. In the past, APKs uploaded to the store were required to be signed with
the app signing certificate (a certificate that will be attached to the app in the Play Store), and if the keystore was lost there was no way to
recover or reset it. Now, you can opt-in to App Signing by Google Play and simply upload an APK signed with an upload certificate, and Google Play will automatically replace it with the app signing certificate. Both the old method (app signing certificate) and new method (upload certificate) are essentially the same mechanisms, but using the new method, if your upload keystore is lost or compromised, you can contact the Google Play support team to reset the key.

From the Expo build process's perspective, there is no difference between whether an app is signed with an upload certificate or an app signing key. Either way, `eas build` will generate an .apk or .aab signed with the keystore currently associated with your application. If you want to generate an upload keystore manually, you can do that the same way you created your original keystore.

See [Android's documentation](https://developer.android.com/studio/publish/app-signing) to find more information about this process.

### App signing by Google Play

When you [upload your first release to Google Play](https://expo.fyi/first-android-submission) you will see a notice about "App signing by Google Play" and "Google is protecting your app signing key". This is the default behavior and requires no action on your behalf except to press "Continue".

If you currently manage your app signing key and want Google to manage it for you, see [Use app signing by Google Play](https://support.google.com/googleplay/android-developer/answer/9842756).

Lost your keystore? Learn how to reset your upload key on Google Play

To sync your Expo keystore with Google, follow these steps:

#### Download credentials

In a terminal window:

1. Run `eas credentials` command.
2. Select `Android` for the platform and the profile whose credentials you wish to download.
3. Select the option `credentials.json: Upload/Download credentials between EAS servers and your local json`.
4. Select `Download credentials from EAS to credentials.json`.

Your application's keystore should be kept private. Under no circumstances should you check it into your repository. Debug keystores are the only exception because we don't use them for uploading apps to the Google Play Store.

#### Export keystore to `pem` format

Once you have downloaded your credentials and the keystore, export it to the `pem` format so that you can submit it to Google:

1. Find the key alias in your credentials.json file under the `keyAlias` key.
2. Use `keytool` to export the certificate:

Terminal

Copy

`-Â``keytool -export -rfc -alias alias_from_step_1 -file certificate_for_google.pem -keystore ./path/to/keystore.jks`

#### Contact Google support

Contact Google Support and request them to change your key using [this support form](https://support.google.com/googleplay/android-developer/contact/key). While filling out the form, attach the `pem` file exported from the keystore.

Once Google updates this on your account, builds created through `eas build` will be correctly signed as expected by the Google Play Store. Note that Google will set the validity start date of the new upload certificate to 72 hours in the future so you'll have to wait before your first submission after performing this process.

iOS
---

The 3 primary iOS credentials, all of which are associated with your Apple Developer account, are:

* Distribution Certificate
* Provisioning Profiles
* Push Notification Keys

Whether you let EAS handle all your credentials, or you handle them yourself, it can be valuable to understand what each of these credentials means, when and where they're used, and what happens when they expire or are revoked. You can inspect and manage all your credentials with EAS CLI by running `eas credentials`.

### Distribution certificate

The distribution certificate is all about you, the developer, and not about any particular app. You may only have one distribution certificate associated with your Apple Developer account. This certificate will be used for all of your apps. If this certificate expires, your apps in production will not be affected. However, you will need to generate a new certificate if you want to upload new apps to the App Store or update any of your existing apps. Deleting a distribution certificate has no effect on any apps already on the App Store. You can clear the distribution certificate Expo currently has stored for your app the next time you build by running `eas credentials` and following the prompts.

### Push Notification keys

Apple Push Notification Keys (often abbreviated as APN keys) allow the associated apps to send and receive push notifications.

You can have a maximum of 2 APN keys associated with your Apple Developer account, and a single key can be used with any number of apps. If you revoke an APN key, all apps that rely on that key will no longer be able to send or receive push notifications until you upload a new key to replace it. Uploading a new APN key will not change your users' [Expo Push Tokens](/versions/latest/sdk/notifications#notificationsgetexpopushtokenasync). Push notification keys do not expire. You can clear the APN key Expo currently has stored for your app by running `eas credentials` and following the prompts.

> APN keys created by Expo can be downloaded on the [Expo website](https://expo.dev/accounts/%5Baccount%5D/settings/credentials).

### Provisioning profiles

Each profile is app-specific, meaning you will have a provisioning profile for every app you submit to the App Store. These provisioning profiles are associated with your distribution certificate, so if that is revoked or expired, you'll need to regenerate the app's provisioning profile, as well. Similar to the distribution certificate, revoking your app's provisioning profile will not have any effect on apps already on the App Store.

Provisioning profiles expire after 12 months, but this won't affect apps in production. You will just need to create a new one the next time you build your app by running `eas build -p ios`, or manually with `eas credentials`.

### Summary

| Credential | Limit Per Account | App-specific? | Can be revoked with no production side effects? | Used at |
| --- | --- | --- | --- | --- |
| Distribution Certificate | 2 |  |  | Build time |
| Push Notification Key | 2 |  |  | Run time |
| Provisioning Profile | Unlimited |  |  | Build time |

### Clearing credentials

When you use the `eas credentials` command to delete your credentials, this only removes those credentials from Expo's servers. It does not delete the credentials from Apple's perspective. This means that to fully delete your credentials (for example, if you want a new push notification key, however, you already have two), you'll need to do so from the [Apple Developer Console](https://developer.apple.com/account/resources/certificates/list).

### Re-signing new credentials

You can use `eas build:resign` to codesign an existing .ipa for iOS to a new ad hoc provisioning profile. This helps reduce time when distributing internally â for example, if you want to add a new test device to an existing build, you can use this command to update the provisioning profile to include the device without rebuilding the entire app from scratch.

Running the command will ask you to select a build that you want to re-sign. For example, running the command in an example project shows an available build:

![Running eas build:resign command shows a list of available builds in a project.](/static/images/eas-build/eas-build-resign.png)

After selecting the build, follow the steps to log in to your Apple Developer account. When prompted Show devices and ask me again, you can select a new provisioning profile.

Select a new device, and the command will run the EAS Build again. Note that the build triggered this time reuses the application artifact from the selected build and codesigns it with the new provisioning profile. Once this process is complete, you can use this new build link to install the .ipa on the iOS device added to the provisioning profile.

[Previous (EAS Build)

Expo Orbit](/build/orbit)[Next (EAS Build - App signing)

Automatically managed credentials](/app-signing/managed-credentials)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/app-signing/app-credentials.mdx)
* Last updated on July 24, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Android](/app-signing/app-credentials/#android)[App signing by Google Play](/app-signing/app-credentials/#app-signing-by-google-play)[iOS](/app-signing/app-credentials/#ios)[Distribution certificate](/app-signing/app-credentials/#distribution-certificate)[Push Notification keys](/app-signing/app-credentials/#push-notification-keys)[Provisioning profiles](/app-signing/app-credentials/#provisioning-profiles)[Summary](/app-signing/app-credentials/#summary)[Clearing credentials](/app-signing/app-credentials/#clearing-credentials)[Re-signing new credentials](/app-signing/app-credentials/#re-signing-new-credentials)