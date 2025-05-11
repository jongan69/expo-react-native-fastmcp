Deploy updates - Expo Documentation

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

Deploy updates
==============

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/deployment.mdx)

Learn a simple but powerful process for safely deploying updates to your users.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/deployment.mdx)

---

When you have an app with multiple binary versions in production (this is common â users do not always stay up to date with your latest store release), it's important to understand what code is running on which versions and to be able to specifically target a particular version with a hotfix.

EAS Update provides "channels", "branches", and "runtime versions" to help you determine which app version to target, to help you with bookkeeping to understand the state of your deployments, and to support a variety of [deployment patterns](/eas-update/deployment-patterns).

What if my preferred release process isn't supported by EAS Update?

Release management is a large topic in software engineering, and everyone has a slightly different take on how they would like to do it. EAS Update is designed to support [a variety of different workflows](/eas-update/deployment-patterns), but this guide will focus on the simplest workflow that works for most apps. That said, there are some other workflows that may not work within the constraints of the EAS Update service. For example, each binary version must always point to a single channel, and you cannot dynamically update the channel.

As an escape hatch, you can host your own update service that is compatible with the [Expo Updates Protocol](/technical-specs/expo-updates-1) and point your `expo-updates` configuration to that service instead. The only concepts relevant to update selection that exist on the protocol level are "Runtime Version" and "Platform", and you are free to create your own concepts on top of those in the same way we built channels and branches. [Learn more about creating a custom expo-updates server](https://github.com/expo/custom-expo-updates-server).

A simple release process
------------------------

In this guide, we'll describe a simple but powerful release process that uses channels and runtime versions, and mostly ignores *branches*. This gives most of the benefits of EAS Update with a minimal amount of conceptual overhead. You can evolve this process to suit your needs as they arise, or move to [other deployment patterns](/eas-update/deployment-patterns).

Why ignore branches in this release process?

The most simple way to use EAS Update is to ignore the concept of "branches" and focus on "channels". Branches will still exist, but you will not have to interact with them directly to manage deployments. You can keep your channels pointed at a branch with the same name as the channel and think of them as a singular concept.

EAS Update branches were meant to map to Git branches and enable teams to publish changes from a Git branch directly to an EAS Update branch of the same name. This can be helpful for [previewing updates](/eas-update/develop-faster), but for many apps, this level of integration with Git is not required. Often, developers are only interested in being able to release hotfixes to a staging or production version of their app manually, and can run `eas update --channel staging` or `eas update --channel production`, when needed rather than managing branches to accomplish the same result.

Configuring your project
------------------------

Channels will indicate which environment the update targets (such as "production" or "staging"), and runtime versions will indicate the app version that the update will target (such as "1.0.0" or "1.0.1").

### Channel configuration

Run `eas update:configure` in your project if you haven't already.

If you use EAS Build, the default configuration that will be applied by the configure command, which is almost what we want to use here: each profile will point to a channel of the same name, so our production release of our app will point to the "production" channel. We only need to add a "staging" profile that points to the "staging" channel.

Example eas.json configuration

The following configuration is approximately what `eas update:configure` will generate for you if you haven't already configured your project.

```
{
  "build": {
    "production": {
      "channel": "production"
    },
    "staging": {
      "channel": "staging"
    },
    "preview": {
      "channel": "preview",
      "distribution": "internal"
    }
  }
}

```

If you do not use EAS Build, you will need to modify the channel used in your [native project configuration](/eas-update/getting-started#configure-the-update-channel). When you release to production, ensure you update the channel name in native config to "production", and when you release to staging, ensure you update the channel name in native config to "preview". It's worth noting that using EAS Build with EAS Update helps you get the best out of the product, but it is not required.

### Runtime version configuration

By default, `eas update:configure` will set `"runtimeVersion": { "policy": "appVersion" }` in your app config. This is the recommended configuration, it will ensure that the runtime version of your app is always the same as the app version, and you have a unique runtime version to target for every release of your app. In this case, the app version refers to the native version of your app that users will see on the app store, and it does not include the build number or version code. For example: `"1.0.0"` will be used as the runtime version, and not `"1.0.0(1)"` (where `1` is the build number or version code).

Example app.json configuration

```
{
  "expo": {
    "runtimeVersion": {
      "policy": "appVersion"
    }
  }
}

```

What about the fingerprint runtime version policy?

We hope that this will be the future of runtime version policies, but for now, we recommend using the `"appVersion"` policy. The `"fingerprint"` policy is experimental and not yet widely recommended.

Deploying previews
------------------

You can preview updates in your internal distribution release builds or in development builds. Using internal distribution instead of deploying to a store beta track reduces the friction of distributing the app to internal testers, and is suitable for cases where you want to, for example, share a build on every pull request or an early concept that you're working on.

### Internal distribution release builds

As explained above, preview builds will point to the "preview" channel. If you want multiple versions of the preview app distributed internally at any given time, you can change the channel name based on the feature name. For example, you might set your channel on your build to "preview-feature-a" when working on feature A, and then set it to "preview-feature-b" when working on feature B.

### Preview in development builds

Development builds can load updates from any channel, provided the runtime version is compatible. Learn more about this in [Previewing updates](/eas-update/develop-faster).

Deploying to staging
--------------------

Run `eas update --channel staging` to publish an update to staging. This will make your hotfix immediately available to users of staging builds with the targeted runtime version.

Your staging environment will be Google Play Beta or TestFlight â the "beta track" on respective app stores. You may alternatively use internal distribution, but deploying to a store beta track is generally recommended when you are staging code for a production release since users are able to access it without any knowledge of internal processes for distributing the app (while using internal distribution would require users to download the app from an expo.dev URL).

A common practice for creating staging builds is to always create one whenever you upload a production build to a store. This allows you to have a staging build with an identical runtime to the production build, which you can use to test your updates before rolling them out to production. With EAS Build, this means running `eas build --profile staging --auto-submit` every time you run `eas build --profile production --auto-submit`.

Deploying to production
-----------------------

Run `eas update --channel production` to bundle and push a new update to production. This will make your hotfix immediately available to production build users with the same runtime version.

If you have already published the fix to staging and verified it there, ensure that you are republishing from the same commit.

For this release process we recommend using identical environment variables and code signing configuration on staging as on production, to ensure that updates verified in staging work exactly the same in production. If do this, then you can `eas update:republish --destination-channel production` to promote the update rather than generating a new one. This will ensure the exact same bundle that you tested in staging is used in production.

Run `eas update --channel production` to publish an update to production. This will make your hotfix immediately available to users of production builds with the same runtime version.

### Runtime versions

When creating a new production build, we recommend incrementing your [app version](/build-reference/app-versions#app-versions) to ensure it has a unique runtime version for each release of your app.

### Gradually rolling out updates

Rollouts that leverage multiple branches can't be used with this workflow. We're working on a solution for this, but in the meantime, you will need to use a process similar to the [branch promotion flow](/eas-update/deployment-patterns#branch-promotion-flow) to incrementally roll out updates.

Learn more in [Rollouts](/eas-update/rollouts).

### Rolling back to a previous update version

If you've mistakenly published an update to any of your environments, you can run `eas update:rollback` initiate a rollback to a previous update.

Learn more in [Rollbacks](/eas-update/rollbacks).

Next steps
----------

* [Learn more about the Persistent staging release process](/eas-update/deployment-patterns#persistent-staging-flow), which is very similar to what is described here.
* [Explore using preview updates in development builds](/eas-update/develop-faster).

[Previous (EAS Update - Preview)

Github PR previews](/eas-update/github-actions)[Next (EAS Update - Deployment)

Downloading updates](/eas-update/download-updates)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/deployment.mdx)
* Last updated on November 14, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[A simple release process](/eas-update/deployment/#a-simple-release-process)[Configuring your project](/eas-update/deployment/#configuring-your-project)[Channel configuration](/eas-update/deployment/#channel-configuration)[Runtime version configuration](/eas-update/deployment/#runtime-version-configuration)[Deploying previews](/eas-update/deployment/#deploying-previews)[Internal distribution release builds](/eas-update/deployment/#internal-distribution-release-builds)[Preview in development builds](/eas-update/deployment/#preview-in-development-builds)[Deploying to staging](/eas-update/deployment/#deploying-to-staging)[Deploying to production](/eas-update/deployment/#deploying-to-production)[Runtime versions](/eas-update/deployment/#runtime-versions)[Gradually rolling out updates](/eas-update/deployment/#gradually-rolling-out-updates)[Rolling back to a previous update version](/eas-update/deployment/#rolling-back-to-a-previous-update-version)[Next steps](/eas-update/deployment/#next-steps)