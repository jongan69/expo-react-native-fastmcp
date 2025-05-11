"Application has not been registered" error - Expo Documentation

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

[Overview](/troubleshooting/overview)["Application has not been registered" error](/troubleshooting/application-has-not-been-registered)[Clear bundler caches on macOS and Linux](/troubleshooting/clear-cache-macos-linux)[Clear bundler caches on Windows](/troubleshooting/clear-cache-windows)["React Native version mismatch" errors](/troubleshooting/react-native-version-mismatch)[Proxies](/troubleshooting/proxies)

Regulatory compliance

[Data and Privacy protection](/regulatory-compliance/data-and-privacy-protection)[GDPR compliance](/regulatory-compliance/gdpr)[HIPAA compliance](/regulatory-compliance/hipaa)[Privacy Shield](/regulatory-compliance/privacy-shield)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

"Application has not been registered" error
===========================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/troubleshooting/application-has-not-been-registered.mdx)

Learn about what the Application has not been registered error means and how to resolve it in an Expo or React Native app.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/troubleshooting/application-has-not-been-registered.mdx)

---

When developing an Expo or React Native app, it's common to run into an error that looks like:

Terminal

`Application "main" has not been registered.``# Or``Invariant Violation: "main" has not been registered.`

In this particular error, `"main"` can be any string.

What this error means
---------------------

### An exception may be preventing your app from registering itself

The most common cause of this error is that there is an exception thrown in your application before it's able to register itself. When a React Native application loads, there are two steps:

1. Load the JavaScript code, and if everything is successful, then your application will be registered. If there is any exception when loading the bundle then execution will be aborted and it will never reach the part where your application is registered.
2. Run the registered application. If loading the code failed, then the application won't be registered and you will see the error that is the subject of this page.

If you're in this situation, the error message you're seeing is a [red herring](https://en.wikipedia.org/wiki/Red_herring), it's distracting you from the real error that led to the application not being registered.

Look at your logs before this error message to see what may have caused it. A frequent cause is multiple versions of a native module dependency that registers itself as a view â for example [this Stack Overflow thread](https://stackoverflow.com/questions/67543844/invariant-violation-main-has-not-been-registered-while-running-react-native-a/67550379) where the poster has multiple versions of `react-native-safe-area-context` in their dependencies.

### Your app root component may not be registered

Another possibility is that there is a mismatch between the `AppKey` being provided to [`AppRegistry.registerComponent`](https://reactnative.dev/docs/appregistry#registercomponent), and the `AppKey` being registered on the native iOS or Android side.

In managed projects, the default behavior is to use "main" as the `AppKey`. This is handled for you automatically, and as long as you don't change the `"main"` field in your package.json from the default value then this will just work. If you want to customize the app entry point, see [registerRootComponent](/versions/latest/sdk/register-root-component) API reference.

In projects with native code, you will see something like this in your index.js by default:

```
import { registerRootComponent } from 'expo';
import App from './App';
registerRootComponent(App);

```

where `registerRootComponent` is implemented as:

```
function registerRootComponent(component) {
  AppRegistry.registerComponent('main', () => component);
}

```

And on the native side, in AppDelegate.m you should see:

```
RCTRootView *rootView = [[RCTRootView alloc] initWithBridge:bridge moduleName:@"main" initialProperties:nil];

```

and in MainActivity.java:

```
@Override
protected String getMainComponentName() {
  return "main";
}

```

By default, "main" is consistently used throughout the project. If you're running into this error, something has likely changed and these values no longer coincide. Ensure that the names you are registering on the JavaScript side are the ones expected on the native side (if you're using Expo's `registerRootComponent` function, that would be "main").

Other considerations
--------------------

This error can also occur in a few other scenarios, but it's less predictable and the fixes would be more specific to your project. For example, some other cases are:

* You're connecting to the wrong project's local development server. Try closing out other Expo CLI or React Native community CLI processes (find them with `ps -A | grep "expo\|react-native"`).
* If this error is only occurring in your production app, then try running the app locally in production mode with `npx expo start --no-dev --minify` to find the source of the error.

[Previous (More - Troubleshooting)

Overview](/troubleshooting/overview)[Next (More - Troubleshooting)

Clear bundler caches on macOS and Linux](/troubleshooting/clear-cache-macos-linux)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/troubleshooting/application-has-not-been-registered.mdx)
* Last updated on October 01, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[What this error means](/troubleshooting/application-has-not-been-registered/#what-this-error-means)[An exception may be preventing your app from registering itself](/troubleshooting/application-has-not-been-registered/#an-exception-may-be-preventing-your-app-from-registering-itself)[Your app root component may not be registered](/troubleshooting/application-has-not-been-registered/#your-app-root-component-may-not-be-registered)[Other considerations](/troubleshooting/application-has-not-been-registered/#other-considerations)