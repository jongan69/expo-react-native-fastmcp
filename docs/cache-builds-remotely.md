Use build cache providers - Expo Documentation

[Docs](/)

[Blog](https://expo.dev/blog)[Changelog](https://expo.dev/changelog)[Star Us on GitHub](https://github.com/expo/expo)

Search

[Home](/)[Guides](/guides/overview)[EAS](/eas)[Reference](/versions/latest)[Learn](/tutorial/overview)

[Overview](/guides/overview)

Development process

[Develop an app with Expo](/workflow/overview)[Configure with app config](/workflow/configuration)[Continuous Native Generation](/workflow/continuous-native-generation)[Using libraries](/workflow/using-libraries)[Privacy manifests](/guides/apple-privacy)[Permissions](/guides/permissions)[Environment variables](/guides/environment-variables)

Linking

Write native code

Compile locally

[Development](/guides/local-app-development)[Production](/guides/local-app-production)[Cache builds remotely](/guides/cache-builds-remotely)

Web

Bundling

Existing React Native apps

Existing native apps

Reference

Expo Router

[Introduction](/router/introduction)[Installation](/router/installation)

Router 101

Navigation patterns

Advanced

Reference

Migration

Expo Modules API

[Overview](/modules/overview)[Get started](/modules/get-started)

Tutorials

Reference

Push notifications

[Overview](/push-notifications/overview)[About notification types](/push-notifications/what-you-need-to-know)[Expo push notifications setup](/push-notifications/push-notifications-setup)[Send notifications with the Expo Push Service](/push-notifications/sending-notifications)[Handle incoming notifications](/push-notifications/receiving-notifications)

Reference

More

[Upgrade Expo SDK](/workflow/upgrading-expo-sdk-walkthrough)

Assorted

Integrations

Troubleshooting

Regulatory compliance

[Data and Privacy protection](/regulatory-compliance/data-and-privacy-protection)[GDPR compliance](/regulatory-compliance/gdpr)[HIPAA compliance](/regulatory-compliance/hipaa)[Privacy Shield](/regulatory-compliance/privacy-shield)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Use build cache providers
=========================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/cache-builds-remotely.mdx)

Accelerate local development by caching and reusing builds from a provider.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/cache-builds-remotely.mdx)

---

Build caching is an experimental feature that speeds up `npx expo run:[android|ios]` by caching builds remotely, based on the project [fingerprint](/versions/latest/sdk/fingerprint).
When you run `npx expo run:[android|ios]`, it checks if a build with a matching fingerprint exists, then downloads and launches it rather than compiling it again. Otherwise, the project is compiled as usual and then the resulting binary is uploaded to the remote cache for future runs.

Using EAS as a build provider
-----------------------------

To use the EAS Build provider plugin, start by installing the `eas-build-cache-provider` package as a developer dependency:

Terminal

Copy

`-Â``npx expo install eas-build-cache-provider`

Then, update your app.json to include the `buildCacheProvider` property and its provider under `experiments`:

app.json

Copy

```
{
  "expo": {
    ...
    "experiments": {
      "buildCacheProvider": "eas"
    }
  }
}

```

You can roll your own cache provider by exporting a plugin that implements the following methods:

```
type BuildCacheProviderPlugin<T = any> = {
  /**
   * Try to fetch an existing build. Return its URL or null if missing.
   */
  resolveBuildCache(props: ResolveBuildCacheProps, options: T): Promise<string | null>;

  /**
   * Upload a new build binary. Return its URL or null on failure.
   */
  uploadBuildCache(props: UploadBuildCacheProps, options: T): Promise<string | null>;

  /**
   * (Optional) Customize the fingerprint hash algorithm.
   */
  calculateFingerprintHash?: (
    props: CalculateFingerprintHashProps,
    options: T
  ) => Promise<string | null>;
};

type ResolveBuildCacheProps = {
  projectRoot: string;
  platform: 'android' | 'ios';
  runOptions: RunOptions;
  fingerprintHash: string;
};
type UploadBuildCacheProps = {
  projectRoot: string;
  buildPath: string;
  runOptions: RunOptions;
  fingerprintHash: string;
  platform: 'android' | 'ios';
};
type CalculateFingerprintHashProps = {
  projectRoot: string;
  platform: 'android' | 'ios';
  runOptions: RunOptions;
};

```

