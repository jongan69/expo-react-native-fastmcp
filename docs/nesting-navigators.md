Nesting navigators - Expo Documentation

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

[Stack](/router/advanced/stack)[Tabs](/router/advanced/tabs)[Drawer](/router/advanced/drawer)[Authentication](/router/advanced/authentication)[Nesting navigators](/router/advanced/nesting-navigators)[Modals](/router/advanced/modals)[Shared routes](/router/advanced/shared-routes)[Protected routes](/router/advanced/protected)

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

Nesting navigators
==================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/advanced/nesting-navigators.mdx)

Learn how to nest navigators in Expo Router.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/advanced/nesting-navigators.mdx)

---

> Navigation UI elements (Link, Tabs, Stack) may move out of the Expo Router library in the future.

[![Using a Stack Navigator with Expo Router](https://i3.ytimg.com/vi/izZv6a99Roo/maxresdefault.jpg)

Using a Stack Navigator with Expo Router

Navigate between screens, pass params between screens, create dynamic routes, and configure the screen titles and animations.](https://www.youtube.com/watch?v=izZv6a99Roo)

Nesting navigators allow rendering a navigator inside the screen of another navigator. This guide is an extension of [React Navigation: Nesting navigators](https://reactnavigation.org/docs/nesting-navigators) to Expo Router. It provides an example of how nesting navigators work when using Expo Router.

Example
-------

Consider the following file structure which is used as an example:

`app`

â`_layout.tsx`

â`index.tsx`

â`home`

ââ`_layout.tsx`

ââ`feed.tsx`

ââ`messages.tsx`

In the above example, app/home/feed.tsx matches `/home/feed`, and app/home/messages.tsx matches `/home/messages`.

app/\_layout.tsx

Copy

```
import { Stack } from 'expo-router';

export default Stack;

```

Both app/home/\_layout.tsx and app/index.tsx below are nested in the app/\_layout.tsx layout so that it will be rendered as a stack.

app/home/\_layout.tsx

Copy

```
import { Tabs } from 'expo-router';

export default Tabs;

```

app/index.tsx

Copy

```
import { Link } from 'expo-router';

export default function Root() {
  return <Link href="/home/messages">Navigate to nested route</Link>;
}

```

Both app/home/feed.tsx and app/home/messages.tsx below are nested in the home/\_layout.tsx layout, so it will be rendered as a tab.

app/home/feed.tsx

Copy

```
import { View, Text } from 'react-native';

export default function Feed() {
  return (
    <View>
      <Text>Feed screen</Text>
    </View>
  );
}

```

app/home/messages.tsx

Copy

```
import { View, Text } from 'react-native';

export default function Messages() {
  return (
    <View>
      <Text>Messages screen</Text>
    </View>
  );
}

```

Navigate to a screen in a nested navigator
------------------------------------------

In React Navigation, navigating to a specific nested screen can be controlled by passing the screen name in params. This renders the specified nested screen instead of the initial screen for that nested navigator.

For example, from the initial screen inside the `root` navigator, you want to navigate to a screen called `media` inside `settings` (a nested navigator). In React Navigation, this is done as shown in the example below:

React Navigation

Copy

```
navigation.navigate('root', {
  screen: 'settings',
  params: {
    screen: 'media',
  },
});

```

In Expo Router, you can use `router.push()` to achieve the same result. There is no need to pass the screen name in the params explicitly.

Expo Router

Copy

```
router.push('/root/settings/media');

```

[Previous (Expo Router - Navigation patterns)

Authentication](/router/advanced/authentication)[Next (Expo Router - Navigation patterns)

Modals](/router/advanced/modals)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/advanced/nesting-navigators.mdx)
* Last updated on April 17, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Example](/router/advanced/nesting-navigators/#example)[Navigate to a screen in a nested navigator](/router/advanced/nesting-navigators/#navigate-to-a-screen-in-a-nested-navigator)