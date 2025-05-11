How to use a standalone Expo module - Expo Documentation

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

[Create a native module](/modules/native-module-tutorial)[Create a native view](/modules/native-view-tutorial)[Create a module with a config plugin](/modules/config-plugin-and-native-module-tutorial)[How to use a standalone Expo module](/modules/use-standalone-expo-module-in-your-project)[Wrap third-party native libraries](/modules/third-party-library)[Integrate in an existing library](/modules/existing-library)[Additional platform support](/modules/additional-platform-support)

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

How to use a standalone Expo module
===================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/modules/use-standalone-expo-module-in-your-project.mdx)

Learn how to use a standalone module created with create-expo-module in your project by using a monorepo or publishing the package to npm.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/modules/use-standalone-expo-module-in-your-project.mdx)

---

The recommended way to create an Expo module in an existing project is described in the [Expo Modules API: Get Started](/modules/get-started) guide. This tutorial explains two additional methods for using a module created with `create-expo-module` in an existing project:

* [Configure a monorepo](/modules/use-standalone-expo-module-in-your-project#use-a-monorepo)
* [Publish the module to npm](/modules/use-standalone-expo-module-in-your-project#publish-the-module-to-npm)

These methods are useful if you still want to keep the module separate from the application or share it with other developers.

Use a monorepo
--------------

Your project should use the following structure:

* apps: A directory to store multiple projects, including React Native apps.
* packages: A directory to keep different packages used by your apps.
* package.json: This is the root package file that contains the Yarn workspaces configuration.

> To learn how to configure your project as a monorepo, check out the [Working with monorepos](/guides/monorepos) guide.

1

### Initialize a new module

Once you have set up the basic monorepo structure, create a new module using `create-expo-module` with the flag `--no-example` to skip creating the example app:

Terminal

Copy

`-Â``npx create-expo-module packages/expo-settings --no-example`

2

### Set up workspace

Configure `autolinking` so your apps can use the new module. Add the following block to the package.json file in each app inside the apps directory:

package.json

Copy

```
"expo": {
  "autolinking": {
    "nativeModulesDir": "../../packages"
  }
}

```

3

### Run the module

Run one of your apps to ensure everything works. Then, start the TypeScript compiler in packages/expo-settings to watch for changes and rebuild the module's JavaScript:

Terminal

Copy

`-Â``cd packages/expo-settings`

`-Â``npm run build`

Open another terminal window, select an app from the apps directory, and run the `prebuild` command with the `--clean` option. Repeat these steps for each app in your monorepo to use the new module.

Terminal

Copy

`-Â``npx expo prebuild --clean`

Compile and run the app with the following command:

Terminal

Copy

`# Run the app on Android`

`-Â``npx expo run:android`

`# Run the app on iOS`

`-Â``npx expo run:ios`

You can now use the module in your app. To test it, edit the app/(tabs)/index.tsx file in your app and render the text message from the `expo-settings` module:

app/(tabs)/index.tsx

Copy

```
import React from 'react';
import { Text, View } from 'react-native';
import * as Settings from 'expo-settings';

export default function TabOneScreen() {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>{Settings.hello()}</Text>
    </View>
  );
}

```

After this configuration, the app displays the text "Hello world! ð".

Publish the module to npm
-------------------------

You can publish the module on npm and install it as a dependency in your project by following the steps below.

1

### Initialize a new module

Start by creating a new module with `create-expo-module`. Follow the prompts carefully, as you will publish this library, and choose a unique name for your npm package.

Terminal

Copy

`-Â``npx create-expo-module expo-settings`

2

### Run the example project

Run one of your apps to ensure everything works. Then, start the TypeScript compiler in the root of your project to watch for changes and rebuild the module's JavaScript:

Terminal

Copy

`# Run this in the root of the project to start the TypeScript compiler`

`-Â``npm run build`

Open another terminal window, compile and run the example app:

Terminal

Copy

`-Â``cd example`

`# Run the example app on Android`

`-Â``npx expo run:android`

`# Run the example app on iOS`

`-Â``npx expo run:ios`

3

### Publish the package to npm

To publish your package to npm, you need an npm account. If you don't have one, create an account on [the npm website](https://www.npmjs.com/signup). After creating an account, log in by running the following command:

Terminal

Copy

`-Â``npm login`

Navigate to the root of your module, then run the following command to publish it:

Terminal

Copy

`-Â``npm publish`

Your module will now be published to npm and can be installed in other projects using `npm install`.

Apart from publishing your module to npm, you can use it in your project in the following ways:

* Create a tarball: Use `npm pack` to create a tarball of your module, then install it in your project by running `npm install /path/to/tarball`. This method is helpful for testing your module locally before publishing it or sharing it with others who don't have access to the npm registry.
* Run a local npm registry: Use a tool such as [Verdaccio](https://verdaccio.org/) to host a local npm registry. You can install your module from this registry, which is useful for managing internal packages within a company or organization.
* Publish a private package: [Use a private registry with EAS Build](/build-reference/private-npm-packages) to manage private modules securely.

4

### Test the published module

To test the published module in a new project, create a new app and install the module as a dependency by running the following command:

Terminal

Copy

`-Â``npx create-expo-app my-app`

`-Â``cd my-app`

`-Â``npx expo install expo-settings`

You can now use the module in your app! To test it, edit app/(tabs)/index.tsx and render the text message from expo-settings.

app/(tabs)/index.tsx

Copy

```
import React from 'react';
import * as Settings from 'expo-settings';
import { Text, View } from 'react-native';

export default function TabOneScreen() {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>{Settings.hello()}</Text>
    </View>
  );
}

```

Finally, prebuild your project and run the app by executing the following commands:

Terminal

Copy

`# Re-generate the native project directories from scratch`

`-Â``npx expo prebuild --clean`

`# Run the example app on Android`

`-Â``npx expo run:android`

`# Run the example app on iOS`

`-Â``npx expo run:ios`

After this configuration, you see the text "Hello world! ð" displayed in the app.

Next steps
----------

[Wrap third-party native libraries

Learn how to wrap third-party native libraries in an Expo module.](/modules/third-party-library)
[Tutorial: Creating a native module

A tutorial on creating a native module that persists settings with Expo Modules API.](/modules/native-module-tutorial)

[Previous (Expo Modules API - Tutorials)

Create a module with a config plugin](/modules/config-plugin-and-native-module-tutorial)[Next (Expo Modules API - Tutorials)

Wrap third-party native libraries](/modules/third-party-library)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/modules/use-standalone-expo-module-in-your-project.mdx)
* Last updated on December 04, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Use a monorepo](/modules/use-standalone-expo-module-in-your-project/#use-a-monorepo)[Initialize a new module](/modules/use-standalone-expo-module-in-your-project/#initialize-a-new-module)[Set up workspace](/modules/use-standalone-expo-module-in-your-project/#set-up-workspace)[Run the module](/modules/use-standalone-expo-module-in-your-project/#run-the-module)[Publish the module to npm](/modules/use-standalone-expo-module-in-your-project/#publish-the-module-to-npm)[Initialize a new module](/modules/use-standalone-expo-module-in-your-project/#initialize-a-new-module-1)[Run the example project](/modules/use-standalone-expo-module-in-your-project/#run-the-example-project)[Publish the package to npm](/modules/use-standalone-expo-module-in-your-project/#publish-the-package-to-npm)[Test the published module](/modules/use-standalone-expo-module-in-your-project/#test-the-published-module)[Next steps](/modules/use-standalone-expo-module-in-your-project/#next-steps)