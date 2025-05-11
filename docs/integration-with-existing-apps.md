Integration with Existing Apps · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/integration-with-existing-apps)

* [Next](/docs/next/integration-with-existing-apps)* [0.79](/docs/integration-with-existing-apps)* [0.78](/docs/0.78/integration-with-existing-apps)* [0.77](/docs/0.77/integration-with-existing-apps)* [0.76](/docs/0.76/integration-with-existing-apps)* [0.75](/docs/0.75/integration-with-existing-apps)* [0.74](/docs/0.74/integration-with-existing-apps)* [0.73](/docs/0.73/integration-with-existing-apps)* [0.72](/docs/0.72/integration-with-existing-apps)* [0.71](/docs/0.71/integration-with-existing-apps)* [0.70](/docs/0.70/integration-with-existing-apps)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [The Basics](/docs/getting-started)

  * [Environment setup](/docs/environment-setup)

    + [Get Started with React Native](/docs/environment-setup)+ [Set Up Your Environment](/docs/set-up-your-environment)+ [Integration with Existing Apps](/docs/integration-with-existing-apps)+ [Integration with an Android Fragment](/docs/integration-with-android-fragment)+ [Building For TV Devices](/docs/building-for-tv)+ [Out-of-Tree Platforms](/docs/out-of-tree-platforms)* [Workflow](/docs/running-on-device)

      * [UI & Interaction](/docs/style)

        * [Debugging](/docs/debugging)

          * [Testing](/docs/testing-overview)

            * [Performance](/docs/performance)

              * [JavaScript Runtime](/docs/javascript-environment)

                * [Codegen](/docs/the-new-architecture/what-is-codegen)

                  * [Native Development](/docs/native-platform)

                    * [Android and iOS guides](/docs/headless-js-android)

                      * [Legacy Architecture](/docs/legacy/native-modules-intro)

Integration with Existing Apps
==============================

React Native is great when you are starting a new mobile app from scratch. However, it also works well for adding a single view or user flow to existing native applications. With a few steps, you can add new React Native based features, screens, views, etc.

The specific steps are different depending on what platform you're targeting.

* Android (Java & Kotlin)* iOS (Objective-C and Swift)

