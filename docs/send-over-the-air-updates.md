Send over-the-air updates - Expo Documentation

[Docs](/)

[Blog](https://expo.dev/blog)[Changelog](https://expo.dev/changelog)[Star Us on GitHub](https://github.com/expo/expo)

Search

[Home](/)[Guides](/guides/overview)[EAS](/eas)[Reference](/versions/latest)[Learn](/tutorial/overview)

Get started

[Introduction](/get-started/introduction)[Create a project](/get-started/create-a-project)[Set up your environment](/get-started/set-up-your-environment)[Start developing](/get-started/start-developing)[Next steps](/get-started/next-steps)

Develop

[Tools for development](/develop/tools)

Navigation

User interface

Development builds

Config plugins

Debugging

[Authentication](/develop/authentication)[Unit testing](/develop/unit-testing)

Review

[Distributing apps for review](/review/overview)[Share previews with your team](/review/share-previews-with-your-team)[Open updates with Orbit](/review/with-orbit)

Deploy

[Build project for app stores](/deploy/build-project)[Submit to app stores](/deploy/submit-to-app-stores)[App stores metadata](/deploy/app-stores-metadata)[Send over-the-air updates](/deploy/send-over-the-air-updates)[Deploy web apps](/deploy/web)

Monitor

[Monitoring services](/monitoring/services)

More

[Core concepts](/core-concepts)[FAQ](/faq)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Send over-the-air updates
=========================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/deploy/send-over-the-air-updates.mdx)

Learn how to send over-the-air updates to push critical bug fixes and improvements to your users.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/deploy/send-over-the-air-updates.mdx)

---

You can send over-the-air updates containing critical bug fixes and improvements to your users.

Get started
-----------

> If you've published [previews](/review/share-previews-with-your-team) or created a [build](/deploy/build-project) before, you may have already set up updates and can skip this section.

To set up updates, run the following [EAS CLI](/develop/tools#eas-cli) command:

Terminal

Copy

`-Â``eas update:configure`

After the command completes, you'll need to make new builds before continuing to the next section.

Send an update
--------------

To send an update, run the following [EAS CLI](/develop/tools#eas-cli) command:

Terminal

Copy

`-Â``eas update --channel production`

This command will create an update and make it available to builds of your app that are configured to receive updates on the `production` channel. This channel is defined in [eas.json](/eas/json#channel).

You can verify the update works by force closing the app and reopening it two times. The update should be applied on the second launch.

Send updates automatically
--------------------------

You can automatically send updates with [EAS Workflows](/eas/workflows/get-started). First, you'll need to [configure your project](/eas/workflows/get-started#configure-your-project), add a file named .eas/workflows/send-updates.yml at the root of your project, then add the following workflow configuration:

.eas/workflows/send-updates.yml

Copy

```
name: Send updates

on:
  push:
    branches: ['main']

jobs:
  send_updates:
    name: Send updates
    type: update
    params:
      channel: production

```

The workflow above will send an over-the-air update for the `production` update channel on every commit to your project's `main` branch. You can also run this workflow manually with the following EAS CLI command:

Terminal

Copy

`-Â``eas workflow:run send-updates.yml`

Learn more about common patterns with the [workflows examples guide](/eas/workflows/examples).

Learn more
----------

You can learn how to [rollout an update](/eas-update/rollouts), [optimize assets](/eas-update/optimize-assets), and more with our [update guides](/eas-update/introduction).

[Previous (Deploy)

App stores metadata](/deploy/app-stores-metadata)[Next (Deploy)

Deploy web apps](/deploy/web)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/deploy/send-over-the-air-updates.mdx)
* Last updated on May 02, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Get started](/deploy/send-over-the-air-updates/#get-started)[Send an update](/deploy/send-over-the-air-updates/#send-an-update)[Send updates automatically](/deploy/send-over-the-air-updates/#send-updates-automatically)[Learn more](/deploy/send-over-the-air-updates/#learn-more)