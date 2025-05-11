Manage branches and channels with EAS CLI - Expo Documentation

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

[How it works](/eas-update/how-it-works)[Manage branches and channels](/eas-update/eas-cli)[Runtime versions](/eas-update/runtime-versions)

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

Manage branches and channels with EAS CLI
=========================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/eas-cli.mdx)

Learn how to link a branch to a channel and publish updates with EAS CLI.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/eas-cli.mdx)

---

EAS Update works by linking *branches* to *channels*. Channels are specified at build time and exist inside a build's native code. Branches are an ordered list of updates, similar to a Git branch, which is an ordered list of commits. With EAS Update, we can link any channel to any branch, allowing us to make different updates available to different builds.

![Channel "production" linked to branch "version-1.0"](/static/images/eas-update/channel-branch-link.png)

The diagram above visualizes this link. Here, we have the builds with the "production" channel linked to the branch named "version-1.0". When we're ready, we can adjust the channelâbranch pointer. Imagine we have more fixes tested and ready on a branch named "version-2.0". We could update this link to make the "version-2.0" branch available to all builds with the "production" channel.

![Channel "production" linked to branch "version-2.0"](/static/images/eas-update/channel-branch-link-2.png)

Inspecting the state of your project's updates
----------------------------------------------

### Inspect channels

View all channels:

Terminal

Copy

`-Â``eas channel:list`

View a specific channel:

Terminal

Copy

`-Â``eas channel:view [channel-name]`

  
`# Example`

`-Â``eas channel:view production`

Create a channel:

Terminal

Copy

`-Â``eas channel:create [channel-name]`

  
`# Example`

`-Â``eas channel:create production`

### Inspect branches

See all branches:

Terminal

Copy

`-Â``eas branch:list`

See a specific branch and a list of its updates:

Terminal

Copy

`-Â``eas branch:view [branch-name]`

  
  
`# Example`

`-Â``eas branch:view version-1.0`

### Inspect updates

View a specific update:

Terminal

Copy

`-Â``eas update:view [update-group-id]`

  
`# Example`

`-Â``eas update:view dbfd479f-d981-44ce-8774-f2fbcc386aa`

Changing the state of your project's updates
--------------------------------------------

### Create a new update and publish it

Terminal

Copy

`-Â``eas update --branch [branch-name] --message "..."`

  
`# Example`

`-Â``eas update --branch version-1.0 --message "Fixes typo"`

If you're using Git, we can use the `--auto` flag to auto-fill the branch name and the message. This flag will use the current Git branch as the branch name and the latest Git commit message as the message.

Terminal

Copy

`-Â``eas update --auto`

### Delete a branch

Terminal

Copy

`-Â``eas branch:delete [branch-name]`

  
`# Example`

`-Â``eas branch:delete version-1.0`

### Rename a branch

Renaming branches do not disconnect any channelâbranch links. If you had a channel named "production" linked to a branch named "version-1.0", and then you renamed the branch named "version-1.0" to "version-1.0-new", the "production" channel would be linked to the now-renamed branch "version-1.0-new".

Terminal

Copy

`-Â``eas branch:rename --from [branch-name] --to [branch-name]`

  
`# Example`

`-Â``eas branch:rename --from version-1.0 --to version-1.0-new`

### Republish a previous update within a branch

We can make a previous update immediately available to all users. This command takes the previous update and publishes it again so that it becomes the most current update on the branch. As your users re-open their apps, the apps will see the newly re-published update and will download it.

> Republish is similar to a Git reversion, where the correct commit is placed on top of the Git history.

Terminal

`-Â``eas update:republish --group [update-group-id]`

`-Â``eas update:republish --branch [branch-name]`

  
`# Example`

`-Â``eas update:republish --group dbfd479f-d981-44ce-8774-f2fbcc386aa`

`-Â``eas update:republish --branch version-1.0`

> If you don't know the exact update group ID, you can use the `--branch` flag. This shows a list of the recent updates on the branch and allows you to select the update group to republish.

[Previous (EAS Update - Concepts)

How it works](/eas-update/how-it-works)[Next (EAS Update - Concepts)

Runtime versions](/eas-update/runtime-versions)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/eas-cli.mdx)
* Last updated on June 16, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Inspecting the state of your project's updates](/eas-update/eas-cli/#inspecting-the-state-of-your-projects-updates)[Inspect channels](/eas-update/eas-cli/#inspect-channels)[Inspect branches](/eas-update/eas-cli/#inspect-branches)[Inspect updates](/eas-update/eas-cli/#inspect-updates)[Changing the state of your project's updates](/eas-update/eas-cli/#changing-the-state-of-your-projects-updates)[Create a new update and publish it](/eas-update/eas-cli/#create-a-new-update-and-publish-it)[Delete a branch](/eas-update/eas-cli/#delete-a-branch)[Rename a branch](/eas-update/eas-cli/#rename-a-branch)[Republish a previous update within a branch](/eas-update/eas-cli/#republish-a-previous-update-within-a-branch)