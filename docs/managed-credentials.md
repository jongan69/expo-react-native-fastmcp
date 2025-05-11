Using automatically managed credentials - Expo Documentation

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

Using automatically managed credentials
=======================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/app-signing/managed-credentials.mdx)

Learn how to automatically manage your app credentials with EAS.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/app-signing/managed-credentials.mdx)

---

For your app to be distributed in an app store, it needs to be digitally signed with credentials such as a keystore or a distribution certificate. This certifies the source of the app and ensures that it can't be tampered with. Other credentials, such as your FCM API Key and Apple Push Key are needed to send push notifications, but they are not involved in app signing.

That's all that you need to know about any of this to build an app with EAS Build, but if you would like to learn more you can refer to the [App Signing](/app-signing/app-credentials) guide.

Read on to learn how EAS can automatically manage credentials for you and your team.

Generating app signing credentials
----------------------------------

When you run `eas build`, you will be prompted to generate credentials if you have not done so already. Follow the simple instructions to generate your credentials. Where needed, they will be stored on EAS servers. On subsequent builds of your app, these credentials will be re-used unless you specify otherwise.

Generating your iOS credentials (distribution certificate, provisioning profile, and push key) requires you to sign in with an [Apple Developer Program](https://developer.apple.com/programs) membership.

> If you have any security concerns about EAS managing your credentials or about logging in to your Apple Developer account through EAS CLI, see [Security](/app-signing/security) guide. If that does not satisfy your concerns, you can reach out to [secure@expo.dev](mailto:secure@expo.dev) for more information, or use [local credentials](/app-signing/local-credentials) instead.

### Push notification credentials

#### Android

The Android push notification credentials setup for EAS Build requires configuring your app with FCM. Run `eas credentials`, select `Android`, then `Push Notifications: Manage your FCM Api Key`, and then choose the appropriate option to set up the key.

#### iOS

If you haven't set up your Push Notifications key yet, EAS CLI will ask you to set it up during the next `eas build` run.

You can also set up the Push Notifications key with the `eas credentials` command. Run it, select `iOS`, then `Push Notifications: Manage your Apple Push Notifications Key`, and then choose the appropriate option to set up the key.

Sharing credentials with your team
----------------------------------

If you collaborate on your project with other developers, it is often useful to give them access to perform builds on their own. [Ensure that your project is configured for collaboration](/accounts/account-types#organizations) and any teammates that you have added through your [Expo dashboard](https://expo.dev/) will be able to run `eas build` seamlessly, provided that they have sufficient permissions.

After you have generated your iOS credentials, it's no longer necessary to have access to the Apple Developer team to start a build. This means that your collaborators can start new iOS builds with only their Expo accounts.

Inspecting credentials configuration
------------------------------------

You can view your currently configured app signing credentials by running `eas credentials`. This command also lets you remove and modify credentials, should you need to make any changes. Typically this is not necessary, but you may want to use it if you want to [sync your credentials to your local machine to run a build locally](/app-signing/syncing-credentials) or [migrate existing credentials to be automatically managed](/app-signing/existing-credentials).

[Previous (EAS Build - App signing)

App credentials](/app-signing/app-credentials)[Next (EAS Build - App signing)

Local credentials](/app-signing/local-credentials)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/app-signing/managed-credentials.mdx)
* Last updated on December 18, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Generating app signing credentials](/app-signing/managed-credentials/#generating-app-signing-credentials)[Push notification credentials](/app-signing/managed-credentials/#push-notification-credentials)[Sharing credentials with your team](/app-signing/managed-credentials/#sharing-credentials-with-your-team)[Inspecting credentials configuration](/app-signing/managed-credentials/#inspecting-credentials-configuration)