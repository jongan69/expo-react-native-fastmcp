Publishing to Google Play Store · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/signed-apk-android)

* [Next](/docs/next/signed-apk-android)* [0.79](/docs/signed-apk-android)* [0.78](/docs/0.78/signed-apk-android)* [0.77](/docs/0.77/signed-apk-android)* [0.76](/docs/0.76/signed-apk-android)* [0.75](/docs/0.75/signed-apk-android)* [0.74](/docs/0.74/signed-apk-android)* [0.73](/docs/0.73/signed-apk-android)* [0.72](/docs/0.72/signed-apk-android)* [0.71](/docs/0.71/signed-apk-android)* [0.70](/docs/0.70/signed-apk-android)* [All versions](/versions)

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

                    * [Android and iOS guides](/docs/headless-js-android)

                      + Android

                        - [Headless JS](/docs/headless-js-android)- [Publishing to Google Play Store](/docs/signed-apk-android)- [Communication between native and React Native](/docs/communication-android)- [React Native Gradle Plugin](/docs/react-native-gradle-plugin)+ iOS

                          - [Linking Libraries](/docs/linking-libraries-ios)- [Running On Simulator](/docs/running-on-simulator-ios)- [Communication between native and React Native](/docs/communication-ios)- [App Extensions](/docs/app-extensions)- [Publishing to Apple App Store](/docs/publishing-to-app-store)* [Legacy Architecture](/docs/legacy/native-modules-intro)

On this page

Publishing to Google Play Store
===============================

