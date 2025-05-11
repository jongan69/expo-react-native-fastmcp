Build lifecycle hooks - Expo Documentation

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

Build lifecycle hooks
=====================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/npm-hooks.mdx)

Learn how to use the EAS Build lifecycle hooks with npm to customize your build process.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/npm-hooks.mdx)

---

EAS Build lifecycle npm hooks allows you to customize your build process by running scripts before or after the build process.

> For better understanding, see the [Android build process](/build-reference/android-builds) and the [iOS build process](/build-reference/ios-builds).

> The lifecycle hooks are not executed by the build process in [custom builds](/custom-builds/get-started). They need to be manually extracted and called by the build steps during the process.

EAS Build lifecycle hooks
-------------------------

There are six EAS Build lifecycle npm hooks available. To use, them, you can set them in your package.json.

| Build Lifecycle npm hook | Description |
| --- | --- |
| `eas-build-pre-install` | Executed before EAS Build runs `npm install`. |
| `eas-build-post-install` | The behavior depends on the platform and project type.     For Android, runs once after the following commands have all completed: `npm install` and `npx expo prebuild` (if needed).   For iOS, runs once after the following commands have all completed: `npm install`, `npx expo prebuild` (if needed), and `pod install`. |
| `eas-build-on-success` | This hook is triggered at the end of the build process if the build was successful. |
| `eas-build-on-error` | This hook is triggered at the end of the build process if the build failed. |
| `eas-build-on-complete` | This hook is triggered at the end of the build process. You can check the build's status with the `EAS_BUILD_STATUS` environment variable. It's either `finished` or `errored`. |
| `eas-build-on-cancel` | This hook is triggered if the build is canceled. |

An example of how a package.json can look when using one or more lifecycle hooks:

package.json

Copy

```
{
  "name": "my-app",
  "scripts": {
    "eas-build-pre-install": "echo 123",
    "eas-build-post-install": "echo 456",
    "eas-build-on-success": "echo 789",
    "eas-build-on-error": "echo 012",
    "eas-build-on-cancel": "echo 345",
    "start": "expo start",
    "test": "jest"
  },
  "dependencies": {
    "expo": "51.0.0"
    %%placeholder-start%%... %%placeholder-end%%
  }
}

```

Platform-specific hook behavior
-------------------------------

To run a script (or some part of a script) only for Android or iOS builds, you can fork the behavior depending on the platform within the script. See the following common examples to do this through a shell script or a Node script.

### Examples

#### package.json and shell script

package.json

Copy

```
{
  "name": "my-app",
  "scripts": {
    "eas-build-pre-install": "./pre-install",
    "start": "expo start"
    %%placeholder-start%%... %%placeholder-end%%
  },
  "dependencies": {
    %%placeholder-start%%... %%placeholder-end%%
  }
}

```

pre-install

Copy

```
#!/bin/bash

# This is a file called "pre-install" in the root of the project

if [[ "$EAS_BUILD_PLATFORM" == "android" ]]; then
  echo "Run commands for Android builds here"
elif [[ "$EAS_BUILD_PLATFORM" == "ios" ]]; then
  echo "Run commands for iOS builds here"
fi

```

Example: Pre-install script that installs `git-lfs` on macOS workers

The following script installs [`git-lfs`](https://git-lfs.com/) if it is not yet installed. This is useful in some cases where `git-lfs` is required to install certain CocoaPods.

pre-install

Copy

```
if [[ "$EAS_BUILD_PLATFORM" == "ios" ]]; then
  if brew list git-lfs > /dev/null 2>&1; then
    echo "=====> git-lfs is already installed."
  else
    echo "=====> Installing git-lfs"
    HOMEBREW_NO_AUTO_UPDATE=1 brew install git-lfs
    git lfs install
  fi
fi

```

#### package.json and Node script

package.json

Copy

```
{
  "name": "my-app",
  "scripts": {
    "eas-build-pre-install": "node pre-install.js",
    "start": "expo start"
    // ...
  },
  "dependencies": {
    // ...
  }
}

```

pre-install.js

Copy

```
// Create a file called "pre-install.js" at the root of the project

if (process.env.EAS_BUILD_PLATFORM === 'android') {
  console.log('Run commands for Android builds here');
} else if (process.env.EAS_BUILD_PLATFORM === 'ios') {
  console.log('Run commands for iOS builds here');
}

```

[Previous (EAS Build - Custom builds)

TypeScript functions](/custom-builds/functions)[Next (EAS Build - Reference)

Using private npm packages](/build-reference/private-npm-packages)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/npm-hooks.mdx)
* Last updated on September 01, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[EAS Build lifecycle hooks](/build-reference/npm-hooks/#eas-build-lifecycle-hooks)[Platform-specific hook behavior](/build-reference/npm-hooks/#platform-specific-hook-behavior)[Examples](/build-reference/npm-hooks/#examples)[package.json and shell script](/build-reference/npm-hooks/#packagejson-and-shell-script)[package.json and Node script](/build-reference/npm-hooks/#packagejson-and-node-script)