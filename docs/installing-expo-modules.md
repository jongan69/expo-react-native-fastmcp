Install Expo modules in an existing native project - Expo Documentation

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

[Overview](/brownfield/overview)[Install Expo modules](/brownfield/installing-expo-modules)

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

Install Expo modules in an existing native project
==================================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/brownfield/installing-expo-modules.mdx)

Learn how to prepare your existing native project to install and use Expo modules and the module API.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/brownfield/installing-expo-modules.mdx)

---

> If your project is a greenfield React Native app â primarily built with React Native from the start, then see [Install Expo modules in an existing React Native project](/bare/installing-expo-modules) instead of this guide.

This guide provides the steps to prepare your existing native project to install and use Expo modules and the module API.

Prerequisites
-------------

> The following instructions may not work for all projects. Support for integrating Expo modules into existing projects is still experimental. If you encounter issues, [create an issue on GitHub](https://github.com/expo/expo/issues).

You should have a brownfield native project with React Native installed and configured to render a root view. If you don't have this yet, follow the [Integration with Existing Apps](https://reactnative.dev/docs/integration-with-existing-apps) guide from the React Native documentation and then come back here once you have followed the steps.

Install the `expo` package
--------------------------

Add the `expo` package to your project. Ensure you are using a version of [the `expo` package that is compatible with the React Native version in your project](/versions/latest#each-expo-sdk-version-depends-on-a-react-native-version).

Terminal

Copy

`-Â``npm install expo`

Configuring native apps
-----------------------

### Android app

1

Add the following to the gradle.properties file in the android directory:

android/gradle.properties

|  |  |  |
| --- | --- | --- |
|  | 20 | newArchEnabled=true |
|  | 21 |  |
|  | 22 | hermesEnabled=true |

2

Add the following to the setting.gradle file in the android directory:

android/settings.gradle

|  |  |  |
| --- | --- | --- |
|  | 1 | apply from: new File(["node", "--print", "require.resolve('expo/package.json')"].execute(null, rootDir).text.trim(), "../scripts/autolinking.gradle"); |
|  | 2 | useExpoModules() |
|  | 3 |  |

3

Inside the android directory, run the following command:

Terminal

Copy

`-Â``./gradlew clean`

Once the above command completes, run:

Terminal

Copy

`-Â``./gradlew assembleDebug`

4

(Optional) Complete the following steps if you would like to use [lifecycle listeners](/modules/android-lifecycle-listeners) in your app. If you do not set up lifecycle listeners, then additional setup will be required for each module that uses them.

4.1

If you already have a class that extends the `Application` class you can move to step 3. If you do not have it, we need to create one. Add a file called MainApplication.kt file to your android/app/src/main/java/com/<your-app-package> directory with the following content:

android/app/src/main/java/com/<my-app-package>/MainApplication.kt

|  |  |  |
| --- | --- | --- |
|  | 1 | package <my.app.package> |
|  | 2 |  |
|  | 3 | import android.app.Application |
|  | 4 | import android.content.res.Configuration |
|  | 5 | import com.facebook.soloader.SoLoader |
|  | 6 | import expo.modules.ApplicationLifecycleDispatcher |
|  | 7 |  |
|  | 8 | class MainApplication() : Application() { |
|  | 9 | override fun onCreate() { |
|  | 10 | super.onCreate() |
|  | 11 | ApplicationLifecycleDispatcher.onApplicationCreate(this) |
|  | 12 | } |
|  | 13 |  |
|  | 14 | override fun onConfigurationChanged(newConfig: Configuration) { |
|  | 15 | super.onConfigurationChanged(newConfig) |
|  | 16 | ApplicationLifecycleDispatcher.onConfigurationChanged(this, newConfig) |
|  | 17 | } |
|  | 18 | } |

4.2

Register the class in the AndroidManifest.xml file.

android/app/src/main/AndroidManifest.xml

|  |  |  |
| --- | --- | --- |
| 7 | 7 | <application |
| 8 | 8 | android:allowBackup="true" |
|  | 9 | android:name=".MainApplication" |
| 9 | 10 | android:fullBackupContent="@xml/backup\_rules" |

4.3

If you have your own class extending `Application`, you can add the following. It includes calls to `ApplicationLifecycleDispatcher` for handling events at the application startup and during device configuration changes.

android/app/src/main/java/com/<my-app-package>/MainApplication.kt

|  |  |  |
| --- | --- | --- |
| 0 | 1 | override fun onCreate() { |
| 1 | 2 | super.onCreate() |
|  | 3 | ApplicationLifecycleDispatcher.onApplicationCreate(this) |
| 2 | 4 | } |
|  | 5 |  |
|  | 6 | override fun onConfigurationChanged(newConfig: Configuration) { |
|  | 7 | super.onConfigurationChanged(newConfig) |
|  | 8 | ApplicationLifecycleDispatcher.onConfigurationChanged(this, newConfig) |
|  | 9 | } |

Override `onConfigurationChanged` if you have not done so already.

### iOS app

1

Add the following to your `Podfile` in the ios directory:

ios/Podfile

|  |  |  |
| --- | --- | --- |
|  | 1 | # Expo requires |
|  | 2 | require File.join(File.dirname(`node --print "require.resolve('expo/package.json')"`), "scripts/autolinking") |
|  | 3 |  |
|  |  |  |
| --- | --- | --- |
| 17 |  | config = use\_native\_modules!() |
|  | 20 | # Need to be added inside the target block |
|  | 21 | use\_expo\_modules! |
|  | 22 |  |
|  | 23 | config\_command = [ |
|  | 24 | 'node', |
|  | 25 | '--no-warnings', |
|  | 26 | '--eval', |
|  | 27 | 'require(require.resolve("expo-modules-autolinking", { paths: [require.resolve("expo/package.json")] }))(process.argv.slice(1))', |
|  | 28 | 'react-native-config', |
|  | 29 | '--json', |
|  | 30 | '--platform', |
|  | 31 | 'ios' |
|  | 32 | ] |
|  | 33 | config = use\_native\_modules!(config\_command) |

2

Open your ios directory in Xcode. From the project navigator, select your project and then select your app target under `TARGETS`. In `Build Settings`, using the search bar, search for `ENABLE_USER_SCRIPT_SANDBOXING`. If it is not already, set its value to `No`.

3

Run `pod install` in the ios directory.

Terminal

Copy

`-Â``cd ios && pod install`

You will need to do this every time you add a dependency that uses native code.

4

(Optional) Complete the following if you would like to use [`AppDelegate` subscribers](/modules/appdelegate-subscribers). If you do not set up `AppDelegate` subscribers, then additional setup will be required for each module that uses them.

ios/<MyAppProject>/AppDelegate.swift

|  |  |  |
| --- | --- | --- |
|  | 1 | import ExpoModulesCore |
| 1 |  | class AppDelegate: UIResponder, UIApplicationDelegate { |
|  | 2 | class AppDelegate: ExpoAppDelegate { |
| 2 |  | func application(\_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool { |
|  | 3 | override func application(\_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool { |
| 3 |  | return true |
|  | 4 | super.application(application, didFinishLaunchingWithOptions: launchOptions) |

[Previous (Development process - Existing native apps)

Overview](/brownfield/overview)[Next (Development process - Reference)

Work with monorepos](/guides/monorepos)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/brownfield/installing-expo-modules.mdx)
* Last updated on April 09, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Prerequisites](/brownfield/installing-expo-modules/#prerequisites)[Install the expo package](/brownfield/installing-expo-modules/#install-the-expo-package)[Configuring native apps](/brownfield/installing-expo-modules/#configuring-native-apps)[Android app](/brownfield/installing-expo-modules/#android-app)[iOS app](/brownfield/installing-expo-modules/#ios-app)