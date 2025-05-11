App stores best practices - Expo Documentation

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

App stores best practices
=========================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/distribution/app-stores.mdx)

Learn about the best practices when submitting an app to the app stores.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/distribution/app-stores.mdx)

---

This guide offers best practices for submitting your app to the app stores. To learn how to generate native binaries for submission, see [Create your first build](/build/setup).

> Disclaimer: Review guidelines and rules are updated frequently, and enforcement of various rules can sometimes be inconsistent. There is no guarantee that your particular project will be accepted by either platform, and you are ultimately responsible for your app's behavior. That said, you can re-submit your app as needed to address feedback from reviews.

[Versioning your app

Learn how to configure native runtime versions for your apps.](/build-reference/app-versions)
[App Store presence

Manage your Apple App Store metadata from the command line.](/eas/metadata)
[Permissions

Refine native permissions and system dialog messages by using app config.](/guides/permissions)
[App icons

App stores have strict rules for home screen icons.](/develop/user-interface/splash-screen-and-app-icon)
[Splash screen

Create a seamless loading experience using the splash screen API.](/develop/user-interface/splash-screen-and-app-icon)
[App store assets

Learn how to create screenshots and previews for your app's store pages.](/guides/store-assets)
[Localizing your app

Prepare versions of your app for different languages and regions.](/guides/localization)
[Apple: Review guidelines

Official Apple guide on preparing your app for App Store review.](https://developer.apple.com/distribute/app-review/)

Responsive design
-----------------

It's a good idea to test your app on a device or simulator with a small screen (for example, an iPhone SE) and a large screen (for example, an iPhone X). Ensure your components render the way you expect, no buttons are blocked, and all text fields are accessible.

Try your app on tablets in addition to handsets. Even if you have `ios.supportsTablet: false` configured, your app will still render at phone resolution on iPads and must be usable.

> Apple may reject your app if elements don't render properly on an iPad, even if your app doesn't target the iPad form factor. Be sure and test your app on an iPad (or iPad simulator).

Privacy policy
--------------

Starting October 3, 2018, all new iOS apps and app updates will be required to have a privacy policy to pass the App Store Review Guidelines.

### App privacy questions

Beginning December 8, 2020, new app submissions and updates are required to provide information about their privacy practices in App Store Connect. See [App privacy details on the App Store](https://developer.apple.com/app-store/app-privacy-details/) for more information.

Apple will ask you a series of questions when you submit the app. Depending on which libraries you use, your answers may vary. For example, if you use `expo-updates`, you will need to say Yes, we collect data from this app and then you will want to select Crash Data.

[Previous (Distribution)

Overview](/distribution/introduction)[Next (Distribution)

App transfers](/distribution/app-transfers)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/distribution/app-stores.mdx)
* Last updated on July 26, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Responsive design](/distribution/app-stores/#responsive-design)[Privacy policy](/distribution/app-stores/#privacy-policy)[App privacy questions](/distribution/app-stores/#app-privacy-questions)