Android requires that all apps be digitally signed with a certificate before they can be installed. In order to distribute your Android application via [Google Play store](https://play.google.com/store) it needs to be signed with a release key that then needs to be used for all future updates. Since 2017 it is possible for Google Play to manage signing releases automatically thanks to [App Signing by Google Play](https://developer.android.com/studio/publish/app-signing#app-signing-google-play) functionality. However, before your application binary is uploaded to Google Play it needs to be signed with an upload key. The [Signing Your Applications](https://developer.android.com/tools/publishing/app-signing.html) page on Android Developers documentation describes the topic in detail. This guide covers the process in brief, as well as lists the steps required to package the JavaScript bundle.

info

If you are using Expo, read the Expo guide for [Deploying to App Stores](https://docs.expo.dev/distribution/app-stores/) to build and submit your app for the Google Play Store. This guide works with any React Native app to automate the deployment process.

Generating an upload key[​](#generating-an-upload-key "Direct link to Generating an upload key")
------------------------------------------------------------------------------------------------

You can generate a private signing key using `keytool`.

### Windows[​](#windows "Direct link to Windows")

On Windows `keytool` must be run from `C:\Program Files\Java\jdkx.x.x_x\bin`, as administrator.

shell

```
keytool -genkeypair -v -storetype PKCS12 -keystore my-upload-key.keystore -alias my-key-alias -keyalg RSA -keysize 2048 -validity 10000  

```

This command prompts you for passwords for the keystore and key and for the Distinguished Name fields for your key. It then generates the keystore as a file called `my-upload-key.keystore`.

The keystore contains a single key, valid for 10000 days. The alias is a name that you will use later when signing your app, so remember to take note of the alias.

### macOS[​](#macos "Direct link to macOS")

On macOS, if you're not sure where your JDK bin folder is, then perform the following command to find it:

shell

```
/usr/libexec/java_home  

```

It will output the directory of the JDK, which will look something like this:

shell

```
/Library/Java/JavaVirtualMachines/jdkX.X.X_XXX.jdk/Contents/Home  

```

Navigate to that directory by using the command `cd /your/jdk/path` and use the keytool command with sudo permission as shown below.

shell

```
sudo keytool -genkey -v -keystore my-upload-key.keystore -alias my-key-alias -keyalg RSA -keysize 2048 -validity 10000  

```

caution

Remember to keep the keystore file private. In case you've lost upload key or it's been compromised you should [follow these instructions](https://support.google.com/googleplay/android-developer/answer/7384423#reset).

Setting up Gradle variables[​](#setting-up-gradle-variables "Direct link to Setting up Gradle variables")
---------------------------------------------------------------------------------------------------------

1. Place the `my-upload-key.keystore` file under the `android/app` directory in your project folder.
2. Edit the file `~/.gradle/gradle.properties` or `android/gradle.properties`, and add the following (replace `*****` with the correct keystore password, alias and key password),

```
MYAPP_UPLOAD_STORE_FILE=my-upload-key.keystore  
MYAPP_UPLOAD_KEY_ALIAS=my-key-alias  
MYAPP_UPLOAD_STORE_PASSWORD=*****  
MYAPP_UPLOAD_KEY_PASSWORD=*****  

```

These are going to be global Gradle variables, which we can later use in our Gradle config to sign our app.

Note about using git

Saving the above Gradle variables in `~/.gradle/gradle.properties` instead of `android/gradle.properties` prevents them from being checked in to git. You may have to create the `~/.gradle/gradle.properties` file in your user's home directory before you can add the variables.

Note about security

If you are not keen on storing your passwords in plaintext, and you are running macOS, you can also [store your credentials in the Keychain Access app](https://pilloxa.gitlab.io/posts/safer-passwords-in-gradle/). Then you can skip the two last rows in `~/.gradle/gradle.properties`.

Adding signing config to your app's Gradle config[​](#adding-signing-config-to-your-apps-gradle-config "Direct link to Adding signing config to your app's Gradle config")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The last configuration step that needs to be done is to setup release builds to be signed using upload key. Edit the file `android/app/build.gradle` in your project folder, and add the signing config,

groovy

```
...  
android {  
    ...  
    defaultConfig { ... }  
    signingConfigs {  
        release {  
            if (project.hasProperty('MYAPP_UPLOAD_STORE_FILE')) {  
                storeFile file(MYAPP_UPLOAD_STORE_FILE)  
                storePassword MYAPP_UPLOAD_STORE_PASSWORD  
                keyAlias MYAPP_UPLOAD_KEY_ALIAS  
                keyPassword MYAPP_UPLOAD_KEY_PASSWORD  
            }  
        }  
    }  
    buildTypes {  
        release {  
            ...  
            signingConfig signingConfigs.release  
        }  
    }  
}  
...  

```

Generating the release AAB[​](#generating-the-release-aab "Direct link to Generating the release AAB")
------------------------------------------------------------------------------------------------------

Run the following command in a terminal:

shell

```
npx react-native build-android --mode=release  

```

This command uses Gradle's `bundleRelease` under the hood that bundles all the JavaScript needed to run your app into the AAB ([Android App Bundle](https://developer.android.com/guide/app-bundle)). If you need to change the way the JavaScript bundle and/or drawable resources are bundled (e.g. if you changed the default file/folder names or the general structure of the project), have a look at `android/app/build.gradle` to see how you can update it to reflect these changes.

note

Make sure `gradle.properties` does not include `org.gradle.configureondemand=true` as that will make the release build skip bundling JS and assets into the app binary.

The generated AAB can be found under `android/app/build/outputs/bundle/release/app-release.aab`, and is ready to be uploaded to Google Play.

In order for Google Play to accept AAB format the App Signing by Google Play needs to be configured for your application on the Google Play Console. If you are updating an existing app that doesn't use App Signing by Google Play, please check our [migration section](#migrating-old-android-react-native-apps-to-use-app-signing-by-google-play) to learn how to perform that configuration change.

Testing the release build of your app[​](#testing-the-release-build-of-your-app "Direct link to Testing the release build of your app")
---------------------------------------------------------------------------------------------------------------------------------------

Before uploading the release build to the Play Store, make sure you test it thoroughly. First uninstall any previous version of the app you already have installed. Install it on the device using the following command in the project root:

* npm* Yarn

shell

```
npm run android -- --mode="release"  

```

shell

```
yarn android --mode release  

```

Note that `--mode release` is only available if you've set up signing as described above.

You can terminate any running bundler instances, since all your framework and JavaScript code is bundled in the APK's assets.

Publishing to other stores[​](#publishing-to-other-stores "Direct link to Publishing to other stores")
------------------------------------------------------------------------------------------------------

By default, the generated APK has the native code for both `x86`, `x86_64`, `ARMv7a` and `ARM64-v8a` CPU architectures. This makes it easier to share APKs that run on almost all Android devices. However, this has the downside that there will be some unused native code on any device, leading to unnecessarily bigger APKs.

You can create an APK for each CPU by adding the following line in your `android/app/build.gradle` file:

diff

```
android {  
  
    splits {  
        abi {  
            reset()  
            enable true  
            universalApk false  
            include "armeabi-v7a", "arm64-v8a", "x86", "x86_64"  
        }  
    }  
  
}  

```

Upload these files to markets which support device targeting, such as [Amazon AppStore](https://developer.amazon.com/docs/app-submission/device-filtering-and-compatibility.html) or [F-Droid](https://f-droid.org/en/), and the users will automatically get the appropriate APK. If you want to upload to other markets, such as [APKFiles](https://www.apkfiles.com/), which do not support multiple APKs for a single app, change the `universalApk false` line to `true` to create the default universal APK with binaries for both CPUs.

Please note that you will also have to configure distinct version codes, as [suggested in this page](https://developer.android.com/studio/build/configure-apk-splits#configure-APK-versions) from the official Android documentation.

Enabling Proguard to reduce the size of the APK (optional)[​](#enabling-proguard-to-reduce-the-size-of-the-apk-optional "Direct link to Enabling Proguard to reduce the size of the APK (optional)")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Proguard is a tool that can slightly reduce the size of the APK. It does this by stripping parts of the React Native Java bytecode (and its dependencies) that your app is not using.

Important

Make sure to thoroughly test your app if you've enabled Proguard. Proguard often requires configuration specific to each native library you're using. See `app/proguard-rules.pro`.

To enable Proguard, edit `android/app/build.gradle`:

groovy

```
/**  
 * Run Proguard to shrink the Java bytecode in release builds.  
 */  
def enableProguardInReleaseBuilds = true  

```

Migrating old Android React Native apps to use App Signing by Google Play[​](#migrating-old-android-react-native-apps-to-use-app-signing-by-google-play "Direct link to Migrating old Android React Native apps to use App Signing by Google Play")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you are migrating from previous version of React Native chances are your app does not use App Signing by Google Play feature. We recommend you enable that in order to take advantage from things like automatic app splitting. In order to migrate from the old way of signing you need to start by [generating new upload key](#generating-an-upload-key) and then replacing release signing config in `android/app/build.gradle` to use the upload key instead of the release one (see section about [adding signing config to gradle](#adding-signing-config-to-your-apps-gradle-config)). Once that's done you should follow the [instructions from Google Play Help website](https://support.google.com/googleplay/android-developer/answer/7384423) in order to send your original release key to Google Play.

Default Permissions[​](#default-permissions "Direct link to Default Permissions")
---------------------------------------------------------------------------------

By default, `INTERNET` permission is added to your Android app as pretty much all apps use it. `SYSTEM_ALERT_WINDOW` permission is added to your Android APK in debug mode but it will be removed in production.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/signed-apk-android.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/signed-apk-android.md)

Last updated on **Apr 14, 2025**

[Previous

Headless JS](/docs/headless-js-android)[Next

Communication between native and React Native](/docs/communication-android)

* [Generating an upload key](#generating-an-upload-key)
  + [Windows](#windows)+ [macOS](#macos)* [Setting up Gradle variables](#setting-up-gradle-variables)* [Adding signing config to your app's Gradle config](#adding-signing-config-to-your-apps-gradle-config)* [Generating the release AAB](#generating-the-release-aab)* [Testing the release build of your app](#testing-the-release-build-of-your-app)* [Publishing to other stores](#publishing-to-other-stores)* [Enabling Proguard to reduce the size of the APK (optional)](#enabling-proguard-to-reduce-the-size-of-the-apk-optional)* [Migrating old Android React Native apps to use App Signing by Google Play](#migrating-old-android-react-native-apps-to-use-app-signing-by-google-play)* [Default Permissions](#default-permissions)

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