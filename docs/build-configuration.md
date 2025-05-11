Build configuration process - Expo Documentation

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

Build configuration process
===========================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/build-configuration.mdx)

Learn how EAS CLI configures a project for EAS Build.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/build-configuration.mdx)

---

In this guide, you will learn what happens when EAS CLI configures your project with `eas build:configure` (or `eas build`, which runs this same process if the project is not yet configured).

EAS CLI performs the following steps when configuring your project:

1

Ask you about the platform(s) to configure
------------------------------------------

When you run the command for the first time, it will initialize your EAS project and ask you to select the platform(s) you want to configure. If you only want to use EAS Build for a single platform, that's fine. If you change your mind, you can come back and configure the other later.

![Terminal running eas build command with platform Android and iOS options available](/static/images/eas-build/configure/01-configure-platform.png)

2

Create eas.json
---------------

The command will create an eas.json file in the root directory with the default configuration. It looks something like this:

eas.json

Copy

```
{
  "build": {
    "development": {
      "developmentClient": true,
      "distribution": "internal"
    },
    "preview": {
      "distribution": "internal"
    },
    "production": {}
  }
}

```

If you have a bare project, it will look a bit different.

This is your EAS Build configuration. It defines three build profiles named `"development"`, `"preview"`, and `"production"` (you can have multiple build profiles like `"production"`, `"debug"`, `"testing"`, and so on) for each platform. If you want to learn more about eas.json see the [Configuration with eas.json](/build/eas-json) page.

3

Configure the project
---------------------

This step varies depending on the project type you have.

3.1

### Initialization complete

This completes the initialization of your project to be compatible with EAS Build.

![Initialization step complete prompt in eas build:configure](/static/images/eas-build/configure/02-initialization-complete.png)

3.2

### Expo project

If you haven't configured your app.json with `android.package` and/or `ios.bundleIdentifier` yet, EAS CLI will prompt you to specify them when you create your first build.

* `android.package` will be used as the Android application ID which is used to identify your app on the Google Play Store
* `ios.bundleIdentifier` will be used to identify you app on the Apple App Store

![Application identifier prompts in eas build:configure](/static/images/eas-build/configure/03-configure-app-ids.png)

In the example above, the `eas build --platform android` command prompts to set the Android application ID. If you run the command with `--platform ios`, it will prompt you to set the iOS bundle identifier.

3.3

### Bare React Native project

There are no additional steps for bare projects.

4

Next steps
----------

That's all there is to configuring a project to be compatible with EAS Build. There is one more step, if you set `cli.requireCommit` to `true` in your eas.json â you'll be prompted to commit all the changes we made for you. You can choose to review them before committing, and you can either specify the git commit message or use a default message.

[Previous (EAS Build - Reference)

iOS build process](/build-reference/ios-builds)[Next (EAS Build - Reference)

Server infrastructure](/build-reference/infrastructure)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/build-configuration.mdx)
* Last updated on February 06, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Ask you about the platform(s) to configure](/build-reference/build-configuration/#ask-you-about-the-platforms-to-configure)[Create eas.json](/build-reference/build-configuration/#create-easjson)[Configure the project](/build-reference/build-configuration/#configure-the-project)[Initialization complete](/build-reference/build-configuration/#initialization-complete)[Expo project](/build-reference/build-configuration/#expo-project)[Bare React Native project](/build-reference/build-configuration/#bare-react-native-project)[Next steps](/build-reference/build-configuration/#next-steps)