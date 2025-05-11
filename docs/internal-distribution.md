Internal distribution - Expo Documentation

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

Internal distribution
=====================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build/internal-distribution.mdx)

Learn how EAS Build provides shareable URLs for your builds with your team for internal distribution.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build/internal-distribution.mdx)

---

Setting up an internal distribution build only takes a few minutes with EAS Build and provides a streamlined way to share your app with your team and other testers for feedback. It does this by providing a URL that allows them to install the app directly to their device. If you are not sure yet if you want to use this approach and want to learn about all of the options available for distributing your app internally, refer to the [overview of distribution apps for review](/review/overview) guide.

Using internal distribution
---------------------------

To configure a build profile for internal distribution, set `"distribution": "internal"` on it. When you set this configuration, it has the following effects on the build profile:

* Android: The default behavior for the `gradleCommand` will change to generate an APK instead of an AAB. If you have specified a custom `gradleCommand`, then make sure that it [produces an APK](/build-reference/apk#configuring-a-profile-to-build-apks), or it won't be directly installable on an Android device. Additionally, EAS Build will generate a new Android keystore for signing the APK, or it will use an existing one if the package name is the same as your [development build](/develop/development-builds/introduction).
* iOS: Builds using this profile will use either [ad hoc or enterprise provisioning](/build/internal-distribution#overview-of-distribution-mechanisms). When using ad hoc provisioning, EAS Build will generate a provisioning profile containing an allow-list of device UDIDs, and only those devices in the list at build time will be able to install it. You can add a device by running `eas device:create` and creating a new build.
* By default, internal distribution build URLs are available to anybody with the URL, and each is identified by a 32 character UUID. If you would like to require sign-in to an authorized Expo account to access these builds, you can disable the Unauthenticated access to internal builds option in your [project settings](https://expo.dev/accounts/%5Baccount%5D/projects/%5Bproject%5D/settings).

See the tutorial on Internal distribution with EAS Build below for more information on how to configure, create, and install a build:

[Create and share internal distribution build

Complete step-by-step guide to setting up and sharing internal distribution builds with EAS Build.](/tutorial/eas/internal-distribution-builds)

### Automation on CI (optional)

It's possible to run internal distribution builds non-interactively in CI using the `--non-interactive` flag. However, if you are using ad hoc provisioning on iOS you will not be able to add new devices to your provisioning profile when using this flag. After registering a device through `eas device:create`, you need to run `eas build` interactively and authenticate with Apple in order for EAS to add the device to your provisioning profile. [Learn more about triggering builds from CI](/build/building-on-ci).

### Managing devices

You can see any devices registered via `eas device:create` by running:

Terminal

Copy

`# List devices registered for ad hoc provisioning`

`-Â``eas device:list`

Devices registered with Expo for ad hoc provisioning will appear on your Apple Developer Portal after they are used to generate a provisioning profile for a new internal build with EAS Build or to [resign an existing build](/app-signing/app-credentials#re-signing-new-credentials) with `eas build:resign`.

#### Remove devices

If a device is no longer in use, it can be removed from this list by running:

Terminal

Copy

`# Delete devices from your Expo account, optionally disable them on the Apple Developer Portal`

`-Â``eas device:delete`

This command will also prompt you to disable the device on the Apple Developer Portal. Disabled
devices still count against [Apple's limit of 100
devices](https://developer.apple.com/support/account/#:~:text=Resetting%20your%20device%20list%20annually)
for ad hoc distribution per app.

#### Rename devices

Devices added via the website URL/QR code will default to displaying their UDID when selecting them for an EAS Build. You can assign friendly names to your devices with the following command:

Terminal

Copy

`# Rename devices on Expo and the Apple Developer Portal`

`-Â``eas device:rename`

Overview of distribution mechanisms
-----------------------------------

The following are the different mechanisms for distributing your app to devices supported by internal distribution.

Android: Build and distribute an APK

To share your app to Android devices, you must build an APK (Android application package file) of your project. APKs can be installed directly to an Android device over USB, by downloading the file over the web or through an email or chat app, once the user accepts the security warning for installing an app that has not gone through Play Store review. AAB (Android app bundle) binaries of your app must be distributed through the Play Store.

iOS: Ad Hoc distribution

Apple offers [ad hoc provisioning profiles](https://help.apple.com/xcode/mac/current/#/dev7ccaf4d3c) to distribute your app to test devices once they have been registered
to your Apple Developer account. This method requires a paid Apple Developer account and that account will only be able to use this method to distribute to at most 100 iPhones per year.

You will need to know the UDID (Unique Device Identifier) of each device that will install your app, which may be challenging if you try to share with someone who is not a developer. Adding a new device will require a rebuild of your app or [re-signing the build with new credentials](/app-signing/app-credentials#re-signing-new-credentials).

Setting up Ad Hoc certificates correctly can be intimidating if you haven't done it before and tedious even if you have. If you're using [EAS Build](/build/internal-distribution#internal-distribution-with-eas-build), which is optimized for Expo and React Native projects, we'll handle the time-consuming parts of setting up Ad Hoc credentials for you.

iOS: Enterprise distribution

If your app is only intended for internal use by employees of a large organization and cannot be distributed through the App Store, you should use Enterprise distribution. Unlike with Ad Hoc Distribution, the number of devices that can install your app is unlimited, and you do not need to manage each device's UDID. Often these apps will be distributed to end users through a mobile device management (MDM) solution. Enterprise Distribution requires membership in the [Apple Developer Enterprise Program](https://developer.apple.com/programs/enterprise/). Organizations joining the Enterprise Program must meet additional requirements beyond what is required for App Store distribution.

[Previous (EAS Build)

Configure with eas.json](/build/eas-json)[Next (EAS Build)

Automate submissions](/build/automate-submissions)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build/internal-distribution.mdx)
* Last updated on May 02, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Using internal distribution](/build/internal-distribution/#using-internal-distribution)[Automation on CI (optional)](/build/internal-distribution/#automation-on-ci-optional)[Managing devices](/build/internal-distribution/#managing-devices)[Overview of distribution mechanisms](/build/internal-distribution/#overview-of-distribution-mechanisms)