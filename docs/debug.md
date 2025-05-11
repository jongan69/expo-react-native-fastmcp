EAS Update Debugging - Expo Documentation

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

Concepts

Troubleshooting

[Debugging](/eas-update/debug)[Error recovery](/eas-update/error-recovery)

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

EAS Update Debugging
====================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/debug.mdx)

Learn how to use basic debugging techniques to fix an update issue.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/debug.mdx)

---

This guide shows how to verify our configuration so that we can find the source of problems like an app not showing a published update. It's important to tell the current state of our app at any given time, so EAS Update was built with this in mind. Once we know which updates are running on which builds, we can make changes so that our apps are in the state we expect.

[![How to debug EAS Update](https://i3.ytimg.com/vi/m9PLTr3t3S4/maxresdefault.jpg)

How to debug EAS Update

In this Expo debugging tutorial, you'll learn how to debug a situation where your build isn't getting an update.](https://www.youtube.com/watch?v=m9PLTr3t3S4)
  
> If we are not using EAS Build, our Deployments page will be empty. Follow the guide on [debugging configuration without EAS Build](/eas-update/debug-advanced#configuration-without-eas-build) instead.

Go to the Deployments page
--------------------------

The EAS website has a [Deployments page](https://expo.dev/accounts/%5Baccount%5D/projects/%5Bproject%5D/deployments) that shows the current state of our app. The term *deployment* refers to a group of builds and their corresponding updates. If we've made builds and updates with EAS, we can see our project's status on the website in the Deployments tab.

![Deployments tab](/static/images/eas-update/deployments-website-tab.png)

Common problems
---------------

The following section describes common problems and how to fix them. Below is a diagram of how EAS Update works and the spots that are useful to inspect when finding the root cause of an issue. In the following sections, we'll inspect and verify these spots and more.

![Map of debugging spots](/static/images/eas-update/debug-map.png)

### Unexpected channel

![Deployment has unexpected channel](/static/images/eas-update/deployments-wrong-channel.png)

If the deployment channel is unexpected, it means our build was not built with the correct channel. To fix this, [configure our channel](/eas-update/debug#configure-channel) and rebuild our app.

### Unexpected runtime version

![Deployment has unexpected runtime version](/static/images/eas-update/deployments-wrong-runtime.png)

If the deployment runtime version is unexpected, it means our build was not built with the correct runtime version. To fix this, [configure our runtime version](/eas-update/debug#configure-runtime-version) and rebuild our app.

### Unexpected branch

![Deployment has unexpected branch](/static/images/eas-update/deployments-wrong-branch.png)

If the deployment has an unexpected branch, we need to [map our channel to the correct branch](/eas-update/debug#map-channel-to-branch).

### Missing updates

![Deployment has no updates](/static/images/eas-update/deployments-no-updates.png)

The displayed deployment does not have any updates. To fix this, [publish an update to the branch](/eas-update/debug#publish-update). If an update was already published, check the [Updates page](https://expo.dev/accounts/%5Baccount%5D/projects/%5Bproject%5D/updates) to make sure it matches the runtime version of our build.

### Missing branch

![Deployment has no branch](/static/images/eas-update/deployments-no-branch.png)

The displayed deployment has the correct channel, but it is not linked to a branch. To fix this, [map the channel to the correct branch](/eas-update/debug#map-channel-to-branch).

### Missing deployment

If our deployment is not displayed, it means our build is not configured properly for EAS Update. To fix this, [configure our channel](/eas-update/debug#configure-channel), [configure our runtime version](/eas-update/debug#configure-runtime-version) and verify our [general configuration](/eas-update/debug-advanced#verifying-app-configuration). We'll need to rebuild our app after making these changes.

### Automatic roll back when an update crashes

If everything looks correct on the Deployments page, but your app still shows the previous update or the code embedded with the build, your new update's code may be crashing. This can happen when this new update crashes before the root component renders after the app downloads and applies the new update.

EAS Update is designed to automatically roll back to the previous update if it detects that a new update crashed shortly after launch. See [how EAS Update detects crashes and rolls back to a previous working version](/eas-update/error-recovery#explaining-the-error-recovery-flow) for more information.

To diagnose the error causing the update crash:

* See the [Troubleshooting guide on runtime issues](/debugging/runtime-issues) to apply a strategy to identify the error.
* After identifying the error, publish a new update that fixes the crash to resolve the issue.

A common reason a new update does not work but embedded code does is due to a missing environment variable. See [how environment variables work with EAS Update](/eas-update/environment-variables) for more information.

Solutions
---------

### Configure channel

To verify that a build has a specific channel, make sure our build profile in eas.json has a channel property:

eas.json

Copy

```
{
  "build": {
    "preview": {
      "distribution": "internal",
      "channel": "preview"
    },
    "production": {
      "channel": "production"
    }
  }
}

```

Then, we can run a command like `eas build --profile preview` to create a build with a channel named "preview".

### Configure runtime version

To verify our runtime version, we make sure our app config (app.json/app.config.js) has a `runtimeVersion` property:

app.json

Copy

```
{
  "expo": {
    "runtimeVersion": {
      "policy": "sdkVersion"
    }
  }
}

```

By default, it is `{ "policy": "sdkVersion" }`, but we can change our runtime to [use a different policy or a specific version](/eas-update/runtime-versions). Then, we can run a command like `eas build --profile preview` to create a build with the runtime version we expect.

### Map channel to branch

If the channel is not mapped to the branch we expect, we can change the link with:

Terminal

Copy

`# eas channel:edit [channel-name] --branch [branch-name]`  
`# Example`

`-Â``eas channel:edit production --branch release-1.0`

If our branch is not listed, we can create a new branch with `eas branch:create`.

### Publish update

To create and publish an update, we can run the following command:

Terminal

Copy

`-Â``eas update`

After publishing, the output will display the branch and the runtime version. This information can help us verify that we're creating an update with the configuration we expect.

General strategies
------------------

Try these strategies before using the more specific ones mentioned in this guide.

### Use `expo-dev-client`

Create a [development version of our build](/eas-update/expo-dev-client). It will help us preview published updates inside a problematic build.

### In-app debugging

The `expo-updates` library exports a variety of functions to interact with updates once the app is already running. In certain cases, making a call to fetch an update and seeing an error message can help us narrow down the root cause. We can make a simulator build of the project and manually check to see if updates are available or if there are errors when fetching updates.

* Print the [Update.Constants](/versions/latest/sdk/updates#constants) to verify our configuration.
* [Examine log entries](/versions/latest/sdk/updates#updatesreadlogentriesasyncmaxage) surfaced from the native layer.
* Fetch and [load updates manually](/versions/latest/sdk/updates#check-for-updates-manually).

Configuration issues
--------------------

Our app is still not receiving the expected update despite following the [basic guide](/eas-update/debug).

### `expo-updates` configuration

The `expo-updates` library runs inside an end-user's app and makes requests to an update server to get the latest update.

#### Verifying app configuration

When we set up EAS Update, we likely ran `eas update:configure` to configure expo-updates to work with EAS Update. This command makes changes to our app config (app.json/app.config.js). Here are the fields we'd expect to see:

* `runtimeVersion` should be set. By default, it is `{ "policy": "sdkVersion" }`. If our project has android and ios directories, we'll have to set the `runtimeVersion` manually.
* `updates.url` should be a value like `https://u.expo.dev/your-project-id`, where `your-project-id` matches the ID of our project. We can see this ID on [our website](https://expo.dev/accounts/%5Baccount%5D/projects/%5Bproject%5D).
* `updates.enabled` should not be `false`. It's `true` by default if it is not specified.

Finally, make sure that `expo-updates` is included in package.json. If it's not, run:

Terminal

Copy

`-Â``npx expo install expo-updates`

#### Inspecting expo-updates configuration after prebuild

Whenever we run `eas build`, the `npx expo prebuild` command is run on our project on EAS servers to unpack the android and ios directories that contain native files. This makes it so EAS Build can build any project, whether it includes the native files or not.

If our project does not have android or ios directories, we can make commit any existing changes, then run `npx expo prebuild` to inspect the project state that EAS Build will act on. After running this, look for the following files: android/app/src/main/AndroidManifest.xml and ios/your-project-name/Supporting/Expo.plist.

In each, we expect to see configuration for the EAS Update URL and the runtime version. Here are the properties we'd expect to see in each file:

AndroidManifest.xml

Copy

```
%%placeholder-start%%... %%placeholder-end%%
<meta-data android:name="expo.modules.updates.EXPO_RUNTIME_VERSION" android:value="your-runtime-version-here"/>
<meta-data android:name="expo.modules.updates.EXPO_UPDATE_URL" android:value="https://u.expo.dev/your-project-id-here"/>
%%placeholder-start%%... %%placeholder-end%%

```

Expo.plist

Copy

```
%%placeholder-start%%... %%placeholder-end%%
<key>EXUpdatesRuntimeVersion</key>
<string>your-runtime-version-here</string>
<key>EXUpdatesURL</key>
<string>https://u.expo.dev/your-project-id-here</string>
%%placeholder-start%%... %%placeholder-end%%

```

### Configuration without EAS Build

If we aren't using EAS Build, this section will walk through debugging the state of EAS Update in our project. We'll need to look at multiple spots in the system. Below is a diagram of how EAS Update works and the spots that are useful to inspect when finding the root cause of an issue. In the sections following, we'll inspect and verify these spots and more.

![Map of debugging spots](/static/images/eas-update/debug-map.png)

#### Verify build configuration

Follow the [Building Locally guide](/eas-update/standalone-service) to configure our app's channel and runtime version. We'll also need to make sure our [general configuration](/eas-update/debug-advanced#expo-updates-configuration) is correct.

#### Verify the channel

Builds have a property named `channel`, which EAS Update uses to link to a branch. A channel is often given to multiple platform-specific builds. For instance, we might have an Android build and an iOS build, both with a channel named `"production"`.

Once a build has a channel name, we can make sure that EAS servers know about it by checking the [Channels page](https://expo.dev/accounts/%5Baccount%5D/projects/%5Bproject%5D/channels).

We'd expect the page to display the same channel name that our build has. If it's not there, we can create the channel on EAS servers with:

Terminal

Copy

`# eas channel:create [channel-name]`  
`# Example`

`-Â``eas channel:create production`

#### Verify the channel/branch mapping

There is a link that is defined by the developer between a channel and a branch. When a channel and branch are linked, an app with a channel will get the most recent compatible update on the linked branch.

The [Channels page](https://expo.dev/accounts/%5Baccount%5D/projects/%5Bproject%5D/channels) will display the channel to branch mapping if it exists.

![Linked branches on the Channels page](/static/images/eas-update/channels-linked-branches.png)

If the channel is not linked to the branch we expect, we can change the link with:

Terminal

Copy

`# eas channel:edit [channel-name] --branch [branch-name]`  
`# Example`

`-Â``eas channel:edit production --branch release-1.0`

#### Verify the update

Every branch contains a list of updates. When a build makes a call for an update, we find the channel of the build, then the branch linked to that channel. Once the branch is found, EAS will return the most recent compatible update on that branch. A build and an update are compatible when they share the same runtime version and platform.

To inspect which updates are on a branch, we can go to the [Branches page](https://expo.dev/accounts/%5Baccount%5D/projects/%5Bproject%5D/branches) and choose our branch of interest.

The Branch Detail page will show us a list of updates and their runtime versions and platforms. From this list, we should be able to figure out which update should apply to a given build, by matching the build's runtime version and platform to update's runtime version and platform. The most recent update that is compatible will be available for a build to download and execute.

![List of updates on the Branch Detail page](/static/images/eas-update/branch-update-list.png)

Debugging EAS Update
--------------------

After verifying `expo-updates` and EAS Update configurations, we can move on to debugging how our project is interacting with updates.

### In-app debugging

The `expo-updates` library exports a variety of functions to interact with updates once the app is already running. In certain cases, making a call to fetch an update and seeing an error message can help us narrow down the root cause. We can make a simulator build of the project and manually check to see if updates are available or if there are errors when fetching updates. See the code example to [check for updates manually](/versions/latest/sdk/updates#use-expo-updates-with-a-custom-server).

### Inspecting a build manually

When building a project into an app, there can be multiple steps that alter the output of `npx expo prebuild`. After making a build, it is possible to open the build's contents and inspect native files to see its final configuration.

Here are the steps for inspecting an iOS Simulator build on macOS:

1. Create an iOS Simulator build of the app using EAS Build. This is done by adding `"ios": { "simulator": true }` to a build profile.
2. Once the build is finished, download the result and unzip it.
3. Then, right click on the app and select "Show Package Contents".
4. From there, we can inspect the Expo.plist file.

Inside the Expo.plist file, we expect to see the following configurations:

Expo.plist

Copy

```
%%placeholder-start%%... %%placeholder-end%%
<key>EXUpdatesRequestHeaders</key>
<dict>
  <key>expo-channel-name</key>
  <string>your-channel-name</string>
</dict>
<key>EXUpdatesRuntimeVersion</key>
<string>your-runtime-version</string>
<key>EXUpdatesURL</key>
<string>https://u.expo.dev/your-project-id</string>
%%placeholder-start%%... %%placeholder-end%%

```

### Inspecting manifests manually

When an update is published with EAS Update, we create a manifest that end-user app's request. The manifest has information like which assets and versions are needed for an update to load. We can inspect the manifest by going to a specific URL in a browser or by using `curl`.

Inside our project's app config (app.json/app.config.json), the URL we can GET is under `updates.url`.

This `url` is EAS' "<https://u.expo.dev>" domain, followed by the project's ID on EAS servers. If we go to the URL directly, we'll see an error about missing a header. We can view a manifest by adding three query parameters to the URL: `runtime-version`, `channel-name`, and `platform`. If we published an update with a runtime version of `1.0.0`, a channel of `production` and a platform of `android`, the full URL we could visit would be similar to this:

```
https://u.expo.dev/your-project-id?runtime-version=1.0.0&channel-name=production&platform=android

```

### Viewing network requests

Another way to identify the root cause of an issue is to look at the network requests that the app is making to EAS servers, then viewing the responses. We recommend using a program like [Proxyman](https://proxyman.io/) or [Charles Proxy](https://www.charlesproxy.com/) to watch network requests from our app.

With either program, we'll need to follow their instructions for installing an SSL certificate, so that the program can decode HTTPS requests. Once that's set up in a simulator or on an actual device, we can open our app and watch requests.

The requests we're interested in are from <https://u.expo.dev> and <https://assets.eascdn.net>. Responses from <https://u.expo.dev> will contain an update manifest, which specifies which assets the app will need to fetch to run the update. Responses from <https://assets.eascdn.net> will contain assets, like images, font files, and so on, that are required for the update to run.

When inspecting the request to <https://u.expo.dev>, we can look for the following request headers:

* `Expo-Runtime-Version`: this should make the runtime version we made our build and update with.
* `expo-channel-name`: this should be the channel name specified in the eas.json build profile.
* `Expo-Platform`: this should be either "android" or "ios".

As for all requests, we expect to see either `200` response codes, or `304` if nothing has changed.

Below is a screenshot showing the request of a successful update manifest request:

![Successful manifest request](/static/images/eas-update/network-request.png)

Runtime issues
--------------

We are able to load the expected update but our project is displaying unexpected behavior.

### Debugging of native code while loading the app through expo-updates

By default, we need to make a release build for `expo-updates` to be enabled and to load updates rather than reading from a development server. This is because debug builds behave like normal React Native project debug builds.

To make it easier to test and debug native code in an environment that is closer to production, follow the steps below to create a debug build of the app with `expo-updates` enabled.

We also provide a [step-by-step guide to try out EAS Update quickly](/eas-update/standalone-service) in a local development environment using Android Studio or Xcode, with either release or debug builds of the app.

#### Android local builds

* Set the debug environment variable: `export EX_UPDATES_NATIVE_DEBUG=1`
* [Ensure the desired channel is set in your AndroidManifest.xml](/eas-update/getting-started#configure-the-update-channel)
* Execute a [debug build](/debugging/runtime-issues#native-debugging) of the app with Android Studio or from the command line.

#### iOS local builds

* Set the debug environment variable: `export EX_UPDATES_NATIVE_DEBUG=1`
* Reinstall pods with `npx pod-install`. The `expo-updates` podspec now detects this environment variable, and makes changes so that the debug code that would normally load from the Metro packager is bypassed, and the app is built with the EXUpdates bundle and other dependencies needed to load updates from EAS.
* [Ensure the desired channel is set in our Expo.plist](/eas-update/getting-started#configure-the-update-channel)
* Modify the application Xcode project file to force bundling of the application JavaScript for both release and debug builds:

  Terminal

  Copy

  `-Â``sed -i '' 's/SKIP_BUNDLING/FORCE_BUNDLING/g;' ios/<project name>.xcodeproj/project.pbxproj`
* Execute a [debug build](/debugging/runtime-issues#native-debugging) of the app with Xcode or from the command line.

#### EAS Build

Alternatively, we can use EAS to create a debug build where `expo-updates` is enabled. The environment variable is set in eas.json, as shown in the example below:

eas.json

Copy

```
{
  "build": {
    "preview_debug": {
      "env": {
        "EX_UPDATES_NATIVE_DEBUG": "1"
      },
      "android": {
        "distribution": "internal",
        "withoutCredentials": true,
        "gradleCommand": ":app:assembleDebug"
      },
      "ios": {
        "simulator": true,
        "buildConfiguration": "Debug"
      },
      "channel": "preview_debug"
    }
  }
}

```

Publishing issues
-----------------

We are not able to publish an update, or parts of our update are not being published as expected.

### Inspecting the latest update locally

When we publish an update with EAS Update, it creates a /dist directory in the root of our project locally, which includes the assets that were uploaded as a part of the update.

![Dist directory](/static/images/eas-update/dist.png)

### Viewing all assets included in an update

It may be helpful to see which assets are included in our update bundle. We can see a list of named assets by running:

Terminal

Copy

`-Â``npx expo export`

Mitigation steps
----------------

Once we've found the root cause of the issue, there are various mitigation steps we might want to take. One of the most common problems is pushing an update that has a bug inside it. When this happens, we can re-publish a previous update to resolve the issue.

### Re-publishing a previous update

The fastest way to "undo" a bad publish is to re-publish a known good update. Imagine we have a branch with two updates:

Terminal

`branch: "production"``updates: [` `update 2 (id: xyz2) "fixes typo" // bad update` `update 1 (id: abc1) "updates color" // good update``]`

If "update 2" turned out to be a bad update, we can re-publish "update 1" with a command like this:

Terminal

`# eas update:republish --group [update-group-id]``# eas update:republish --branch [branch-name]`  
`# Example`

`-Â``eas update:republish --group abc1`

`-Â``eas update:republish --branch production`

The example command above would result in a branch that now appears like this:

Terminal

`branch: "production"``updates: [` `update 3 (id: def3) "updates color" // re-publish of update 1 (id: abc1)` `update 2 (id: xyz2) "fixes typo" // bad update` `update 1 (id: abc1) "updates color" // good update``]`

Since "update 3" is now the most recent update on the "production" branch, all users who query for an update in the future will receive "update 3" instead of the bad update, "update 2".

While this will prevent all new users from seeing the bad update, users who've already received the bad update will run it until they can download the latest update. Since mobile networks are not always able to download the most recent update, sometimes users may run a bad update for a long time. When viewing error logs for our app, it's normal to see a lingering long tail of errors as our users' apps get the most recent update or build. We'll know we solved the bug when we see the error rate decline dramatically; however, it likely will not disappear completely if we have a diverse user base across many locations and mobile networks.

[Previous (EAS Update - Concepts)

Runtime versions](/eas-update/runtime-versions)[Next (EAS Update - Troubleshooting)

Error recovery](/eas-update/error-recovery)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/debug.mdx)
* Last updated on December 30, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Go to the Deployments page](/eas-update/debug/#go-to-the-deployments-page)[Common problems](/eas-update/debug/#common-problems)[Unexpected channel](/eas-update/debug/#unexpected-channel)[Unexpected runtime version](/eas-update/debug/#unexpected-runtime-version)[Unexpected branch](/eas-update/debug/#unexpected-branch)[Missing updates](/eas-update/debug/#missing-updates)[Missing branch](/eas-update/debug/#missing-branch)[Missing deployment](/eas-update/debug/#missing-deployment)[Automatic roll back when an update crashes](/eas-update/debug/#automatic-roll-back-when-an-update-crashes)[Solutions](/eas-update/debug/#solutions)[Configure channel](/eas-update/debug/#configure-channel)[Configure runtime version](/eas-update/debug/#configure-runtime-version)[Map channel to branch](/eas-update/debug/#map-channel-to-branch)[Publish update](/eas-update/debug/#publish-update)[General strategies](/eas-update/debug/#general-strategies)[Use expo-dev-client](/eas-update/debug/#use-expo-dev-client)[In-app debugging](/eas-update/debug/#in-app-debugging)[Configuration issues](/eas-update/debug/#configuration-issues)[expo-updates configuration](/eas-update/debug/#expo-updates-configuration)[Configuration without EAS Build](/eas-update/debug/#configuration-without-eas-build)[Debugging EAS Update](/eas-update/debug/#debugging-eas-update)[In-app debugging](/eas-update/debug/#in-app-debugging-1)[Inspecting a build manually](/eas-update/debug/#inspecting-a-build-manually)[Inspecting manifests manually](/eas-update/debug/#inspecting-manifests-manually)[Viewing network requests](/eas-update/debug/#viewing-network-requests)[Runtime issues](/eas-update/debug/#runtime-issues)[Debugging of native code while loading the app through expo-updates](/eas-update/debug/#debugging-of-native-code-while-loading-the-app-through-expo-updates)[Publishing issues](/eas-update/debug/#publishing-issues)[Inspecting the latest update locally](/eas-update/debug/#inspecting-the-latest-update-locally)[Viewing all assets included in an update](/eas-update/debug/#viewing-all-assets-included-in-an-update)[Mitigation steps](/eas-update/debug/#mitigation-steps)[Re-publishing a previous update](/eas-update/debug/#re-publishing-a-previous-update)