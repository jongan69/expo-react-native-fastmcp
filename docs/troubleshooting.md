Troubleshooting · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/troubleshooting)

* [Next](/docs/next/troubleshooting)* [0.79](/docs/troubleshooting)* [0.78](/docs/0.78/troubleshooting)* [0.77](/docs/0.77/troubleshooting)* [0.76](/docs/0.76/troubleshooting)* [0.75](/docs/0.75/troubleshooting)* [0.74](/docs/0.74/troubleshooting)* [0.73](/docs/0.73/troubleshooting)* [0.72](/docs/0.72/troubleshooting)* [0.71](/docs/0.71/troubleshooting)* [0.70](/docs/0.70/troubleshooting)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [The Basics](/docs/getting-started)

  + [Introduction](/docs/getting-started)+ [Core Components and Native Components](/docs/intro-react-native-components)+ [React Fundamentals](/docs/intro-react)+ [Handling Text Input](/docs/handling-text-input)+ [Using a ScrollView](/docs/using-a-scrollview)+ [Using List Views](/docs/using-a-listview)+ [Troubleshooting](/docs/troubleshooting)+ [Platform-Specific Code](/docs/platform-specific-code)+ [More Resources](/docs/more-resources)* [Environment setup](/docs/environment-setup)

    * [Workflow](/docs/running-on-device)

      * [UI & Interaction](/docs/style)

        * [Debugging](/docs/debugging)

          * [Testing](/docs/testing-overview)

            * [Performance](/docs/performance)

              * [JavaScript Runtime](/docs/javascript-environment)

                * [Codegen](/docs/the-new-architecture/what-is-codegen)

                  * [Native Development](/docs/native-platform)

                    * [Android and iOS guides](/docs/headless-js-android)

                      * [Legacy Architecture](/docs/legacy/native-modules-intro)

On this page

Troubleshooting
===============

