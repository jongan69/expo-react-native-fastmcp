Run EAS Build locally with local flag - Expo Documentation

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

Run EAS Build locally with local flag
=====================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/local-builds.mdx)

Learn how to use EAS Build locally on your machine or a custom infrastructure using the --local flag.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/local-builds.mdx)

---

You can run the same build process that is typically run on the EAS Build servers directly on your machine by using the `eas build --local` flag. This is a useful way to debug build failures that are happening on your cloud builds, which you may not be able to reproduce without running the same set of steps.

Terminal

`-Â``eas build --platform android --local`

`# or`

`-Â``eas build --platform ios --local`

Prerequisites
-------------

You need to be authenticated with Expo:

* Run `eas login`
* Alternatively, set `EXPO_TOKEN` [using token-based authentication](/accounts/programmatic-access)

Use cases for local builds
--------------------------

* [Debugging](/build-reference/local-builds#use-local-builds-for-debugging) build failures on EAS servers.
* Company policies that restrict the use of third-party CI/CD services. With local builds, the entire process runs on your infrastructure and the only communication with EAS servers is:
  + to make sure project `@account/slug` exists
  + if you are using managed credentials to download them

Use local builds for debugging
------------------------------

If you encounter build failures on EAS servers and you're unable to determine the cause from inspecting the logs, you may find it helpful to debug the issue locally. To simplify that process we support several environment variables to configure the local build process.

* `EAS_LOCAL_BUILD_SKIP_CLEANUP=1` - Set this to disable cleaning up the working directory after the build process is finished.
* `EAS_LOCAL_BUILD_WORKINGDIR` - Specify the working directory for the build process, by default it's somewhere (it's platform dependent) in /tmp directory.
* `EAS_LOCAL_BUILD_ARTIFACTS_DIR` - The directory where artifacts are copied after a successful build. By default, these files are copied to the current directory, which may be undesirable if you are running many consecutive builds.

If you use `EAS_LOCAL_BUILD_SKIP_CLEANUP` and `EAS_LOCAL_BUILD_WORKINGDIR` for iOS builds you should be able to inspect the contents of the `logs` subdirectory of the working directory to read your Xcode logs.

Limitations
-----------

Some of the options available for cloud builds are not available locally. Limitations you should be aware of:

* You can only build for a specific platform (option `all` is disabled).
* Customizing versions of software is not supported, fields `node`, `yarn`, `fastlane`, `cocoapods`, `ndk`, `image` in eas.json are ignored.
* Caching is not supported.
* EAS environment variables with ["Secret" visibility](/eas/environment-variables#visibility-settings-for-environment-variables) are not supported (set them in your local environment instead).
* You are responsible for making sure that the environment has all the necessary tools installed:
  + Node.js/Yarn/npm
  + fastlane (iOS only)
  + CocoaPods (iOS only)
  + Android SDK and NDK
* On Windows, you can use [WSL](https://docs.microsoft.com/en-us/windows/wsl/install) for local EAS Builds. However, we do not officially test against this platform and do not support Windows for local builds (macOS and Linux are supported).

App compilation for development and production builds locally
-------------------------------------------------------------

To compile your app locally for development with Expo CLI, use `npx expo run:android` or `npx expo run:ios` commands instead. If you use [Continuous Native Generation](/workflow/continuous-native-generation), you can also run [prebuild](/workflow/prebuild) to generate your android and ios directories and then proceed to open the projects in the respective IDEs and build them like any native project. For more details, see:

[Local app development

Learn how to compile and build your Expo app locally.](/guides/local-app-development)

To create a production build locally, you need Android Studio and Xcode installed on your computer. See the following guide for more information:

[Create a production build locally

Learn how to create a production build for your Expo app locally on your computer.](/guides/local-app-production)

With any of the above approaches, you'll be following procedures which are different from creating a build on the cloud with EAS Build â that is what the `eas build --local` flag is for.

[Previous (EAS Build - Reference)

iOS capabilities](/build-reference/ios-capabilities)[Next (EAS Build - Reference)

Cache dependencies](/build-reference/caching)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/local-builds.mdx)
* Last updated on April 02, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Prerequisites](/build-reference/local-builds/#prerequisites)[Use cases for local builds](/build-reference/local-builds/#use-cases-for-local-builds)[Use local builds for debugging](/build-reference/local-builds/#use-local-builds-for-debugging)[Limitations](/build-reference/local-builds/#limitations)[App compilation for development and production builds locally](/build-reference/local-builds/#app-compilation-for-development-and-production-builds-locally)