Clear bundler caches on Windows - Expo Documentation

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

[Overview](/troubleshooting/overview)["Application has not been registered" error](/troubleshooting/application-has-not-been-registered)[Clear bundler caches on macOS and Linux](/troubleshooting/clear-cache-macos-linux)[Clear bundler caches on Windows](/troubleshooting/clear-cache-windows)["React Native version mismatch" errors](/troubleshooting/react-native-version-mismatch)[Proxies](/troubleshooting/proxies)

Regulatory compliance

[Data and Privacy protection](/regulatory-compliance/data-and-privacy-protection)[GDPR compliance](/regulatory-compliance/gdpr)[HIPAA compliance](/regulatory-compliance/hipaa)[Privacy Shield](/regulatory-compliance/privacy-shield)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Clear bundler caches on Windows
===============================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/troubleshooting/clear-cache-windows.mdx)

Learn how to clear the bundler cache when using Yarn or npm with Expo CLI or React Native CLI on Windows.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/troubleshooting/clear-cache-windows.mdx)

---

> Need to clear development caches on macOS or Linux? [Find the relevant commands here.](/troubleshooting/clear-cache-macos-linux)

There are a number of different caches associated with your project that can prevent your project from running as intended. Clearing a cache sometimes can help you work around issues related to stale or corrupt data and is often useful when troubleshooting and debugging.

Expo CLI and Yarn
-----------------

Terminal

`# With Yarn workspaces, you may need to delete node_modules in each workspace`

`-Â``rm -rf node_modules`

  

`-Â``yarn cache clean`

  

`-Â``yarn`

  

`-Â``watchman watch-del-all`

  

`-Â``del %localappdata%Temphaste-map-*`

  

`-Â``del %localappdata%Tempmetro-cache`

  

`-Â``npx expo start --clear`

Expo CLI and npm
----------------

Terminal

`-Â``rm -rf node_modules`

  

`-Â``npm cache clean --force`

  

`-Â``npm install`

  

`-Â``watchman watch-del-all`

  

`-Â``del %localappdata%Temphaste-map-*`

  

`-Â``del %localappdata%Tempmetro-cache`

  

`-Â``npx expo start --clear`

React Native CLI and Yarn
-------------------------

Terminal

`# With Yarn workspaces, you may need to delete node_modules in each workspace`

`-Â``rm -rf node_modules`

  

`-Â``yarn cache clean`

  

`-Â``yarn`

  

`-Â``watchman watch-del-all`

  

`-Â``del %localappdata%Temphaste-map-*`

  

`-Â``del %localappdata%Tempmetro-cache`

  

`-Â``yarn start -- --reset-cache`

React Native CLI and npm
------------------------

Terminal

`-Â``rm -rf node_modules`

  

`-Â``npm cache clean --force`

  

`-Â``npm install`

  

`-Â``watchman watch-del-all`

  

`-Â``del %localappdata%Temphaste-map-*`

  

`-Â``del %localappdata%Tempmetro-cache`

  

`-Â``npm start -- --reset-cache`

What these commands are doing
-----------------------------

It is a good habit to understand commands you find on the internet before you run them. We explain each command below for Expo CLI, npm, and Yarn, but the corresponding commands React Native CLI have the same behavior.

| Command | Description |
| --- | --- |
| `del node_modules` | Clear all of the dependencies of your project |
| `yarn cache clean` | Clear the global Yarn cache |
| `npm cache clean --force` | Clear the global npm cache |
| `yarn`/`npm install` | Reinstall all dependencies |
| `watchman watch-del-all` | Reset the `watchman` file watcher |
| `del %localappdata%\Temp/<cache>` | Clear the given packager/bundler cache file or directory |
| `npx expo start --clear` | Restart the development server and clear the JavaScript transformation caches |

[Previous (More - Troubleshooting)

Clear bundler caches on macOS and Linux](/troubleshooting/clear-cache-macos-linux)[Next (More - Troubleshooting)

"React Native version mismatch" errors](/troubleshooting/react-native-version-mismatch)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/troubleshooting/clear-cache-windows.mdx)
* Last updated on August 05, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Expo CLI and Yarn](/troubleshooting/clear-cache-windows/#expo-cli-and-yarn)[Expo CLI and npm](/troubleshooting/clear-cache-windows/#expo-cli-and-npm)[React Native CLI and Yarn](/troubleshooting/clear-cache-windows/#react-native-cli-and-yarn)[React Native CLI and npm](/troubleshooting/clear-cache-windows/#react-native-cli-and-npm)[What these commands are doing](/troubleshooting/clear-cache-windows/#what-these-commands-are-doing)