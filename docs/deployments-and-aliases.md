Assign aliases and promote to production - Expo Documentation

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

Assign aliases and promote to production
========================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas/hosting/deployments-and-aliases.mdx)

Learn about deployment URLs and how to set up aliases.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas/hosting/deployments-and-aliases.mdx)

---

Deployments
-----------

Deployments to EAS Hosting are immutable. Each deployment is accessible via a unique deployment URL consisting of the preview subdomain name and the deployment ID.

### Preview subdomain name

To activate EAS Hosting for a project, you'll need to choose a preview subdomain name. You can do this via the Hosting section of your project on the [expo.dev](http://expo.dev) website. Alternatively, you'll be prompted to choose a preview subdomain when you create your first deployment using the EAS CLI.

### Preview and production URLs

A preview subdomain name is a prefix used for the preview URL of your app. For example, if you choose `my-app` as the preview subdomain name, your preview URL would be: `https://my-app--or1170q9ix.expo.app/`, and your production URL would be: `https://my-app.expo.app/`.

### Deployment ID

Each deployment is identifiable using a unique deployment ID. This ID can be customized but will be a random string of letters and numbers by default.

Deployments are immutable. Once they are deployed, they cannot be changed and will always remain accessible and identifiable using their deployment ID.

Aliases
-------

Aliases are user-defined values used for creating custom URLs for deployments.

To make a deployment and assign it to an alias, use the `--alias` option:

Terminal

Copy

`-Â``eas deploy --alias hello`

The above command will create a deployment with both a standard URL at `https://my-app--or1170q9ix.expo.app/` and an alias at `https://my-app--hello.expo.app/`.

> Aliases are unique per project. If you choose an alias that was already in use, it will get re-assigned to the new deployment.

A single deployment can have multiple aliases. Aliases can also be assigned to an existing deployment by using the `--id` option:

Terminal

Copy

`-Â``eas deploy:alias --id=my-id`

In the above command, the `my-id` is the ID in the preview URL.

Aliases can have arbitrary names. For example, if you want to create a staging environment, you may create an alias called `staging` and assign a deployment to it.

### Production alias

If your preview subdomain name is `my-app`, your production URL will be `https://my-app.expo.app/`.

Similar to other aliases, a deployment can be promoted to production using `--prod` option:

Terminal

Copy

`-Â``eas deploy --prod`

Existing deployment can also be promoted to production using its deployment ID with the `--id` option:

Terminal

Copy

`-Â``eas deploy:alias --prod --id=deploymentId`

Terminology
-----------

In the following example, `my-app` is selected as the preview subdomain name:

* `https://my-app--or1170q9ix.expo.app/` : Preview URL, which is unique and where your deployment is available.
  + `my-app`: Preview subdomain name. Globally unique prefix tied to your project.
  + `or1170q9ix`: Deployment ID, which is unique to this deployment.
* `https://my-app--hello.expo.app/`: A deployment URL with an alias.
  + `hello`: User-defined alias.
* `https://my-app.expo.app/`: Production deployment URL.

Common questions
----------------

### Does EAS Hosting provide dedicated IP addresses?

No, EAS Hosting uses SNI (Server Name Indication), which means that IP addresses are shared and are not dedicated to a single project.

[Previous (EAS Hosting)

Get started](/eas/hosting/get-started)[Next (EAS Hosting)

Environment variables](/eas/hosting/environment-variables)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas/hosting/deployments-and-aliases.mdx)
* Last updated on May 06, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Deployments](/eas/hosting/deployments-and-aliases/#deployments)[Preview subdomain name](/eas/hosting/deployments-and-aliases/#preview-subdomain-name)[Preview and production URLs](/eas/hosting/deployments-and-aliases/#preview-and-production-urls)[Deployment ID](/eas/hosting/deployments-and-aliases/#deployment-id)[Aliases](/eas/hosting/deployments-and-aliases/#aliases)[Production alias](/eas/hosting/deployments-and-aliases/#production-alias)[Terminology](/eas/hosting/deployments-and-aliases/#terminology)[Common questions](/eas/hosting/deployments-and-aliases/#common-questions)[Does EAS Hosting provide dedicated IP addresses?](/eas/hosting/deployments-and-aliases/#does-eas-hosting-provide-dedicated-ip-addresses)