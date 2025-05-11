Tutorial: Creating a native module - Expo Documentation

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

Tutorial: Creating a native module
==================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/modules/native-module-tutorial.mdx)

A tutorial on creating a native module that persists settings with Expo Modules API.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/modules/native-module-tutorial.mdx)

---

In this tutorial, you build a module that stores the user's preferred app theme: dark, light, or system. On Android, use [`SharedPreferences`](https://developer.android.com/reference/android/content/SharedPreferences), and on iOS, use [`UserDefaults`](https://developer.apple.com/documentation/foundation/userdefaults). You can implement web support with [`localStorage`](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage), but this tutorial does not cover that.

[![Watch: How to create a native module with the Expo Modules API](https://i3.ytimg.com/vi/CdaQSlyGik8/maxresdefault.jpg)

Watch: How to create a native module with the Expo Modules API](https://www.youtube.com/watch?v=CdaQSlyGik8)


---

1

Initialize a new module
-----------------------

First, create a new module. For this tutorial, the module is named `expo-settings` or `ExpoSettings`. You can choose a different name, but adjust the instructions to match your choice.

Terminal

Copy

`-Â``npx create-expo-module expo-settings`

> Since you aren't going to actually ship this library, you can hit `return` for all the prompts to accept the default values.

2

Set up workspace
----------------

Clean up the default module to start with a clean slate. Delete the view module since this guide does not use it.

Terminal

Copy

`-Â``cd expo-settings`

`-Â``rm ios/ExpoSettingsView.swift`

`-Â``rm android/src/main/java/expo/modules/settings/ExpoSettingsView.kt`

`-Â``rm src/ExpoSettingsView.tsx src/ExpoSettings.types.ts`

`-Â``rm src/ExpoSettingsView.web.tsx src/ExpoSettingsModule.web.ts`

Locate the following files and replace their contents with the provided minimal boilerplate:

ios/ExpoSettingsModule.swift

Copy

```
import ExpoModulesCore

public class ExpoSettingsModule: Module {
  public func definition() -> ModuleDefinition {
    Name("ExpoSettings")

    Function("getTheme") { () -> String in
      "system"
    }
  }
}

```

android/src/main/java/expo/modules/settings/ExpoSettingsModule.kt

Copy

```
package expo.modules.settings

import expo.modules.kotlin.modules.Module
import expo.modules.kotlin.modules.ModuleDefinition

class ExpoSettingsModule : Module() {
  override fun definition() = ModuleDefinition {
    Name("ExpoSettings")

    Function("getTheme") {
      return@Function "system"
    }
  }
}

```

src/index.ts

Copy

```
import ExpoSettingsModule from './ExpoSettingsModule';

export function getTheme(): string {
  return ExpoSettingsModule.getTheme();
}

```

example/App.tsx

Copy

```
import * as Settings from 'expo-settings';
import { Text, View } from 'react-native';

export default function App() {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Theme: {Settings.getTheme()}</Text>
    </View>
  );
}

```

3

Run the example project
-----------------------

Start the TypeScript compiler to watch for changes.

Terminal

Copy

`# Run this in the root of the project to start the TypeScript compiler`

`-Â``npm run build`

In a separate terminal window, run the example app.

Terminal

Copy

`-Â``cd example`

`# Run the example app on Android`

`-Â``npx expo run:android`

`# Run the example app on iOS`

`-Â``npx expo run:ios`

You should see the text "Theme: system" in the center of the screen when you launch the example app. The value `"system"` comes from synchronously calling the `getTheme()` function in the native module. You will change this value in the next step.

4

Get, set, and persist the theme preference value
------------------------------------------------

### Android native module

To read the value, look for a `SharedPreferences` string under the key `"theme"`. If the key does not exist, default to `"system"`. Use the `reactContext` (a React Native [ContextWrapper](https://developer.android.com/reference/android/content/ContextWrapper)) to access the `SharedPreferences` instance with `getSharedPreferences()`.

To set the value, use the `edit()` method of `SharedPreferences` to get an `Editor` instance. Then, use `putString()` to set the value. Ensure the `setTheme` function accepts a value of type `String`.

android/src/main/java/expo/modules/settings/ExpoSettingsModule.kt

Copy

```
package expo.modules.settings

import android.content.Context
import android.content.SharedPreferences
import expo.modules.kotlin.modules.Module
import expo.modules.kotlin.modules.ModuleDefinition

class ExpoSettingsModule : Module() {
  override fun definition() = ModuleDefinition {
    Name("ExpoSettings")

    Function("setTheme") { theme: String ->
      getPreferences().edit().putString("theme", theme).commit()
    }

    Function("getTheme") {
      return@Function getPreferences().getString("theme", "system")
    }
  }

  private val context
  get() = requireNotNull(appContext.reactContext)

  private fun getPreferences(): SharedPreferences {
    return context.getSharedPreferences(context.packageName + ".settings", Context.MODE_PRIVATE)
  }
}

```

### iOS native module

To read the value on iOS, look for a `UserDefaults` string under the key `"theme"`. If the key does not exist, default to `"system"`.

To set the value, use the `set(_:forKey:)` method of `UserDefaults`. Ensure the `setTheme` function accepts a value of type `String`.

ios/ExpoSettingsModule.swift

Copy

```
import ExpoModulesCore

public class ExpoSettingsModule: Module {
  public func definition() -> ModuleDefinition {
    Name("ExpoSettings")

    Function("setTheme") { (theme: String) -> Void in
      UserDefaults.standard.set(theme, forKey:"theme")
    }

    Function("getTheme") { () -> String in
      UserDefaults.standard.string(forKey: "theme") ?? "system"
    }
  }
}

```

### TypeScript module

Now, call your native modules from TypeScript.

src/index.ts

Copy

```
import ExpoSettingsModule from './ExpoSettingsModule';

export function getTheme(): string {
  return ExpoSettingsModule.getTheme();
}

export function setTheme(theme: string): void {
  return ExpoSettingsModule.setTheme(theme);
}

```

### Example app

You can now use the Settings API in your example app.

example/App.tsx

Copy

```
import * as Settings from 'expo-settings';
import { Button, Text, View } from 'react-native';

export default function App() {
  const theme = Settings.getTheme();
  // Toggle between dark and light theme
  const nextTheme = theme === 'dark' ? 'light' : 'dark';

  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Theme: {Settings.getTheme()}</Text>
      <Button title={`Set theme to ${nextTheme}`} onPress={() => Settings.setTheme(nextTheme)} />
    </View>
  );
}

```

When you rebuild and run the app, the "system" theme is still set. Pressing the button does nothing, but when you reload the app, the theme changes. This happens because the app does not fetch the new theme value or re-render. You will fix this in the next step.

5

Emit change events for the theme value
--------------------------------------

Ensure developers using your API can react to theme value changes by emitting a change event whenever the value updates. Use the [Events](/modules/module-api#events) definition component to describe the events your module emits, `sendEvent` to emit the event from native code, and the [EventEmitter](/modules/module-api#sending-events) API to subscribe to events in JavaScript. The event payload is `{ theme: string }`.

### Android native module

Events payloads are represented as [`Bundle`](https://developer.android.com/reference/android/os/Bundle.html) instances on Android, which you can create using the [`bundleOf`](https://developer.android.com/reference/kotlin/androidx/core/os/package-summary#bundleOf(kotlin.Array)) function.

android/src/main/java/expo/modules/settings/ExpoSettingsModule.kt

Copy

```
package expo.modules.settings

import android.content.Context
import android.content.SharedPreferences
import androidx.core.os.bundleOf
import expo.modules.kotlin.modules.Module
import expo.modules.kotlin.modules.ModuleDefinition

class ExpoSettingsModule : Module() {
  override fun definition() = ModuleDefinition {
    Name("ExpoSettings")

    Events("onChangeTheme")

    Function("setTheme") { theme: String ->
      getPreferences().edit().putString("theme", theme).commit()
      this@ExpoSettingsModule.sendEvent("onChangeTheme", bundleOf("theme" to theme))
    }

    Function("getTheme") {
      return@Function getPreferences().getString("theme", "system")
    }
  }

  private val context
  get() = requireNotNull(appContext.reactContext)

  private fun getPreferences(): SharedPreferences {
    return context.getSharedPreferences(context.packageName + ".settings", Context.MODE_PRIVATE)
  }
}

```

### iOS native module

ios/ExpoSettingsModule.swift

Copy

```
import ExpoModulesCore

public class ExpoSettingsModule: Module {
  public func definition() -> ModuleDefinition {
    Name("ExpoSettings")

    Events("onChangeTheme")

    Function("setTheme") { (theme: String) -> Void in
      UserDefaults.standard.set(theme, forKey:"theme")
      sendEvent("onChangeTheme", [
        "theme": theme
      ])
    }

    Function("getTheme") { () -> String in
      UserDefaults.standard.string(forKey: "theme") ?? "system"
    }
  }
}

```

### TypeScript module

src/index.ts

Copy

```
import { EventSubscription } from 'expo-modules-core';
import ExpoSettingsModule from './ExpoSettingsModule';

export type ThemeChangeEvent = {
  theme: string;
};

export function addThemeListener(listener: (event: ThemeChangeEvent) => void): EventSubscription {
  return ExpoSettingsModule.addListener('onChangeTheme', listener);
}

export function getTheme(): string {
  return ExpoSettingsModule.getTheme();
}

export function setTheme(theme: string): void {
  return ExpoSettingsModule.setTheme(theme);
}

```

### Example app

example/App.tsx

Copy

```
import * as Settings from 'expo-settings';
import { useEffect, useState } from 'react';
import { Button, Text, View } from 'react-native';

export default function App() {
  const [theme, setTheme] = useState<string>(Settings.getTheme());

  useEffect(() => {
    const subscription = Settings.addThemeListener(({ theme: newTheme }) => {
      setTheme(newTheme);
    });

    return () => subscription.remove();
  }, [setTheme]);

  // Toggle between dark and light theme
  const nextTheme = theme === 'dark' ? 'light' : 'dark';

  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Theme: {Settings.getTheme()}</Text>
      <Button title={`Set theme to ${nextTheme}`} onPress={() => Settings.setTheme(nextTheme)} />
    </View>
  );
}

```

6

Improve type safety with Enums
------------------------------

It's easy to make mistakes when using the `Settings.setTheme()` API in its current form, as it allows any string value. Improve the type safety of this API by using an enum to restrict the possible values to `system`, `light`, and `dark`.

### Android native module

android/src/main/java/expo/modules/settings/ExpoSettingsModule.kt

Copy

```
package expo.modules.settings

import android.content.Context
import android.content.SharedPreferences
import androidx.core.os.bundleOf
import expo.modules.kotlin.modules.Module
import expo.modules.kotlin.modules.ModuleDefinition
import expo.modules.kotlin.types.Enumerable

class ExpoSettingsModule : Module() {
  override fun definition() = ModuleDefinition {
    Name("ExpoSettings")

    Events("onChangeTheme")

    Function("setTheme") { theme: Theme ->
      getPreferences().edit().putString("theme", theme.value).commit()
      this@ExpoSettingsModule.sendEvent("onChangeTheme", bundleOf("theme" to theme.value))
    }

    Function("getTheme") {
      return@Function getPreferences().getString("theme", Theme.SYSTEM.value)
    }
  }

  private val context
  get() = requireNotNull(appContext.reactContext)

  private fun getPreferences(): SharedPreferences {
    return context.getSharedPreferences(context.packageName + ".settings", Context.MODE_PRIVATE)
  }
}

enum class Theme(val value: String) : Enumerable {
  LIGHT("light"),
  DARK("dark"),
  SYSTEM("system")
}

```

### iOS native module

ios/ExpoSettingsModule.swift

Copy

```
import ExpoModulesCore

public class ExpoSettingsModule: Module {
  public func definition() -> ModuleDefinition {
    Name("ExpoSettings")

    Events("onChangeTheme")

    Function("setTheme") { (theme: Theme) -> Void in
      UserDefaults.standard.set(theme.rawValue, forKey:"theme")
      sendEvent("onChangeTheme", [
        "theme": theme.rawValue
      ])
    }

    Function("getTheme") { () -> String in
      UserDefaults.standard.string(forKey: "theme") ?? Theme.system.rawValue
    }
  }

  enum Theme: String, Enumerable {
    case light
    case dark
    case system
  }
}

```

### TypeScript module

src/index.ts

Copy

```
import { EventSubscription } from 'expo-modules-core';

import ExpoSettingsModule from './ExpoSettingsModule';

export type Theme = 'light' | 'dark' | 'system';

export type ThemeChangeEvent = {
  theme: Theme;
};

export function addThemeListener(listener: (event: ThemeChangeEvent) => void): EventSubscription {
  return ExpoSettingsModule.addListener('onChangeTheme', listener);
}

export function getTheme(): Theme {
  return ExpoSettingsModule.getTheme();
}

export function setTheme(theme: Theme): void {
  return ExpoSettingsModule.setTheme(theme);
}

```

### Example app

If you change `Settings.setTheme(nextTheme)` to `Settings.setTheme("not-a-real-theme")`, TypeScript will raise an error. If you ignore the error and press the button, you will see the following runtime error:

```
 ERROR  Error: FunctionCallException: Calling the 'setTheme' function has failed (at ExpoModulesCore/SyncFunctionComponent.swift:76)
â Caused by: ArgumentCastException: Argument at index '0' couldn't be cast to type Enum<Theme> (at ExpoModulesCore/JavaScriptUtils.swift:41)
â Caused by: EnumNoSuchValueException: 'not-a-real-theme' is not present in Theme enum, it must be one of: 'light', 'dark', 'system' (at ExpoModulesCore/Enumerable.swift:37)

```

The last line of the error message shows that `not-a-real-theme` is not a valid value for the `Theme` enum. The only valid values are `light`, `dark`, and `system`.

Congratulations! You have created your first Expo Module for Android and iOS.

Next steps
----------

[Expo Modules API Reference

Create native modules using Kotlin and Swift.](/modules/module-api)
[Tutorial: Creating a native view

A tutorial on creating a native view with Expo Modules API.](/modules/native-view-tutorial)

[Previous (Expo Modules API)

Get started](/modules/get-started)[Next (Expo Modules API - Tutorials)

Create a native view](/modules/native-view-tutorial)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/modules/native-module-tutorial.mdx)
* Last updated on April 07, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Initialize a new module](/modules/native-module-tutorial/#initialize-a-new-module)[Set up workspace](/modules/native-module-tutorial/#set-up-workspace)[Run the example project](/modules/native-module-tutorial/#run-the-example-project)[Get, set, and persist the theme preference value](/modules/native-module-tutorial/#get-set-and-persist-the-theme-preference-value)[Android native module](/modules/native-module-tutorial/#android-native-module)[iOS native module](/modules/native-module-tutorial/#ios-native-module)[TypeScript module](/modules/native-module-tutorial/#typescript-module)[Example app](/modules/native-module-tutorial/#example-app)[Emit change events for the theme value](/modules/native-module-tutorial/#emit-change-events-for-the-theme-value)[Android native module](/modules/native-module-tutorial/#android-native-module-1)[iOS native module](/modules/native-module-tutorial/#ios-native-module-1)[TypeScript module](/modules/native-module-tutorial/#typescript-module-1)[Example app](/modules/native-module-tutorial/#example-app-1)[Improve type safety with Enums](/modules/native-module-tutorial/#improve-type-safety-with-enums)[Android native module](/modules/native-module-tutorial/#android-native-module-2)[iOS native module](/modules/native-module-tutorial/#ios-native-module-2)[TypeScript module](/modules/native-module-tutorial/#typescript-module-2)[Example app](/modules/native-module-tutorial/#example-app-2)[Next steps](/modules/native-module-tutorial/#next-steps)