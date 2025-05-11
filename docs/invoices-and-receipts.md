View payment history, invoices, and receipts - Expo Documentation

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

View payment history, invoices, and receipts
============================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/billing/invoices-and-receipts.mdx)

Learn how to view your account's payment history, download invoices and receipts, and request a refund for a charge.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/billing/invoices-and-receipts.mdx)

---

Receipts in the Expo dashboard provide information about an account's payment history and access to invoices and receipts. It also provides information on payment dates, payment status, and the total amount for that payment. You can also request a refund for a charge if you believe it has been made in error.

> Note: You can only access the Receipts if you have [Owner or Admin access](/accounts/account-types#manage-access) to your account.

Receipts
--------

To view your account's payment history, click [Receipts](https://expo.dev/settings/receipts) in the navigation menu under Account settings or Organization settings.

For example, an [Organization account's](/accounts/account-types#organizations) receipts are shown below:

![Receipts page in the Expo dashboard.](/static/images/billing/receipts-01.png)

### Download and view an invoice

To download and view an invoice for a billing period, go to [Receipts](https://expo.dev/settings/receipts) and:

* Click the Date for the billing period corresponding to the invoice. You will be navigated to a page hosted by Stripe. As an example, the March 22, 2024 invoice below links to this page:

![Download invoice shown in the Stripe dashboard.](/static/images/billing/receipts-02.png)

* Click Download invoice. You will receive a PDF copy of the invoice.

### Download and view a receipt

To download and view a receipt for a billing period, go to [Receipts](https://expo.dev/settings/receipts) and:

* Click the Date for the billing period corresponding to the receipt. You will be navigated to the appropriate receipt hosted by Stripe. As an example, the March 22, 2024 receipt below links to this page:

![Download receipt shown in the Stripe dashboard.](/static/images/billing/receipts-02.png)

* Click on Download receipt. You will receive a PDF copy of the receipt.

### Request a refund

You can request a refund directly from the [Receipts](https://expo.dev/settings/receipts) page. The approval process is manual and our team investigates any errors before providing a refund.

To request a refund:

* Next to a receipt, click the three-dot menu and then click Request Refund:

![Receipts page in the Expo dashboard.](/static/images/billing/receipts-04.png)

* Fill the Request a refund form with details for the refund and click Continue:

![Download invoice shown in the Stripe dashboard.](/static/images/billing/receipts-05.png)

* Our billing team receives and reviews refund requests. Once a refund is approved, the amount is credited to your payment method. Refunds typically take 5 to 10 business days to fully process.

Read an invoice
---------------

An invoice contains your legally registered business name, address, tax ID, invoice number, due date, and more. It also includes a description of any charges and the total amount due. In a typical invoice, the charges are divided into:

* Current plan's subscription amount (if subscribed to a plan)
* Any overage charges (if applicable)
* A plan's credit limit

Let's consider three different examples to understand how your invoice might look. If you subscribe to a [Production](/billing/plans#production), [Enterprise](/billing/plans#enterprise), or [On-demand](/billing/plans#on-demand) plan, one of these scenarios may apply to you.

### Subscription charges

In the first example, the invoice table shows a subscription charge for a Production plan:

| Description | Quantity | Unit price | Amount |
| --- | --- | --- | --- |
| *FEB 1 - MAR 1, 2024* |  |  |  |
| EAS Build - Build (Android: 5 large and 5 medium builds; iOS: 5 large and 5 medium builds) | 1 | $40.00 | $40.00 |
| EAS Build - Plan credit | 1 | -$40.00 | -$40.00 |
| *MAR 1 - APR 1, 2024* |  |  |  |
| Expo Application Services - Production | 1 | $99.00 | $99.00 |
| Total (USD) |  |  | $99.00 |

In the above example:

* The first line item describes the EAS Build usage for the billing period of February 1 to March 1, 2024. It contains all the details about how many Android and iOS builds were created during this billing period and their cost.
* The second line item describes the credit limit for the Production plan for the billing period of February 1 to March 1, 2024.
* The third line item describes the subscription charge for the Production plan for the next billing period of March 1 to April 1, 2024.

Since the EAS Build usage doesn't exceed the plan's credit amount, the subscriber only has to pay the subscription amount of the Production plan.

### Overage charges

In the second example, the invoice table shows a subscription charge for a Production plan with an overage charge:

| Description | Quantity | Unit price | Amount |
| --- | --- | --- | --- |
| *FEB 1 - MAR 1, 2024* |  |  |  |
| EAS Build - Build (Android: 15 large and 10 medium builds; iOS 10 large and 15 medium builds) | 1 | $110.00 | $110.00 |
| EAS Build - Plan credit | 1 | -$99.00 | -$99.00 |
| *MAR 1 - APR 1, 2024* |  |  |  |
| Expo Application Services - Production | 1 | $99.00 | $99.00 |
| Total (USD) |  |  | $110.00 |

In the above example:

* The first line item describes the EAS Build usage for the billing period of February 1 to March 1, 2024. It contains all the details about how many Android and iOS builds were created during this billing period and their cost.
* The second line item describes the credit limit for the Production plan for the billing period of February 1 to March 1, 2024.
* The third line item describes the subscription charge for the Production plan for the next billing period of March 1 to April 1, 2024.

Since the EAS Build usage exceeds the plan's credit amount for the billing period of February 1 to March 1, 2024, the subscriber has to pay the overage charge and the subscription amount for the Production plan for the next billing period.

### On-demand charges

In the third example, the subscriber is on an On-demand plan. Any charges incurred during the billing period are listed in the invoice:

| Description | Quantity | Unit price | Amount |
| --- | --- | --- | --- |
| *FEB 1 - MAR 1, 2024* |  |  |  |
| EAS Build - Build (Android: 10 medium builds; iOS 10 medium builds) | 1 | $30.00 | $30.00 |
| Total (USD) |  |  | $30.00 |

The above table shows the total amount due based on usage only since the On-demand plan doesn't include any credits.

[Previous (Reference - Billing)

Manage plans and billing](/billing/manage)[Next (Reference - Billing)

Usage-based pricing](/billing/usage-based-pricing)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/billing/invoices-and-receipts.mdx)
* Last updated on June 16, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Receipts](/billing/invoices-and-receipts/#receipts)[Download and view an invoice](/billing/invoices-and-receipts/#download-and-view-an-invoice)[Download and view a receipt](/billing/invoices-and-receipts/#download-and-view-a-receipt)[Request a refund](/billing/invoices-and-receipts/#request-a-refund)[Read an invoice](/billing/invoices-and-receipts/#read-an-invoice)[Subscription charges](/billing/invoices-and-receipts/#subscription-charges)[Overage charges](/billing/invoices-and-receipts/#overage-charges)[On-demand charges](/billing/invoices-and-receipts/#on-demand-charges)