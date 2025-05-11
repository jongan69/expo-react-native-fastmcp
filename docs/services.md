Monitoring services - Expo Documentation

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

Monitoring services
===================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/monitoring/services.mdx)

Learn how to monitor the usage of your Expo and React Native app after its release.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/monitoring/services.mdx)

---

Once your app is released, you can track anonymized usage data to give you insights on how users use your app. This data includes which updates are in use, when users experience bugs, and more.

EAS Insights
------------

Expo provides the [`expo-insights`](/eas-insights/introduction) library, which tracks information related to [EAS Update](/deploy/send-over-the-air-updates). This data includes the app version, platform, OS version, and update adoption. After you install it and release production builds on the app stores, you'll be able to see additional data on your project dashboard:

![Active user insights on the Expo dashboard.](/static/images/monitoring/monitor-your-app/expo-insights.png)

Get started with the following guide:

[EAS Insights

Learn how to use EAS Insights to monitor your app.](/eas-insights/introduction)

LogRocket
---------

You can get more insights with [LogRocket](https://logrocket.com). LogRocket records user sessions and identifies bugs as your users use your app. You can filter sessions by update IDs and also connect to your LogRocket account on the Expo dashboard to get quick access to your app's session data.

![User sessions on the LogRocket dashboard.](/static/images/monitoring/monitor-your-app/logrocket.png)

Get started with the following guide:

[Using LogRocket

Learn how to use LogRocket to monitor your app.](/guides/using-logrocket)

Sentry
------

[Sentry](http://getsentry.com/) is a crash reporting platform that provides real-time insight into production deployments with information to reproduce and fix crashes.

It notifies you of exceptions or errors that your users run into while using your app and organizes them for you on a web dashboard. Reported exceptions include stacktraces, device info, version, and other relevant context automatically. You can also provide additional context that is specific to your app, such as the current route and user ID.

![Issues on the Sentry dashboard.](/static/images/monitoring/monitor-your-app/sentry.png)

Get started with the following guide:

[Using Sentry

Learn how to use Sentry to monitor your app.](/guides/using-sentry)

Vexo
----

[Vexo](https://www.vexo.co/) helps you understand how users interact with your Expo app, identify friction points, and improve engagement. It provides real-time user analytics with a simple two-line integration and offers a complete dashboard with insights into user activity, app performance, and adoption trends, along with features like heatmaps, session replays, and more.

![The Vexo dashboard.](/static/images/monitoring/monitor-your-app/vexo.png)

Get started with the following guide:

[Using Vexo

Learn how to use Vexo to monitor your app.](/guides/using-vexo)

BugSnag
-------

[BugSnag](https://www.bugsnag.com/) is a stability monitoring solution that provides rich, end-to-end error reporting and analytics to reproduce and fix errors with speed and precision. BugSnag supports the full stack with open-source libraries for more than 50 platforms, including React Native.

Get started with the following guide:

[Using BugSnag

Learn how to use BugSnag to monitor your app.](/guides/using-bugsnag)

[Previous (Deploy)

Deploy web apps](/deploy/web)[Next (More)

Core concepts](/core-concepts)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/monitoring/services.mdx)
* Last updated on February 17, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[EAS Insights](/monitoring/services/#eas-insights)[LogRocket](/monitoring/services/#logrocket)[Sentry](/monitoring/services/#sentry)[Vexo](/monitoring/services/#vexo)[BugSnag](/monitoring/services/#bugsnag)