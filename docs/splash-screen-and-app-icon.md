Splash screen and app icon - Expo Documentation

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

[Splash screen and app icon](/develop/user-interface/splash-screen-and-app-icon)[Safe areas](/develop/user-interface/safe-areas)[System bars](/develop/user-interface/system-bars)[Fonts](/develop/user-interface/fonts)[Assets](/develop/user-interface/assets)[Color themes](/develop/user-interface/color-themes)[Animation](/develop/user-interface/animation)[Store data](/develop/user-interface/store-data)[Next steps](/develop/user-interface/next-steps)

Development builds

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

Splash screen and app icon
==========================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/user-interface/splash-screen-and-app-icon.mdx)

Learn how to add a splash screen and app icon to your Expo project.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/user-interface/splash-screen-and-app-icon.mdx)

---

A splash screen and an app icon are fundamental elements of a mobile app. They play an important role in the user experience and branding of the app. This guide provides steps on how to create and add them to your app.

[![Create an App Icon and Splash Screen](https://i3.ytimg.com/vi/3Bsw8a1BJoQ/maxresdefault.jpg)

Create an App Icon and Splash Screen

See a detailed walkthrough on how to create an app icon and splash screen for an Expo project.](https://www.youtube.com/watch?v=3Bsw8a1BJoQ)


---

Splash screen
-------------

A splash screen, also known as a launch screen, is the first screen a user sees when they open your app. It stays visible while the app is loading. You can also control the behavior of when a splash screen disappears by using the native [SplashScreen API](/versions/latest/sdk/splash-screen).

The [`expo-splash-screen`](/versions/latest/sdk/splash-screen) has a built-in [config plugin](/config-plugins/introduction) that lets you configure properties such as the splash icon and background color.

> Do not use Expo Go or a development build to test your splash screen. Expo Go renders your app icon while the splash screen is visible, which can interfere with testing. Development builds include `expo-dev-client`, which has its own splash screen and may cause conflicts. Instead, use a [preview build](/build/eas-json#preview-builds) or a [production build](/build/eas-json#production-builds).

1

### Create a splash screen icon

To create a splash screen icon, you can use this [Figma template](https://www.figma.com/community/file/1466490409418563617). It provides a bare minimum design for an icon and splash images for Android and iOS.

Recommended:

* Use a 1024x1024 image.
* Use a .png file.
* Use a transparent background.

2

### Export the splash icon as a .png

After creating a splash screen icon, export it as a .png and save it in the assets/images directory. By default, Expo uses splash-icon.png as the file name. If you decide to change the name of your splash screen file, make sure to use that in the next step.

> Note: Currently, only .png images are supported to use as a splash screen icon in an Expo project. If you use another image format, making a production build of your app will fail.

3

### Configure the splash screen icon

Open the app config file, and under plugins, set the following properties:

app.json

Copy

```
{
  "expo": {
    "plugins": [
      [
        "expo-splash-screen",
        {
          "backgroundColor": "#232323",
          "image": "./assets/images/splash-icon.png",
          "dark": {
            "image": "./assets/images/splash-icon-dark.png",
            "backgroundColor": "#000000"
          },
          "imageWidth": 200
        }
      ]
    ]
  }
}

```

To test your new splash screen, build your app for [internal distribution](/tutorial/eas/internal-distribution-builds) or for production, see guides on [Android](/tutorial/eas/android-production-build) and [iOS](/tutorial/eas/ios-production-build).

[Configurable splash screen properties

Learn about the configurable properties of the SplashScreen API.](/versions/latest/sdk/splash-screen#configurable-properties)

Configuring `expo-splash-screen` properties separately for Android and iOS

[`expo-splash-screen`](/versions/latest/sdk/splash-screen) also supports `android` and `ios` properties for configuring the splash screen for a specific platform. See the following example:

app.json

Copy

```
{
  "expo": {
    "plugins": [
      [
        "expo-splash-screen",
        {
          "ios": {
            "backgroundColor": "#ffffff",
            "image": "./assets/images/splash-icon.png",
            "resizeMode": "cover"
          },
          "android": {
            "backgroundColor": "#0c7cff",
            "image": "./assets/images/splash-android-icon.png",
            "imageWidth": 150
          }
        }
      ]
    ]
  }
}

```

Not using prebuild?

If your app does not use [Expo Prebuild](/workflow/prebuild) (formerly the *managed workflow*) to generate the native android and ios directories, then changes in the app config will have no effect. For more information, see [how you can customize the configuration manually](https://github.com/expo/expo/tree/main/packages/expo-splash-screen#-installation-in-bare-react-native-projects).

Troubleshooting: New splash screen not appearing on iOS

For SDK 51 and below, in iOS development builds, launch screens can sometimes remain cached between builds, making it harder to test new images. Apple recommends clearing the *derived data* directory before rebuilding, this can be done with Expo CLI by running:

Terminal

Copy

`-Â``npx expo run:ios --no-build-cache`

See [Apple's guide on testing launch screens](https://developer.apple.com/documentation/technotes/tn3118-debugging-your-apps-launch-screen) for more information.

App icon
--------

An app's icon is what your app users see on their device's home screen and app stores. Android and iOS have different and strict requirements.

1

### Create an app icon

To create an app icon, you can use this [Figma template](https://www.figma.com/community/file/1466490409418563617). It provides a bare minimum design for an icon and splash images for Android and iOS.

2

### Export the icon image as a .png

After creating an app icon, export it as .png and save it in the assets/images directory. By default, Expo uses icon.png as the file name. If you decide to use a different file name, make sure to use that in the next step.

3

### Add the icon in app config

Open the app config and add the local path as the value of [`icon`](/versions/latest/config/app#icon) property to point it to your new app icon:

app.json

Copy

```
{
  "icon": "./assets/images/icon.png"
}

```

Custom configuration tips for Android and iOS

#### Android

Further customization of the Android icon is possible using the [`android.adaptiveIcon`](/versions/latest/config/app#adaptiveicon) property, which will override both of the previously mentioned settings.

The Android Adaptive Icon is formed from two separate layers â a foreground image and a background color or image. This allows the OS to mask the icon into different shapes and also supports visual effects. For Android 13 and later, the OS supports a themed app icon that uses a wallpaper and theme to determine the color set by the device's theme.

The design you provide should follow the [Android Adaptive Icon Guidelines](https://developer.android.com/develop/ui/views/launch/icon_design_adaptive) for launcher icons. You should also:

* Use .png files.
* Use the `android.adaptiveIcon.foregroundImage` property to specify the path to your foreground image.
* Use the `android.adaptiveIcon.monochromeImage` property to specify the path to your monochrome image.
* The default background color is white; to specify a different background color, use the `android.adaptiveIcon.backgroundColor` property. You can instead specify a background image using the `android.adaptiveIcon.backgroundImage` property. Make sure that it has the same dimensions as your foreground image.

You may also want to provide a separate icon for older Android devices that do not support Adaptive Icons. You can do so with the `android.icon` property. This single icon would be a combination of your foreground and background layers.

> See [Apple best practices](https://developer.apple.com/design/human-interface-guidelines/app-icons/#Best-practices) to ensure your icon looks professional, such as testing your icon on different wallpapers and avoiding text beside your product's wordmark. Provide an icon that's at least 512x512 pixels.

#### iOS

For iOS, your app's icon should follow the [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/app-icons/). You should also:

* Use a .png file.
* 1024x1024 is a good size. If you have an Expo project created using `npx create-expo-app`, [EAS Build](/build/setup) will generate the other sizes for you. In case of a bare React Native project, generate the icons on your own. The largest size EAS Build generates is 1024x1024.
* The icon must be exactly square. For example, a 1023x1024 icon is not valid.
* Make sure the icon fills the whole square, with no rounded corners or other transparent pixels. The operating system will mask your icon when appropriate.
* Use `ios.icon` to specify different icons for various system appearances (for example, dark and tinted) can be provided. If specified, this overrides the top-level icon key in the app config file. See the example below:

app.json

Copy

```
{
  "expo": {
    "ios": {
      "icon": {
        "dark": "./assets/images/ios-dark.png",
        "light": "./assets/images/ios-light.png",
        "tinted": "./assets/images/ios-tinted.png"
      }
    }
  }
}

```

[Previous (Develop - Navigation)

Next steps](/develop/next-steps)[Next (Develop - User interface)

Safe areas](/develop/user-interface/safe-areas)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/user-interface/splash-screen-and-app-icon.mdx)
* Last updated on March 21, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Splash screen](/develop/user-interface/splash-screen-and-app-icon/#splash-screen)[Create a splash screen icon](/develop/user-interface/splash-screen-and-app-icon/#create-a-splash-screen-icon)[Export the splash icon as a .png](/develop/user-interface/splash-screen-and-app-icon/#export-the-splash-icon-as-a-png)[Configure the splash screen icon](/develop/user-interface/splash-screen-and-app-icon/#configure-the-splash-screen-icon)[App icon](/develop/user-interface/splash-screen-and-app-icon/#app-icon)[Create an app icon](/develop/user-interface/splash-screen-and-app-icon/#create-an-app-icon)[Export the icon image as a .png](/develop/user-interface/splash-screen-and-app-icon/#export-the-icon-image-as-a-png)[Add the icon in app config](/develop/user-interface/splash-screen-and-app-icon/#add-the-icon-in-app-config)