Linking · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/linking)

* [Next](/docs/next/linking)* [0.79](/docs/linking)* [0.78](/docs/0.78/linking)* [0.77](/docs/0.77/linking)* [0.76](/docs/0.76/linking)* [0.75](/docs/0.75/linking)* [0.74](/docs/0.74/linking)* [0.73](/docs/0.73/linking)* [0.72](/docs/0.72/linking)* [0.71](/docs/0.71/linking)* [0.70](/docs/0.70/linking)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [APIs](/docs/accessibilityinfo)

  + [AccessibilityInfo](/docs/accessibilityinfo)+ [Alert](/docs/alert)+ [Animated](/docs/animated)+ [Animated.Value](/docs/animatedvalue)+ [Animated.ValueXY](/docs/animatedvaluexy)+ [Appearance](/docs/appearance)+ [AppRegistry](/docs/appregistry)+ [AppState](/docs/appstate)+ [DevSettings](/docs/devsettings)+ [Dimensions](/docs/dimensions)+ [Easing](/docs/easing)+ [InteractionManager](/docs/interactionmanager)+ [Keyboard](/docs/keyboard)+ [LayoutAnimation](/docs/layoutanimation)+ [Linking](/docs/linking)+ [PanResponder](/docs/panresponder)+ [PixelRatio](/docs/pixelratio)+ [Platform](/docs/platform)+ [PlatformColor](/docs/platformcolor)+ [RootTag](/docs/roottag)+ [Share](/docs/share)+ [StyleSheet](/docs/stylesheet)+ [Systrace](/docs/systrace)+ [Transforms](/docs/transforms)+ [Vibration](/docs/vibration)+ [Hooks](/docs/usecolorscheme)

                                                      - [useColorScheme](/docs/usecolorscheme)- [useWindowDimensions](/docs/usewindowdimensions)+ [Android APIs](/docs/backhandler)

                                                        - [BackHandler](/docs/backhandler)- [PermissionsAndroid](/docs/permissionsandroid)- [ToastAndroid](/docs/toastandroid)+ [iOS APIs](/docs/actionsheetios)

                                                          - [ActionSheetIOS](/docs/actionsheetios)- [DynamicColorIOS](/docs/dynamiccolorios)- [Settings](/docs/settings)

On this page

Linking
=======

`Linking` gives you a general interface to interact with both incoming and outgoing app links.

Every Link (URL) has a URL Scheme, some websites are prefixed with `https://` or `http://` and the `http` is the URL Scheme. Let's call it scheme for short.

In addition to `https`, you're likely also familiar with the `mailto` scheme. When you open a link with the mailto scheme, your operating system will open an installed mail application. Similarly, there are schemes for making phone calls and sending SMS. Read more about [built-in URL](#built-in-url-schemes) schemes below.

Like using the mailto scheme, it's possible to link to other applications by using custom url schemes. For example, when you get a **Magic Link** email from Slack, the **Launch Slack** button is an anchor tag with an href that looks something like: `slack://secret/magic-login/other-secret`. Like with Slack, you can tell the operating system that you want to handle a custom scheme. When the Slack app opens, it receives the URL that was used to open it. This is often referred to as deep linking. Read more about how to [get the deep link](#get-the-deep-link) into your app.

A custom URL scheme isn't the only way to open your application on mobile. For example, if you want to email someone a link to be opened on mobile, using a custom URL scheme isn't ideal because the user might open the email on a desktop, where the link wouldn't work. Instead, you should use standard `https` links, such as `https://www.myapp.io/records/1234546`. On mobile, these links can be configured to open your app. On Android, this feature is called **Deep Links**, while on iOS, it is known as **Universal Links**.

### Built-in URL Schemes[​](#built-in-url-schemes "Direct link to Built-in URL Schemes")

As mentioned in the introduction, there are some URL schemes for core functionality that exist on every platform. The following is a non-exhaustive list, but covers the most commonly used schemes.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Scheme Description iOS Android|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `mailto` Open mail app, eg: mailto: [support@expo.io](mailto:support@expo.io) ✅ ✅|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `tel` Open phone app, eg: tel:+123456789 ✅ ✅|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | `sms` Open SMS app, eg: sms:+123456789 ✅ ✅|  |  |  |  | | --- | --- | --- | --- | | `https` / `http` Open web browser app, eg: <https://expo.io> ✅ ✅ | | | | | | | | | | | | | | | | | | | |

### Enabling Deep Links[​](#enabling-deep-links "Direct link to Enabling Deep Links")

### Projects with Native Code Only

