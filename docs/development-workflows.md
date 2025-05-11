Tools, workflows and extensions - Expo Documentation

[Docs](/)

[Blog](https://expo.dev/blog)[Changelog](https://expo.dev/changelog)[Star Us on GitHub](https://github.com/expo/expo)

Search

[Home](/)[Guides](/guides/overview)[EAS](/eas)[Reference](/versions/latest)[Learn](/tutorial/overview)

Get started

[Introduction](/get-started/introduction)[Create a project](/get-started/create-a-project)[Set up your environment](/get-started/set-up-your-environment)[Start developing](/get-started/start-developing)[Next steps](/get-started/next-steps)

Develop

[Tools for development](/develop/tools)

Navigation

User interface

Development builds

[Introduction](/develop/development-builds/introduction)[Create a build](/develop/development-builds/create-a-build)[Use a build](/develop/development-builds/use-development-builds)[Share with your team](/develop/development-builds/share-with-your-team)[Tools, workflows and extensions](/develop/development-builds/development-workflows)[Next steps](/develop/development-builds/next-steps)

Config plugins

Debugging

[Authentication](/develop/authentication)[Unit testing](/develop/unit-testing)

Review

[Distributing apps for review](/review/overview)[Share previews with your team](/review/share-previews-with-your-team)[Open updates with Orbit](/review/with-orbit)

Deploy

[Build project for app stores](/deploy/build-project)[Submit to app stores](/deploy/submit-to-app-stores)[App stores metadata](/deploy/app-stores-metadata)[Send over-the-air updates](/deploy/send-over-the-air-updates)[Deploy web apps](/deploy/web)

Monitor

[Monitoring services](/monitoring/services)

More

[Core concepts](/core-concepts)[FAQ](/faq)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Tools, workflows and extensions
===============================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/development-builds/development-workflows.mdx)

Learn more about different tools, workflows and extensions available when working with development builds.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/development-builds/development-workflows.mdx)

---

Development builds allow you to iterate quickly. However, you can extend the capabilities of your development build to provide a better developer experience when working in teams or customize the build to suit your needs.

Tools
-----

### Tunnel URLs

Sometimes, restrictive network conditions make it difficult to connect to the development server. The `npx expo start` command exposes your development server on a publicly available URL that is accessible through firewalls from around the globe. This option is helpful if you are not able to connect to your development server with the default LAN option or if you want to get feedback on your implementation while you are developing.

