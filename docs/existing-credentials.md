Using existing credentials - Expo Documentation

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

Using existing credentials
==========================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/app-signing/existing-credentials.mdx)

Learn about different options for supplying your app signing credentials to EAS Build.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/app-signing/existing-credentials.mdx)

---

EAS Build gives you two options for how you can supply your build jobs with app signing credentials:

1. [Automatically managed credentials](/app-signing/managed-credentials): EAS can host your app signing credentials and take care of sharing them with teammates that have the necessary permissions.
2. [Local credentials](/app-signing/local-credentials): You create a credentials.json file in your project that points to your keystore (Android) and/or provisioning profile and distribution certificate (iOS), along with associated passwords. This is uploaded from your local machine at the time any given build job is run, and disposed of once that build job has completed.

Regardless of which option you choose, your first step for using your existing set of credentials is to set them up as local credentials in credentials.json. Refer to the [credentials.json section of the local credentials guide](/app-signing/local-credentials#credentialsjson) for more information on how to do this.

Once your credentials.json file is configured, you can run `eas credentials`, choose a platform, and then select `"Update credentials on Expo servers with values from credentials.json"` to upload them to be hosted and managed by EAS, if you would like. [Read more about syncing credentials](/app-signing/syncing-credentials).

[Previous (EAS Build - App signing)

Local credentials](/app-signing/local-credentials)[Next (EAS Build - App signing)

Sync credentials between remote and local sources](/app-signing/syncing-credentials)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/app-signing/existing-credentials.mdx)
* Last updated on December 18, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).