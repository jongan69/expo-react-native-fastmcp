Native Modules: Introduction · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/turbo-native-modules-introduction)

* [Next](/docs/next/turbo-native-modules-introduction)* [0.79](/docs/turbo-native-modules-introduction)* [0.78](/docs/0.78/turbo-native-modules-introduction)* [0.77](/docs/0.77/turbo-native-modules-introduction)* [0.76](/docs/0.76/turbo-native-modules-introduction)* [0.75](/docs/0.75/getting-started)* [0.74](/docs/0.74/getting-started)* [0.73](/docs/0.73/getting-started)* [0.72](/docs/0.72/getting-started)* [0.71](/docs/0.71/getting-started)* [0.70](/docs/0.70/getting-started)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [The Basics](/docs/getting-started)

  * [Environment setup](/docs/environment-setup)

    * [Workflow](/docs/running-on-device)

      * [UI & Interaction](/docs/style)

        * [Debugging](/docs/debugging)

          * [Testing](/docs/testing-overview)

            * [Performance](/docs/performance)

              * [JavaScript Runtime](/docs/javascript-environment)

                * [Codegen](/docs/the-new-architecture/what-is-codegen)

                  * [Native Development](/docs/native-platform)

                    + [Introduction](/docs/native-platform)+ Modules

                        - [Android and iOS](/docs/turbo-native-modules-introduction)- [Cross-Platform with C++](/docs/the-new-architecture/pure-cxx-modules)- [Advanced Topics](/docs/the-new-architecture/advanced-topics-modules)+ Components

                          - [Android & iOS](/docs/fabric-native-components-introduction)- [Advanced Topics](/docs/the-new-architecture/advanced-topics-components)+ [Miscellaneous](/docs/appendix)* [Android and iOS guides](/docs/headless-js-android)

                      * [Legacy Architecture](/docs/legacy/native-modules-intro)

On this page

Native Modules
==============

Your React Native application code may need to interact with native platform APIs that aren't provided by React Native or an existing library. You can write the integration code yourself using a **Turbo Native Module**. This guide will show you how to write one.

The basic steps are:

1. **define a typed JavaScript specification** using one of the most popular JavaScript type annotation languages: Flow or TypeScript;
2. **configure your dependency management system to run Codegen**, which converts the specification into native language interfaces;
3. **write your application code** using your specification; and
4. **write your native platform code using the generated interfaces** to write and hook your native code into the React Native runtime environment.

Lets work through each of these steps by building an example Turbo Native Module. The rest of this guide assume that you have created your application running the command:

shell

```
npx @react-native-community/cli@latest init TurboModuleExample --version 0.76.0  

```

