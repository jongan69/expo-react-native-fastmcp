Errors and warnings - Expo Documentation

[Docs](/)

[Blog](https://expo.dev/blog)[Changelog](https://expo.dev/changelog)[Star Us on GitHub](https://github.com/expo/expo)

Search

[Home](/)[Guides](/guides/overview)[EAS](/eas)[Reference](/versions/latest)[Learn](/tutorial/overview)

Get started

[Introduction](/get-started/introduction)[Create a project](/get-started/create-a-project)[Set up your environment](/get-started/set-up-your-environment)[Start developing](/get-started/start-developing)[Next steps](/get-started/next-steps)

Develop

[Tools for development](/develop/tools)

Navigation

User interface

Development builds

Config plugins

Debugging

[Errors and warnings](/debugging/errors-and-warnings)[Runtime issues](/debugging/runtime-issues)[Tools](/debugging/tools)[Dev tools plugins](/debugging/devtools-plugins)[Create a dev tools plugin](/debugging/create-devtools-plugins)

[Authentication](/develop/authentication)[Unit testing](/develop/unit-testing)

Review

[Distributing apps for review](/review/overview)[Share previews with your team](/review/share-previews-with-your-team)[Open updates with Orbit](/review/with-orbit)

Deploy

[Build project for app stores](/deploy/build-project)[Submit to app stores](/deploy/submit-to-app-stores)[App stores metadata](/deploy/app-stores-metadata)[Send over-the-air updates](/deploy/send-over-the-air-updates)[Deploy web apps](/deploy/web)

Monitor

[Monitoring services](/monitoring/services)

More

[Core concepts](/core-concepts)[FAQ](/faq)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Errors and warnings
===================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/debugging/errors-and-warnings.mdx)

Learn about Redbox errors and stack traces in your Expo project.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/debugging/errors-and-warnings.mdx)

---

When developing an application using Expo, you'll encounter a Redbox error or Yellowbox warning. These logging experiences are provided by [LogBox in React Native](https://reactnative.dev/blog/2020/07/06/version-0.63).

Redbox error and Yellowbox warning
----------------------------------

A Redbox error is displayed when a fatal error prevents your app from running. A Yellowbox warning is displayed to inform you that there is a possible issue and you should probably resolve it before shipping your app.

You can also create warnings and errors on your own with `console.warn("Warning message")` and `console.error("Error message")`. Another way to trigger the redbox is to throw an error and not catch it: `throw Error("Error message")`.

> This is a brief introduction to debugging a React Native app with Expo CLI. For in-depth information, see [Debugging](/debugging/runtime-issues).

Stack traces
------------

When you encounter an error during development, you'll see the error message and a stack trace, which is a report of the recent calls your application made when it crashed. This stack trace is shown both in your terminal and the Expo Go app or if you have created a development build.

This stack trace is extremely valuable since it gives you the location of the error's occurrence. For example, in the following image, the error comes from the file HomeScreen.js and is caused on line 7 in that file.

![An example of a stack trace in a React Native app.](/static/images/stack-trace.jpg)

When you look at that file, on line 7, you will see that a variable called `renderDescription` is referenced. The error message describes that the variable is not found because the variable is not declared in HomeScreen.js. This is a typical example of how helpful error messages and stack traces can be if you take the time to decipher them.

Debugging errors is one of the most frustrating but satisfying parts of development. Remember that you're never alone. The Expo community and the React and React Native communities are great resources for help when you get stuck. There's a good chance someone else has run into your exact error. Make sure to read the documentation, search the [forums](https://chat.expo.dev/), [GitHub issues](https://github.com/expo/expo/issues/), and [Stack Overflow](https://stackoverflow.com/).

[Previous (Develop - Config plugins)

Development and debugging](/config-plugins/development-and-debugging)[Next (Develop - Debugging)

Runtime issues](/debugging/runtime-issues)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/debugging/errors-and-warnings.mdx)
* Last updated on June 16, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Redbox error and Yellowbox warning](/debugging/errors-and-warnings/#redbox-error-and-yellowbox-warning)[Stack traces](/debugging/errors-and-warnings/#stack-traces)