Github Action for PR previews - Expo Documentation

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

[Preview updates](/eas-update/preview)[Override update configuration at runtime](/eas-update/override)[Using development builds](/eas-update/expo-dev-client)[Github PR previews](/eas-update/github-actions)

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

Github Action for PR previews
=============================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/github-actions.mdx)

Learn how to use GitHub Actions to automate publishing updates with EAS Update.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/github-actions.mdx)

---

A GitHub Action is a cloud function that runs every time an event on GitHub occurs. You can configure GitHub Actions to automate building and publishing updates when you or members of your team merge to a branch, like "production". This makes the process of deploying consistent and fast, leaving you more time to develop your app.

This guide will walk you through how to set up GitHub Actions to publish previews on pull requests.

Publish previews on pull requests
---------------------------------

Another common use case is to create a new update for every pull request. This allows you to test the changes in the pull request on a device before merging the code, and without having to start the project locally. Below are the steps to publish an update every time a pull request is opened:

1

Create a file path named .github/workflows/preview.yml at the root of your project.

2

Inside preview.yml, copy and paste the following snippet:

preview.yml

Copy

```
name: preview
on: pull_request

jobs:
  update:
    name: EAS Update
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write
    steps:
      - name: Check for EXPO_TOKEN
        run: |
          if [ -z "${{ secrets.EXPO_TOKEN }}" ]; then
            echo "You must provide an EXPO_TOKEN secret linked to this project's Expo account in this repo's secrets. Learn more: https://docs.expo.dev/eas-update/github-actions"
            exit 1
          fi

      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: 18.x
          cache: yarn

      - name: Setup EAS
        uses: expo/expo-github-action@v8
        with:
          eas-version: latest
          token: ${{ secrets.EXPO_TOKEN }}

      - name: Install dependencies
        run: yarn install

      - name: Create preview
        uses: expo/expo-github-action/preview@v8
        with:
          command: eas update --auto

```

In the above script:

* You are using the workflow event `on` to run every time a pull request is opened or updated.
* In the `update` job, the Node.js version, Expo's GitHub Action and the dependencies are set up using GitHub Action's built-in cache.
* The `eas update --auto` is run by the [preview subaction](https://github.com/expo/expo-github-action/tree/main/preview#readme). It adds a comment to the pull request with basic information about the update and a QR code to scan the update.

> Don't forget to add the `permissions` section to the job. This enables the job to add comments to the pull request.

3

You can skip this step if you have already set up `EXPO_TOKEN` in the previous section. Only one valid `EXPO_TOKEN` is required to authenticate GitHub Actions with your Expo account.

If you haven't, you need to give the script above permission to run by providing an `EXPO_TOKEN` environment variable.

* Navigate to <https://expo.dev/settings/access-tokens>.
* Click Create token to create a new personal access token.
* Copy the token generated.
* Navigate to <https://github.com/your-username/your-repo-name/settings/secrets/actions> by replacing "your-username" and "your-repo-name" with your project's info.
* Under Repository secrets, click New repository secret.
* Create a secret with the name EXPO\_TOKEN, and paste the copied access token in as the value.

Your GitHub Action should be set up now. Whenever a developer creates a pull request, this action will build an update and publish it, making it available to all reviewers with builds that have access to the EAS branch.

> Some repositories or organizations might need to explicitly enable GitHub Workflows and allow third-party Actions.

Using Bun instead of Yarn
-------------------------

To use [Bun](/guides/using-bun) as the package manager instead of Yarn, follow the steps below for both publishing updates on push and previews on pull requests:

1

Replace the `Setup Node` step in update.yml or preview.yml with the following snippet:

update.yml/preview.yml

Copy

```
- name: Setup Bun
  uses: oven-sh/setup-bun@v1
  with:
    bun-version: latest

```

2

To install dependencies using Bun, replace the Install dependencies step with the following snippet:

update.yml/preview.yml

Copy

```
- name: Install dependencies
  run: bun install

```

[Previous (EAS Update - Preview)

Using development builds](/eas-update/expo-dev-client)[Next (EAS Update - Deployment)

Deploy updates](/eas-update/deployment)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/github-actions.mdx)
* Last updated on September 20, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Publish previews on pull requests](/eas-update/github-actions/#publish-previews-on-pull-requests)[Using Bun instead of Yarn](/eas-update/github-actions/#using-bun-instead-of-yarn)