Developing and debugging a plugin - Expo Documentation

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

Config plugins

[Introduction](/config-plugins/introduction)[Plugins and mods](/config-plugins/plugins-and-mods)[Development and debugging](/config-plugins/development-and-debugging)

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

Developing and debugging a plugin
=================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/config-plugins/development-and-debugging.mdx)

Learn about development best practices and debugging techniques for Expo config plugins.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/config-plugins/development-and-debugging.mdx)

---

Developing a plugin is a great way to extend the Expo ecosystem. However, there are times you'll want to debug your plugin. This page provides some of the best practices for developing and debugging a plugin.

Develop a plugin
----------------

> Use [modifier previews](https://github.com/expo/vscode-expo#expo-preview-modifier) to debug the results of your plugin live.

To make plugin development easier, we've added plugin support to [`expo-module-scripts`](https://www.npmjs.com/package/expo-module-scripts).
Refer to the [config plugins guide](https://github.com/expo/expo/tree/main/packages/expo-module-scripts#-config-plugin) for more info on using TypeScript, and Jest to build plugins.

### Install dependencies

Use the following dependencies in a library that provides a config plugin:

package.json

Copy

```
{
  "dependencies": {},
  "devDependencies": {
    "expo": "^47.0.0"
  },
  "peerDependencies": {
    "expo": ">=47.0.0"
  },
  "peerDependenciesMeta": {
    "expo": {
      "optional": true
    }
  }
}

```

* You may update the exact version of `expo` to build against a specific version.
* For simple config plugins that depend on core, stable APIs, such as a plugin that only modifies AndroidManifest.xml or Info.plist, you can use a loose dependency such as in the example above.
* You may also want to install [`expo-module-scripts`](https://github.com/expo/expo/blob/main/packages/expo-module-scripts/README.md) as a development dependency, but it's not required.

### Import the config plugins package

The `expo/config-plugins` and `expo/config` packages are re-exported from the `expo` package.

```
const { %%placeholder-start%%...%%placeholder-end%%/* @end */ } = require('expo/config-plugins');
const { %%placeholder-start%%...%%placeholder-end%%/* @end */ } = require('expo/config');

```

Importing through the `expo` package ensures that you are using the version of the `expo/config-plugins` and `expo/config` packages that are depended on by the `expo` package.

If you do not import the package through the `expo` re-export in this way, you may accidentally be importing an incompatible version
(depending on the implementation details of module hoisting in the package manager used by the developer consuming the module) or be unable to import the module at all
(if using "plug and play" features of a package manager such as Yarn Berry or pnpm).

Config types are exported directly from `expo/config`, so there is no need to install or import from `expo/config-types`:

```
import { ExpoConfig, ConfigContext } from 'expo/config';

```

### Best practices for mods

* Avoid regex: [static modification](/config-plugins/development-and-debugging#static-modification) is key. If you want to modify a value in an Android gradle file, consider using `gradle.properties`. If you want to modify some code in the Podfile, consider writing to JSON and having the Podfile read the static values.
* Avoid performing long-running tasks like making network requests or installing Node modules in mods.
* Do not add interactive terminal prompts in mods.
* Generate, move, and delete new files in dangerous mods only. Failing to do so will break [introspection](/config-plugins/development-and-debugging#introspection).
* Utilize built-in config plugins like `withXcodeProject` to minimize the amount of times a file is read and parsed.
* Stick with the XML parsing libraries that prebuild uses internally, this helps prevent changes where code is rearranged needlessly.

### Tooling

We highly recommend installing the [Expo Tools VS Code extension](https://marketplace.visualstudio.com/items?itemName=expo.vscode-expo-tools)
as this will perform automatic validation on the plugins and surface error information along with other quality of life improvements for Config Plugin development.

### Setup up a playground environment

You can develop plugins easily using JS, but if you want to setup Jest tests and use TypeScript, you will want a monorepo.

A monorepo will enable you to work on a node module and import it in your app config like you would if it were published to npm.
Expo config plugins have full monorepo support built-in so all you need to do is setup a project.

In your monorepo's `packages/` directory, create a module, and [bootstrap a config plugin](https://github.com/expo/expo/tree/main/packages/expo-module-scripts#-config-plugin) in it.

### Manually run a plugin

If you aren't comfortable setting up a monorepo, you can try manually running a plugin:

* Run `npm pack` in the package with the config plugin
* In your test project, run `npm install path/to/react-native-my-package-1.0.0.tgz`, this will add the package to your package.json `dependencies` object.
* Add the package to the `plugins` array in your app.json: `{ "plugins": ["react-native-my-package"] }`
  + If you have [VS Code Expo Tools](https://marketplace.visualstudio.com/items?itemName=expo.vscode-expo-tools) installed, autocomplete should work for the plugin.
* If you need to update the package, change the `version` in the package's package.json and repeat the process.

### Modify AndroidManifest.xml

Packages should attempt to use the built-in AndroidManifest.xml [merging system](https://developer.android.com/studio/build/manage-manifests)
before using a config plugin. This can be used for static, non-optional features like permissions.
This will ensure features are merged during build-time and not prebuild-time, which minimizes the possibility of users forgetting to prebuild.
The drawback is that users cannot use [introspection](/config-plugins/development-and-debugging#introspection) to preview the changes and debug any potential issues.

Here is an example of a package's AndroidManifest.xml, which injects a required permission:

AndroidManifest.xml

Copy

```
<manifest package="expo.modules.filesystem" xmlns:android="http://schemas.android.com/apk/res/android">
  <uses-permission android:name="android.permission.INTERNET"/>
</manifest>

```

If you're building a plugin for your local project, or if your package needs more control, then you should implement a plugin.

You can use built-in types and helpers to ease the process of working with complex objects.
Here's an example of adding a `<meta-data android:name="..." android:value="..."/>` to the default `<application android:name=".MainApplication" />`.

my-config-plugin.ts

Copy

```
import { AndroidConfig, ConfigPlugin, withAndroidManifest } from 'expo/config-plugins';
import { ExpoConfig } from 'expo/config';

// Using helpers keeps error messages unified and helps cut down on XML format changes.
const { addMetaDataItemToMainApplication, getMainApplicationOrThrow } = AndroidConfig.Manifest;

export const withMyCustomConfig: ConfigPlugin = config => {
  return withAndroidManifest(config, async config => {
    // Modifiers can be async, but try to keep them fast.
    config.modResults = await setCustomConfigAsync(config, config.modResults);
    return config;
  });
};

// Splitting this function out of the mod makes it easier to test.
async function setCustomConfigAsync(
  config: Pick<ExpoConfig, 'android'>,
  androidManifest: AndroidConfig.Manifest.AndroidManifest
): Promise<AndroidConfig.Manifest.AndroidManifest> {
  const appId = 'my-app-id';
  // Get the <application /> tag and assert if it doesn't exist.
  const mainApplication = getMainApplicationOrThrow(androidManifest);

  addMetaDataItemToMainApplication(
    mainApplication,
    // value for `android:name`
    'my-app-id-key',
    // value for `android:value`
    appId
  );

  return androidManifest;
}

```

### Modify Info.plist

Using the `withInfoPlist` is a bit safer than statically modifying the `expo.ios.infoPlist` object in the app.json because it reads the contents of the Info.plist and merges it with the `expo.ios.infoPlist`, this means you can attempt to keep your changes from being overwritten.

Here's an example of adding a `GADApplicationIdentifier` to the Info.plist:

my-config-plugin.ts

Copy

```
import { ConfigPlugin, withInfoPlist } from 'expo/config-plugins';

// Pass `<string>` to specify that this plugin requires a string property.
export const withCustomConfig: ConfigPlugin<string> = (config, id) => {
  return withInfoPlist(config, config => {
    config.modResults.GADApplicationIdentifier = id;
    return config;
  });
};

```

### Modify iOS Podfile

The iOS Podfile is the config file for CocoaPods, the dependency manager on iOS. It is similar to package.json for iOS.
The Podfile is a Ruby file, which means you cannot safely modify it from Expo config plugins and should opt for another approach, such as [Expo Autolinking](/modules/autolinking) hooks.

We do expose one mechanism for safely interacting with the Podfile, but it's very limited.
The versioned [template Podfile](https://github.com/expo/expo/tree/main/templates/expo-template-bare-minimum/ios/Podfile) is hard coded to read
from a static JSON file Podfile.properties.json, we expose a mod (`ios.podfileProperties`, `withPodfileProperties`) to safely read and write from this file.
This is used by [expo-build-properties](/versions/latest/sdk/build-properties) and to configure the JavaScript engine.

### Add plugins to `pluginHistory`

`_internal.pluginHistory` was created to prevent duplicate plugins from running while migrating from legacy UNVERSIONED plugins to versioned plugins.

my-config-plugin.ts

Copy

```
import { ConfigPlugin, createRunOncePlugin } from 'expo/config-plugins';

// Keeping the name, and version in sync with it's package.
const pkg = require('my-cool-plugin/package.json');

const withMyCoolPlugin: ConfigPlugin = config => config;

// A helper method that wraps `withRunOnce` and appends items to `pluginHistory`.
export default createRunOncePlugin(
  // The plugin to guard.
  withMyCoolPlugin,
  // An identifier used to track if the plugin has already been run.
  pkg.name,
  // Optional version property, if omitted, defaults to UNVERSIONED.
  pkg.version
);

```

### Plugin development best practices

* Instructions in your README: If the plugin is tied to a React Native module, then you should document manual setup instructions for the package.
  If anything goes wrong with the plugin, users should still be able to manually add the package to their project.
  Doing this often helps you find ways to reduce the setup, which can lead to a simpler plugin.
  + Document the available properties for the plugin, and specify if the plugin works without props.
  + If you can make your plugin work after running prebuild multiple times, that's a big plus! It can improve the developer experience to be able to run `npx expo prebuild` without the `--clean` flag to sync changes.
* Naming conventions: Use `withFeatureName` if cross-platform. If the plugin is platform specific, use a camel case naming with the platform right after "with". For example, `withAndroidSplash`, `withIosSplash`.
  There is no universally agreed upon casing for `iOS` in camel cased identifiers, we prefer this style and suggest using it for your config plugins too.
* Leverage built-in plugins: Account for built-in plugins from the [prebuild config](https://github.com/expo/expo-cli/blob/master/packages/prebuild-config/src/plugins/withDefaultPlugins.ts).
  Some features are included for historical reasons, like the ability to automatically copy and link [Google services files](https://github.com/expo/expo-cli/blob/3a0ef962a27525a0fe4b7e5567fb7b3fb18ec786/packages/config-plugins/src/ios/Google.ts#L15) defined in the app config.
  If there is overlap, then maybe recommend the user uses the built-in types to keep your plugin as simple as possible.
* Split up plugins by platform: For example â `withIosSplash`, `withAndroidSplash`. This makes using the `--platform` flag in `npx expo prebuild` a bit easier to follow in `EXPO_DEBUG` mode.
* Unit test your plugin: Write Jest tests for complex modifications. If your plugin requires access to the filesystem,
  use a mock system (we strongly recommend [`memfs`](https://www.npmjs.com/package/memfs)), you can see examples of this in the [`expo-notifications`](https://github.com/expo/expo/blob/fc3fb2e81ad3a62332fa1ba6956c1df1c3186464/packages/expo-notifications/plugin/src/__tests__/withNotificationsAndroid-test.ts#L34) plugin tests.
  + Notice the root [\*\*/\_\_mocks\_\_/\*\*/\*](https://github.com/expo/expo/tree/main/packages/expo-notifications/plugin/__mocks__) directory and [plugin/jest.config.js](https://github.com/expo/expo/tree/main/packages/expo-notifications/plugin/jest.config.js).
* A TypeScript plugin is always better than a JavaScript plugin. Check out the [`expo-module-script` plugin](https://github.com/expo/expo/tree/main/packages/expo-module-scripts#-config-plugin) tooling for more info.
* Do not modify the `sdkVersion` via a config plugin, this can break commands like `expo install` and cause other unexpected issues.

### Versioning

By default, `npx expo prebuild` runs transformations on a [source template](https://github.com/expo/expo/tree/main/templates/expo-template-bare-minimum) associated with the Expo SDK version that a project is using.
The SDK version is defined in the app.json or inferred from the installed version of `expo` that the project has.

When Expo SDK upgrades to a new version of React Native for instance, the template may change significantly to account for changes in React Native or new releases of Android or iOS.

If your plugin is mostly using [static modifications](/config-plugins/development-and-debugging#static-modification) then it will work well across versions.
If it's using a regular expression to transform application code, then you'll definitely want to document which Expo SDK version your plugin is intended for.
Expo releases a new version quarterly (every 3 months), and there is a [beta period](https://github.com/expo/expo/blob/main/guides/releasing/Release%20Workflow.md#stage-5---beta-release) where you can test if your plugin works with the new version before it's released.

### Plugin properties

Properties are used to customize the way a plugin works during prebuild.

Properties MUST always be static values (no functions, or promises). Consider the following types:

```
type StaticValue = boolean | number | string | null | StaticArray | StaticObject;

type StaticArray = StaticValue[];

interface StaticObject {
  [key: string]: StaticValue | undefined;
}

```

Static properties are required because the app config must be serializable to JSON for use as the app manifest.
Static properties can also enable tooling that generates JSON schema type checking for autocomplete and IntelliSense.

If possible, attempt to make your plugin work without props, this will help resolution tooling like [`expo install`](/config-plugins/development-and-debugging#expo-install) or [VS Code Expo Tools](https://marketplace.visualstudio.com/items?itemName=expo.vscode-expo-tools) work better.
Remember that every property you add increases complexity, making it harder to change in the future and increase the amount of features you'll need to test.
Good default values are preferred over mandatory configuration when feasible.

### Configure Android app startup

You may find that your project requires configuration to be setup before the JS engine has started.
For example, in `expo-splash-screen` on Android, we need to specify the resize mode in the MainActivity.java's `onCreate` method.
Instead of attempting to dangerously regex these changes into the `MainActivity` via a dangerous mod, we use a system of lifecycle hooks and static settings
to safely ensure the feature works across all supported Android languages (Java, Kotlin), versions of Expo, and combination of config plugins.

This system is made up of three components:

* `ReactActivityLifecycleListeners`: An interface exposed by `expo-modules-core` to get a native callback when the project `ReactActivity`'s `onCreate` method is invoked.
* `withStringsXml`: A mod exposed by `expo/config-plugins` which writes a property to the Android strings.xml file, the library can safely read the strings.xml value and do initial setup. The string XML values follow a designated format for consistency.
* `SingletonModule` (optional): An interface exposed by `expo-modules-core` to create a shared interface between native modules and `ReactActivityLifecycleListeners`.

Consider this example: We want to set a custom "value" string to a property on the Android `Activity`, directly after the `onCreate` method was invoked.
We can do this safely by creating a node module `expo-custom`, implementing `expo-modules-core`, and Expo config plugins:

First, we register the `ReactActivity` listener in our Android native module, this will only be invoked if the user has `expo-modules-core` support, setup in their project (default in projects bootstrapped with Expo CLI, Create React Native App, Ignite CLI, and Expo prebuilding).

expo-custom/android/src/main/java/expo/modules/custom/CustomPackage.kt

Copy

```
package expo.modules.custom

import android.content.Context
import expo.modules.core.BasePackage
import expo.modules.core.interfaces.ReactActivityLifecycleListener

class CustomPackage : BasePackage() {
  override fun createReactActivityLifecycleListeners(activityContext: Context): List<ReactActivityLifecycleListener> {
    return listOf(CustomReactActivityLifecycleListener(activityContext))
  }

  // ...
}

```

Next we implement the `ReactActivity` listener, this is passed the `Context` and is capable of reading from the project strings.xml file.

expo-custom/android/src/main/java/expo/modules/custom/CustomReactActivityLifecycleListener.kt

Copy

```
package expo.modules.custom

import android.app.Activity
import android.content.Context
import android.os.Bundle
import android.util.Log
import expo.modules.core.interfaces.ReactActivityLifecycleListener

class CustomReactActivityLifecycleListener(activityContext: Context) : ReactActivityLifecycleListener {
  override fun onCreate(activity: Activity, savedInstanceState: Bundle?) {
    // Execute static tasks before the JS engine starts.
    // These values are defined via config plugins.

    var value = getValue(activity)
    if (value != "") {
      // Do something to the Activity that requires the static value...
    }
  }

  // Naming is node module name (`expo-custom`) plus value name (`value`) using underscores as a delimiter
  // i.e. `expo_custom_value`
  // `@expo/vector-icons` + `iconName` -> `expo__vector_icons_icon_name`
  private fun getValue(context: Context): String = context.getString(R.string.expo_custom_value).toLowerCase()
}

```

We must define default string.xml values which the user will overwrite locally by using the same `name` property in their strings.xml file.

expo-custom/android/src/main/res/values/strings.xml

Copy

```
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="expo_custom_value" translatable="false"></string>
</resources>

```

At this point, bare users can configure this value by creating a string in their local strings.xml file (assuming they also have `expo-modules-core` support setup):

./android/app/src/main/res/values/strings.xml

Copy

```
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="expo_custom_value" translatable="false">I Love Expo</string>
</resources>

```

For managed users, we can expose this functionality (safely!) via an Expo config plugin:

expo-custom/app.plugin.js

Copy

```
const { AndroidConfig, withStringsXml } = require('expo/config-plugins');

function withCustom(config, value) {
  return withStringsXml(config, config => {
    config.modResults = setStrings(config.modResults, value);
    return config;
  });
}

function setStrings(strings, value) {
  // Helper to add string.xml JSON items or overwrite existing items with the same name.
  return AndroidConfig.Strings.setStringItem(
    [
      // XML represented as JSON
      // <string name="expo_custom_value" translatable="false">value</string>
      { $: { name: 'expo_custom_value', translatable: 'false' }, _: value },
    ],
    strings
  );
}

```

Managed Expo users can now interact with this API like so:

app.json

Copy

```
{
  "expo": {
    "plugins": [["expo-custom", "I Love Expo"]]
  }
}

```

By re-running `npx expo prebuild -p` (`eas build -p android`, or `npx expo run:ios`) the user can now see the changes, safely applied in their managed project!

As you can see from the example, we rely heavily on application code (expo-modules-core) to interact with application code (the native project). This ensures that our config plugins are safe and reliable, hopefully for a very long time!

Debug config plugins
--------------------

You can debug config plugins by running `EXPO_DEBUG=1 expo prebuild`. If `EXPO_DEBUG` is enabled, the plugin stack logs will be printed, these are useful for viewing which mods ran, and in what order they ran in. To view all static plugin resolution errors, enable `EXPO_CONFIG_PLUGIN_VERBOSE_ERRORS`, this should only be needed for plugin authors. By default, some automatic plugin errors are hidden because they're usually related to versioning issues and aren't very helpful (that is, legacy package doesn't have a config plugin yet).

Running `npx expo prebuild --clean` with remove the generated native directories before compiling.

You can also run `npx expo config --type prebuild` to print the results of the plugins with the mods unevaluated (no code is generated).

Expo CLI commands can be profiled using `EXPO_PROFILE=1`.

Introspection
-------------

Introspection is an advanced technique used to read the evaluated results of modifiers without generating any code in the project.
This can be used to quickly debug the results of [static modifications](/config-plugins/development-and-debugging#static-modification) without needing to run prebuild.
You can interact with introspection live, by using the [preview feature](https://github.com/expo/vscode-expo#expo-preview-modifier) of `vscode-expo`.

You can try introspection by running `expo config --type introspect` in a project.

Introspection only supports a subset of modifiers:

* `android.manifest`
* `android.gradleProperties`
* `android.strings`
* `android.colors`
* `android.colorsNight`
* `android.styles`
* `ios.infoPlist`
* `ios.entitlements`
* `ios.expoPlist`
* `ios.podfileProperties`

> Introspection only works on safe modifiers (static files like JSON, XML, plist, properties), except `ios.xcodeproj` which often requires file system changes, making it non idempotent.

Introspection works by creating custom base mods that work like the default base mods, except they don't write the `modResults` to disk at the end.
Instead of persisting, they save the results to the app config under `_internal.modResults`, followed by the name of the mod
such as the `ios.infoPlist` mod saves to `_internal.modResults.ios.infoPlist: {}`.

As a real-world example, introspection is used by `eas-cli` to determine what the final iOS entitlements will be in a managed app, so it can sync them with the Apple Developer Portal before building. Introspection can also be used as a handy debugging and development tool.

Legacy plugins
--------------

To make `eas build` work the same as the classic `expo build` service, we added support for "legacy plugins" which are applied automatically to a project when they're installed in the project.

For instance, say a project has `expo-camera` installed but doesn't have `plugins: ['expo-camera']` in their app.json.
Expo CLI would automatically add `expo-camera` to the plugins to ensure that the required camera and microphone permissions are added to the project.
The user can still customize the `expo-camera` plugin by adding it to the `plugins` array manually, and the manually defined plugins will take precedence over the automatic plugins.

You can debug which plugins were added by running `expo config --type prebuild` and seeing the `_internal.pluginHistory` property.

This will show an object with all plugins that were added using `withRunOnce` plugin from `expo/config-plugins`.

Notice that `expo-location` uses `version: '11.0.0'`, and `react-native-maps` uses `version: 'UNVERSIONED'`. This means the following:

* `expo-location` and `react-native-maps` are both installed in the project.
* `expo-location` is using the plugin from the project's `node_modules/expo-location/app.plugin.js`
* The version of `react-native-maps` installed in the project doesn't have a plugin, so it's falling back on the unversioned plugin that is shipped with `expo-cli` for legacy support.

```
{
  _internal: {
    pluginHistory: {
      'expo-location': {
        name: 'expo-location',
        version: '11.0.0',
      },
      'react-native-maps': {
        name: 'react-native-maps',
        version: 'UNVERSIONED',
      },
    },
  },
};

```

For the most *stable* experience, you should try to have no `UNVERSIONED` plugins in your project. This is because the `UNVERSIONED` plugin may not support the native code in your project.
For instance, say you have an `UNVERSIONED` Facebook plugin in your project, if the Facebook native code or plugin has a breaking change, that will break the way your project prebuilds and cause it to error on build.

Static modification
-------------------

Plugins can transform application code with regular expressions, but these modifications are dangerous if the template changes over time then the regex becomes hard to predict (similarly if the user modifies a file manually or uses a custom template). Here are some examples of files you shouldn't modify manually, and alternatives.

### Android Gradle Files

Gradle files are written in either Groovy or Kotlin. They are used to manage dependencies, versioning, and other settings in the Android app.
Instead of modifying them directly with the `withProjectBuildGradle`, `withAppBuildGradle`, or `withSettingsGradle` mods, utilize the static `gradle.properties` file.

The `gradle.properties` is a static key/value pair that groovy files can read from. For example, say you wanted to control some toggle in Groovy:

gradle.properties

Copy

```
expo.react.jsEngine=hermes

```

Then later in a Gradle file:

app/build.gradle

Copy

```
project.ext.react = [enableHermes: findProperty('expo.react.jsEngine') ?: 'jsc']

```

* For keys in the `gradle.properties`, use camel case separated by `.`s, and usually starting with the `expo` prefix to denote that the property is managed by prebuild.
* To access the property, use one of two global methods:
  + `property`: Get a property, throw an error if the property is not defined.
  + `findProperty`: Get a property without throwing an error if the property is missing. This can often be used with the `?:` operator to provide a default value.

Generally, you should only interact with the Gradle file via Expo [Autolinking](/more/glossary-of-terms#autolinking), this provides a programmatic interface with the project files.

### iOS AppDelegate

Some modules may need to add delegate methods to the project AppDelegate. This can be done safely by using [AppDelegate subscribers](/modules/appdelegate-subscribers) or dangerously via the `withAppDelegate` mod (*strongly discouraged*).
Using AppDelegate subscribers allows native Expo modules to react to important events in a safe and reliable way.

Below are some examples of the AppDelegate subscribers in action. Additionally, you will find many examples in community repositories on GitHub ([one such example](https://github.com/bamlab/react-native-app-security/blob/c1a861cbd348f404ec18ffae90d1c9bdc66bc00d/ios/RNASAppLifecyleDelegate.swift)).

* `expo-linking`: [LinkingAppDelegateSubscriber.swift](https://github.com/expo/expo/blob/b4ca25a4319d7148258ebd5121d1df40a3b1333e/packages/expo-linking/ios/LinkingAppDelegateSubscriber.swift#L14) (openURL)
* `expo-notifications`: [NotificationsAppDelegateSubscriber.swift](https://github.com/expo/expo/blob/bd469e421856f348d539b1b57325890147935dbc/packages/expo-notifications/ios/EXNotifications/PushToken/EXPushTokenManager.m) (didRegisterForRemoteNotificationsWithDeviceToken, didFailToRegisterForRemoteNotificationsWithError, didReceiveRemoteNotification)

### iOS CocoaPods Podfile

The Podfile can be customized with a regular expression (this is considered dangerous because these types of changes do not compose well and multiple changes are likely to collide), but it's more reliable to instead set configuration values in JSON file called Podfile.properties.json. See how `podfile_properties` is used to customize the Podfile below:

Podfile

Copy

```
require 'json'

podfile_properties = JSON.parse(File.read(File.join(__dir__, 'Podfile.properties.json'))) rescue {}

platform :ios, podfile_properties['ios.deploymentTarget'] || '15.1'

target 'yolo27' do
  use_expo_modules!
  # ...

  # podfile_properties['your_property']
end

```

Generally, you should only interact with the Podfile via Expo [Autolinking](/more/glossary-of-terms#autolinking), this provides a programmatic interface with the project files.

### Custom base modifiers

The Expo CLI `npx expo prebuild` command uses [`@expo/prebuild-config`](https://github.com/expo/expo-cli/tree/main/packages/prebuild-config#readme) to get the default base modifiers. These defaults only manage a subset of common files, if you want to manage custom files you can do that locally by adding new base modifiers.

For example, say you wanted to add support for managing the `ios/*/AppDelegate.h` file, you could do this by adding a `ios.appDelegateHeader` modifier.

> This example uses `ts-node` for simple local TypeScript support, this isn't strictly necessary. [Learn more](/guides/typescript#appconfigjs).

withAppDelegateHeaderBaseMod.ts

Copy

```
import { ConfigPlugin, IOSConfig, Mod, withMod, BaseMods } from 'expo/config-plugins';
import fs from 'fs';

/**
 * A plugin which adds new base modifiers to the prebuild config.
 */
export function withAppDelegateHeaderBaseMod(config) {
  return BaseMods.withGeneratedBaseMods<'appDelegateHeader'>(config, {
    platform: 'ios',
    providers: {
      // Append a custom rule to supply AppDelegate header data to mods on `mods.ios.appDelegateHeader`
      appDelegateHeader: BaseMods.provider<IOSConfig.Paths.AppDelegateProjectFile>({
        // Get the local filepath that should be passed to the `read` method.
        getFilePath({ modRequest: { projectRoot } }) {
          const filePath = IOSConfig.Paths.getAppDelegateFilePath(projectRoot);
          // Replace the .m with a .h
          if (filePath.endsWith('.m')) {
            return filePath.substr(0, filePath.lastIndexOf('.')) + '.h';
          }
          // Possibly a Swift project...
          throw new Error(`Could not locate a valid AppDelegate.h at root: "${projectRoot}"`);
        },
        // Read the input file from the filesystem.
        async read(filePath) {
          return IOSConfig.Paths.getFileInfo(filePath);
        },
        // Write the resulting output to the filesystem.
        async write(filePath: string, { modResults: { contents } }) {
          await fs.promises.writeFile(filePath, contents);
        },
      }),
    },
  });
}

/**
 * (Utility) Provides the AppDelegate header file for modification.
 */
export const withAppDelegateHeader: ConfigPlugin<Mod<IOSConfig.Paths.AppDelegateProjectFile>> = (
  config,
  action
) => {
  return withMod(config, {
    platform: 'ios',
    mod: 'appDelegateHeader',
    action,
  });
};

// (Example) Log the contents of the modifier.
export const withSimpleAppDelegateHeaderMod = config => {
  return withAppDelegateHeader(config, config => {
    console.log('modify header:', config.modResults);
    return config;
  });
};

```

To use this new base mod, add it to the plugins array. The base mod MUST be added last after all other plugins that use the mod, this is because it must write the results to disk at the end of the process.

app.config.js

Copy

```
// Required for external files using TS
require('ts-node/register');

import {
  withAppDelegateHeaderBaseMod,
  withSimpleAppDelegateHeaderMod,
} from './withAppDelegateHeaderBaseMod.ts';

export default ({ config }) => {
  if (!config.plugins) config.plugins = [];
  config.plugins.push(
    withSimpleAppDelegateHeaderMod,

    // Base mods MUST be last
    withAppDelegateHeaderBaseMod
  );
  return config;
};

```

For more info, see [the PR that adds support](https://github.com/expo/expo-cli/pull/3852) for this feature.

expo install
------------

Node modules with config plugins can be added to the project's app config automatically by using the `expo install` command. [Related PR](https://github.com/expo/expo-cli/pull/3437).

This makes setup a bit easier and helps prevent users from forgetting to add a plugin.

This does come with a couple of caveats:

1. Packages can use both use a root app.plugin.js file or use the `main` entry point to ship a config plugin. `expo install` only adds config plugins using the root app.config.js file automatically to the app manifest. This rule was added to prevent popular packages like `lodash` from being mistaken for a config plugin and breaking the prebuild.
2. There is currently no mechanism for detecting if a config plugin has mandatory props. Because of this, `expo install` will only add the plugin, and not attempt to add any extra props. For example, `expo-camera` has optional extra props, so `plugins: ['expo-camera']` is valid, but if it had mandatory props then `expo-camera` would throw an error.
3. Plugins can only be automatically added when the user's project uses a static app config (app.json and app.config.json). If the user runs `expo install expo-camera` in a project with an app.config.js, they'll see a warning like:

```
Cannot automatically write to dynamic config at: app.config.js
Please add the following to your app config

{
  "plugins": [
    "expo-camera"
  ]
}

```

[Previous (Develop - Config plugins)

Plugins and mods](/config-plugins/plugins-and-mods)[Next (Develop - Debugging)

Errors and warnings](/debugging/errors-and-warnings)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/config-plugins/development-and-debugging.mdx)
* Last updated on April 30, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Develop a plugin](/config-plugins/development-and-debugging/#develop-a-plugin)[Install dependencies](/config-plugins/development-and-debugging/#install-dependencies)[Import the config plugins package](/config-plugins/development-and-debugging/#import-the-config-plugins-package)[Best practices for mods](/config-plugins/development-and-debugging/#best-practices-for-mods)[Tooling](/config-plugins/development-and-debugging/#tooling)[Setup up a playground environment](/config-plugins/development-and-debugging/#setup-up-a-playground-environment)[Manually run a plugin](/config-plugins/development-and-debugging/#manually-run-a-plugin)[Modify AndroidManifest.xml](/config-plugins/development-and-debugging/#modify-androidmanifestxml)[Modify Info.plist](/config-plugins/development-and-debugging/#modify-infoplist)[Modify iOS Podfile](/config-plugins/development-and-debugging/#modify-ios-podfile)[Add plugins to pluginHistory](/config-plugins/development-and-debugging/#add-plugins-to-pluginhistory)[Plugin development best practices](/config-plugins/development-and-debugging/#plugin-development-best-practices)[Versioning](/config-plugins/development-and-debugging/#versioning)[Plugin properties](/config-plugins/development-and-debugging/#plugin-properties)[Configure Android app startup](/config-plugins/development-and-debugging/#configure-android-app-startup)[Debug config plugins](/config-plugins/development-and-debugging/#debug-config-plugins)[Introspection](/config-plugins/development-and-debugging/#introspection)[Legacy plugins](/config-plugins/development-and-debugging/#legacy-plugins)[Static modification](/config-plugins/development-and-debugging/#static-modification)[Android Gradle Files](/config-plugins/development-and-debugging/#android-gradle-files)[iOS AppDelegate](/config-plugins/development-and-debugging/#ios-appdelegate)[iOS CocoaPods Podfile](/config-plugins/development-and-debugging/#ios-cocoapods-podfile)[Custom base modifiers](/config-plugins/development-and-debugging/#custom-base-modifiers)[expo install](/config-plugins/development-and-debugging/#expo-install)