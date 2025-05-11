Install Expo Router - Expo Documentation

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

Install Expo Router
===================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/installation.mdx)

Learn how to quickly get started by creating a new project with Expo Router or adding the library to an existing project.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/installation.mdx)

---

Find the steps below to create a new project with Expo Router library or add it to your existing project.

Quick start
-----------

1

We recommend creating a new Expo app using `create-expo-app` to create a project with Expo Router library already installed and configured:

Terminal

Copy

`-Â``npx create-expo-app@latest`

2

Now, you can start your project by running:

Terminal

Copy

`-Â``npx expo start`

* To view your app on a mobile device, we recommend starting with [Expo Go](/get-started/set-up-your-environment#how-would-you-like-to-develop). As your application grows in complexity and you need more control, you can create a [development build](/develop/development-builds/introduction).
* Open the project in a web browser by pressing `w` in the Terminal UI. Press `a` for Android (Android Studio is required), or `i` for iOS (macOS with Xcode is required).

Manual installation
-------------------

Follow the steps below if you have a project that was previously created with Expo but does not have Expo Router library installed.

### Prerequisites

Make sure your computer is [set up for running an Expo app](/get-started/create-a-project).

1

### Install dependencies

You'll need to install the following dependencies:

Terminal

Copy

`-Â``npx expo install expo-router react-native-safe-area-context react-native-screens expo-linking expo-constants expo-status-bar`

The above command will install versions of these libraries that are compatible with the Expo SDK version your project is using.

2

### Setup entry point

For the property `main`, use the `expo-router/entry` as its value in the package.json. The initial client file is [app/\_layout.tsx](/router/basics/layout#root-layout).

package.json

Copy

```
{
  "main": "expo-router/entry"
}

```

Custom entry point to initialize and load side-effects

You can create a custom entry point in your Expo Router project to initialize and load side-effects before your app loads the root layout (app/\_layout.tsx). Below are some of the common cases for a custom entry point:

* Initializing global services like analytics, error reporting, and so on.
* Setting up polyfills
* Ignoring specific logs using `LogBox` from `react-native`

1. Create a new file in the root of your project, such as index.js. After creating this file, the project structure should look like this:

   `app`

   â`_layout.tsx`

   `index.js`

   `package.json`

   `Other project files`
2. Import or add your custom configuration to the file. Then, import `expo-router/entry` to register the app entry. Remember to always import it last to ensure all configurations are properly set up before the app renders.

   index.js

   Copy

   ```
   // Import side effects first and services

   // Initialize services

   // Register app entry through Expo Router
   import 'expo-router/entry';

   ```
3. Update the `main` property in package.json to point to the new entry file.

   package.json

   Copy

   ```
   {
     "main": "index.js"
   }

   ```

3

### Modify project configuration

Add a deep linking `scheme` in your [app config](/workflow/configuration):

app.json

Copy

```
{
  "scheme": "your-app-scheme"
}

```

If you are developing your app for web, install the following dependencies:

Terminal

Copy

`-Â``npx expo install react-native-web react-dom`

Then, enable [Metro web](/guides/customizing-metro#adding-web-support-to-metro) support by adding the following to your [app config](/workflow/configuration):

app.json

Copy

```
{
  "web": {
    "bundler": "metro"
  }
}

```

4

### Modify babel.config.js

Ensure you use `babel-preset-expo` as the `preset`, in the babel.config.js file or delete the file:

babel.config.js

Copy

```
module.exports = function (api) {
  api.cache(true);
  return {
    presets: ['babel-preset-expo'],
  };
};

```

5

### Clear bundler cache

After updating the Babel config file, run the following command to clear the bundler cache:

Terminal

Copy

`-Â``npx expo start --clear`

6

### Update resolutions

If you're upgrading from an older version of Expo Router, ensure you remove all outdated Yarn resolutions or npm overrides in your package.json. Specifically, remove `metro`, `metro-resolver`, `react-refresh` resolutions from your package.json.

[Previous (Expo Router)

Introduction](/router/introduction)[Next (Expo Router - Router 101)

Core concepts](/router/basics/core-concepts)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/installation.mdx)
* Last updated on May 01, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Quick start](/router/installation/#quick-start)[Manual installation](/router/installation/#manual-installation)[Prerequisites](/router/installation/#prerequisites)[Install dependencies](/router/installation/#install-dependencies)[Setup entry point](/router/installation/#setup-entry-point)[Modify project configuration](/router/installation/#modify-project-configuration)[Modify babel.config.js](/router/installation/#modify-babelconfigjs)[Clear bundler cache](/router/installation/#clear-bundler-cache)[Update resolutions](/router/installation/#update-resolutions)