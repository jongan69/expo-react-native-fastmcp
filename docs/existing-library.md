Integrate in an existing library - Expo Documentation

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

Integrate in an existing library
================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/modules/existing-library.mdx)

Learn how to integrate Expo Modules API into an existing React Native library.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/modules/existing-library.mdx)

---

There are cases where you may want to integrate the Expo Modules API into an existing React Native library. For example, it might be useful to incrementally rewrite your library or to take advantage of [Android lifecycle listeners](/modules/android-lifecycle-listeners) and [iOS AppDelegate subscribers](/modules/appdelegate-subscribers) to automatically set up the library.

This guide will help you set up your existing React Native library to access Expo Modules API.

Prerequisites
-------------

Create the [expo-module.config.json](/modules/module-config) file at the root of your project and add an empty object `{}` inside it. You will fill it in later to enable specific features.

Creating this file is necessary for [Expo Autolinking](/modules/autolinking) to recognize your library as an Expo module and automatically link your native code.

1

Add the `expo-modules-core` native dependency
---------------------------------------------

Add `expo-modules-core` as a dependency in your build.gradle and podspec files:

build.gradle

Copy

```
// ...
dependencies {
  // ...
  implementation project(':expo-modules-core')
}

```

\*.podspec

Copy

```
# ...
Pod::Spec.new do |s|
  # ...
  s.dependency 'ExpoModulesCore'
end

```

2

Add Expo packages to dependencies
---------------------------------

Add `expo` package as a peer dependency in your package.json â we recommend using `*` as a version range so as not to cause any duplicated packages in user's node\_modules directory.

Your library also needs to depend on `expo-modules-core` but only as a dev dependency â it's already provided in the projects depending on your library by the `expo` package with the version of core that is compatible with the specific SDK used in the project.

package.json

Copy

```
{
  %%placeholder-start%%... %%placeholder-end%%
  "devDependencies": {
    "expo-modules-core": "^X.Y.Z"
  },
  "peerDependencies": {
    "expo": "*"
  },
  "peerDependenciesMeta": {
    "expo": {
      "optional": true
    }
  }
}

```

3

Create a native module
----------------------

Create Kotlin and Swift files from the templates below:

MyModule.kt

Copy

```
package my.module.package

import expo.modules.kotlin.modules.Module
import expo.modules.kotlin.modules.ModuleDefinition

class MyModule : Module() {
  override fun definition() = ModuleDefinition {
    // Definition components go here
  }
}

```

MyModule.swift

Copy

```
import ExpoModulesCore

public class MyModule: Module {
  public func definition() -> ModuleDefinition {
    // Definition components go here
  }
}

```

Then, add your classes to Android and/or iOS `modules` in the [expo-module.config.json](/modules/module-config) file. Expo Autolinking will automatically link these classes as native modules in the user's project.

expo-module.config.json

Copy

```
{
  "ios": {
    "modules": ["MyModule"]
  },
  "android": {
    "modules": ["my.module.package.MyModule"]
  }
}

```

If you already have an example app in your workspace, ensure that the module is linked correctly.

* On Android the native module class will be linked automatically before building, as part of the Gradle build task.
* On iOS you need to run `pod install` to link the new class.

These module classes are now accessible from the JavaScript code using the `requireNativeModule` function from the `expo-modules-core` package. We recommend creating a separate file that exports the native module for simplicity.

MyModule.ts

Copy

```
import { requireNativeModule } from 'expo-modules-core';

export default requireNativeModule('MyModule');

```

Now that the class is set up and linked, you can start to implement its functionality. See the [native module API](/modules/module-api) reference page and links to [examples](/modules/module-api#examples) from simple to moderately complex real-world modules to understand how to use the API.

[Previous (Expo Modules API - Tutorials)

Wrap third-party native libraries](/modules/third-party-library)[Next (Expo Modules API - Tutorials)

Additional platform support](/modules/additional-platform-support)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/modules/existing-library.mdx)
* Last updated on December 30, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Prerequisites](/modules/existing-library/#prerequisites)[Add the expo-modules-core native dependency](/modules/existing-library/#add-the-expo-modules-core-native-dependency)[Add Expo packages to dependencies](/modules/existing-library/#add-expo-packages-to-dependencies)[Create a native module](/modules/existing-library/#create-a-native-module)