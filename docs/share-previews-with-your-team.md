Share previews with your team - Expo Documentation

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

Share previews with your team
=============================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/review/share-previews-with-your-team.mdx)

Share previews of your app with your team by publishing updates on branches.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/review/share-previews-with-your-team.mdx)

---

Once you've made changes on a branch, you can share them with your team by publishing an update. This allows you to get feedback on your changes during review.

The following steps will outline a basic flow for publishing a preview of your changes, and then sharing it with your team. For a more comprehensive resource, see the [Preview updates](/eas-update/preview) guide.

Publish a preview of your changes
---------------------------------

You can publish a preview of your current changes by running the following [EAS CLI](/develop/tools#eas-cli) command:

Terminal

Copy

`-Â``eas update --auto`

This command will publish an update under the current branch name.

Share with your team
--------------------

Once the preview is published, you'll see output like this in the terminal window:

Terminal

`â Published!`  
`...``EAS Dashboard https://expo.dev/accounts/your-account/projects/your-project/updates/708b05d8-9bcf-4212-a052-ce40583b04fd`

Share the EAS dashboard link with a reviewer. After opening the link, they can click on the Preview button. They will see a QR code that they can scan to open the preview on their device.

![Preview update QR code UI on expo.dev.](/static/images/eas-update/preview-updates-qr-code.png)

Create previews automatically
-----------------------------

You can automatically create previews on every commit with [EAS Workflows](/eas/workflows/get-started). First, you'll need to [configure your project](/eas/workflows/get-started#configure-your-project), add a file named .eas/workflows/publish-preview-update.yml at the root of your project, then add the following workflow configuration:

.eas/workflows/publish-preview-update.yml

Copy

```
name: Publish preview update

on:
  push:
    branches: ['*']

jobs:
  publish_preview_update:
    name: Publish preview update
    type: update
    params:
      branch: ${{ github.ref_name || 'test' }}

```

The workflow above will publish an update on every commit to every branch. You can also run this workflow manually with the following EAS CLI command:

Terminal

Copy

`-Â``eas workflow:run publish-preview-update.yml`

Learn more about common patterns with the [workflows examples guide](/eas/workflows/examples).

Learn more
----------

[Preview updates

Learn how to preview updates in development, preview, and production builds.](/eas-update/preview)

[Previous (Review)

Distributing apps for review](/review/overview)[Next (Review)

Open updates with Orbit](/review/with-orbit)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/review/share-previews-with-your-team.mdx)
* Last updated on May 02, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Publish a preview of your changes](/review/share-previews-with-your-team/#publish-a-preview-of-your-changes)[Share with your team](/review/share-previews-with-your-team/#share-with-your-team)[Create previews automatically](/review/share-previews-with-your-team/#create-previews-automatically)[Learn more](/review/share-previews-with-your-team/#learn-more)