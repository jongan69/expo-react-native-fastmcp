Analyzing JavaScript bundles - Expo Documentation

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

Web

Bundling

[Bundle with Metro](/guides/customizing-metro)[Analyzing JavaScript bundles](/guides/analyzing-bundles)[Tree shaking](/guides/tree-shaking)[Minification](/guides/minify)[Why Metro?](/guides/why-metro)

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

Analyzing JavaScript bundles
============================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/analyzing-bundles.mdx)

Learn about improving the production JavaScript bundle size of Expo apps and websites.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/analyzing-bundles.mdx)

---

Bundle performance varies for different platforms. For example, web browsers don't support precompiled bytecode, so the JavaScript bundle size is important for improving startup time and performance. The smaller the bundle, the faster it can be downloaded and parsed.

Analyzing bundle size with Atlas
--------------------------------

![Expo Atlas overview page.](/static/images/atlas/atlas-overview.avif)
> Available only for SDK 51 and above.

The libraries used in a project influence the size of the production JavaScript bundle. Starting from Expo SDK 51, you can use [Expo Atlas](https://github.com/expo/expo-atlas#readme) to visualize the production bundle and identify which libraries contribute to the bundle size.

### Using Atlas with `npx expo start`

You can use Expo Atlas with the local development server. This method allows Atlas to update whenever you change any code in your project.

Once your app is running using the local development server on Android, iOS, and/or web, you can open Atlas through the [dev tools plugin menu](/debugging/devtools-plugins#using-a-dev-tools-plugin) using `shift` + `m`.

Terminal

Copy

`# Start the local development server with Atlas`

`-Â``EXPO_UNSTABLE_ATLAS=true npx expo start`

#### Changing development mode to production

By default, Expo starts the local development server in [development mode](/workflow/development-mode#development-mode). Development mode disables some optimizations that are enabled in [production mode](/workflow/development-mode#production-mode). You can also start the local development server in production mode to get a more accurate representation of the production bundle size:

Terminal

Copy

`# Run the local development server in production mode`

`-Â``EXPO_UNSTABLE_ATLAS=true npx expo start --no-dev`

### Using Atlas with `npx expo export`

You can also use Expo Atlas when generating a production bundle for your app or EAS Update. Atlas generates a .expo/atlas.jsonl file during export, which you can share and open without having access to the project.

Terminal

`# Export your app for all platforms`

`-Â``EXPO_UNSTABLE_ATLAS=true npx expo export`

  
`# Open the generated Atlas file`

`-Â``npx expo-atlas .expo/atlas.jsonl`

You can also specify the platforms you want to analyze using the `--platform` option. Atlas will gather the data for the exported platforms only.

### Analyzing transformed modules

![Expo Atlas module page.](/static/images/atlas/atlas-module.avif)

Inside Atlas, you can hold `â Cmd` and click on a graph node to see the transformed module details. This feature helps you understand how a module is transformed by Babel, which modules it imports, and which modules imported it. This can be used to trace the origin of a module across the dependency graph.

Analyzing bundle size with source-map-explorer
----------------------------------------------

> Alternative method for SDK 50 and below.

If you are using SDK 50 or below, you can use the [`source-map-explorer`](https://www.npmjs.com/package/source-map-explorer) library to visualize and analyze the production JavaScript bundle.

1

To use source map explorer, run the following command to install it:

Terminal

Copy

`-Â``npm i --save-dev source-map-explorer`

2

Add a script to package.json to run it. You might have to adjust the input path depending on the platform or SDK you are using. For brevity, the following example assumes the project is Expo SDK 50 and does not use Expo Router `server` output.

package.json

Copy

```
{
  "scripts": {
    "analyze:web": "source-map-explorer 'dist/_expo/static/js/web/*.js' 'dist/_expo/static/js/web/*.js.map'",
    "analyze:ios": "source-map-explorer 'dist/_expo/static/js/ios/*.js' 'dist/_expo/static/js/ios/*.js.map'",
    "analyze:android": "source-map-explorer 'dist/_expo/static/js/android/*.js' 'dist/_expo/static/js/android/*.js.map'"
  }
}

```

If you are using the SDK 50 `server` output for web, then use the following to map web bundles:

Terminal

Copy

`-Â``npx source-map-explorer 'dist/client/_expo/static/js/web/*.js' 'dist/client/_expo/static/js/web/*.js.map'`

Web bundles are output to the dist/client subdirectory to prevent exposing server code to the client.

3

Export your production JavaScript bundle and include the `--source-maps` flag so that the source map explorer can read the source maps. For native apps using Hermes, you can use the `--no-bytecode` option to disable bytecode generation.

Terminal

`-Â``npx expo export --source-maps --platform web`

  
`# Native apps using Hermes can disable bytecode for analyzing the JavaScript bundle.`

`-Â``npx expo export --source-maps --platform ios --no-bytecode`

This command shows the JavaScript bundle and source map paths in the output. In the next step, you will pass these paths to the source map explorer.

> Avoid publishing source maps to production as they can cause both security issues and performance issues (a browser will download the large maps).

4

Run the script to analyze your bundle:

Terminal

Copy

`-Â``npm run analyze:web`

On running this command, you might see the following error:

```
You must provide the URL of lib/mappings.wasm by calling SourceMapConsumer.initialize({ 'lib/mappings.wasm': ... }) before using SourceMapConsumer

```

This is probably due to a [known issue](https://github.com/danvk/source-map-explorer/issues/247) in `source-map-explorer` in Node.js 18 and above. To resolve this, set the environment variable `NODE_OPTIONS=--no-experimental-fetch` before running the analyze script.

You might encounter a warning such as `Unable to map 809/13787 bytes (5.87%)`. This occurs because source maps often exclude bundler runtime definitions (for example, `__d(() => {}, [])`). This value is consistent and not a reason for concern.

Lighthouse
----------

Lighthouse is a great way to see how fast, accessible, and performant your website is. You can test your project with the Audit tab in Chrome, or with the [Lighthouse CLI](https://github.com/GoogleChrome/lighthouse#using-the-node-cli).

After creating a production build with `npx expo export -p web` and serving it (using either `npx serve dist`, or production deployment, or custom server), run Lighthouse with the URL your site is hosted at.

Terminal

`# Install the lighthouse CLI`

`-Â``npm install -g lighthouse`

  
`# Run the lighthouse CLI for your site`

`-Â``npx lighthouse <url> --view`

[Previous (Development process - Bundling)

Bundle with Metro](/guides/customizing-metro)[Next (Development process - Bundling)

Tree shaking](/guides/tree-shaking)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/analyzing-bundles.mdx)
* Last updated on August 26, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Analyzing bundle size with Atlas](/guides/analyzing-bundles/#analyzing-bundle-size-with-atlas)[Using Atlas with npx expo start](/guides/analyzing-bundles/#using-atlas-with-npx-expo-start)[Using Atlas with npx expo export](/guides/analyzing-bundles/#using-atlas-with-npx-expo-export)[Analyzing transformed modules](/guides/analyzing-bundles/#analyzing-transformed-modules)[Analyzing bundle size with source-map-explorer](/guides/analyzing-bundles/#analyzing-bundle-size-with-source-map-explorer)[Lighthouse](/guides/analyzing-bundles/#lighthouse)