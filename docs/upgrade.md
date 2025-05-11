Native project upgrade helper - Expo Documentation

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

[Overview](/bare/overview)[Install Expo modules](/bare/installing-expo-modules)[Migrate to Expo CLI](/bare/using-expo-cli)[Install expo-updates](/bare/installing-updates)[Install expo-dev-client](/bare/install-dev-builds-in-bare)[Native project upgrade helper](/bare/upgrade)

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

Native project upgrade helper
=============================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/bare/upgrade.mdx)

View file-by-file diffs of all the changes you need to make to your native projects to upgrade them to the next Expo SDK version.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/bare/upgrade.mdx)

---

If you manage your native projects (previously known as bare workflow), to [upgrade to the latest Expo SDK](/workflow/upgrading-expo-sdk-walkthrough), you have to make changes to your native projects. It can be a complex process to find which native file changes and what to update in which file.

The following guide provides diffs to compare native project files between your project's current SDK version and the target SDK version you want to upgrade. You can use them to make changes to your project depending on the `expo` package version your project uses. The tools on this page are similar to [React Native Upgrade Helper](https://react-native-community.github.io/upgrade-helper/). However, they are oriented around projects that use Expo modules and related tooling.

> Interested in avoiding upgrading native code altogether? See [Continuous Native Generation (CNG)](/workflow/continuous-native-generation) to learn how Expo Prebuild can generate your native projects before a build.

Upgrade native project files
----------------------------

