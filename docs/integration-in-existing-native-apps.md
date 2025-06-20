Using EAS Update in an existing native app - Expo Documentation

[Docs](/)

[Blog](https://expo.dev/blog)[Changelog](https://expo.dev/changelog)[Star Us on GitHub](https://github.com/expo/expo)

Search

[Home](/)[Guides](/guides/overview)[EAS](/eas)[Reference](/versions/latest)[Learn](/tutorial/overview)

[Introduction](/eas)[Configuration with eas.json](/eas/json)[Environment variables](/eas/environment-variables)

EAS Workflows

[Get started](/eas/workflows/get-started)[Example CI/CD workflows](/eas/workflows/examples)[Syntax for EAS Workflows](/eas/workflows/syntax)[Automating EAS CLI commands](/eas/workflows/automating-eas-cli)

Reference

EAS Build

[Introduction](/build/introduction)[Create your first build](/build/setup)[Configure with eas.json](/build/eas-json)[Internal distribution](/build/internal-distribution)[Automate submissions](/build/automate-submissions)[Using EAS Update](/build/updates)[Trigger builds from CI](/build/building-on-ci)[Trigger builds from GitHub App](/build/building-from-github)[Expo Orbit](/build/orbit)

App signing

Custom builds

Reference

EAS Hosting

[Introduction](/eas/hosting/introduction)[Get started](/eas/hosting/get-started)[Deployments and aliases](/eas/hosting/deployments-and-aliases)[Environment variables](/eas/hosting/environment-variables)[Custom domain](/eas/hosting/custom-domain)[Monitoring API routes](/eas/hosting/api-routes)[Workflows](/eas/hosting/workflows)

Reference

EAS Submit

[Introduction](/submit/introduction)[Submit to the Google Play Store](/submit/android)[Submit to the Apple App Store](/submit/ios)[Configure with eas.json](/submit/eas-json)

EAS Update

[Introduction](/eas-update/introduction)[Get started](/eas-update/getting-started)

Preview

Deployment

Concepts

Troubleshooting

Reference

[Code signing](/eas-update/code-signing)[Asset selection and exclusion](/eas-update/asset-selection)[Using without other EAS services](/eas-update/standalone-service)[Migrate from CodePush](/eas-update/codepush)[Migrate from Classic Updates](/eas-update/migrate-from-classic-updates)[Trace update ID back to the Expo Dashboard](/eas-update/trace-update-id-expo-dashboard)[Estimate bandwidth usage](/eas-update/estimate-bandwidth)[Integrate in existing native apps](/eas-update/integration-in-existing-native-apps)[FAQ](/eas-update/faq)

EAS Metadata

[Introduction](/eas/metadata)[Get started](/eas/metadata/getting-started)

Reference

EAS Insights

[Introduction](/eas-insights/introduction)

Distribution

[Overview](/distribution/introduction)[App stores best practices](/distribution/app-stores)[App transfers](/distribution/app-transfers)[Understanding app size](/distribution/app-size)

Reference

[Webhooks](/eas/webhooks)

Expo accounts

Billing

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Using EAS Update in an existing native app
==========================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/integration-in-existing-native-apps.mdx)

Learn how to integrate EAS Update into your existing native Android and iOS app to enable over-the-air updates.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/integration-in-existing-native-apps.mdx)

---

> If your project is a greenfield React Native app â primarily built with React Native from the start, and the entry point of the app is React Native, then skip this guide and proceed to [Get started with EAS Update](/eas-update/getting-started).

This guide explains how to integrate EAS Update in an existing native app, sometimes referred to as a brownfield app. It assumes that you are using Expo SDK 52 or later, and React Native 0.76 or later.

