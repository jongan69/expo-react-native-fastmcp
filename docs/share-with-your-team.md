Share a development build with your team - Expo Documentation

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

[Introduction](/develop/development-builds/introduction)[Create a build](/develop/development-builds/create-a-build)[Use a build](/develop/development-builds/use-development-builds)[Share with your team](/develop/development-builds/share-with-your-team)[Tools, workflows and extensions](/develop/development-builds/development-workflows)[Next steps](/develop/development-builds/next-steps)

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

Share a development build with your team
========================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/development-builds/share-with-your-team.mdx)

Learn how to install and share the development with your team or run it on multiple devices.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/development-builds/share-with-your-team.mdx)

---

Android and iOS both offer ways to install a build of your application directly on devices. This gives you full control of putting specific builds on devices, allowing you to iterate quickly and have multiple builds of your application available for review at the same time. You can also share it with your team or run it on multiple test devices.

Share the URL
-------------

When a development build is ready, a shareable URL is generated for your build with instructions on how to get it up and running. You can use this URL with a teammate or send it to your test device to install the build. The URL generated is unique to the build for your project.

![An example of shareable development build URL after the Android internal distribution build is ready.](/static/images/share-dev-build/shareable-url.png)
> If you register any new iOS devices after creating a development build, you'll need to create a new development build to install it on those devices. For more information, see [internal distribution](/build/internal-distribution).

### Use the Expo dashboard

You can also direct your teammate to the build page in the Expo dashboard. From there, they can download the build artifact directly on their device.

![An example of shareable development build URL from Expo dashboard.](/static/images/share-dev-build/expo-dashboard.png)

### Use EAS CLI

Your teammate can also download and install the development build using EAS CLI. They have to make sure that they are signed from the Expo account associated with the development build and then can run the following command:

Terminal

Copy

`-Â``eas build:run --profile development`

If the profile name for the development build is different from `development`, use it instead with `--profile`.

### iOS-only instructions

> If you're running iOS 16 or above and haven't yet turned on Developer Mode, you'll need to [enable it](/guides/ios-developer-mode) before you can run your build. (This doesn't apply if you're using enterprise provisioning.)

You can use `eas build:resign` to codesign an existing .ipa for iOS to a new ad hoc provisioning profile. This helps reduce time when distributing with your team. For example, if you want to add a new test device to an existing build, you can use this command to update the provisioning profile to include the device without rebuilding the entire app from scratch. For more information, see [Re-signing new credentials](/app-signing/app-credentials#re-signing-new-credentials).

Next steps
----------

[Install multiple app variants on the same device

Learn how to install multiple variants (development, preview, production) of an app on the same device side by side by converting `app.json` to `app.config.js` and additional configuration that is required to start the development server for each variant.](/build-reference/variants)
[Sharing pre-release versions of your app

Learn more about sharing pre-release versions of your app.](/guides/sharing-preview-releases)

[Previous (Develop - Development builds)

Use a build](/develop/development-builds/use-development-builds)[Next (Develop - Development builds)

Tools, workflows and extensions](/develop/development-builds/development-workflows)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/development-builds/share-with-your-team.mdx)
* Last updated on July 01, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Share the URL](/develop/development-builds/share-with-your-team/#share-the-url)[Use the Expo dashboard](/develop/development-builds/share-with-your-team/#use-the-expo-dashboard)[Use EAS CLI](/develop/development-builds/share-with-your-team/#use-eas-cli)[iOS-only instructions](/develop/development-builds/share-with-your-team/#ios-only-instructions)[Next steps](/develop/development-builds/share-with-your-team/#next-steps)