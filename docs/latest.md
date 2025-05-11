Reference - Expo Documentation

[Docs](/)

[Blog](https://expo.dev/blog)[Changelog](https://expo.dev/changelog)[Star Us on GitHub](https://github.com/expo/expo)

Search

[Home](/)[Guides](/guides/overview)[EAS](/eas)[Reference](/versions/latest)[Learn](/tutorial/overview)

Reference version

Configuration files

[app.json / app.config.js](/versions/latest/config/app)[babel.config.js](/versions/latest/config/babel)[metro.config.js](/versions/latest/config/metro)[package.json](/versions/latest/config/package-json)

Expo SDK

[Expo](/versions/latest/sdk/expo)[Accelerometer](/versions/latest/sdk/accelerometer)[AppleAuthentication](/versions/latest/sdk/apple-authentication)[Application](/versions/latest/sdk/application)[Asset](/versions/latest/sdk/asset)[Audio (expo-audio)](/versions/latest/sdk/audio)[Audio (expo-av)](/versions/latest/sdk/audio-av)[AuthSession](/versions/latest/sdk/auth-session)[AV](/versions/latest/sdk/av)[BackgroundFetch](/versions/latest/sdk/background-fetch)[BackgroundTask

NEW](/versions/latest/sdk/background-task)[Barometer](/versions/latest/sdk/barometer)[Battery](/versions/latest/sdk/battery)[BlurView](/versions/latest/sdk/blur-view)[Brightness](/versions/latest/sdk/brightness)[BuildProperties](/versions/latest/sdk/build-properties)[Calendar](/versions/latest/sdk/calendar)[Camera](/versions/latest/sdk/camera)[Cellular](/versions/latest/sdk/cellular)[Checkbox](/versions/latest/sdk/checkbox)[Clipboard](/versions/latest/sdk/clipboard)[Constants](/versions/latest/sdk/constants)[Contacts](/versions/latest/sdk/contacts)[Crypto](/versions/latest/sdk/crypto)[DevClient](/versions/latest/sdk/dev-client)[Device](/versions/latest/sdk/device)[DeviceMotion](/versions/latest/sdk/devicemotion)[DocumentPicker](/versions/latest/sdk/document-picker)[FileSystem](/versions/latest/sdk/filesystem)[FileSystem (next)](/versions/latest/sdk/filesystem-next)[Fingerprint

NEW](/versions/latest/sdk/fingerprint)[Font](/versions/latest/sdk/font)[GLView](/versions/latest/sdk/gl-view)[Gyroscope](/versions/latest/sdk/gyroscope)[Haptics](/versions/latest/sdk/haptics)[Image](/versions/latest/sdk/image)[ImageManipulator](/versions/latest/sdk/imagemanipulator)[ImagePicker](/versions/latest/sdk/imagepicker)[IntentLauncher](/versions/latest/sdk/intent-launcher)[KeepAwake](/versions/latest/sdk/keep-awake)[LightSensor](/versions/latest/sdk/light-sensor)[LinearGradient](/versions/latest/sdk/linear-gradient)[Linking](/versions/latest/sdk/linking)[LivePhoto](/versions/latest/sdk/live-photo)[LocalAuthentication](/versions/latest/sdk/local-authentication)[Localization](/versions/latest/sdk/localization)[Location](/versions/latest/sdk/location)[Magnetometer](/versions/latest/sdk/magnetometer)[MailComposer](/versions/latest/sdk/mail-composer)[Manifests](/versions/latest/sdk/manifests)[Maps

ALPHA](/versions/latest/sdk/maps)[MediaLibrary](/versions/latest/sdk/media-library)[MeshGradient

NEW](/versions/latest/sdk/mesh-gradient)[NavigationBar](/versions/latest/sdk/navigation-bar)[Network](/versions/latest/sdk/network)[Notifications](/versions/latest/sdk/notifications)[Pedometer](/versions/latest/sdk/pedometer)[Print](/versions/latest/sdk/print)[Router](/versions/latest/sdk/router)[Router UI](/versions/latest/sdk/router-ui)[ScreenCapture](/versions/latest/sdk/screen-capture)[ScreenOrientation](/versions/latest/sdk/screen-orientation)[SecureStore](/versions/latest/sdk/securestore)[Sensors](/versions/latest/sdk/sensors)[Sharing](/versions/latest/sdk/sharing)[SMS](/versions/latest/sdk/sms)[Speech](/versions/latest/sdk/speech)[SplashScreen](/versions/latest/sdk/splash-screen)[SQLite](/versions/latest/sdk/sqlite)[StatusBar](/versions/latest/sdk/status-bar)[StoreReview](/versions/latest/sdk/storereview)[Symbols](/versions/latest/sdk/symbols)[SystemUI](/versions/latest/sdk/system-ui)[TaskManager](/versions/latest/sdk/task-manager)[TrackingTransparency](/versions/latest/sdk/tracking-transparency)[UI

ALPHA](/versions/latest/sdk/ui)[Updates](/versions/latest/sdk/updates)[Video (expo-av)](/versions/latest/sdk/video-av)[Video (expo-video)](/versions/latest/sdk/video)[VideoThumbnails](/versions/latest/sdk/video-thumbnails)[WebBrowser](/versions/latest/sdk/webbrowser)

Third-party libraries

[Overview](/versions/latest/sdk/third-party-overview)[@react-native-async-storage/async-storage](/versions/latest/sdk/async-storage)[@react-native-community/datetimepicker](/versions/latest/sdk/date-time-picker)[@react-native-community/netinfo](/versions/latest/sdk/netinfo)[@react-native-community/slider](/versions/latest/sdk/slider)[@react-native-masked-view/masked-view](/versions/latest/sdk/masked-view)[@react-native-picker/picker](/versions/latest/sdk/picker)[@react-native-segmented-control/segmented-control](/versions/latest/sdk/segmented-control)[@shopify/flash-list](/versions/latest/sdk/flash-list)[@shopify/react-native-skia](/versions/latest/sdk/skia)[@stripe/stripe-react-native](/versions/latest/sdk/stripe)[lottie-react-native](/versions/latest/sdk/lottie)[react-native-gesture-handler](/versions/latest/sdk/gesture-handler)[react-native-maps](/versions/latest/sdk/map-view)[react-native-pager-view](/versions/latest/sdk/view-pager)[react-native-reanimated](/versions/latest/sdk/reanimated)[react-native-safe-area-context](/versions/latest/sdk/safe-area-context)[react-native-screens](/versions/latest/sdk/screens)[react-native-svg](/versions/latest/sdk/svg)[react-native-view-shot](/versions/latest/sdk/captureRef)[react-native-webview](/versions/latest/sdk/webview)

Technical specs

[Expo Updates v1](/technical-specs/expo-updates-1)[Expo Structured Field Values](/technical-specs/expo-sfv-0)

More

[Expo CLI](/more/expo-cli)[create-expo-app](/more/create-expo)[qr.expo.dev](/more/qr-codes)[Glossary of terms](/more/glossary-of-terms)

React Native

[Visit documentation](https://reactnative.dev/docs/components-and-apis)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Reference
=========

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/versions/unversioned/index.mdx)

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/versions/unversioned/index.mdx)

