Android build process - Expo Documentation

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

Android build process
=====================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/android-builds.mdx)

Learn how an Android project is built on EAS Build.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/android-builds.mdx)

---

This page describes the process of building Android projects with EAS Build. You may want to read this if you are interested in the implementation details of the build service.

Build process
-------------

Let's take a closer look at the steps for building Android projects with EAS Build. We'll first run some steps on your local machine to prepare the project, and then we'll build the project on a remote service.

### Local steps

The first phase happens on your computer. EAS CLI is in charge of completing the following steps:

1. If `cli.requireCommit` is set to `true` in eas.json, check if the git index is clean - this means that there aren't any uncommitted changes. If it's not clean, EAS CLI will provide an option to commit local changes for you or abort the build process.
2. Prepare the credentials needed for the build unless `builds.android.PROFILE_NAME.withoutCredentials` is set to `true`.

   * Depending on the value of `builds.android.PROFILE_NAME.credentialsSource`, the credentials are obtained from either the local credentials.json file or from the EAS servers. If the `remote` mode is selected but no credentials exist yet, you're prompted to generate a new keystore.
3. Create a tarball containing a copy of the repository. Actual behavior depends on the [VCS workflow](https://expo.fyi/eas-vcs-workflow) you are using.
4. Upload the project tarball to a private AWS S3 bucket and send the build request to EAS Build.

### Remote steps

Next, this is what happens when EAS Build picks up your request:

1. Create a new Docker container for the build.

   * Every build gets its own fresh container with all build tools installed there (Java JDK, Android SDK, NDK, and so on).
2. Download the project tarball from a private AWS S3 bucket and unpack it.
3. [Create .npmrc](/build-reference/private-npm-packages) if `NPM_TOKEN` is set.
4. Run the `eas-build-pre-install` script from package.json if defined.
5. Run `npm install` in the project root (or `yarn install` if `yarn.lock` exists).
6. Run `npx expo-doctor` to diagnose potential issues with your project configuration.
7. Additional step for managed projects: Run `npx expo prebuild` to convert the project to a bare one. This step will use the versioned Expo CLI.
8. Restore a previously saved cache identified by the `cache.key` value in the [build profile](/build/eas-json).
9. Run the `eas-build-post-install` script from package.json if defined.
10. Restore the keystore (if it was included in the build request).
11. Inject the signing [configuration into build.gradle](/build-reference/android-builds#configuring-gradle).
12. Run `./gradlew COMMAND` in the android directory inside your project.

    * `COMMAND` is the command defined in your eas.json at `builds.android.PROFILE_NAME.gradleCommand`. It defaults to `:app:bundleRelease` which produces the AAB (Android App Bundle).
13. Deprecated: Run the `eas-build-pre-upload-artifacts` script from package.json if defined.
14. Store a cache of files and directories defined in the [build profile](/build/eas-json). Subsequent builds will restore this cache.
15. Upload the application archive to AWS S3.

    * The artifact path can be configured in eas.json at `builds.android.PROFILE_NAME.applicationArchivePath`. It defaults to `android/app/build/outputs/**/*.{apk,aab}`. We're using the [fast-glob](https://github.com/mrmlnc/fast-glob#pattern-syntax) package for pattern matching.
16. If the build was successful: run the `eas-build-on-success` script from package.json if defined.
17. If the build failed: run the `eas-build-on-error` script from package.json if defined.
18. Run the `eas-build-on-complete` script from package.json if defined. The `EAS_BUILD_STATUS` env variable is set to either `finished` or `errored`.
19. Upload the build artifacts archive to a private AWS S3 bucket if `buildArtifactPaths` is specified in the build profile.

Project auto-configuration
--------------------------

Every time you want to build a new Android app binary, we validate that the project is set up correctly so we can seamlessly run the build process on our servers. This mainly applies to bare projects, but similar steps are run when building managed projects.

### Android keystore

Android requires you to sign your application with a certificate. That certificate is stored in your keystore. The Google Play Store identifies applications based on the certificate. This means that if you lose your keystore, you may not be able to update your application in the store. However, with [Play App Signing](https://developer.android.com/studio/publish/app-signing#app-signing-google-play), you can mitigate the risk of losing your keystore.

Your application's keystore should be kept private. Under no circumstances should you check it in to your repository. Debug keystores are the only exception because we don't use them for uploading apps to the Google Play Store.

### Configuring Gradle

Your app binary needs to be signed with a keystore. Since we're building the project on a remote server, we had to come up with a way to provide Gradle with credentials which aren't, for security reasons, checked in to your repository. In one of the remote steps, we inject the signing configuration into your build.gradle. EAS Build creates the android/app/eas-build.gradle file with the following contents:

android/app/eas-build.gradle

Copy

```
// Build integration with EAS

import java.nio.file.Paths

android {
  signingConfigs {
    release {
      // This is necessary to avoid needing the user to define a release signing config manually
      // If no release config is defined, and this is not present, build for assembleRelease will crash
    }
  }

  buildTypes {
    release {
      // This is necessary to avoid needing the user to define a release build type manually
    }
    debug {
      // This is necessary to avoid needing the user to define a debug build type manually
    }
  }
}

tasks.whenTaskAdded {
  android.signingConfigs.release {
    def credentialsJson = rootProject.file("../credentials.json");
    def credentials = new groovy.json.JsonSlurper().parse(credentialsJson)
    def keystorePath = Paths.get(credentials.android.keystore.keystorePath);
    def storeFilePath = keystorePath.isAbsolute()
      ? keystorePath
      : rootProject.file("..").toPath().resolve(keystorePath);

    storeFile storeFilePath.toFile()
    storePassword credentials.android.keystore.keystorePassword
    keyAlias credentials.android.keystore.keyAlias
    if (credentials.android.keystore.containsKey("keyPassword")) {
      keyPassword credentials.android.keystore.keyPassword
    } else {
      // key password is required by Gradle, but PKCS keystores don't have one
      // using the keystore password seems to satisfy the requirement
      keyPassword credentials.android.keystore.keystorePassword
    }
  }

  android.buildTypes.release {
    signingConfig android.signingConfigs.release
  }

  android.buildTypes.debug {
    signingConfig android.signingConfigs.release
  }
}


```

The most important part is the `release` signing config. It's configured to read the keystore and passwords from the credentials.json file at the project root. Even though you're not required to create this file on your own, it's created and populated with your credentials by EAS Build before running the build.

This file is imported in android/app/build.gradle like this:

android/app/build.gradle

Copy

```
// ...

apply from: "./eas-build.gradle"

```

[Previous (EAS Build - Reference)

Cache dependencies](/build-reference/caching)[Next (EAS Build - Reference)

iOS build process](/build-reference/ios-builds)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/android-builds.mdx)
* Last updated on June 19, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Build process](/build-reference/android-builds/#build-process)[Local steps](/build-reference/android-builds/#local-steps)[Remote steps](/build-reference/android-builds/#remote-steps)[Project auto-configuration](/build-reference/android-builds/#project-auto-configuration)[Android keystore](/build-reference/android-builds/#android-keystore)[Configuring Gradle](/build-reference/android-builds/#configuring-gradle)