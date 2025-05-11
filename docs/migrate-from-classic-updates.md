Migrate from Classic Updates - Expo Documentation

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

Migrate from Classic Updates
============================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/migrate-from-classic-updates.mdx)

A guide to help migrate from Classic Updates to EAS Update.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/migrate-from-classic-updates.mdx)

---

> SDK 49 was the last version to support Classic Updates. To continue using the deprecated `expo publish` command, set [`updates.useClassicUpdates`](/versions/latest/config/app#useclassicupdates) in your app config.

EAS Update is the next generation of Expo's updates service. If you're using Classic Updates, this guide will help you upgrade to EAS Update.

Prerequisites
-------------

EAS Update requires the following versions or greater:

* Expo SDK >= 45.0.0
* Expo CLI >= 5.3.0
* EAS CLI >= 0.50.0
* expo-updates >= 0.13.0

Install EAS CLI
---------------

1

Install EAS CLI:

Terminal

Copy

`-Â``npm install --global eas-cli`

2

Then, log in with your expo account:

Terminal

Copy

`-Â``eas login`

Configure your project
----------------------

You'll need to make the following changes to your project:

1

Initialize your project with EAS Update:

Terminal

Copy

`-Â``eas update:configure`

After this command, you should have two new fields in your app config at `expo.updates.url` and `expo.runtimeVersion`.

2

To ensure that updates are compatible with the underlying native code inside a build, EAS Update uses a new field named `runtimeVersion` that replaces the `sdkVersion` field in your project's app config. Remove the `expo.sdkVersion` property from your app config.

3

To allow updates to apply to builds built with EAS, update your EAS Build profiles in eas.json to include `channel` properties. These channels replace `releaseChannel` properties. We find it convenient to name the `channel` after the profile's name. For instance, the `preview` profile has a `channel` named `"preview"` and the `production` profile has a `channel` named `"production"`.

eas.json

Copy

```
{
  "build": {
    "development": {
      "developmentClient": true,
      "distribution": "internal"
    },
    "preview": {
      "distribution": "internal",
      "channel": "preview"
    },
    "production": {
      "channel": "production"
    }
  }
}

```

4

Optional: If your project is a bare React Native project, see [Use EAS Update in an existing project](/eas-update/getting-started) for the extra configuration you may need.

Create new builds
-----------------

The changes above affect the native code layer inside builds, which means you'll need to make new builds to start sending updates. Once your builds are complete, you'll be ready to publish an update.

Publish an update
-----------------

After making a change to your project locally, you're ready to publish an update, run:

Terminal

Copy

`-Â``eas update --channel [channel-name] --message [message]`

  
`# Example`

`-Â``eas update --channel production --message "Fixes typo"`

Once published, you can see the update in the [Expo dashboard](https://expo.dev/accounts/%5Baccount%5D/projects/%5Bproject%5D/updates).

Additional migration steps
--------------------------

* Replace instances of `expo publish` with `eas update` in scripts. You can view all the options for publishing with `eas update --help`.
* If you have any code that references `Updates.releaseChannel` from the `expo-updates` library, replace them with `Updates.channel`.
* Remove any code that references `Constants.manifest`. That will now always return `null`. You can access most properties you'll need with `Constants.expoConfig` from the `expo-constants` library.

Learn more
----------

The steps described above allow you to use a similar flow to Classic Updates. However, EAS Update is more flexible and has more features. It can be used to create more stable release flows. Learn [how EAS Update works](/eas-update/how-it-works) and how you can craft a more stable [deployment process](/eas-update/deployment-patterns) for your project and your team.

If you experience issues with migrating, check out our [debugging guide](/eas-update/debug). If you have feedback, join us on [Discord](https://chat.expo.dev/) in the #update channel.

[Previous (EAS Update - Reference)

Migrate from CodePush](/eas-update/codepush)[Next (EAS Update - Reference)

Trace update ID back to the Expo Dashboard](/eas-update/trace-update-id-expo-dashboard)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/migrate-from-classic-updates.mdx)
* Last updated on April 29, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Prerequisites](/eas-update/migrate-from-classic-updates/#prerequisites)[Install EAS CLI](/eas-update/migrate-from-classic-updates/#install-eas-cli)[Configure your project](/eas-update/migrate-from-classic-updates/#configure-your-project)[Create new builds](/eas-update/migrate-from-classic-updates/#create-new-builds)[Publish an update](/eas-update/migrate-from-classic-updates/#publish-an-update)[Additional migration steps](/eas-update/migrate-from-classic-updates/#additional-migration-steps)[Learn more](/eas-update/migrate-from-classic-updates/#learn-more)