A reference implementation using GitHub Releases to cache builds can be found in the [Build Cache Provider Example](https://github.com/expo/examples/tree/master/with-github-remote-build-cache-provider).

Creating a custom build provider
--------------------------------

Start by creating a provider directory for writing the provider plugin in TypeScript and add a provider.plugin.js file in the project root, which will be the plugin's entry point.

1

### Create a `provider/tsconfig.json` file

provider/tsconfig.json

Copy

```
{
  "extends": "expo-module-scripts/tsconfig.plugin",
  "compilerOptions": {
    "outDir": "build",
    "rootDir": "src"
  },
  "include": ["./src"],
  "exclude": ["**/__mocks__/*", "**/__tests__/*"]
}

```

2

### Create a `provider/src/index.ts` file for your plugin

provider/src/index.ts

Copy

```
import { BuildCacheProviderPlugin } from '@expo/config';

const plugin: BuildCacheProviderPlugin {
  resolveBuildCache: () => {
    console.log('Searching for remote builds...')
    return null;
  },
  uploadBuildCache: () => {
    console.log('Uploading build to remote...')
    return null;
  },,
};

export default plugin;

```

3

### Create an `provider.plugin.js` file in the root directory

provider.plugin.js

Copy

```
// This file configures the entry file for your plugin.
module.exports = require('./provider/build');

```

4

### Build your provider plugin

At the root of your project, run `npm run build provider` to start the TypeScript compiler in watch mode.

5

### Configure your example project to use your plugin by adding the following line to the `example/app.json` file:

example/app.json

Copy

```
{
  "expo": {
    ...
    "experiments": {
      "buildCacheProvider": {
        "plugin": "./provider.plugin.js"
      }
    }
  }
}

```

6

### Test your provider

When you run the `npx expo run` command inside your example directory, you should see your plugin's console statements in the logs.

Terminal

`-Â``cd example`

`-Â``npx expo run:ios`

That's it! You now have a remote build cache provider to speed up your builds.

### Passing custom options

To inject custom options to your plugin you can use the `options` field and it will be forwarded as the second parameter of your custom functions. To do so modify the `buildCacheProvider` field in example/app.json as shown below:

example/app.json

Copy

```
{
  "expo": {
    ...
    "experiments": {
      "buildCacheProvider": {
        "plugin": "./provider.plugin.js",
        "options": {
          "myCustomKey": "XXX-XXX-XXX"
        }
      }
    }
  }
}

```

[Previous (Development process - Compile locally)

Production](/guides/local-app-production)[Next (Development process - Web)

Develop websites](/workflow/web)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/cache-builds-remotely.mdx)
* Last updated on May 06, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Using EAS as a build provider](/guides/cache-builds-remotely/#using-eas-as-a-build-provider)[Creating a custom build provider](/guides/cache-builds-remotely/#creating-a-custom-build-provider)[Create a provider/tsconfig.json file](/guides/cache-builds-remotely/#create-a-providertsconfigjson-file)[Create a provider/src/index.ts file for your plugin](/guides/cache-builds-remotely/#create-a-providersrcindexts-file-for-your-plugin)[Create an provider.plugin.js file in the root directory](/guides/cache-builds-remotely/#create-an-providerpluginjs-file-in-the-root-directory)[Build your provider plugin](/guides/cache-builds-remotely/#build-your-provider-plugin)[Configure your example project to use your plugin by adding the following line to the example/app.json file:](/guides/cache-builds-remotely/#configure-your-example-project-to-use-your-plugin-by-adding-the-following-line-to-the-exampleappjson-file)[Test your provider](/guides/cache-builds-remotely/#test-your-provider)[Passing custom options](/guides/cache-builds-remotely/#passing-custom-options)