Once you have [upgraded your Expo SDK version and related dependencies](/workflow/upgrading-expo-sdk-walkthrough#how-to-upgrade-to-the-latest-sdk-version), use the diff tool below to learn about changes you need to make to your native project and bring them up to date with the current Expo SDK version.

Choose your from SDK version and to SDK version to see the generated diff. Then, apply those changes to your native projects by copying and pasting or manually making changes to the project files.

#### From SDK version:

#### To SDK version:

### Native code changes from SDK 52 to 53

[android/app/build.gradle

MODIFIED

Raw](#androidappbuildgradle)

|  |  |  |
| --- | --- | --- |
| 14 | 14 | hermesCommand = new File(["node", "--print", "require.resolve('react-native/package.json')"].execute(null, rootDir).text.trim()).getParentFile().getAbsolutePath() + "/sdks/hermesc/%OS-BIN%/hermesc" |
| 15 | 15 | codegenDir = new File(["node", "--print", "require.resolve('@react-native/codegen/package.json', { paths: [require.resolve('react-native/package.json')] })"].execute(null, rootDir).text.trim()).getParentFile().getAbsoluteFile() |
| 16 | 16 |  |
|  | 17 | enableBundleCompression = (findProperty('android.enableBundleCompression') ?: false).toBoolean() |
| 17 | 18 | // Use Expo CLI to bundle the app, this ensures the Metro config |
| 18 | 19 | // works correctly with Expo projects. |
| 19 | 20 | cliFile = new File(["node", "--print", "require.resolve('@expo/cli', { paths: [require.resolve('expo/package.json')] })"].execute(null, rootDir).text.trim()) |
|  |  |  |
| --- | --- | --- |
| 78 | 79 | \* give correct results when using with locales other than en-US. Note that |
| 79 | 80 | \* this variant is about 6MiB larger per architecture than default. |
| 80 | 81 | \*/ |
| 81 |  | def jscFlavor = 'org.webkit:android-jsc:+' |
|  | 82 | def jscFlavor = 'io.github.react-native-community:jsc-android:2026004.+' |
| 82 | 83 |  |
| 83 | 84 | android { |
| 84 | 85 | ndkVersion rootProject.ext.ndkVersion |
|  |  |  |
| --- | --- | --- |
| 156 | 157 |  |
| 157 | 158 | if (isGifEnabled) { |
| 158 | 159 | // For animated gif support |
| 159 |  | implementation("com.facebook.fresco:animated-gif:${reactAndroidLibs.versions.fresco.get()}") |
|  | 160 | implementation("com.facebook.fresco:animated-gif:${expoLibs.versions.fresco.get()}") |
| 160 | 161 | } |
| 161 | 162 |  |
| 162 | 163 | if (isWebpEnabled) { |
| 163 | 164 | // For webp support |
| 164 |  | implementation("com.facebook.fresco:webpsupport:${reactAndroidLibs.versions.fresco.get()}") |
|  | 165 | implementation("com.facebook.fresco:webpsupport:${expoLibs.versions.fresco.get()}") |
| 165 | 166 | if (isWebpAnimatedEnabled) { |
| 166 | 167 | // Animated webp support |
| 167 |  | implementation("com.facebook.fresco:animated-webp:${reactAndroidLibs.versions.fresco.get()}") |
|  | 168 | implementation("com.facebook.fresco:animated-webp:${expoLibs.versions.fresco.get()}") |
| 168 | 169 | } |
| 169 | 170 | } |
| 170 | 171 |  |

[android/app/src/main/res/values/styles.xml

MODIFIED

Raw](#androidappsrcmainresvaluesstylesxml)

|  |  |  |
| --- | --- | --- |
| 1 | 1 | <resources> |
| 2 |  | <style name="AppTheme" parent="Theme.AppCompat.Light.NoActionBar"> |
| 3 |  | <item name="android:textColor">@android:color/black</item> |
| 4 |  | <item name="android:editTextStyle">@style/ResetEditText</item> |
|  | 2 | <style name="AppTheme" parent="Theme.AppCompat.DayNight.NoActionBar"> |
| 5 | 3 | <item name="android:editTextBackground">@drawable/rn\_edit\_text\_material</item> |
| 6 | 4 | </style> |
| 7 |  | <style name="ResetEditText" parent="@android:style/Widget.EditText"> |
| 8 |  | <item name="android:padding">0dp</item> |
| 9 |  | <item name="android:textColorHint">#c8c8c8</item> |
| 10 |  | <item name="android:textColor">@android:color/black</item> |
| 11 |  | </style> |
| 12 | 5 | <style name="Theme.App.SplashScreen" parent="AppTheme"> |
| 13 | 6 | <item name="android:windowBackground">@drawable/splashscreen\_logo</item> |
| 14 | 7 | </style> |

[android/build.gradle

MODIFIED

Raw](#androidbuildgradle)

|  |  |  |
| --- | --- | --- |
| 1 | 1 | // Top-level build file where you can add configuration options common to all sub-projects/modules. |
| 2 | 2 |  |
| 3 | 3 | buildscript { |
| 4 |  | ext { |
| 5 |  | buildToolsVersion = findProperty('android.buildToolsVersion') ?: '35.0.0' |
| 6 |  | minSdkVersion = Integer.parseInt(findProperty('android.minSdkVersion') ?: '24') |
| 7 |  | compileSdkVersion = Integer.parseInt(findProperty('android.compileSdkVersion') ?: '35') |
| 8 |  | targetSdkVersion = Integer.parseInt(findProperty('android.targetSdkVersion') ?: '34') |
| 9 |  | kotlinVersion = findProperty('android.kotlinVersion') ?: '1.9.25' |
| 10 |  |  |
| 11 |  | ndkVersion = "26.1.10909125" |
| 12 |  | } |
| 13 |  | repositories { |
| 14 |  | google() |
| 15 |  | mavenCentral() |
| 16 |  | } |
| 17 |  | dependencies { |
| 18 |  | classpath('com.android.tools.build:gradle') |
| 19 |  | classpath('com.facebook.react:react-native-gradle-plugin') |
| 20 |  | classpath('org.jetbrains.kotlin:kotlin-gradle-plugin') |
| 21 |  | } |
|  | 4 | repositories { |
|  | 5 | google() |
|  | 6 | mavenCentral() |
|  | 7 | } |
|  | 8 | dependencies { |
|  | 9 | classpath('com.android.tools.build:gradle') |
|  | 10 | classpath('com.facebook.react:react-native-gradle-plugin') |
|  | 11 | classpath('org.jetbrains.kotlin:kotlin-gradle-plugin') |
|  | 12 | } |
| 22 | 13 | } |
| 23 | 14 |  |
| 24 |  | apply plugin: "com.facebook.react.rootproject" |
|  | 15 | def reactNativeAndroidDir = new File( |
|  | 16 | providers.exec { |
|  | 17 | workingDir(rootDir) |
|  | 18 | commandLine("node", "--print", "require.resolve('react-native/package.json')") |
|  | 19 | }.standardOutput.asText.get().trim(), |
|  | 20 | "../android" |
|  | 21 | ) |
| 25 | 22 |  |
| 26 | 23 | allprojects { |
| 27 |  | repositories { |
| 28 |  | maven { |
| 29 |  | // All of React Native (JS, Obj-C sources, Android binaries) is installed from npm |
| 30 |  | url(new File(['node', '--print', "require.resolve('react-native/package.json')"].execute(null, rootDir).text.trim(), '../android')) |
| 31 |  | } |
| 32 |  | maven { |
| 33 |  | // Android JSC is installed from npm |
| 34 |  | url(new File(['node', '--print', "require.resolve('jsc-android/package.json', { paths: [require.resolve('react-native/package.json')] })"].execute(null, rootDir).text.trim(), '../dist')) |
| 35 |  | } |
| 36 |  |  |
| 37 |  | google() |
| 38 |  | mavenCentral() |
| 39 |  | maven { url 'https://www.jitpack.io' } |
|  | 24 | repositories { |
|  | 25 | maven { |
|  | 26 | // All of React Native (JS, Obj-C sources, Android binaries) is installed from npm |
|  | 27 | url(reactNativeAndroidDir) |
| 40 | 28 | } |
|  | 29 |  |
|  | 30 | google() |
|  | 31 | mavenCentral() |
|  | 32 | maven { url 'https://www.jitpack.io' } |
|  | 33 | } |
| 41 | 34 | } |
|  | 35 |  |
|  | 36 | apply plugin: "expo-root-project" |
|  | 37 | apply plugin: "com.facebook.react.rootproject" |

[android/gradle.properties

MODIFIED

Raw](#androidgradleproperties)

|  |  |  |
| --- | --- | --- |
| 35 | 35 | # your application. You should enable this flag either if you want |
| 36 | 36 | # to write custom TurboModules/Fabric components OR use libraries that |
| 37 | 37 | # are providing them. |
| 38 |  | newArchEnabled=false |
|  | 38 | newArchEnabled=true |
| 39 | 39 |  |
| 40 | 40 | # Use this property to enable or disable the Hermes JS engine. |
| 41 | 41 | # If set to false, you will be using JSC instead. |

[android/gradle/wrapper/gradle-wrapper.properties

MODIFIED

Raw](#androidgradlewrappergradle-wrapperproperties)

|  |  |  |
| --- | --- | --- |
| 1 | 1 | distributionBase=GRADLE\_USER\_HOME |
| 2 | 2 | distributionPath=wrapper/dists |
| 3 |  | distributionUrl=https\://services.gradle.org/distributions/gradle-8.10.2-all.zip |
|  | 3 | distributionUrl=https\://services.gradle.org/distributions/gradle-8.13-bin.zip |
| 4 | 4 | networkTimeout=10000 |
| 5 | 5 | validateDistributionUrl=true |
| 6 | 6 | zipStoreBase=GRADLE\_USER\_HOME |

[android/gradlew

MODIFIED

Raw](#androidgradlew)

|  |  |  |
| --- | --- | --- |
| 86 | 86 | # shellcheck disable=SC2034 |
| 87 | 87 | APP\_BASE\_NAME=${0##\*/} |
| 88 | 88 | # Discard cd standard output in case $CDPATH is set (https://github.com/gradle/gradle/issues/25036) |
| 89 |  | APP\_HOME=$( cd -P "${APP\_HOME:-./}" > /dev/null && printf '%s |
| 90 |  | ' "$PWD" ) || exit |
|  | 89 | APP\_HOME=$( cd -P "${APP\_HOME:-./}" > /dev/null && printf '%s\n' "$PWD" ) || exit |
| 91 | 90 |  |
| 92 | 91 | # Use the maximum available, or set MAX\_FD != -1 to use that value. |
| 93 | 92 | MAX\_FD=maximum |

[android/settings.gradle

MODIFIED

Raw](#androidsettingsgradle)

|  |  |  |
| --- | --- | --- |
| 1 | 1 | pluginManagement { |
| 2 |  | includeBuild(new File(["node", "--print", "require.resolve('@react-native/gradle-plugin/package.json', { paths: [require.resolve('react-native/package.json')] })"].execute(null, rootDir).text.trim()).getParentFile().toString()) |
|  | 2 | def reactNativeGradlePlugin = new File( |
|  | 3 | providers.exec { |
|  | 4 | workingDir(rootDir) |
|  | 5 | commandLine("node", "--print", "require.resolve('@react-native/gradle-plugin/package.json', { paths: [require.resolve('react-native/package.json')] })") |
|  | 6 | }.standardOutput.asText.get().trim() |
|  | 7 | ).getParentFile().absolutePath |
|  | 8 | includeBuild(reactNativeGradlePlugin) |
|  | 9 |  |
|  | 10 | def expoPluginsPath = new File( |
|  | 11 | providers.exec { |
|  | 12 | workingDir(rootDir) |
|  | 13 | commandLine("node", "--print", "require.resolve('expo-modules-autolinking/package.json', { paths: [require.resolve('expo/package.json')] })") |
|  | 14 | }.standardOutput.asText.get().trim(), |
|  | 15 | "../android/expo-gradle-plugin" |
|  | 16 | ).absolutePath |
|  | 17 | includeBuild(expoPluginsPath) |
|  | 18 | } |
|  | 19 |  |
|  | 20 | plugins { |
|  | 21 | id("com.facebook.react.settings") |
|  | 22 | id("expo-autolinking-settings") |
| 3 | 23 | } |
| 4 |  | plugins { id("com.facebook.react.settings") } |
| 5 | 24 |  |
| 6 | 25 | extensions.configure(com.facebook.react.ReactSettingsExtension) { ex -> |
| 7 | 26 | if (System.getenv('EXPO\_USE\_COMMUNITY\_AUTOLINKING') == '1') { |
| 8 | 27 | ex.autolinkLibrariesFromCommand() |
| 9 | 28 | } else { |
| 10 |  | def command = [ |
| 11 |  | 'node', |
| 12 |  | '--no-warnings', |
| 13 |  | '--eval', |
| 14 |  | 'require(require.resolve(\'expo-modules-autolinking\', { paths: [require.resolve(\'expo/package.json\')] }))(process.argv.slice(1))', |
| 15 |  | 'react-native-config', |
| 16 |  | '--json', |
| 17 |  | '--platform', |
| 18 |  | 'android' |
| 19 |  | ].toList() |
| 20 |  | ex.autolinkLibrariesFromCommand(command) |
|  | 29 | ex.autolinkLibrariesFromCommand(expoAutolinking.rnConfigCommand) |
| 21 | 30 | } |
| 22 | 31 | } |
|  | 32 | expoAutolinking.useExpoModules() |
| 23 | 33 |  |
| 24 | 34 | rootProject.name = 'HelloWorld' |
| 25 | 35 |  |
| 26 |  | dependencyResolutionManagement { |
| 27 |  | versionCatalogs { |
| 28 |  | reactAndroidLibs { |
| 29 |  | from(files(new File(["node", "--print", "require.resolve('react-native/package.json')"].execute(null, rootDir).text.trim(), "../gradle/libs.versions.toml"))) |
| 30 |  | } |
| 31 |  | } |
| 32 |  | } |
| 33 |  |  |
| 34 |  | apply from: new File(["node", "--print", "require.resolve('expo/package.json')"].execute(null, rootDir).text.trim(), "../scripts/autolinking.gradle"); |
| 35 |  | useExpoModules() |
|  | 36 | expoAutolinking.useExpoVersionCatalog() |
| 36 | 37 |  |
| 37 | 38 | include ':app' |
| 38 |  | includeBuild(new File(["node", "--print", "require.resolve('@react-native/gradle-plugin/package.json', { paths: [require.resolve('react-native/package.json')] })"].execute(null, rootDir).text.trim()).getParentFile()) |
|  | 39 | includeBuild(expoAutolinking.reactNativeGradlePlugin) |

[ios/HelloWorld.xcodeproj/project.pbxproj

MODIFIED

Raw](#ioshelloworldxcodeprojprojectpbxproj)

|  |  |  |
| --- | --- | --- |
| 3 | 3 | archiveVersion = 1; |
| 4 | 4 | classes = { |
| 5 | 5 | }; |
| 6 |  | objectVersion = 46; |
|  | 6 | objectVersion = 54; |
| 7 | 7 | objects = { |
| 8 | 8 |  |
| 9 | 9 | /\* Begin PBXBuildFile section \*/ |
| 10 |  | 13B07FBC1A68108700A75B9A /\* AppDelegate.mm in Sources \*/ = {isa = PBXBuildFile; fileRef = 13B07FB01A68108700A75B9A /\* AppDelegate.mm \*/; }; |
| 11 | 10 | 13B07FBF1A68108700A75B9A /\* Images.xcassets in Resources \*/ = {isa = PBXBuildFile; fileRef = 13B07FB51A68108700A75B9A /\* Images.xcassets \*/; }; |
| 12 |  | 13B07FC11A68108700A75B9A /\* main.m in Sources \*/ = {isa = PBXBuildFile; fileRef = 13B07FB71A68108700A75B9A /\* main.m \*/; }; |
| 13 | 11 | 3E461D99554A48A4959DE609 /\* SplashScreen.storyboard in Resources \*/ = {isa = PBXBuildFile; fileRef = AA286B85B6C04FC6940260E9 /\* SplashScreen.storyboard \*/; }; |
| 14 |  | 96905EF65AED1B983A6B3ABC /\* libPods-HelloWorld.a in Frameworks \*/ = {isa = PBXBuildFile; fileRef = 58EEBF8E8E6FB1BC6CAF49B5 /\* libPods-HelloWorld.a \*/; }; |
| 15 |  | B18059E884C0ABDD17F3DC3D /\* ExpoModulesProvider.swift in Sources \*/ = {isa = PBXBuildFile; fileRef = FAC715A2D49A985799AEE119 /\* ExpoModulesProvider.swift \*/; }; |
| 16 | 12 | BB2F792D24A3F905000567C9 /\* Expo.plist in Resources \*/ = {isa = PBXBuildFile; fileRef = BB2F792C24A3F905000567C9 /\* Expo.plist \*/; }; |
|  | 13 | F11748422D0307B40044C1D9 /\* AppDelegate.swift in Sources \*/ = {isa = PBXBuildFile; fileRef = F11748412D0307B40044C1D9 /\* AppDelegate.swift \*/; }; |
| 17 | 14 | /\* End PBXBuildFile section \*/ |
| 18 | 15 |  |
| 19 | 16 | /\* Begin PBXFileReference section \*/ |
| 20 | 17 | 13B07F961A680F5B00A75B9A /\* HelloWorld.app \*/ = {isa = PBXFileReference; explicitFileType = wrapper.application; includeInIndex = 0; path = HelloWorld.app; sourceTree = BUILT\_PRODUCTS\_DIR; }; |
| 21 |  | 13B07FAF1A68108700A75B9A /\* AppDelegate.h \*/ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.c.h; name = AppDelegate.h; path = HelloWorld/AppDelegate.h; sourceTree = "<group>"; }; |
| 22 |  | 13B07FB01A68108700A75B9A /\* AppDelegate.mm \*/ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.cpp.objcpp; name = AppDelegate.mm; path = HelloWorld/AppDelegate.mm; sourceTree = "<group>"; }; |
| 23 | 18 | 13B07FB51A68108700A75B9A /\* Images.xcassets \*/ = {isa = PBXFileReference; lastKnownFileType = folder.assetcatalog; name = Images.xcassets; path = HelloWorld/Images.xcassets; sourceTree = "<group>"; }; |
| 24 | 19 | 13B07FB61A68108700A75B9A /\* Info.plist \*/ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = text.plist.xml; name = Info.plist; path = HelloWorld/Info.plist; sourceTree = "<group>"; }; |
| 25 |  | 13B07FB71A68108700A75B9A /\* main.m \*/ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.c.objc; name = main.m; path = HelloWorld/main.m; sourceTree = "<group>"; }; |
| 26 |  | 58EEBF8E8E6FB1BC6CAF49B5 /\* libPods-HelloWorld.a \*/ = {isa = PBXFileReference; explicitFileType = archive.ar; includeInIndex = 0; path = "libPods-HelloWorld.a"; sourceTree = BUILT\_PRODUCTS\_DIR; }; |
| 27 |  | 6C2E3173556A471DD304B334 /\* Pods-HelloWorld.debug.xcconfig \*/ = {isa = PBXFileReference; includeInIndex = 1; lastKnownFileType = text.xcconfig; name = "Pods-HelloWorld.debug.xcconfig"; path = "Target Support Files/Pods-HelloWorld/Pods-HelloWorld.debug.xcconfig"; sourceTree = "<group>"; }; |
| 28 |  | 7A4D352CD337FB3A3BF06240 /\* Pods-HelloWorld.release.xcconfig \*/ = {isa = PBXFileReference; includeInIndex = 1; lastKnownFileType = text.xcconfig; name = "Pods-HelloWorld.release.xcconfig"; path = "Target Support Files/Pods-HelloWorld/Pods-HelloWorld.release.xcconfig"; sourceTree = "<group>"; }; |
| 29 | 20 | AA286B85B6C04FC6940260E9 /\* SplashScreen.storyboard \*/ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = file.storyboard; name = SplashScreen.storyboard; path = HelloWorld/SplashScreen.storyboard; sourceTree = "<group>"; }; |
| 30 | 21 | BB2F792C24A3F905000567C9 /\* Expo.plist \*/ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = text.plist.xml; path = Expo.plist; sourceTree = "<group>"; }; |
| 31 | 22 | ED297162215061F000B7C4FE /\* JavaScriptCore.framework \*/ = {isa = PBXFileReference; lastKnownFileType = wrapper.framework; name = JavaScriptCore.framework; path = System/Library/Frameworks/JavaScriptCore.framework; sourceTree = SDKROOT; }; |
| 32 |  | FAC715A2D49A985799AEE119 /\* ExpoModulesProvider.swift \*/ = {isa = PBXFileReference; includeInIndex = 1; lastKnownFileType = sourcecode.swift; name = ExpoModulesProvider.swift; path = "Pods/Target Support Files/Pods-HelloWorld/ExpoModulesProvider.swift"; sourceTree = "<group>"; }; |
|  | 23 | F11748412D0307B40044C1D9 /\* AppDelegate.swift \*/ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; name = AppDelegate.swift; path = HelloWorld/AppDelegate.swift; sourceTree = "<group>"; }; |
|  | 24 | F11748442D0722820044C1D9 /\* HelloWorld-Bridging-Header.h \*/ = {isa = PBXFileReference; lastKnownFileType = sourcecode.c.h; name = "HelloWorld-Bridging-Header.h"; path = "HelloWorld/HelloWorld-Bridging-Header.h"; sourceTree = "<group>"; }; |
| 33 | 25 | /\* End PBXFileReference section \*/ |
| 34 | 26 |  |
| 35 | 27 | /\* Begin PBXFrameworksBuildPhase section \*/ |
|  |  |  |
| --- | --- | --- |
| 37 | 29 | isa = PBXFrameworksBuildPhase; |
| 38 | 30 | buildActionMask = 2147483647; |
| 39 | 31 | files = ( |
| 40 |  | 96905EF65AED1B983A6B3ABC /\* libPods-HelloWorld.a in Frameworks \*/, |
| 41 | 32 | ); |
| 42 | 33 | runOnlyForDeploymentPostprocessing = 0; |
| 43 | 34 | }; |
|  |  |  |
| --- | --- | --- |
| 47 | 38 | 13B07FAE1A68108700A75B9A /\* HelloWorld \*/ = { |
| 48 | 39 | isa = PBXGroup; |
| 49 | 40 | children = ( |
|  | 41 | F11748412D0307B40044C1D9 /\* AppDelegate.swift \*/, |
|  | 42 | F11748442D0722820044C1D9 /\* HelloWorld-Bridging-Header.h \*/, |
| 50 | 43 | BB2F792B24A3F905000567C9 /\* Supporting \*/, |
| 51 |  | 13B07FAF1A68108700A75B9A /\* AppDelegate.h \*/, |
| 52 |  | 13B07FB01A68108700A75B9A /\* AppDelegate.mm \*/, |
| 53 | 44 | 13B07FB51A68108700A75B9A /\* Images.xcassets \*/, |
| 54 | 45 | 13B07FB61A68108700A75B9A /\* Info.plist \*/, |
| 55 |  | 13B07FB71A68108700A75B9A /\* main.m \*/, |
| 56 | 46 | AA286B85B6C04FC6940260E9 /\* SplashScreen.storyboard \*/, |
| 57 | 47 | ); |
| 58 | 48 | name = HelloWorld; |
|  |  |  |
| --- | --- | --- |
| 62 | 52 | isa = PBXGroup; |
| 63 | 53 | children = ( |
| 64 | 54 | ED297162215061F000B7C4FE /\* JavaScriptCore.framework \*/, |
| 65 |  | 58EEBF8E8E6FB1BC6CAF49B5 /\* libPods-HelloWorld.a \*/, |
| 66 | 55 | ); |
| 67 | 56 | name = Frameworks; |
| 68 | 57 | sourceTree = "<group>"; |
|  |  |  |
| --- | --- | --- |
| 81 | 70 | 832341AE1AAA6A7D00B99B32 /\* Libraries \*/, |
| 82 | 71 | 83CBBA001A601CBA00E9B192 /\* Products \*/, |
| 83 | 72 | 2D16E6871FA4F8E400B85C8A /\* Frameworks \*/, |
| 84 |  | D65327D7A22EEC0BE12398D9 /\* Pods \*/, |
| 85 |  | D7E4C46ADA2E9064B798F356 /\* ExpoModulesProviders \*/, |
| 86 | 73 | ); |
| 87 | 74 | indentWidth = 2; |
| 88 | 75 | sourceTree = "<group>"; |
|  |  |  |
| --- | --- | --- |
| 97 | 84 | name = Products; |
| 98 | 85 | sourceTree = "<group>"; |
| 99 | 86 | }; |
| 100 |  | 92DBD88DE9BF7D494EA9DA96 /\* HelloWorld \*/ = { |
| 101 |  | isa = PBXGroup; |
| 102 |  | children = ( |
| 103 |  | FAC715A2D49A985799AEE119 /\* ExpoModulesProvider.swift \*/, |
| 104 |  | ); |
| 105 |  | name = HelloWorld; |
| 106 |  | sourceTree = "<group>"; |
| 107 |  | }; |
| 108 | 87 | BB2F792B24A3F905000567C9 /\* Supporting \*/ = { |
| 109 | 88 | isa = PBXGroup; |
| 110 | 89 | children = ( |
|  |  |  |
| --- | --- | --- |
| 114 | 93 | path = HelloWorld/Supporting; |
| 115 | 94 | sourceTree = "<group>"; |
| 116 | 95 | }; |
| 117 |  | D65327D7A22EEC0BE12398D9 /\* Pods \*/ = { |
| 118 |  | isa = PBXGroup; |
| 119 |  | children = ( |
| 120 |  | 6C2E3173556A471DD304B334 /\* Pods-HelloWorld.debug.xcconfig \*/, |
| 121 |  | 7A4D352CD337FB3A3BF06240 /\* Pods-HelloWorld.release.xcconfig \*/, |
| 122 |  | ); |
| 123 |  | path = Pods; |
| 124 |  | sourceTree = "<group>"; |
| 125 |  | }; |
| 126 |  | D7E4C46ADA2E9064B798F356 /\* ExpoModulesProviders \*/ = { |
| 127 |  | isa = PBXGroup; |
| 128 |  | children = ( |
| 129 |  | 92DBD88DE9BF7D494EA9DA96 /\* HelloWorld \*/, |
| 130 |  | ); |
| 131 |  | name = ExpoModulesProviders; |
| 132 |  | sourceTree = "<group>"; |
| 133 |  | }; |
| 134 | 96 | /\* End PBXGroup section \*/ |
| 135 | 97 |  |
| 136 | 98 | /\* Begin PBXNativeTarget section \*/ |
|  |  |  |
| --- | --- | --- |
| 265 | 227 | isa = PBXSourcesBuildPhase; |
| 266 | 228 | buildActionMask = 2147483647; |
| 267 | 229 | files = ( |
| 268 |  | 13B07FBC1A68108700A75B9A /\* AppDelegate.mm in Sources \*/, |
| 269 |  | 13B07FC11A68108700A75B9A /\* main.m in Sources \*/, |
| 270 |  | B18059E884C0ABDD17F3DC3D /\* ExpoModulesProvider.swift in Sources \*/, |
|  | 230 | F11748422D0307B40044C1D9 /\* AppDelegate.swift in Sources \*/, |
| 271 | 231 | ); |
| 272 | 232 | runOnlyForDeploymentPostprocessing = 0; |
| 273 | 233 | }; |
|  |  |  |
| --- | --- | --- |
| 276 | 236 | /\* Begin XCBuildConfiguration section \*/ |
| 277 | 237 | 13B07F941A680F5B00A75B9A /\* Debug \*/ = { |
| 278 | 238 | isa = XCBuildConfiguration; |
| 279 |  | baseConfigurationReference = 6C2E3173556A471DD304B334 /\* Pods-HelloWorld.debug.xcconfig \*/; |
| 280 | 239 | buildSettings = { |
| 281 | 240 | ASSETCATALOG\_COMPILER\_APPICON\_NAME = AppIcon; |
| 282 | 241 | CLANG\_ENABLE\_MODULES = YES; |
|  |  |  |
| --- | --- | --- |
| 288 | 247 | ); |
| 289 | 248 | INFOPLIST\_FILE = HelloWorld/Info.plist; |
| 290 | 249 | IPHONEOS\_DEPLOYMENT\_TARGET = 15.1; |
| 291 |  | LD\_RUNPATH\_SEARCH\_PATHS = "$(inherited) @executable\_path/Frameworks"; |
|  | 250 | LD\_RUNPATH\_SEARCH\_PATHS = ( |
|  | 251 | "$(inherited)", |
|  | 252 | "@executable\_path/Frameworks", |
|  | 253 | ); |
| 292 | 254 | MARKETING\_VERSION = 1.0; |
| 293 | 255 | OTHER\_LDFLAGS = ( |
| 294 | 256 | "$(inherited)", |
|  |  |  |
| --- | --- | --- |
| 297 | 259 | ); |
| 298 | 260 | PRODUCT\_BUNDLE\_IDENTIFIER = org.name.HelloWorld; |
| 299 | 261 | PRODUCT\_NAME = HelloWorld; |
|  | 262 | SWIFT\_OBJC\_BRIDGING\_HEADER = "HelloWorld/HelloWorld-Bridging-Header.h"; |
| 300 | 263 | SWIFT\_OPTIMIZATION\_LEVEL = "-Onone"; |
| 301 | 264 | SWIFT\_VERSION = 5.0; |
| 302 | 265 | VERSIONING\_SYSTEM = "apple-generic"; |
|  |  |  |
| --- | --- | --- |
| 305 | 268 | }; |
| 306 | 269 | 13B07F951A680F5B00A75B9A /\* Release \*/ = { |
| 307 | 270 | isa = XCBuildConfiguration; |
| 308 |  | baseConfigurationReference = 7A4D352CD337FB3A3BF06240 /\* Pods-HelloWorld.release.xcconfig \*/; |
| 309 | 271 | buildSettings = { |
| 310 | 272 | ASSETCATALOG\_COMPILER\_APPICON\_NAME = AppIcon; |
| 311 | 273 | CLANG\_ENABLE\_MODULES = YES; |
| 312 | 274 | CURRENT\_PROJECT\_VERSION = 1; |
| 313 | 275 | INFOPLIST\_FILE = HelloWorld/Info.plist; |
| 314 | 276 | IPHONEOS\_DEPLOYMENT\_TARGET = 15.1; |
| 315 |  | LD\_RUNPATH\_SEARCH\_PATHS = "$(inherited) @executable\_path/Frameworks"; |
|  | 277 | LD\_RUNPATH\_SEARCH\_PATHS = ( |
|  | 278 | "$(inherited)", |
|  | 279 | "@executable\_path/Frameworks", |
|  | 280 | ); |
| 316 | 281 | MARKETING\_VERSION = 1.0; |
| 317 | 282 | OTHER\_LDFLAGS = ( |
| 318 | 283 | "$(inherited)", |
|  |  |  |
| --- | --- | --- |
| 321 | 286 | ); |
| 322 | 287 | PRODUCT\_BUNDLE\_IDENTIFIER = org.name.HelloWorld; |
| 323 | 288 | PRODUCT\_NAME = HelloWorld; |
|  | 289 | SWIFT\_OBJC\_BRIDGING\_HEADER = "HelloWorld/HelloWorld-Bridging-Header.h"; |
| 324 | 290 | SWIFT\_VERSION = 5.0; |
| 325 | 291 | VERSIONING\_SYSTEM = "apple-generic"; |
| 326 | 292 | }; |
|  |  |  |
| --- | --- | --- |
| 374 | 340 | GCC\_WARN\_UNUSED\_FUNCTION = YES; |
| 375 | 341 | GCC\_WARN\_UNUSED\_VARIABLE = YES; |
| 376 | 342 | IPHONEOS\_DEPLOYMENT\_TARGET = 15.1; |
| 377 |  | LD\_RUNPATH\_SEARCH\_PATHS = "/usr/lib/swift $(inherited)"; |
|  | 343 | LD\_RUNPATH\_SEARCH\_PATHS = ( |
|  | 344 | /usr/lib/swift, |
|  | 345 | "$(inherited)", |
|  | 346 | ); |
| 378 | 347 | LIBRARY\_SEARCH\_PATHS = "\"$(inherited)\""; |
| 379 | 348 | MTL\_ENABLE\_DEBUG\_INFO = YES; |
| 380 | 349 | ONLY\_ACTIVE\_ARCH = YES; |
|  |  |  |
| --- | --- | --- |
| 423 | 392 | GCC\_WARN\_UNUSED\_FUNCTION = YES; |
| 424 | 393 | GCC\_WARN\_UNUSED\_VARIABLE = YES; |
| 425 | 394 | IPHONEOS\_DEPLOYMENT\_TARGET = 15.1; |
| 426 |  | LD\_RUNPATH\_SEARCH\_PATHS = "/usr/lib/swift $(inherited)"; |
|  | 395 | LD\_RUNPATH\_SEARCH\_PATHS = ( |
|  | 396 | /usr/lib/swift, |
|  | 397 | "$(inherited)", |
|  | 398 | ); |
| 427 | 399 | LIBRARY\_SEARCH\_PATHS = "\"$(inherited)\""; |
| 428 | 400 | MTL\_ENABLE\_DEBUG\_INFO = NO; |
| 429 | 401 | SDKROOT = iphoneos; |

[ios/HelloWorld.xcworkspace/contents.xcworkspacedata

DELETED](#ioshelloworldxcworkspacecontentsxcworkspacedata)

[ios/HelloWorld.xcworkspace/xcshareddata/IDEWorkspaceChecks.plist

DELETED](#ioshelloworldxcworkspacexcshareddataideworkspacechecksplist)

[ios/HelloWorld/AppDelegate.h

DELETED](#ioshelloworldappdelegateh)

[ios/HelloWorld/AppDelegate.mm

DELETED](#ioshelloworldappdelegatemm)

[ios/HelloWorld/AppDelegate.swift

ADDED

Raw](#ioshelloworldappdelegateswift)

|  |  |  |
| --- | --- | --- |
|  | 1 | import Expo |
|  | 2 | import React |
|  | 3 | import ReactAppDependencyProvider |
|  | 4 |  |
|  | 5 | @UIApplicationMain |
|  | 6 | public class AppDelegate: ExpoAppDelegate { |
|  | 7 | var window: UIWindow? |
|  | 8 |  |
|  | 9 | var reactNativeDelegate: ExpoReactNativeFactoryDelegate? |
|  | 10 | var reactNativeFactory: RCTReactNativeFactory? |
|  | 11 |  |
|  | 12 | public override func application( |
|  | 13 | \_ application: UIApplication, |
|  | 14 | didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil |
|  | 15 | ) -> Bool { |
|  | 16 | let delegate = ReactNativeDelegate() |
|  | 17 | let factory = ExpoReactNativeFactory(delegate: delegate) |
|  | 18 | delegate.dependencyProvider = RCTAppDependencyProvider() |
|  | 19 |  |
|  | 20 | reactNativeDelegate = delegate |
|  | 21 | reactNativeFactory = factory |
|  | 22 | bindReactNativeFactory(factory) |
|  | 23 |  |
|  | 24 | #if os(iOS) || os(tvOS) |
|  | 25 | window = UIWindow(frame: UIScreen.main.bounds) |
|  | 26 | factory.startReactNative( |
|  | 27 | withModuleName: "main", |
|  | 28 | in: window, |
|  | 29 | launchOptions: launchOptions) |
|  | 30 | #endif |
|  | 31 |  |
|  | 32 | return super.application(application, didFinishLaunchingWithOptions: launchOptions) |
|  | 33 | } |
|  | 34 |  |
|  | 35 | // Linking API |
|  | 36 | public override func application( |
|  | 37 | \_ app: UIApplication, |
|  | 38 | open url: URL, |
|  | 39 | options: [UIApplication.OpenURLOptionsKey: Any] = [:] |
|  | 40 | ) -> Bool { |
|  | 41 | return super.application(app, open: url, options: options) || RCTLinkingManager.application(app, open: url, options: options) |
|  | 42 | } |
|  | 43 |  |
|  | 44 | // Universal Links |
|  | 45 | public override func application( |
|  | 46 | \_ application: UIApplication, |
|  | 47 | continue userActivity: NSUserActivity, |
|  | 48 | restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void |
|  | 49 | ) -> Bool { |
|  | 50 | let result = RCTLinkingManager.application(application, continue: userActivity, restorationHandler: restorationHandler) |
|  | 51 | return super.application(application, continue: userActivity, restorationHandler: restorationHandler) || result |
|  | 52 | } |
|  | 53 | } |
|  | 54 |  |
|  | 55 | class ReactNativeDelegate: ExpoReactNativeFactoryDelegate { |
|  | 56 | // Extension point for config-plugins |
|  | 57 |  |
|  | 58 | override func sourceURL(for bridge: RCTBridge) -> URL? { |
|  | 59 | // needed to return the correct URL for expo-dev-client. |
|  | 60 | bridge.bundleURL ?? bundleURL() |
|  | 61 | } |
|  | 62 |  |
|  | 63 | override func bundleURL() -> URL? { |
|  | 64 | #if DEBUG |
|  | 65 | return RCTBundleURLProvider.sharedSettings().jsBundleURL(forBundleRoot: ".expo/.virtual-metro-entry") |
|  | 66 | #else |
|  | 67 | return Bundle.main.url(forResource: "main", withExtension: "jsbundle") |
|  | 68 | #endif |
|  | 69 | } |
|  | 70 | } |

[ios/HelloWorld/HelloWorld-Bridging-Header.h

ADDED

Raw](#ioshelloworldhelloworld-bridging-headerh)

|  |  |  |
| --- | --- | --- |
|  | 1 | // |
|  | 2 | // Use this file to import your target's public headers that you would like to expose to Swift. |
|  | 3 | // |

[ios/HelloWorld/main.m

DELETED](#ioshelloworldmainm)

[ios/Podfile

MODIFIED

Raw](#iospodfile)

|  |  |  |
| --- | --- | --- |
| 4 | 4 | require 'json' |
| 5 | 5 | podfile\_properties = JSON.parse(File.read(File.join(\_\_dir\_\_, 'Podfile.properties.json'))) rescue {} |
| 6 | 6 |  |
| 7 |  | ENV['RCT\_NEW\_ARCH\_ENABLED'] = podfile\_properties['newArchEnabled'] == 'true' ? '1' : '0' |
|  | 7 | ENV['RCT\_NEW\_ARCH\_ENABLED'] = '0' if podfile\_properties['newArchEnabled'] == 'false' |
| 8 | 8 | ENV['EX\_DEV\_CLIENT\_NETWORK\_INSPECTOR'] = podfile\_properties['EX\_DEV\_CLIENT\_NETWORK\_INSPECTOR'] |
| 9 | 9 |  |
| 10 | 10 | platform :ios, podfile\_properties['ios.deploymentTarget'] || '15.1' |
|  |  |  |
| --- | --- | --- |
| 20 | 20 | config\_command = ['node', '-e', "process.argv=['', '', 'config'];require('@react-native-community/cli').run()"]; |
| 21 | 21 | else |
| 22 | 22 | config\_command = [ |
| 23 |  | 'node', |
| 24 |  | '--no-warnings', |
| 25 |  | '--eval', |
| 26 |  | 'require(require.resolve(\'expo-modules-autolinking\', { paths: [require.resolve(\'expo/package.json\')] }))(process.argv.slice(1))', |
|  | 23 | 'npx', |
|  | 24 | 'expo-modules-autolinking', |
| 27 | 25 | 'react-native-config', |
| 28 | 26 | '--json', |
| 29 | 27 | '--platform', |

[package.json

MODIFIED

Raw](#packagejson)

|  |  |  |
| --- | --- | --- |
| 2 | 2 | "name": "expo-template-bare-minimum", |
| 3 | 3 | "description": "This bare project template includes a minimal setup for using unimodules with React Native.", |
| 4 | 4 | "license": "0BSD", |
| 5 |  | "version": "52.0.76", |
|  | 5 | "version": "53.0.25", |
| 6 | 6 | "main": "index.js", |
| 7 | 7 | "scripts": { |
| 8 | 8 | "start": "expo start --dev-client", |
|  |  |  |
| --- | --- | --- |
| 11 | 11 | "web": "expo start --web" |
| 12 | 12 | }, |
| 13 | 13 | "dependencies": { |
| 14 |  | "expo": "~52.0.46", |
| 15 |  | "expo-status-bar": "~2.0.1", |
| 16 |  | "react": "18.3.1", |
| 17 |  | "react-native": "0.76.9" |
|  | 14 | "expo": "~53.0.7", |
|  | 15 | "expo-status-bar": "~2.2.3", |
|  | 16 | "react": "19.0.0", |
|  | 17 | "react-native": "0.79.2" |
| 18 | 18 | }, |
| 19 | 19 | "devDependencies": { |
| 20 | 20 | "@babel/core": "^7.20.0" |

[Previous (Development process - Existing React Native apps)

Install expo-dev-client](/bare/install-dev-builds-in-bare)[Next (Development process - Existing native apps)

Overview](/brownfield/overview)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/bare/upgrade.mdx)
* Last updated on June 10, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Upgrade native project files](/bare/upgrade/#upgrade-native-project-files)[`android/../build.gradle`](/bare/upgrade/#androidappbuildgradle)[`android/../styles.xml`](/bare/upgrade/#androidappsrcmainresvaluesstylesxml)[`android/build.gradle`](/bare/upgrade/#androidbuildgradle)[`android/gradle.properties`](/bare/upgrade/#androidgradleproperties)[`android/../gradle-wrapper.properties`](/bare/upgrade/#androidgradlewrappergradle-wrapperproperties)[`android/gradlew`](/bare/upgrade/#androidgradlew)[`android/settings.gradle`](/bare/upgrade/#androidsettingsgradle)[`ios/../project.pbxproj`](/bare/upgrade/#ioshelloworldxcodeprojprojectpbxproj)[`ios/../contents.xcworkspacedata`](/bare/upgrade/#ioshelloworldxcworkspacecontentsxcworkspacedata)[`ios/../IDEWorkspaceChecks.plist`](/bare/upgrade/#ioshelloworldxcworkspacexcshareddataideworkspacechecksplist)[`ios/../AppDelegate.h`](/bare/upgrade/#ioshelloworldappdelegateh)[`ios/../AppDelegate.mm`](/bare/upgrade/#ioshelloworldappdelegatemm)[`ios/../AppDelegate.swift`](/bare/upgrade/#ioshelloworldappdelegateswift)[`ios/../HelloWorld-Bridging-Header.h`](/bare/upgrade/#ioshelloworldhelloworld-bridging-headerh)[`ios/../main.m`](/bare/upgrade/#ioshelloworldmainm)[`ios/Podfile`](/bare/upgrade/#iospodfile)[`package.json`](/bare/upgrade/#packagejson)