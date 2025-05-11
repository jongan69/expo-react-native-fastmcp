Expo Structured Field Values - Expo Documentation

[Docs](/)

[Blog](https://expo.dev/blog)[Changelog](https://expo.dev/changelog)[Star Us on GitHub](https://github.com/expo/expo)

Search

[Home](/)[Guides](/guides/overview)[EAS](/eas)[Reference](/versions/latest)[Learn](/tutorial/overview)

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

Expo Structured Field Values
============================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/technical-specs/expo-sfv-0.mdx)

Version 0

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/technical-specs/expo-sfv-0.mdx)

---

Structured Field Values for HTTP, [IETF RFC 8941](https://tools.ietf.org/html/rfc8941), is a proposal to formalize header syntax and facilitate nested data.

Since it is still a work in progress, Expo maintains a custom version that only implements the following subset of the protocol defined in [IETF RFC 8941](https://tools.ietf.org/html/rfc8941):

* All key values
* String, integer, and decimal items
* Dictionaries

[Previous (Technical specs)

Expo Updates v1](/technical-specs/expo-updates-1)[Next (More)

Expo CLI](/more/expo-cli)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/technical-specs/expo-sfv-0.mdx)
* Last updated on May 24, 2021

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page