EAS Metadata - Expo Documentation

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

EAS Metadata
============

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas/metadata.mdx)

An introduction to automate and maintain your app store presence from the command line with EAS Metadata.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas/metadata.mdx)

---

> EAS Metadata is in preview and subject to breaking changes.

EAS Metadata enables you to automate and maintain your app store presence from the command line.

You need to provide a lot of information to multiple app stores before your users can use your app. This information is often about complex topics that don't apply to your app. You have to start a lengthy review process after providing the information. When the reviewer finds any issues in the information you provided, you need to restart this process.

EAS Metadata uses a [store.config.json](/eas/metadata/config#static-store-config) file to provide information instead of going through multiple forms in the app store dashboards. When it's time to update the app stores, you can push the store config to the app stores.

Terminal

Copy

`-Â``eas metadata:push`

EAS Metadata can also instantly identify known app store restrictions that could trigger a rejection after a lengthy review queue.

Adding the store config file to your repository enables you to collaborate with other team members to prepare the app submission.

> Using VS Code? Install the [Expo Tools extension](https://github.com/expo/vscode-expo#readme) for auto-complete, suggestions, and warnings in your store.config.json files.

Get started
-----------

[Introduction

Add EAS Metadata to a new project, or generate the store config from an existing app.](/eas/metadata/getting-started)
[Customize the store config

Customize the store config to adapt EAS Metadata to your preferred workflow.](/eas/metadata/config)
[Store config schema

Explore all configurable options EAS Metadata has to offer.](/eas/metadata/schema)

[Previous (EAS Update - Reference)

FAQ](/eas-update/faq)[Next (EAS Metadata)

Get started](/eas/metadata/getting-started)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas/metadata.mdx)
* Last updated on April 29, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).