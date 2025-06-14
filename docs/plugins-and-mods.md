Plugins and mods - Expo Documentation

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

Plugins and mods
================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/config-plugins/plugins-and-mods.mdx)

Learn about what are plugins and mods when creating a config plugin.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/config-plugins/plugins-and-mods.mdx)

---

Plugins are synchronous functions that accept an [`ExpoConfig`](/versions/latest/config/app) and return a modified [`ExpoConfig`](/versions/latest/config/app).

* Plugins should be named using the following convention: `with<Plugin Functionality>`, for example, `withFacebook`.
* Plugins should be synchronous and their return value should be serializable, except for any `mods` that are added.
* Optionally, a second argument can be passed to the plugin to configure it.
* `plugins` are always invoked when the config is read by the `expo/config` method `getConfig`. However, the `mods` are only invoked during the "syncing" phase of `npx expo prebuild`.

Create a plugin
---------------

Here is an example of the most basic config plugin:

```
const withNothing = config => config;

```

Say you wanted to create a plugin that added custom values to Info.plist in an iOS project:

my-plugin.js

Copy

```
const withMySDK = (config, { apiKey }) => {
  if (!config.ios) {
    config.ios = {};
  }
  if (!config.ios.infoPlist) {
    config.ios.infoPlist = {};
  }

  config.ios.infoPlist['MY_CUSTOM_NATIVE_IOS_API_KEY'] = apiKey;

  return config;
};

module.exports.withMySDK = withMySDK;

```

To use the plugin, import it and wrap the config:

app.config.js

Copy

```
const { withMySDK } = require('./my-plugin');

const config = {
  name: 'my app',
};

module.exports = withMySDK(config, { apiKey: 'X-XXX-XXX' });

```

Import a plugin
---------------

You may want to create a plugin in a different file, here's how:

