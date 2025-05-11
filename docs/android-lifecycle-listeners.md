Android lifecycle listeners - Expo Documentation

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

Android lifecycle listeners
===========================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/modules/android-lifecycle-listeners.mdx)

Learn about the mechanism that allows your library to hook into Android Activity and Application functions using Expo modules API.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/modules/android-lifecycle-listeners.mdx)

---

To respond to certain Android system events relevant to an app, such as inbound links and configuration changes, it is necessary to override the corresponding lifecycle callbacks in MainActivity.java and/or MainApplication.java.

The React Native module API does not provide any mechanism to hook into these, and so setup instructions for React Native libraries often include steps to copy code into these files. To simplify and automate setup and maintenance, the Expo Modules API provides a mechanism that allows your library to hook into `Activity` or `Application` functions.

Get started
-----------

First, you need to have created an Expo module or integrated the Expo modules API in the library using the React Native module API. [Learn more](/modules/overview#setup).

Inside your module, create a concrete class that implements the [`Package`](https://github.com/expo/expo/tree/main/packages/expo-modules-core/android/src/main/java/expo/modules/core/interfaces/Package.java) interface. For most cases, you only need to implement the `createReactActivityLifecycleListeners` or `createApplicationLifecycleListeners` methods.

`Activity` lifecycle listeners
------------------------------

You can hook into the `Activity` lifecycle using `ReactActivityLifecycleListener`. `ReactActivityLifecycleListener` hooks into React Native's `ReactActivity` lifecycle using its `ReactActivityDelegate` and provides a similar experience to the Android `Activity` lifecycle.

The following `Activity` lifecycle callbacks are currently supported:

* `onCreate`
* `onResume`
* `onPause`
* `onDestroy`
* `onNewIntent`
* `onBackPressed`

To create a `ReactActivityLifecycleListener`, you should implement `createReactActivityLifecycleListeners` in your derived `Package` class. For example, `MyLibPackage`.

Kotlin

Java

```
// android/src/main/java/expo/modules/mylib/MyLibPackage.kt
package expo.modules.mylib

import android.content.Context
import expo.modules.core.interfaces.Package
import expo.modules.core.interfaces.ReactActivityLifecycleListener

class MyLibPackage : Package {
  override fun createReactActivityLifecycleListeners(activityContext: Context): List<ReactActivityLifecycleListener> {
    return listOf(MyLibReactActivityLifecycleListener())
  }
}

```

```
// android/src/main/java/expo/modules/mylib/MyLibPackage.java
package expo.modules.mylib;

import android.content.Context;
import expo.modules.core.interfaces.Package;
import expo.modules.core.interfaces.ReactActivityLifecycleListener;

import java.util.Collections;
import java.util.List;

public class MyLibPackage implements Package {
  @Override
  public List<? extends ReactActivityLifecycleListener> createReactActivityLifecycleListeners(Context activityContext) {
    return Collections.singletonList(new MyLibReactActivityLifecycleListener());
  }
}

```

`MyLibReactActivityLifecycleListener` is a `ReactActivityLifecycleListener` derived class that you can hook into the lifecycles. You can only override the methods you need.

Kotlin

Java

```
// android/src/main/java/expo/modules/mylib/MyLibReactActivityLifecycleListener.kt
package expo.modules.mylib

import android.app.Activity
import android.os.Bundle
import expo.modules.core.interfaces.ReactActivityLifecycleListener

class MyLibReactActivityLifecycleListener : ReactActivityLifecycleListener {
  override fun onCreate(activity: Activity, savedInstanceState: Bundle?) {
    // Your setup code in `Activity.onCreate`.
    doSomeSetupInActivityOnCreate(activity)
  }
}

```

```
// android/src/main/java/expo/modules/mylib/MyLibReactActivityLifecycleListener.java
package expo.modules.mylib;

import android.app.Activity;
import android.os.Bundle;

import expo.modules.core.interfaces.ReactActivityLifecycleListener;

public class MyLibReactActivityLifecycleListener implements ReactActivityLifecycleListener {
  @Override
  public void onCreate(Activity activity, Bundle savedInstanceState) {
    // Your setup code in `Activity.onCreate`.
    doSomeSetupInActivityOnCreate(activity);
  }
}

```

`Application` lifecycle listeners
---------------------------------

You can hook into the `Application` lifecycle using `ApplicationLifecycleListener`.

The following `Application` lifecycle callbacks are currently supported:

* `onCreate`
* `onConfigurationChanged`

To create an `ApplicationLifecycleListener`, you should implement `createApplicationLifecycleListeners` in your derived `Package` class. For example, `MyLibPackage`.

Kotlin

Java

```
// android/src/main/java/expo/modules/mylib/MyLibPackage.kt
package expo.modules.mylib

import android.content.Context
import expo.modules.core.interfaces.ApplicationLifecycleListener
import expo.modules.core.interfaces.Package

class MyLibPackage : Package {
  override fun createApplicationLifecycleListeners(context: Context): List<ApplicationLifecycleListener> {
    return listOf(MyLibApplicationLifecycleListener())
  }
}

```

```
// android/src/main/java/expo/modules/mylib/MyLibPackage.java
import android.content.Context;

import java.util.Collections;
import java.util.List;

import expo.modules.core.interfaces.ApplicationLifecycleListener;
import expo.modules.core.interfaces.Package;

public class MyLibPackage implements Package {
  @Override
  public List<? extends ApplicationLifecycleListener> createApplicationLifecycleListeners(Context context) {
    return Collections.singletonList(new MyLibApplicationLifecycleListener());
  }
}

```

`MyLibApplicationLifecycleListener` is an `ApplicationLifecycleListener` derived class that can hook into the `Application` lifecycle callbacks. You should only override the methods you need ([due to possible maintenance costs](/modules/android-lifecycle-listeners#interface-stability)).

Kotlin

Java

```
// android/src/main/java/expo/modules/mylib/MyLibApplicationLifecycleListener.kt
package expo.modules.mylib

import android.app.Application
import expo.modules.core.interfaces.ApplicationLifecycleListener

class MyLibApplicationLifecycleListener : ApplicationLifecycleListener {
  override fun onCreate(application: Application) {
    // Your setup code in `Application.onCreate`.
    doSomeSetupInApplicationOnCreate(application)
  }
}

```

```
// android/src/main/java/expo/modules/mylib/MyLibApplicationLifecycleListener.java
package expo.modules.mylib;

import android.app.Application;

import expo.modules.core.interfaces.ApplicationLifecycleListener;

public class MyLibApplicationLifecycleListener implements ApplicationLifecycleListener {
  @Override
  public void onCreate(Application application) {
    // Your setup code in `Application.onCreate`.
    doSomeSetupInApplicationOnCreate(application);
  }
}

```

Known issues
------------

### Why there are no `onStart` and `onStop` Activity listeners

In the current implementation, we do not set up the hooks from `MainActivity` but from [`ReactActivityDelegate`](https://github.com/facebook/react-native/blob/400902093aa3ccfc05712a996c592a86f342253a/ReactAndroid/src/main/java/com/facebook/react/ReactActivityDelegate.java). There are some slight differences between `MainActivity` and `ReactActivityDelegate`. Since `ReactActivityDelegate` does not have `onStart` and `onStop`, we don't yet support them here.

### Interface stability

The listener interfaces may change from time to time between Expo SDK releases. Our strategy for backward compatibility is always to add new interfaces and add `@Deprecated` annotation for interfaces we plan to remove. Our interfaces are all based on Java 8 interface default method; you don't have to and should not implement all methods. Doing this will benefit your module's maintenance cost between Expo SDKs.

[Previous (Expo Modules API - Reference)

Module API](/modules/module-api)[Next (Expo Modules API - Reference)

iOS AppDelegate subscribers](/modules/appdelegate-subscribers)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/modules/android-lifecycle-listeners.mdx)
* Last updated on January 19, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Get started](/modules/android-lifecycle-listeners/#get-started)[Activity lifecycle listeners](/modules/android-lifecycle-listeners/#activity-lifecycle-listeners)[Application lifecycle listeners](/modules/android-lifecycle-listeners/#application-lifecycle-listeners)[Known issues](/modules/android-lifecycle-listeners/#known-issues)[Why there are no onStart and onStop Activity listeners](/modules/android-lifecycle-listeners/#why-there-are-no-onstart-and-onstop-activity-listeners)[Interface stability](/modules/android-lifecycle-listeners/#interface-stability)