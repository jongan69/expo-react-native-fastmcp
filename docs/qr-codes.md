qr.expo.dev - Expo Documentation

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

qr.expo.dev
===========

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/more/qr-codes.mdx)

Reference for the QR code generator at qr.expo.dev.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/more/qr-codes.mdx)

---

qr.expo.dev is a cloud function that generates Expo-branded QR codes. This function creates QR codes for [EAS Update](/eas-update/introduction), which are used to preview updates in [development builds](/develop/development-builds/introduction) and Expo Go.

For example, if you and your team have a development build, and you'd like to load the latest update on a specific build's channel, you could go to the following endpoint to generate a QR code:

```
https://qr.expo.dev/eas-update?projectId=your-project-id&runtimeVersion=your-runtime-version&channel=your-channel

```

Which would produce the following QR code SVG:

![QR code generated by qr.expo.dev](https://qr.expo.dev/eas-update?slug=your-slug&projectId=your-project-id&runtimeVersion=your-runtime-version&channel=your-channel)

This QR code represents the following URL:

```
exp+your-slug://expo-development-client/?url=https://u.expo.dev/your-project-id?runtime-version=your-runtime-version&channel-name=your-channel

```

This URL will deep link into a development build and instruct it to fetch the latest update on the specified channel.

> If sharing the URL is more convenient, you can request the URL directly by adding `format=url` to the query parameters.

General
-------

The following parameters apply to the `/eas-update` endpoint.

### Base query parameters

The following base query parameters can be included with any request to `/eas-update`.

| Param | Required | Default | Description |
| --- | --- | --- | --- |
| `slug` | No | exp | Use [`slug`](/versions/latest/config/app#slug) from [app config](/workflow/configuration) to target a development build. Otherwise use "exp" to target Expo Go. |
| `appScheme` (deprecated) | No | exp | Replaced by `slug`. Use `slug` instead. |
| `host` | No | u.expo.dev | The hostname of the server that handles update requests. |
| `format` | No | svg | Endpoints respond with SVGs by default. To receive a plain text URL, use `url`. |

### Update by device traits

Preview and production builds make requests to the EAS Update service with `runtimeVersion` and `channel` properties. You can emulate this behavior with the following query parameters:

| Param | Required | Description |
| --- | --- | --- |
| `projectId` | Yes | The ID of the project |
| `runtimeVersion` | Yes | The [runtime version](/eas-update/runtime-versions) of the build |
| `channel` | Yes | The channel name of the build |

#### Example

```
https://qr.expo.dev/eas-update?projectId=your-project-id&runtimeVersion=your-runtime-version&channel=your-channel

```

### Update by ID

You can create a QR code for a specific update given its platform-specific ID.

| Param | Required | Description |
| --- | --- | --- |
| `updateId` | Yes | The ID of the update |

#### Example

```
https://qr.expo.dev/eas-update?updateId=your-update-id

```

### Update by group ID

You can create a QR code for an update group given the update's group ID.

| Param | Required | Description |
| --- | --- | --- |
| `projectId` | Yes | The ID of the project |
| `groupId` | Yes | The ID of the update group |

#### Example

```
https://qr.expo.dev/eas-update?projectId=your-project-id&groupId=your-update-id

```

### Update by branch ID

You can create a QR code with a branch's ID, which will return the latest update available on that branch.

| Param | Required | Description |
| --- | --- | --- |
| `projectId` | Yes | The ID of the project |
| `branchId` | Yes | The ID of the branch |

#### Example

```
https://qr.expo.dev/eas-update?projectId=your-project-id&branchId=your-branch-id

```

### Update by channel ID

You can create a QR code with a channel's ID, which will return the latest update available on the branch or branches that are mapped to that channel.

| Param | Required | Description |
| --- | --- | --- |
| `projectId` | Yes | The ID of the project |
| `channelId` | Yes | The ID of the channel |

#### Example

```
https://qr.expo.dev/eas-update?projectId=your-project-id&channelId=your-channel-id

```

[Previous (More)

create-expo-app](/more/create-expo)[Next (More)

Glossary of terms](/more/glossary-of-terms)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/more/qr-codes.mdx)
* Last updated on June 16, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[General](/more/qr-codes/#general)[Base query parameters](/more/qr-codes/#base-query-parameters)[Update by device traits](/more/qr-codes/#update-by-device-traits)[Update by ID](/more/qr-codes/#update-by-id)[Update by group ID](/more/qr-codes/#update-by-group-id)[Update by branch ID](/more/qr-codes/#update-by-branch-id)[Update by channel ID](/more/qr-codes/#update-by-channel-id)