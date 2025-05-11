Using EAS Update without other EAS services - Expo Documentation

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

[Code signing](/eas-update/code-signing)[Asset selection and exclusion](/eas-update/asset-selection)[Using without other EAS services](/eas-update/standalone-service)[Migrate from CodePush](/eas-update/codepush)[Migrate from Classic Updates](/eas-update/migrate-from-classic-updates)[Trace update ID back to the Expo Dashboard](/eas-update/trace-update-id-expo-dashboard)[Estimate bandwidth usage](/eas-update/estimate-bandwidth)[Integrate in existing native apps](/eas-update/integration-in-existing-native-apps)[FAQ](/eas-update/faq)

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

Using EAS Update without other EAS services
===========================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/standalone-service.mdx)

Learn how to use EAS Update independently of other EAS services, such as Build.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/standalone-service.mdx)

---

EAS Update works great as a standalone service, so you can use it with or without EAS Build and other EAS services. All of its main features are designed to be agnostic of the build pipeline, and its used in production by large organizations that do not use other EAS services.

What are the downsides of using EAS Update without other EAS services?

EAS Update and Build work closely together to provide an experience that is greater than the sum of its parts. For example, when you create a build with EAS Build we will help with the bookkeeping for various aspects related to updates, such as the runtime version and channel.

Builds that use the same channel and runtime version are grouped into a Deployments section on [expo.dev](https://expo.dev/accounts/%5Baccount-name/projects/%5Bproject-name%5D/deployments). These sorts of bookkeeping and insights features that depend on knowledge of builds or other aspects of your app won't be available if you use EAS Update independently of other EAS services.

That said, many organizations are already heavily invested in their CI/CD infrastructure or may have other reasons for wanting to use another build pipeline, and the benefits offered by deeper integration across EAS services may not be worth the switching costs of migrating to a different CI/CD provider.

Using EAS Update without EAS Build
----------------------------------

Most of the [installation and configuration steps](/eas-update/getting-started) are identical whether or not you use EAS Build. The primary difference is how the update [channel](/eas-update/eas-cli) is configured. When using EAS Build, the channel from eas.json will automatically be added to your build's AndroidManifest.xml and Expo.plist at build time. When not using EAS Build, this must be configured manually by [setting the request header in the app config](/eas-update/getting-started#configure-update-channels-in-appjson), followed by manually creating the channel on the server.

Terminal

Copy

`# Create a channel named `production` (for example, which points to the production EAS Update branch by default)``# Your channel names may vary depending on release process`

`-Â``eas channel:create production`

[Previous (EAS Update - Reference)

Asset selection and exclusion](/eas-update/asset-selection)[Next (EAS Update - Reference)

Migrate from CodePush](/eas-update/codepush)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/standalone-service.mdx)
* Last updated on February 13, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).