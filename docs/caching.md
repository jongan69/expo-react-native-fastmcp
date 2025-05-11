Cache dependencies - Expo Documentation

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

Cache dependencies
==================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/caching.mdx)

Learn how to speed up your builds by caching dependencies.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/caching.mdx)

---

Before a build job can begin compiling your project, all project dependencies need to be available on disk. The longer it takes to acquire the dependencies, the more you need to wait for your build to complete â so caching dependencies is an important part of speeding up your builds.

> We're actively working on improving caching and other aspects of the build process to make builds reliably fast.

Custom caching
--------------

The `cache` field on build profiles in [eas.json](/build/eas-json) can be used to configure caching for specific files and directories. Specified files will be saved to persistent storage after a successful build and restored on subsequent builds after the JavaScript dependencies are installed. Restoring does not overwrite existing files. Changing the `cache.key` value will invalidate the cache. Changing any other property of the `cache` object will also invalidate the cache.

JavaScript dependencies
-----------------------

EAS Build runs an npm cache server that can speed up downloading JavaScript dependencies for your build jobs. By default, projects using npm or Yarn 2+ will use the cache. However, Yarn 1 (Classic) requires that you apply this [workaround](/build-reference/npm-cache-with-yarn) to use the cache in your project's package.json.

To disable using our npm cache server for your builds set the `EAS_BUILD_DISABLE_NPM_CACHE` env variable value to `"1"` in eas.json.

eas.json

Copy

```
{
  "build": {
    "production": {
      "env": {
        "EAS_BUILD_DISABLE_NPM_CACHE": "1"
        %%placeholder-start%%... %%placeholder-end%%
      }
      %%placeholder-start%%... %%placeholder-end%%
    }
    %%placeholder-start%%... %%placeholder-end%%
  }
  %%placeholder-start%%... %%placeholder-end%%
}

```

Android dependencies
--------------------

EAS Build runs a Maven cache server that can speed up downloading Android dependencies for your build jobs.

Currently, we are caching:

* `maven-central` - <https://repo1.maven.org/maven2/>
* `google` - <https://maven.google.com/>
* `jcenter` - <https://jcenter.bintray.com/>
* `plugins` - <https://plugins.gradle.org/m2/>

To disable using our Maven cache server for your builds set the `EAS_BUILD_DISABLE_MAVEN_CACHE` env variable value to `"1"` in eas.json.

eas.json

Copy

```
{
  "build": {
    "production": {
      "env": {
        "EAS_BUILD_DISABLE_MAVEN_CACHE": "1"
        %%placeholder-start%%... %%placeholder-end%%
      }
      %%placeholder-start%%... %%placeholder-end%%
    }
    %%placeholder-start%%... %%placeholder-end%%
  }
  %%placeholder-start%%... %%placeholder-end%%
}

```

iOS dependencies
----------------

EAS Build serves most CocoaPods artifacts from a cache server. This improves the consistency of `pod install` times and generally improves speed. The cache will be bypassed automatically if you provide your own .netrc or .curlrc files.

To disable using our CocoaPods cache server for your builds set the `EAS_BUILD_DISABLE_COCOAPODS_CACHE` env variable value to `"1"` in eas.json.

eas.json

Copy

```
{
  "build": {
    "production": {
      "env": {
        "EAS_BUILD_DISABLE_COCOAPODS_CACHE": "1"
        %%placeholder-start%%... %%placeholder-end%%
      }
      %%placeholder-start%%... %%placeholder-end%%
    }
    %%placeholder-start%%... %%placeholder-end%%
  }
  %%placeholder-start%%... %%placeholder-end%%
}

```

It is typical to not have your project Podfile.lock committed to source control when using [prebuild](/workflow/prebuild) to generate your ios directory [remotely at build time](/build-reference/ios-builds).
It can be useful to cache your Podfile.lock to have deterministic builds, but the tradeoff in this case is that, because you don't use the lockfile during local development, your ability to determine when a change is needed and to update specific dependencies is limited.
If you cache this file, you may occasionally end up with build errors that require clearing the cache.
To cache Podfile.lock, add ./ios/Podfile.lock to the `cache.paths` list in your build profile in eas.json.

eas.json

Copy

```
{
  "build": {
    "production": {
      "cache": {
        "paths": ["./ios/Podfile.lock"]
        %%placeholder-start%%... %%placeholder-end%%
      }
      %%placeholder-start%%... %%placeholder-end%%
    }
    %%placeholder-start%%... %%placeholder-end%%
  }
  %%placeholder-start%%... %%placeholder-end%%
}

```

[Previous (EAS Build - Reference)

Run EAS Build locally](/build-reference/local-builds)[Next (EAS Build - Reference)

Android build process](/build-reference/android-builds)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/caching.mdx)
* Last updated on December 05, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Custom caching](/build-reference/caching/#custom-caching)[JavaScript dependencies](/build-reference/caching/#javascript-dependencies)[Android dependencies](/build-reference/caching/#android-dependencies)[iOS dependencies](/build-reference/caching/#ios-dependencies)