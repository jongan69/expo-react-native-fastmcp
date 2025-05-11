Continuous deployment - Expo Documentation

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

[Deploy updates](/eas-update/deployment)[Downloading updates](/eas-update/download-updates)[Rollouts](/eas-update/rollouts)[Rollbacks](/eas-update/rollbacks)[Optimize assets](/eas-update/optimize-assets)[Continuous deployment](/eas-update/continuous-deployment)[Alternative deployment patterns](/eas-update/deployment-patterns)

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

Continuous deployment
=====================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/continuous-deployment.mdx)

Learn how to use the fingerprint runtime version and GitHub actions for continuous deployment.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/continuous-deployment.mdx)

---

Prerequisites
-------------

* You need to have a GitHub account and use it to host your git project.
* You need to have an Expo token configured in your GitHub repository.

How to configure the `EXPO_TOKEN` environment variable on your GitHub repository

* Navigate to [expo.dev/settings/access-tokens](https://expo.dev/settings/access-tokens) and then:
* Click Create token to create a new personal access token.
* Copy the generated token.
* Navigate to <https://github.com/your-username/your-repo-name/settings/secrets/actions> by replacing "your-username" and "your-repo-name" with your project's info.
* Under Repository secrets, click New repository secret.
* Create a secret with the name EXPO\_TOKEN, and paste the copied access token in as the value.

GitHub Action: continuous-deploy-fingerprint
--------------------------------------------

> Available for SDK 52 and above.

Expo provides the [continuous-deploy-fingerprint](https://github.com/expo/expo-github-action/tree/main/continuous-deploy-fingerprint) GitHub Action to continuously deploy React Native projects that use the [`fingerprint` runtime version policy](/versions/latest/sdk/updates#fingerprint). It deploys every JS change as an EAS Update to all compatible builds over-the-air, and new builds are automatically created using EAS Build when a runtime change is detected.

How do I debug the commands that are run in the action?

Running your GitHub workflows in debug mode will automatically add the `--debug` flag to the commands run as part of the action, and the output will be available in the workflow run logs.

### Fingerprint runtime versioning

The [`fingerprint` runtime version policy](/versions/latest/sdk/updates#fingerprint) uses the [`@expo/fingerprint`](/versions/latest/sdk/fingerprint) package to generate a hash of your project when making a build or publishing an update, and then uses that hash as the runtime version. The hash is calculated based on dependencies, custom native code, native project files, and configuration, amongst other things.

By automatically calculating the runtime version, you don't have to be concerned about native layer compatibility with the JavaScript application when deploying updates to builds.

How does fingerprint generation differ between managed and bare workflows?

The default project files included in the fingerprint hash differs between managed and bare workflow projects. EAS automatically detects your workflow by checking if the android and ios and directories are gitignored. If they are, EAS will treat the project as a managed workflow project, thus dictating that a hash of the `package.json` dependencies are sufficient to determine fingerprint compatibility.

How do I debug fingerprint mismatches between my local machine and CI/CD?

If you notice different fingerprints being generated across different machines or environments, it may mean that unanticipated files are being included in the hash calculation. `@expo/fingerprint` has a predetermined set of files to include/exclude for hash calculation, but often your project setup may require additional excludes. For projects that include native directories (android and ios) this is more common.

We provide tools for identifying which files are causing fingerprint inconsistencies and mechanisms to exclude those files from fingerprint calculations for your project.

To identify differences in fingerprints on different machines or environments:

* When running fingerprint generation commands on each machine/environment (`npx expo-updates fingerprint:generate`), pass `--debug` flag.
* Diff outputs from those command runs to determine files causing the difference. These tools may be helpful:
  + [JSON Pretty Print](https://jsonformatter.org/json-pretty-print) to format the output.
  + [JSON Diff](https://www.jsondiff.com/) to compare the output and identify the files causing the discrepancies.

To exclude files causing the differences, add them to the .fingerprintignore file as described in the documentation for [`@expo/fingerprint`](/versions/latest/sdk/fingerprint).

### App version numbers

When using continuous deployment, version number incrementation must be done automatically. While the specifics will differ based on the preferred numbering scheme, the general strategy is:

1. Before continuous deployment CI steps, check if a new release will be created (due to a new fingerprint).
2. If so, bump the version number in the source code and push the version bump commit.
3. Continue continuous deployment CI steps with the new commit.

An example is provided in the [`continuous-deploy-fingerprint` GitHub Action documentation](https://github.com/expo/expo-github-action/tree/main/continuous-deploy-fingerprint#continuous-deployment-on-main-advanced).

GitHub Action: expo-github-action
---------------------------------

An alternative GitHub action is [expo-github-action](https://github.com/expo/expo-github-action/tree/main) that can be used to publish updates on push and previews on pull requests. `continuous-deploy-fingerprint` uses fingerprints to determine if a build is needed or not to deploy an update, while `expo-github-action` will only publish updates.

* To learn about publishing updates when code is pushed to the main branch, refer to the [README](https://github.com/expo/expo-github-action/tree/main?tab=readme-ov-file#create-new-eas-update-on-push-to-main).
* To learn about Pull Request previews with `expo-github-action`, refer to the [GitHub PR Previews guide](/eas-update/github-actions).

[Previous (EAS Update - Deployment)

Optimize assets](/eas-update/optimize-assets)[Next (EAS Update - Deployment)

Alternative deployment patterns](/eas-update/deployment-patterns)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/continuous-deployment.mdx)
* Last updated on February 04, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Prerequisites](/eas-update/continuous-deployment/#prerequisites)[GitHub Action: continuous-deploy-fingerprint](/eas-update/continuous-deployment/#github-action-continuous-deploy-fingerprint)[Fingerprint runtime versioning](/eas-update/continuous-deployment/#fingerprint-runtime-versioning)[App version numbers](/eas-update/continuous-deployment/#app-version-numbers)[GitHub Action: expo-github-action](/eas-update/continuous-deployment/#github-action-expo-github-action)