* The root file can be any JS file or a file named app.plugin.js in the root of a Node module.
* The file should export a function that satisfies the [`ConfigPlugin`](https://github.com/expo/expo-cli/blob/3a0ef962a27525a0fe4b7e5567fb7b3fb18ec786/packages/config-plugins/src/Plugin.types.ts#L76) type.
* Plugins should be transpiled for Node environments ahead of time!
  + They should support the versions of Node that [Expo supports](/get-started/create-a-project) (LTS).
  + No `import/export` keywords, use `module.exports` in the shipped plugin file.
  + Expo only transpiles the user's initial `app.config` file, anything more would require a bundler which would add too many "opinions" for a config file.

Consider the following example that changes the config name:

`app.config.js``Expo config`

`my-plugin.js``Custom Config Plugin file`

my-plugin.js

Copy

```
module.exports = function withPrefixedName(config, prefix) {
  // Modify the config
  config.name = prefix + '-' + config.name;
  // Return the results
  return config;
};

```

app.config.js

Copy

```
{
  "name": "my-app",
  "plugins": [["./my-plugin", "custom"]]
}

```

It evaluates to the following JSON config:

Evaluated config JSON

Copy

```
{
  "name": "custom-my-app",
  "plugins": [["./my-plugin", "custom"]]
}

```

Chain plugins
-------------

Once you add a few plugins, your app.config.js code can become difficult to read and manipulate. To combat this, `expo/config-plugins` provides a `withPlugins` function which can be used to chain plugins together and execute them in order.

app.config.js

Copy

```
/// Create a config
const config = {
  name: 'my app',
};

// â Hard to read
withDelta(withFoo(withBar(config, 'input 1'), 'input 2'), 'input 3');

// â Easy to read
import { withPlugins } from 'expo/config-plugins';

withPlugins(config, [
  [withBar, 'input 1'],
  [withFoo, 'input 2'],
  // When no input is required, you can just pass the method...
  withDelta,
]);

```

To support JSON configs, we also added the `plugins` array which just uses `withPlugins` under the hood.
Here is the same config as above, but even simpler:

app.config.js

Copy

```
export default {
  name: 'my app',
  plugins: [
    [withBar, 'input 1'],
    [withFoo, 'input 2'],
    [withDelta, 'input 3'],
  ],
};

```

What are mods
-------------

A modifier (mod for short) is an async function that accepts a config and a data object, then manipulates and returns both as an object.

Mods are added to the `mods` object of the app config. The `mods` object is different from the rest of the app config because it doesn't get serialized
after the initial reading, which means you can use it to perform actions *during* code generation.
If possible, you should attempt to use basic plugins instead of mods, as they're simpler to work with.

* `mods` are omitted from the manifest and cannot be accessed via `Updates.manifest`. Mods exist for the sole purpose of modifying native project files during code generation!
* `mods` can be used to read and write files safely during the `npx expo prebuild` command. This is how Expo CLI modifies the Info.plist, entitlements, xcproj, and so on.
* `mods` are platform-specific and should always be added to a platform-specific object:

app.config.js

Copy

```
module.exports = {
  name: 'my-app',
  mods: {
    ios: {
      /* iOS mods... */
    },
    android: {
      /* Android mods... */
    },
  },
};

```

How mods work
-------------

* The config is read using [`getPrebuildConfig`](https://github.com/expo/expo-cli/blob/43a6162edd646b550c1b7eae6039daf1aaec4fb0/packages/prebuild-config/src/getPrebuildConfig.ts#L12) from `@expo/prebuild-config`.
* All of the core functionality supported by Expo is added via plugins in `withIosExpoPlugins`. This includes name, version, icons, locales, and so on.
* The config is passed to the compiler `compileModsAsync`
* The compiler adds base mods that are responsible for reading data (like Info.plist), executing a named mod (like `mods.ios.infoPlist`), then writing the results to the file system.
* The compiler iterates over all the mods and asynchronously evaluates them, providing some base props like the `projectRoot`.
  + After each mod, error handling asserts if the mod chain was corrupted by an invalid mod.

### Default mods

The following default mods are provided by the mod compiler for common file manipulation.

> Dangerous modifications rely on regular expressions (regex) to modify application code, which may cause the build to break.
> Regex mods are also difficult to version, and therefore should be used sparingly.
> Always opt towards using application code to modify application code, that is, [Expo Modules](https://github.com/expo/expo/tree/main/packages/expo-modules-core) native API.

| Android mod | Dangerous | Description |
| --- | --- | --- |
| `mods.android.manifest` | - | Modify the android/app/src/main/AndroidManifest.xml as JSON (parsed with [`xml2js`](https://www.npmjs.com/package/xml2js)). |
| `mods.android.strings` | - | Modify the android/app/src/main/res/values/strings.xml as JSON (parsed with [`xml2js`](https://www.npmjs.com/package/xml2js)). |
| `mods.android.colors` | - | Modify the android/app/src/main/res/values/colors.xml as JSON (parsed with [`xml2js`](https://www.npmjs.com/package/xml2js)). |
| `mods.android.colorsNight` | - | Modify the android/app/src/main/res/values-night/colors.xml as JSON (parsed with [`xml2js`](https://www.npmjs.com/package/xml2js)). |
| `mods.android.styles` | - | Modify the android/app/src/main/res/values/styles.xml as JSON (parsed with [`xml2js`](https://www.npmjs.com/package/xml2js)). |
| `mods.android.gradleProperties` | - | Modify the android/gradle.properties as a `Properties.PropertiesItem[]`. |
| `mods.android.mainActivity` |  | Modify the android/app/src/main/<package>/MainActivity.java as a string. |
| `mods.android.mainApplication` |  | Modify the android/app/src/main/<package>/MainApplication.java as a string. |
| `mods.android.appBuildGradle` |  | Modify the android/app/build.gradle as a string. |
| `mods.android.projectBuildGradle` |  | Modify the android/build.gradle as a string. |
| `mods.android.settingsGradle` |  | Modify the android/settings.gradle as a string. |

| iOS mod | Dangerous | Description |
| --- | --- | --- |
| `mods.ios.infoPlist` | - | Modify the ios/<name>/Info.plist as JSON (parsed with [`@expo/plist`](https://www.npmjs.com/package/@expo/plist)). |
| `mods.ios.entitlements` | - | Modify the ios/<name>/<product-name>.entitlements as JSON (parsed with [`@expo/plist`](https://www.npmjs.com/package/@expo/plist)). |
| `mods.ios.expoPlist` | - | Modify the ios/<ame>/Expo.plist as JSON (Expo updates config for iOS) (parsed with [`@expo/plist`](https://www.npmjs.com/package/@expo/plist)). |
| `mods.ios.xcodeproj` | - | Modify the ios/<name>.xcodeproj as an `XcodeProject` object (parsed with [`xcode`](https://www.npmjs.com/package/xcode)). |
| `mods.ios.podfile` | - | Modify the ios/Podfile as a string. |
| `mods.ios.podfileProperties` | - | Modify the ios/Podfile.properties.json as JSON. |
| `mods.ios.appDelegate` |  | Modify the ios/<name>/AppDelegate.m as a string. |

After the mods are resolved, the contents of each mod will be written to disk. Custom default mods can be added to support new native files.
For example, you can create a mod to support the `GoogleServices-Info.plist`, and pass it to other mods.

### Mod plugins

Mods are responsible for a lot of tasks, so they can be pretty difficult to understand at first.
If you're developing a feature that requires mods, it's best not to interact with them directly.

Instead you should use the helper mods provided by `expo/config-plugins`:

#### Android

| Android mod | Mod plugin | Dangerous |
| --- | --- | --- |
| `mods.android.manifest` | `withAndroidManifest` | - |
| `mods.android.strings` | `withStringsXml` | - |
| `mods.android.colors` | `withAndroidColors` | - |
| `mods.android.colorsNight` | `withAndroidColorsNight` | - |
| `mods.android.styles` | `withAndroidStyles` | - |
| `mods.android.gradleProperties` | `withGradleProperties` | - |
| `mods.android.mainActivity` | `withMainActivity` |  |
| `mods.android.mainApplication` | `withMainApplication` |  |
| `mods.android.appBuildGradle` | `withAppBuildGradle` |  |
| `mods.android.projectBuildGradle` | `withProjectBuildGradle` |  |
| `mods.android.settingsGradle` | `withSettingsGradle` |  |

#### iOS

| iOS mod | Mod plugin | Dangerous |
| --- | --- | --- |
| `mods.ios.infoPlist` | `withInfoPlist` | - |
| `mods.ios.entitlements` | `withEntitlementsPlist` | - |
| `mods.ios.expoPlist` | `withExpoPlist` | - |
| `mods.ios.xcodeproj` | `withXcodeProject` | - |
| `mods.ios.podfile` | `withPodfile` | - |
| `mods.ios.podfileProperties` | `withPodfileProperties` | - |
| `mods.ios.appDelegate` | `withAppDelegate` |  |

A mod plugin gets passed a `config` object with additional properties `modResults` and `modRequest` added to it.

* `modResults`: The object to modify and return. The type depends on the mod that's being used.
* `modRequest`: Additional properties supplied by the mod compiler.
  + `projectRoot: string`: Project root directory for the universal app.
  + `platformProjectRoot: string`: Project root for the specific platform.
  + `modName: string`: Name of the mod.
  + `platform: ModPlatform`: Name of the platform used in the mods config.
  + `projectName?: string`: (iOS only) The path component used for querying project files. ex. `projectRoot/ios/[projectName]/`

Create a mod
------------

Say you wanted to write a mod to update the Xcode Project's "product name":

my-config-plugin.ts

Copy

```
import { ConfigPlugin, withXcodeProject, IOSConfig } from 'expo/config-plugins';

const withCustomProductName: ConfigPlugin<string> = (config, customName) => {
  return withXcodeProject(
    config,
    async (
      config
    ) => {
      config.modResults = IOSConfig.Name.setProductName({ name: customName }, config.modResults);
      return config;
    }
  );
};

// ð¡ Usage:

/// Create a config
const config = {
  name: 'my app',
};

/// Use the plugin
export default withCustomProductName(config, 'new_name');

```

### Experimental functionality

Some parts of the mod system aren't fully fleshed out, these parts use `withDangerousMod` to read/write data without a base mod.
These methods essentially act as their own base mod and cannot be extended.
Icons, for example, currently use the dangerous mod to perform a single generation step with no ability to customize the results.

my-config-plugin.js

Copy

```
export const withIcons = config => {
  return withDangerousMod(config, [
    'ios',
    async config => {
      await setIconsAsync(config, config.modRequest.projectRoot);
      return config;
    },
  ]);
};

```

Be careful using `withDangerousMod` as it is subject to change in the future.
The order with which it gets executed is not reliable either.
Currently, dangerous mods run first before all other modifiers, this is because we use dangerous mods internally for large file system refactoring like when the package name changes.

Plugin module resolution
------------------------

The strings passed to the `plugins` array can be resolved in a few different ways.

> Any resolution pattern that isn't specified below is unexpected behavior, and subject to breaking changes.

### Project file

You can quickly create a plugin in your project and use it in your config.

`app.config.js``import "./my-config-plugin"`

`my-config-plugin.js` `Imported from config`

In this example, the config plugin file contains a bare minimum function:

my-config-plugin.js

Copy

```
module.exports = config => config;

```

### app.plugin.js

Sometimes you want your package to export React components and also support a plugin. To do this, multiple entry points need to be used because the transpilation (Babel preset) may be different.
If an app.plugin.js file is present in the root of a Node module's directory, it'll be used instead of the package's `main` file.

`app.config.js``import "expo-splash-screen"`

`node_modules`

â`expo-splash-screen``Node module`

ââ`package.json``"main": "./build/index.js"`

ââ`app.plugin.js` `Entry file for custom plugins`

ââ`build`

âââ`index.js` `Skipped in favor of app.plugin.js`

node\_modules/expo-splash-screen/app.plugin.js

Copy

```
module.exports = config => config;

```

### Node module default file

A config plugin in a node module (without an app.plugin.js) will use the `main` file defined in the package.json.

`app.config.js``import "expo-splash-screen"`

`node_modules`

â`expo-splash-screen``Node module`

ââ`package.json``"main": "./build/index.js"`

ââ`build`

âââ`index.js` `Node resolve to this file`

### Project directory

This is different to how Config Plugins in Node modules work because app.plugin.js won't be resolved by default in a directory. You'll have to manually specify `./my-config-plugin/app.plugin.js` to use it, otherwise index.js in the directory will be used.

`app.config.js``import "./my-config-plugin"`

`my-config-plugin`

â`index.js` `Config Plugin`

â`app.plugin.js` `Skipped outside of a node module`

### Module internals

> Avoid importing module internals.

If a file inside a Node module is directly imported, then the module's root app.plugin.js resolution will be skipped. This is referred to as "reaching inside a package" and is considered bad form.
We support this to make testing, and plugin authoring easier, but we don't expect library authors to expose their plugins like this as a public API.

`app.config.js``import "expo-splash-screen/build/index.js"`

`node_modules`

â`expo-splash-screen`

ââ`package.json``"main": "./build/index.js"`

ââ`app.plugin.js` `Ignored due to direct import`

ââ`build`

âââ`index.js` `expo-splash-screen/build/index.js`

### Raw functions

Expo config objects also support passing functions as-is to the `plugins` array. This is useful for testing, or if you want to use a plugin without creating a file.

app.config.js

Copy

```
const withCustom = (config, props) => config;

const config = {
  plugins: [
    [
      withCustom,
      {
        /* props */
      },
    ],
    withCustom,
  ],
};

```

One caveat to using functions instead of strings is that serialization will replace the function with the function's name. This keeps manifests (kinda like the index.html for your app) working as expected.

Here is what the serialized config would look like:

```
{
  "plugins": [["withCustom", {}], "withCustom"]
}

```

Why app.plugin.js for plugins
-----------------------------

Config resolution searches for a file named app.plugin.js first when a Node module ID is provided as a plugin.
This is because Node environments are often different to Android, iOS, or web JS environments and therefore require different transpilation presets (for example, `module.exports` instead of `import/export`).

Because of this reasoning, the root of a Node module is searched instead of right next to the index.js.
Imagine you had a TypeScript Node module where the transpiled main file was located at build/index.js,
if app config plugin resolution searched for build/app.plugin.js you'd lose the ability to transpile the file differently.

[Previous (Develop - Config plugins)

Introduction](/config-plugins/introduction)[Next (Develop - Config plugins)

Development and debugging](/config-plugins/development-and-debugging)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/config-plugins/plugins-and-mods.mdx)
* Last updated on December 30, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Create a plugin](/config-plugins/plugins-and-mods/#create-a-plugin)[Import a plugin](/config-plugins/plugins-and-mods/#import-a-plugin)[Chain plugins](/config-plugins/plugins-and-mods/#chain-plugins)[What are mods](/config-plugins/plugins-and-mods/#what-are-mods)[How mods work](/config-plugins/plugins-and-mods/#how-mods-work)[Default mods](/config-plugins/plugins-and-mods/#default-mods)[Mod plugins](/config-plugins/plugins-and-mods/#mod-plugins)[Create a mod](/config-plugins/plugins-and-mods/#create-a-mod)[Experimental functionality](/config-plugins/plugins-and-mods/#experimental-functionality)[Plugin module resolution](/config-plugins/plugins-and-mods/#plugin-module-resolution)[Project file](/config-plugins/plugins-and-mods/#project-file)[app.plugin.js](/config-plugins/plugins-and-mods/#apppluginjs)[Node module default file](/config-plugins/plugins-and-mods/#node-module-default-file)[Project directory](/config-plugins/plugins-and-mods/#project-directory)[Module internals](/config-plugins/plugins-and-mods/#module-internals)[Raw functions](/config-plugins/plugins-and-mods/#raw-functions)[Why app.plugin.js for plugins](/config-plugins/plugins-and-mods/#why-apppluginjs-for-plugins)