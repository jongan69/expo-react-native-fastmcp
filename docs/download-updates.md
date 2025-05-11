Downloading updates - Expo Documentation

[Docs](/)

[Blog](https://expo.dev/blog)[Changelog](https://expo.dev/changelog)[Star Us on GitHub](https://github.com/expo/expo)

Search

[Home](/)[Guides](/guides/overview)[EAS](/eas)[Reference](/versions/latest)[Learn](/tutorial/overview)

[Introduction](/eas)[Configuration with eas.json](/eas/json)[Environment variables](/eas/environment-variables)

EAS Workflows

[Get started](/eas/workflows/get-started)[Example CI/CD workflows](/eas/workflows/examples)[Syntax for EAS Workflows](/eas/workflows/syntax)[Automating EAS CLI commands](/eas/workflows/automating-eas-cli)

Reference

EAS Build

[Introduction](/build/introduction)[Create your first build](/build/setup)[Configure with eas.json](/build/eas-json)[Internal distribution](/build/internal-distribution)[Automate submissions](/build/automate-submissions)[Using EAS Update](/build/updates)[Trigger builds from CI](/build/building-on-ci)[Trigger builds from GitHub App](/build/building-from-github)[Expo Orbit](/build/orbit)

App signing

Custom builds

Reference

EAS Hosting

[Introduction](/eas/hosting/introduction)[Get started](/eas/hosting/get-started)[Deployments and aliases](/eas/hosting/deployments-and-aliases)[Environment variables](/eas/hosting/environment-variables)[Custom domain](/eas/hosting/custom-domain)[Monitoring API routes](/eas/hosting/api-routes)[Workflows](/eas/hosting/workflows)

Reference

EAS Submit

[Introduction](/submit/introduction)[Submit to the Google Play Store](/submit/android)[Submit to the Apple App Store](/submit/ios)[Configure with eas.json](/submit/eas-json)

EAS Update

[Introduction](/eas-update/introduction)[Get started](/eas-update/getting-started)

Preview

Deployment

[Deploy updates](/eas-update/deployment)[Downloading updates](/eas-update/download-updates)[Rollouts](/eas-update/rollouts)[Rollbacks](/eas-update/rollbacks)[Optimize assets](/eas-update/optimize-assets)[Continuous deployment](/eas-update/continuous-deployment)[Alternative deployment patterns](/eas-update/deployment-patterns)

Concepts

Troubleshooting

Reference

EAS Metadata

[Introduction](/eas/metadata)[Get started](/eas/metadata/getting-started)

Reference

EAS Insights

[Introduction](/eas-insights/introduction)

Distribution

[Overview](/distribution/introduction)[App stores best practices](/distribution/app-stores)[App transfers](/distribution/app-transfers)[Understanding app size](/distribution/app-size)

Reference

[Webhooks](/eas/webhooks)

Expo accounts

Billing

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Downloading updates
===================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/download-updates.mdx)

Learn strategies for downloading and launching updates.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/download-updates.mdx)

---

