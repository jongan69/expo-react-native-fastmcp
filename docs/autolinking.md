Autolinking - Expo Documentation

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

[Module API](/modules/module-api)[Android lifecycle listeners](/modules/android-lifecycle-listeners)[iOS AppDelegate subscribers](/modules/appdelegate-subscribers)[Autolinking](/modules/autolinking)[expo-module.config.json](/modules/module-config)[Mocking native calls](/modules/mocking)[Design considerations](/modules/design)

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

Autolinking
===========

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/modules/autolinking.mdx)

Learn how to use Expo Autolinking to automatically link native dependencies in your Expo project.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/modules/autolinking.mdx)

---

Usually, when you're developing a native mobile app and want to install a third-party library, you're asked to add the dependency to the manifest files of your package managers (build.gradle on Android, Podfile for CocoaPods on iOS, Package.swift for SwiftPM on iOS).
In Expo and React Native, you already do that with your package.json file by installing the package from the [npm](https://www.npmjs.com) registry. Since most of the React Native libraries come with some native (platform-specific) code,
installing a library will require configuring even up to three different package managers!

Expo Autolinking is a mechanism that automates this process and reduces the library installation process to the minimum â usually just installing the package from `npm` and re-running `pod install`.
The core implementation can be found in the [`expo-modules-autolinking`](https://github.com/expo/expo/tree/main/packages/expo-modules-autolinking) package and is divided into three parts:

1. common JavaScript CLI tool with the module resolution algorithm
2. code that integrates with the Gradle build system for Android platform
3. Ruby script that integrates with CocoaPods for iOS platform

CLI commands
------------

### `search`

Searching is the first phase of resolving the Expo modules installed in a project. Its implementation is shared between all platforms. It finds all modules marked as Expo modules and determines which version is of the highest precedence (in case of duplicates).

Terminal

Copy

`-Â``npx expo-modules-autolinking search`

The above command returns an object in JSON format with modules that have been found as dependencies:

```
{
  "expo-random": {
    "path": "/absolute/path/to/node_modules/expo-random",
    "version": "13.0.0",
    "config": {
      // Contents of `expo-module.config.json`
      "platforms": ["ios", "android"],
      "ios": { "modules": ["RandomModule"] },
      "android": { "modules": ["expo.modules.random.RandomModule"] }
    },
    "duplicates": [] // An array of other revisions (with lower precedence) of the same module
  }
  // more modules...
}

```

### `resolve`

Resolving is the second phase based on the results from the `search` command. It resolves each search result to an object with more (platform-specific) details, such as the path to the podspec or build.gradle files and module classes to link.

Terminal

Copy

`-Â``npx expo-modules-autolinking resolve --platform <apple|android>`

For example, with the `--platform apple` option it returns an object in JSON format with an array of modules and resolved details for the platform:

```
{
  "modules": [
    {
      "packageName": "expo-random",
      "packageVersion": "13.0.0",
      "pods": [
        {
          "podName": "ExpoRandom",
          "podspecDir": "/absolute/path/to/node_modules/expo-random/ios"
        }
      ],
      "swiftModuleNames": ["ExpoRandom"],
      "modules": ["RandomModule"],
      "appDelegateSubscribers": [],
      "reactDelegateHandlers": [],
      "debugOnly": false
    }
    // more modules...
  ]
}

```

### `verify`

Verifies the search results by checking whether there are no duplicate packages, otherwise an appropriate warning is shown.

Terminal

Copy

`-Â``npx expo-modules-autolinking verify`

Configuration
-------------

The behavior of the module resolution can be customized using some configuration options. These options can be defined in three different places, from the lowest to the highest precedence:

* `expo.autolinking` config object in application's package.json
* per platform overrides with `expo.autolinking.ios` and `expo.autolinking.android` objects
* options provided to the CLI command, the `use_expo_modules!` method in the Podfile or `useExpoModules` function in the settings.gradle

### `searchPaths`

A list of paths relative to the app's root directory where the autolinking script should search for Expo modules.
It defaults to a list of all node\_modules directories found when traversing up through a monorepo, starting from the app's root directory.
Useful when your project has a custom structure or you want to link local packages from directories different than node\_modules.

package.json

Copy

```
{
  "expo": {
    "autolinking": {
      "searchPaths": ["../../packages"]
    }
  }
}

```

When used with the CLI, you can pass the search paths as command arguments like this:

Terminal

Copy

`-Â``npx expo-modules-autolinking search ../../packages`

### `exclude`

A list of package names to exclude from autolinking. These packages will not be autolinked even if they are found in the search paths.
For example, you may want not to link some packages that you don't use on the specific platform to reduce the binary size.
The following config in package.json will exclude `expo-random` and `third-party-expo-module` from autolinking on Android:

package.json

Copy

```
{
  "expo": {
    "autolinking": {
      "android": {
        "exclude": ["expo-random", "third-party-expo-module"]
      }
    }
  }
}

```

Note that the `exclude` option is for excluding the autolinking of Expo packages. To exclude the autolinking for any other packages, create react-native.config.js at the root directory of your project and apply the configuration as shown in the example below:

react-native.config.js

Copy

```
module.exports = {
  dependencies: {
    'library-name': {
      platforms: {
        android: null,
      },
    },
  },
};

```

### `flags`

CocoaPods flags to pass to each autolinked pod. `inhibit_warnings` is likely the only flag most developers want to use, to inhibit Xcode warnings produced when compiling the autolinked modules.
You can refer to the [CocoaPods Podfile documentation](https://guides.cocoapods.org/syntax/podfile.html#pod) for available flags.

Podfile

Copy

```
use_expo_modules!({
  flags: {
    :inhibit_warnings => false
  }
})

```

package.json

Copy

```
{
  "expo": {
    "autolinking": {
      "ios": {
        "flags": {
          "inhibit_warnings": true
        }
      }
    }
  }
}

```

Common questions
----------------

### How to set up the autolinking in my app?

All projects created with the `npx create-expo-app` command are already configured to use Expo Autolinking. If your project was created using a different tool, see [Installing Expo modules](/bare/installing-expo-modules) to make sure your project includes all necessary changes.

### What do I need to have in my module to make it autolinkable?

The module resolution algorithm searches only for packages that contain the [Expo module config](/modules/module-config) file (expo-module.config.json) at the root directory, next to the package.json file.
It's also necessary to include supported platforms in the `platforms` array â if the platform for which the autolinking algorithm is run is not present in this array, it's just skipped in the search results.

### How is it different from React Native community CLI autolinking?

* Expo Autolinking comes in with built-in support for monorepos, Yarn workspaces and transitive dependencies.
* It's also significantly faster, even though the module resolution algorithm is more complex to be more reliable and match the Node's module resolution.
* Expo module resolution is also capable of detecting the duplicates which is a common issue in monorepos.
* Last but not least, it integrates well with all the features offered by Expo Modules APIs.

### Opting out of Expo Autolinking

Starting from SDK 52, Expo Autolinking comes enabled by default, if you would like to use the React Native community CLI autolinking instead, set `EXPO_USE_COMMUNITY_AUTOLINKING=1` and add `@react-native-community/cli` as a dev dependency to your project.

[Previous (Expo Modules API - Reference)

iOS AppDelegate subscribers](/modules/appdelegate-subscribers)[Next (Expo Modules API - Reference)

expo-module.config.json](/modules/module-config)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/modules/autolinking.mdx)
* Last updated on April 20, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[CLI commands](/modules/autolinking/#cli-commands)[search](/modules/autolinking/#search)[resolve](/modules/autolinking/#resolve)[verify](/modules/autolinking/#verify)[Configuration](/modules/autolinking/#configuration)[searchPaths](/modules/autolinking/#searchpaths)[exclude](/modules/autolinking/#exclude)[flags](/modules/autolinking/#flags)[Common questions](/modules/autolinking/#common-questions)[How to set up the autolinking in my app?](/modules/autolinking/#how-to-set-up-the-autolinking-in-my-app)[What do I need to have in my module to make it autolinkable?](/modules/autolinking/#what-do-i-need-to-have-in-my-module-to-make-it-autolinkable)[How is it different from React Native community CLI autolinking?](/modules/autolinking/#how-is-it-different-from-react-native-community-cli-autolinking)[Opting out of Expo Autolinking](/modules/autolinking/#opting-out-of-expo-autolinking)