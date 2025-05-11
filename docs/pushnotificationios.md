🚧 PushNotificationIOS · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/pushnotificationios)

* [Next](/docs/next/pushnotificationios)* [0.79](/docs/pushnotificationios)* [0.78](/docs/0.78/pushnotificationios)* [0.77](/docs/0.77/pushnotificationios)* [0.76](/docs/0.76/pushnotificationios)* [0.75](/docs/0.75/pushnotificationios)* [0.74](/docs/0.74/pushnotificationios)* [0.73](/docs/0.73/pushnotificationios)* [0.72](/docs/0.72/pushnotificationios)* [0.71](/docs/0.71/pushnotificationios)* [0.70](/docs/0.70/pushnotificationios)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

On this page

🚧 PushNotificationIOS
=====================

> **Deprecated.** Use the [community package](https://github.com/react-native-push-notification/ios) instead.

### Projects with Native Code Only

The following section only applies to projects with native code exposed. If you are using the managed Expo workflow, see the guide on [Notifications](https://docs.expo.dev/versions/latest/sdk/notifications/) in the Expo documentation for the appropriate alternative.

Handle notifications for your app, including scheduling and permissions.

---

Getting Started[​](#getting-started "Direct link to Getting Started")
---------------------------------------------------------------------

To enable push notifications, [configure your notifications with Apple](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server) and your server-side system.

Then, [enable remote notifications](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app#2980038) in your project. This will automatically enable the required settings.

### Enable support for `register` events[​](#enable-support-for-register-events "Direct link to enable-support-for-register-events")

In your `AppDelegate.m`, add:

objectivec

```
#import <React/RCTPushNotificationManager.h>  

```

Then implement the following in order to handle remote notification registration events:

objectivec

```
- (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken  
{  
 // This will trigger 'register' events on PushNotificationIOS  
 [RCTPushNotificationManager didRegisterForRemoteNotificationsWithDeviceToken:deviceToken];  
}  
- (void)application:(UIApplication *)application didFailToRegisterForRemoteNotificationsWithError:(NSError *)error  
{  
 // This will trigger 'registrationError' events on PushNotificationIOS  
 [RCTPushNotificationManager didFailToRegisterForRemoteNotificationsWithError:error];  
}  

```

### Handle notifications[​](#handle-notifications "Direct link to Handle notifications")

You'll need to implement `UNUserNotificationCenterDelegate` in your `AppDelegate`:

objectivec

```
#import <UserNotifications/UserNotifications.h>  
  
@interface YourAppDelegate () <UNUserNotificationCenterDelegate>  
@end  

```

Set the delegate on app launch:

objectivec

```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions  
{  
  ...  
  UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];  
  center.delegate = self;  
  
  return YES;  
}  

```

#### Foreground notifications[​](#foreground-notifications "Direct link to Foreground notifications")

Implement `userNotificationCenter:willPresentNotification:withCompletionHandler:` to handle notifications that arrive when the app is in the foreground. Use the completionHandler to determine if the notification will be shown to the user and notify `RCTPushNotificationManager` accordingly:

objectivec

```
// Called when a notification is delivered to a foreground app.  
- (void)userNotificationCenter:(UNUserNotificationCenter *)center  
       willPresentNotification:(UNNotification *)notification  
         withCompletionHandler:(void (^)(UNNotificationPresentationOptions options))completionHandler  
{  
  // This will trigger 'notification' and 'localNotification' events on PushNotificationIOS  
  [RCTPushNotificationManager didReceiveNotification:notification];  
  // Decide if and how the notification will be shown to the user  
  completionHandler(UNNotificationPresentationOptionNone);  
}  

```

#### Background notifications[​](#background-notifications "Direct link to Background notifications")

Implement `userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` to handle when a notification is tapped, typically called for background notifications which the user taps to open the app. However, if you had set foreground notifications to be shown in `userNotificationCenter:willPresentNotification:withCompletionHandler:`, this method will also be invoked on foreground notifications when tapped. In this case, you should only notify `RCTPushNotificationManager` in one of these callbacks.

If the tapped notification resulted in app launch, call `setInitialNotification:`. If the notification was not previously handled by `userNotificationCenter:willPresentNotification:withCompletionHandler:`, call `didReceiveNotification:` as well:

objectivec

```
- (void)  userNotificationCenter:(UNUserNotificationCenter *)center  
  didReceiveNotificationResponse:(UNNotificationResponse *)response  
           withCompletionHandler:(void (^)(void))completionHandler  
{  
  // This condition passes if the notification was tapped to launch the app  
  if ([response.actionIdentifier isEqualToString:UNNotificationDefaultActionIdentifier]) {  
    // Allow the notification to be retrieved on the JS side using getInitialNotification()  
    [RCTPushNotificationManager setInitialNotification:response.notification];  
  }  
  // This will trigger 'notification' and 'localNotification' events on PushNotificationIOS  
  [RCTPushNotificationManager didReceiveNotification:response.notification];  
  completionHandler();  
}  

```

---

Reference
=========

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### `presentLocalNotification()`[​](#presentlocalnotification "Direct link to presentlocalnotification")

tsx

```
static presentLocalNotification(details: PresentLocalNotificationDetails);  

```

Schedules a local notification for immediate presentation.

**Parameters:**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  | | --- | --- | --- | --- | | details object Yes See below. | | | | | | | |

`details` is an object containing:

* `alertTitle` : The text displayed as the title of the notification alert.
* `alertBody` : The message displayed in the notification alert.
* `userInfo` : An object containing additional notification data (optional).
* `category` : The category of this notification, required for actionable notifications (optional). e.g. notifications with additional actions such as Reply or Like.
* `applicationIconBadgeNumber` The number to display as the app's icon badge. The default value of this property is 0, which means that no badge is displayed (optional).
* `isSilent` : If true, the notification will appear without sound (optional).
* `soundName` : The sound played when the notification is fired (optional).
* `alertAction` : DEPRECATED. This was used for iOS's legacy UILocalNotification.

---

### `scheduleLocalNotification()`[​](#schedulelocalnotification "Direct link to schedulelocalnotification")

tsx

```
static scheduleLocalNotification(details: ScheduleLocalNotificationDetails);  

```

Schedules a local notification for future presentation.

**Parameters:**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  | | --- | --- | --- | --- | | details object Yes See below. | | | | | | | |

`details` is an object containing:

* `alertTitle` : The text displayed as the title of the notification alert.
* `alertBody` : The message displayed in the notification alert.
* `fireDate` : When the notification will be fired. Schedule notifications using either `fireDate` or `fireIntervalSeconds`, with `fireDate` taking precedence.
* `fireIntervalSeconds` : Seconds from now to display the notification.
* `userInfo` : An object containing additional notification data (optional).
* `category` : The category of this notification, required for actionable notifications (optional). e.g. notifications with additional actions such as Reply or Like.
* `applicationIconBadgeNumber` The number to display as the app's icon badge. The default value of this property is 0, which means that no badge is displayed (optional).
* `isSilent` : If true, the notification will appear without sound (optional).
* `soundName` : The sound played when the notification is fired (optional).
* `alertAction` : DEPRECATED. This was used for iOS's legacy UILocalNotification.
* `repeatInterval` : DEPRECATED. Use `fireDate` or `fireIntervalSeconds` instead.

---

### `cancelAllLocalNotifications()`[​](#cancelalllocalnotifications "Direct link to cancelalllocalnotifications")

tsx

```
static cancelAllLocalNotifications();  

```

Cancels all scheduled local notifications.

---

### `removeAllDeliveredNotifications()`[​](#removealldeliverednotifications "Direct link to removealldeliverednotifications")

tsx

```
static removeAllDeliveredNotifications();  

```

Removes all delivered notifications from Notification Center.

---

### `getDeliveredNotifications()`[​](#getdeliverednotifications "Direct link to getdeliverednotifications")

tsx

```
static getDeliveredNotifications(callback: (notifications: Object[]) => void);  

```

Provides a list of the app’s notifications that are currently displayed in Notification Center.

**Parameters:**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  | | --- | --- | --- | --- | | callback function Yes Function which receives an array of delivered notifications. | | | | | | | |

A delivered notification is an object containing:

* `identifier` : The identifier of this notification.
* `title` : The title of this notification.
* `body` : The body of this notification.
* `category` : The category of this notification (optional).
* `userInfo` : An object containing additional notification data (optional).
* `thread-id` : The thread identifier of this notification, if it has one.

---

### `removeDeliveredNotifications()`[​](#removedeliverednotifications "Direct link to removedeliverednotifications")

tsx

```
static removeDeliveredNotifications(identifiers: string[]);  

```

Removes the specified notifications from Notification Center.

**Parameters:**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  | | --- | --- | --- | --- | | identifiers array Yes Array of notification identifiers. | | | | | | | |

---

### `setApplicationIconBadgeNumber()`[​](#setapplicationiconbadgenumber "Direct link to setapplicationiconbadgenumber")

tsx

```
static setApplicationIconBadgeNumber(num: number);  

```

Sets the badge number for the app icon on the Home Screen.

**Parameters:**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  | | --- | --- | --- | --- | | number number Yes Badge number for the app icon. | | | | | | | |

---

### `getApplicationIconBadgeNumber()`[​](#getapplicationiconbadgenumber "Direct link to getapplicationiconbadgenumber")

tsx

```
static getApplicationIconBadgeNumber(callback: (num: number) => void);  

```

Gets the current badge number for the app icon on the Home Screen.

**Parameters:**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  | | --- | --- | --- | --- | | callback function Yes Function which processes the current badge number. | | | | | | | |

---

### `cancelLocalNotifications()`[​](#cancellocalnotifications "Direct link to cancellocalnotifications")

tsx

```
static cancelLocalNotifications(userInfo: Object);  

```

Cancels any scheduled local notifications which match the fields in the provided `userInfo`.

**Parameters:**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  | | --- | --- | --- | --- | | userInfo object No  | | | | | | | |

---

### `getScheduledLocalNotifications()`[​](#getscheduledlocalnotifications "Direct link to getscheduledlocalnotifications")

tsx

```
static getScheduledLocalNotifications(  
  callback: (notifications: ScheduleLocalNotificationDetails[]) => void,  
);  

```

Gets the list of local notifications that are currently scheduled.

**Parameters:**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  | | --- | --- | --- | --- | | callback function Yes Function which processes an array of objects describing local notifications. | | | | | | | |

---

### `addEventListener()`[​](#addeventlistener "Direct link to addeventlistener")

tsx

```
static addEventListener(  
  type: PushNotificationEventName,  
  handler:  
    | ((notification: PushNotification) => void)  
    | ((deviceToken: string) => void)  
    | ((error: {message: string; code: number; details: any}) => void),  
);  

```

Attaches a listener to notification events including local notifications, remote notifications, and notification registration results.

**Parameters:**

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | type string Yes Event type to listen to. See below.|  |  |  |  | | --- | --- | --- | --- | | handler function Yes Listener. | | | | | | | | | | | |

Valid events types include:

* `notification` : Fired when a remote notification is received. The handler will be invoked with an instance of `PushNotificationIOS`. This will handle notifications that arrive in the foreground or were tapped to open the app from the background.
* `localNotification` : Fired when a local notification is received. The handler will be invoked with an instance of `PushNotificationIOS`. This will handle notifications that arrive in the foreground or were tapped to open the app from the background.
* `register`: Fired when the user registers successfully for remote notifications. The handler will be invoked with a hex string representing the deviceToken.
* `registrationError`: Fired when the user fails to register for remote notifications. Typically occurs due to APNS issues or if the device is a simulator. The handler will be invoked with `{message: string, code: number, details: any}`.

---

### `removeEventListener()`[​](#removeeventlistener "Direct link to removeeventlistener")

tsx

```
static removeEventListener(  
  type: PushNotificationEventName,  
);  

```

Removes the event listener. Do this in `componentWillUnmount` to prevent memory leaks.

**Parameters:**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  | | --- | --- | --- | --- | | type string Yes Event type. See `addEventListener()` for options. | | | | | | | |

---

### `requestPermissions()`[​](#requestpermissions "Direct link to requestpermissions")

tsx

```
static requestPermissions(permissions?: PushNotificationPermissions[]);  

```

Requests notification permissions from iOS, prompting the user with a dialog box. By default, this will request all notification permissions, but you can optionally specify which permissions to request. The following permissions are supported:

* `alert`
* `badge`
* `sound`

If a map is provided to the method, only the permissions with truthy values will be requested.

This method returns a promise that will resolve when the user accepts or rejects the request, or if the permissions were previously rejected. The promise resolves to the state of the permissions after the request has been completed.

**Parameters:**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  | | --- | --- | --- | --- | | permissions array No alert, badge, or sound | | | | | | | |

---

### `abandonPermissions()`[​](#abandonpermissions "Direct link to abandonpermissions")

tsx

```
static abandonPermissions();  

```

Unregister for all remote notifications received via Apple Push Notification service.

You should call this method in rare circumstances only, such as when a new version of the app removes support for all types of remote notifications. Users can temporarily prevent apps from receiving remote notifications through the Settings app. Apps unregistered through this method can always re-register.

---

### `checkPermissions()`[​](#checkpermissions "Direct link to checkpermissions")

tsx

```
static checkPermissions(  
  callback: (permissions: PushNotificationPermissions) => void,  
);  

```

Check which push permissions are currently enabled.

**Parameters:**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  | | --- | --- | --- | --- | | callback function Yes See below. | | | | | | | |

`callback` will be invoked with a `permissions` object:

* `alert: boolean`
* `badge: boolean`
* `sound: boolean`

---

### `getInitialNotification()`[​](#getinitialnotification "Direct link to getinitialnotification")

tsx

```
static getInitialNotification(): Promise<PushNotification | null>;  

```

This method returns a promise. If the app was launched by a push notification, this promise resolves to an object of type `PushNotificationIOS` for the notification that was tapped. Otherwise, it resolves to `null`.

---

### `getAuthorizationStatus()`[​](#getauthorizationstatus "Direct link to getauthorizationstatus")

tsx

```
static getAuthorizationStatus(): Promise<number>;  

```

This method returns a promise that resolves to the current notification authorization status. See [UNAuthorizationStatus](https://developer.apple.com/documentation/usernotifications/unauthorizationstatus?language=objc) for possible values.

---

### `finish()`[​](#finish "Direct link to finish")

tsx

```
finish(result: string);  

```

This method is available for remote notifications that have been received via [`application:didReceiveRemoteNotification:fetchCompletionHandler:`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application?language=objc). However, this is superseded by `UNUserNotificationCenterDelegate` and will no longer be invoked if both `application:didReceiveRemoteNotification:fetchCompletionHandler:` and the newer handlers from `UNUserNotificationCenterDelegate` are implemented.

If for some reason you're still relying on `application:didReceiveRemoteNotification:fetchCompletionHandler:`, you'll need to set up event handling on the iOS side:

objectivec

```
- (void)           application:(UIApplication *)application  
  didReceiveRemoteNotification:(NSDictionary *)userInfo  
        fetchCompletionHandler:(void (^)(UIBackgroundFetchResult result))handler  
{  
  [RCTPushNotificationManager didReceiveRemoteNotification:userInfo fetchCompletionHandler:handler];  
}  

```

Call `finish()` to execute the native completion handlers once you're done handling the notification on the JS side. When calling this block, pass in the fetch result value that best describes the results of your operation. For a list of possible values, see `PushNotificationIOS.FetchResult`.

If you're using `application:didReceiveRemoteNotification:fetchCompletionHandler:`, you *must* call this handler and should do so as soon as possible. See the [official documentation](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application?language=objc) for more details.

---

### `getMessage()`[​](#getmessage "Direct link to getmessage")

tsx

```
getMessage(): string | Object;  

```

An alias for `getAlert` to get the notification's main message string.

---

### `getSound()`[​](#getsound "Direct link to getsound")

tsx

```
getSound(): string;  

```

Gets the sound string from the `aps` object. This will be `null` for local notifications.

---

### `getCategory()`[​](#getcategory "Direct link to getcategory")

tsx

```
getCategory(): string;  

```

Gets the category string from the `aps` object.

---

### `getAlert()`[​](#getalert "Direct link to getalert")

tsx

```
getAlert(): string | Object;  

```

Gets the notification's main message from the `aps` object. Also see the alias: `getMessage()`.

---

### `getContentAvailable()`[​](#getcontentavailable "Direct link to getcontentavailable")

tsx

```
getContentAvailable(): number;  

```

Gets the content-available number from the `aps` object.

---

### `getBadgeCount()`[​](#getbadgecount "Direct link to getbadgecount")

tsx

```
getBadgeCount(): number;  

```

Gets the badge count number from the `aps` object.

---

### `getData()`[​](#getdata "Direct link to getdata")

tsx

```
getData(): Object;  

```

Gets the data object on the notification.

---

### `getThreadID()`[​](#getthreadid "Direct link to getthreadid")

tsx

```
getThreadID();  

```

Gets the thread ID on the notification.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/pushnotificationios.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/pushnotificationios.md)

Last updated on **Apr 14, 2025**

* [Getting Started](#getting-started)
  + [Enable support for `register` events](#enable-support-for-register-events)+ [Handle notifications](#handle-notifications)* [Methods](#methods)
    + [`presentLocalNotification()`](#presentlocalnotification)+ [`scheduleLocalNotification()`](#schedulelocalnotification)+ [`cancelAllLocalNotifications()`](#cancelalllocalnotifications)+ [`removeAllDeliveredNotifications()`](#removealldeliverednotifications)+ [`getDeliveredNotifications()`](#getdeliverednotifications)+ [`removeDeliveredNotifications()`](#removedeliverednotifications)+ [`setApplicationIconBadgeNumber()`](#setapplicationiconbadgenumber)+ [`getApplicationIconBadgeNumber()`](#getapplicationiconbadgenumber)+ [`cancelLocalNotifications()`](#cancellocalnotifications)+ [`getScheduledLocalNotifications()`](#getscheduledlocalnotifications)+ [`addEventListener()`](#addeventlistener)+ [`removeEventListener()`](#removeeventlistener)+ [`requestPermissions()`](#requestpermissions)+ [`abandonPermissions()`](#abandonpermissions)+ [`checkPermissions()`](#checkpermissions)+ [`getInitialNotification()`](#getinitialnotification)+ [`getAuthorizationStatus()`](#getauthorizationstatus)+ [`finish()`](#finish)+ [`getMessage()`](#getmessage)+ [`getSound()`](#getsound)+ [`getCategory()`](#getcategory)+ [`getAlert()`](#getalert)+ [`getContentAvailable()`](#getcontentavailable)+ [`getBadgeCount()`](#getbadgecount)+ [`getData()`](#getdata)+ [`getThreadID()`](#getthreadid)

Develop

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

Participate

* [Showcase](/showcase)* [Contributing](/contributing/overview)* [Community](/community/overview)* [Directory](https://reactnative.directory/)* [Stack Overflow](https://stackoverflow.com/questions/tagged/react-native)

Find us

* [Blog](/blog)* [X](https://x.com/reactnative)* [Bluesky](https://bsky.app/profile/reactnative.dev)* [GitHub](https://github.com/facebook/react-native)

Explore More

* [ReactJS](https://react.dev/)* [Privacy Policy](https://opensource.fb.com/legal/privacy/)* [Terms of Service](https://opensource.fb.com/legal/terms/)

[![Meta Open Source Logo](/img/oss_logo.svg)![Meta Open Source Logo](/img/oss_logo.svg)](https://opensource.fb.com/)

Copyright © 2025 Meta Platforms, Inc.