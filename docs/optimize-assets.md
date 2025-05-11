Optimize assets for EAS Update - Expo Documentation

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

[Deploy updates](/eas-update/deployment)[Downloading updates](/eas-update/download-updates)[Rollouts](/eas-update/rollouts)[Rollbacks](/eas-update/rollbacks)[Optimize assets](/eas-update/optimize-assets)[Continuous deployment](/eas-update/continuous-deployment)[Alternative deployment patterns](/eas-update/deployment-patterns)

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

Optimize assets for EAS Update
==============================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/optimize-assets.mdx)

Learn how EAS Update downloads assets and how to optimize them for download size.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/optimize-assets.mdx)

---

> The new [asset selection feature](/eas-update/asset-selection) can greatly reduce the total number and size of downloaded assets.

When an app finds a new update, it downloads a manifest and then downloads any new or updated assets so that it can run the update. The process is as follows:

![Update download timeline](/static/images/eas-update/process.png)

Many users running Android and iOS apps are using mobile connections that are not as consistent or fast as when they are using Wi-Fi, so it's important that the assets shipped as a part of an update are as small as possible.

Code assets
-----------

When publishing an update, EAS CLI runs Expo CLI to bundle the project into an update. The update will appear in our project's dist directory.

In dist/bundles, we can see the size of the index.android.js and index.ios.js files that will be part of the Android and iOS updates, respectively. Note that these are uncompressed file sizes; EAS Update uses Brotli and gzip compression, which can significantly reduce download sizes. Nevertheless, these files will be downloaded to a user's device when getting the new update if the device has not downloaded them before. Making these file sizes as small as possible helps end-users download updates quickly.

Image assets
------------

App users will have to download any new images or other assets when they detect a new update if those assets are not already a part of their build. You can view all the assets uploaded to EAS servers in dist/assets. The assets there are hashed with their extensions removed, so it is difficult to know what assets are there. To see a pretty-printed list of assets, we can run:

Terminal

Copy

`-Â``npx expo export`

### Optimizing image assets

To manually optimize image assets in your project, you can use the `npx expo-optimize` command. It uses [sharp](https://sharp.pixelplumbing.com/) library to compress images.

Terminal

Copy

`-Â``npx expo-optimize`

After running the command, all image assets are compressed except the ones that are already optimized. You can adjust the compression quality by including the `--quality [number]` option with the command. For example, to compress to 90%, run:

Terminal

Copy

`-Â``npx expo-optimize --quality 90`

### Other manual optimization methods

To optimize images and videos manually, see [Assets](/develop/user-interface/assets#manual-optimization-methods) for more information.

Ensuring assets are included in updates
---------------------------------------

When you publish an update, EAS will upload your assets to the CDN so that they may be fetched when users run your app. However, for assets to be uploaded to the CDN, they must be explicitly required somewhere in your application's code. Conditionally requiring assets will result in the bundler being unable to detect them, and they will not be uploaded when you publish your project.

Further considerations
----------------------

It's important to note that a user's app will only download new or updated assets. It will not re-download unchanged assets that already exist inside the app.

One way to make sure that updates stay as slim as possible is to build and submit the app frequently to the app stores so that users can download a new app binary that includes more up-to-date assets. Generally, it's a good practice to build and submit an app when adding large or multiple assets, and it's good to use updates to fix small bugs and make minor changes between app store releases.

[Previous (EAS Update - Deployment)

Rollbacks](/eas-update/rollbacks)[Next (EAS Update - Deployment)

Continuous deployment](/eas-update/continuous-deployment)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/optimize-assets.mdx)
* Last updated on May 01, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Code assets](/eas-update/optimize-assets/#code-assets)[Image assets](/eas-update/optimize-assets/#image-assets)[Optimizing image assets](/eas-update/optimize-assets/#optimizing-image-assets)[Other manual optimization methods](/eas-update/optimize-assets/#other-manual-optimization-methods)[Ensuring assets are included in updates](/eas-update/optimize-assets/#ensuring-assets-are-included-in-updates)[Further considerations](/eas-update/optimize-assets/#further-considerations)