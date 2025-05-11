Asset selection and exclusion - Expo Documentation

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

Asset selection and exclusion
=============================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/asset-selection.mdx)

Learn how to use the asset selection feature and verify that an update includes all required app assets.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/asset-selection.mdx)

---

Experimental asset selection feature allows the developer to specify that only certain assets should be included in updates. This can greatly reduce the number of assets that need to be uploaded to and downloaded from the updates server. This feature will work with the EAS Update server or any custom server that complies with the [`expo-updates` protocol](/technical-specs/expo-updates-1).

SDK 52 launched this feature to general availability.

Using asset selection
---------------------

To use asset selection in SDK 51 and below, include the property `extra.updates.assetPatternsToBeBundled` in your app config. It should define one or more file-matching patterns (regular expressions). For example, an app.json file has the patterns defined in the following way:

app.json

Copy

```
  "expo": {
    %%placeholder-start%%... %%placeholder-end%%
    "extra": {
      "updates": {
        "assetPatternsToBeBundled": [
          "app/images/**/*.png"
        ]
      }
    }
  }

```

To use asset selection in SDK 52 and above, include the property `updates.assetPatternsToBeBundled` in your app config. It should define one or more file-matching patterns (regular expressions). For example, an app.json file has the patterns defined in the following way:

app.json

Copy

```
  "expo": {
    %%placeholder-start%%... %%placeholder-end%%
    "updates": {
      "assetPatternsToBeBundled": [
        "app/images/**/*.png"
      ]
    }
  }

```

After adding this configuration all .png files in all subdirectories of app/images will be included in updates. You have to also ensure that these assets need to be required in your JavaScript code.

If `assetPatternsToBeBundled` isn't included in the app config, all assets resolved by the bundler will be included in updates (as per SDK 49 and earlier behavior).

Verifying that an update includes all required app assets
---------------------------------------------------------

When using the asset selection, assets that do not match any file patterns will resolve in the Metro bundler. However, these assets will not be uploaded to the updates server. You have to be certain that assets not included in updates are built into the native build of the app.

If you are building your app locally or have access to the correct build for publishing updates (with the same [runtime version](/eas-update/runtime-versions)), then use the `npx expo-updates assets:verify` command. It allows you to check whether all required assets will be included when you publish an update:

Terminal

Copy

`-Â``npx expo-updates assets:verify <dir>`

> This new command is part of the `expo-updates` CLI, which also supports [EAS Update code signing](/eas-update/code-signing). It is not part of the [Expo CLI](/more/expo-cli) or the [EAS CLI](https://github.com/expo/eas-cli). Only available for ([`expo-updates`](/versions/latest/sdk/updates) >= 0.24.10).

You can also use the `--help` option with the command to see the available options:

| Option | Description |
| --- | --- |
| `<dir>` | Directory of the Expo project. Default: Current working directory. |
| `-a, --asset-map-path <path>` | Path to the assetmap.json in an export produced by the command `npx expo export --dump-assetmap` . |
| `-e, --exported-manifest-path <path>` | Path to the metadata.json in an export produced by the command `npx expo export --dump-assetmap`. |
| `-b, --build-manifest-path <path>` | Path to the app.manifest file created by `expo-updates` in an Expo application build (either android or ios). |
| `-p, --platform <platform>` | Options: ["android", "ios"] |
| `-h, --help` | Usage info. |

Example
-------

[Working example

See a working example of using asset selection, the `assets:verify` command, and other EAS Update features.](https://github.com/expo/UpdatesAPIDemo)

[Previous (EAS Update - Reference)

Code signing](/eas-update/code-signing)[Next (EAS Update - Reference)

Using without other EAS services](/eas-update/standalone-service)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/asset-selection.mdx)
* Last updated on May 01, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Using asset selection](/eas-update/asset-selection/#using-asset-selection)[Verifying that an update includes all required app assets](/eas-update/asset-selection/#verifying-that-an-update-includes-all-required-app-assets)[Example](/eas-update/asset-selection/#example)