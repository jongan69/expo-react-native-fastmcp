Preview updates - Expo Documentation

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

[Preview updates](/eas-update/preview)[Override update configuration at runtime](/eas-update/override)[Using development builds](/eas-update/expo-dev-client)[Github PR previews](/eas-update/github-actions)

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

Preview updates
===============

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/preview.mdx)

Learn how to preview updates in development, preview, and production builds.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/preview.mdx)

---

Before deploying an update to production, you will often want to test it in a production-like environment. This guide will outline different approaches for previewing updates, and link out to more detailed guides for each approach.

Previewing updates in development builds
----------------------------------------

Development builds are a great way to preview updates from pull requests, directly from the EAS dashboard, or from the built-in UI provided by the `expo-dev-client` library.

[Preview updates in development builds

Learn how to preview updates in development builds.](/eas-update/expo-dev-client)
[Use GitHub Actions to automate publishing updates

Learn how to use GitHub Actions to automate publishing updates with EAS Update](/eas-update/github-actions)
[Launch preview updates from the EAS dashboard using Orbit

Learn how to launch updates with the macOS, Windows, and Linux desktop app Expo Orbit](/review/with-orbit)

Previewing updates in preview builds
------------------------------------

Non-technical users will typically not want to interact with a development build, and they will want to test changes from a preview build on an [App store testing track](/review/overview#app-store-testing-tracks) or [internal distribution](/review/overview#internal-distribution-with-eas-build).

If your team is smaller, it may be sufficient to deploy a single preview build at a time to an app store testing track or internal distribution. You can then publish updates to the channel that is used by that preview build. [Learn more about preview builds](/review/overview).

Alternatively, you can build a mechanism into your preview build that allows users to select a different update or channel to load. This can be useful in cases where the [app runtime](/eas-update/runtime-versions) doesn't change often, and many different updates can be loaded in the same app. [Learn more](/eas-update/override).

[Override update configuration at runtime

Learn how to override the update URL and channel at runtime.](/eas-update/override)

Previewing updates in production builds
---------------------------------------

Before deploying an update to all end-users, some teams will want to first roll it out in production to a small set of internal users. One way this can be accomplished is by [overriding the update channel](/eas-update/override) at runtime for a known subset of users. Be sure to note the [security considerations](/eas-update/override#security-considerations) before proceeding down this path. Additionally, it is not recommended to use this approach for non-internal users because it makes it possible to get the app into a state where it must be uninstalled and reinstalled.

Another approach is to use a deployment pattern like the [Persistent Staging Flow](/eas-update/deployment-patterns#persistent-staging-flow), which involves always having a version of your production app that points to a staging channel.

[Persistent Staging Flow

Learn how to use the Persistent Staging Flow to always have a version of your production app that points to a staging channel.](/eas-update/deployment-patterns#persistent-staging-flow)

[Previous (EAS Update)

Get started](/eas-update/getting-started)[Next (EAS Update - Preview)

Override update configuration at runtime](/eas-update/override)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/preview.mdx)
* Last updated on March 12, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Previewing updates in development builds](/eas-update/preview/#previewing-updates-in-development-builds)[Previewing updates in preview builds](/eas-update/preview/#previewing-updates-in-preview-builds)[Previewing updates in production builds](/eas-update/preview/#previewing-updates-in-production-builds)