Key Concepts[​](#key-concepts "Direct link to Key Concepts")
------------------------------------------------------------

The keys to integrating React Native components into your Android application are to:

1. Set up the correct directory structure.
2. Install the necessary NPM dependencies.
3. Adding React Native to your Gradle configuration.
4. Writing the TypeScript code for your first React Native screen.
5. Integrate React Native with your Android code using a ReactActivity.
6. Testing your integration by running the bundler and seeing your app in action.

Using the Community Template[​](#using-the-community-template "Direct link to Using the Community Template")
------------------------------------------------------------------------------------------------------------

While you follow this guide, we suggest you to use the [React Native Community Template](https://github.com/react-native-community/template/) as reference. The template contains a **minimal Android app** and will help you understanding how to integrate React Native into an existing Android app.

Prerequisites[​](#prerequisites "Direct link to Prerequisites")
---------------------------------------------------------------

Follow the guide on [setting up your development environment](/docs/set-up-your-environment) and using [React Native without a framework](/docs/getting-started-without-a-framework) to configure your development environment for building React Native apps for Android.
This guide also assumes you're familiar with the basics of Android development such as creating Activities and editing the `AndroidManifest.xml` file.

1. Set up directory structure[​](#1-set-up-directory-structure "Direct link to 1. Set up directory structure")
--------------------------------------------------------------------------------------------------------------

To ensure a smooth experience, create a new folder for your integrated React Native project, then **move your existing Android project** to the `/android` subfolder.

2. Install NPM dependencies[​](#2-install-npm-dependencies "Direct link to 2. Install NPM dependencies")
--------------------------------------------------------------------------------------------------------

Go to the root directory and run the following command:

shell

```
curl -O https://raw.githubusercontent.com/react-native-community/template/refs/heads/0.75-stable/template/package.json  

```

This will copy the `package.json` [file from the Community template](https://github.com/react-native-community/template/blob/0.75-stable/template/package.json) to your project.

Next, install the NPM packages by running:

* npm* Yarn

shell

```
npm install  

```

shell

```
yarn install  

```

Installation process has created a new `node_modules` folder. This folder stores all the JavaScript dependencies required to build your project.

Add `node_modules/` to your `.gitignore` file (here the [Community default one](https://github.com/react-native-community/template/blob/0.75-stable/template/_gitignore)).

3. Adding React Native to your app[​](#3-adding-react-native-to-your-app "Direct link to 3. Adding React Native to your app")
-----------------------------------------------------------------------------------------------------------------------------

### Configuring Gradle[​](#configuring-gradle "Direct link to Configuring Gradle")

React Native uses the React Native Gradle Plugin to configure your dependencies and project setup.

First, let's edit your `settings.gradle` file by adding those lines (as suggested from the [Community template](https://github.com/react-native-community/template/blob/0.77-stable/template/android/settings.gradle)):

groovy

```
// Configures the React Native Gradle Settings plugin used for autolinking  
pluginManagement { includeBuild("../node_modules/@react-native/gradle-plugin") }  
plugins { id("com.facebook.react.settings") }  
extensions.configure(com.facebook.react.ReactSettingsExtension){ ex -> ex.autolinkLibrariesFromCommand() }  
// If using .gradle.kts files:  
// extensions.configure<com.facebook.react.ReactSettingsExtension> { autolinkLibrariesFromCommand() }  
includeBuild("../node_modules/@react-native/gradle-plugin")  
  
// Include your existing Gradle modules here.  
// include(":app")  

```

Then you need to open your top level `build.gradle` and include this line (as suggested from the [Community template](https://github.com/react-native-community/template/blob/0.77-stable/template/android/build.gradle)):

diff

```
buildscript {  
    repositories {  
        google()  
        mavenCentral()  
    }  
    dependencies {  
        classpath("com.android.tools.build:gradle:7.3.1")  
+       classpath("com.facebook.react:react-native-gradle-plugin")  
    }  
}  

```

This makes sure the React Native Gradle Plugin (RNGP) is available inside your project.
Finally, add those lines inside your Applications's `build.gradle` file (it's a different `build.gradle` file usually inside your `app` folder - you can use the [Community template file as reference](https://github.com/react-native-community/template/blob/0.77-stable/template/android/app/build.gradle)):

diff

```
apply plugin: "com.android.application"  
+apply plugin: "com.facebook.react"  
  
repositories {  
    mavenCentral()  
}  
  
dependencies {  
    // Other dependencies here  
+   // Note: we intentionally don't specify the version number here as RNGP will take care of it.  
+   // If you don't use the RNGP, you'll have to specify version manually.  
+   implementation("com.facebook.react:react-android")  
+   implementation("com.facebook.react:hermes-android")  
}  
  
+react {  
+   // Needed to enable Autolinking - https://github.com/react-native-community/cli/blob/master/docs/autolinking.md  
+   autolinkLibrariesWithApp()  
+}  

```

Finally, open your application `gradle.properties` files and add the following line (here the [Community template file as reference](https://github.com/react-native-community/template/blob/0.77-stable/template/android/gradle.properties)):

diff

```
+reactNativeArchitectures=armeabi-v7a,arm64-v8a,x86,x86_64  
+newArchEnabled=true  
+hermesEnabled=true  

```

### Configuring your manifest[​](#configuring-your-manifest "Direct link to Configuring your manifest")

First, make sure you have the Internet permission in your `AndroidManifest.xml`:

diff

```
<manifest xmlns:android="http://schemas.android.com/apk/res/android">  
  
+   <uses-permission android:name="android.permission.INTERNET" />  
  
    <application  
      android:name=".MainApplication">  
    </application>  
</manifest>  

```

Then you need to enable [cleartext traffic](https://developer.android.com/training/articles/security-config#CleartextTrafficPermitted) in your **debug** `AndroidManifest.xml`:

diff

```
<?xml version="1.0" encoding="utf-8"?>  
<manifest xmlns:android="http://schemas.android.com/apk/res/android"  
    xmlns:tools="http://schemas.android.com/tools">  
  
    <application  
+       android:usesCleartextTraffic="true"  
+       tools:targetApi="28"  
    />  
</manifest>  

```

As usual, here the AndroidManifest.xml file from the Community template to use as a reference: [main](https://github.com/react-native-community/template/blob/0.77-stable/template/android/app/src/main/AndroidManifest.xml) and [debug](https://github.com/react-native-community/template/blob/0.77-stable/template/android/app/src/debug/AndroidManifest.xml)

This is needed as your application will communicate with your local bundler, [Metro][<https://metrobundler.dev/>], via HTTP.

Make sure you add this only to your **debug** manifest.

4. Writing the TypeScript Code[​](#4-writing-the-typescript-code "Direct link to 4. Writing the TypeScript Code")
-----------------------------------------------------------------------------------------------------------------

Now we will actually modify the native Android application to integrate React Native.

The first bit of code we will write is the actual React Native code for the new screen that will be integrated into our application.

### Create a `index.js` file[​](#create-a-indexjs-file "Direct link to create-a-indexjs-file")

First, create an empty `index.js` file in the root of your React Native project.

`index.js` is the starting point for React Native applications, and it is always required. It can be a small file that `import`s other file that are part of your React Native component or application, or it can contain all the code that is needed for it.

Our index.js should look as follows (here the [Community template file as reference](https://github.com/react-native-community/template/blob/0.77-stable/template/index.js)):

js

```
import {AppRegistry} from 'react-native';  
import App from './App';  
  
AppRegistry.registerComponent('HelloWorld', () => App);  

```

### Create a `App.tsx` file[​](#create-a-apptsx-file "Direct link to create-a-apptsx-file")

Let's create an `App.tsx` file. This is a [TypeScript](https://www.typescriptlang.org/) file that can have [JSX](https://en.wikipedia.org/wiki/JSX_(JavaScript)) expressions. It contains the root React Native component that we will integrate into our Android application ([link](https://github.com/react-native-community/template/blob/0.77-stable/template/App.tsx)):

tsx

```
import React from 'react';  
import {  
  SafeAreaView,  
  ScrollView,  
  StatusBar,  
  StyleSheet,  
  Text,  
  useColorScheme,  
  View,  
} from 'react-native';  
  
import {  
  Colors,  
  DebugInstructions,  
  Header,  
  ReloadInstructions,  
} from 'react-native/Libraries/NewAppScreen';  
  
function App(): React.JSX.Element {  
  const isDarkMode = useColorScheme() === 'dark';  
  
  const backgroundStyle = {  
    backgroundColor: isDarkMode ? Colors.darker : Colors.lighter,  
  };  
  
  return (  
    <SafeAreaView style={backgroundStyle}>  
      <StatusBar  
        barStyle={isDarkMode ? 'light-content' : 'dark-content'}  
        backgroundColor={backgroundStyle.backgroundColor}  
      />  
      <ScrollView  
        contentInsetAdjustmentBehavior="automatic"  
        style={backgroundStyle}>  
        <Header />  
        <View  
          style={{  
            backgroundColor: isDarkMode  
              ? Colors.black  
              : Colors.white,  
            padding: 24,  
          }}>  
          <Text style={styles.title}>Step One</Text>  
          <Text>  
            Edit <Text style={styles.bold}>App.tsx</Text> to  
            change this screen and see your edits.  
          </Text>  
          <Text style={styles.title}>See your changes</Text>  
          <ReloadInstructions />  
          <Text style={styles.title}>Debug</Text>  
          <DebugInstructions />  
        </View>  
      </ScrollView>  
    </SafeAreaView>  
  );  
}  
  
const styles = StyleSheet.create({  
  title: {  
    fontSize: 24,  
    fontWeight: '600',  
  },  
  bold: {  
    fontWeight: '700',  
  },  
});  
  
export default App;  

```

Here the [Community template file as reference](https://github.com/react-native-community/template/blob/0.77-stable/template/App.tsx)

5. Integrating with your Android code[​](#5-integrating-with-your-android-code "Direct link to 5. Integrating with your Android code")
--------------------------------------------------------------------------------------------------------------------------------------

We now need to add some native code in order to start the React Native runtime and tell it to render our React components.

### Updating your Application class[​](#updating-your-application-class "Direct link to Updating your Application class")

First, we need to update your `Application` class to properly initialize React Native as follows:

* Java* Kotlin

diff

```
package <your-package-here>;  
  
import android.app.Application;  
+import com.facebook.react.PackageList;  
+import com.facebook.react.ReactApplication;  
+import com.facebook.react.ReactHost;  
+import com.facebook.react.ReactNativeHost;  
+import com.facebook.react.ReactPackage;  
+import com.facebook.react.defaults.DefaultNewArchitectureEntryPoint;  
+import com.facebook.react.defaults.DefaultReactHost;  
+import com.facebook.react.defaults.DefaultReactNativeHost;  
+import com.facebook.soloader.SoLoader;  
+import com.facebook.react.soloader.OpenSourceMergedSoMapping  
+import java.util.List;  
  
-class MainApplication extends Application {  
+class MainApplication extends Application implements ReactApplication {  
+ @Override  
+ public ReactNativeHost getReactNativeHost() {  
+   return new DefaultReactNativeHost(this) {  
+     @Override  
+     protected List<ReactPackage> getPackages() { return new PackageList(this).getPackages(); }  
+     @Override  
+     protected String getJSMainModuleName() { return "index"; }  
+     @Override  
+     public boolean getUseDeveloperSupport() { return BuildConfig.DEBUG; }  
+     @Override  
+     protected boolean isNewArchEnabled() { return BuildConfig.IS_NEW_ARCHITECTURE_ENABLED; }  
+     @Override  
+     protected Boolean isHermesEnabled() { return BuildConfig.IS_HERMES_ENABLED; }  
+   };  
+ }  
  
+ @Override  
+ public ReactHost getReactHost() {  
+   return DefaultReactHost.getDefaultReactHost(getApplicationContext(), getReactNativeHost());  
+ }  
  
  @Override  
  public void onCreate() {  
    super.onCreate();  
+   SoLoader.init(this, OpenSourceMergedSoMapping);  
+   if (BuildConfig.IS_NEW_ARCHITECTURE_ENABLED) {  
+     DefaultNewArchitectureEntryPoint.load();  
+   }  
  }  
}  

```

diff

```
// package <your-package-here>  
  
import android.app.Application  
+import com.facebook.react.PackageList  
+import com.facebook.react.ReactApplication  
+import com.facebook.react.ReactHost  
+import com.facebook.react.ReactNativeHost  
+import com.facebook.react.ReactPackage  
+import com.facebook.react.defaults.DefaultNewArchitectureEntryPoint.load  
+import com.facebook.react.defaults.DefaultReactHost.getDefaultReactHost  
+import com.facebook.react.defaults.DefaultReactNativeHost  
+import com.facebook.soloader.SoLoader  
+import com.facebook.react.soloader.OpenSourceMergedSoMapping  
  
-class MainApplication : Application() {  
+class MainApplication : Application(), ReactApplication {  
  
+ override val reactNativeHost: ReactNativeHost =  
+      object : DefaultReactNativeHost(this) {  
+        override fun getPackages(): List<ReactPackage> = PackageList(this).packages  
+        override fun getJSMainModuleName(): String = "index"  
+        override fun getUseDeveloperSupport(): Boolean = BuildConfig.DEBUG  
+        override val isNewArchEnabled: Boolean = BuildConfig.IS_NEW_ARCHITECTURE_ENABLED  
+        override val isHermesEnabled: Boolean = BuildConfig.IS_HERMES_ENABLED  
+      }  
  
+ override val reactHost: ReactHost  
+   get() = getDefaultReactHost(applicationContext, reactNativeHost)  
  
  override fun onCreate() {  
    super.onCreate()  
+   SoLoader.init(this, OpenSourceMergedSoMapping)  
+   if (BuildConfig.IS_NEW_ARCHITECTURE_ENABLED) {  
+     load()  
+   }  
  }  
}  

```

As usual, here the [MainApplication.kt Community template file as reference](https://github.com/react-native-community/template/blob/0.77-stable/template/android/app/src/main/java/com/helloworld/MainApplication.kt)

#### Creating a `ReactActivity`[​](#creating-a-reactactivity "Direct link to creating-a-reactactivity")

Finally, we need to create a new `Activity` that will extend `ReactActivity` and host the React Native code. This activity will be responsible for starting the React Native runtime and rendering the React component.

* Java* Kotlin

java

```
// package <your-package-here>;  
  
import com.facebook.react.ReactActivity;  
import com.facebook.react.ReactActivityDelegate;  
import com.facebook.react.defaults.DefaultNewArchitectureEntryPoint;  
import com.facebook.react.defaults.DefaultReactActivityDelegate;  
  
public class MyReactActivity extends ReactActivity {  
  
    @Override  
    protected String getMainComponentName() {  
        return "HelloWorld";  
    }  
  
    @Override  
    protected ReactActivityDelegate createReactActivityDelegate() {  
        return new DefaultReactActivityDelegate(this, getMainComponentName(), DefaultNewArchitectureEntryPoint.getFabricEnabled());  
    }  
}  

```

kotlin

```
// package <your-package-here>  
  
import com.facebook.react.ReactActivity  
import com.facebook.react.ReactActivityDelegate  
import com.facebook.react.defaults.DefaultNewArchitectureEntryPoint.fabricEnabled  
import com.facebook.react.defaults.DefaultReactActivityDelegate  
  
class MyReactActivity : ReactActivity() {  
  
    override fun getMainComponentName(): String = "HelloWorld"  
  
    override fun createReactActivityDelegate(): ReactActivityDelegate =  
        DefaultReactActivityDelegate(this, mainComponentName, fabricEnabled)  
}  

```

As usual, here the [MainActivity.kt Community template file as reference](https://github.com/react-native-community/template/blob/0.77-stable/template/android/app/src/main/java/com/helloworld/MainApplication.kt)

Whenever you create a new Activity, you need to add it to your `AndroidManifest.xml` file. You also need set the theme of `MyReactActivity` to `Theme.AppCompat.Light.NoActionBar` (or to any non-ActionBar theme) as otherwise your application will render an ActionBar on top of your React Native screen:

diff

```
<manifest xmlns:android="http://schemas.android.com/apk/res/android">  
  
    <uses-permission android:name="android.permission.INTERNET" />  
  
    <application  
      android:name=".MainApplication">  
  
+     <activity  
+       android:name=".MyReactActivity"  
+       android:label="@string/app_name"  
+       android:theme="@style/Theme.AppCompat.Light.NoActionBar">  
+     </activity>  
    </application>  
</manifest>  

```

Now your activity is ready to run some JavaScript code.

6. Test your integration[​](#6-test-your-integration "Direct link to 6. Test your integration")
-----------------------------------------------------------------------------------------------

You have completed all the basic steps to integrate React Native with your application. Now we will start the [Metro bundler](https://metrobundler.dev/) to build your TypeScript application code into a bundle. Metro's HTTP server shares the bundle from `localhost` on your developer environment to a simulator or device. This allows for [hot reloading](https://reactnative.dev/blog/2016/03/24/introducing-hot-reloading).

First, you need to create a `metro.config.js` file in the root of your project as follows:

js

```
const {getDefaultConfig} = require('@react-native/metro-config');  
module.exports = getDefaultConfig(__dirname);  

```

You can checkout the [metro.config.js file](https://github.com/react-native-community/template/blob/0.77-stable/template/metro.config.js) from the Community template file as reference.

Once you have the config file in place, you can run the bundler. Run the following command in the root directory of your project:

* npm* Yarn

shell

```
npm start  

```

shell

```
yarn start  

```

Now build and run your Android app as normal.

Once you reach your React-powered Activity inside the app, it should load the JavaScript code from the development server and display:

![](/docs/assets/EmbeddedAppAndroidVideo.gif)

### Creating a release build in Android Studio[​](#creating-a-release-build-in-android-studio "Direct link to Creating a release build in Android Studio")

You can use Android Studio to create your release builds too! It’s as quick as creating release builds of your previously-existing native Android app.

The React Native Gradle Plugin will take care of bundling the JS code inside your APK/App Bundle.

If you're not using Android Studio, you can create a release build with:

```
cd android  
# For a Release APK  
./gradlew :app:assembleRelease  
# For a Release AAB  
./gradlew :app:bundleRelease  

```

### Now what?[​](#now-what "Direct link to Now what?")

At this point you can continue developing your app as usual. Refer to our [debugging](/docs/debugging) and [deployment](/docs/running-on-device) docs to learn more about working with React Native.

Key Concepts[​](#key-concepts "Direct link to Key Concepts")
------------------------------------------------------------

The keys to integrating React Native components into your iOS application are to:

1. Set up the correct directory structure.
2. Install the necessary NPM dependencies.
3. Adding React Native to your Podfile configuration.
4. Writing the TypeScript code for your first React Native screen.
5. Integrate React Native with your iOS code using a `RCTRootView`.
6. Testing your integration by running the bundler and seeing your app in action.

Using the Community Template[​](#using-the-community-template "Direct link to Using the Community Template")
------------------------------------------------------------------------------------------------------------

While you follow this guide, we suggest you to use the [React Native Community Template](https://github.com/react-native-community/template/) as reference. The template contains a **minimal iOS app** and will help you understanding how to integrate React Native into an existing iOS app.

Prerequisites[​](#prerequisites "Direct link to Prerequisites")
---------------------------------------------------------------

Follow the guide on [setting up your development environment](/docs/set-up-your-environment) and using [React Native without a framework](/docs/getting-started-without-a-framework) to configure your development environment for building React Native apps for iOS.
This guide also assumes you're familiar with the basics of iOS development such as creating a `UIViewController` and editing the `Podfile` file.

### 1. Set up directory structure[​](#1-set-up-directory-structure "Direct link to 1. Set up directory structure")

To ensure a smooth experience, create a new folder for your integrated React Native project, then **move your existing iOS project** to the `/ios` subfolder.

2. Install NPM dependencies[​](#2-install-npm-dependencies "Direct link to 2. Install NPM dependencies")
--------------------------------------------------------------------------------------------------------

Go to the root directory and run the following command:

shell

```
curl -O https://raw.githubusercontent.com/react-native-community/template/refs/heads/0.78-stable/template/package.json  

```

This will copy the `package.json` [file from the Community template](https://github.com/react-native-community/template/blob/0.78-stable/template/package.json) to your project.

Next, install the NPM packages by running:

* npm* Yarn

shell

```
npm install  

```

shell

```
yarn install  

```

Installation process has created a new `node_modules` folder. This folder stores all the JavaScript dependencies required to build your project.

Add `node_modules/` to your `.gitignore` file (here the [Community default one](https://github.com/react-native-community/template/blob/0.78-stable/template/_gitignore)).

### 3. Install Development tools[​](#3-install-development-tools "Direct link to 3. Install Development tools")

### Command Line Tools for Xcode[​](#command-line-tools-for-xcode "Direct link to Command Line Tools for Xcode")

Install the Command Line Tools. Choose **Settings... (or Preferences...)** in the Xcode menu. Go to the Locations panel and install the tools by selecting the most recent version in the Command Line Tools dropdown.

![Xcode Command Line Tools](/assets/images/GettingStartedXcodeCommandLineTools-7ddc121ba824227ca88a078b9ad9105e.png)

### CocoaPods[​](#cocoapods "Direct link to CocoaPods")

[CocoaPods](https://cocoapods.org) is a package management tool for iOS and macOS development. We use it to add the actual React Native framework code locally into your current project.

We recommend installing CocoaPods using [Homebrew](https://brew.sh/):

shell

```
brew install cocoapods  

```

4. Adding React Native to your app[​](#4-adding-react-native-to-your-app "Direct link to 4. Adding React Native to your app")
-----------------------------------------------------------------------------------------------------------------------------

### Configuring CocoaPods[​](#configuring-cocoapods "Direct link to Configuring CocoaPods")

To configure CocoaPods, we need two files:

* A **Gemfile** that defines which Ruby dependencies we need.
* A **Podfile** that defines how to properly install our dependencies.

For the **Gemfile**, go to the root directory of your project and run this command

sh

```
curl -O https://raw.githubusercontent.com/react-native-community/template/refs/heads/0.78-stable/template/Gemfile  

```

This will download the Gemfile from the template.

note

If you created your project with Xcode 16, you need to update the Gemfile as it follows:

diff

```
-gem 'cocoapods', '>= 1.13', '!= 1.15.0', '!= 1.15.1'  
+gem 'cocoapods', '1.16.2'  
gem 'activesupport', '>= 6.1.7.5', '!= 7.1.0'  
-gem 'xcodeproj', '< 1.26.0'  
+gem 'xcodeproj', '1.27.0'  

```

Xcode 16 generates a project in a slightly different ways from previous versions of Xcode, and you need the latest CocoaPods and Xcodeproj gems to make it work properly.

Similarly, for the **Podfile**, go to the `ios` folder of your project and run

sh

```
curl -O https://raw.githubusercontent.com/react-native-community/template/refs/heads/0.78-stable/template/ios/Podfile  

```

Please use the Community Template as a reference point for the [Gemfile](https://github.com/react-native-community/template/blob/0.78-stable/template/Gemfile) and for the [Podfile](https://github.com/react-native-community/template/blob/0.78-stable/template/ios/Podfile).

note

Remember to change [this line](https://github.com/react-native-community/template/blob/0.78-stable/template/ios/Podfile#L17).

Now, we need to run a couple of extra commands to install the Ruby gems and the Pods.
Navigate to the `ios` folder and run the following commands:

sh

```
bundle install  
bundle exec pod install  

```

The first command will install the Ruby dependencies and the second command will actually integrate the React Native code in your application so that your iOS files can import the React Native headers.

5. Writing the TypeScript Code[​](#5-writing-the-typescript-code "Direct link to 5. Writing the TypeScript Code")
-----------------------------------------------------------------------------------------------------------------

Now we will actually modify the native iOS application to integrate React Native.

The first bit of code we will write is the actual React Native code for the new screen that will be integrated into our application.

### Create a `index.js` file[​](#create-a-indexjs-file "Direct link to create-a-indexjs-file")

First, create an empty `index.js` file in the root of your React Native project.

`index.js` is the starting point for React Native applications, and it is always required. It can be a small file that `import`s other file that are part of your React Native component or application, or it can contain all the code that is needed for it.

Our `index.js` should look as follows (here the [Community template file as reference](https://github.com/react-native-community/template/blob/0.78-stable/template/index.js)):

js

```
import {AppRegistry} from 'react-native';  
import App from './App';  
  
AppRegistry.registerComponent('HelloWorld', () => App);  

```

### Create a `App.tsx` file[​](#create-a-apptsx-file "Direct link to create-a-apptsx-file")

Let's create an `App.tsx` file. This is a [TypeScript](https://www.typescriptlang.org/) file that can have [JSX](https://en.wikipedia.org/wiki/JSX_(JavaScript)) expressions. It contains the root React Native component that we will integrate into our iOS application ([link](https://github.com/react-native-community/template/blob/0.78-stable/template/App.tsx)):

tsx

```
import React from 'react';  
import {  
  SafeAreaView,  
  ScrollView,  
  StatusBar,  
  StyleSheet,  
  Text,  
  useColorScheme,  
  View,  
} from 'react-native';  
  
import {  
  Colors,  
  DebugInstructions,  
  Header,  
  ReloadInstructions,  
} from 'react-native/Libraries/NewAppScreen';  
  
function App(): React.JSX.Element {  
  const isDarkMode = useColorScheme() === 'dark';  
  
  const backgroundStyle = {  
    backgroundColor: isDarkMode ? Colors.darker : Colors.lighter,  
  };  
  
  return (  
    <SafeAreaView style={backgroundStyle}>  
      <StatusBar  
        barStyle={isDarkMode ? 'light-content' : 'dark-content'}  
        backgroundColor={backgroundStyle.backgroundColor}  
      />  
      <ScrollView  
        contentInsetAdjustmentBehavior="automatic"  
        style={backgroundStyle}>  
        <Header />  
        <View  
          style={{  
            backgroundColor: isDarkMode  
              ? Colors.black  
              : Colors.white,  
            padding: 24,  
          }}>  
          <Text style={styles.title}>Step One</Text>  
          <Text>  
            Edit <Text style={styles.bold}>App.tsx</Text> to  
            change this screen and see your edits.  
          </Text>  
          <Text style={styles.title}>See your changes</Text>  
          <ReloadInstructions />  
          <Text style={styles.title}>Debug</Text>  
          <DebugInstructions />  
        </View>  
      </ScrollView>  
    </SafeAreaView>  
  );  
}  
  
const styles = StyleSheet.create({  
  title: {  
    fontSize: 24,  
    fontWeight: '600',  
  },  
  bold: {  
    fontWeight: '700',  
  },  
});  
  
export default App;  

```

Here the [Community template file as reference](https://github.com/react-native-community/template/blob/0.78-stable/template/App.tsx)

5. Integrating with your iOS code[​](#5-integrating-with-your-ios-code "Direct link to 5. Integrating with your iOS code")
--------------------------------------------------------------------------------------------------------------------------

We now need to add some native code in order to start the React Native runtime and tell it to render our React components.

### Requirements[​](#requirements "Direct link to Requirements")

React Native intialization is now unbound to any specific part of an iOS app.

React Native can be initialized using a class called `RCTReactNativeFactory`, that takes care of handling the React Native lifecycle for you.

Once the class is initialized, you can either start a React Native view providing a `UIWindow` object, or you can ask for the factory to generate a `UIView` that you can load in any `UIViewController.`

In the following example, we will create a ViewController that can load a React Native view as it's `view`.

#### Create the ReactViewController[​](#create-the-reactviewcontroller "Direct link to Create the ReactViewController")

Create a new file from template (`⌘`+`N`) and choose the Cocoa Touch Class template.

Make sure to select `UIViewController` as the "Subclass of" field.

* ObjectiveC* Swift

Now open the `ReactViewController.m` file and apply the following changes

ReactViewController.m

```
#import "ReactViewController.h"  
+#import <React/RCTBundleURLProvider.h>  
+#import <RCTReactNativeFactory.h>  
+#import <RCTDefaultReactNativeFactoryDelegate.h>  
+#import <RCTAppDependencyProvider.h>  
  
  
@interface ReactViewController ()  
  
@end  
  
+@interface ReactNativeFactoryDelegate: RCTDefaultReactNativeFactoryDelegate  
+@end  
  
-@implementation ReactViewController  
+@implementation ReactViewController {  
+  RCTReactNativeFactory *_factory;  
+  id<RCTReactNativeFactoryDelegate> _factoryDelegate;  
+}  
  
 - (void)viewDidLoad {  
     [super viewDidLoad];  
     // Do any additional setup after loading the view.  
+    _factoryDelegate = [ReactNativeFactoryDelegate new];  
+    _factoryDelegate.dependencyProvider = [RCTAppDependencyProvider new];  
+    _factory = [[RCTReactNativeFactory alloc] initWithDelegate:_factoryDelegate];  
+    self.view = [_factory.rootViewFactory viewWithModuleName:@"HelloWorld"];  
 }  
  
@end  
  
+@implementation ReactNativeFactoryDelegate  
+  
+- (NSURL *)sourceURLForBridge:(RCTBridge *)bridge  
+{  
+  return [self bundleURL];  
+}  
+  
+- (NSURL *)bundleURL  
+{  
+#if DEBUG  
+  return [RCTBundleURLProvider.sharedSettings jsBundleURLForBundleRoot:@"index"];  
+#else  
+  return [NSBundle.mainBundle URLForResource:@"main" withExtension:@"jsbundle"];  
+#endif  
+}  
  
@end  
  

```

Now open the `ReactViewController.swift` file and apply the following changes

ReactViewController.swift

```
import UIKit  
+import React  
+import React_RCTAppDelegate  
+import ReactAppDependencyProvider  
  
class ReactViewController: UIViewController {  
+  var reactNativeFactory: RCTReactNativeFactory?  
+  var reactNativeFactoryDelegate: RCTReactNativeFactoryDelegate?  
  
  override func viewDidLoad() {  
    super.viewDidLoad()  
+    reactNativeFactoryDelegate = ReactNativeDelegate()  
+    reactNativeFactoryDelegate!.dependencyProvider = RCTAppDependencyProvider()  
+    reactNativeFactory = RCTReactNativeFactory(delegate: reactNativeFactoryDelegate!)  
+    view = reactNativeFactory!.rootViewFactory.view(withModuleName: "HelloWorld")  
  
  }  
}  
  
+class ReactNativeDelegate: RCTDefaultReactNativeFactoryDelegate {  
+    override func sourceURL(for bridge: RCTBridge) -> URL? {  
+      self.bundleURL()  
+    }  
+  
+    override func bundleURL() -> URL? {  
+      #if DEBUG  
+      RCTBundleURLProvider.sharedSettings().jsBundleURL(forBundleRoot: "index")  
+      #else  
+      Bundle.main.url(forResource: "main", withExtension: "jsbundle")  
+      #endif  
+    }  
+  
+}  

```

#### Presenting a React Native view in a rootViewController[​](#presenting-a-react-native-view-in-a-rootviewcontroller "Direct link to Presenting a React Native view in a rootViewController")

Finally, we can present our React Native view. To do so, we need a new View Controller that can host a view in which we can load the JS content.
We already have the initial `ViewController`, and we can make it present the `ReactViewController`. There are several ways to do so, depending on your app. For this example, we assume that you have a button that presents React Native modally.

* ObjectiveC* Swift

ViewController.m

```
#import "ViewController.h"  
+#import "ReactViewController.h"  
  
@interface ViewController ()  
  
@end  
  
- @implementation ViewController  
+@implementation ViewController {  
+  ReactViewController *reactViewController;  
+}  
  
 - (void)viewDidLoad {  
   [super viewDidLoad];  
   // Do any additional setup after loading the view.  
   self.view.backgroundColor = UIColor.systemBackgroundColor;  
+  UIButton *button = [UIButton new];  
+  [button setTitle:@"Open React Native" forState:UIControlStateNormal];  
+  [button setTitleColor:UIColor.systemBlueColor forState:UIControlStateNormal];  
+  [button setTitleColor:UIColor.blueColor forState:UIControlStateHighlighted];  
+  [button addTarget:self action:@selector(presentReactNative) forControlEvents:UIControlEventTouchUpInside];  
+  [self.view addSubview:button];  
  
+  button.translatesAutoresizingMaskIntoConstraints = NO;  
+  [NSLayoutConstraint activateConstraints:@[  
+    [button.leadingAnchor constraintEqualToAnchor:self.view.leadingAnchor],  
+    [button.trailingAnchor constraintEqualToAnchor:self.view.trailingAnchor],  
+    [button.centerYAnchor constraintEqualToAnchor:self.view.centerYAnchor],  
+    [button.centerXAnchor constraintEqualToAnchor:self.view.centerXAnchor],  
+  ]];  
 }  
  
+- (void)presentReactNative  
+{  
+  if (reactViewController == NULL) {  
+    reactViewController = [ReactViewController new];  
+  }  
+  [self presentViewController:reactViewController animated:YES];  
+}  
  
@end  

```

ViewController.swift

```
import UIKit  
  
class ViewController: UIViewController {  
  
+  var reactViewController: ReactViewController?  
  
  override func viewDidLoad() {  
    super.viewDidLoad()  
    // Do any additional setup after loading the view.  
    self.view.backgroundColor = .systemBackground  
  
+    let button = UIButton()  
+    button.setTitle("Open React Native", for: .normal)  
+    button.setTitleColor(.systemBlue, for: .normal)  
+    button.setTitleColor(.blue, for: .highlighted)  
+    button.addAction(UIAction { [weak self] _ in  
+      guard let self else { return }  
+      if reactViewController == nil {  
+       reactViewController = ReactViewController()  
+      }  
+      present(reactViewController!, animated: true)  
+    }, for: .touchUpInside)  
+    self.view.addSubview(button)  
+  
+    button.translatesAutoresizingMaskIntoConstraints = false  
+    NSLayoutConstraint.activate([  
+      button.leadingAnchor.constraint(equalTo: self.view.leadingAnchor),  
+      button.trailingAnchor.constraint(equalTo: self.view.trailingAnchor),  
+      button.centerXAnchor.constraint(equalTo: self.view.centerXAnchor),  
+      button.centerYAnchor.constraint(equalTo: self.view.centerYAnchor),  
+    ])  
  }  
}  

```

Make sure to disable the Sandbox scripting. To achieve this, in Xcode, click on your app, then on build settings. Filter for script and set the `User Script Sandboxing` to `NO`. This step is needed to properly switch between the Debug and Release version of the [Hermes engine](https://github.com/facebook/hermes/blob/main/README.md) that we ship with React Native.

![Disable Sandboxing](/assets/images/disable-sandboxing-837fd639c3510f4bf9b0ea67e3bbe142.png)

Finally, make sure to add the `UIViewControllerBasedStatusBarAppearance` key into your `Info.plist` file, with value of `NO`.

![Disable UIViewControllerBasedStatusBarAppearance](/assets/images/disable-UIViewControllerBasedStatusBarAppearance-54a3f3ba9efde1694f7d7bfbfa0adbe1.png)

6. Test your integration[​](#6-test-your-integration "Direct link to 6. Test your integration")
-----------------------------------------------------------------------------------------------

You have completed all the basic steps to integrate React Native with your application. Now we will start the [Metro bundler](https://metrobundler.dev/) to build your TypeScript application code into a bundle. Metro's HTTP server shares the bundle from `localhost` on your developer environment to a simulator or device. This allows for [hot reloading](https://reactnative.dev/blog/2016/03/24/introducing-hot-reloading).

First, you need to create a `metro.config.js` file in the root of your project as follows:

js

```
const {getDefaultConfig} = require('@react-native/metro-config');  
module.exports = getDefaultConfig(__dirname);  

```

You can checkout the [metro.config.js file](https://github.com/react-native-community/template/blob/0.78-stable/template/metro.config.js) from the Community template file as reference.

Then, you need to create a `.watchmanconfig` file in the root of your project. The file must contain an empty json object:

sh

```
echo {} > .watchmanconfig  

```

Once you have the configurations file in place, you can run the bundler. Run the following command in the root directory of your project:

* npm* Yarn

shell

```
npm start  

```

shell

```
yarn start  

```

Now build and run your iOS app as normal.

Once you reach your React-powered Activity inside the app, it should load the JavaScript code from the development server and display:

![](/docs/assets/EmbeddedAppIOS078.gif)

### Creating a release build in Xcode[​](#creating-a-release-build-in-xcode "Direct link to Creating a release build in Xcode")

You can use Xcode to create your release builds too! The only additional step is to add a script that is executed when the app is built to package your JS and images into the iOS application.

1. In Xcode, select your application
2. Click on `Build Phases`
3. Click on the `+` in the top left corner and select `New Run Script Phase`
4. Click on the `Run Script` line and rename the Script to `Bundle React Native code and images`
5. Paste in the text box the following script

Build React Native code and image

```
set -e  
  
WITH_ENVIRONMENT="$REACT_NATIVE_PATH/scripts/xcode/with-environment.sh"  
REACT_NATIVE_XCODE="$REACT_NATIVE_PATH/scripts/react-native-xcode.sh"  
  
/bin/sh -c "$WITH_ENVIRONMENT $REACT_NATIVE_XCODE"  

```

6. Drag and drop the script before the one called `[CP] Embed Pods Frameworks`.

Now, if you build your app for Release, it will work as expected.

7. Passing initial props to the React Native view[​](#7-passing-initial-props-to-the-react-native-view "Direct link to 7. Passing initial props to the React Native view")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In some case, you'd like to pass some information from the Native app to JavaScript. For example, you might want to pass the user id of the currently logged user to React Native, together with a token that can be used to retrieve information from a database.

This is possible by using the `initialProperties` parameter of the `view(withModuleName:initialProperty)` overload of the `RCTReactNativeFactory` class. The following steps shows you how to do it.

### Update the App.tsx file to read the initial properties.[​](#update-the-apptsx-file-to-read-the-initial-properties "Direct link to Update the App.tsx file to read the initial properties.")

Open the `App.tsx` file and add the following code:

App.tsx

```
import {  
  Colors,  
  DebugInstructions,  
  Header,  
  ReloadInstructions,  
} from 'react-native/Libraries/NewAppScreen';  
  
-function App(): React.JSX.Element {  
+function App(props): React.JSX.Element {  
  const isDarkMode = useColorScheme() === 'dark';  
  
  const backgroundStyle = {  
    backgroundColor: isDarkMode ? Colors.darker : Colors.lighter,  
  };  
  
  return (  
    <SafeAreaView style={backgroundStyle}>  
      <StatusBar  
        barStyle={isDarkMode ? 'light-content' : 'dark-content'}  
        backgroundColor={backgroundStyle.backgroundColor}  
      />  
      <ScrollView  
        contentInsetAdjustmentBehavior="automatic"  
        style={backgroundStyle}>  
        <Header />  
-       <View  
-         style={{  
-           backgroundColor: isDarkMode  
-             ? Colors.black  
-             : Colors.white,  
-           padding: 24,  
-         }}>  
-         <Text style={styles.title}>Step One</Text>  
-         <Text>  
-           Edit <Text style={styles.bold}>App.tsx</Text> to  
-           change this screen and see your edits.  
-         </Text>  
-         <Text style={styles.title}>See your changes</Text>  
-         <ReloadInstructions />  
-         <Text style={styles.title}>Debug</Text>  
-         <DebugInstructions />  
+         <Text style={styles.title}>UserID: {props.userID}</Text>  
+         <Text style={styles.title}>Token: {props.token}</Text>  
        </View>  
      </ScrollView>  
    </SafeAreaView>  
  );  
}  
  
const styles = StyleSheet.create({  
  title: {  
    fontSize: 24,  
    fontWeight: '600',  
+   marginLeft: 20,  
  },  
  bold: {  
    fontWeight: '700',  
  },  
});  
  
export default App;  

```

These changes will tell React Native that your App component is now accepting some properties. The `RCTreactNativeFactory` will take care of passing them to the component when it's rendered.

### Update the Native code to pass the initial properties to JavaScript.[​](#update-the-native-code-to-pass-the-initial-properties-to-javascript "Direct link to Update the Native code to pass the initial properties to JavaScript.")

* ObjectiveC* Swift

Modify the `ReactViewController.mm` to pass the initial properties to JavaScript.

ReactViewController.mm

```
 - (void)viewDidLoad {  
   [super viewDidLoad];  
   // Do any additional setup after loading the view.  
  
   _factoryDelegate = [ReactNativeFactoryDelegate new];  
   _factoryDelegate.dependencyProvider = [RCTAppDependencyProvider new];  
   _factory = [[RCTReactNativeFactory alloc] initWithDelegate:_factoryDelegate];  
-  self.view = [_factory.rootViewFactory viewWithModuleName:@"HelloWorld"];  
+  self.view = [_factory.rootViewFactory viewWithModuleName:@"HelloWorld" initialProperties:@{  
+    @"userID": @"12345678",  
+    @"token": @"secretToken"  
+  }];  
}  

```

Modify the `ReactViewController.swift` to pass the initial properties to the React Native view.

ReactViewController.swift

```
  override func viewDidLoad() {  
    super.viewDidLoad()  
    reactNativeFactoryDelegate = ReactNativeDelegate()  
    reactNativeFactoryDelegate!.dependencyProvider = RCTAppDependencyProvider()  
    reactNativeFactory = RCTReactNativeFactory(delegate: reactNativeFactoryDelegate!)  
-   view = reactNativeFactory!.rootViewFactory.view(withModuleName: "HelloWorld")  
+   view = reactNativeFactory!.rootViewFactory.view(withModuleName: "HelloWorld" initialProperties: [  
+     "userID": "12345678",  
+     "token": "secretToken"  
+])  
  
  }  
}  

```

3. Run your app once again. You should see the following screen after you present the `ReactViewController`:

![](/docs/assets/brownfield-with-initial-props.png)

Now what?[​](#now-what "Direct link to Now what?")
--------------------------------------------------

At this point you can continue developing your app as usual. Refer to our [debugging](/docs/debugging) and [deployment](/docs/running-on-device) docs to learn more about working with React Native.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/integration-with-existing-apps.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/integration-with-existing-apps.md)

Last updated on **Apr 14, 2025**

[Previous

Set Up Your Environment](/docs/set-up-your-environment)[Next

Integration with an Android Fragment](/docs/integration-with-android-fragment)

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