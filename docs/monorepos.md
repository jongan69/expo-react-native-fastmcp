Work with monorepos - Expo Documentation

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

Existing React Native apps

Existing native apps

Reference

[Work with monorepos](/guides/monorepos)[View logs](/workflow/logging)[Development and production modes](/workflow/development-mode)[Common development errors](/workflow/common-development-errors)[Android Studio Emulator](/workflow/android-studio-emulator)[iOS Simulator](/workflow/ios-simulator)[New Architecture](/guides/new-architecture)[React Compiler](/guides/react-compiler)

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

Work with monorepos
===================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/monorepos.mdx)

Learn about setting up Expo projects in a monorepo with Yarn v1 workspaces.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/monorepos.mdx)

---

Monorepos, or *"monolithic repositories"*, are single repositories containing multiple apps or packages. It can help speed up development for larger projects, make it easier to share code, and act as a single source of truth. This guide will set up a simple monorepo with an Expo project. We currently have first-class support for [Yarn 1 (Classic)](https://classic.yarnpkg.com/lang/en/) workspaces. If you want to use another tool, make sure you know how to configure it.

> Monorepos are not for everyone. It requires in-depth knowledge of the used tooling, adds more complexity, and often requires specific tooling configuration. You can get far with just a single repository.

Automatic configuration
-----------------------

Starting from SDK 48, Expo automatically detects monorepos and configures new app projects added to a monorepo when using [bun](https://bun.sh/docs/install/workspaces), [npm](https://docs.npmjs.com/cli/using-npm/workspaces), or [yarn](https://yarnpkg.com/features/workspaces). From SDK 52, Expo also performs this automatic configuration when using [pnpm](https://pnpm.io/workspaces). The detection is based on the workspaces configuration in your project.

> Expo's automatic monorepo setup adds all workspaces in your monorepo as `watchFolders` to Metro. This might slow Metro down for larger monorepos. You can also manually configure which directories Metro should watch by changing the `watchFolders` in your metro.config.js, see [Modify the Metro config](/guides/monorepos#modify-the-metro-config).

Manual configuration
--------------------

In this example, we will set up a monorepo using Yarn workspaces without the [nohoist](https://classic.yarnpkg.com/blog/2018/02/15/nohoist/) option. We will assume some familiar names, but you can fully customize them. After this guide, our basic structure should look like this:

* apps - Contains multiple projects, including React Native apps.
* packages - Contains different packages used by our apps.
* package.json - Root package file, containing Yarn workspaces config.

### Root package file

All Yarn monorepos should have a "root" package.json file. It is the main configuration for our monorepo and may contain packages installed for all projects in the repository. You can run `yarn init`, or create the package.json manually. It should look something like this:

package.json

Copy

```
{
  "name": "monorepo",
  "version": "1.0.0"
}

```

### Set up yarn workspaces

Yarn and other tooling have a concept called *"workspaces"*. Every package and app in our repository has its own workspace. Before we can use them, we have to instruct Yarn where to find these workspaces. We can do that by setting the `workspaces` property using [glob patterns](https://classic.yarnpkg.com/lang/en/docs/workspaces/#toc-tips-tricks), in the package.json:

package.json

Copy

```
{
  "private": true,
  "name": "monorepo",
  "version": "1.0.0",
  "workspaces": ["apps/*", "packages/*"]
}

```

> Yarn workspaces require the root package.json to be private. If you don't set this, `yarn install` will error with a message mentioning this.

### Create our first app

Now that we have the basic monorepo structure set up, let's add our first app.

Before we create our app, we have to create the apps directory. This directory contains all separate apps or websites that belong to this monorepo. Inside this apps directory, we can create a sub-directory that contains the React Native app.

Terminal

Copy

`-Â``yarn create expo apps/cool-app`

> If you have an existing app, you can copy all those files into a directory inside apps.

After copying or creating the first app, run `yarn` to check for common warnings.

#### Modify the Metro config

Expo's Metro config has monorepo support for Bun, npm, pnpm and Yarn. You don't have to manually configure Metro when using monorepos if you use the config from [`expo/metro-config`](/guides/customizing-metro). If that's the case, you can skip this step.

To configure a monorepo with Metro manually, there are two main changes:

1. Make sure Metro is watching all relevant code within the monorepo, not just apps/cool-app.
2. Tell Metro where it can resolve packages. They might be installed in apps/cool-app/node\_modules or node\_modules.

We can configure this by [creating a metro.config.js](/guides/customizing-metro#customizing) with the following content:

metro.config.js

Copy

```
const { getDefaultConfig } = require('expo/metro-config');
const path = require('path');

// Find the project and workspace directories
const projectRoot = __dirname;
// This can be replaced with `find-yarn-workspace-root`
const monorepoRoot = path.resolve(projectRoot, '../..');

const config = getDefaultConfig(projectRoot);

// 1. Watch all files within the monorepo
config.watchFolders = [monorepoRoot];
// 2. Let Metro know where to resolve packages and in what order
config.resolver.nodeModulesPaths = [
  path.resolve(projectRoot, 'node_modules'),
  path.resolve(monorepoRoot, 'node_modules'),
];

module.exports = config;

```

> Learn more about [customizing Metro](/guides/customizing-metro).

1. Why do we need to watch all files with the monorepo?

Metro has three separate stages in its bundling process, [documented here](https://metrobundler.dev/docs/concepts). During the first phase, Resolution, Metro resolves your app's required files and dependencies. Metro does that with the `watchFolders` option, which is set to the project directory by default. This default setting works great for apps that don't use a monorepo structure.

When using monorepos, your app dependencies splits up into different directories. Each of these directories must be within the scope of the [`watchFolders`](https://metrobundler.dev/docs/configuration/#watchfolders). If a changed file is outside of that scope, Metro won't be able to find it. Setting this path to the root of your monorepo will force Metro to watch all files within the repository and possibly cause a slow initial startup time.

As your monorepo increases in size, watching all files within the monorepo becomes slower. You can speed things up by only watching the packages your app uses. Typically, these are the ones that are installed with an asterisk (\*) in your package.json. For example:

metro.config.js

Copy

```
const { getDefaultConfig } = require('expo/metro-config');
const path = require('path');

const projectRoot = __dirname;
const monorepoRoot = path.resolve(projectRoot, '../..');

const config = getDefaultConfig(projectRoot);

// Only list the packages within your monorepo that your app uses. No need to add anything else.
// If your monorepo tooling can give you the list of monorepo workspaces linked
// in your app workspace, you can automate this list instead of hardcoding them.
const monorepoPackages = {
  '@acme/api': path.resolve(monorepoRoot, 'packages/api'),
  '@acme/components': path.resolve(monorepoRoot, 'packages/components'),
};

// 1. Watch the local app directory, and only the shared packages (limiting the scope and speeding it up)
// Note how we change this from `monorepoRoot` to `projectRoot`. This is part of the optimization!
config.watchFolders = [projectRoot, ...Object.values(monorepoPackages)];

// Add the monorepo workspaces as `extraNodeModules` to Metro.
// If your monorepo tooling creates workspace symlinks in the `node_modules` directory,
// you can either add symlink support to Metro or set the `extraNodeModules` to avoid the symlinks.
// See: https://metrobundler.dev/docs/configuration/#extranodemodules
config.resolver.extraNodeModules = monorepoPackages;

// 2. Let Metro know where to resolve packages and in what order
config.resolver.nodeModulesPaths = [
  path.resolve(projectRoot, 'node_modules'),
  path.resolve(monorepoRoot, 'node_modules'),
];

module.exports = config;

```

2. Why do we need to tell Metro how to resolve packages?

This option is important to resolve libraries in the correct node\_modules directories. Monorepo tooling, like Yarn, usually creates two different node\_modules directories which are used for a single workspace.

1. apps/mobile/node\_modules - The "project" directory
2. node\_modules - The "root" directory

Yarn uses the root directory to install packages used in multiple workspaces. If a workspace uses a different package version, it installs that different version in the project directory.

We have to tell Metro to look in these two directories. The order is important here because the project directory node\_modules can contain specific versions we use for our app. When the package does not exist in the project directory, it should try the shared root directory.

#### Change default entrypoint

In monorepos, we can't hardcode paths to packages anymore since we can't be sure if they are installed in the root node\_modules or the workspace node\_modules directory. If you are using a managed project, we have to change our default entry point that looks like `node_modules/expo/AppEntry.js`.

> This new entry point already exists for existing React Native (bare) projects. You only need to add this if you have a project generated with `npx create-expo-app`.

If you are using [Expo Router](/router/introduction), do not change the entrypoint. By default [`EXPO_USE_METRO_WORKSPACE_ROOT`](/more/expo-cli#environment-variables) is activated, which enables the auto server root detection for Metro. You can skip this step.

Otherwise, open your app's package.json, change the `main` property to `index.js`, and create this new index.js file in the app directory with the content below.

index.js

Copy

```
import { registerRootComponent } from 'expo';

import App from './App';

// registerRootComponent calls AppRegistry.registerComponent('main', () => App);
// It also ensures that whether you load the app in Expo Go or in a native build,
// the environment is set up appropriately
registerRootComponent(App);

```

### Create a package

Monorepos can help us group code in a single repository. That includes apps but also separate packages. They also don't need to be published. The [Expo repository](https://github.com/expo/expo) uses this as well. All the Expo SDK packages live inside the [packages](https://github.com/expo/expo/tree/main/packages) directory in our repo. It helps us test the code inside one of our [apps](https://github.com/expo/expo/tree/main/apps/native-component-list) directory before we publish them.

Let's go back to the root and create the packages directory. This directory can contain all the separate packages that you want to make. Once you are inside this directory, we need to add a new sub-directory. The sub-directory is a separate package that we can use inside our app. In the example below, we named it cool-package.

Terminal

Copy

`# Create our new package directory`

`-Â``mkdir -p packages/cool-package`

`-Â``cd packages/cool-package`

  
`# And create the new package`

`-Â``yarn init`

We won't go into too much detail in creating a package. If you are not familiar with this, consider using a simple app without monorepos. But, to make the example complete, let's add an index.js file with the following content:

index.js

Copy

```
export const greeting = 'Hello!';

```

### Using the package

Like standard packages, we need to add our cool-package as a dependency to our cool-app. The main difference between a standard package, and one from the monorepo, is you'll always want to use the *"current state of the package"* instead of a version. Let's add cool-package to our app by adding `"cool-package": "*"` to our app package.json file:

package.json

Copy

```
{
  "name": "cool-app",
  "version": "1.0.0",
  "scripts": {
    "start": "expo start",
    "android": "expo start --android",
    "ios": "expo start --ios",
    "web": "expo start --web"
  },
  "dependencies": {
    "cool-package": "*",
    "expo": "~50.0.0",
    "expo-status-bar": "~1.10.0",
    "react": "18.2.0",
    "react-dom": "18.2.0",
    "react-native": "0.73.0",
    "react-native-web": "~0.19.13"
  },
  "devDependencies": {
    "@babel/core": "^7.20.0"
  }
}

```

> After adding the package as a dependency, run `yarn install` to install or link the dependency to your app.

Now you should be able to use the package inside your app! To test this, let's edit the App.js in our app and render the `greeting` text from our cool-package.

App.js

Copy

```
import { greeting } from 'cool-package';
import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { Text, View } from 'react-native';

export default function App() {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>{greeting}</Text>
      <StatusBar style="auto" />
    </View>
  );
}

```

Common issues
-------------

As mentioned earlier, using monorepos is not for everyone. You take on increased complexity and need to solve issues you most likely will run into. Here are a couple of common issues you might encounter.

### Multiple React Native versions within the monorepo

Expo SDK has improved support for more complete node\_modules patterns, such as isolated modules. Unfortunately, React Native can still cause issues when installing multiple versions inside a single monorepo. Because of that, it's recommended to only use a single version of React Native.

You can check if your monorepo has multiple React Native versions and why they are installed through the package manager you use.

Terminal

`# Bun does not support `bun why` yet, but you can use `yarn why``

`-Â``bun install --yarn && yarn why react-native`

  
`# npm supports the `npm explain` command, aliased to `npm why```# https://docs.npmjs.com/cli/v10/commands/npm-explain`

`-Â``npm why react-native`

  
`# pnpm only iterates the full monorepo with the `--recursive` flag``# https://pnpm.io/cli/why`

`-Â``pnpm why --recursive react-native`

  
`# Yarn supports the `yarn why` command``# https://classic.yarnpkg.com/en/docs/cli/why`

`-Â``yarn why react-native`

### Can I use another monorepo tool instead of Yarn workspaces?

There are a lot of monorepo tools available, and each of these tools has its benefits. It's hard for us to keep up with the latest tools and methods, and because of that, we can't officially support new monorepo tools. That being said, if the tool follows these three rules, it should work fine.

1. All dependencies must be installed in a node\_modules directory

React Native dependencies contain many other files besides JavaScript, like Gradle files such as react-native/react.gradle. These native files are referenced from different sources other than Node.js, and because of that, it makes it fundamentally incompatible with concepts like Plug'n'Play modules.

2. Dependencies used in multiple workspaces can be installed in the root node\_modules directory

Whenever multiple workspaces use the same version of a single dependency, they can be installed in a root node\_modules directory. Monorepo tools usually do this to remove duplicate tasks, like installing the same dependency twice in different places. This rule isn't necessary but does set us up for next rule.

3. Different versions of dependencies must be installed in the app node\_modules directory

In the [Modify the Metro config](/guides/monorepos#modify-the-metro-config) step, we instructed Metro to do a couple of this, specifically:

* #2 - Resolve dependencies in the order of the local apps/<name>/node\_modules and root node\_modules directories.
* #3 - Disable resolving dependencies using the hierarchical lookup strategy.

If a workspace uses a different library version than the one installed in the root node\_modules, that different library version must be installed in the workspace apps/<name>/node\_modules directory.

When Metro resolves a library, for example, `react`, from the workspace, it should find that different version in apps/<name>/node\_modules and not look inside the root node\_modules directory.

When importing a dependency from the root node\_modules directory that also imports `react`, `react` should still resolve to the different version installed in apps/<name>/node\_modules. That's what the disabled hierarchical lookup option does for Metro. Without this, some libraries might import the wrong `react` version and cause "multiple React versions found" errors.

The default settings of tools like [pnpm](https://pnpm.io/) do not follow these rules. You can change that by adding a .npmrc file with `node-linker=hoisted` ([see docs](https://pnpm.io/npmrc#node-linker)). That config option will change the behavior to match these rules.

### Script '...' does not exist

React Native uses packages to ship both JavaScript and native files. These native files also need to be linked, like the [react-native/react.Gradle](https://github.com/facebook/react-native/blob/v0.70.6/react.gradle) file from android/app/build.Gradle. Usually, this path is hardcoded to something like:

Android ([source](https://github.com/facebook/react-native/blob/e918362be3cb03ae9dee3b8d50a240c599f6723f/template/android/app/build.gradle#L84))

```
apply from: "../../node_modules/react-native/react.gradle"

```

iOS ([source](https://github.com/facebook/react-native/blob/e918362be3cb03ae9dee3b8d50a240c599f6723f/template/ios/Podfile#L1))

```
require_relative '../node_modules/react-native/scripts/react_native_pods'

```

Unfortunately, this path can be different in monorepos because of [hoisting](https://classic.yarnpkg.com/blog/2018/02/15/nohoist/). It also doesn't use the [Node module resolution](https://nodejs.org/api/modules.html#all-together). You can avoid this issue by using Node to find the location of the package instead of hardcoding this:

Android ([source](https://github.com/expo/expo/blob/6877c1f5cdca62b395b0d5f49d87f2f3dbb50bec/templates/expo-template-bare-minimum/android/app/build.gradle#L87))

```
apply from: new File(["node", "--print", "require.resolve('react-native/package.json')"].execute(null, rootDir).text.trim(), "../react.gradle")

```

iOS ([source](https://github.com/expo/expo/blob/61cbd9a5092af319b44c319f7d51e4093210e81b/templates/expo-template-bare-minimum/ios/Podfile#L2))

```
require File.join(File.dirname(`node --print "require.resolve('react-native/package.json')"`), "scripts/react_native_pods")

```

In the snippets above, you can see that we use Node's own [`require.resolve()`](https://nodejs.org/api/modules.html#requireresolverequest-options) method to find the package location. We explicitly refer to `package.json` because we want to find the root location of the package, not the location of the entry point. And with that root location, we can resolve to the expected relative path within the package. [Learn more about these references here](https://github.com/expo/expo/blob/4633ab2364e30ea87ca2da968f3adaf5cdde9d8b/packages/expo-modules-core/README.mdx#importing-native-dependencies---autolinking).

All Expo SDK modules and templates have these dynamic references and work with monorepos. However, occasionally, you might run into packages that still use the hardcoded path. You can manually edit it with [`patch-package`](https://github.com/ds300/patch-package#readme) or mention this to the package maintainers.

[Previous (Development process - Existing native apps)

Install Expo modules](/brownfield/installing-expo-modules)[Next (Development process - Reference)

View logs](/workflow/logging)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/monorepos.mdx)
* Last updated on May 01, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Automatic configuration](/guides/monorepos/#automatic-configuration)[Manual configuration](/guides/monorepos/#manual-configuration)[Root package file](/guides/monorepos/#root-package-file)[Set up yarn workspaces](/guides/monorepos/#set-up-yarn-workspaces)[Create our first app](/guides/monorepos/#create-our-first-app)[Create a package](/guides/monorepos/#create-a-package)[Using the package](/guides/monorepos/#using-the-package)[Common issues](/guides/monorepos/#common-issues)[Multiple React Native versions within the monorepo](/guides/monorepos/#multiple-react-native-versions-within-the-monorepo)[Can I use another monorepo tool instead of Yarn workspaces?](/guides/monorepos/#can-i-use-another-monorepo-tool-instead-of-yarn-workspaces)[Script '...' does not exist](/guides/monorepos/#script--does-not-exist)