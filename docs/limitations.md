EAS Build Limitations - Expo Documentation

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

[Build lifecycle hooks](/build-reference/npm-hooks)[Using private npm packages](/build-reference/private-npm-packages)[Git submodules](/build-reference/git-submodules)[Using npm cache with Yarn 1 (Classic)](/build-reference/npm-cache-with-yarn)[Set up EAS Build with a monorepo](/build-reference/build-with-monorepos)[Build APKs for Android Emulators and devices](/build-reference/apk)[Build for iOS Simulators](/build-reference/simulators)[App version management](/build-reference/app-versions)[Troubleshoot build errors and crashes](/build-reference/troubleshooting)[Install app variants on the same device](/build-reference/variants)[iOS capabilities](/build-reference/ios-capabilities)[Run EAS Build locally](/build-reference/local-builds)[Cache dependencies](/build-reference/caching)[Android build process](/build-reference/android-builds)[iOS build process](/build-reference/ios-builds)[Configuration process](/build-reference/build-configuration)[Server infrastructure](/build-reference/infrastructure)[iOS App Extensions](/build-reference/app-extensions)[Ignore files via .easignore](/build-reference/easignore)[Limitations](/build-reference/limitations)

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

EAS Build Limitations
=====================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/limitations.mdx)

Learn about the current limitations of EAS Build.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/limitations.mdx)

---

EAS Build is designed to work for any React Native project. However, it is good to be aware of certain limitations that we plan to address since they could prevent you from being able to use the service for your applications or might cause an inconvenience.

Fixed memory and CPU limits on build worker servers
---------------------------------------------------

The resources available might be insufficient to build your app if your build process requires a significant amount of memory. In this case, consider using a [`large` resource class](/eas/json#resourceclass) in the eas.json. See [Android-specific resource class](/build-reference/infrastructure#android-build-server-configurations) and [iOS-specific resource class](/build-reference/infrastructure#ios-build-server-configurations).

See [Server infrastructure reference](/build-reference/infrastructure) for more information. It contains the most up-to-date information about the current specifications of the Android (Ubuntu) and iOS (macOS) build servers.

Limited dependency caching
--------------------------

Build jobs for Android install npm and Maven dependencies from a local cache. Build jobs for iOS install npm dependencies from a local cache, and CocoaPods artifacts from a cache server.

Intermediate artifacts like node\_modules directories are not cached and restored (for example, based on package-lock.json or yarn.lock), but if you commit them to your Git repository then they will be uploaded to build servers.

See [dependency caching](/build-reference/caching) for more information.

Maximum build duration of 2 hours
---------------------------------

If your build takes longer than 2 hours to run, it will be canceled. This limit is lower on the free plan, and the limit is subject to change in the future.

Maximum number of pending builds is 50 per platform per account
---------------------------------------------------------------

If you have more than 50 builds pending for a platform, new builds will be rejected until the number of pending builds drops below the limit.

Yarn workspaces is recommended for monorepos
--------------------------------------------

> Note: Official guidance for package managers other than Yarn is limited.

While you likely can have success using other monorepo tools like Nx if you are willing to dig in and understand the tooling and get your hands dirty, the Expo team will be unable to provide support and guidance on those tools. We recommend using [Yarn Workspaces](https://yarnpkg.com/en/docs/workspaces) because it is the only monorepo tool that we provide first-class integration with at the moment.

Get notified about changes
--------------------------

To be notified as progress is made on these items, you can subscribe to the EAS newsletter on [expo.dev/eas](https://expo.dev/eas).

[Previous (EAS Build - Reference)

Ignore files via .easignore](/build-reference/easignore)[Next (EAS Hosting)

Introduction](/eas/hosting/introduction)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/limitations.mdx)
* Last updated on January 28, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Fixed memory and CPU limits on build worker servers](/build-reference/limitations/#fixed-memory-and-cpu-limits-on-build-worker-servers)[Limited dependency caching](/build-reference/limitations/#limited-dependency-caching)[Maximum build duration of 2 hours](/build-reference/limitations/#maximum-build-duration-of-2-hours)[Maximum number of pending builds is 50 per platform per account](/build-reference/limitations/#maximum-number-of-pending-builds-is-50-per-platform-per-account)[Yarn workspaces is recommended for monorepos](/build-reference/limitations/#yarn-workspaces-is-recommended-for-monorepos)[Get notified about changes](/build-reference/limitations/#get-notified-about-changes)