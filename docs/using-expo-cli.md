Migrate from React Native CLI to Expo CLI - Expo Documentation

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

Migrate from React Native CLI to Expo CLI
=========================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/bare/using-expo-cli.mdx)

Learn how to migrate from React Native CLI (@react-native-community/cli) to Expo CLI for any React Native project.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/bare/using-expo-cli.mdx)

---

To migrate from React Native CLI (`npx @react-native-community/cli@latest init`) to Expo CLI, you'll need to install the `expo` package, which includes the Expo Modules API and Expo CLI. This guide covers the installation step, the benefits of using Expo CLI, and how to compile and run your project after migrating to Expo CLI.

It is strongly recommended to use Expo CLI when using other Expo tools. It is required for many tools, such as EAS Update, Expo Router, and expo-dev-client, and other features may not work as well without it.

Install the `expo` package
--------------------------

In most cases, executing the following command in a project directory to install the package is all you need to do:

Terminal

Copy

`-Â``npx install-expo-modules@latest`

For a detailed installation guide, see [Install Expo modules](/bare/installing-expo-modules).

Why Expo CLI instead of React Native CLI
----------------------------------------

Expo CLI commands provide several benefits over the similar commands in `@react-native-community/cli`, which includes:

* Instant access to Hermes debugger with `j` keystroke.
* The debugger ships with [React Native DevTools](/debugging/tools#debugging-with-react-native-devtools).
* [Continuous Native Generation (CNG)](/workflow/continuous-native-generation) support with [`expo prebuild`](/workflow/prebuild) for upgrades, white-labeling, easy third-party package setup, and better maintainability of the codebase (by reducing the surface area).
* Support for file-based routing with [`expo-router`](/router/introduction).
  + [Async bundling](/router/reference/async-routes) in development.
* Built-in [environment variable support](/guides/environment-variables) and .env file integration.
* View native logs directly in the terminal alongside JavaScript logs.
* Improved native build log formatting using Expo CLI's `xcpretty`-style tool built specifically for React Native apps. For example, when compiling a Pod, you can see which Node module included it.
* [First-class TypeScript support](/guides/typescript).
* Support for tsconfig.json aliases with `paths` and `baseUrl` [built-in to Metro](/guides/typescript#path-aliases-optional).
* [Web support](/guides/customizing-metro#adding-web-support-to-metro) with Metro. Fully typed for React Native Web.
* Modern [CSS support](/versions/latest/config/metro#css) with Tailwind, PostCSS, CSS Modules, SASS, and more.
* Static site generation with Expo Router and Metro web.
* Out of the box [support for monorepos](/guides/monorepos).
* Support for Expo tooling such as [`expo-dev-client`](/develop/development-builds/introduction), the [Expo Updates protocol](/technical-specs/expo-updates-1) and [EAS Update](/eas-update/introduction).
* Automated `pod install` execution when using `npx expo run:ios`.
* `npx expo install` selects compatible dependency versions for well-known packages.
* Automatic port detection when running `npx expo run:[android|ios]` and `npx expo start`. If another app is running on the default port, a different port is used.
* Android or iOS device launch selection shortcuts using `Shift` + `a` or `Shift` + `i` from the interactive prompt.
* Built-in support for serving your app over an [ngrok tunnel](/develop/development-builds/development-workflows#tunnel-urls).
* Develop on any port with any entry JavaScript file.

We recommend Expo CLI for most React Native projects that target Android, iOS, and/or web. It does not yet have built-in support for the most popular out-of-tree platforms, such as
Windows and macOS. If building for these platforms, you can utilize Expo CLI for the supported platforms and `@react-native-community/cli` for the others.

Compile and run your app
------------------------

After installing the `expo` package, you can use the following commands which are alternatives to `npx react-native run-android` and `npx react-native run-ios`:

Terminal

`# for Android`

`-Â``npx expo run:android`

  
`# for iOS`

`-Â``npx expo run:ios`

When building your project, you can choose a device or simulator by using the `--device` flag. This also applies to any iOS device that is connected to your computer.

Start the bundler independently
-------------------------------

`npx expo run:[android|ios]` automatically starts the bundler/development server. If you want to independently start the bundler with `npx expo start` command, pass the `--no-bundler` to the `npx expo run:[android|ios]` command.

Common questions
----------------

Can I use Expo CLI without installing the Expo Modules API?

Expo Modules API is also installed when you install the `expo` package with `npx install-expo-modules`. If you want to try out Expo CLI for now without installing Expo Modules API, install the `expo` package with `npm install` and then configure the react-native.config.js to exclude the package from autolinking:

react-native.config.js

Copy

```
module.exports = {
  dependencies: {
    expo: {
      platforms: {
        android: null,
        ios: null,
        macos: null,
      },
    },
  },
};

```

> Note: Without Expo API Modules installed, certain features such as `expo-dev-client` or `expo-router` are unavailable.

Can I use prebuild for out-of-tree platforms, such as macOS or Windows?

Yes! Refer to the [Customized Prebuild Example repository](https://github.com/byCedric/custom-prebuild-example) for more information.

Next steps
----------

Now, with the `expo` package installed and configured in your project, you can start using all features from Expo CLI and SDK. Here are some recommended next steps to dive deep:

[Expo CLI Reference

Learn more about the commands and flags available in Expo CLI.](/more/expo-cli)
[Adopt Prebuild

Automate your native directories using the app.json.](/guides/adopting-prebuild)
[Use Expo SDK

Try out libraries from the Expo SDK in your app.](/versions)
[Expo Router

Expo Router brings the best routing concepts from the web to native Android and iOS apps.](/router/introduction)

[Previous (Development process - Existing React Native apps)

Install Expo modules](/bare/installing-expo-modules)[Next (Development process - Existing React Native apps)

Install expo-updates](/bare/installing-updates)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/bare/using-expo-cli.mdx)
* Last updated on April 02, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Install the expo package](/bare/using-expo-cli/#install-the-expo-package)[Why Expo CLI instead of React Native CLI](/bare/using-expo-cli/#why-expo-cli-instead-of-react-native-cli)[Compile and run your app](/bare/using-expo-cli/#compile-and-run-your-app)[Start the bundler independently](/bare/using-expo-cli/#start-the-bundler-independently)[Common questions](/bare/using-expo-cli/#common-questions)[Next steps](/bare/using-expo-cli/#next-steps)