These are some common issues you may run into while setting up React Native. If you encounter something that is not listed here, try [searching for the issue in GitHub](https://github.com/facebook/react-native/issues/).

### Port already in use[​](#port-already-in-use "Direct link to Port already in use")

The [Metro bundler](https://metrobundler.dev/) runs on port 8081. If another process is already using that port, you can either terminate that process, or change the port that the bundler uses.

#### Terminating a process on port 8081[​](#terminating-a-process-on-port-8081 "Direct link to Terminating a process on port 8081")

Run the following command to find the id for the process that is listening on port 8081:

shell

```
sudo lsof -i :8081  

```

Then run the following to terminate the process:

shell

```
kill -9 <PID>  

```

On Windows you can find the process using port 8081 using [Resource Monitor](https://stackoverflow.com/questions/48198/how-can-you-find-out-which-process-is-listening-on-a-port-on-windows) and stop it using Task Manager.

#### Using a port other than 8081[​](#using-a-port-other-than-8081 "Direct link to Using a port other than 8081")

You can configure the bundler to use a port other than 8081 by using the `port` parameter, from the root of your project run:

* npm* Yarn

shell

```
npm start -- --port=8088  

```

shell

```
yarn start --port 8088  

```

You will also need to update your applications to load the JavaScript bundle from the new port. If running on device from Xcode, you can do this by updating occurrences of `8081` to your chosen port in the `ios/__App_Name__.xcodeproj/project.pbxproj` file.

### NPM locking error[​](#npm-locking-error "Direct link to NPM locking error")

If you encounter an error such as `npm WARN locking Error: EACCES` while using the React Native CLI, try running the following:

shell

```
sudo chown -R $USER ~/.npm  
sudo chown -R $USER /usr/local/lib/node_modules  

```

### Missing libraries for React[​](#missing-libraries-for-react "Direct link to Missing libraries for React")

If you added React Native manually to your project, make sure you have included all the relevant dependencies that you are using, like `RCTText.xcodeproj`, `RCTImage.xcodeproj`. Next, the binaries built by these dependencies have to be linked to your app binary. Use the `Linked Frameworks and Binaries` section in the Xcode project settings. More detailed steps are here: [Linking Libraries](/docs/linking-libraries-ios#content).

If you are using CocoaPods, verify that you have added React along with the subspecs to the `Podfile`. For example, if you were using the `<Text />`, `<Image />` and `fetch()` APIs, you would need to add these in your `Podfile`:

```
pod 'React', :path => '../node_modules/react-native', :subspecs => [  
  'RCTText',  
  'RCTImage',  
  'RCTNetwork',  
  'RCTWebSocket',  
]  

```

Next, make sure you have run `pod install` and that a `Pods/` directory has been created in your project with React installed. CocoaPods will instruct you to use the generated `.xcworkspace` file henceforth to be able to use these installed dependencies.

#### React Native does not compile when being used as a CocoaPod[​](#react-native-does-not-compile-when-being-used-as-a-cocoapod "Direct link to React Native does not compile when being used as a CocoaPod")

There is a CocoaPods plugin called [cocoapods-fix-react-native](https://github.com/orta/cocoapods-fix-react-native) which handles any potential post-fixing of the source code due to differences when using a dependency manager.

#### Argument list too long: recursive header expansion failed[​](#argument-list-too-long-recursive-header-expansion-failed "Direct link to Argument list too long: recursive header expansion failed")

In the project's build settings, `User Search Header Paths` and `Header Search Paths` are two configs that specify where Xcode should look for `#import` header files specified in the code. For Pods, CocoaPods uses a default array of specific folders to look in. Verify that this particular config is not overwritten, and that none of the folders configured are too large. If one of the folders is a large folder, Xcode will attempt to recursively search the entire directory and throw above error at some point.

To revert the `User Search Header Paths` and `Header Search Paths` build settings to their defaults set by CocoaPods - select the entry in the Build Settings panel, and hit delete. It will remove the custom override and return to the CocoaPod defaults.

### No transports available[​](#no-transports-available "Direct link to No transports available")

React Native implements a polyfill for WebSockets. These [polyfills](https://github.com/facebook/react-native/blob/main/packages/react-native/Libraries/Core/InitializeCore.js) are initialized as part of the react-native module that you include in your application through `import React from 'react'`. If you load another module that requires WebSockets, such as [Firebase](https://github.com/facebook/react-native/issues/3645), be sure to load/require it after react-native:

```
import React from 'react';  
import Firebase from 'firebase';  

```

Shell Command Unresponsive Exception[​](#shell-command-unresponsive-exception "Direct link to Shell Command Unresponsive Exception")
------------------------------------------------------------------------------------------------------------------------------------

If you encounter a ShellCommandUnresponsiveException exception such as:

```
Execution failed for task ':app:installDebug'.  
  com.android.builder.testing.api.DeviceException: com.android.ddmlib.ShellCommandUnresponsiveException  

```

Try [downgrading your Gradle version to 1.2.3](https://github.com/facebook/react-native/issues/2720) in `android/build.gradle`.

react-native init hangs[​](#react-native-init-hangs "Direct link to react-native init hangs")
---------------------------------------------------------------------------------------------

If you run into issues where running `npx react-native init` hangs in your system, try running it again in verbose mode and referring to [#2797](https://github.com/facebook/react-native/issues/2797) for common causes:

shell

```
npx react-native init --verbose  

```

When you're debugging a process or need to know a little more about the error being thrown, you may want to use the verbose option to output more logs and information to nail down your issue.

Run the following command in your project's root directory.

* npm* Yarn

shell

```
npm run android -- --verbose  

```

shell

```
yarn android --verbose  

```

Unable to start react-native package manager (on Linux)[​](#unable-to-start-react-native-package-manager-on-linux "Direct link to Unable to start react-native package manager (on Linux)")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Case 1: Error "code":"ENOSPC","errno":"ENOSPC"[​](#case-1-error-codeenospcerrnoenospc "Direct link to Case 1: Error \"code\":\"ENOSPC\",\"errno\":\"ENOSPC\"")

Issue caused by the number of directories [inotify](https://github.com/guard/listen/blob/master/README.md#increasing-the-amount-of-inotify-watchers) (used by watchman on Linux) can monitor. To solve it, run this command in your terminal window

shell

```
echo fs.inotify.max_user_watches=582222 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p  

```

### Error: spawnSync ./gradlew EACCES[​](#error-spawnsync-gradlew-eacces "Direct link to Error: spawnSync ./gradlew EACCES")

If you run into issue where executing `npm run android` or `yarn android` on macOS throws the above error, try to run `sudo chmod +x android/gradlew` command to make `gradlew` files into executable.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/troubleshooting.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/troubleshooting.md)

Last updated on **Apr 14, 2025**

[Previous

Using List Views](/docs/using-a-listview)[Next

Platform-Specific Code](/docs/platform-specific-code)

* [Port already in use](#port-already-in-use)* [NPM locking error](#npm-locking-error)* [Missing libraries for React](#missing-libraries-for-react)* [No transports available](#no-transports-available)* [Shell Command Unresponsive Exception](#shell-command-unresponsive-exception)* [react-native init hangs](#react-native-init-hangs)* [Unable to start react-native package manager (on Linux)](#unable-to-start-react-native-package-manager-on-linux)
              + [Case 1: Error "code":"ENOSPC","errno":"ENOSPC"](#case-1-error-codeenospcerrnoenospc)+ [Error: spawnSync ./gradlew EACCES](#error-spawnsync-gradlew-eacces)

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