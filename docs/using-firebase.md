Using Firebase - Expo Documentation

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

[Using Analytics](/guides/using-analytics)[Using Facebook authentication](/guides/facebook-authentication)[Using Supabase](/guides/using-supabase)[Using Firebase](/guides/using-firebase)[Using Google authentication](/guides/google-authentication)[Using ESLint and Prettier](/guides/using-eslint)[Using Next.js](/guides/using-nextjs)[Using LogRocket](/guides/using-logrocket)[Using Sentry](/guides/using-sentry)[Using BugSnag](/guides/using-bugsnag)[Using Vexo](/guides/using-vexo)[Build apps for TV](/guides/building-for-tv)[Using TypeScript](/guides/typescript)[Using In-app purchase](/guides/in-app-purchases)[Using push notifications](/guides/using-push-notifications-services)

Troubleshooting

Regulatory compliance

[Data and Privacy protection](/regulatory-compliance/data-and-privacy-protection)[GDPR compliance](/regulatory-compliance/gdpr)[HIPAA compliance](/regulatory-compliance/hipaa)[Privacy Shield](/regulatory-compliance/privacy-shield)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Using Firebase
==============

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/using-firebase.mdx)

A guide on getting started and using Firebase JS SDK and React Native Firebase library.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/using-firebase.mdx)

---