Instructions are not available for older Expo SDK and React Native versions. Additional hands-on support for integrating with older versions can only be provided for enterprise customers ([contact us](https://expo.dev/contact)).

Prerequisites
-------------

> The following instructions may not work for all projects. The specifics of integrating EAS Update into existing projects depend heavily on the specifics of your app, and so you may need to adapt the instructions to your unique setup. If you encounter issues, [create an issue on GitHub](https://github.com/expo/expo/issues) or open a pull request to suggest improvements to this guide.

You should have a brownfield native project with React Native installed and configured to render a root view. If you don't have this yet, follow the [Integration with Existing Apps](https://reactnative.dev/docs/integration-with-existing-apps) guide from the React Native documentation and then come back here once you have followed the steps.

* Your app must be using the [latest Expo SDK version and its supported React Native version](/versions/latest#each-expo-sdk-version-depends-on-a-react-native-version).
* Remove any other update library integration from your app, such as react-native-code-push, and ensure that your app compiles and runs successfully in both debug and release on your supported platforms.
* Support for Expo modules (through the `expo` package) must be installed and configured in your project. [Learn more](/brownfield/installing-expo-modules).
* Your metro.config.js [must extend `expo/metro-config`](/guides/customizing-metro#customizing) .
* Your babel.config.js [must extend `babel-preset-expo`](/versions/latest/config/babel).
* The command `npx expo export -p android` must run successfully in your project if it supports Android, and `npx expo export -p ios` if it supports iOS.

Installation and basic configuration
------------------------------------

Follow steps 1, 2, 3, and 4 from the [Get started with EAS Update](/eas-update/getting-started) guide.

After this is complete, you will have installed and authenticated with `eas-cli`, installed `expo-updates` to your project, initialized an associated EAS project, and added basic configuration to your native projects.

Opt out of automatic setup
--------------------------

The next step is to disable the default behavior of `expo-updates` to automatically set itself up in a way that supports greenfield React Native projects.

### Disable automatic setup on Android

Modify android/settings.gradle to set the property that disables automatic updates initialization, as in the example below:

### Disable automatic setup on iOS

Pass in the environment variable to CocoaPods installation to disable automatic updates initialization.

Terminal

Copy

`-Â``EX_UPDATES_CUSTOM_INIT=1 npx pod-install`

Set up your React Native app to use expo-updates for loading the release bundle
-------------------------------------------------------------------------------

The next step is to integrate `expo-updates` into your Android and iOS projects so that your app will use `expo-updates` as the source of your app JavaScript in release builds.

Example

A complete working example is available at [this GitHub repository](https://github.com/expo/CustomRNView) .

### Integrating expo-updates with your React Native bundling

1. Ensure that your Metro config extends the Expo config, as in this example:

   metro.config.js

   Copy

   ```
   // Learn more https://docs.expo.io/guides/customizing-metro
   const { getDefaultConfig } = require('expo/metro-config');

   /** @type {import('expo/metro-config').MetroConfig} */
   const config = getDefaultConfig(__dirname); // eslint-disable-line no-undef

   // Make any custom changes you need for your project by
   // directly modifying "config"

   module.exports = config;

   ```
2. If you are using a custom entry point, be sure to include Expo initialization there. This ensures that Expo libraries (including `expo-updates`) are all initialized properly. Here are two examples:

   First Custom Entry Point file example

   Copy

   ```
   // Expo recommends using registerRootComponent().
   // It registers the component with the react-native AppRegistry,
   // and performs all required Expo initialization
   // (including expo-updates setup)

   import App from './App';
   import { registerRootComponent } from 'expo';

   registerRootComponent(App);

   ```

   Second custom entry point file example

   Copy

   ```
   // If you need to keep an existing entry point that uses AppRegistry directly,
   // you will need to add a call to Expo's initialization before registering the
   // app, as shown below.
   import App from './App';
   import 'expo/src/Expo.fx';
   import { AppRegistry } from 'react-native';

   function getApp() {
     return <App />;
   }

   AppRegistry.registerComponent('App', () => getApp());

   ```

### Integrating expo-updates on Android

The following instructions assume you have an app written in Kotlin, with one or more native activities. Open android/app/src/main/java/com/<your-app-name>/MainActivity.kt and follow the steps below.

1. Your React Native activity should subclass `com.facebook.react.ReactActivity`.
2. In this activity, add code to `onCreate()` to initialize the updates system. The initialization should not happen in the main thread (otherwise a lockup and ANR will occur).
3. Override `getMainComponentName()` to return the name of the app you registered in your JS entry point above.
4. Show the React Native view, by overriding the `createReactActivityDelegate()` method as shown below.

android/app/src/main/java/com/<your-app-name>/MainActivity.kt

Copy

```
package com.yourpackagename

import android.content.Context
import android.os.Bundle
import com.facebook.react.ReactActivity
import com.facebook.react.ReactActivityDelegate
import com.facebook.react.defaults.DefaultNewArchitectureEntryPoint.fabricEnabled
import com.facebook.react.defaults.DefaultReactActivityDelegate
import expo.modules.ReactActivityDelegateWrapper
import expo.modules.updates.UpdatesController
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch

// Step 1
class MainActivity : ReactActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        CoroutineScope(Dispatchers.IO).launch {
            startUpdatesController(applicationContext)
        }
    }

    // Step 2
    private fun startUpdatesController(context: Context) {
        UpdatesController.initialize(context)
        // Call the synchronous `launchAssetFile()` function to wait for updates ready
        UpdatesController.instance.launchAssetFile
    }

    // Step 3
    override fun getMainComponentName(): String = "App"

    // Step 4
    override fun createReactActivityDelegate(): ReactActivityDelegate {
        return ReactActivityDelegateWrapper(
            this,
            BuildConfig.IS_NEW_ARCHITECTURE_ENABLED,
            object : DefaultReactActivityDelegate(
                this,
                mainComponentName,
                fabricEnabled
            ) {})
    }
}

```

### Integrating expo-updates on iOS

The following instructions assume you have an app written in Swift, with one or more native screens that have custom UIViewControllers. We will add a custom view controller that renders your React Native app.

SDK 53 and above

SDK 52

#### AppDelegate changes

1. Modify AppDelegate.swift so that it extends `ExpoAppDelegate`.
2. If you are not already doing so, add a public method to get the running `AppDelegate` instance, so that your custom view controller can access it later.
3. Add a reference to the singleton instance of the `expo-updates` `AppController` class, which manages the updates system on iOS.
4. Add a new class, `CustomReactNativeFactoryDelegate`, that extends `ExpoReactNativeFactoryDelegate` and overrides the `bundleUrl()` method to return the correct bundle URL for updates, if the updates system is running.
5. The `didFinishLaunchingWithOptions()` method needs to perform two steps:
   1. Initialize the `ExpoReactNativeFactory` using the `CustomReactNativeFactoryDelegate` created above. This will be used later to create the React Native root view.
   2. Call `AppController.initializeWithoutStarting()`. This creates the controller instance, but defers the rest of the updates startup procedure until it is needed.

ios/<your-app-name>/AppDelegate.swift

Copy

```
import Expo
import EXUpdates
import React
import ReactAppDependencyProvider
import UIKit

@UIApplicationMain
// Step 1
class AppDelegate: ExpoAppDelegate {
  var launchOptions: [UIApplication.LaunchOptionsKey: Any]?

  // Step 2
  public static func shared() -> AppDelegate {
    guard let delegate = UIApplication.shared.delegate as? AppDelegate else {
      fatalError("Could not get app delegate")
    }
    return delegate
  }

  // Step 3
  var updatesController: (any InternalAppControllerInterface)?

  // Step 5
  private func initializeReactNativeAndUpdates(_ launchOptions: [UIApplication.LaunchOptionsKey: Any]?) {
    // Step 5.1
    self.launchOptions = launchOptions
    let delegate = CustomReactNativeFactoryDelegate()
    let factory = ExpoReactNativeFactory(delegate: delegate)
    delegate.dependencyProvider = RCTAppDependencyProvider()

    reactNativeFactoryDelegate = delegate
    reactNativeFactory = factory
    // Step 5.2
    AppController.initializeWithoutStarting()
  }

  /**
   Application launch initializes the custom view controller: all React Native
   and updates initialization is handled there
   */
  override func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil
  ) -> Bool {
    initializeReactNativeAndUpdates(launchOptions)

    // Create custom view controller, where the React Native view will be created
    self.window = UIWindow(frame: UIScreen.main.bounds)
    let controller = CustomViewController()
    controller.view.clipsToBounds = true
    self.window?.rootViewController = controller
    window?.makeKeyAndVisible()

    return true
  }

  override func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey: Any] = [:]) -> Bool {
    return super.application(app, open: url, options: options) ||
      RCTLinkingManager.application(app, open: url, options: options)
  }
}

// Step 4
class CustomReactNativeFactoryDelegate: ExpoReactNativeFactoryDelegate {
  let bundledUrl = Bundle.main.url(forResource: "main", withExtension: "jsbundle")
  override func sourceURL(for bridge: RCTBridge) -> URL? {
    // needed to return the correct URL for expo-dev-client.
    bridge.bundleURL ?? bundleURL()
  }

  override func bundleURL() -> URL? {
    if let updatesUrl = AppDelegate.shared().updatesController?.launchAssetUrl() {
      return updatesUrl
    }
    return bundledUrl
  }
}

```

#### Implementing a custom view controller

1. The view controller should implement the updates protocol `AppControllerDelegate`.
2. The view controller initialization should
   1. Set the app delegate's updates controller instance, so that its `bundleURL()` method above works correctly for updates.
   2. Set the `AppController` delegate to the view controller instance
   3. Start the `AppController`
3. Finally, the view controller must implement the one method in the `AppControllerDelegate` protocol, `appController(_ appController: AppControllerInterface, didStartWithSuccess success: Bool)`. This method will be called once the updates system is fully initialized, and the latest update (or the embedded bundle) is ready to be rendered.
   1. Create the React Native root view using the `ExpoReactNativeFactory` created by the app delegate. The app name passed in must match the app name that you registered in your JS entry point above.
   2. Add this root view to the view controller.

ios/<your-app-name>/CustomViewController.swift

Copy

```
import UIKit
import EXUpdates
import ExpoModulesCore


/**
 Custom view controller that handles React Native and expo-updates initialization
 */
// Step 1
public class CustomViewController: UIViewController, AppControllerDelegate {
  let appDelegate = AppDelegate.shared()

  // Step 2
  public convenience init() {
    self.init(nibName: nil, bundle: nil)
    self.view.backgroundColor = .clear
    // Step 2.1
    appDelegate.updatesController = AppController.sharedInstance
    // Step 2.2
    AppController.sharedInstance.delegate = self
    // Step 2.3
    AppController.sharedInstance.start()
  }

  required public override init(nibName nibNameOrNil: String?, bundle nibBundleOrNil: Bundle?) {
    super.init(nibName: nibNameOrNil, bundle: nibBundleOrNil)
  }

  @available(*, unavailable)
  required public init?(coder aDecoder: NSCoder) {
    fatalError("init(coder:) has not been implemented")
  }

  // Step 3
  public func appController(
    _ appController: AppControllerInterface,
    didStartWithSuccess success: Bool
  ) {
    createView()
  }

  private func createView() {
    // Step 3.1
    guard let rootViewFactory: RCTRootViewFactory = appDelegate.reactNativeFactory?.rootViewFactory else {
      fatalError("rootViewFactory has not been initialized")
    }
    let rootView = rootViewFactory.view(
      withModuleName: "main",
      initialProperties: [:],
      launchOptions: appDelegate.launchOptions
    )
    // Step 3.2
    let controller = self
    controller.view.clipsToBounds = true
    controller.view.addSubview(rootView)
    rootView.translatesAutoresizingMaskIntoConstraints = false
    NSLayoutConstraint.activate([
      rootView.topAnchor.constraint(equalTo: controller.view.safeAreaLayoutGuide.topAnchor),
      rootView.bottomAnchor.constraint(equalTo: controller.view.safeAreaLayoutGuide.bottomAnchor),
      rootView.leadingAnchor.constraint(equalTo: controller.view.safeAreaLayoutGuide.leadingAnchor),
      rootView.trailingAnchor.constraint(equalTo: controller.view.safeAreaLayoutGuide.trailingAnchor)
    ])
  }
}

```

#### AppDelegate changes

1. Modify AppDelegate.swift so that it extends `EXAppDelegateWrapper`.
2. If you are not already doing so, add a public method to get the running `AppDelegate` instance, so that your custom view controller can access it later.
3. Add a reference to the singleton instance of the `expo-updates` `AppController` class, which manages the updates system on iOS.
4. Override the `bundleUrl()` method to return the correct bundle URL for updates, if the updates system is running.
5. The `didFinishLaunchingWithOptions()` method needs to perform two steps:
   1. Initialize the root view factory used later to create the React Native root view.
   2. Call `AppController.initializeWithoutStarting()` . This creates the controller instance, but defers the rest of the updates startup procedure until it is needed.

ios/<your-app-name>/AppDelegate.swift

Copy

```
import ExpoModulesCore
import EXUpdates
import React
import UIKit

@UIApplicationMain
// Step 1
class AppDelegate: EXAppDelegateWrapper {
  let bundledUrl = Bundle.main.url(forResource: "main", withExtension: "jsbundle")
  var launchOptions: [UIApplication.LaunchOptionsKey: Any]?

  // Step 2
  public static func shared() -> AppDelegate {
    guard let delegate = UIApplication.shared.delegate as? AppDelegate else {
      fatalError("Could not get app delegate")
    }
    return delegate
  }

  // Step 3
  var updatesController: (any InternalAppControllerInterface)?

  // Step 4
  override func bundleURL() -> URL? {
    if let updatesUrl = updatesController?.launchAssetUrl() {
      return updatesUrl
    }
    return bundledUrl
  }

  // Step 5
  private func initializeReactNativeAndUpdates(_ launchOptions: [UIApplication.LaunchOptionsKey: Any]?) {
    // Step 5.1
    self.launchOptions = launchOptions
    self.moduleName = "App"
    self.initialProps = [:]
    self.rootViewFactory = createRCTRootViewFactory()
    // Step 5.2
    AppController.initializeWithoutStarting()
  }

  /**
   * Application launch initializes the custom view controller; all React Native
   * and updates initialization is handled there
   */
  override func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil
  ) -> Bool {

    initializeReactNativeAndUpdates(launchOptions)

    // Create custom view controller, where the React Native view will be created
    self.window = UIWindow(frame: UIScreen.main.bounds)
    let controller = CustomViewController()
    controller.view.clipsToBounds = true
    self.window.rootViewController = controller
    window.makeKeyAndVisible()
    return true
  }
}

```

#### Implementing a custom view controller

1. The view controller should implement the updates protocol `AppControllerDelegate`.
2. The view controller initialization should
   1. Set the app delegate's updates controller instance, so that its `bundleURL()` method above works correctly for updates.
   2. Set the `AppController` delegate to the view controller instance
   3. Start the `AppController`
3. Finally, the view controller must implement the one method in the `AppControllerDelegate` protocol, `appController(_ appController: AppControllerInterface, didStartWithSuccess success: Bool)`. This method will be called once the updates system is fully initialized, and the latest update (or the embedded bundle) is ready to be rendered.
   1. Create the React Native root view using the root view factory created by the app delegate. The app name passed in must match the app name that you registered in your JS entry point above.
   2. Add this root view to the view controller.

ios/<your-app-name>/CustomViewController.swift

Copy

```
import UIKit
import EXUpdates
import ExpoModulesCore

// Step 1
public class CustomViewController: UIViewController, AppControllerDelegate {
  let appDelegate = AppDelegate.shared()

  // Step 2
  public convenience init() {
    self.init(nibName: nil, bundle: nil)
    self.view.backgroundColor = .clear
    // Step 2.1
    appDelegate.updatesController = AppController.sharedInstance
    // Step 2.2
    AppController.sharedInstance.delegate = self
    // Step 2.3
    AppController.sharedInstance.start()
  }

  required public override init(nibName nibNameOrNil: String?, bundle nibBundleOrNil: Bundle?) {
    super.init(nibName: nibNameOrNil, bundle: nibBundleOrNil)
  }

  @available(*, unavailable)
  required public init?(coder aDecoder: NSCoder) {
    fatalError("init(coder:) has not been implemented")
  }

  // Step 3
  public func appController(
    _ appController: AppControllerInterface,
    didStartWithSuccess success: Bool
  ) {
    createView()
  }

  private func createView() {
    // Step 3.1
    guard let rootViewFactory: RCTRootViewFactory = appDelegate.reactNativeFactory?.rootViewFactory else {
      fatalError("rootViewFactory has not been initialized")
    }
    let rootView = rootViewFactory.view(
      withModuleName: appDelegate.moduleName,
      initialProperties: appDelegate.initialProps,
      launchOptions: appDelegate.launchOptions
    )
    // Step 3.2
    let controller = self
    controller.view.clipsToBounds = true
    controller.view.addSubview(rootView)
    rootView.translatesAutoresizingMaskIntoConstraints = false
    NSLayoutConstraint.activate([
      rootView.topAnchor.constraint(equalTo: controller.view.safeAreaLayoutGuide.topAnchor),
      rootView.bottomAnchor.constraint(equalTo: controller.view.safeAreaLayoutGuide.bottomAnchor),
      rootView.leadingAnchor.constraint(equalTo: controller.view.safeAreaLayoutGuide.leadingAnchor),
      rootView.trailingAnchor.constraint(equalTo: controller.view.safeAreaLayoutGuide.trailingAnchor)
    ])
  }
}

```

Common questions
----------------

How long will this take to add to my app?

Assuming you are using the latest version of React Native supported by the Expo SDK, and you are comfortable with the React Native integration in your native projects, then you can likely integrate EAS Update in a similar amount of time as it would take you to integrate with a tool like CodePush or Sentry.

The most important factor is the React Native version that your app uses. If your app uses anything older than the latest supported version by the Expo SDK (as referenced at the top of this guide), then you will want to upgrade to that version first, and the time that will take is heavily dependent on the size and complexity of the app and skill and experience level of the team working on it.

I'm migrating from CodePush, what else do I need to know?

To learn more, see [Migrating from CodePush](/eas-update/codepush) guide.

[Previous (EAS Update - Reference)

Estimate bandwidth usage](/eas-update/estimate-bandwidth)[Next (EAS Update - Reference)

FAQ](/eas-update/faq)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/integration-in-existing-native-apps.mdx)
* Last updated on April 25, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Prerequisites](/eas-update/integration-in-existing-native-apps/#prerequisites)[Installation and basic configuration](/eas-update/integration-in-existing-native-apps/#installation-and-basic-configuration)[Opt out of automatic setup](/eas-update/integration-in-existing-native-apps/#opt-out-of-automatic-setup)[Disable automatic setup on Android](/eas-update/integration-in-existing-native-apps/#disable-automatic-setup-on-android)[Disable automatic setup on iOS](/eas-update/integration-in-existing-native-apps/#disable-automatic-setup-on-ios)[Set up your React Native app to use expo-updates for loading the release bundle](/eas-update/integration-in-existing-native-apps/#set-up-your-react-native-app-to-use-expo-updates-for-loading-the-release-bundle)[Integrating expo-updates with your React Native bundling](/eas-update/integration-in-existing-native-apps/#integrating-expo-updates-with-your-react-native-bundling)[Integrating expo-updates on Android](/eas-update/integration-in-existing-native-apps/#integrating-expo-updates-on-android)[Integrating expo-updates on iOS](/eas-update/integration-in-existing-native-apps/#integrating-expo-updates-on-ios)[Common questions](/eas-update/integration-in-existing-native-apps/#common-questions)