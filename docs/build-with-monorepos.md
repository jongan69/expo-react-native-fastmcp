Set up EAS Build with a monorepo - Expo Documentation

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

Set up EAS Build with a monorepo
================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/build-with-monorepos.mdx)

Learn how to set up EAS Build with a monorepo.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/build-with-monorepos.mdx)

---

To set up EAS Build with a monorepo, you need to follow the standard process as described below:

* Run all EAS CLI commands from the root of the app directory. For example, if your project exists inside your git repository at apps/my-app, then run `eas build` from there.
* All files related to EAS Build, such as eas.json and credentials.json, should be in the root of the app directory. If you have multiple apps that use EAS Build in your monorepo, each app directory will have its own copy of these files.
* If you are building a managed project in a monorepo, see [Working with Monorepos](/guides/monorepos) guide.
* If your project needs additional setup beyond what is provided, add a `postinstall` step to package.json in your project that builds all necessary dependencies in other workspaces. For example:

package.json

Copy

```
{
  "scripts": {
    "postinstall": "cd ../.. && yarn build"
  }
}

```

[Previous (EAS Build - Reference)

Using npm cache with Yarn 1 (Classic)](/build-reference/npm-cache-with-yarn)[Next (EAS Build - Reference)

Build APKs for Android Emulators and devices](/build-reference/apk)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/build-with-monorepos.mdx)
* Last updated on June 10, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).