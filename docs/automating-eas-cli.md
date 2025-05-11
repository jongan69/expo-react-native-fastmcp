Automating EAS CLI commands - Expo Documentation

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

Automating EAS CLI commands
===========================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas/workflows/automating-eas-cli.mdx)

Learn how to automate sequences of EAS CLI commands with EAS Workflows.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas/workflows/automating-eas-cli.mdx)

---

If you're using EAS CLI to build, submit, and update your app, you can automate sequences of commands with EAS Workflows. EAS Workflows can build, submit, and update your app, while also running other jobs like Maestro tests, unit tests, custom scripts, and more.

Below you'll find how to set up your project to use EAS Workflows, followed by common examples of EAS CLI commands and how you can run them using EAS Workflows.

Configure your project
----------------------

EAS Workflows require a GitHub repository that's linked to your EAS project to run. You can link a GitHub repo to your EAS project with the following steps:

* Navigate to your project's [GitHub settings](https://expo.dev/accounts/%5Baccount%5D/projects/%5BprojectName%5D/github).
* Follow the UI to install the GitHub app.
* Select the GitHub repository that matches the Expo project and connect it.

Creating builds
---------------

You can make a build of your project using EAS CLI with the `eas build` command. To make an iOS build with the `production` build profile, you could run the following EAS CLI command:

Terminal

Copy

`-Â``eas build --platform ios --profile production`

To write this command as a workflow, create a workflow file named .eas/workflows/build-ios-production.yml at the root of your project.

Inside build-ios-production.yml, you can use the following workflow to kick off a job that creates an iOS build with the `production` build profile.

.eas/workflows/build-ios-production.yml

Copy

```
name: iOS production build

on:
  push:
    branches: ['main']

jobs:
  build_ios:
    name: Build iOS
    type: build
    params:
      platform: ios
      profile: production

```

Once you have this workflow file, you can kick it off by pushing a commit to the `main` branch, or by running the following EAS CLI command:

Terminal

Copy

`-Â``eas workflow:run build-ios-production.yml`

You can provide parameters to make Android builds or use other build profiles. Learn more about build job parameters with the [build job documentation](/eas/workflows/syntax#build).

Submitting builds
-----------------

You can submit your app to the app stores using EAS CLI with the `eas submit` command. To submit an iOS app, you could run the following EAS CLI command:

Terminal

Copy

`-Â``eas submit --platform ios`

To write this command as a workflow, create a workflow file named .eas/workflows/submit-ios.yml at the root of your project.

Inside submit-ios.yml, you can use the following workflow to kick off a job that submits an iOS app.

.eas/workflows/submit-ios.yml

Copy

```
name: Submit iOS app

on:
  push:
    branches: ['main']

jobs:
  submit_ios:
    name: Submit iOS
    type: submit
    params:
      platform: ios

```

Once you have this workflow file, you can kick it off by pushing a commit to the `main` branch, or by running the following EAS CLI command:

Terminal

Copy

`-Â``eas workflow:run submit-ios.yml`

You can provide parameters to submit other platforms or use other submit profiles. Learn more about submit job parameters with the [submit job documentation](/eas/workflows/syntax#submit).

Publishing updates
------------------

You can update your app using EAS CLI with the `eas update` command. To update your app, you could run the following EAS CLI command:

Terminal

Copy

`-Â``eas update --auto`

To write this command as a workflow, create a workflow file named .eas/workflows/publish-update.yml at the root of your project.

Inside publish-update.yml, you can use the following workflow to kick off a job that sends and over-the-air update.

.eas/workflows/publish-update.yml

Copy

```
name: Publish update

on:
  push:
    branches: ['*']

jobs:
  update:
    name: Update
    type: update
    params:
      branch: ${{ github.ref_name || 'test'}}

```

Once you have this workflow file, you can kick it off by pushing a commit to any branch, or by running the following EAS CLI command:

Terminal

Copy

`-Â``eas workflow:run publish-update.yml`

You can provide parameters to update specific branches or channels, and configure the update's message. Learn more about update job parameters with the [update job documentation](/eas/workflows/syntax#update).

Next step
---------

Workflows are a powerful way to automate your development and release processes. Learn how to create development builds, publish preview updates, and create production builds with the workflows examples guide:

[Workflow examples

Learn how to use workflows to create development builds, publish preview updates, and create production builds.](/eas/workflows/examples)

[Previous (EAS Workflows)

Syntax for EAS Workflows](/eas/workflows/syntax)[Next (EAS Workflows - Reference)

Run E2E tests](/eas/workflows/reference/e2e-tests)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas/workflows/automating-eas-cli.mdx)
* Last updated on March 07, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Configure your project](/eas/workflows/automating-eas-cli/#configure-your-project)[Creating builds](/eas/workflows/automating-eas-cli/#creating-builds)[Submitting builds](/eas/workflows/automating-eas-cli/#submitting-builds)[Publishing updates](/eas/workflows/automating-eas-cli/#publishing-updates)[Next step](/eas/workflows/automating-eas-cli/#next-step)