---

The Expo SDK provides access to device and system functionality such as contacts, camera, gyroscope, GPS location, and so on, in the form of packages. You can install any Expo SDK package using the `npx expo install` command. For example, three different packages are installed using the following command:

Terminal

Copy

`-Â``npx expo install expo-camera expo-contacts expo-sensors`

After installing one or more packages, you can import them into your JavaScript code:

```
import { CameraView } from 'expo-camera';
import * as Contacts from 'expo-contacts';
import { Gyroscope } from 'expo-sensors';

```

This allows you to write [`Contacts.getContactsAsync()`](/versions/latest/sdk/contacts#contactsgetcontactsasynccontactquery) and read the contacts from the device, read the gyroscope sensor to detect device movement, or start the phone's camera and take photos.

All Expo SDK packages work in any React Native app
--------------------------------------------------

Expo apps are React Native apps, so all Expo SDK packages work in any React Native app with the `expo` package installed and configured. The easiest way to create a React Native app with support for Expo SDK packages is to use `create-expo-app`. However, you can also add Expo SDK support to an existing React Native app with the `npx install-expo-modules` command.

Terminal

Copy

`# Create a project named my-app`

`-Â``npx create-expo-app my-app --template bare-minimum`

[Install Expo SDK packages in existing React Native apps

Learn more about configuring projects created with `npx @react-native-community/cli@latest init` to Expo SDK packages.](/bare/installing-expo-modules)
[Use libraries

Learn how to install Expo SDK packages in your project.](/workflow/using-libraries)

Using pre-release versions
--------------------------

New Expo SDK versions are released three times each year. Between these releases, we publish pre-release versions of the `expo` package and all of the Expo SDK packages. Pre-releases are not considered stable and should only be used if you are comfortable with the risk of encountering bugs or other issues.

### Canary releases

Canary releases represent a snapshot of the state of the `main` branch at the time they are published. Canary package versions include `-canary` in the name, along with the date and commit hash, such as `51.0.0-canary-20240418-8d74597`. To install the latest canary release:

Terminal

Copy

`# Install the alpha version of expo and its related packages`

`-Â``npm install expo@canary && npx expo install --fix`

You can often use pre-release versions of individual packages with stable releases of the Expo SDK. There may occasionally be incompatibilities or other issues that arise in canary-quality releases. You may want to [silence dependency validation warnings](/more/expo-cli#configuring-dependency-validation) if you opt in to the canary package and once you have verified that it works well for your use cases.

### Beta releases

Before each Expo SDK release, we publish beta versions of the `expo` package and all of the Expo SDK packages. Beta releases are considered much more stable than canary releases, and we encourage developers to try them out on their apps and share their feedback. Beta releases use the `beta` tag on npm and follow the instructions in the related [changelog](https://expo.dev/changelog) post.

Each Expo SDK version depends on a React Native version
-------------------------------------------------------

| Expo SDK version | React Native version | React Native Web version |
| --- | --- | --- |
| 53.0.0 | 0.79 | 0.20.0 |
| 52.0.0 | 0.76 | 0.19.13 |
| 51.0.0 | 0.74 | 0.19.10 |

### Additional information

Expo SDK policy for tracking React Native releases

* Expo SDK versions are released three times each year, and each Expo SDK release targets a single React Native version. This is typically the latest stable version at the time of the release.
* The release cadence of React Native has varied over its history and it is currently on pace for six releases in 2025. While on this cadence, you can expect that there will be an Expo SDK version for every second React Native release.
* Pre-release versions of the upcoming Expo SDK will include support for the latest version of React Native quickly, usually the same day it is released. A member of the Expo SDK team works on the React Native releases team for each release, and is responsible for continuously updating the React Native version in the Expo repository, verifying compatibility, and reporting regressions back to the team at Meta.

 Why not release a new Expo SDK version immediately for every React Native release?

At Expo, we have found that releasing three major version provides a good balance of stability and innovation for developers depending on our open source tools. Expo and Meta work closely together on releases, and we will keep improving our processes to get the latest Expo and React Native features to you as quickly as possible.

What if I need a change from the latest React Native version and it's not yet in an Expo SDK release?

We work closely with the team at Meta to ensure that any urgent fixes are included in the React Native version used by the latest Expo SDK. If your issue won't be cherrypicked into an existing release because it is more niche, or it involves a breaking change, then you have two options:

1. Use [`patch-package`](https://github.com/ds300/patch-package) to pull in the fix.
2. Use a [pre-release version of the Expo SDK](/versions/latest#using-pre-release-versions). An ([example](https://expo.dev/changelog/react-native-78)).

Can I use an older version of React Native with the latest Expo SDK?

Packages in the Expo SDK are intended to support the target React Native version for that SDK. Typically, they will not support older versions of React Native, but they may. When a new version of React Native is released, the latest versions of the Expo SDK packages are typically updated to support it. However, this may take weeks or more, depending on the extent of the changes in the release.

Support for Android and iOS versions
------------------------------------

Each version of Expo SDK supports a minimum OS version of Android and iOS. For Android, the `compileSdkVersion` is defined which tells the [Gradle](https://developer.android.com/studio/build) which Android SDK version to use to compile the app. This also means that you can use the Android API features included in that SDK version and from the previous versions. For iOS, the [Xcode](https://developer.apple.com/news/upcoming-requirements/) tells the minimum Xcode SDK version to use to compile the app.

| Expo SDK version | Android version | `compileSdkVersion` | iOS version | Xcode version |
| --- | --- | --- | --- | --- |
| 53.0.0 | 7+ | 35 | 15.1+ | 16.0+ |
| 52.0.0 | 7+ | 35 | 15.1+ | 16.0+ |
| 51.0.0 | 6+ | 34 | 13.4+ | 15.4 - 16.2 |

When deciding whether to upgrade your Expo SDK version, consider both Expo's SDK version and app store submission requirements, as described in the above table. Google Play Store and Apple App Store periodically increase their minimum required OS versions and API levels, which are required for new app submissions. Expo has no control over the app store requirements, and you should check [Google](https://developer.android.com/studio/build) and [Apple](https://developer.apple.com/news/upcoming-requirements/) for the current store submission requirements.

[Next (Configuration files)

app.json / app.config.js](/versions/latest/config/app)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/versions/unversioned/index.mdx)
* Last updated on May 10, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).