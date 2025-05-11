Using LogRocket - Expo Documentation

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

[Using Analytics](/guides/using-analytics)[Using Facebook authentication](/guides/facebook-authentication)[Using Supabase](/guides/using-supabase)[Using Firebase](/guides/using-firebase)[Using Google authentication](/guides/google-authentication)[Using ESLint and Prettier](/guides/using-eslint)[Using Next.js](/guides/using-nextjs)[Using LogRocket](/guides/using-logrocket)[Using Sentry](/guides/using-sentry)[Using BugSnag](/guides/using-bugsnag)[Using Vexo](/guides/using-vexo)[Build apps for TV](/guides/building-for-tv)[Using TypeScript](/guides/typescript)[Using In-app purchase](/guides/in-app-purchases)[Using push notifications](/guides/using-push-notifications-services)

Troubleshooting

Regulatory compliance

[Data and Privacy protection](/regulatory-compliance/data-and-privacy-protection)[GDPR compliance](/regulatory-compliance/gdpr)[HIPAA compliance](/regulatory-compliance/hipaa)[Privacy Shield](/regulatory-compliance/privacy-shield)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Using LogRocket
===============

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/using-logrocket.mdx)

A guide on installing and configuring LogRocket for session replays and error monitoring.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/using-logrocket.mdx)

---

[LogRocket](https://logrocket.com) records user sessions and identifies bugs as your users use your app. You can filter sessions by update IDs and also connect to your LogRocket account on the Expo dashboard to get quick access to your app's session data.

Install and configure LogRocket
-------------------------------

You can install the LogRocket SDK with the following command:

Terminal

Copy

`-Â``npx expo install @logrocket/react-native expo-build-properties`

Then, in your [app config](/workflow/configuration), include the LogRocket config plugin:

app.json

Copy

```
{
  "plugins": [
    [
      "expo-build-properties",
      {
        "android": {
          "minSdkVersion": 25
        }
      }
    ],
    "@logrocket/react-native"
  ]
}

```

Finally, initialize LogRocket in your app in a top-level file, like app/\_layout.tsx:

app/\_layout.tsx

Copy

```
import { useEffect } from 'react';
import * as Updates from 'expo-updates';
import LogRocket from '@logrocket/react-native';

const App = () => {
  useEffect(() => {
    LogRocket.init('<App ID>', {
      updateId: Updates.isEmbeddedLaunch ? null : Updates.updateId,
      expoChannel: Updates.channel,
    });
  }, []);
};

```

In the code above, replace `<App ID>` with your [LogRocket App ID](https://app.logrocket.com/r/settings/setup).

Connecting LogRocket on the Expo dashboard
------------------------------------------

You can link your LogRocket account and project to your Expo account and project on Expo's dashboard, so that you can see the last few sessions from your app in the deployments and updates dashboards.

Go to your [account settings](https://expo.dev/accounts/%5Baccount%5D/settings) and click Connect to authenticate with LogRocket:

![Connect LogRocket account to Expo account.](/static/images/monitoring/monitor-your-app/logrocket-connect-account.png)

Then, go to your [project settings](https://expo.dev/accounts/%5Baccount%5D/projects/%5BprojectName%5D/settings) and click Connect to link your LogRocket project with your project on Expo:

![Connect LogRocket project to Expo project.](/static/images/monitoring/monitor-your-app/logrocket-connect-project.png)

Then, you'll start to see View on LogRocket buttons in the Expo dashboard in the Deployments and Updates dashboards, along with the last few sessions from your app.

![View on LogRocket button and sessions in the deployment dashboard.](/static/images/monitoring/monitor-your-app/logrocket-view-on-logrocket.png)

Learn more about LogRocket
--------------------------

To learn more about how to use LogRocket with Expo, check out the [LogRocket documentation](https://docs.logrocket.com/reference/react-native-expo-adding-the-sdk).

[Previous (More - Integrations)

Using Next.js](/guides/using-nextjs)[Next (More - Integrations)

Using Sentry](/guides/using-sentry)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/using-logrocket.mdx)
* Last updated on February 17, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Install and configure LogRocket](/guides/using-logrocket/#install-and-configure-logrocket)[Connecting LogRocket on the Expo dashboard](/guides/using-logrocket/#connecting-logrocket-on-the-expo-dashboard)[Learn more about LogRocket](/guides/using-logrocket/#learn-more-about-logrocket)