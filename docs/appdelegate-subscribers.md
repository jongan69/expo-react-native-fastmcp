iOS AppDelegate subscribers - Expo Documentation

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

iOS AppDelegate subscribers
===========================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/modules/appdelegate-subscribers.mdx)

Learn how to subscribe to iOS system events relevant to an app, such as inbound links and notifications using Expo modules API.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/modules/appdelegate-subscribers.mdx)

---

To respond to certain iOS system events relevant to an app, such as inbound links and notifications, it is necessary to handle the corresponding methods in the `AppDelegate`.

The React Native module API does not provide any mechanism to hook into these methods, and so setup instructions for React Native libraries often include a step to copy code into the `AppDelegate` file. To simplify and automate setup and maintenance, the Expo Modules API provides a mechanism that allows your library to subscribe to calls to `AppDelegate` functions. For this to work, the app `AppDelegate` must inherit from `ExpoAppDelegate`, and this is a requirement for using Expo Modules.

`ExpoAppDelegate` implements most functions from [`UIApplicationDelegate`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate) protocol and forwards their calls to all the subscribers.

Get started
-----------

First, you need to have created an Expo module or integrated the Expo modules API in library using the React Native module API. [Learn more](/modules/overview#setup).

Create a new public Swift class that extends `ExpoAppDelegateSubscriber` from `ExpoModulesCore` and add its name to the `apple.appDelegateSubscribers` array in the [module config](/modules/module-config). Run `pod install`, and the subscriber will be generated in the ExpoModulesProvider.swift file within the application project.

Now you can subscribe to events by adding delegate functions to your subscriber class. For the full list of functions that you can subscribe to, see the functions that are overridden in [`ExpoAppDelegate.swift`](https://github.com/expo/expo/blob/main/packages/expo/ios/AppDelegates/ExpoAppDelegate.swift). App delegate functions that may cause side effects when provided are not supported yet (for example, [`application(_:viewControllerWithRestorationIdentifierPath:coder:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623062-application)).

> Objective-C classes are not supported.

Result values
-------------

Delegate functions that need to return a value have some additional logic to reconcile responses from multiple subscribers and try to satisfy all of them. There are two good examples of such edge cases:

#### `application(_:didFinishLaunchingWithOptions:) -> Bool`

According to the [Apple documentation](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application), you should return `false` if the app cannot handle the URL resource or continue a user activity, otherwise `true` should be returned. The return value is ignored if the app is launched because of a remote notification.
In such situations, if at least one of the subscribers returns `true`, the `ExpoAppDelegate` will return `true` as well.

#### `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`

This method tells the app delegate that a remote notification arrived and gives the app the opportunity to fetch new data. It receives a completion block to execute when the fetch operation is completed. This block should be called with the fetch result value that best describes the results of your fetch request. Possible values are: `UIBackgroundFetchResult.newData`, `UIBackgroundFetchResult.noData` or `UIBackgroundFetchResult.failed`.
In this scenario, `ExpoAppDelegate` passes a new completion block to each subscriber, waits until all are completed and collects the results before calling the original completion block. The final result depends on the results collected from the subscribers, as follows in the following order:

* If at least one subscriber called the completion block with `failed` result, the delegate returns `failed` as well.
* If there is at least one `newData` result, the delegate returns `newData`.
* Otherwise `noData` is returned.

> To check out how other functions process the result of your subscriber, we recommend reading the code directly: [`ExpoAppDelegate.swift`](https://github.com/expo/expo/blob/main/packages/expo/ios/AppDelegates/ExpoAppDelegate.swift).

Example
-------

AppLifecycleDelegate.swift

Copy

```
import ExpoModulesCore

public class AppLifecycleDelegate: ExpoAppDelegateSubscriber {
  public func applicationDidBecomeActive(_ application: UIApplication) {
    // The app has become active.
  }

  public func applicationWillResignActive(_ application: UIApplication) {
    // The app is about to become inactive.
  }

  public func applicationDidEnterBackground(_ application: UIApplication) {
    // The app is now in the background.
  }

  public func applicationWillEnterForeground(_ application: UIApplication) {
    // The app is about to enter the foreground.
  }

  public func applicationWillTerminate(_ application: UIApplication) {
    // The app is about to terminate.
  }
}

```

expo-module.config.json

Copy

```
{
  "apple": {
    "appDelegateSubscribers": ["AppLifecycleDelegate"]
  }
}

```

[Previous (Expo Modules API - Reference)

Android lifecycle listeners](/modules/android-lifecycle-listeners)[Next (Expo Modules API - Reference)

Autolinking](/modules/autolinking)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/modules/appdelegate-subscribers.mdx)
* Last updated on April 11, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Get started](/modules/appdelegate-subscribers/#get-started)[Result values](/modules/appdelegate-subscribers/#result-values)[Example](/modules/appdelegate-subscribers/#example)