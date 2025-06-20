Native Modules Lifecycle · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/the-new-architecture/native-modules-lifecycle)

* [Next](/docs/next/the-new-architecture/native-modules-lifecycle)* [0.79](/docs/the-new-architecture/native-modules-lifecycle)* [0.78](/docs/0.78/getting-started)* [0.77](/docs/0.77/getting-started)* [0.76](/docs/0.76/getting-started)* [0.75](/docs/0.75/getting-started)* [0.74](/docs/0.74/getting-started)* [0.73](/docs/0.73/getting-started)* [0.72](/docs/0.72/getting-started)* [0.71](/docs/0.71/getting-started)* [0.70](/docs/0.70/getting-started)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

On this page

Native Modules Lifecycle
========================

In React Native, Native Modules are singleton. The Native Module infrastructure lazily creates a Native Modules the first time it is accessed and it keeps it around whenever the app requires it. This is a performance optimization that allows us to avoid the overhead of creating Native Modules eagerly, at app start, and it ensure faster startup times.

In a pure React Native app, the Native Modules are created once and they are never destroyed. However, in more complex apps, there might be use cases where the Native Modules are destroyed and recreated. Imagine, for example, a brownfield app that mixes some native views with some React Native surfaces, as presented in the [Integrating with Existing App guide](/docs/integration-with-existing-apps). In that case it might make sense to destroy a React Native instance when the user navigates away from a React Native surface and recreate it when the user navigates back to that surface.

When this happens, Native Module that are stateless won't cause any issues. However, for stateful Native Modules it might be necessary to properly invalidate the Native Module to ensure that the state is reset and the resources released.

In this guide, you will explore how to initialize and invalidate a Native Module properly. This guide assumes that you are familiar with how to write a Native Modules and you are comfortable writing native code. If you are not familiar with Native Modules, please read the [Native Modules guide](/docs/next/turbo-native-modules-introduction) first.

Android[​](#android "Direct link to Android")
---------------------------------------------

When it comes to Android, all the Native Modules already implements a [TurboModule](https://github.com/facebook/react-native/blob/main/packages/react-native/ReactAndroid/src/main/java/com/facebook/react/turbomodule/core/interfaces/TurboModule.kt) interface that defines two methods: `initialize()` and `invalidate()`.

The `initialize()` method is called by the Native Module infrastructure when the Native Module is created. This is the best place to put all the initialization code that needs access to the ReactApplicationContext, for example. These are some Native Modules from core that implements the `initialize()` method: [BlobModule](https://github.com/facebook/react-native/blob/0617accecdcb11159ba15c34885f294bc206aa89/packages/react-native/ReactAndroid/src/main/java/com/facebook/react/modules/blob/BlobModule.java#L155-L157), [NetworkingModule](https://github.com/facebook/react-native/blob/0617accecdcb11159ba15c34885f294bc206aa89/packages/react-native/ReactAndroid/src/main/java/com/facebook/react/modules/network/NetworkingModule.java#L193-L197).

The `invalidate()` method is called by the Native Module infrastructure when the Native Module is destroyed. This is the best place to put all the cleanup code, resetting the Native Module state and release resources that are no longer needed, such as memory and files. These are some Native Modules from core that implements the `invalidate()` method: [DeviceInfoModule](https://github.com/facebook/react-native/blob/0617accecdcb11159ba15c34885f294bc206aa89/packages/react-native/ReactAndroid/src/main/java/com/facebook/react/modules/deviceinfo/DeviceInfoModule.kt#L72-L76), [NetworkModule](https://github.com/facebook/react-native/blob/0617accecdcb11159ba15c34885f294bc206aa89/packages/react-native/ReactAndroid/src/main/java/com/facebook/react/modules/network/NetworkingModule.java#L200-L212)

iOS[​](#ios "Direct link to iOS")
---------------------------------

On iOS, Native Modules conforms to the [`RCTTurboModule`](https://github.com/facebook/react-native/blob/0617accecdcb11159ba15c34885f294bc206aa89/packages/react-native/ReactCommon/react/nativemodule/core/platform/ios/ReactCommon/RCTTurboModule.h#L196-L200) protocol. However, this protocol does not expose the `initialize` and `invalidate` method that are exposed by the Android's `TurboModule` class.

Instead, on iOS, there are two additional protocols: [`RCTInitializing`](https://github.com/facebook/react-native/blob/0617accecdcb11159ba15c34885f294bc206aa89/packages/react-native/React/Base/RCTInitializing.h) and [`RCTInvalidating`](https://github.com/facebook/react-native/blob/0617accecdcb11159ba15c34885f294bc206aa89/packages/react-native/React/Base/RCTInvalidating.h). These protocols are used to define the `initialize` and `invalidate` methods, respectively.

If your module needs to run some initialization code, then you can conform to the `RCTInitializing` protocol and implement the `initialize` method. To do so, you have to:

1. Moduify the `NativeModule.h` file by adding the following lines:

NativeModule.h

```
+ #import <React/RCTInitializing.h>  
  
//...  
  
- @interface NativeModule : NSObject <NativeModuleSpec>  
+ @interface NativeModule : NSObject <NativeModuleSpec, RCTInitializing>  
//...  
@end  

```

2. Implement the `initialize` method in the `NativeModule.mm` file:

NativeModule.mm

```
// ...  
  
@implementation NativeModule  
  
+- (void)initialize {  
+ // add the initialization code here  
+}  
  
@end  

```

These are some Native Modules from core that implements the `initialize` method: [RCTBlobManager](https://github.com/facebook/react-native/blob/0617accecdcb11159ba15c34885f294bc206aa89/packages/react-native/Libraries/Blob/RCTBlobManager.mm#L58-L68), [RCTTiming](https://github.com/facebook/react-native/blob/0617accecdcb11159ba15c34885f294bc206aa89/packages/react-native/React/CoreModules/RCTTiming.mm#L121-L124).

If your module needs to run some cleanup code, then you can conform to the `RCTInvalidating` protocol and implement the `invalidate` method. To do so, you have to:

1. Moduify the `NativeModule.h` file by adding the following lines:

NativeModule.h

```
+ #import <React/RCTInvalidating.h>  
  
//...  
  
- @interface NativeModule : NSObject <NativeModuleSpec>  
+ @interface NativeModule : NSObject <NativeModuleSpec, RCTInvalidating>  
  
//...  
  
@end  

```

2. Implement the `invalidate` method in the `NativeModule.mm` file:

NativeModule.mm

```
  
// ...  
  
@implementation NativeModule  
  
+- (void)invalidate {  
+ // add the cleanup code here  
+}  
  
@end  

```

These are some Native Modules from core that implements the `invalidate` method: [RCTAppearance](https://github.com/facebook/react-native/blob/0617accecdcb11159ba15c34885f294bc206aa89/packages/react-native/React/CoreModules/RCTAppearance.mm#L151-L155), [RCTDeviceInfo](https://github.com/facebook/react-native/blob/0617accecdcb11159ba15c34885f294bc206aa89/packages/react-native/React/CoreModules/RCTDeviceInfo.mm#L127-L133).

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/the-new-architecture/native-modules-lifecycle.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/the-new-architecture/native-modules-lifecycle.md)

Last updated on **Apr 14, 2025**

* [Android](#android)* [iOS](#ios)

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