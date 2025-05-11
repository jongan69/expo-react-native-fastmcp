Use a development build - Expo Documentation

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

Use a development build
=======================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/development-builds/use-development-builds.mdx)

Learn how to use development builds for a project.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/development-builds/use-development-builds.mdx)

---

Usually, creating a new native build from scratch takes long enough that you'll be tempted to switch tasks and lose your focus. However, with the development build installed on your device or an emulator/simulator, you won't have to wait for the native build process until you [change the underlying native code](/develop/development-builds/use-development-builds#rebuild-a-development-build) that powers your app.

Add error handling
------------------

Import `expo-dev-client` at the top of the App.{js|tsx} or [app/\_layout.tsx](/router/basics/layout#root-layout) to add additional context for certain errors beyond what is provided by default in React Native. In particular, `expo-dev-client` will help detect situations related to a mismatch between your JavaScript and native code, such as when a native module is missing and you should make a new development build.

App.js

Copy

```
import 'expo-dev-client';

```

> This will only affect the application in which you make this change. If you want to load multiple projects from a single development app, you'll need to add this import statement to each project.

Start the development server
----------------------------

To start developing, run the following command to start the development server:

Terminal

Copy

`-Â``npx expo start`

To open the project inside your development client:

* Press `a` or `i` keys to open your project on an Android Emulator or an iOS Simulator.
* On a physical device, scan the QR code from your system's camera or a QR code reader to open the project on your device.

The launcher screen
-------------------

If you launch the development build from your device's Home screen, you will see your launcher screen, which looks similar to the following:

![The launcher screen of a development build](/static/images/dev-client/launcher-screen.png)

If a bundler is detected on your local network, or if you have signed in to an Expo account in both Expo CLI and your development build, you can connect to it directly from this screen. Otherwise, you can connect by scanning the QR code displayed by the Expo CLI.

Rebuild a development build
---------------------------

If you add a library to your project that contains native code APIs, for example, [`expo-secure-store`](/versions/latest/sdk/securestore), you will have to rebuild the development client. This is because the native code of the library is not included in the development client automatically when installing the library as a dependency on your project.

Debug a development build
-------------------------

When you need to, you can access the menu by pressing `Cmd â` + `d` or `Ctrl` + `d` in Expo CLI or by shaking your phone or tablet. Here you'll be able to access all of the functions of your development build, any debugging functionality you need, or switch to a different version of your app.

See [Debugging](/debugging/runtime-issues) guide for more information.

[Previous (Develop - Development builds)

Create a build](/develop/development-builds/create-a-build)[Next (Develop - Development builds)

Share with your team](/develop/development-builds/share-with-your-team)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/development-builds/use-development-builds.mdx)
* Last updated on April 03, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Add error handling](/develop/development-builds/use-development-builds/#add-error-handling)[Start the development server](/develop/development-builds/use-development-builds/#start-the-development-server)[The launcher screen](/develop/development-builds/use-development-builds/#the-launcher-screen)[Rebuild a development build](/develop/development-builds/use-development-builds/#rebuild-a-development-build)[Debug a development build](/develop/development-builds/use-development-builds/#debug-a-development-build)