> All of the following information on this page applies only to release builds and debug builds [with `EX_UPDATES_NATIVE_DEBUG` enabled](/eas-update/debug#runtime-issues).

In this section, we'll cover the different strategies for downloading and launching updates. The goal is to ensure that the end user adopts the latest version of the app as soon as possible after it is published, without sacrificing the user experience by introducing slow loading screens or other issues. The strategies are not mutually exclusive, and you can mix and match them as needed for the requirements of your app.

Updates are loaded asynchronously on startup by default
-------------------------------------------------------

The default behavior is to check for an update when the app is cold booted (launched from a killed state) and download the update if it's available. This process does not block loading the app, so when using this strategy the end user will only load the update when they cold boot the app after an update has been published, and then at some point kill and restart the app (for example, if they close it from the recent apps list on the OS or if they turn the device off and on).

This behavior is safe because it doesn't interfere with app startup to wait for a network request to complete (which would be a bad user experience in common real-world cases where a user finds themself with a slow connection and they are stuck on a loading screen for several seconds). The downside is that it takes much longer for users to adopt the latest version of the app. If the ideal is for an update to be adopted immediately by all users as soon as it is published, then this strategy falls very short of that.

What if I want to always block app startup until the latest update is downloaded?

We recommend against this strategy because the resulting user experience is extremely poor. Typically when a user is stuck waiting on a splash screen when booting an app, they will close the app and try again (and so downloading the update won't complete), or give up and use another app. When the users' device is connected to a slow network, even when there is no update, they may have to wait several seconds or more to load the app. If ensuring that your users always have the latest version of your app is critical, you may want to explore one of the other strategies explained here.

How can I disable the default behavior?

You can disable the default behavior by setting the [`checkAutomatically`](/versions/latest/sdk/updates#updatescheckautomaticallyvalue) option to `NEVER` in the `updates` configuration. This will prevent the app from checking for updates and downloading them automatically.

Checking for updates while the app is running
---------------------------------------------

You can use `Updates.checkForUpdateAsync()` to check for updates while the app is running. This will return a promise that resolves to a [`UpdateCheckResult` object](/versions/latest/sdk/updates#updatecheckresult), with `isAvailable` set to `true` if an update is available, and information about the update in the [`manifest`](/versions/latest/sdk/manifests#expoupdatesmanifest) property.

If an update is available, you can use the `Updates.downloadAsync()` method to download the update. This will return a promise that resolves when the download is complete. Finally, you can use the `Updates.reloadAsync()` method to reload the app with the new version. The `useUpdates()` hook can also be used to monitor the state of the `expo-updates` library from a React component.

What are common patterns for checking for updates while the app is running?

* You can check for updates at various points in your app's lifecycle, such as [when it is foregrounded](https://reactnative.dev/docs/appstate) or at some interval. When an update is found, you may want to show a dialog to the user to prompt the user to update.
* You can check for updates at launch and display your own custom loading screen, if it is very important for your use case to ensure that users always get the latest version at launch.

Checking for updates while the app is backgrounded
--------------------------------------------------

You can use [`expo-background-task`](/versions/latest/sdk/background-task) to check for updates while the app is backgrounded. To do this, use the same `Updates.checkForUpdateAsync()` and `Updates.downloadAsync()` methods as you would in the foreground, but execute them inside of a background task. This is a great way to ensure that the user always has the latest version of the app, even if they have not opened the app in a while.

It's worth considering whether you want to reload the app after an update is downloaded in the background, or wait for the user to close and reopen it. If you choose to only download it in the background and not apply it, this should still be useful to ensure that the next boot will immediately have the latest version, and it will lead to a faster adoption rate for updates compared to the default behavior.

An example of how to check for updates in the background

To ensure the background task is registered when the application starts, import and invoke the `setupBackgroundUpdates` function within the top-level component.

```
import * as TaskManager from 'expo-task-manager';
import * as BackgroundTask from 'expo-background-task';
import * as Updates from 'expo-updates';

const BACKGROUND_TASK_NAME = 'task-run-expo-update';

export const setupBackgroundUpdates = async () => {
  TaskManager.defineTask(BACKGROUND_TASK_NAME, async () => {
    const update = await Updates.checkForUpdateAsync();
    if (update.isAvailable) {
      await Updates.fetchUpdateAsync();
      await Updates.reloadAsync();
    }
    return Promise.resolve();
  });

  await BackgroundTask.registerTaskAsync(BACKGROUND_TASK_NAME, {
    minimumInterval: 60 * 24,
  });
};

setupBackgroundUpdates();

```

Should I also apply the update with Updates.reloadAsync() when the app is backgrounded?

Support for calling `Updates.reloadAsync()` while the app is backgrounded is experimental. This is a new feature and it is not widely used, be sure to monitor for crashes when you first enable it. Downloading an update in the background is safe.

Reloading an update while the app is backgrounded can be a great way to ensure that the user has the latest version of the app when they open it again. However, it is important to note that, unless you persist the state that the app was in at the time it was backgrounded and restore that state, the user will experience a cold boot when they open the app again. One way to mitigate this is to only do a reload in the background if the app has been inactive for a certain period of time, after which a user is unlikely to expect the app to restore its previous state.

Critical/mandatory updates
--------------------------

There is no first-class support for critical/mandatory updates in the `expo-updates` library. However, you can implement your own logic to check for critical updates and apply them manually. The [`expo/UpdatesAPIDemo` repository](https://github.com/expo/UpdatesAPIDemo) contains an example of one way to approach this. You can combine that approach with the strategies above to check for updates.

Controlling which update to load from the client side
-----------------------------------------------------

The typical way to use EAS Update is to have a single update URL and a set of request headers (such as update channel name) embedded in a build of your app. To control which update is loaded, you make changes on the server through the `eas update` command or the EAS dashboard. For example, you publish a new update to a channel that your build is pointing to, then the build fetches that update on the next launch. Updates published to a channel different from the one your build is pointing to will not be downloaded with this approach.

You can override the update URL and request headers at runtime using the `Updates.setUpdateURLAndRequestHeadersOverride()` method. This can be useful if you want to load a specific update or change the update channel while the app is running. [Learn more](/eas-update/override).

Monitoring adoption of updates
------------------------------

The details page for an update (for example: `https://expo.dev/accounts/[account]/projects/[project]/updates/[id]`) shows metrics for the number of users who have run the update, in addition to the number of failed installs (users who download and attempted to run the update, but it crashed).

The deployments page (for example: `https://expo.dev/accounts/[account]/projects/[project]/deployments/production/[runtime-version]`) includes a table and chart that shows the number of users who have run each update related to a particular update channel and runtime version combination, over a given time period.

[Previous (EAS Update - Deployment)

Deploy updates](/eas-update/deployment)[Next (EAS Update - Deployment)

Rollouts](/eas-update/rollouts)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/download-updates.mdx)
* Last updated on April 25, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Updates are loaded asynchronously on startup by default](/eas-update/download-updates/#updates-are-loaded-asynchronously-on-startup-by-default)[Checking for updates while the app is running](/eas-update/download-updates/#checking-for-updates-while-the-app-is-running)[Checking for updates while the app is backgrounded](/eas-update/download-updates/#checking-for-updates-while-the-app-is-backgrounded)[Critical/mandatory updates](/eas-update/download-updates/#criticalmandatory-updates)[Controlling which update to load from the client side](/eas-update/download-updates/#controlling-which-update-to-load-from-the-client-side)[Monitoring adoption of updates](/eas-update/download-updates/#monitoring-adoption-of-updates)