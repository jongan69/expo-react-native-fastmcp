Using Expo SDK, React Native, and third-party libraries - Expo Documentation

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

Using Expo SDK, React Native, and third-party libraries
=======================================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/workflow/using-libraries.mdx)

Learn how to use Expo SDK, React Native libraries, and other third-party npm packages in your project.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/workflow/using-libraries.mdx)

---

Every app is inevitably going to use a third-party library, so it's important to understand how to determine whether a library is compatible with your project.

React Native core libraries
---------------------------

React Native provides a set of built-in primitives that most developers will need in their apps. These include components such as `<ActivityIndicator>`, `<TextInput>`, `<Text>`, `<ScrollView>`, and `<View>`. These are listed at [Core Components and APIs](https://reactnative.dev/docs/components-and-apis) in React Native documentation. You can also view the [React Native version that corresponds to your Expo SDK version](/versions/latest).

To use a React Native component or API in your project, import it from the `react-native` package in your code:

Example

Copy

Open in Snack

```
import { Text, View } from 'react-native';

export default function App() {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Hello, world!</Text>
    </View>
  );
}

```

Expo SDK libraries
------------------

The Expo SDK picks up where the React Native core libraries end. It provides access to a lot of device and system functionality such as audio, barcode scanning, camera, calendar, contacts, video, and so on. It also adds other powerful libraries like updates, maps, OAuth authentication tools, and more. For more information, see how we decide [what goes into the Expo SDK](https://expo.fyi/whats-in-the-sdk).

To use a library from the Expo SDK, find the one you are looking for in the [API reference](/versions/latest) or use the documentation search.

Are you using this library in an existing React Native app?

If you initialized your app using `npx @react-native-community/cli@latest init` and you don't have the `expo` package installed in it yet, see the [installing Expo modules guide](/bare/installing-expo-modules) for more information.

You will see the platform compatibility tags at the top of each API reference. It tells you which platforms and environments the library is compatible with. For example, the platform tags for the [`expo-device`](/versions/latest/sdk/device) library look like the following:

![Platform compatibility tags for expo-device library on its API reference.](/static/images/guides/platform-tags.png)

After the platform compatibility table, there is a library's description and a section with instructions on installing the library. For example:

Terminal

Copy

`-Â``npx expo install expo-device`

The `npx expo install` command picks a library version compatible with your project and then uses your JavaScript package manager (such as npm) to install it.

Next, a typical API reference includes:

* Config plugin usage information if the library requires a config plugin.
* A code example that shows how to use the library.
* API section that lists how to import the library, followed by a list of hooks, props, types, methods, and classes that the library provides.

> Note: If you use TypeScript, you can see the information included in the API section in your TypeScript-compatible code editor (such as VS Code) with auto-completion.

Third-party libraries
---------------------

### Finding a third-party library

[React Native Directory](https://reactnative.directory) is a searchable database of libraries built specifically for React Native. If the library that you are looking for is not provided by React Native or the Expo SDK then this is the best place to look first when trying to find a library for your app.

After the React Native Directory, the [npm registry](https://www.npmjs.com/) is the next best place. The npm registry is the definitive source for JavaScript libraries, but the libraries that it lists may not all be compatible with React Native. React Native is one of many JavaScript programming environments, including Node.js, web browsers, Electron, and more, and npm includes libraries that work for all of these environments. Any library that is compatible with React Native is compatible with the Expo project when you create a [development build](/workflow/overview#development-builds). However, it may not be compatible with the [Expo Go](https://expo.dev/go) app.

### Determining third-party library compatibility

Use Expo [development builds](/workflow/overview#development-builds) for building production-quality apps. It includes all of the native code that your project needs to run. This is a great way to test your app before you publish it to the App Store or Google Play. You can also include libraries that require native projects (android and ios directories) configuration.

The Expo Go app is an optional stepping stone towards development builds. You can use it to quickly test your app while you are developing it, but it does not include all of the native code required to support every library. You can check React Native Directory to find a library compatible with Expo Go by visiting the website and verifying that it has a "âï¸ Expo Go" tag. You can also enable the [filter by Expo Go](https://reactnative.directory/?expoGo=true).

To determine if a new dependency changes native project directories, you can check the following:

* Does the library includes android or ios directories?
* Does the library's README mention linking?
* Does the library requires you to change android/app/src/main/AndroidManifest.xml or ios/Podfile or ios/Info.plist to change the project configuration?
* Does the library have a [config plugin](/config-plugins/introduction)?

If you answered yes to any of these questions, then you should [create a development build](/develop/development-builds/introduction) to use the library in your project.

Not listed on the directory? You can find the project on GitHub. A simple way to do this is with `npx npm-home --github <package-name>`. For example, to open the GitHub page for `react-native-localize`, run:

Terminal

Copy

`-Â``npx npm-home --github react-native-localize`

> If you want some help determining library compatibility, [create an issue on the React Native Directory repository](https://github.com/react-native-community/directory/issues/new/choose) and let us know. This will not just help you, it will also help other developers have an easy answer in the future!

### Installing a third-party library

> We recommend always using `npx expo install` instead of `npm install` or `yarn add` directly because it allows [Expo CLI](/more/expo-cli) to pick a compatible version of a library when possible and also warn you about known incompatibilities.

Once you have determined if the library is compatible with React Native, use [Expo CLI](/more/expo-cli) to install the package:

Terminal

Copy

`-Â``npx expo install @react-navigation/native`

Be sure to follow the project website or README for any additional configuration and usage instructions. You can get to the README quickly using this command:

Terminal

Copy

`-Â``npx npm-home @react-navigation/native`

If the module needs additional native configuration, you can do so using [config plugins](/config-plugins/introduction). Some packages require a config plugin but they don't have one yet, you can refer to the list of [out-of-tree config plugins](https://github.com/expo/config-plugins/).

Are you using this library in an existing React Native app?

If your project does not support [Expo Prebuild](/workflow/prebuild) then you won't be able to use [config plugins](/config-plugins/introduction). You can either [adopt Expo Prebuild](/guides/adopting-prebuild) or set up and configure each library manually by following any additional setup guides from the respective module's website or README.

If the module is not supported in [Expo Go](https://expo.dev/go), you can create a [development build](/develop/development-builds/introduction):

[Add custom native code

Learn how to add custom native code to your Expo project.](/workflow/customizing)

### Excluding a third-party library from version checks

If you have a specific version of a third-party library installed and want it to be excluded from version checks performed by `npx expo install`, `npx expo-doctor`, or `npx expo start`, use the [`expo.install.exclude`](/versions/latest/config/package-json#exclude) property in the package.json file.

[Previous (Development process)

Continuous Native Generation](/workflow/continuous-native-generation)[Next (Development process)

Privacy manifests](/guides/apple-privacy)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/workflow/using-libraries.mdx)
* Last updated on December 18, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[React Native core libraries](/workflow/using-libraries/#react-native-core-libraries)[Expo SDK libraries](/workflow/using-libraries/#expo-sdk-libraries)[Third-party libraries](/workflow/using-libraries/#third-party-libraries)[Finding a third-party library](/workflow/using-libraries/#finding-a-third-party-library)[Determining third-party library compatibility](/workflow/using-libraries/#determining-third-party-library-compatibility)[Installing a third-party library](/workflow/using-libraries/#installing-a-third-party-library)[Excluding a third-party library from version checks](/workflow/using-libraries/#excluding-a-third-party-library-from-version-checks)