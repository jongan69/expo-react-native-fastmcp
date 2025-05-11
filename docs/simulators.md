Build for iOS Simulators - Expo Documentation

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

Build for iOS Simulators
========================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/simulators.mdx)

Learn how to configure and install build for iOS simulators when using EAS Build.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/simulators.mdx)

---

Running a build of your app on an iOS Simulator is useful. You can configure the build profile and install the build automatically on the simulator. This provides a standalone (independent of Expo Go) version of the app running without needing to deploy to TestFlight or even having an Apple Developer account.

Configuring a profile to build for simulators
---------------------------------------------

To install a build of your app on an iOS Simulator, modify the build profile in [eas.json](/build/eas-json) and set the `ios.simulator` value to `true`:

eas.json

Copy

```
{
  "build": {
    "preview": {
      "ios": {
        "simulator": true
      }
    },
    "production": {}
  }
}

```

Now, execute the command as shown below to run the build:

Terminal

Copy

`-Â``eas build -p ios --profile preview`

Remember that a profile can be named whatever you like. In the above example, it is called `preview`. However, you can call it `local`, `simulator`, or whatever makes the most sense.

Installing build on the simulator
---------------------------------

> If you haven't installed or run the iOS Simulator before, follow the [iOS Simulator guide](/workflow/ios-simulator) before proceeding.

Once your build is completed, the CLI will prompt you to automatically download and install it on the iOS Simulator. When prompted, press `Y` to directly install it on the simulator.

In case you have multiple builds, you can also run the `eas build:run` command at any time to download a specific build and automatically install it on the iOS Simulator:

Terminal

Copy

`-Â``eas build:run -p ios`

The command also shows a list of available builds of your project. You can select the build to install on the simulator from this list. Each build in the list has a build ID, the time elapsed since the build creation, the build number, the version number, and the git commit information. The list also displays invalid builds if a project has any.

For example, the image below lists two previous builds of a project:

![Running eas build:run command shows a list of available builds in a project.](/static/images/eas-build/eas-build-run-on-ios.png)

When the build's installation is complete, it will appear on the home screen. If it's a development build, open a terminal window and start the development server by running the command `npx expo start`.

### Running the latest build

Pass the `--latest` flag to the `eas build:run` command to download and install the latest build on the iOS Simulator:

Terminal

Copy

`-Â``eas build:run -p ios --latest`

[Previous (EAS Build - Reference)

Build APKs for Android Emulators and devices](/build-reference/apk)[Next (EAS Build - Reference)

App version management](/build-reference/app-versions)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/simulators.mdx)
* Last updated on July 01, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Configuring a profile to build for simulators](/build-reference/simulators/#configuring-a-profile-to-build-for-simulators)[Installing build on the simulator](/build-reference/simulators/#installing-build-on-the-simulator)[Running the latest build](/build-reference/simulators/#running-the-latest-build)