The following section only applies to projects with native code exposed. If you are using the managed Expo workflow, see the guide on [Linking](https://docs.expo.dev/guides/linking/) in the Expo documentation for the appropriate alternative.

If you want to enable deep links in your app, please read the below guide:

* Android* iOS

> For instructions on how to add support for deep linking on Android, refer to [Enabling Deep Links for App Content - Add Intent Filters for Your Deep Links](https://developer.android.com/training/app-indexing/deep-linking.html#adding-filters).

If you wish to receive the intent in an existing instance of MainActivity, you may set the `launchMode` of MainActivity to `singleTask` in `AndroidManifest.xml`. See [`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element.html) documentation for more information.

xml

```
<activity  
  android:name=".MainActivity"  
  android:launchMode="singleTask">  

```

> **NOTE:** On iOS, you'll need to add the `LinkingIOS` folder into your header search paths as described in step 3 [here](/docs/linking-libraries-ios#step-3). If you also want to listen to incoming app links during your app's execution, you'll need to add the following lines to your `*AppDelegate.m`:

* ObjectiveC* Swift

AppDelegate.mm

```
// iOS 9.x or newer  
#import <React/RCTLinkingManager.h>  
  
- (BOOL)application:(UIApplication *)application  
   openURL:(NSURL *)url  
   options:(NSDictionary<UIApplicationOpenURLOptionsKey,id> *)options  
{  
  return [RCTLinkingManager application:application openURL:url options:options];  
}  

```

If your app is using [Universal Links](https://developer.apple.com/ios/universal-links/), you'll need to add the following code as well:

AppDelegate.mm

```
- (BOOL)application:(UIApplication *)application continueUserActivity:(nonnull NSUserActivity *)userActivity  
 restorationHandler:(nonnull void (^)(NSArray<id<UIUserActivityRestoring>> * _Nullable))restorationHandler  
{  
 return [RCTLinkingManager application:application  
                  continueUserActivity:userActivity  
                    restorationHandler:restorationHandler];  
}  

```

AppDelegate.swift

```
func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {  
  return RCTLinkingManager.application(app, open: url, options: options)  
}  

```

If your app is using [Universal Links](https://developer.apple.com/ios/universal-links/), you'll need to add the following code as well:

AppDelegate.swift

```
func application(  
  _ application: UIApplication,  
  continue userActivity: NSUserActivity,  
  restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {  
    return RCTLinkingManager.application(  
      application,  
      continue: userActivity,  
      restorationHandler: restorationHandler  
    )  
  }  

```

### Handling Deep Links[​](#handling-deep-links "Direct link to Handling Deep Links")

There are two ways to handle URLs that open your app.

#### 1. If the app is already open, the app is foregrounded and a Linking 'url' event is fired[​](#1-if-the-app-is-already-open-the-app-is-foregrounded-and-a-linking-url-event-is-fired "Direct link to 1. If the app is already open, the app is foregrounded and a Linking 'url' event is fired")

You can handle these events with `Linking.addEventListener('url', callback)` - it calls `callback({url})` with the linked URL

#### 2. If the app is not already open, it is opened and the url is passed in as the initialURL[​](#2-if-the-app-is-not-already-open-it-is-opened-and-the-url-is-passed-in-as-the-initialurl "Direct link to 2. If the app is not already open, it is opened and the url is passed in as the initialURL")

You can handle these events with `Linking.getInitialURL()` - it returns a Promise that resolves to the URL, if there is one.

---

Example[​](#example "Direct link to Example")
---------------------------------------------

### Open Links and Deep Links (Universal Links)[​](#open-links-and-deep-links-universal-links "Direct link to Open Links and Deep Links (Universal Links)")

* TypeScript* JavaScript

### Open Custom Settings[​](#open-custom-settings "Direct link to Open Custom Settings")

* TypeScript* JavaScript

### Get the Deep Link[​](#get-the-deep-link "Direct link to Get the Deep Link")

* TypeScript* JavaScript

### Send Intents (Android)[​](#send-intents-android "Direct link to Send Intents (Android)")

* TypeScript* JavaScript

Reference
=========

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### `addEventListener()`[​](#addeventlistener "Direct link to addeventlistener")

tsx

```
static addEventListener(  
  type: 'url',  
  handler: (event: {url: string}) => void,  
): EmitterSubscription;  

```

Add a handler to Linking changes by listening to the `url` event type and providing the handler.

---

### `canOpenURL()`[​](#canopenurl "Direct link to canopenurl")

tsx

```
static canOpenURL(url: string): Promise<boolean>;  

```

Determine whether or not an installed app can handle a given URL.

The method returns a `Promise` object. When it is determined whether or not the given URL can be handled, the promise is resolved and the first parameter is whether or not it can be opened.

The `Promise` will reject on Android if it was impossible to check if the URL can be opened or when targeting Android 11 (SDK 30) if you didn't specify the relevant intent queries in `AndroidManifest.xml`. Similarly on iOS, the promise will reject if you didn't add the specific scheme in the `LSApplicationQueriesSchemes` key inside `Info.plist` (see bellow).

**Parameters:**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Name Type Description|  |  |  | | --- | --- | --- | | url Required  string The URL to open. | | | | | |

> For web URLs, the protocol (`"http://"`, `"https://"`) must be set accordingly!

> This method has limitations on iOS 9+. From [the official Apple documentation](https://developer.apple.com/documentation/uikit/uiapplication/1622952-canopenurl):
>
> * If your app is linked against an earlier version of iOS but is running in iOS 9.0 or later, you can call this method up to 50 times. After reaching that limit, subsequent calls always resolve to `false`. If the user reinstalls or upgrades the app, iOS resets the limit.
>
> As of iOS 9, your app also needs to provide the `LSApplicationQueriesSchemes` key inside `Info.plist` or `canOpenURL()` will always resolve to `false`.

> When targeting Android 11 (SDK 30) you must specify the intents for the schemes you want to handle in `AndroidManifest.xml`. A list of common intents can be found [here](https://developer.android.com/guide/components/intents-common).
>
> For example to handle `https` schemes the following needs to be added to your manifest:
>
> ```
> <manifest ...>  
>     <queries>  
>         <intent>  
>             <action android:name="android.intent.action.VIEW" />  
>             <data android:scheme="https"/>  
>         </intent>  
>     </queries>  
> </manifest>  
>
> ```

---

### `getInitialURL()`[​](#getinitialurl "Direct link to getinitialurl")

tsx

```
static getInitialURL(): Promise<string | null>;  

```

If the app launch was triggered by an app link, it will give the link url, otherwise it will give `null`.

> To support deep linking on Android, refer <https://developer.android.com/training/app-indexing/deep-linking.html#handling-intents>

> getInitialURL may return `null` when Remote JS Debugging is active. Disable the debugger to ensure it gets passed.

---

### `openSettings()`[​](#opensettings "Direct link to opensettings")

tsx

```
static openSettings(): Promise<void>;  

```

Open the Settings app and displays the app’s custom settings, if it has any.

---

### `openURL()`[​](#openurl "Direct link to openurl")

tsx

```
static openURL(url: string): Promise<any>;  

```

Try to open the given `url` with any of the installed apps.

You can use other URLs, like a location (e.g. "geo:37.484847,-122.148386" on Android or "<https://maps.apple.com/?ll=37.484847,-122.148386>" on iOS), a contact, or any other URL that can be opened with the installed apps.

The method returns a `Promise` object. If the user confirms the open dialog or the url automatically opens, the promise is resolved. If the user cancels the open dialog or there are no registered applications for the url, the promise is rejected.

**Parameters:**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Name Type Description|  |  |  | | --- | --- | --- | | url Required  string The URL to open. | | | | | |

> This method will fail if the system doesn't know how to open the specified URL. If you're passing in a non-http(s) URL, it's best to check `canOpenURL()` first.

> For web URLs, the protocol (`"http://"`, `"https://"`) must be set accordingly!

> This method may behave differently in a simulator e.g. `"tel:"` links are not able to be handled in the iOS simulator as there's no access to the dialer app.

---

### `sendIntent()` Android [​](#sendintent-android "Direct link to sendintent-android")

tsx

```
static sendIntent(  
  action: string,  
  extras?: Array<{key: string; value: string | number | boolean}>,  
): Promise<void>;  

```

Launch an Android intent with extras.

**Parameters:**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Name Type|  |  |  |  | | --- | --- | --- | --- | | action Required  string|  |  | | --- | --- | | extras `Array<{key: string, value: string ｜ number ｜ boolean}>` | | | | | |

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/linking.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/linking.md)

Last updated on **Apr 14, 2025**

[Previous

LayoutAnimation](/docs/layoutanimation)[Next

PanResponder](/docs/panresponder)

* [Built-in URL Schemes](#built-in-url-schemes)* [Enabling Deep Links](#enabling-deep-links)* [Handling Deep Links](#handling-deep-links)* [Example](#example)
        + [Open Links and Deep Links (Universal Links)](#open-links-and-deep-links-universal-links)+ [Open Custom Settings](#open-custom-settings)+ [Get the Deep Link](#get-the-deep-link)+ [Send Intents (Android)](#send-intents-android)* [Methods](#methods)
          + [`addEventListener()`](#addeventlistener)+ [`canOpenURL()`](#canopenurl)+ [`getInitialURL()`](#getinitialurl)+ [`openSettings()`](#opensettings)+ [`openURL()`](#openurl)+ [`sendIntent()`

                      Android](#sendintent-android)

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