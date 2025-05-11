create-expo-app - Expo Documentation

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

create-expo-app
===============

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/more/create-expo.mdx)

A command-line tool to create a new Expo and React Native project.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/more/create-expo.mdx)

---

`create-expo-app` is a command-line tool to create and set up a new Expo and React Native project. This tool simplifies the initialization process by providing various templates to get started quickly without the need for manual configuration.

Create a new project
--------------------

To create a new project, run the following command:

npm

Yarn

pnpm

Bun

Terminal

Copy

`-Â``npx create-expo-app@latest`

Terminal

Copy

`-Â``yarn create expo-app`

Terminal

Copy

`-Â``pnpm create expo-app`

Terminal

Copy

`-Â``bun create expo`

Running the above command will prompt you to enter the app name of your project. This app name is also used in the app config's [`name`](/versions/latest/config/app#name) property.

Terminal

Copy

`What is your app named? my-app`

Options
-------

Uses the following options to customize the command behavior.

### `--yes`

Uses the default options to create a new project.

### `--no-install`

Skips installing npm dependencies or CocoaPods.

### `--template`

Running `create-expo-app` with a [Node Package Manager](/more/create-expo#node-package-managers-support) initializes and sets up a new Expo project using the default template.

You can use the `--template` option to select one of the following templates or pass it as an argument to the option. For example, `--template default`.

| Template | Description |
| --- | --- |
| [`default`](https://github.com/expo/expo/tree/main/templates/expo-template-default) | Default template. Designed to build multi-screen apps. Includes recommended tools such as Expo CLI, Expo Router library and TypeScript configuration enabled. Suitable for most apps. |
| [`blank`](https://github.com/expo/expo/tree/main/templates/expo-template-blank) | Installs minimum required npm dependencies without configuring navigation. |
| [`blank-typescript`](https://github.com/expo/expo/tree/main/templates/expo-template-blank-typescript) | A Blank template with TypeScript enabled. |
| [`tabs`](https://github.com/expo/expo/tree/main/templates/expo-template-tabs) | Installs and configures file-based routing with Expo Router and TypeScript enabled. |
| [`bare-minimum`](https://github.com/expo/expo/tree/main/templates/expo-template-bare-minimum) | A Blank template with native directories (android and ios) generated. Runs [`npx expo prebuild`](/workflow/prebuild) during the setup. |

### `--example`

Use this option to initialize a project using an example from [expo/examples](https://github.com/expo/examples).

For example, running `npx create-expo-app --example with-router` will set up a project with Expo Router library.

### `--version`

Prints the version number and exits.

### `--help`

Prints the list of available options and exits.

Node Package Managers support
-----------------------------

Creating a new project with `create-expo-app` also handles setting up additional configuration needed for a specific Node Package Manager.

If you are migrating from one package manager to another, you've to manually carry out the additional configuration in your project. If you are using [EAS](/eas), you also have to configure your project for any additional required steps manually.

All the additional steps for each package manager are listed below.

### npm

#### Local installation

npm is installed as part of Node.js installation. See [Node.js documentation](https://nodejs.org/en/download/package-manager) for installation instructions.

#### EAS installation

Supported by default if the project directory contains package-lock.json.

### Yarn 1 (Classic)

#### Local installation

Yarn 1 (Classic) is usually installed as a global dependency of npm. See [Yarn 1 documentation](https://classic.yarnpkg.com/en/docs/getting-started) for installation instructions.

#### EAS installation

Supported by default if the project directory contains yarn.lock.

### Yarn 2+ (Modern)

#### Local installation

See [Yarn documentation](https://yarnpkg.com/getting-started/install) for installation instructions.

Yarn 2+ handles package management differently than Yarn 1. One of the core changes in Yarn 2+ is the [Plug'n'Play (PnP)](https://yarnpkg.com/features/pnp) node linking model that does not work with React Native.

By default, a project created with `create-expo-app` and Yarn 2+ uses [`nodeLinker`](https://yarnpkg.com/features/linkers#nodelinker-node-modules) with its value set to `node-modules` to install dependencies.

.yarnrc.yml

Copy

```
nodeLinker: node-modules

```

#### EAS installation

Yarn Modern on EAS requires adding [`eas-build-pre-install` hook](/build-reference/npm-hooks). In your project's package.json, add the following configuration:

package.json

Copy

```
{
  "scripts": {
    "eas-build-pre-install": "corepack enable && yarn set version 4"
  }
}

```

### pnpm

#### Local installation

Requires installing Node.js. See [pnpm documentation](https://pnpm.io/installation) for installation instructions.

By default, a project created with `create-expo-app` and pnpm uses [`node-linker`](https://pnpm.io/npmrc#node-linker) with its value set to `hoisted` to install dependencies.

.npmrc

Copy

```
node-linker=hoisted

```

#### EAS installation

Supported by default if the project directory contains pnpm-lock.yaml.

### Bun

See [Bun](/guides/using-bun) guide for details on creating a new Expo project with `bun`, migration from another package manager, and usage with EAS.

[Previous (More)

Expo CLI](/more/expo-cli)[Next (More)

qr.expo.dev](/more/qr-codes)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/more/create-expo.mdx)
* Last updated on January 15, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Create a new project](/more/create-expo/#create-a-new-project)[Options](/more/create-expo/#options)[--yes](/more/create-expo/#--yes)[--no-install](/more/create-expo/#--no-install)[--template](/more/create-expo/#--template)[--example](/more/create-expo/#--example)[--version](/more/create-expo/#--version)[--help](/more/create-expo/#--help)[Node Package Managers support](/more/create-expo/#node-package-managers-support)[npm](/more/create-expo/#npm)[Local installation](/more/create-expo/#local-installation)[EAS installation](/more/create-expo/#eas-installation)[Yarn 1 (Classic)](/more/create-expo/#yarn-1-classic)[Local installation](/more/create-expo/#local-installation-1)[EAS installation](/more/create-expo/#eas-installation-1)[Yarn 2+ (Modern)](/more/create-expo/#yarn-2-modern)[Local installation](/more/create-expo/#local-installation-2)[EAS installation](/more/create-expo/#eas-installation-2)[pnpm](/more/create-expo/#pnpm)[Local installation](/more/create-expo/#local-installation-3)[EAS installation](/more/create-expo/#eas-installation-3)[Bun](/more/create-expo/#bun)