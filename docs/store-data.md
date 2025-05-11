Store data - Expo Documentation

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

[Splash screen and app icon](/develop/user-interface/splash-screen-and-app-icon)[Safe areas](/develop/user-interface/safe-areas)[System bars](/develop/user-interface/system-bars)[Fonts](/develop/user-interface/fonts)[Assets](/develop/user-interface/assets)[Color themes](/develop/user-interface/color-themes)[Animation](/develop/user-interface/animation)[Store data](/develop/user-interface/store-data)[Next steps](/develop/user-interface/next-steps)

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

Store data
==========

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/user-interface/store-data.mdx)

Learn about different libraries available to store data in your Expo project.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/user-interface/store-data.mdx)

---

Storing data can be essential to the features implemented in your mobile app. There are different ways to save data in your Expo project depending on the type of data you want to store and the security requirements of your app. This page lists a variety of libraries to help you decide which solution is best for your project.

Expo SecureStore
----------------

`expo-secure-store` provides a way to encrypt and securely store key-value pairs locally on the device.

[![Icon](/static/images/packages/expo-secure-store.png)

Expo SecureStore API reference

For more information on how to install and use expo-secure-store, see its API documentation.](/versions/latest/sdk/securestore)

Expo FileSystem
---------------

`expo-file-system` provides access to a file system stored locally on the device. Within Expo Go, each project has a separate file system and no access to other Expo projects' files. However, it can save content shared by other projects to the local filesystem and share local files with other projects. It is also capable of uploading and downloading files from network URLs.

[![Icon](/static/images/packages/expo-file-system.png)

Expo FileSystem API reference

For more information on how to install and use expo-file-system, see its API documentation.](/versions/latest/sdk/filesystem)

Expo SQLite
-----------

`expo-sqlite` package gives your app access to a database that can be queried through a WebSQL-like API. The database is persisted across restarts of your app. You can use it for importing an existing database, opening databases, creating tables, inserting items, querying and displaying results, and using prepared statements.

[![Icon](/static/images/packages/expo-sqlite.png)

Expo SQLite API reference

For more information on how to install and use expo-sqlite, see its API documentation.](/versions/latest/sdk/sqlite)

Async Storage
-------------

[Async Storage](https://react-native-async-storage.github.io/async-storage/) is an asynchronous, unencrypted, persistent key-value storage for React Native apps. It has a simple API and is a good choice for storing small amounts of data. It is also a good choice for storing data that does not need encryption, such as user preferences or app state.

[![Icon](https://react-native-async-storage.github.io/async-storage/img/logo.svg)

Async Storage documentation

For more information on how to install and use Async Storage, see its documentation.](https://react-native-async-storage.github.io/async-storage/docs/usage)

Other libraries
---------------

There are other libraries available for storing data for different purposes. For example, you might not need encryption in your project or are looking for a faster solution similar to Async Storage.

We recommend checking out [React Native for a list of libraries](https://reactnative.directory/?search=storage) to help you store your project's data.

[Previous (Develop - User interface)

Animation](/develop/user-interface/animation)[Next (Develop - User interface)

Next steps](/develop/user-interface/next-steps)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/user-interface/store-data.mdx)
* Last updated on July 01, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Expo SecureStore](/develop/user-interface/store-data/#expo-securestore)[Expo FileSystem](/develop/user-interface/store-data/#expo-filesystem)[Expo SQLite](/develop/user-interface/store-data/#expo-sqlite)[Async Storage](/develop/user-interface/store-data/#async-storage)[Other libraries](/develop/user-interface/store-data/#other-libraries)