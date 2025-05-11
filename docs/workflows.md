Deploy with Workflows - Expo Documentation

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

Deploy with Workflows
=====================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas/hosting/workflows.mdx)

Learn how to automate React Native CI/CD for web deployments with EAS Hosting and Workflows.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas/hosting/workflows.mdx)

---

EAS Workflows is a great way to automate the React Native CI/CD pipeline for web deployment of your project to EAS Hosting with pull request (PR) previews and production deployments.

Setup workflows
---------------

To use [EAS workflows](/eas/workflows/get-started) to automatically deploy your project, follow the instructions in [Get started with EAS workflows](/eas/workflows/get-started) and add the [GitHub integration](/eas/workflows/get-started#configure-your-project) for your project.

Create a deployment workflow
----------------------------

Add the following file to .eas/workflows/deploy.yml. This will use the production environment variables, export the web bundle, deploy your project and promote it to production whenever you push to the `main` branch.

.eas/workflows/deploy.yml

Copy

```
name: Deploy

on:
  push:
    branches: ['main']

jobs:
  deploy:
    type: deploy
    name: Deploy
    environment: production
    params:
      prod: true

```

Now, whenever a commit is pushed to `main` or a PR is merged, the workflow will run to deploy your website.

You can also test this workflow by triggering it manually:

Terminal

Copy

`-Â``eas workflow:run .eas/workflows/deploy.yml`

[Previous (EAS Hosting)

Monitoring API routes](/eas/hosting/api-routes)[Next (EAS Hosting - Reference)

Caching](/eas/hosting/reference/caching)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas/hosting/workflows.mdx)
* Last updated on April 29, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Setup workflows](/eas/hosting/workflows/#setup-workflows)[Create a deployment workflow](/eas/hosting/workflows/#create-a-deployment-workflow)