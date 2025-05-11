Install app variants on the same device - Expo Documentation

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

Install app variants on the same device
=======================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/variants.mdx)

Learn how to install multiple variants of an app on the same device.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/variants.mdx)

---

When creating [development, preview, and production builds](/build/eas-json#common-use-cases), installing these build variants simultaneously on the same device is common. This allows working in development, previewing the next version of the app, and running the production version on a device without needing to uninstall and reinstall the app.

This guide provides the steps required to configure multiple (development and production) variants to install and use them on the same device.

Prerequisites
-------------

To have multiple variants of an app installed on your device, each variant must have a unique [Application ID (Android)](/versions/latest/config/app#package) or [Bundle Identifier (iOS)](/versions/latest/config/app#bundleidentifier).

Configure development and production variants
---------------------------------------------

You have created a project using Expo tooling, and now you want to create a development and a production build. Your project's app.json may have the following configuration:

app.json

Copy

```
{
  "expo": {
    "name": "MyApp",
    "slug": "my-app",
    "ios": {
      "bundleIdentifier": "com.myapp"
    },
    "android": {
      "package": "com.myapp"
    }
  }
}

```

If your project has EAS Build configured, the eas.json also has a similar configuration as shown below:

eas.json

Copy

```
{
  "build": {
    "development": {
      "developmentClient": true
    },
    "production": {}
  }
}

```

### Convert app.json to app.config.js

To have multiple variants of the app installed on the same device, rename the app.json to app.config.js and export the configuration as shown below:

app.config.js

Copy

```
export default {
  name: 'MyApp',
  slug: 'my-app',
  ios: {
    bundleIdentifier: 'com.myapp',
  },
  android: {
    package: 'com.myapp',
  },
};

```

In app.config.js, add an environment variable called `IS_DEV` to switch the `android.package` and `ios.bundleIdentifier` for each variant based on the variable:

app.config.js

Copy

```
const IS_DEV = process.env.APP_VARIANT === 'development';

export default {
  name: IS_DEV ? 'MyApp (Dev)' : 'MyApp',
  slug: 'my-app',
  ios: {
    bundleIdentifier: IS_DEV ? 'com.myapp.dev' : 'com.myapp',
  },
  android: {
    package: IS_DEV ? 'com.myapp.dev' : 'com.myapp',
  }
};

```

In the above example, the environment variable `IS_DEV` is used to differentiate between the development and production environment. Based on its value, the different Application IDs or Bundle Identifiers are set for each variant.

Additional app variant customizations

You can customize other aspects of your app on a per-variant basis. You can swap any configuration that you used previously in app.json using the same approach as above.

Examples:

* If you are using a library that requires you to register your application identifier with an external service to use its SDK, such as Google Maps or Firebase Cloud Messaging (FCM), you'll need to have a separate configuration for that API for the `android.package` and `ios.bundleIdentifier`.
* If you're using [development builds](/develop/development-builds/introduction), you can configure the `expo-dev-client` plugin to disable the app scheme used by Expo CLI and EAS Update QR codes in non-development builds. This ensures that those URLs will always launch the development build, regardless of your device's defaults:

app.config.js

Copy

```
plugins: [
  [
    'expo-dev-client',
    {
      addGeneratedScheme: !!IS_DEV,
    },
  ],
],

```

### Configuration for EAS Build

In eas.json, set the `APP_VARIANT` environment variable to run builds with the development profile by using the `env` property:

eas.json

Copy

```
{
  "build": {
    "development": {
      "developmentClient": true,
      "env": {
        "APP_VARIANT": "development"
      }
    },
    "production": {}
  }
}

```

Now, when you run `eas build --profile development`, the environment variable `APP_VARIANT` is set to `development` when evaluating app.config.js both locally and on the EAS Build builder.

### Using the development server

When you start your development server, you'll need to run `APP_VARIANT=development npx expo start` (or the platform equivalent if you use Windows).

A shortcut for this is to add the following script to your package.json:

package.json

Copy

```
{
  "scripts": {
    "dev": "APP_VARIANT=development npx expo start"
  }
}

```

### Using production variant

When you run `eas build --profile production` the `APP_VARIANT` variable environment is not set, and the build runs as the production variant.

> Note: If you use EAS Update to publish JavaScript updates of your app, you should be cautious to set the correct environment variables for the app variant that you are publishing for when you run the `eas update` command. See the EAS Build [Environment variables and secrets](/build/updates) for more information.

### In bare project

#### Android

In android/app/build.gradle, create a separate flavor for every build profile from eas.json that you want to build.

android/app/build.gradle

Copy

```
android {
    %%placeholder-start%%... %%placeholder-end%%
    flavorDimensions "env"
    productFlavors {
        production {
            dimension "env"
            applicationId 'com.myapp'
        }
        development {
            dimension "env"
            applicationId 'com.myapp.dev'
        }
    }
    %%placeholder-start%%... %%placeholder-end%%
}

```

> Note: Currently, EAS CLI supports only the `applicationId` field. If you use `applicationIdSuffix` inside `productFlavors` or `buildTypes` sections then this value will not be detected correctly.

Assign Android flavors to EAS Build profiles by specifying a `gradleCommand` in the eas.json:

eas.json

Copy

```
{
  "build": {
    "development": {
      "android": {
        "gradleCommand": ":app:assembleDevelopmentDebug"
      }
    },
    "production": {
      "android": {
        "gradleCommand": ":app:bundleProductionRelease"
      }
    }
  }
}

```

By default, every flavor can be built in either debug or release mode. If you want to restrict some flavor to a specific mode, see the snippet below, and modify build.gradle.

android/app/build.gradle

Copy

```
android {
    %%placeholder-start%%... %%placeholder-end%%
    variantFilter { variant ->
        def validVariants = [
                ["production", "release"],
                ["development", "debug"],
        ]
        def buildTypeName = variant.buildType*.name
        def flavorName = variant.flavors*.name

        def isValid = validVariants.any { flavorName.contains(it[0]) && buildTypeName.contains(it[1]) }
        if (!isValid) {
            setIgnore(true)
        }
    }
    %%placeholder-start%%... %%placeholder-end%%
}

```

The rest of the configuration at this point is not specific to EAS, it's the same as it would be for any Android project with flavors. There are a few common configurations that you might want to apply to your project:

* To change the name of the app built with the development profile, create a android/app/src/development/res/value/strings.xml file:

  android/app/src/development/res/value/strings.xml

  Copy

  ```
  <resources>
      <string name="app_name">MyApp - Dev</string>
  </resources>

  ```
* To change the icon of the app built with the development profile, create android/app/src/development/res/mipmap-\* directories with appropriate assets (you can copy them from android/app/src/main/res and replace the icon files).
* To specify google-services.json for a specific flavor, put it in the android/app/src/{flavor}/google-services.json file.
* To configure sentry, add `project.ext.sentryCli = [ flavorAware: true ]` to android/app/build.gradle and name your properties file android/sentry-{flavor}-{buildType}.properties (for example, android/sentry-production-release.properties)

#### iOS

Assign a different `scheme` to every build profile in eas.json:

eas.json

Copy

```
{
  "build": {
    "development": {
      "ios": {
        "buildConfiguration": "Debug",
        "scheme": "myapp-dev"
      }
    },
    "production": {
      "ios": {
        "buildConfiguration": "Release",
        "scheme": "myapp"
      }
    }
  }
}

```

Podfile should have a target defined like this:

Podfile

Copy

```
target 'myapp' do
  %%placeholder-start%%... %%placeholder-end%%
end

```

Replace it with an abstract target, where the common configuration can be copied from the old target:

Podfile

Copy

```
abstract_target 'common' do
  # put common target configuration here

  target 'myapp' do
  end

  target 'myapp-dev' do
  end
end

```

Open project in Xcode, click on the project name in the navigation panel, right click on the existing target, and click "Duplicate":

![Duplicate Xcode target](/static/images/eas-build/variants/1-ios-duplicate-target.png)

Rename the target to something more meaningful, for example, `myapp copy` -> `myapp-dev`.

Configure a scheme for the new target:

* Go to `Product` -> `Scheme` -> `Manage schemes`.
* Find scheme `myapp copy` on the list.
* Change scheme name `myapp copy` -> `myapp-dev`.
* By default, the new scheme should be marked as shared, but Xcode does not create `.xcscheme` files. To fix that, uncheck the "Shared" checkbox and check it again, after that new `.xcscheme` file should show up in the ios/myapp.xcodeproj/xcshareddata/xcschemes directory.

![Xcode scheme list](/static/images/eas-build/variants/2-scheme-list.png)

By default, the newly created target has separate Info.plist file (in the above example, it's ios/myapp copy-Info.plist). To simplify your project we recommend using the same file for all targets:

* Delete ./ios/myapp copy-Info.plist.
* Click on the new target.
* Go to `Build Settings` tab.
* Find `Packaging` section.
* Change Info.plist value - myapp copy-Info.plist -> myapp/Info.plist.
* Change `Product Bundle Identifier`.

![Xcode build settings](/static/images/eas-build/variants/3-target-build-settings.png)

To change the display name:

* Open Info.plist and add key `Bundle display name` with value `$(DISPLAY_NAME)`.
* Open `Build Settings` for both targets and find `User-Defined` section.
* Add key `DISPLAY_NAME` with the name you want to use for that target.

To change the app icon:

* Create a new image set (you can create it from the existing image set for the current icon, it's usually named `AppIcon`)
* Open `Build Settings` for the target that you want to change icon.
* Find `Asset Catalog Compiler - Options` section.
* Change `Primary App Icon Set Name` to the name of the new image set.

[Previous (EAS Build - Reference)

Troubleshoot build errors and crashes](/build-reference/troubleshooting)[Next (EAS Build - Reference)

iOS capabilities](/build-reference/ios-capabilities)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/variants.mdx)
* Last updated on January 09, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Prerequisites](/build-reference/variants/#prerequisites)[Configure development and production variants](/build-reference/variants/#configure-development-and-production-variants)[Convert app.json to app.config.js](/build-reference/variants/#convert-appjson-to-appconfigjs)[Configuration for EAS Build](/build-reference/variants/#configuration-for-eas-build)[Using the development server](/build-reference/variants/#using-the-development-server)[Using production variant](/build-reference/variants/#using-production-variant)[In bare project](/build-reference/variants/#in-bare-project)[Android](/build-reference/variants/#android)[iOS](/build-reference/variants/#ios)