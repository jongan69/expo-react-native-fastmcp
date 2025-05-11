Using private npm packages - Expo Documentation

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

Using private npm packages
==========================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/private-npm-packages.mdx)

Learn how to configure EAS Build to use private npm packages.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/private-npm-packages.mdx)

---

EAS Build has full support for using private npm packages in your project. These can either be published to npm (if you have [the Pro/Teams plan](https://www.npmjs.com/products)) or to a private registry (for example, using self-hosted [Verdaccio](https://verdaccio.org/)).

Before starting the build, you will need to configure your project to provide EAS Build with your npm token.

Default npm configuration
-------------------------

By default, EAS Build uses a self-hosted npm cache that speeds up installing dependencies for all builds. Every EAS Build builder is configured with a .npmrc file for each platform:

### Android

```
registry=http://npm-cache-service.worker-infra-production.svc.cluster.local:4873

```

### iOS

```
registry=http://10.254.24.8:4873

```

Private packages published to npm
---------------------------------

If your project is using private packages published to npm, you need to provide EAS Build with [a read-only npm token](https://docs.npmjs.com/about-access-tokens) so that it can install your dependencies successfully.

The recommended way is to add the `NPM_TOKEN` secret to your account or project's secrets:

![Secret creation UI filled.](/static/images/eas-build/environment-secrets/secrets-create-filled.png)

For more information on how to do that, see [secret environment variables](/build-reference/variables#secrets-on-the-expo-website).

When EAS detects that the `NPM_TOKEN` environment variable is available during a build, it automatically creates the following .npmrc:

.npmrc

Copy

```
//registry.npmjs.org/:_authToken=${NPM_TOKEN}
registry=https://registry.npmjs.org/

```

However, this only happens when .npmrc is not in your project's root directory. If you already have this file, you need to update it manually.

You can verify if it worked by viewing build logs and looking for the Prepare project build phase:

![.npmrc created and shown in the build logs.](/static/images/eas-build/npmrc.png)

Packages published to a private registry
----------------------------------------

If you're using a private npm registry such as self-hosted [Verdaccio](https://verdaccio.org/), you will need to configure the .npmrc manually.

Create a .npmrc file in your project's root directory with the following contents:

.npmrc

Copy

```
registry=__REPLACE_WITH_REGISTRY_URL__

```

If your registry requires authentication, you will need to provide the token. For example, if your registry URL is `https://registry.johndoe.com/`, then update the file with:

.npmrc

Copy

```
//registry.johndoe.com/:_authToken=${NPM_TOKEN}
registry=https://registry.johndoe.com/

```

Both private npm packages and private registry
----------------------------------------------

> This is an advanced example.

Private npm packages are always [scoped](https://docs.npmjs.com/about-scopes#scopes-and-package-visibility). For example, if your npm username is `johndoe`, the private self-hosted registry URL is `https://registry.johndoe.com/`. If you want to install dependencies from both sources, create a .npmrc in your project's root directory with the following:

.npmrc

Copy

```
//registry.npmjs.org/:_authToken=${NPM_TOKEN}
@johndoe:registry=https://registry.npmjs.org/
registry=https://registry.johndoe.com/

```

Submodules in private repositories
----------------------------------

If you have a submodule in a private repository, you will need to initialize it by setting up an SSH key. For more information, see [submodules initialization](/build-reference/git-submodules#submodules-initialization).

[Previous (EAS Build - Reference)

Build lifecycle hooks](/build-reference/npm-hooks)[Next (EAS Build - Reference)

Git submodules](/build-reference/git-submodules)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/private-npm-packages.mdx)
* Last updated on December 18, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Default npm configuration](/build-reference/private-npm-packages/#default-npm-configuration)[Android](/build-reference/private-npm-packages/#android)[iOS](/build-reference/private-npm-packages/#ios)[Private packages published to npm](/build-reference/private-npm-packages/#private-packages-published-to-npm)[Packages published to a private registry](/build-reference/private-npm-packages/#packages-published-to-a-private-registry)[Both private npm packages and private registry](/build-reference/private-npm-packages/#both-private-npm-packages-and-private-registry)[Submodules in private repositories](/build-reference/private-npm-packages/#submodules-in-private-repositories)