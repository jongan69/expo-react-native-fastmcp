Install expo-dev-client in an existing React Native project - Expo Documentation

[Docs](/)

[Blog](https://expo.dev/blog)[Changelog](https://expo.dev/changelog)[Star Us on GitHub](https://github.com/expo/expo)

Search

[Home](/)[Guides](/guides/overview)[EAS](/eas)[Reference](/versions/latest)[Learn](/tutorial/overview)

[Overview](/guides/overview)

Development process

[Develop an app with Expo](/workflow/overview)[Configure with app config](/workflow/configuration)[Continuous Native Generation](/workflow/continuous-native-generation)[Using libraries](/workflow/using-libraries)[Privacy manifests](/guides/apple-privacy)[Permissions](/guides/permissions)[Environment variables](/guides/environment-variables)

Linking

Write native code

Compile locally

Web

Bundling

Existing React Native apps

[Overview](/bare/overview)[Install Expo modules](/bare/installing-expo-modules)[Migrate to Expo CLI](/bare/using-expo-cli)[Install expo-updates](/bare/installing-updates)[Install expo-dev-client](/bare/install-dev-builds-in-bare)[Native project upgrade helper](/bare/upgrade)

Existing native apps

Reference

Expo Router

[Introduction](/router/introduction)[Installation](/router/installation)

Router 101

Navigation patterns

Advanced

Reference

Migration

Expo Modules API

[Overview](/modules/overview)[Get started](/modules/get-started)

Tutorials

Reference

Push notifications

[Overview](/push-notifications/overview)[About notification types](/push-notifications/what-you-need-to-know)[Expo push notifications setup](/push-notifications/push-notifications-setup)[Send notifications with the Expo Push Service](/push-notifications/sending-notifications)[Handle incoming notifications](/push-notifications/receiving-notifications)

Reference

More

[Upgrade Expo SDK](/workflow/upgrading-expo-sdk-walkthrough)

Assorted

Integrations

Troubleshooting

Regulatory compliance

[Data and Privacy protection](/regulatory-compliance/data-and-privacy-protection)[GDPR compliance](/regulatory-compliance/gdpr)[HIPAA compliance](/regulatory-compliance/hipaa)[Privacy Shield](/regulatory-compliance/privacy-shield)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Install expo-dev-client in an existing React Native project
===========================================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/bare/install-dev-builds-in-bare.mdx)

Learn how to install and configure expo-dev-client in your existing React Native project.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/bare/install-dev-builds-in-bare.mdx)

---

The following guide explains how to install and configure `expo-dev-client` in an existing React Native project.

Do you need to create a new project?

If you're starting with a new project, create it using the `with-dev-client` template:

Terminal

Copy

`-Â``npx create-expo-app -e with-dev-client`

Do you use Continuous Native Generation (CNG) in your project?

To use `expo-dev-client` in a project that uses [CNG](/workflow/continuous-native-generation), see [Create a development build](/develop/development-builds/create-a-build).

Prerequisites
-------------

The `expo` package must be installed and configured. If you created your project with `npx @react-native-community/cli@latest init` and do not have any other Expo libraries installed, you will need to [install Expo modules](/bare/installing-expo-modules) before proceeding.

1

Install expo-dev-client
-----------------------

Add the `expo-dev-client` library to your package.json:

Terminal

Copy

`-Â``npx expo install expo-dev-client`

If your project has an ios directory on disk, run the following command to fully install the native code for `expo-dev-client`:

Terminal

Copy

`-Â``npx pod-install`

If your project doesn't have an ios directory, you can skip this step.

2

Configure deep links
--------------------

Expo CLI uses a deep link to launch your project, and it's also useful if you use plan to [use `expo-dev-client` for launching preview updates](/eas-update/getting-started) if you have added a custom deep link scheme to your project.

If you haven't configured a `scheme` for your app yet to support deep linking, then use `uri-scheme` library to do this for you.

Terminal

`# List your project's schemes`

`-Â``npx uri-scheme list`

  
`# Add a scheme to your project`

`-Â``npx uri-scheme add your-scheme`

For more information, see the [`uri-scheme` library](https://www.npmjs.com/package/uri-scheme).

3

Add additional optional configuration
-------------------------------------

For certain types of errors, you can obtain more helpful error messages when using `expo-dev-client`. To turn this on, import `expo-dev-client` in the project's index file. Make sure that the import statement is executed early, before your application's JS code is imported (place the import above `import App from './App'`).

```
import 'expo-dev-client';
%%placeholder-start%%... %%placeholder-end%%
import App from './App';

```

For more information, see [Error handling](/develop/development-builds/use-development-builds#add-error-handling).

4

Build and install the app
-------------------------

Create a debug build of your app using the tools of your choice. For example, you can do this [locally with Expo CLI](/guides/local-app-development) or [in the cloud with EAS Build](/develop/development-builds/create-a-build).

[Previous (Development process - Existing React Native apps)

Install expo-updates](/bare/installing-updates)[Next (Development process - Existing React Native apps)

Native project upgrade helper](/bare/upgrade)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/bare/install-dev-builds-in-bare.mdx)
* Last updated on November 06, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Prerequisites](/bare/install-dev-builds-in-bare/#prerequisites)[Install expo-dev-client](/bare/install-dev-builds-in-bare/#install-expo-dev-client)[Configure deep links](/bare/install-dev-builds-in-bare/#configure-deep-links)[Add additional optional configuration](/bare/install-dev-builds-in-bare/#add-additional-optional-configuration)[Build and install the app](/bare/install-dev-builds-in-bare/#build-and-install-the-app)