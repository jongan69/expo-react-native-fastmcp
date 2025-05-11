Runtime versions and updates - Expo Documentation

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

[How it works](/eas-update/how-it-works)[Manage branches and channels](/eas-update/eas-cli)[Runtime versions](/eas-update/runtime-versions)

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

Runtime versions and updates
============================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/runtime-versions.mdx)

Learn about different runtime version policies and how they may suit your project.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/runtime-versions.mdx)

---

Runtime versions are a property that guarantees compatibility between a build's native code and an update. When a project is made into a build, the build will contain some native code that cannot be changed with an update. Therefore, an update must be compatible with a build's native code to run on the build.

To illustrate how builds and updates interact, take a look at the following diagram:

![Native and update layers diagram](/static/images/eas-update/layers.png)

Builds can be thought of as two layers: a native layer that's built into the app's binary, and an update layer, that is swappable with other compatible updates. This separation allows us to ship bug fixes to builds as long as the update with the bug fix can run on the native layer inside the build. The `"runtimeVersion"` property allows us to guarantee that an update is compatible with a specific build's native code.

Since updates must be compatible with a build's native code, any time native code is updated, we're required to make a new build before publishing an update. Some developers only update native code when upgrading to a new Expo SDK, while others may upgrade native code between builds or at other intervals. Below is an explanation of different situations and configurations that may suite your project.

Setting `"runtimeVersion"`
--------------------------

To make managing the `"runtimeVersion"` property easier between builds and updates, we've created policies that derive the runtime version from another piece of information already present in your project. If these policies do not match the development flow of a project, there's also an option to set the `"runtimeVersion"` manually.

### Runtime version policies

The available policies are documented in the [`expo-updates` library documentation](/versions/latest/sdk/updates#automatic-configuration-using-runtime-version-policies).

### Custom runtime version

You can also set a custom runtime version that meets the [runtime version formatting requirements](/versions/latest/config/app#runtimeversion):

```
{
  "expo": {
    "runtimeVersion": "1.0.0"
  }
}

```

This option is good for developers who want to manage the runtime version manually, separately from any other version numbers present in a project's app config. It gives the developer complete control over which updates are compatible with which builds.

### Platform-specific runtime version

You can also set runtime version per-platform, for example

```
{
  "expo": {
    "android": {
      "runtimeVersion": "1.0.0"
    }
  }
}

```

Or:

```
{
  "expo": {
    "android": {
      "runtimeVersion": {
        "policy": "appVersion"
      }
    }
  }
}

```

When both a top level runtime and a platform specific runtime are set, the platform specific one takes precedence.

Avoiding crashes with incompatible updates
------------------------------------------

The main issue that can arise when publishing updates is that the update could rely on native code that the build it's running on does not support. For instance, imagine we made a build with a runtime version of `"1.0.0"`. Then, we submitted that build to the app stores and released it to the public.

Later on, imagine that we developed an update that relied on a newly installed native library, like the `expo-in-app-purchases` library, and we did not update the `"runtimeVersion"` property, so that it is still `"1.0.0"`. If we published an update, the builds with the `"runtimeVersion"` of `"1.0.0"` would think the incoming update with the same runtime version was compatible and it would attempt to load the update. Since the update would make calls to code that does not exist inside the build, the app would crash.

There are a few ways to avoid crashes like this:

* Whenever we install or update native code, iterate the `"runtimeVersion"` property in the project's app config (app.json/app.config.js).
* Create a preview build of your app and load it on a test device. Then, publish the update to the "preview" branch to make sure it works as expected before publishing it to the project's production branch.

If this error does occur, then you can republish a previous known-good update, then ask users to delete the app and reinstall it.

In the future, the `expo-updates` library will prevent many instances of this from crashing the app. If we can detect this particular issue, we'll automatically roll back to a previous update instead of loading the bad update.

[Previous (EAS Update - Concepts)

Manage branches and channels](/eas-update/eas-cli)[Next (EAS Update - Troubleshooting)

Debugging](/eas-update/debug)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/runtime-versions.mdx)
* Last updated on October 07, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Setting "runtimeVersion"](/eas-update/runtime-versions/#setting-runtimeversion)[Runtime version policies](/eas-update/runtime-versions/#runtime-version-policies)[Custom runtime version](/eas-update/runtime-versions/#custom-runtime-version)[Platform-specific runtime version](/eas-update/runtime-versions/#platform-specific-runtime-version)[Avoiding crashes with incompatible updates](/eas-update/runtime-versions/#avoiding-crashes-with-incompatible-updates)