To get a tunneled URL, pass the [`--tunnel` flag](/more/expo-cli#tunneling) to `npx expo start` from the command line.

### Published updates

EAS CLI's `eas update` command bundles the current state of your JavaScript and asset files into an optimized "update". This update is stored on a hosting service by Expo. A development build of your app can load published updates without needing to check out a particular commit or leave a development machine running.

### Manually entering an update's URL

When a development build launches, it will expose UI to load a development server, or to "Enter URL manually". You can provide a URL manually that will launch a specific branch. The URL follows this pattern:

```
https://u.expo.dev/[your-project-id]?channel-name=[channel-name]

# Example
https://u.expo.dev/F767ADF57-B487-4D8F-9522-85549C39F43F?channel-name=main

```

To get your project's ID, use the URL in the [app config's `expo.updates.url`](/versions/latest/config/app#url) field. To see a list of channels, run `eas channel:list`.

### Deep linking to an update's URL

You can load your app on a device that has a compatible build of your custom client by opening a URL of the form `{scheme}://expo-development-client/?url={manifestUrl}`. You'll need to pass the following parameters:

| parameter | value |
| --- | --- |
| `scheme` | URL scheme of your client (defaults to `exp+{slug}` where [`slug`](/versions/latest/config/app#slug) is the value set in the app config) |
| `manifestUrl` | URL-encoded URL of an update manifest to load. The URL will be `https://u.expo.dev/[your-project-id]?channel-name=[channel-name]` |

Example:

```
exp+app-slug://expo-development-client/?url=https%3A%2F%2Fu.expo.dev%2F767ADF57-B487-4D8F-9522-85549C39F43F%2F%3Fchannel-name%3Dmain

```

In the example above, the `scheme` is `exp+app-slug`, and the `manifestUrl` is a project with an ID of `F767ADF57-B487-4D8F-9522-85549C39F43F` and a channel of `main`.

#### App-specific deep links

When testing deep links in your development build, such as when navigating to a specific screen in an Expo Router app or testing redirecting back to your app during an Oauth login flow, construct the URL exactly as you would if you were deep-linking into a standalone build of your app (for example, `myscheme://path/to/screen`).

Your project must be already open in the development build for an app-specific deep link to work. Cold-launching a development build with an app-specific deep link is not currently supported. Avoid using `expo-development-client` in your app-specific deep links in the path, as it is a reserved path used for launching an updated URL.

### QR codes

You can use our endpoint to generate a QR code that can be easily loaded by a development build.

Requests send to `https://qr.expo.dev/development-client` when supplied the query parameters such as `appScheme` and `url` will receive a response with an SVG image containing a QR code that can be easily scanned to load a version of your project in your development build.

| parameter | value |
| --- | --- |
| `appScheme` | URL-encoded deeplinking scheme of your development build (defaults to `exp+{slug}` where [`slug`](/versions/latest/config/app#slug) is the value set in the app config) |
| `url` | URL-encoded URL of an update manifest to load. The URL will be `https://u.expo.dev/[your-project-id]?channel-name=[channel-name]` |

Example:

```
https://qr.expo.dev/development-client?appScheme=exp%2Bapps-slug&url=https%3A%2F%2Fu.expo.dev%2FF767ADF57-B487-4D8F-9522-85549C39F43F0%3Fchannel-name%3Dmain

```

In the example above, the `scheme` is `exp+app-slug`, and the `url` is a project with an ID of `F767ADF57-B487-4D8F-9522-85549C39F43F` and a channel of `main`.

Example workflows
-----------------

These are a few examples of workflows to help your team get the most out of your development build. If you come up with others that would be useful for other teams, [submit a PR](https://github.com/expo/expo/tree/main/CONTRIBUTING.md#-updating-documentation) to share your knowledge!

### PR previews

You can set up your CI process to publish an EAS Update whenever a pull request is updated and add a QR code that is used to view the change in a compatible development build.

See [instructions for publishing app previews on pull requests](/eas-update/github-actions#publish-previews-on-pull-requests) to implement this workflow in your project using GitHub Actions or serve as a template in your CI of choice.

Extensions
----------

Extensions allow you to extend your development client with additional capabilities.

### Extending the dev menu

The dev menu can be extended to include extra buttons by using the `registerDevMenuItems` API:

```
import { registerDevMenuItems } from 'expo-dev-menu';

const devMenuItems = [
  {
    name: 'My Custom Button',
    callback: () => console.log('Hello world!'),
  },
];

registerDevMenuItems(devMenuItems);

```

This will create a new section in the dev menu that includes the buttons you have registered:

![An example of a custom menu button in expo-dev-menu](/static/images/dev-client/custom-menu-button.png)
> Subsequent calls of `registerDevMenuItems` will override all previous entries.

### EAS Update

![An example list of EAS Update that can be loaded in the expo-dev-client.](/static/images/dev-client/eas-updates-screen.png)

The EAS Update extension provides the ability to view and load published updates in your development client.

It's available for all development clients `v0.9.0` and above. To install it, you'll need the most recent publish of `expo-updates`:

Terminal

Copy

`-Â``npx expo install expo-dev-client expo-updates`

#### Configure EAS Update

If you have not yet configured EAS Updates in your project, you can find [additional instructions on how to do so here.](/eas-update/getting-started)

You can now view and load EAS Updates in your development build via the `Extensions` panel.

Set runtimeVersion in app config
--------------------------------

When you create a development build of your project, you'll get a stable environment to load any changes to your app that are defined in JavaScript or other asset-related changes. Other changes to your app, whether defined directly in android and ios directories or by packages or SDKs you choose to install, will require you to create a new build of your development build.

To enforce an API contract between the JavaScript and native layers of your app, you should set the [`runtimeVersion`](/eas-update/runtime-versions) value in the app config. Each build you make will have this value embedded and will only load bundles with the same `runtimeVersion`, in both development and production.

[Previous (Develop - Development builds)

Share with your team](/develop/development-builds/share-with-your-team)[Next (Develop - Development builds)

Next steps](/develop/development-builds/next-steps)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/development-builds/development-workflows.mdx)
* Last updated on December 27, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Tools](/develop/development-builds/development-workflows/#tools)[Tunnel URLs](/develop/development-builds/development-workflows/#tunnel-urls)[Published updates](/develop/development-builds/development-workflows/#published-updates)[Manually entering an update's URL](/develop/development-builds/development-workflows/#manually-entering-an-updates-url)[Deep linking to an update's URL](/develop/development-builds/development-workflows/#deep-linking-to-an-updates-url)[QR codes](/develop/development-builds/development-workflows/#qr-codes)[Example workflows](/develop/development-builds/development-workflows/#example-workflows)[PR previews](/develop/development-builds/development-workflows/#pr-previews)[Extensions](/develop/development-builds/development-workflows/#extensions)[Extending the dev menu](/develop/development-builds/development-workflows/#extending-the-dev-menu)[EAS Update](/develop/development-builds/development-workflows/#eas-update)[Set runtimeVersion in app config](/develop/development-builds/development-workflows/#set-runtimeversion-in-app-config)