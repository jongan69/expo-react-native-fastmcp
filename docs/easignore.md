Ignore files via .easignore - Expo Documentation

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

Ignore files via .easignore
===========================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/easignore.mdx)

Learn how to configure EAS to ignore unnecessary files during the build process.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/easignore.mdx)

---

A .easignore file defines which files [EAS](https://expo.dev/eas) should ignore when uploading your project to the [EAS Build](/build/introduction) servers.

> Ignoring unnecessary files can help reduce your app's archive size and upload time.

By default, the [EAS CLI](/build/setup#install-the-latest-eas-cli) refers to the [.gitignore](https://git-scm.com/docs/gitignore) file (if it exists) to determine which files to ignore. If you create a .easignore file, the EAS CLI prioritizes it over the .gitignore file. When creating a .easignore file, include all files and directories from your .gitignore file and add additional files you want to ignore.

1

Create a .easignore file in the root of your project.

2

Copy the content of the .gitignore file into the .easignore file. Then, add any files that are unnecessary for the build process.

.easignore

Copy

```
# Copy everything from your .gitignore file here

# Ignore files and directories that EAS Build doesn't need to build your app
/docs

# Ignore native directories (if you are using EAS Build)
/android
/ios

# Ignore test coverage reports
/coverage

```

If your project does not contain android and ios directories, [EAS Build will run Prebuild](/workflow/prebuild#usage-with-eas-build) to generate these native directories before compilation.

3

Save the file and trigger a new build.

Terminal

Copy

`-Â``eas build --platform ios --profile development`

You've successfully configured your .easignore file.

Adding files to your project upload with .easignore
---------------------------------------------------

In addition to ignoring additional files beyond what is in your gitignore file, you can also use the .easignore file to include files with your EAS Build upload that are not committed to source control. This is useful if you have custom scripts that generate temporary files needed for your build process just before the build. To upload a file not in source control to EAS Build, add it to the .easignore file with a `!` prefix, along with the rest of your .gitignore contents. The `!` prefixed file should be last, so it takes precedence over any prior rules that would ignore it.

.easignore

Copy

```
# Copy everything from your .gitignore file here

/android
/ios

# Include a file not in source control
!temp_file.json

```

[Previous (EAS Build - Reference)

iOS App Extensions](/build-reference/app-extensions)[Next (EAS Build - Reference)

Limitations](/build-reference/limitations)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/easignore.mdx)
* Last updated on April 02, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).