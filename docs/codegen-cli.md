The Codegen CLI · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/the-new-architecture/codegen-cli)

* [Next](/docs/next/the-new-architecture/codegen-cli)* [0.79](/docs/the-new-architecture/codegen-cli)* [0.78](/docs/0.78/the-new-architecture/codegen-cli)* [0.77](/docs/0.77/the-new-architecture/codegen-cli)* [0.76](/docs/0.76/the-new-architecture/codegen-cli)* [0.75](/docs/0.75/getting-started)* [0.74](/docs/0.74/getting-started)* [0.73](/docs/0.73/getting-started)* [0.72](/docs/0.72/getting-started)* [0.71](/docs/0.71/getting-started)* [0.70](/docs/0.70/getting-started)* [All versions](/versions)

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

                  + [What is Codegen?](/docs/the-new-architecture/what-is-codegen)+ [Using Codegen](/docs/the-new-architecture/using-codegen)+ [The Codegen CLI](/docs/the-new-architecture/codegen-cli)* [Native Development](/docs/native-platform)

                    * [Android and iOS guides](/docs/headless-js-android)

                      * [Legacy Architecture](/docs/legacy/native-modules-intro)

On this page

The Codegen CLI
===============

Calling Gradle or manually calling a script might be hard to remember and it requires a lot of ceremony.

To simplify it, we created a CLI tool that can help you running those tasks: the **Codegen** cli. This command runs [@react-native/codegen](https://www.npmjs.com/package/@react-native/codegen) for your project. The following options are available:

sh

```
npx @react-native-community/cli codegen --help  
Usage: rnc-cli codegen [options]  
  
Options:  
  --verbose            Increase logging verbosity  
  --path <path>        Path to the React Native project root. (default: "/Users/MyUsername/projects/my-app")  
  --platform <string>  Target platform. Supported values: "android", "ios", "all". (default: "all")  
  --outputPath <path>  Path where generated artifacts will be output to.  
  -h, --help           display help for command  

```

Examples[​](#examples "Direct link to Examples")
------------------------------------------------

* Read `package.json` from the current working directory, generate code based on its codegenConfig.

shell

```
npx @react-native-community/cli codegen  

```

* Read `package.json` from the current working directory, generate iOS code in the location defined in the codegenConfig.

shell

```
npx @react-native-community/cli codegen --platform ios  

```

* Read `package.json` from `third-party/some-library`, generate Android code in `third-party/some-library/android/generated`.

shell

```
npx @react-native-community/cli codegen \  
    --path third-party/some-library \  
    --platform android \  
    --outputPath third-party/some-library/android/generated  

```

Including Generated Code into Libraries[​](#including-generated-code-into-libraries "Direct link to Including Generated Code into Libraries")
---------------------------------------------------------------------------------------------------------------------------------------------

The Codegen CLI is a great tool for library developers. It can be used to take a sneak-peek at the generated code to see which interfaces you need to implement.

Normally the generated code is not included in the library, and the app that uses the library is responsible for running the Codegen at build time.
This is a good setup for most cases, but Codegen also offers a mechanism to include the generated code in the library itself via the `includesGeneratedCode` property.

It's important to understand what are the implications of using `includesGeneratedCode = true`. Including the generated code comes with several benefits such as:

* No need to rely on the app to run **Codegen** for you, the generated code is always there.
* The implementation files are always consistent with the generated interfaces (this makes your library code more resilient against API changes in codegen).
* No need to include two sets of files to support both architectures on Android. You can only keep the New Architecture one, and it is guaranteed to be backwards compatible.
* Since all native code is there, it is possible to ship the native part of the library as a prebuild.

On the other hand, you also need to be aware of one drawback:

* The generated code will use the React Native version defined inside your library. So if your library is shipping with React Native 0.76, the generated code will be based on that version. This could mean that the generated code is not compatible with apps using **previous** React Native version used by the app (e.g. an App running on React Native 0.75).

Enabling `includesGeneratedCode`[​](#enabling-includesgeneratedcode "Direct link to enabling-includesgeneratedcode")
--------------------------------------------------------------------------------------------------------------------

To enable this setup:

* Add the `includesGeneratedCode` property into your library's `codegenConfig` field in the `package.json` file. Set its value to `true`.
* Run **Codegen** locally with the codegen CLI.
* Update your `package.json` to include the generated code.
* Update your `podspec` to include the generated code.
* Update your `build.Gradle` file to include the generated code.
* Update `cmakeListsPath` in `react-native.config.js` so that Gradle doesn't look for CMakeLists file in the build directory but instead in your outputDir.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/the-new-architecture/codegen-cli.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/the-new-architecture/codegen-cli.md)

Last updated on **Apr 14, 2025**

[Previous

Using Codegen](/docs/the-new-architecture/using-codegen)[Next

Introduction](/docs/native-platform)

* [Examples](#examples)* [Including Generated Code into Libraries](#including-generated-code-into-libraries)* [Enabling `includesGeneratedCode`](#enabling-includesgeneratedcode)

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