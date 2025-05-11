How to launch an update using Expo Orbit - Expo Documentation

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

How to launch an update using Expo Orbit
========================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/review/with-orbit.mdx)

Learn how to open updates with Expo Orbit as part of a review workflow.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/review/with-orbit.mdx)

---

[Expo Orbit](https://expo.dev/orbit) is a macOS and Windows app designed to speed up installing and running builds from EAS. It makes running your builds and updates as easy as pressing Open in Orbit.

How does automatic installation and launching of updates work?

When you launch an update, Orbit will look for the latest development build that matches the runtime version and target platform of the update. If a compatible build is found, the update will install automatically on the target device and launch with a deep link that points to the update.

If you don't have any development builds available, either because they have all expired, you haven't created one, you don't use EAS Build, or you are [building your app locally](/guides/local-app-development), then Orbit will prompt you on how to proceed. Click Launch with deep link in the prompt to open the update if you already have a compatible development build installed on your target device.

Prerequisites
-------------

* Install the Orbit app before following the steps in this guide. You can download it directly from [GitHub releases](https://github.com/expo/orbit/releases) or see the [alternative method](/build/orbit#installation) to install it.
* After installing the app, sign in to your Expo account from Settings.

Preview an update with Expo Orbit
---------------------------------

Expo Orbit launching an update directly from Expo dashboard to an iOS Simulator.

Previewing with Expo Orbit requires you to have an update published. If you haven't published an update, see [Publish an update](/eas-update/getting-started#publish-an-update) before following the steps in the next section.

### Install and launch the update

> Note: Launching updates using Expo Orbit is not supported on physical iOS devices. It is supported on Android devices/emulators or iOS Simulators.

After the update is published, follow these steps to open it on an Android Emulator or iOS Simulator:

* Navigate your project's Updates tab.
* Select the update you want to preview.
* Click Preview. This will open the Preview dialog.
* Under Open with Orbit, select a platform to launch the update.
* Orbit will install and launch the update on the selected Android Emulator or iOS Simulator.

You can now seamlessly launch and review updates using Expo Orbit.

[Previous (Review)

Share previews with your team](/review/share-previews-with-your-team)[Next (Deploy)

Build project for app stores](/deploy/build-project)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/review/with-orbit.mdx)
* Last updated on September 26, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Prerequisites](/review/with-orbit/#prerequisites)[Preview an update with Expo Orbit](/review/with-orbit/#preview-an-update-with-expo-orbit)[Install and launch the update](/review/with-orbit/#install-and-launch-the-update)