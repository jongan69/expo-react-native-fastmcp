Platform-specific Modules - Expo Documentation

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

Expo Router

[Introduction](/router/introduction)[Installation](/router/installation)

Router 101

Navigation patterns

Advanced

[Platform-specific Modules](/router/advanced/platform-specific-modules)[Customizing links](/router/advanced/native-intent)[Settings](/router/advanced/router-settings)[Apple Handoff](/router/advanced/apple-handoff)[Custom tabs](/router/advanced/custom-tabs)

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

Platform-specific Modules
=========================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/advanced/platform-specific-modules.mdx)

Learn how to switch modules based on the platform in Expo Router.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/advanced/platform-specific-modules.mdx)

---

> Platform specific extensions were added in Expo Router `3.5.0`. Follow this guide only if you are using an older version of Expo Router.

While building your app, you may want to show specific content based on the current platform. Platform-specific modules can make the experience more native to a given platform. The following sections describe the ways you can achieve this with Expo Router.

Platform module
---------------

You can use the [`Platform`](https://reactnative.dev/docs/platform-specific-code#platform-module) module from React Native to detect the current platform and render the appropriate content based on the result. For example, you can render a `Tabs` layout on native and a custom layout on the web.

app/\_layout.tsx

Copy

```
import { Platform } from 'react-native';
import { Link, Slot, Tabs } from 'expo-router';

export default function Layout() {
  if (Platform.OS === 'web') {
    // Use a basic custom layout on web.
    return (
      <div style={{ flex: 1 }}>
        <header>
          <Link href="/">Home</Link>
          <Link href="/settings">Settings</Link>
        </header>
        <Slot />
      </div>
    );
  }
  // Use a native bottom tabs layout on native platforms.
  return (
    <Tabs>
      <Tabs.Screen name="index" options={{ title: 'Home' }} />
      <Tabs.Screen name="settings" options={{ title: 'Settings' }} />
    </Tabs>
  );
}

```

Platform specific extensions
----------------------------

Metro bundler's platform-specific extensions (for example, .ios.tsx or .native.tsx) are not supported in the app directory. This ensures that routes are universal across platforms for deep linking. However, you can create platform-specific files outside the app directory and use them from within the app directory.

Consider the following project:

`app`

â`_layout.tsx`

â`index.tsx`

â`about.tsx`

`components`

â`about.tsx`

â`about.ios.tsx`

â`about.web.tsx`

For example, the designs require you to build different `about` screens for each platform. In that case, you can create a component for each platform in the components directory using platform extensions. When imported, Metro will ensure the correct component version is used based on the current platform. You can then re-export the component as a screen in the app directory.

app/about.tsx

Copy

```
export { default } from '../components/about';

```

> Best practice: Always provide a file without a platform extension to ensure every platform has a default implementation.

[Previous (Expo Router - Navigation patterns)

Protected routes](/router/advanced/protected)[Next (Expo Router - Advanced)

Customizing links](/router/advanced/native-intent)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/advanced/platform-specific-modules.mdx)
* Last updated on July 10, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Platform module](/router/advanced/platform-specific-modules/#platform-module)[Platform specific extensions](/router/advanced/platform-specific-modules/#platform-specific-extensions)