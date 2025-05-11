Rollbacks - Expo Documentation

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

[Deploy updates](/eas-update/deployment)[Downloading updates](/eas-update/download-updates)[Rollouts](/eas-update/rollouts)[Rollbacks](/eas-update/rollbacks)[Optimize assets](/eas-update/optimize-assets)[Continuous deployment](/eas-update/continuous-deployment)[Alternative deployment patterns](/eas-update/deployment-patterns)

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

Rollbacks
=========

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/rollbacks.mdx)

Rollback a branch to a previous update or the embedded update.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/rollbacks.mdx)

---

There are two types of rollbacks supported by EAS Update:

* Roll back to a previously-published update.
* Roll back to the update embedded in the build.

Start a rollback
----------------

To start a rollback, run the following command:

Terminal

Copy

`-Â``eas update:rollback`

In the terminal, an interactive guide will assist you in selecting the type of rollback and doing the rollback.

Rolling back to a previously-published update
---------------------------------------------

The above command re-publishes a previously-published update to functionally roll back clients to that update.

Rolling back to the update embedded in the build
------------------------------------------------

The above command instructs the client to run the update embedded in the build.

Publishing after the rollback
-----------------------------

Upon publishing again after a rollback, all clients will receive the new update.

[Previous (EAS Update - Deployment)

Rollouts](/eas-update/rollouts)[Next (EAS Update - Deployment)

Optimize assets](/eas-update/optimize-assets)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/rollbacks.mdx)
* Last updated on March 03, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Start a rollback](/eas-update/rollbacks/#start-a-rollback)[Rolling back to a previously-published update](/eas-update/rollbacks/#rolling-back-to-a-previously-published-update)[Rolling back to the update embedded in the build](/eas-update/rollbacks/#rolling-back-to-the-update-embedded-in-the-build)[Publishing after the rollback](/eas-update/rollbacks/#publishing-after-the-rollback)