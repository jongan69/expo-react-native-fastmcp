Create a production build locally - Expo Documentation

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

[Development](/guides/local-app-development)[Production](/guides/local-app-production)[Cache builds remotely](/guides/cache-builds-remotely)

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

Create a production build locally
=================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/local-app-production.mdx)

Learn how to create a production build for your Expo app locally.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/local-app-production.mdx)

---

To create your app's production build (also known as release build) locally, you need to follow separate steps on your computer and use the tools required to create any native app. This guide provides the necessary steps for Android and iOS.

Android
-------

Creating a production build locally for Android requires signing it with an [upload key](https://developer.android.com/studio/publish/app-signing#certificates-keystores) and generating an Android Application Bundle (.aab). Follow the steps below:

### Prerequisites

* [OpenJDK distribution](/get-started/set-up-your-environment?mode=development-build&buildEnv=local#install-watchman-and-jdk) installed to access the `keytool` command
* android directory generated. If you are using [CNG](/workflow/continuous-native-generation), then run `npx expo prebuild` to generate it.

1

### Create an upload key

Already created a build with EAS Build? Download your credentials and skip to the next step.

If you've already created a build with EAS Build, follow the steps below to download the credentials, which contains the upload key and its password, key alias, and key password:

1. In your terminal, run `eas credentials -p android` and select the build profile.
2. Select credentials.json > Download credentials from EAS to credentials.json.
3. Move the downloaded keystore.jks file to the android/app directory.
4. Copy the values for the upload keystore password, key alias, and key password from the credentials.json as you will need them in the next step.

Inside your Expo project directory, run the following `keytool` command to create an upload key:

Terminal

Copy

`-Â``sudo keytool -genkey -v -keystore my-upload-key.keystore -alias my-key-alias -keyalg RSA -keysize 2048 -validity 10000`

After running this command, you will be prompted to enter a password for the keystore. This password will protect the upload key. Remember the password you enter here, as you'll need it in the next step.

This command also generates the keystore file named my-upload-key.keystore in your project directory. Move it to the android/app directory.

> If you commit the android directory to a version control system like Git, don't commit this keystore file. It contains your upload key and should be kept private.

2

### Update gradle variables

Open android/gradle.properties file and add the following gradle variables at the end of the file. Replace the `*****` with the correct keystore and key password that you provided in the previous step.

These variables contain information about your upload key:

android/gradle.properties

Copy

```
# If you've downloaded the credentials from `eas credentials` command, see comments below for each value.

MYAPP_UPLOAD_STORE_FILE=my-upload-key.keystore     # Path to the "keystore.jks" file
MYAPP_UPLOAD_KEY_ALIAS=my-key-alias                # Replace with value of the `keystore.keyAlias` field in the credentials.json file
MYAPP_UPLOAD_STORE_PASSWORD=*****                  # Replace with value of the `keystore.password` field in the credentials.json file
MYAPP_UPLOAD_KEY_PASSWORD=*****                    # Replace with value of the `keystore.keyPassword` field in the credentials.json file

```

> If you commit the android directory to a version control system like Git, don't commit the above information. Instead, create a ~/.gradle/gradle.properties file on your computer and add the above variables to this file.

3

### Add signing config to build.gradle

Open android/app/build.gradle file and add the following configuration:

4

### Generate release Android Application Bundle (aab)

Navigate inside the android directory and create a production build in .aab format by running Gradle's `bundleRelease` command:

Terminal

Copy

`-Â``cd android`

  

`-Â``./gradlew app:bundleRelease`

This command will generate app-release.aab inside the android/app/build/outputs/bundle/release directory.

5

### Manual app submission to Google Play Console

Google Play Store requires manual app submission when submitting the .aab file for the first time.

[Manual submission of an Android app

Follow the steps from the FYI guide on manually submitting your app to Google Play Store for the first time.](https://expo.fyi/first-android-submission)

iOS
---

To create an iOS production build locally for Apple App Store, you need to use Xcode which handles the signing and submission process via App Store Connect.

### Prerequisites

* Paid Apple Developer membership
* [Xcode installed](/get-started/set-up-your-environment?platform=ios&device=physical&mode=development-build&buildEnv=local#set-up-xcode-and-watchman) on your computer
* ios directory generated. If you are using [CNG](/workflow/continuous-native-generation), then run `npx expo prebuild` to generate it.

1

### Open iOS workspace in Xcode

Inside your Expo project directory, run the following command to open `your-project.xcworkspace` in Xcode:

Terminal

Copy

`-Â``xed ios`

After opening the iOS project in Xcode:

1. From the sidebar on the left, select your app's workspace.
2. Go to Signing & Capabilities and select All or Release.
3. Under Signing > Team, ensure your Apple Developer team is selected. Xcode will generate an automatically managed Provisioning Profile and Signing Certificate.

2

### Configure a release scheme

To configure your app's release scheme:

1. From the menu bar, open Product > Scheme > Edit Scheme.
2. Select Run from the sidebar, then set the Build configuration to Release using the dropdown.

3

### Build app for release

To build your app for release, From the menu bar, open Product > Build. This step will build your app binary for release.

4

### App submission using App Store Connect

Once the build is complete, you can distribute your app to TestFlight or submit it to the App Store using App Store Connect:

1. From the menu bar, open Product > Archive.
2. Under Archives, click Distribute App from the right sidebar.
3. Click App Store Connect and follow the prompts shown in the window. This step will create an app store record and upload your app to the App Store.
4. Now you can go to your App Store Connect account, select your app under Apps, and submit it for testing using TestFlight or prepare it for final release by following the steps in the App Store Connect dashboard.

[Previous (Development process - Compile locally)

Development](/guides/local-app-development)[Next (Development process - Compile locally)

Cache builds remotely](/guides/cache-builds-remotely)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/local-app-production.mdx)
* Last updated on March 26, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Android](/guides/local-app-production/#android)[Prerequisites](/guides/local-app-production/#prerequisites)[Create an upload key](/guides/local-app-production/#create-an-upload-key)[Update gradle variables](/guides/local-app-production/#update-gradle-variables)[Add signing config to build.gradle](/guides/local-app-production/#add-signing-config-to-buildgradle)[Generate release Android Application Bundle (aab)](/guides/local-app-production/#generate-release-android-application-bundle-aab)[Manual app submission to Google Play Console](/guides/local-app-production/#manual-app-submission-to-google-play-console)[iOS](/guides/local-app-production/#ios)[Prerequisites](/guides/local-app-production/#prerequisites-1)[Open iOS workspace in Xcode](/guides/local-app-production/#open-ios-workspace-in-xcode)[Configure a release scheme](/guides/local-app-production/#configure-a-release-scheme)[Build app for release](/guides/local-app-production/#build-app-for-release)[App submission using App Store Connect](/guides/local-app-production/#app-submission-using-app-store-connect)