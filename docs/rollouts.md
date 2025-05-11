Rollouts - Expo Documentation

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

Rollouts
========

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/rollouts.mdx)

Learn how to incrementally deploy updates to your users by using a rollout mechanism.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/rollouts.mdx)

---

A rollout allows you to roll out a change to a portion of your users to catch bugs or other issues before releasing that change to all your users.

EAS provides per-update and branch-based rollout mechanisms depending on your use case.

Per-update rollouts
-------------------

This rollout mechanism allows you to specify a percentage of users that should receive a new update when you publish it, and then increase that percentage gradually afterwards.

### Starting a rollout

To start an update-based rollout, add the `--rollout-percentage` flag to your normal `eas update` command:

Terminal

Copy

`-Â``eas update --rollout-percentage=10`

In this example, when published, the update will only be available to 10% of your end users.

### Progressing a rollout

To edit the percentage of an update-based rollout:

Terminal

Copy

`-Â``eas update:edit`

You will be guided through the process of selecting the update to edit and asked for the new percentage.

### Ending a rollout

When ending an update-based rollout, you have two options:

* Roll out fully: To accomplish this end state, progress the rollout as detailed above and set the percentage to 100.
* Revert: To accomplish this end state, republish the previous update by using the `eas update:republish` command.

### Working with rollouts

* Only one update can be rolled out on a branch at one time.
* When a rollout is in progress, it must be ended using one of the options above before a new update (with the same runtime version) can be published. This prevents accidentally clobbering the rollout.
* To see the state of the rollout, use the `eas update:list` or `eas update:view` commands.

Branch-based rollouts
---------------------

This rollout mechanism allows you to incrementally roll out a set of updates on a new branch to a percentage of end users and leave the remaining percentage of users on the current branch.

### Starting a rollout

To start a branch-based rollout, run the following EAS CLI command:

Terminal

Copy

`-Â``eas channel:rollout`

In the terminal, an interactive guide will assist you in selecting a channel, choosing a branch for the rollout, and setting the percentage of users for the rollout. To increase or decrease the rollout amount, run the command again and choose the `Edit` option to adjust the rollout percentage.

### Ending a rollout

Two methods are available to end a rollout when you choose the `End` option in the interactive guide:

* Republish and revert: Use this option when you are confident with the state of the new branch. This will republish the latest update from the new branch to the old branch, and all users will be pointed to the old branch.
* Revert: Choose to disregard the updates on the new branch and return users to the old branch.

### Working with rollouts

* Only one branch can be rolled out on a channel at a single time.
* To see the state of the rollout, use the `eas channel:rollout` command.
* When a rollout is in progress, you can publish updates to both rolled out and current branches by running `eas update --branch [branch]`, for example.
* `eas update --channel [channel]` cannot be used when a rollout is in progress since it cannot know which branch in the rollout to associate the update with.

[Previous (EAS Update - Deployment)

Downloading updates](/eas-update/download-updates)[Next (EAS Update - Deployment)

Rollbacks](/eas-update/rollbacks)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/rollouts.mdx)
* Last updated on March 04, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Per-update rollouts](/eas-update/rollouts/#per-update-rollouts)[Starting a rollout](/eas-update/rollouts/#starting-a-rollout)[Progressing a rollout](/eas-update/rollouts/#progressing-a-rollout)[Ending a rollout](/eas-update/rollouts/#ending-a-rollout)[Working with rollouts](/eas-update/rollouts/#working-with-rollouts)[Branch-based rollouts](/eas-update/rollouts/#branch-based-rollouts)[Starting a rollout](/eas-update/rollouts/#starting-a-rollout-1)[Ending a rollout](/eas-update/rollouts/#ending-a-rollout-1)[Working with rollouts](/eas-update/rollouts/#working-with-rollouts-1)