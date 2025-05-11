How to trace an update ID back to the Expo Dashboard - Expo Documentation

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

How to trace an update ID back to the Expo Dashboard
====================================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/trace-update-id-expo-dashboard.mdx)

Learn how to trace an update ID back to the Expo Dashboard when using EAS Update and expo-updates library.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/trace-update-id-expo-dashboard.mdx)

---

When working with [EAS Updates](/eas-update/introduction), you might encounter a scenario where you need to trace an `updateId` back to the [Expo dashboard](https://expo.dev/accounts/%5Baccount%5D). This can be challenging because `Updates.updateId` always returns an ID, regardless of whether [`Updates.isEmbeddedLaunch`](/versions/latest/sdk/updates#updatesisembeddedlaunch) is `true` or `false`. However, if the app is running an embedded update, attempting to look up the `updateId` in the [Expo dashboard](https://expo.dev/accounts/%5Baccount%5D) will result in an error. This happens because embedded updates are not tracked in the dashboard.

Determine if the update is embedded or downloaded
-------------------------------------------------

To avoid this issue, you can use the `Updates.isEmbeddedLaunch` property to determine whether the app is running an embedded update or one downloaded from the server. If `Updates.isEmbeddedLaunch` is `true`, the currently running update is embedded in the build, which means it won't be available in the Expo dashboard.

Here's an example of how you can display whether the update is embedded or downloaded:

UpdateStatus.tsx

Copy

```
import * as Updates from 'expo-updates';
import { Text } from 'react-native';

export default function UpdateStatus() {
  return (
    <Text>
      {Updates.isEmbeddedLaunch
        ? '(Embedded) â You cannot trace this update in the Expo dashboard.'
        : '(Downloaded) â You can trace this update in the Expo dashboard.'}
    </Text>
  );
}

```

When you navigate to an update group in the Expo dashboard (open your project, select Updates, and click a specific update), the URL displays as:

```
https://expo.dev/accounts/[accountName]/projects/[projectName]/updates/[updateGroupId]

```

You can replace `updateGroupId` with the `Updates.updateId` to navigate directly to a specific platform update:

```
https://expo.dev/accounts/[accountName]/projects/[projectName]/updates/[updateId]

```

This opens the corresponding update group for the platform-specific update.

[Previous (EAS Update - Reference)

Migrate from Classic Updates](/eas-update/migrate-from-classic-updates)[Next (EAS Update - Reference)

Estimate bandwidth usage](/eas-update/estimate-bandwidth)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/trace-update-id-expo-dashboard.mdx)
* Last updated on January 31, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).