System bars - Expo Documentation

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

System bars
===========

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/user-interface/system-bars.mdx)

Learn how to handle and customize system bars for safe areas and edge-to-edge layout in your Expo project.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/user-interface/system-bars.mdx)

---

System bars are the UI elements at the edges of the screen that provide essential device information and navigation controls. Depending on the mobile OS, they include the status bar ([Android](https://developer.android.com/design/ui/mobile/guides/foundations/system-bars) and [iOS](https://developer.apple.com/design/human-interface-guidelines/status-bars)), caption bar ([Android](https://medium.com/androiddevelopers/insets-handling-tips-for-android-15s-edge-to-edge-enforcement-872774e8839b#:~:text=or%20SHORT_EDGES.-,Caption%20bars,-When%20your%20app) only), navigation bar ([Android](https://developer.android.com/design/ui/mobile/guides/foundations/system-bars#navigation-bar) and [iOS](https://developer.apple.com/design/human-interface-guidelines/navigation-bars)), and home indicator (iOS only).

These components are used to display device information such as battery level, time, notification alerts, and provide direct interaction with the device from anywhere in the device's interface. For example, an app user can pull down the status bar to access quick settings and notifications regardless of which app they're currently using.

System bars are fundamental to the mobile experience, and understanding how to work with them properly is important for creating your app.

![System bars and navigation bars on Android and iOS.](/static/images/system-bars.png)

Handling overlaps using safe areas
----------------------------------

Some of your app's content may draw behind the system bars. To handle this, you need to position your app's content correctly by avoiding the overlap and ensuring that the controls from the system bars are present.

The following guide walks you through how to use `SafeAreaView` or a hook to apply insets directly for each edge of the screen.

[Safe areas

Learn how to add safe areas for screen components inside your Expo project.](/develop/user-interface/safe-areas)

### Safe areas and edge-to-edge layout on Android

Before [edge-to-edge on Android](https://expo.dev/blog/edge-to-edge-display-now-streamlined-for-android), it was common to have a translucent status bar and navigation bar. With this approach, the content drawn behind these bars was already underneath them, and it was typically not necessary to factor in safe areas.

Now, [with edge-to-edge on Android](https://expo.dev/blog/edge-to-edge-display-now-streamlined-for-android), you will need to use safe areas to ensure that content does not overlap with system bars.

Customizing system bars
-----------------------

System bars can be customized to match your app's design and provide better visibility in different scenarios. When using Expo, there are two libraries available for this: `expo-status-bar` and `expo-navigation-bar` (Android only).

### Status bar configuration

The status bar appears at the top of the screen on both Android and iOS. You can customize it using [`expo-status-bar`](/versions/latest/sdk/status-bar). It provides a `StatusBar` component that you can use to control the appearance of the status bar while your app is running using the [`style`](/versions/latest/sdk/status-bar#style) property or the [`setStatusBarStyle`](/versions/latest/sdk/status-bar#statusbarsetstatusbarstylestyle-animated) method:

app/\_layout.tsx

Copy

```
import { StatusBar } from 'expo-status-bar';

export default function RootLayout() {
  <>
    {/* Use light text instead of dark text in the status bar to provide more contrast with a dark background. */}
    <StatusBar style="light" />
  </>;
}

```

> Note: In Expo default template, the `style` property is set to `auto`. It automatically picks the appropriate style depending on the color scheme (light or dark mode) currently used by your app.

To control the `StatusBar` visibility, you can set the [`hidden`](/versions/latest/sdk/status-bar#hidden) property to `true` or use the [`setStatusBarHidden`](/versions/latest/sdk/status-bar#statusbarsetstatusbarhiddenhidden-animation) method.

With edge-to-edge enabled on Android, features from `expo-status-bar` that depend on an opaque status bar [are unavailable](https://developer.android.com/about/versions/15/behavior-changes-15#edge-to-edge). It's only possible to customize the style and visibility. Other properties will no-op and warn.

### Navigation bar configuration (Android only)

On Android devices, the Navigation Bar appears at the bottom of the screen. You can customize it using the [`expo-navigation-bar`](/versions/latest/sdk/navigation-bar) library. It provides a `NavigationBar` component that you can use to set the style of the navigation bar using the [`setStyle`](/versions/latest/sdk/navigation-bar#navigationbarsetstylestyle) method:

app/\_layout.tsx

Copy

```
import { NavigationBar } from 'expo-navigation-bar';
import { useEffect } from 'react';

useEffect(() => {
  if (Platform.OS === 'android') {
    // Set the navigation bar style
    NavigationBar.setStyle('dark');
  }
}, []);

```

To control the `NavigationBar` visibility, you can use the [`setVisibilityAsync`](/versions/latest/sdk/navigation-bar#navigationbarsetvisibilityasyncvisibility) method.

With edge-to-edge enabled on Android, features from `expo-navigation-bar` that depend on an opaque navigation bar [are unavailable](https://developer.android.com/about/versions/15/behavior-changes-15#edge-to-edge). It's only possible to customize the style and visibility. Other properties will no-op and warn.

[Previous (Develop - User interface)

Safe areas](/develop/user-interface/safe-areas)[Next (Develop - User interface)

Fonts](/develop/user-interface/fonts)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/user-interface/system-bars.mdx)
* Last updated on April 29, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Handling overlaps using safe areas](/develop/user-interface/system-bars/#handling-overlaps-using-safe-areas)[Safe areas and edge-to-edge layout on Android](/develop/user-interface/system-bars/#safe-areas-and-edge-to-edge-layout-on-android)[Customizing system bars](/develop/user-interface/system-bars/#customizing-system-bars)[Status bar configuration](/develop/user-interface/system-bars/#status-bar-configuration)[Navigation bar configuration (Android only)](/develop/user-interface/system-bars/#navigation-bar-configuration-android-only)