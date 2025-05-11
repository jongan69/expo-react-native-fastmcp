Sync credentials between remote and local sources - Expo Documentation

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

Sync credentials between remote and local sources
=================================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/app-signing/syncing-credentials.mdx)

Learn how to sync credentials between remote and local sources.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/app-signing/syncing-credentials.mdx)

---

If you use automatically managed credentials, your credentials will be hosted remotely on EAS servers, but you may encounter a situation where you want to pull your credentials down to run a build locally. And if you use local credentials, you may find yourself in a position where you want to upload credentials specified in credentials.json up to EAS to be managed for you. Both of these are possible using the `eas credentials` command.

Downloading credentials
-----------------------

To download your automatically managed credentials, run `eas credentials` in the root of your project, pick a platform, choose `"Credentials.json: Upload/Download credentials between EAS servers and your local json"`, and then `"Download credentials from EAS to credentials.json"`. Run the command again to download the credentials for another platform, if needed.

Android credentials will be ready to use immediately because your project will read the credentials from credentials.json.

iOS credentials require two steps to set up locally. You will first need to install the distribution certificate into your keychain. Next, open your project Xcode and navigate to the "Signing & Capabilities" section, then import your provisioning profile and select it.

Uploading credentials
---------------------

To upload your credentials from credentials.json to be managed by EAS, run `eas credentials` in the root of your project, pick a platform, choose `"Credentials.json: Upload/Download credentials between EAS servers and your local json"`, and then `"Upload credentials from credentials.json to EAS"`. Run the command again to upload the credentials for another platform, if needed.

[Previous (EAS Build - App signing)

Existing credentials](/app-signing/existing-credentials)[Next (EAS Build - App signing)

Security](/app-signing/security)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/app-signing/syncing-credentials.mdx)
* Last updated on June 22, 2023

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Downloading credentials](/app-signing/syncing-credentials/#downloading-credentials)[Uploading credentials](/app-signing/syncing-credentials/#uploading-credentials)