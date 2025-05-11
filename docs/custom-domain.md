Custom domain - Expo Documentation

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

Custom domain
=============

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas/hosting/custom-domain.mdx)

Set up a custom domain for your production deployment.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas/hosting/custom-domain.mdx)

---

By default, your production deployment on EAS Hosting will look like this: `my-app.expo.app` , where `my-app` is your chosen preview subdomain name. If you own a domain, you may assign it as a custom domain to the production deployment.

Each project can have exactly one custom domain, which is assigned to the production deployment.

> Note: Setting up a custom domain is a premium feature and isn't available on the free plan. Learn more about different plans and benefits at [EAS pricing](https://expo.dev/pricing).

Prerequisites
-------------

An EAS Hosting project with a production deployment

The custom domain will always load the production deployment. Therefore, to add a custom domain to your project, you will need a deployment that's been promoted to production first.

A domain name

You will need to own a domain name you want to use.

Assigning a custom domain
-------------------------

1. In your project's dashboard, navigate to [Hosting settings](https://expo.dev/accounts/%5BaccountName%5D/projects/%5BprojectName%5D/hosting/settings).
2. If you do not have a production deployment, you'll be prompted to assign one first.
3. Under Custom domain, enter the custom domain you'd like to set up. Both apex domains and subdomains are supported. If you own `example.com`, you can select:

   * `example.com`: apex domain
   * `anything.example.com`: a subdomain
4. Next, you'll be prompted to fill out some DNS records with your DNS provider:

   * Verification: to prove you own the domain
   * SSL: to set up SSL certificates
   * CNAME (subdomains) or A record (apex domains): to point the domain at your production deployment
5. Press the refresh button until all checks pass. Depending on your DNS provider, this step usually only takes a couple of minutes.

> If you require for the domain name switchover to be zero downtime, it's important to fill out these records one by one in the order they are presented in the table.
> That is, add the TXT record for verification, press the refresh button until the UI says verification is successful, then proceed to the next one.
> If downtime isn't important or relevant, you may add all three DNS records at once.

After assigning a custom domain to your app, the custom domain will route to your production deployment.

[Previous (EAS Hosting)

Environment variables](/eas/hosting/environment-variables)[Next (EAS Hosting)

Monitoring API routes](/eas/hosting/api-routes)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas/hosting/custom-domain.mdx)
* Last updated on January 14, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Prerequisites](/eas/hosting/custom-domain/#prerequisites)[Assigning a custom domain](/eas/hosting/custom-domain/#assigning-a-custom-domain)