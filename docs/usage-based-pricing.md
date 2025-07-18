Usage-based pricing - Expo Documentation

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

[Overview](/billing/overview)[Subscriptions, plans, and add-ons](/billing/plans)[Manage plans and billing](/billing/manage)[Payment history, invoices, and receipts](/billing/invoices-and-receipts)[Usage-based pricing](/billing/usage-based-pricing)[FAQ](/billing/faq)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Usage-based pricing
===================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/billing/usage-based-pricing.mdx)

Learn how Expo applies usage-based billing for customers who exceed their plan quotas and how to monitor your EAS Build usage.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/billing/usage-based-pricing.mdx)

---

Expo applies usage-based billing for customers who exceed their [plan](/billing/plans) allowances. This enables our customers to use what they need without worrying about limitations or requiring contractual obligations.

Usage-based billing is enabled for EAS Build and EAS Update and is billed monthly. We provide an estimate of your existing usage and any overage charges on your [account's Billing](https://expo.dev/settings/billing).

How usage-based pricing works
-----------------------------

### EAS Build

For EAS Build, a flat fee is charged for an individual build executed at higher-priority levels. This is totaled monthly and charged at the end of your billing period or sooner if you cancel your plan.

> Note: Builds that are canceled before any work is done are not charged.

[Production, Enterprise, and Legacy plans](/billing/plans#plans) subscribers receive credits for EAS Build. These credits can be used to offset the cost of builds. They are reset at the start of the billing period and expire at the end of that billing period. Visit our [pricing page](https://expo.dev/pricing) for more information on the pricing schedule for supported build platforms and the available resource classes.

#### Example: EAS Build credit usage

Consider an account subscribed to the Production plan that has 15 medium Android builds, and 10 large iOS builds in a billing period:

| Description | Price | Quantity | Total |
| --- | --- | --- | --- |
| Android builds (medium) | $1 | 15 | $15 |
| iOS builds (large) | $4 | 10 | $40 |
| EAS Build Credit |  |  | -$55 |
| Total (USD) |  |  | $0 |

Since the credit is included in the Production plan, the subscriber pays $0 for their 25 builds.

#### Example: EAS Build credit exceeded

Consider another example where the credit limit is exceeded:

| Description | Price | Quantity | Total |
| --- | --- | --- | --- |
| Android builds (medium) | $1 | 20 | $20 |
| Android builds (large) | $2 | 10 | $20 |
| iOS builds (medium) | $2 | 15 | $30 |
| iOS builds (large) | $4 | 15 | $60 |
| EAS Build Credit |  |  | -$99 |
| Total (USD) |  |  | $31 |

In this scenario, the subscriber pays $31 for 60 builds instead of $130 because the EAS Build Credit covers $99.

### EAS Update

Usage-based pricing for EAS Update comprises two metrics: monthly active users and global edge bandwidth.

The "updated users" reflect the number of unique users who download at least one update in a billing period, also known as "monthly active users" (MAU). Global edge bandwidth represents the total amount of bandwidth used beyond your subscription plan's base bandwidth allocation. If your monthly active users exceed your plan's base MAU allocation, 40 MiB of global edge bandwidth is included for each additional user.

> Note: A monthly active user counts only once per billing period, regardless of how many updates this user downloads. In the context of EAS Update, a "user" is considered a unique installation of your app on a device.

Each plan has a number of monthly active users and global edge bandwidth included as part of the subscription. These differ for each plan and the most updated numbers. See our [pricing page](https://expo.dev/pricing), for more information.

#### Example: EAS Update usage

> Note: The [On-demand plan](/billing/plans#on-demand) includes the same amount of monthly active users and global edge bandwidth as the Free plan.

Consider a subscriber to the On-demand plan who deploys 20 updates of 5 MiB each via EAS Update to 10,000 users. The subscription to the plan includes 1,000 monthly active users and 100 GiB per month. As a result, the subscriber's bill for extra usage will be:

| Description | Price | Quantity | Total |
| --- | --- | --- | --- |
| Updated users | $0.005 per user | 9,000 | $45 |
| Global edge bandwidth | $0.10 per GiB | 525 GiB | $52.5 |
| Total (USD) |  |  | $97.5 |

Out of the 10,000 users, 1,000 are included in the On-demand plan. As a result, 9,000 are billed for as part of usage-based billing. Paying for 9,000 updated users also includes approximately 351.6 GiB (9000 users \* 40 MiB / 1024).

The global edge bandwidth calculation is:

| Description | Calculation | Quantity |
| --- | --- | --- |
| Bandwidth used to send updates | 20 updates \* 5 MiB \* 10,000 users | 976.5625 GiB |
|  |  |  |
| Bandwidth included in plan |  | 100 GiB |
| Bandwidth included with 9,000 extra updated users | 9,000 \* 40 MiB | 351.5625 GiB |
| Total | 976.5625 - 100 - 351.5625 | 525 GiB |

If the same subscriber sends the 21st update of 5 MiB to the same 10,000 users in the current billing period, they will only pay for any extra bandwidth used.

| Description | Calculation | Quantity |
| --- | --- | --- |
| Bandwidth used to send updates | 21 updates \* 5 MiB \* 10,000 users | 1,025.39 GiB |
|  |  |  |
| Bandwidth included in plan |  | 100 GiB |
| Bandwidth included with 9,000 extra updated users | 9,000 \* 40 MiB | 351.5625 GiB |
| Total | 1,025.39 - 100 - 351.5625 | 573.83 GiB |

This is because Expo only charges for [unique monthly active users](/eas-update/faq#how-are-monthly-updated-users-counted-for-a-billing-cycle). As a result, the subscriber's bill for extra usage will be:

| Description | Price | Quantity | Total |
| --- | --- | --- | --- |
| Updated users | $0.005 per user | 9,000 | $45 |
| Global edge bandwidth | $0.10 per GiB | 573.83 GiB | $57.4 |
| Total (USD) |  |  | $102.4 |

If the same subscriber is on a Production plan, they will pay $0 as the Production plan includes 50,000 monthly active users and 1 TiB (1024 GiB). As such, there is no extra bandwidth usage.

Monitor usage
-------------

> Note: Billing estimates shown may be delayed by up to 24 hours (one day).

To see the current billing period's usage summary, go to the [Billing](https://expo.dev/settings/billing) and under Usage this month, you will find a summary for both EAS Build and EAS Update usage.

![Billing usage summary for EAS Build and EAS update in the Expo dashboard.](/static/images/billing/usage-01.png)

### EAS Build usage history

To see detailed EAS Build usage for a current or previous billing period:

* Click Usage in the navigation menu.
* Under the EAS Build section, you will find details on builds count and executed builds based on their platform and resource class.

![Detailed EAS Build usage in the Expo dashboard.](/static/images/billing/usage-02.png)

### EAS Update usage history

To see detailed EAS Update usage for a current or previous billing period:

* Click Usage in the navigation menu.
* Under the EAS Update section, you will find details on updated users and global edge bandwidth details.

![Detailed EAS Update usage in the Expo dashboard.](/static/images/billing/usage-03.png)

### Enable notifications for EAS Build usage

You can enable Plan credit usage notifications to closely monitor your EAS Build usage. It enables email notifications when 80% and 100% of your plan's EAS Build credit is used.

To enable EAS Build credit usage notification

* Click Email notifications in the navigation menu under your account's settings:
* Under EAS Build notifications, click Subscribe for Plan credit usage notifications.

![Enabling EAS Build plan credit usage notifications in the Expo dashboard.](/static/images/billing/usage-04.png)

### How to optimize build usage

You can use [EAS Update](/eas-update/introduction) and [development builds](/develop/development-builds/introduction) to test and deploy new code without having to create an entirely new build. This will help you iterate faster and reduce build usage.

For most apps, the JavaScript code changes more frequently than the underlying native code and configuration. If you are building a new build every time for code changes, consider [using EAS Update to take advantage of the different iteration frequency](/eas-update/how-it-works) between JavaScript and native code. This way, you can ship those changes as an update instead.

When using Continuous Integration (CI)/Continuous Deployment (CD) to build pre-production code, you can reduce unnecessary usage by automating the process of building only when changes are made to the native code. You can create a workflow in your CI/CD using [Expo Fingerprint](https://expo.dev/blog/fingerprint-your-native-runtime) to detect when your native code has changed, and only execute a build if it has changed. Otherwise, publish an update if the native code has not changed.

A development build can run any EAS Update that is compatible with its native runtime. If you are using EAS Update with multiple testing channels, you can reduce the need for creating additional builds by having your testers or test devices use the same development build.

### How to optimize update usage

You can manage certain assets to include or exclude when using EAS Update. This reduces the number of assets uploaded or downloaded from the updates server and the global edge bandwidth used.

To optimize storage and bandwidth usage, you can choose to exclude assets that haven't been modified. For example, images or videos that haven't been changed can be excluded. Excluded assets won't be uploaded to the update server and won't be downloaded by the app. However, it's important to make sure that assets that are not part of an update are included in the native build of the app.

> Note: If an app has already downloaded an asset that is also part of a new update, the app will not re-download that asset. This will also not add to your account's bandwidth usage.

You can use `npx expo-updates assets:verify <dir>` to check all required assets are included in the update. For more information, see [Asset selection and exclusion](/eas-update/asset-selection).

[Previous (Reference - Billing)

Payment history, invoices, and receipts](/billing/invoices-and-receipts)[Next (Reference - Billing)

FAQ](/billing/faq)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/billing/usage-based-pricing.mdx)
* Last updated on February 14, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[How usage-based pricing works](/billing/usage-based-pricing/#how-usage-based-pricing-works)[EAS Build](/billing/usage-based-pricing/#eas-build)[EAS Update](/billing/usage-based-pricing/#eas-update)[Monitor usage](/billing/usage-based-pricing/#monitor-usage)[EAS Build usage history](/billing/usage-based-pricing/#eas-build-usage-history)[EAS Update usage history](/billing/usage-based-pricing/#eas-update-usage-history)[Enable notifications for EAS Build usage](/billing/usage-based-pricing/#enable-notifications-for-eas-build-usage)[How to optimize build usage](/billing/usage-based-pricing/#how-to-optimize-build-usage)[How to optimize update usage](/billing/usage-based-pricing/#how-to-optimize-update-usage)