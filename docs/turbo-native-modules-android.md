Turbo Native Modules: Android · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/turbo-native-modules-android)

* [Next](/docs/next/turbo-native-modules-android)* [0.79](/docs/turbo-native-modules-android)* [0.78](/docs/0.78/turbo-native-modules-android)* [0.77](/docs/0.77/turbo-native-modules-android)* [0.76](/docs/0.76/turbo-native-modules-android)* [0.75](/docs/0.75/getting-started)* [0.74](/docs/0.74/getting-started)* [0.73](/docs/0.73/getting-started)* [0.72](/docs/0.72/getting-started)* [0.71](/docs/0.71/getting-started)* [0.70](/docs/0.70/getting-started)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

Turbo Native Modules: Android
=============================

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

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/turbo-native-modules-android.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/turbo-native-modules-android.md)

Last updated on **Apr 14, 2025**

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