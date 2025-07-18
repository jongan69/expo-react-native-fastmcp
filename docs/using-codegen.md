Using Codegen · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/the-new-architecture/using-codegen)

* [Next](/docs/next/the-new-architecture/using-codegen)* [0.79](/docs/the-new-architecture/using-codegen)* [0.78](/docs/0.78/the-new-architecture/using-codegen)* [0.77](/docs/0.77/the-new-architecture/using-codegen)* [0.76](/docs/0.76/the-new-architecture/using-codegen)* [0.75](/docs/0.75/getting-started)* [0.74](/docs/0.74/getting-started)* [0.73](/docs/0.73/getting-started)* [0.72](/docs/0.72/getting-started)* [0.71](/docs/0.71/getting-started)* [0.70](/docs/0.70/getting-started)* [All versions](/versions)

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

Using Codegen
=============

This guide teaches how to:

* Configure **Codegen**.
* Invoke it manually for each platform.

It also describes the generated code.

Prerequisites[​](#prerequisites "Direct link to Prerequisites")
---------------------------------------------------------------

You always need a React Native app to generate the code properly, even when invoking the **Codegen** manually.

The **Codegen** process is tightly coupled with the build of the app, and the scripts are located in the `react-native` NPM package.

For the sake of this guide, create a project using the React Native CLI as follows:

bash

```
npx @react-native-community/cli@latest init SampleApp --version 0.76.0  

```

**Codegen** is used to generate the glue-code for your custom modules or components. See the guides for Turbo Native Modules and Fabric Native Components for more details on how to create them.

Configuring **Codegen**[​](#configuring-codegen "Direct link to configuring-codegen")
-------------------------------------------------------------------------------------

**Codegen** can be configured in your app by modifying the `package.json` file. **Codegen** is controlled by a custom field called `codegenConfig`.

package.json

```
  "codegenConfig": {  
    "name": "<SpecName>",  
    "type": "<types>",  
    "jsSrcsDir": "<source_dir>",  
    "android": {  
      "javaPackageName": "<java.package.name>"  
    },  
    "ios": {  
      "modulesConformingToProtocol": {  
        "RCTImageURLLoader": [  
          "<iOS-class-conforming-to-RCTImageURLLoader>",  
          // example from react-native-camera-roll: https://github.com/react-native-cameraroll/react-native-cameraroll/blob/8a6d1b4279c76e5682a4b443e7a4e111e774ec0a/package.json#L118-L127  
          // "RNCPHAssetLoader",  
        ],  
        "RCTURLRequestHandler": [  
          "<iOS-class-conforming-to-RCTURLRequestHandler>",  
          // example from react-native-camera-roll: https://github.com/react-native-cameraroll/react-native-cameraroll/blob/8a6d1b4279c76e5682a4b443e7a4e111e774ec0a/package.json#L118-L127  
          // "RNCPHAssetUploader",  
        ],  
        "RCTImageDataDecoder": [  
          "<iOS-class-conforming-to-RCTImageDataDecoder>",  
          // we don't have a good example for this, but it works in the same way. Pass the name of the class that implements the RCTImageDataDecoder. It must be a Native Module.  
        ]  
      },  
      "componentProvider": {  
        "<componentName>": "<iOS-class-implementing-the-component>"  
      },  
      "modulesProvider": {  
        "<moduleName>": "<iOS-class-implementing-the-RCTModuleProvider-protocol>"  
      }  
    }  
  },  

```

You can add this snippet to your app and customize the various fields:

* `name:` This is the name that will be used to create files containing your specs. As a convention, It should have the suffix `Spec`, but this is not mandatory.
* `type`: the type of code we need to generate. Allowed values are `modules`, `components`, `all`.
  + `modules:` use this value if you only need to generate code for Turbo Native Modules.
  + `components:` use this value if you only need to generate code for Native Fabric Components.
  + `all`: use this value if you have a mixture of components and modules.
* `jsSrcsDir`: this is the root folder where all your specs live.
* `android.javaPackageName`: this is an Android specific setting to let **Codegen** generate the files in a custom package.
* `ios`: the `ios` field is an object that can be used by app developers and library maintainers to provide some advanced functionalities. All the following fields are **optional**.
  + `ios.modulesConformingToProtocol`: React Native offers some protocols that native modules can implement to customize some behaviors. These fields allow you to define the list of module that conforms to those protocols. These modules will be injected in the React Native runtime when the app starts.
    - `ios.modulesConformingToProtocol.RCTImageURLLoader`: list of iOS native module that implements the [`RCTImageURLLoader` protocol](https://github.com/facebook/react-native/blob/00d5caee9921b6c10be8f7d5b3903c6afe8dbefa/packages/react-native/Libraries/Image/RCTImageURLLoader.h#L26-L81). You need to pass the class names of iOS classes that implements the `RCTImageURLLoader`. They must be Native Modules.
    - `ios.modulesConformingToProtocol.RCTURLRequestHandler`: list of iOS native module that implements the [`RCTURLRequestHandler` protocol](https://github.com/facebook/react-native/blob/00d5caee9921b6c10be8f7d5b3903c6afe8dbefa/packages/react-native/React/Base/RCTURLRequestHandler.h#L11-L52). You need to pass the class names of iOS classes that implements the `RCTURLRequestHandler`. They must be Native Modules.
    - `ios.modulesConformingToProtocol.RCTImageDataDecoder`: list of iOS native module that implements the [`RCTImageDataDecoder` protocol](https://github.com/facebook/react-native/blob/00d5caee9921b6c10be8f7d5b3903c6afe8dbefa/packages/react-native/Libraries/Image/RCTImageDataDecoder.h#L15-L53). You need to pass the class names of iOS classes that implements the `RCTImageDataDecoder`. They must be Native Modules.
  + `ios.componentProvider`: this field is a map used to generate the association between a custom JS React component and the native class that implements it. The key of the map is the JS name of the component (for example `TextInput`), and the value is the iOS class that implements the component (for example `RCTTextInput`).
  + `ios.modulesProvider`: this field is a map used to generate the association between a custom JS Native Module and the native class that can provide it. The key of the map is the JS name of the module (for example `NativeLocalStorage`), and the value is the iOS class that implements the [`RCTModuleProvider` protocol](https://github.com/facebook/react-native/blob/0.79-stable/packages/react-native/ReactCommon/react/nativemodule/core/platform/ios/ReactCommon/RCTTurboModule.h#L179-L190). For Objective-C modules, the class implementing the [`RCTTurboModule` protocol](https://github.com/facebook/react-native/blob/0.79-stable/packages/react-native/ReactCommon/react/nativemodule/core/platform/ios/ReactCommon/RCTTurboModule.h#L192-L200) is also implementing the `RCTModuleProvider` protocol. For more information, looks at the [Cross-Platform Native Modules (C++) guide](/docs/next/the-new-architecture/pure-cxx-modules).

When **Codegen** runs, it searches among all the dependencies of the app, looking for JS files that respects some specific conventions, and it generates the required code:

* Turbo Native Modules require that the spec files are prefixed with `Native`. For example, `NativeLocalStorage.ts` is a valid name for a spec file.
* Native Fabric Components require that the spec files are suffixed with `NativeComponent`. For example, `WebViewNativeComponent.ts` is a valid name for a spec file.

Running **Codegen**[​](#running-codegen "Direct link to running-codegen")
-------------------------------------------------------------------------

The rest of this guide assumes that you have a Native Turbo Module, a Native Fabric Component or both already set up in your project. We also assume that you have valid specification files in the `jsSrcsDir` specified in the `package.json`.

### Android[​](#android "Direct link to Android")

**Codegen** for Android is integrated with the React Native Gradle Plugin (RNGP). The RNGP contains a task that can be invoked that reads the configurations defined in the `package.json` file and execute **Codegen**. To run the gradle task, first navigate inside the `android` folder of your project. Then run:

bash

```
./gradlew generateCodegenArtifactsFromSchema  

```

This task invokes the `generateCodegenArtifactsFromSchema` command on all the imported projects of the app (the app and all the node modules which are linked to it). It generates the code in the corresponding `node_modules/<dependency>` folder. For example, if you have a Fabric Native Component whose Node module is called `my-fabric-component`, the generated code is located in the `SampleApp/node_modules/my-fabric-component/android/build/generated/source/codegen` path. For the app, the code is generated in the `android/app/build/generated/source/codegen` folder.

#### The Generated Code[​](#the-generated-code "Direct link to The Generated Code")

After running the gradle command above, you will find the codegen code in the `SampleApp/android/app/build` folder. The structure will look like this:

```
build  
└── generated  
    └── source  
        └── codegen  
            ├── java  
            │   └── com  
            │       ├── facebook  
            │       │   └── react  
            │       │       └── viewmanagers  
            │       │           ├── <nativeComponent>ManagerDelegate.java  
            │       │           └── <nativeComponent>ManagerInterface.java  
            │       └── sampleapp  
            │           └── NativeLocalStorageSpec.java  
            ├── jni  
            │   ├── <codegenConfig.name>-generated.cpp  
            │   ├── <codegenConfig.name>.h  
            │   ├── CMakeLists.txt  
            │   └── react  
            │       └── renderer  
            │           └── components  
            │               └── <codegenConfig.name>  
            │                   ├── <codegenConfig.name>JSI-generated.cpp  
            │                   ├── <codegenConfig.name>.h  
            │                   ├── ComponentDescriptors.cpp  
            │                   ├── ComponentDescriptors.h  
            │                   ├── EventEmitters.cpp  
            │                   ├── EventEmitters.h  
            │                   ├── Props.cpp  
            │                   ├── Props.h  
            │                   ├── ShadowNodes.cpp  
            │                   ├── ShadowNodes.h  
            │                   ├── States.cpp  
            │                   └── States.h  
            └── schema.json  

```

The generated code is split in two folders:

* `java` which contains the platform specific code
* `jni` which contains the C++ code required to let JS and Java interact correctly.

In the `java` folder, you can find the Fabric Native component generated code in the `com/facebook/viewmanagers` subfolder.

* the `<nativeComponent>ManagerDelegate.java` contains the methods that the `ViewManager` can call on the custom Native Component
* the `<nativeComponent>ManagerInterface.java` contains the interface of the `ViewManager`.

In the folder whose name was set up in the `codegenConfig.android.javaPackageName`, instead, you can find the abstract class that a Turbo Native Module has to implement to carry out its tasks.

In the `jni` folder, finally, there is all the boilerplate code to connect JS to Android.

* `<codegenConfig.name>.h` this contains the interface of your custom C++ Turbo Native Modules.
* `<codegenConfig.name>-generated.cpp` this contains the glue code of your custom C++ Turbo Native Modules.
* `react/renderer/components/<codegenConfig.name>`: this folder contains all the glue-code required by your custom component.

This structure has been generated by using the value `all` for the `codegenConfig.type` field. If you use the value `modules`, expect to see no `react/renderer/components/` folder. If you use the value `components`, expect not to see any of the other files.

### iOS[​](#ios "Direct link to iOS")

**Codegen** for iOS relies on some Node scripts that are invoked during the build process. The scripts are located in the `SampleApp/node_modules/react-native/scripts/` folder.

The main script is the `generate-codegen-artifacts.js` script. To invoke the script, you can run this command from the root folder of your app:

bash

```
node node_modules/react-native/scripts/generate-codegen-artifacts.js  
  
Usage: generate-codegen-artifacts.js -p [path to app] -t [target platform] -o [output path]  
  
Options:  
      --help            Show help                                      [boolean]  
      --version         Show version number                            [boolean]  
  -p, --path            Path to the React Native project root.        [required]  
  -t, --targetPlatform  Target platform. Supported values: "android", "ios",  
                        "all".                                        [required]  
  -o, --outputPath      Path where generated artifacts will be output to.  

```

where:

* `--path` is the path to the root folder of your app.
* `--outputPath` is the destination where **Codegen** will write the generated files.
* `--targetPlatform` is the platform you'd like to generate the code for.

#### The Generated Code[​](#the-generated-code-1 "Direct link to The Generated Code")

Running the script with these arguments:

shell

```
node node_modules/react-native/scripts/generate-codegen-artifacts.js \  
    --path . \  
    --outputPath ios/ \  
    --targetPlatform ios  

```

Will generate these files in the `ios/build` folder:

```
build  
└── generated  
    └── ios  
        ├── <codegenConfig.name>  
        │   ├── <codegenConfig.name>-generated.mm  
        │   └── <codegenConfig.name>.h  
        ├── <codegenConfig.name>JSI-generated.cpp  
        ├── <codegenConfig.name>JSI.h  
        ├── FBReactNativeSpec  
        │   ├── FBReactNativeSpec-generated.mm  
        │   └── FBReactNativeSpec.h  
        ├── FBReactNativeSpecJSI-generated.cpp  
        ├── FBReactNativeSpecJSI.h  
        ├── RCTModulesConformingToProtocolsProvider.h  
        ├── RCTModulesConformingToProtocolsProvider.mm  
        └── react  
            └── renderer  
                └── components  
                    └── <codegenConfig.name>  
                        ├── ComponentDescriptors.cpp  
                        ├── ComponentDescriptors.h  
                        ├── EventEmitters.cpp  
                        ├── EventEmitters.h  
                        ├── Props.cpp  
                        ├── Props.h  
                        ├── RCTComponentViewHelpers.h  
                        ├── ShadowNodes.cpp  
                        ├── ShadowNodes.h  
                        ├── States.cpp  
                        └── States.h  

```

Part of these generated files are used by React Native in the Core. Then there is a set of files which contains the same name you specified in the package.json `codegenConfig.name` field.

* `<codegenConfig.name>/<codegenConfig.name>.h`: this contains the interface of your custom iOS Turbo Native Modules.
* `<codegenConfig.name>/<codegenConfig.name>-generated.mm`: this contains the glue code of your custom iOS Turbo Native Modules.
* `<codegenConfig.name>JSI.h`: this contains the interface of your custom C++ Turbo Native Modules.
* `<codegenConfig.name>JSI-generated.h`: this contains the glue code of your custom C++ Turbo Native Modules.
* `react/renderer/components/<codegenConfig.name>`: this folder contains all the glue-code required by your custom component.

This structure has been generated by using the value `all` for the `codegenConfig.type` field. If you use the value `modules`, expect to see no `react/renderer/components/` folder. If you use the value `components`, expect not to see any of the other files.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/the-new-architecture/using-codegen.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/the-new-architecture/using-codegen.md)

Last updated on **Apr 14, 2025**

[Previous

What is Codegen?](/docs/the-new-architecture/what-is-codegen)[Next

The Codegen CLI](/docs/the-new-architecture/codegen-cli)

* [Prerequisites](#prerequisites)* [Configuring **Codegen**](#configuring-codegen)* [Running **Codegen**](#running-codegen)
      + [Android](#android)+ [iOS](#ios)

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