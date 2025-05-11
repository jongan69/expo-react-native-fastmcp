Estimate bandwidth usage - Expo Documentation

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

Estimate bandwidth usage
========================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/estimate-bandwidth.mdx)

Learn how to estimate bandwidth usage for EAS Update.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/estimate-bandwidth.mdx)

---

Understanding update bandwidth usage
------------------------------------

EAS Update enables an app to update its own non-native pieces (such as JavaScript, styling, and images) over-the-air. This guide explains how bandwidth is consumed and how consumption can be optimized.

Bandwidth calculation breakdown
-------------------------------

Each subscription plan includes a predefined bandwidth allocation per monthly billing period in addition to its monthly active user (MAU) allocation ([learn more about how MAU are calculated](/eas-update/faq#how-are-monthly-updated-users-counted-for-a-billing-cycle)). MAU's beyond the standard allocation are billed at [usage-based pricing rates](https://expo.dev/pricing#update), and each of those additional MAU add an extra 40 MiB to your standard bandwidth allocation. This bandwidth determines the number of updates your users can download before being charged for additional bandwidth usage.

Here's how to estimate bandwidth usage per update:

* Update size: The key factor in bandwidth consumption is the size of update assets that are not already on the device. If an update only modifies the JavaScript portion of your app, users will only download the new JavaScript. To begin an example, let's say the uncompressed JavaScript portion generated during export is 10 MB. Compression will further reduce its size.
* Compression ratio: The level of compression depends on the file type. JavaScript and Hermes bytecode (commonly used in React Native apps) can be compressed, while images and icons are not automatically compressed. In the example above, a Hermes bytecode bundle achieves an estimated 2.6Ã compression ratio, reducing the actual download size to:

  ```
  10 MB / 2.6 â 3.85 MB update bandwidth size

  ```

Given a bandwidth allocation, we estimate how many updates can be downloaded in a monthly billing period before additional bandwidth charges apply. For example, if you have 60,000 MAUs on a production plan, it includes 50,0000 MAU and 1 TiB (1,024 GiB) of bandwidth per month. An additional 10,000 MAUs purchased through usage-based pricing receives an additional 40 MiB of bandwidth per MAU. The total number of updates that can be downloaded is:

```
(1,024 GiB Ã 1,024 MiB/GiB) + (10,000 MAU Ã 40 MiB/MAU) = 1,448,576 MiB per month
1,448,576 MiB / 3.85 MiB â 376,254 updates

```

Measuring your actual update size
---------------------------------

To determine the actual compressed size of your Hermes bundle, run the following commands:

Terminal

Copy

`-Â``brotli -5 -k bundle.hbc`

`-Â``gzip -9 -k bundle.hbc`

`-Â``ls -lh bundle.hbc.br bundle.hbc.gz`

This will generate Brotli- and Gzip-compressed versions of your Hermes bundle (bundle.hbc.br and bundle.hbc.gz) and display their sizes. You can use this to refine bandwidth calculations based on your app's real-world update sizes.

Factors that affect bandwidth consumption
-----------------------------------------

Actual bandwidth usage varies due to:

* User behavior: Theoretical calculations assume every user downloads every update. However, many users only get updates when they reopen the app, often skipping intermediate updates. As a result, actual bandwidth usage is usually much lower than the theoretical maximum.
* Missing assets: If an update includes assets such as fonts and images that are not already on the device from the build or previously downloaded updates, they will need to be downloaded as well.

Optimizing bandwidth usage
--------------------------

1. Monitor usage first: The easiest way to manage bandwidth is to track your [usage metrics](https://expo.dev/accounts/%5Baccount%5D/settings/usage) and identify any unusual spikes or inefficiencies.
2. Optimize asset size: Reduce the size of your assets with [this guide](/eas-update/optimize-assets).
3. Exclude assets when needed: Use [asset selection](/eas-update/asset-selection) to reduce the number of assets included with each update. This is an advanced optimization and other approaches should be tried first.

[Previous (EAS Update - Reference)

Trace update ID back to the Expo Dashboard](/eas-update/trace-update-id-expo-dashboard)[Next (EAS Update - Reference)

Integrate in existing native apps](/eas-update/integration-in-existing-native-apps)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/estimate-bandwidth.mdx)
* Last updated on February 18, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Understanding update bandwidth usage](/eas-update/estimate-bandwidth/#understanding-update-bandwidth-usage)[Bandwidth calculation breakdown](/eas-update/estimate-bandwidth/#bandwidth-calculation-breakdown)[Measuring your actual update size](/eas-update/estimate-bandwidth/#measuring-your-actual-update-size)[Factors that affect bandwidth consumption](/eas-update/estimate-bandwidth/#factors-that-affect-bandwidth-consumption)[Optimizing bandwidth usage](/eas-update/estimate-bandwidth/#optimizing-bandwidth-usage)