[Firebase](https://firebase.google.com/) is a Backend-as-a-Service (BaaS) app development platform that provides hosted backend services such as real-time database, cloud storage, authentication, crash reporting, analytics, and so on.
It is built on Google's infrastructure and scales automatically.

There are two different ways you can use Firebase in your projects:

* Using [Firebase JS SDK](/guides/using-firebase#using-firebase-js-sdk)
* Using [React Native Firebase](/guides/using-firebase#using-react-native-firebase)

React Native supports both the JS SDK and the native SDK. The following sections will guide you through when to use which SDK and all the configuration steps required to use Firebase in your Expo projects.

Prerequisites
-------------

Before proceeding, make sure that you have created a new Firebase project or have an existing one using the [Firebase console](https://console.firebase.google.com/).

Using Firebase JS SDK
---------------------

The [Firebase JS SDK](https://firebase.google.com/docs/web/setup) is a JavaScript library that allows you to interact with Firebase services in your project.
It supports services such as [Authentication](https://firebase.google.com/docs/auth), [Firestore](https://firebase.google.com/docs/firestore), [Realtime Database](https://firebase.google.com/docs/database), and [Storage](https://firebase.google.com/docs/storage) in a React Native app.

### When to use Firebase JS SDK

You can consider using the Firebase JS SDK when you:

* Want to use Firebase services such as Authentication, Firestore, Realtime Database, and Storage in your app and want to develop your app with [Expo Go](/get-started/set-up-your-environment).
* Want a quick start with Firebase services.
* Want to create a universal app for Android, iOS, and the web.

#### Caveats

Firebase JS SDK does not support all services for mobile apps. Some of these services are Analytics, Dynamic Links and Crashlytics. See the [React Native Firebase](/guides/using-firebase#using-react-native-firebase) section if you want to use these services.

### Install and initialize Firebase JS SDK

The following sub-sections use `firebase@9.x.x`. Expo SDK does not enforce or recommend any specific version of Firebase to use in your app.

If you are using an older version of the firebase library in your project, you may have to adapt the code examples to match the version that you are using with the help of the [Firebase JS SDK documentation](https://github.com/firebase/firebase-js-sdk).

1

#### Install the SDK

After you have created your [Expo project](/get-started/create-a-project), you can install the Firebase JS SDK using the following command:

Terminal

Copy

`-Â``npx expo install firebase`

2

#### Initialize the SDK in your project

To initialize the Firebase instance in your Expo project, you must create a config object and pass it to the `initializeApp()` method imported from the `firebase/app` module.

The config object requires an API key and other unique identifiers. To obtain these values, you will have to register a web app in your Firebase project. You can find these instructions in the [Firebase documentation](https://firebase.google.com/docs/web/setup#register-app).

After you have the API key and other identifiers, you can paste the following code snippet by creating a new firebaseConfig.js file in your project's root directory or any other directory where you keep the configuration files.

firebaseConfig.js

Copy

```
import { initializeApp } from 'firebase/app';

// Optionally import the services that you want to use
// import {...} from 'firebase/auth';
// import {...} from 'firebase/database';
// import {...} from 'firebase/firestore';
// import {...} from 'firebase/functions';
// import {...} from 'firebase/storage';

// Initialize Firebase
const firebaseConfig = {
  apiKey: 'api-key',
  authDomain: 'project-id.firebaseapp.com',
  databaseURL: 'https://project-id.firebaseio.com',
  projectId: 'project-id',
  storageBucket: 'project-id.appspot.com',
  messagingSenderId: 'sender-id',
  appId: 'app-id',
  measurementId: 'G-measurement-id',
};

const app = initializeApp(firebaseConfig);
// For more information on how to access Firebase in your project,
// see the Firebase documentation: https://firebase.google.com/docs/web/setup#access-firebase

```

You do not have to install other plugins or configurations to use Firebase JS SDK.

Firebase version 9 and above provide a modular API. You can directly import any service you want to use from the `firebase` package. For example, if you want to use an authentication service in your project, you can import the `auth` module from the `firebase/auth` package.

> Troubleshooting tip: If you encounter issues related to authentication persistence with Firebase JS SDK, see the guide for [setting up persistence to keep users logged in between reloads](https://expo.fyi/firebase-js-auth-setup).

3

#### Configure Metro

> If you are using Firebase version `9.7.x` and above, you need to add the following configuration to a metro.config.js file to make sure that the Firebase JS SDK is bundled correctly.

Expo CLI uses [Metro](https://metrobundler.dev/) to bundle your JavaScript code and assets, and add [support for more file extensions](/guides/customizing-metro#adding-more-file-extensions-to--assetexts).

Start by generating the template file metro.config.js in your project's root directory using the following command:

Terminal

Copy

`-Â``npx expo customize metro.config.js`

Then, update the file with the following configuration:

metro.config.js

Copy

```
const { getDefaultConfig } = require('@expo/metro-config');

const config = getDefaultConfig(__dirname);
config.resolver.sourceExts.push('cjs');
config.resolver.unstable_enablePackageExports = false;

module.exports = config;

```

### Next steps

[Authentication

For more information on how to use Authentication in your project, see Firebase documentation.](https://firebase.google.com/docs/auth/web/start)
[Firestore

For more information on how to use Firestore database in your project, see Firebase documentation.](https://firebase.google.com/docs/firestore/quickstart)
[Realtime Database

For more information on how to use Realtime Database in your project, see Firebase documentation.](https://firebase.google.com/docs/database)
[Storage

For more information on how to use Storage, see Firebase documentation.](https://firebase.google.com/docs/storage/web/start)
[Firebase Storage example

Learn how to use Firebase Storage in an Expo project with our example.](https://github.com/expo/examples/tree/master/with-firebase-storage-upload)
[Managing API keys for Firebase projects

For more information about managing API Key and unique identifiers in a Firebase project.](https://firebase.google.com/docs/projects/api-keys)
[Migrate from Expo Firebase packages to React Native Firebase

For more information on migrating from expo-firebase-analytics or expo-firebase-recaptcha packages to React Native Firebase.](https://expo.fyi/firebase-migration-guide)

Using React Native Firebase
---------------------------

[React Native Firebase](https://rnfirebase.io/) provides access to native code by wrapping the native SDKs for Android and iOS into a JavaScript API.
Each Firebase service is available as a module that can be added as a dependency to your project. For example, the `auth` module provides access to the Firebase Authentication service.

### When to use React Native Firebase

You can consider using React Native Firebase when:

* Your app requires access to Firebase services not supported by the Firebase JS SDK, such as [Dynamic Links](https://rnfirebase.io/dynamic-links/usage), [Crashlytics](https://rnfirebase.io/crashlytics/usage), and so on.
  For more information on the additional capabilities offered by the native SDK's, see [React Native Firebase documentation](https://rnfirebase.io/faqs-and-tips#why-react-native-firebase-over-firebase-js-sdk).
* You want to use native SDKs in your app.
* You have a bare React Native app with React Native Firebase already configured but are migrating to use Expo SDK.
* You want to use [Firebase Analytics](https://rnfirebase.io/analytics/usage) in your app.

Migrating from Expo Firebase packages?

If your project has been previously using `expo-firebase-analytics` and `expo-firebase-recaptcha` packages, you can migrate to the React Native Firebase library. For more information, see [Firebase migration guide](https://expo.fyi/firebase-migration-guide).

#### Caveats

React Native Firebase requires [custom native code and cannot be used with Expo Go](/workflow/customizing).

### Install and initialize React Native Firebase

1

#### Install expo-dev-client

Since React Native Firebase requires custom native code, you need to install the `expo-dev-client` library in your project.
It also allows configuring any native code required by React Native Firebase using [Config plugins](/config-plugins/introduction) without writing native code yourself.

To install [`expo-dev-client`](/development/getting-started#installing--expo-dev-client--in-your-project), run the following command in your project:

Terminal

Copy

`-Â``npx expo install expo-dev-client`

2

#### Install React Native Firebase

To use React Native Firebase, it is necessary to install the `@react-native-firebase/app` module. This module provides the core functionality for all other modules.
It also adds custom native code in your project using a config plugin. You can install it using the following command:

Terminal

Copy

`-Â``npx expo install @react-native-firebase/app`

At this point, you must follow the instructions from [React Native Firebase documentation](https://rnfirebase.io/#managed-workflow) as it covers all the steps required to configure your project with the library.

Once you have configured the React Native Firebase library in your project, come back to this guide to learn how to run your project in the next step.

3

#### Run the project

If you are using [EAS Build](/build/introduction), you can create and install a development build on your devices. You do not need to run the project locally before creating a development build.
For more information on creating a development build, see the section on [installing a development build](/develop/development-builds/create-a-build).

Run project locally?

If you want to run the project locally, you need both Android Studio and Xcode installed and configured on your machine. See [Local app development](/guides/local-app-development) guide for more information.

If a particular React Native Firebase module requires custom native configuration steps, you must add it as a `plugin` to [app config](/workflow/configuration) file. Then, to run the project locally, run the `npx expo prebuild --clean` command to apply the native changes before the `npx expo run` commands.

### Next steps

After configuring React Native Firebase library, you can use any module it provides in your Expo project.

[React Native Firebase documentation

For more information to install and use a certain module from React Native Firebase, we recommend you to check their documentation.](https://rnfirebase.io/)

[Previous (More - Integrations)

Using Supabase](/guides/using-supabase)[Next (More - Integrations)

Using Google authentication](/guides/google-authentication)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/using-firebase.mdx)
* Last updated on May 07, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Prerequisites](/guides/using-firebase/#prerequisites)[Using Firebase JS SDK](/guides/using-firebase/#using-firebase-js-sdk)[When to use Firebase JS SDK](/guides/using-firebase/#when-to-use-firebase-js-sdk)[Caveats](/guides/using-firebase/#caveats)[Install and initialize Firebase JS SDK](/guides/using-firebase/#install-and-initialize-firebase-js-sdk)[Install the SDK](/guides/using-firebase/#install-the-sdk)[Initialize the SDK in your project](/guides/using-firebase/#initialize-the-sdk-in-your-project)[Configure Metro](/guides/using-firebase/#configure-metro)[Next steps](/guides/using-firebase/#next-steps)[Using React Native Firebase](/guides/using-firebase/#using-react-native-firebase)[When to use React Native Firebase](/guides/using-firebase/#when-to-use-react-native-firebase)[Caveats](/guides/using-firebase/#caveats-1)[Install and initialize React Native Firebase](/guides/using-firebase/#install-and-initialize-react-native-firebase)[Install expo-dev-client](/guides/using-firebase/#install-expo-dev-client)[Install React Native Firebase](/guides/using-firebase/#install-react-native-firebase)[Run the project](/guides/using-firebase/#run-the-project)[Next steps](/guides/using-firebase/#next-steps-1)