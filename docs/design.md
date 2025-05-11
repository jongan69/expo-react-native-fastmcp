Expo Modules API: Design considerations - Expo Documentation

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

[Module API](/modules/module-api)[Android lifecycle listeners](/modules/android-lifecycle-listeners)[iOS AppDelegate subscribers](/modules/appdelegate-subscribers)[Autolinking](/modules/autolinking)[expo-module.config.json](/modules/module-config)[Mocking native calls](/modules/mocking)[Design considerations](/modules/design)

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

Expo Modules API: Design considerations
=======================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/modules/design.mdx)

An overview of the design considerations behind the Expo Modules API.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/modules/design.mdx)

---

The Expo team maintains a large set of libraries, and maintaining native modules over time and in a constantly changing environment can be challenging. With the Expo Modules API, we set out to build powerful tooling that would make building and maintaining these libraries easier.

### Take advantage of modern language features

After several years of maintaining over 50 native modules in the Expo SDK, we have discovered that many issues were caused by unhandled null values or incorrect types. Modern language features can help developers avoid these bugs; for example, the lack of optional types combined with the dynamism of Objective-C made it tough to catch certain classes of bugs that would have been caught by the compiler in Swift.

Another difficulty of writing React Native modules is context switching between the vastly different languages and paradigms for writing native modules on each platform. Due to the differences between these platforms, it cannot be avoided completely. We feel the need to have just one common API and documentation to simplify the development as much as possible and make it easier for a single developer to maintain a library on multiple platforms.

This is one of the reasons why the Expo Modules ecosystem was designed from the ground up to be used with modern native languages: Swift and Kotlin.

### Make it easy to pass data between runtimes

The Expo Modules API has full knowledge of the argument types the native function expects. It can pre-validate and convert the arguments for you, and dictionaries can be represented as native structs that we call [Records](/modules/module-api#records).

One big pain point we aimed to solve with the API is the validation of arguments passed from JavaScript to native functions. This is especially error-prone, time-consuming, and difficult to maintain when it comes to `NSDictionary` or `ReadableMap`, where the type of values is unknown in runtime, and each property needs to be validated separately by the developer.

Knowing the argument types, it is also possible to [automatically convert arguments](/modules/module-api#convertibles) to some platform-specific types (for example, `{ x: number, y: number }` or `[number, number]` can be translated to CoreGraphics's `CGPoint` for your convenience).

In summary, Expo Modules has powerful built-in and extensible type conversion and type safety. It supports automatic of primitive values (for example, `Bool`/`Int`/`UInt`/`Float32`/`Double`/`Pair`/`String`), complex built-in types (for example, `URL`, `CGPoint`, `UIColor`, `Data`, `java.net.URL`, `android.graphics.Color`, `kotlin.ByteArray`), records (user defined types, like a `struct`/`Object`), and enums.

### Support expressive object-oriented APIs

Keep the source of truth for the state of your native module in one place, rather than spreading it across JavaScript and native and doing the associated book-keeping yourself. We call this feature Shared Objects. For example, [`expo-sqlite` database instances are backed by Shared Objects](https://github.com/expo/expo/blob/718a9ac107231475ca4b2e6427317ade9d1e70fa/packages/expo-sqlite/src/SQLiteDatabase.ts#L421). Detailed documentation for Shared Objects is coming soon.

### Provide a safe and composable mechanism to hook into app lifecycle events

[Android lifecycle listeners](/modules/android-lifecycle-listeners) and [iOS AppDelegate subscribers](/modules/appdelegate-subscribers) are a powerful feature that allows you to hook into the lifecycle of your app, without needing to spread the code out for your module across your `MainActivity` and `AppDelegate` classes or require that users of your library do the same. This is particularly useful for smooth integration with [Continuous Native Generation](/workflow/continuous-native-generation) because it provides libraries with a mechanism to hook into app lifecycle events in a composable way â without having to be concerned about what other libraries might be doing.

### Support the New Architecture while remaining backwards compatible

React Native version 0.68 introduced the [New Architecture](https://reactnative.dev/docs/the-new-architecture/landing-page), which offers developers new capabilities for building mobile apps. It consists of the new native modules system called [Turbo Modules](https://reactnative.dev/docs/the-new-architecture/pillars-turbomodules) and the new rendering system called [Fabric](https://reactnative.dev/architecture/fabric-renderer).
Native libraries need to be adapted to take advantage of these new systems. For Fabric, it needs even more work as it doesn't provide any compatibility layer, which means that view managers written in the old way don't work with Fabric and the other way around â Fabric native components don't work with the old renderer. It basically implies that existing libraries have to provide support for both architectures for a while, increasing the technical debt.

The new architecture is mostly written in C++, so you may end up writing some C++ code for your library as well. As we all React Native developers, use high-level JavaScript on a daily basis, we are rather reluctant to write C++, which is on the opposite side of the spectrum. Moreover, including C++ code in the library has a negative impact on build times, especially on Android, and can be more difficult to debug.

We took these into account when designing the Expo Modules API with the goal in mind to make it renderer-agnostic, so that the module doesn't need to know whether the app is run on the new architecture or not, significantly reducing the cost for library developers.

[Previous (Expo Modules API - Reference)

Mocking native calls](/modules/mocking)[Next (Push notifications)

Overview](/push-notifications/overview)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/modules/design.mdx)
* Last updated on September 17, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Take advantage of modern language features](/modules/design/#take-advantage-of-modern-language-features)[Make it easy to pass data between runtimes](/modules/design/#make-it-easy-to-pass-data-between-runtimes)[Support expressive object-oriented APIs](/modules/design/#support-expressive-object-oriented-apis)[Provide a safe and composable mechanism to hook into app lifecycle events](/modules/design/#provide-a-safe-and-composable-mechanism-to-hook-into-app-lifecycle-events)[Support the New Architecture while remaining backwards compatible](/modules/design/#support-the-new-architecture-while-remaining-backwards-compatible)