Native Persistent Storage[​](#native-persistent-storage "Direct link to Native Persistent Storage")
---------------------------------------------------------------------------------------------------

This guide will show you how to write an implementation of the [Web Storage API](https://html.spec.whatwg.org/multipage/webstorage.html#dom-localstorage-dev): `localStorage`. The API is relatable to a React developer who might be writing application code on your project.

To make this work on mobile, we need to use Android and iOS APIs:

* Android: [SharedPreferences](https://developer.android.com/reference/android/content/SharedPreferences), and
* iOS: [NSUserDefaults](https://developer.apple.com/documentation/foundation/nsuserdefaults).

### 1. Declare Typed Specification[​](#1-declare-typed-specification "Direct link to 1. Declare Typed Specification")

React Native provides a tool called [Codegen](/docs/the-new-architecture/what-is-codegen), which takes a specification written in TypeScript or Flow and generates platform specific code for Android and iOS. The specification declares the methods and data types that will pass back and forth between your native code and the React Native JavaScript runtime. A Turbo Native Module is both your specification, the native code you write, and the Codegen interfaces generated from your specification.

To create a specs file:

1. Inside the root folder of your app, create a new folder called `specs`.
2. Create a new file called `NativeLocalStorage.ts`.

info

You can see all of the types you can use in your specification and the native types that are generated in the [Appendix](/docs/appendix) documentation.

Here is an implementation of the `localStorage` specification:

* TypeScript* Flow

specs/NativeLocalStorage.ts

```
import type {TurboModule} from 'react-native';  
import {TurboModuleRegistry} from 'react-native';  
  
export interface Spec extends TurboModule {  
  setItem(value: string, key: string): void;  
  getItem(key: string): string | null;  
  removeItem(key: string): void;  
  clear(): void;  
}  
  
export default TurboModuleRegistry.getEnforcing<Spec>(  
  'NativeLocalStorage',  
);  

```

NativeLocalStorage.js

```
import type {TurboModule} from 'react-native';  
import {TurboModule, TurboModuleRegistry} from 'react-native';  
  
export interface Spec extends TurboModule {  
  setItem(value: string, key: string): void;  
  getItem(key: string): ?string;  
  removeItem(key: string): void;  
  clear(): void;  
}  

```

### 2. Configure Codegen to run[​](#2-configure-codegen-to-run "Direct link to 2. Configure Codegen to run")

The specification is used by the React Native Codegen tools to generate platform specific interfaces and boilerplate for us. To do this, Codegen needs to know where to find our specification and what to do with it. Update your `package.json` to include:

package.json

```
     "start": "react-native start",  
     "test": "jest"  
   },  
   "codegenConfig": {  
     "name": "NativeLocalStorageSpec",  
     "type": "modules",  
     "jsSrcsDir": "specs",  
     "android": {  
       "javaPackageName": "com.nativelocalstorage"  
     }  
   },  
   "dependencies": {  

```

With everything wired up for Codegen, we need to prepare our native code to hook into our generated code.

* Android* iOS

Codegen is executed through the `generateCodegenArtifactsFromSchema` Gradle task:

bash

```
cd android  
./gradlew generateCodegenArtifactsFromSchema  
  
BUILD SUCCESSFUL in 837ms  
14 actionable tasks: 3 executed, 11 up-to-date  

```

This is automatically run when you build your Android application.

Codegen is run as part of the script phases that's automatically added to the project generated by CocoaPods.

bash

```
cd ios  
bundle install  
bundle exec pod install  

```

The output will look like this:

shell

```
...  
Framework build type is static library  
[Codegen] Adding script_phases to ReactCodegen.  
[Codegen] Generating ./build/generated/ios/ReactCodegen.podspec.json  
[Codegen] Analyzing /Users/me/src/TurboModuleExample/package.json  
[Codegen] Searching for codegen-enabled libraries in the app.  
[Codegen] Found TurboModuleExample  
[Codegen] Searching for codegen-enabled libraries in the project dependencies.  
[Codegen] Found react-native  
...  

```

### 3. Write Application Code using the Turbo Native Module[​](#3-write-application-code-using-the-turbo-native-module "Direct link to 3. Write Application Code using the Turbo Native Module")

Using `NativeLocalStorage`, here’s a modified `App.tsx` that includes some text we want persisted, an input field and some buttons to update this value.

The `TurboModuleRegistry` supports 2 modes of retrieving a Turbo Native Module:

* `get<T>(name: string): T | null` which will return `null` if the Turbo Native Module is unavailable.
* `getEnforcing<T>(name: string): T` which will throw an exception if the Turbo Native Module is unavailable. This assumes the module is always available.

App.tsx

```
import React from 'react';  
import {  
  SafeAreaView,  
  StyleSheet,  
  Text,  
  TextInput,  
  Button,  
} from 'react-native';  
  
import NativeLocalStorage from './specs/NativeLocalStorage';  
  
const EMPTY = '<empty>';  
  
function App(): React.JSX.Element {  
  const [value, setValue] = React.useState<string | null>(null);  
  
  const [editingValue, setEditingValue] = React.useState<  
    string | null  
  >(null);  
  
  React.useEffect(() => {  
    const storedValue = NativeLocalStorage?.getItem('myKey');  
    setValue(storedValue ?? '');  
  }, []);  
  
  function saveValue() {  
    NativeLocalStorage?.setItem(editingValue ?? EMPTY, 'myKey');  
    setValue(editingValue);  
  }  
  
  function clearAll() {  
    NativeLocalStorage?.clear();  
    setValue('');  
  }  
  
  function deleteValue() {  
    NativeLocalStorage?.removeItem('myKey');  
    setValue('');  
  }  
  
  return (  
    <SafeAreaView style={{flex: 1}}>  
      <Text style={styles.text}>  
        Current stored value is: {value ?? 'No Value'}  
      </Text>  
      <TextInput  
        placeholder="Enter the text you want to store"  
        style={styles.textInput}  
        onChangeText={setEditingValue}  
      />  
      <Button title="Save" onPress={saveValue} />  
      <Button title="Delete" onPress={deleteValue} />  
      <Button title="Clear" onPress={clearAll} />  
    </SafeAreaView>  
  );  
}  
  
const styles = StyleSheet.create({  
  text: {  
    margin: 10,  
    fontSize: 20,  
  },  
  textInput: {  
    margin: 10,  
    height: 40,  
    borderColor: 'black',  
    borderWidth: 1,  
    paddingLeft: 5,  
    paddingRight: 5,  
    borderRadius: 5,  
  },  
});  
  
export default App;  

```

### 4. Write your Native Platform code[​](#4-write-your-native-platform-code "Direct link to 4. Write your Native Platform code")

With everything prepared, we're going to start writing native platform code. We do this in 2 parts:

note

This guide shows you how to create a Turbo Native Module that only works with the New Architecture. If you need to support both the New Architecture and the Legacy Architecture, please refer to our [backwards compatibility guide](https://github.com/reactwg/react-native-new-architecture/blob/main/docs/backwards-compat.md).

* Android* iOS

Now it's time to write some Android platform code to make sure `localStorage` survives after the application is closed.

The first step is to implement the generated `NativeLocalStorageSpec` interface:

* Java* Kotlin

android/app/src/main/java/com/nativelocalstorage/NativeLocalStorageModule.java

```
package com.nativelocalstorage;  
  
import android.content.Context;  
import android.content.SharedPreferences;  
import com.nativelocalstorage.NativeLocalStorageSpec;  
import com.facebook.react.bridge.ReactApplicationContext;  
  
public class NativeLocalStorageModule extends NativeLocalStorageSpec {  
  
  public static final String NAME = "NativeLocalStorage";  
  
  public NativeLocalStorageModule(ReactApplicationContext reactContext) {  
    super(reactContext);  
  }  
  
  @Override  
  public String getName() {  
    return NAME;  
  }  
  
  @Override  
  public void setItem(String value, String key) {  
    SharedPreferences sharedPref = getReactApplicationContext().getSharedPreferences("my_prefs", Context.MODE_PRIVATE);  
    SharedPreferences.Editor editor = sharedPref.edit();  
    editor.putString(key, value);  
    editor.apply();  
  }  
  
  @Override  
  public String getItem(String key) {  
    SharedPreferences sharedPref = getReactApplicationContext().getSharedPreferences("my_prefs", Context.MODE_PRIVATE);  
    String username = sharedPref.getString(key, null);  
    return username;  
  }  
  
  @Override  
  public void removeItem(String key) {  
    SharedPreferences sharedPref = getReactApplicationContext().getSharedPreferences("my_prefs", Context.MODE_PRIVATE);  
    sharedPref.edit().remove(key).apply();  
  }  
}  

```

android/app/src/main/java/com/nativelocalstorage/NativeLocalStorageModule.kt

```
package com.nativelocalstorage  
  
import android.content.Context  
import android.content.SharedPreferences  
import com.nativelocalstorage.NativeLocalStorageSpec  
import com.facebook.react.bridge.ReactApplicationContext  
  
class NativeLocalStorageModule(reactContext: ReactApplicationContext) : NativeLocalStorageSpec(reactContext) {  
  
  override fun getName() = NAME  
  
  override fun setItem(value: String, key: String) {  
    val sharedPref = getReactApplicationContext().getSharedPreferences("my_prefs", Context.MODE_PRIVATE)  
    val editor = sharedPref.edit()  
    editor.putString(key, value)  
    editor.apply()  
  }  
  
  override fun getItem(key: String): String? {  
    val sharedPref = getReactApplicationContext().getSharedPreferences("my_prefs", Context.MODE_PRIVATE)  
    val username = sharedPref.getString(key, null)  
    return username.toString()  
  }  
  
  override fun removeItem(key: String) {  
    val sharedPref = getReactApplicationContext().getSharedPreferences("my_prefs", Context.MODE_PRIVATE)  
    val editor = sharedPref.edit()  
    editor.remove(key)  
    editor.apply()  
  }  
  
  override fun clear() {  
    val sharedPref = getReactApplicationContext().getSharedPreferences("my_prefs", Context.MODE_PRIVATE)  
    val editor = sharedPref.edit()  
    editor.clear()  
    editor.apply()  
  }  
  
  companion object {  
    const val NAME = "NativeLocalStorage"  
  }  
}  

```

Next we need to create `NativeLocalStoragePackage`. It provides an object to register our Module in the React Native runtime, by wrapping it as a Base Native Package:

* Java* Kotlin

android/app/src/main/java/com/nativelocalstorage/NativeLocalStoragePackage.java

```
package com.nativelocalstorage;  
  
import com.facebook.react.BaseReactPackage;  
import com.facebook.react.bridge.NativeModule;  
import com.facebook.react.bridge.ReactApplicationContext;  
import com.facebook.react.module.model.ReactModuleInfo;  
import com.facebook.react.module.model.ReactModuleInfoProvider;  
  
import java.util.HashMap;  
import java.util.Map;  
  
public class NativeLocalStoragePackage extends BaseReactPackage {  
  
  @Override  
  public NativeModule getModule(String name, ReactApplicationContext reactContext) {  
    if (name.equals(NativeLocalStorageModule.NAME)) {  
      return new NativeLocalStorageModule(reactContext);  
    } else {  
      return null;  
    }  
  }  
  
  @Override  
  public ReactModuleInfoProvider getReactModuleInfoProvider() {  
    return new ReactModuleInfoProvider() {  
      @Override  
      public Map<String, ReactModuleInfo> getReactModuleInfos() {  
        Map<String, ReactModuleInfo> map = new HashMap<>();  
        map.put(NativeLocalStorageModule.NAME, new ReactModuleInfo(  
          NativeLocalStorageModule.NAME,       // name  
          NativeLocalStorageModule.NAME,       // className  
          false, // canOverrideExistingModule  
          false, // needsEagerInit  
          false, // isCXXModule  
          true   // isTurboModule  
        ));  
        return map;  
      }  
    };  
  }  
}  

```

android/app/src/main/java/com/nativelocalstorage/NativeLocalStoragePackage.kt

```
package com.nativelocalstorage  
  
import com.facebook.react.BaseReactPackage  
import com.facebook.react.bridge.NativeModule  
import com.facebook.react.bridge.ReactApplicationContext  
import com.facebook.react.module.model.ReactModuleInfo  
import com.facebook.react.module.model.ReactModuleInfoProvider  
  
class NativeLocalStoragePackage : BaseReactPackage() {  
  
  override fun getModule(name: String, reactContext: ReactApplicationContext): NativeModule? =  
    if (name == NativeLocalStorageModule.NAME) {  
      NativeLocalStorageModule(reactContext)  
    } else {  
      null  
    }  
  
  override fun getReactModuleInfoProvider() = ReactModuleInfoProvider {  
    mapOf(  
      NativeLocalStorageModule.NAME to ReactModuleInfo(  
        name = NativeLocalStorageModule.NAME,  
        className = NativeLocalStorageModule.NAME,  
        canOverrideExistingModule = false,  
        needsEagerInit = false,  
        isCxxModule = false,  
        isTurboModule = true  
      )  
    )  
  }  
}  

```

Finally, we need to tell the React Native in our main application how to find this `Package`. We call this "registering" the package in React Native.

In this case, you add it to be returned by the [getPackages](https://github.com/facebook/react-native/blob/8d8b8c343e62115a5509e1aed62047053c2f6e39/packages/react-native/ReactAndroid/src/main/java/com/facebook/react/ReactNativeHost.java#L233) method.

info

Later you’ll learn how to distribute your Native Modules as [npm packages](/docs/the-new-architecture/create-module-library#publish-the-library-on-npm), which our build tooling will autolink for you.

* Java* Kotlin

android/app/src/main/java/com/turobmoduleexample/MainApplication.java

```
package com.inappmodule;  
  
import android.app.Application;  
import com.facebook.react.PackageList;  
import com.facebook.react.ReactApplication;  
import com.facebook.react.ReactHost;  
import com.facebook.react.ReactNativeHost;  
import com.facebook.react.ReactPackage;  
import com.facebook.react.defaults.DefaultNewArchitectureEntryPoint;  
import com.facebook.react.defaults.DefaultReactHost;  
import com.facebook.react.defaults.DefaultReactNativeHost;  
import com.facebook.soloader.SoLoader;  
import com.nativelocalstorage.NativeLocalStoragePackage;  
  
import java.util.ArrayList;  
import java.util.List;  
  
public class MainApplication extends Application implements ReactApplication {  
  
  private final ReactNativeHost reactNativeHost = new DefaultReactNativeHost(this) {  
    @Override  
    public List<ReactPackage> getPackages() {  
      List<ReactPackage> packages = new PackageList(this).getPackages();  
      // Packages that cannot be autolinked yet can be added manually here, for example:  
      // packages.add(new MyReactNativePackage());  
      packages.add(new NativeLocalStoragePackage());  
      return packages;  
    }  
  
    @Override  
    public String getJSMainModuleName() {  
      return "index";  
    }  
  
    @Override  
    public boolean getUseDeveloperSupport() {  
      return BuildConfig.DEBUG;  
    }  
  
    @Override  
    public boolean isNewArchEnabled() {  
      return BuildConfig.IS_NEW_ARCHITECTURE_ENABLED;  
    }  
  
    @Override  
    public boolean isHermesEnabled() {  
      return BuildConfig.IS_HERMES_ENABLED;  
    }  
  };  
  
  @Override  
  public ReactHost getReactHost() {  
    return DefaultReactHost.getDefaultReactHost(getApplicationContext(), reactNativeHost);  
  }  
  
  @Override  
  public void onCreate() {  
    super.onCreate();  
    SoLoader.init(this, false);  
    if (BuildConfig.IS_NEW_ARCHITECTURE_ENABLED) {  
      // If you opted-in for the New Architecture, we load the native entry point for this app.  
      DefaultNewArchitectureEntryPoint.load();  
    }  
  }  
}  

```

android/app/src/main/java/com/turobmoduleexample/MainApplication.kt

```
package com.inappmodule  
  
import android.app.Application  
import com.facebook.react.PackageList  
import com.facebook.react.ReactApplication  
import com.facebook.react.ReactHost  
import com.facebook.react.ReactNativeHost  
import com.facebook.react.ReactPackage  
import com.facebook.react.defaults.DefaultNewArchitectureEntryPoint.load  
import com.facebook.react.defaults.DefaultReactHost.getDefaultReactHost  
import com.facebook.react.defaults.DefaultReactNativeHost  
import com.facebook.soloader.SoLoader  
import com.nativelocalstorage.NativeLocalStoragePackage  
  
class MainApplication : Application(), ReactApplication {  
  
  override val reactNativeHost: ReactNativeHost =  
      object : DefaultReactNativeHost(this) {  
        override fun getPackages(): List<ReactPackage> =  
            PackageList(this).packages.apply {  
              // Packages that cannot be autolinked yet can be added manually here, for example:  
              // add(MyReactNativePackage())  
              add(NativeLocalStoragePackage())  
            }  
  
        override fun getJSMainModuleName(): String = "index"  
  
        override fun getUseDeveloperSupport(): Boolean = BuildConfig.DEBUG  
  
        override val isNewArchEnabled: Boolean = BuildConfig.IS_NEW_ARCHITECTURE_ENABLED  
        override val isHermesEnabled: Boolean = BuildConfig.IS_HERMES_ENABLED  
      }  
  
  override val reactHost: ReactHost  
    get() = getDefaultReactHost(applicationContext, reactNativeHost)  
  
  override fun onCreate() {  
    super.onCreate()  
    SoLoader.init(this, false)  
    if (BuildConfig.IS_NEW_ARCHITECTURE_ENABLED) {  
      // If you opted-in for the New Architecture, we load the native entry point for this app.  
      load()  
    }  
  }  
}  

```

You can now build and run your code on an emulator:

* npm* Yarn

bash

```
npm run android  

```

bash

```
yarn run android  

```

[](/docs/assets/turbo-native-modules/turbo-native-modules-android.webm)

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

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/turbo-native-modules.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/turbo-native-modules.md)

Last updated on **Apr 14, 2025**

[Previous

Introduction](/docs/native-platform)[Next

Cross-Platform with C++](/docs/the-new-architecture/pure-cxx-modules)

* [Native Persistent Storage](#native-persistent-storage)
  + [1. Declare Typed Specification](#1-declare-typed-specification)+ [2. Configure Codegen to run](#2-configure-codegen-to-run)+ [3. Write Application Code using the Turbo Native Module](#3-write-application-code-using-the-turbo-native-module)+ [4. Write your Native Platform code](#4-write-your-native-platform-code)

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