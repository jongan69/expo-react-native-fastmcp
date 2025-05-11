Turbo Native Modules: iOS · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/turbo-native-modules-ios)

* [Next](/docs/next/turbo-native-modules-ios)* [0.79](/docs/turbo-native-modules-ios)* [0.78](/docs/0.78/turbo-native-modules-ios)* [0.77](/docs/0.77/turbo-native-modules-ios)* [0.76](/docs/0.76/turbo-native-modules-ios)* [0.75](/docs/0.75/getting-started)* [0.74](/docs/0.74/getting-started)* [0.73](/docs/0.73/getting-started)* [0.72](/docs/0.72/getting-started)* [0.71](/docs/0.71/getting-started)* [0.70](/docs/0.70/getting-started)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

On this page

Turbo Native Modules: iOS
=========================

Now it's time to write some iOS platform code to make sure `localStorage` survives after the application is closed.

Prepare your Xcode Project[​](#prepare-your-xcode-project "Direct link to Prepare your Xcode Project")
------------------------------------------------------------------------------------------------------

We need to prepare your iOS project using Xcode. After completing these **6 steps** you'll have `RCTNativeLocalStorage` that implements the generated `NativeLocalStorageSpec` interface.

1. Open the CocoPods generated Xcode Workspace:

bash

```
cd ios  
open TurboModuleExample.xcworkspace  

```

![Open Xcode Workspace](/docs/assets/turbo-native-modules/xcode/1.webp)

2. Right click on app and select `New Group`, call the new group `NativeLocalStorage`.

![Right click on app and select New Group](/docs/assets/turbo-native-modules/xcode/2.webp)

3. In the `NativeLocalStorage` group, create `New`→`File from Template`.

![Create a new file using the Cocoa Touch Class template](/docs/assets/turbo-native-modules/xcode/3.webp)

4. Use the `Cocoa Touch Class`.

![Use the Cocoa Touch Class template](/docs/assets/turbo-native-modules/xcode/4.webp)

5. Name the Cocoa Touch Class `RCTNativeLocalStorage` with the `Objective-C` language.

![Create an Objective-C RCTNativeLocalStorage class](/docs/assets/turbo-native-modules/xcode/5.webp)

6. Rename `RCTNativeLocalStorage.m` → `RCTNativeLocalStorage.mm` making it an Objective-C++ file.

![Convert to and Objective-C++ file](/docs/assets/turbo-native-modules/xcode/6.webp)

Implement localStorage with NSUserDefaults[​](#implement-localstorage-with-nsuserdefaults "Direct link to Implement localStorage with NSUserDefaults")
------------------------------------------------------------------------------------------------------------------------------------------------------

Start by updating `RCTNativeLocalStorage.h`:

NativeLocalStorage/RCTNativeLocalStorage.h

```
//  RCTNativeLocalStorage.h  
//  TurboModuleExample  
  
#import <Foundation/Foundation.h>  
#import <NativeLocalStorageSpec/NativeLocalStorageSpec.h>  
  
NS_ASSUME_NONNULL_BEGIN  
  
@interface RCTNativeLocalStorage : NSObject  
@interface RCTNativeLocalStorage : NSObject <NativeLocalStorageSpec>  
  
@end  

```

Then update our implementation to use `NSUserDefaults` with a custom [suite name](https://developer.apple.com/documentation/foundation/nsuserdefaults/1409957-initwithsuitename).

NativeLocalStorage/RCTNativeLocalStorage.mm

```
//  RCTNativeLocalStorage.m  
//  TurboModuleExample  
  
#import "RCTNativeLocalStorage.h"  
  
static NSString *const RCTNativeLocalStorageKey = @"local-storage";  
  
@interface RCTNativeLocalStorage()  
@property (strong, nonatomic) NSUserDefaults *localStorage;  
@end  
  
@implementation RCTNativeLocalStorage  
  
- (id) init {  
  if (self = [super init]) {  
    _localStorage = [[NSUserDefaults alloc] initWithSuiteName:RCTNativeLocalStorageKey];  
  }  
  return self;  
}  
  
- (std::shared_ptr<facebook::react::TurboModule>)getTurboModule:(const facebook::react::ObjCTurboModule::InitParams &)params {  
  return std::make_shared<facebook::react::NativeLocalStorageSpecJSI>(params);  
}  
  
- (NSString * _Nullable)getItem:(NSString *)key {  
  return [self.localStorage stringForKey:key];  
}  
  
- (void)setItem:(NSString *)value  
          key:(NSString *)key {  
  [self.localStorage setObject:value forKey:key];  
}  
  
- (void)removeItem:(NSString *)key {  
  [self.localStorage removeObjectForKey:key];  
}  
  
- (void)clear {  
  NSDictionary *keys = [self.localStorage dictionaryRepresentation];  
  for (NSString *key in keys) {  
    [self removeItem:key];  
  }  
}  
  
+ (NSString *)moduleName  
{  
  return @"NativeLocalStorage";  
}  
  
@end  

```

Important things to note:

* You can use Xcode to jump to the Codegen `@protocol NativeLocalStorageSpec`. You can also use Xcode to generate stubs for you.

Register the Native Module in your app[​](#register-the-native-module-in-your-app "Direct link to Register the Native Module in your app")
------------------------------------------------------------------------------------------------------------------------------------------

The last step consist in updating the `package.json` to tell React Native about the link between the JS specs of the Native Module and the concrete implementation of those specs in native code.

Modify the `package.json` as it follows:

package.json

```
     "start": "react-native start",  
     "test": "jest"  
   },  
   "codegenConfig": {  
     "name": "AppSpecs",  
     "type": "modules",  
     "jsSrcsDir": "specs",  
     "android": {  
       "javaPackageName": "com.sampleapp.specs"  
     }  
     "ios":  
        "modulesProvider": {  
          "NativeLocalStorage": "RCTNativeLocalStorage"  
        }  
   },  
  
   "dependencies": {  

```

At this point, you need to re-install the pods to make sure that codegen runs again to generate the new files:

bash

```
# from the ios folder  
bundle exec pod install  
open SampleApp.xcworkspace  

```

If you now build your application from Xcode, you should be able to build successfully.

Build and run your code on a Simulator[​](#build-and-run-your-code-on-a-simulator "Direct link to Build and run your code on a Simulator")
------------------------------------------------------------------------------------------------------------------------------------------

* npm* Yarn

bash

```
npm run ios  

```

bash

```
yarn run ios  

```

[](/docs/assets/turbo-native-modules/turbo-native-modules-ios.webm)

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/turbo-native-modules-ios.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/turbo-native-modules-ios.md)

Last updated on **Apr 14, 2025**

* [Prepare your Xcode Project](#prepare-your-xcode-project)* [Implement localStorage with NSUserDefaults](#implement-localstorage-with-nsuserdefaults)* [Register the Native Module in your app](#register-the-native-module-in-your-app)* [Build and run your code on a Simulator](#build-and-run-your-code-on-a-simulator)

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