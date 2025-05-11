Manage plans and billing - Expo Documentation

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

Manage plans and billing
========================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/billing/manage.mdx)

Learn how to update, downgrade, or cancel your Expo account's plans and manage billing details.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/billing/manage.mdx)

---

Billing in the Expo dashboard provides information about your account's currently subscribed plan and monthly usage. It also allows you to manage your plan and billing details.

This guide explains how to manage your account's plans and billing information.

Manage plans
------------

### View the current plan

For Organization accounts

For Personal accounts

* Click [Billing](https://expo.dev/settings/billing) from the navigation menu under Organization settings.
* Under Plan, you can see the current plan for your account.

For example, an Organization account is subscribed to the Production plan below:

![Billing page in Expo dashboard displays the current plan for an Organization account.](/static/images/billing/management/billing-01.png)

* Click [Billing](https://expo.dev/settings/billing) from the navigation menu under Account settings.
* Under Plan, you can see the current plan for your account.

For example, a Personal account is subscribed to the Production plan below:

![Billing page in Expo dashboard displays the current plan for a Personal account.](/static/images/billing/management/billing-02.png)

### Upgrade to a new plan

To upgrade to a different plan:

* Click [Billing](https://expo.dev/settings/billing) from the navigation menu in Expo dashboard.
* Under Plan, click Change Plan if you are already on a paid plan. If you are on the Free plan, click Subscribe. It opens the Cart page.
* Under Choose a plan, you can see a list of all available plans. Choose the plan you want to upgrade to and click the Continue to Review button at the bottom of this page.

![Billing page in Expo dashboard displays the list of available plans to upgrade.](/static/images/billing/management/billing-03.png)

* Next, you are asked to review and confirm your new plan. After reviewing the details on this page, enable the checkbox and click Continue to Checkout to open the checkout page.

![Billing page in Expo dashboard displays the review page for the selected plan to upgrade.](/static/images/billing/management/billing-04.png)

* On Checkout, you are asked to enter your email, card details, and billing address. After adding these details, click Pay Now to subscribe to the new plan.

> Note: If you are subscribing to the [On-demand plan](/billing/plans#on-demand), you are not charged any fee when you check out. Since this is a usage-based plan, all charges are due at the end of the billing period.

### Downgrade a plan

If you are on a Production, Enterprise, or Legacy plan, you can downgrade to the On-demand or Free plan.

To On-demand plan

To Free plan

Downgrading to the On-demand plan takes effect after your current billing period ends.

To downgrade, go to [Billing](https://expo.dev/settings/billing) and follow the steps below:

* Under Plan, click Change Plan.

![Billing page in Expo dashboard displays the Change Plan button to downgrade a plan.](/static/images/billing/management/billing-05.png)

* Under Choose a plan, select On-demand plan. Then, click Continue to Review at the bottom of the page.

![On Cart, select On-demand plan under Choose a plan and Continue to Review at the bottom of the page in Expo dashboard.](/static/images/billing/management/billing-06.png)

* Next, you need to review and confirm that you're switching to the On-demand plan. Verify that the account you're downgrading from is correct (see the *warning* on this page). After reviewing the details, enable the checkbox and click Continue to Checkout.

![Billing page in Expo dashboard displays the review page for the selected plan to downgrade.](/static/images/billing/management/billing-07.png)

* A Checkout dialog opens up where you can confirm all the details. Click Schedule Downgrade to schedule a downgrade of your plan.

![Billing page in Expo dashboard displays the review page for the selected plan to downgrade.](/static/images/billing/management/billing-08.png)

* After confirming your account for a plan downgrade to On-demand, the same information is also reflected under Billing > Plan.

![Billing page in Expo dashboard displays the review page for the selected plan to downgrade.](/static/images/billing/management/billing-09.png)

Downgrading to the Free plan takes effect after your current billing period ends and is equivalent to canceling a paid plan.

To downgrade, go to [Billing](https://expo.dev/settings/billing) and follow the steps below:

* Under Plan, click Change Plan.

![Billing page in Expo dashboard displays the Change Plan button to downgrade a plan.](/static/images/billing/management/billing-05.png)

* Under Choose a plan, select Free plan. Then, click Continue to Review at the bottom of the page.

![On Cart, select Free plan under Choose a plan and Continue to Review at the bottom of the page in the Expo dashboard.](/static/images/billing/management/billing-10.png)

* Next, you need to review and confirm that you're switching to the Free plan. Verify that the account you're downgrading is correct (see the *warning* on this page). After reviewing the details, enable the checkbox and click Cancel Paid Plan.

![Billing page in Expo dashboard displays the review page for the selected plan to downgrade.](/static/images/billing/management/billing-11.png)

* You will be redirected to Stripe's cancel plan screen, where you can cancel your plan. Switching to the Free plan is equivalent to canceling a paid plan at the end of the billing period.

### Cancel a plan

From Production or Enterprise plan

From On-demand to Free plan

Cancellation from a Production or Enterprise plan takes effect after your current billing period ends.

To cancel your plan, on [Billing](https://expo.dev/settings/billing), click Cancel Plan and then click Continue to Stripe to follow the process of your current plan's cancellation.

![Billing page in Expo dashboard displays the Cancel Plan button to cancel a plan.](/static/images/billing/management/billing-12.png)

Cancellation for the On-demand plan takes effect immediately and resets your account's quota to the Free plan.

To cancel your plan, on [Billing](https://expo.dev/settings/billing), click Cancel Plan and then click Cancel Immediately.

![Billing page in Expo dashboard displays the Cancel Plan button to cancel a plan.](/static/images/billing/management/billing-12.png)
> Note: If you unsubscribe from an On-demand plan, you will be charged for any usage incurred during the current billing period.

Manage billing information
--------------------------

You can manage your billing-related details such as name, email, address, and payment information, or add a tax ID. All of this information is mentioned on the [monthly invoice](/billing/invoices-and-receipts) you receive for the subscribed plan.

### Update Billing name, email, or address

To update your billing name, email, or address:

* On [Billing](https://expo.dev/settings/billing), click Update billing information. This will open Stripe's portal where you can view payment methods, billing information, invoicing history, and update your billing information. Then, click Update information.

![Billing page in Expo dashboard displays the Update billing information button to update billing details.](/static/images/billing/management/billing-13.png)

* Update your billing details by entering your new name, email or address, then click Save.

![On Billing information, enter the new name, email, or address and click Save to update the billing details.](/static/images/billing/management/billing-14.png)

### Tax ID

To add or update your billing tax ID:

* On [Billing](https://expo.dev/settings/billing), click Update billing information. This will open Stripe's portal where you can view and update your billing information. Then, click Update information.

![Billing page in Expo dashboard displays the Update billing information button to update billing details.](/static/images/billing/management/billing-13.png)

* Under Tax ID, select the ID type, enter your valid tax ID, and click Save.

![On Billing information, enter the new tax ID and click Save to update the billing detail.](/static/images/billing/management/billing-15.png)

### Payment method

To add a new payment method information:

* On [Billing](https://expo.dev/settings/billing), click Update billing information. This will open Stripe's portal where you can view and update your billing information.
* Under Payment method, click on Add payment method to add a new payment method.

![On Billing information, you can add a new payment method.](/static/images/billing/management/payment-01.png)

* Enter your new payment method details and click Add.

![On add a new payment method, enter the new payment method details.](/static/images/billing/management/payment-02.png)

[Previous (Reference - Billing)

Subscriptions, plans, and add-ons](/billing/plans)[Next (Reference - Billing)

Payment history, invoices, and receipts](/billing/invoices-and-receipts)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/billing/manage.mdx)
* Last updated on July 01, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Manage plans](/billing/manage/#manage-plans)[View the current plan](/billing/manage/#view-the-current-plan)[Upgrade to a new plan](/billing/manage/#upgrade-to-a-new-plan)[Downgrade a plan](/billing/manage/#downgrade-a-plan)[Cancel a plan](/billing/manage/#cancel-a-plan)[Manage billing information](/billing/manage/#manage-billing-information)[Update Billing name, email, or address](/billing/manage/#update-billing-name-email-or-address)[Tax ID](/billing/manage/#tax-id)[Payment method](/billing/manage/#payment-method)