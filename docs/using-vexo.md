Using Vexo - Expo Documentation

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

Using Vexo
==========

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/using-vexo.mdx)

A guide on installing and configuring Vexo for real-time user analytics.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/using-vexo.mdx)

---

[Vexo](https://www.vexo.co/) provides real-time user analytics for your Expo application, helping you understand how users interact with your app, identify friction points, and improve engagement.

With a two-line integration, Vexo starts collecting data automatically, giving you actionable insights to optimize your app's user experience. If needed, you can also create custom events.

Features
--------

1. Complete Dashboard
   * Active Users
   * Session Time
   * Downloads
   * OS Distribution
   * Version Adoption
   * Geographic Insights
   * Popular Screens
2. Session Replays
   * Watch real user sessions to understand their interactions.
3. Heatmaps
   * Identify the most engaged areas of your app.
4. Funnels
   * Analyze user flows and optimize conversion rates.
5. Custom Events and Dashboard Personalization
   * Track specific user actions by creating custom events.
   * Customize your dashboard to visualize key metrics.

Getting started
---------------

1. Create an account: Sign up for a [Vexo account](https://www.vexo.co/).
2. Create a new app: You'll be prompted to create a new app. Give it a name (you can change it later), and once you submit it, you'll receive an API key.
3. Install the Vexo package: Run the following command in your project:

   npm

   yarn

   Terminal

   Copy

   `-Â``npm install vexo-analytics`

   Terminal

   Copy

   `-Â``yarn add vexo-analytics`
4. Initialize Vexo: Add the following code in your app's entry file (for example, index.js, App.js, or app/\_layout.tsx if using Expo Router):

   app/\_layout.tsx

   Copy

   ```
   import { vexo } from 'vexo-analytics';

   // You may want to wrap this with `if (!__DEV__) { ... }` to only run Vexo in production.
   vexo('YOUR_API_KEY');

   ```
5. Rebuild and run your app: Since `vexo-analytics` includes native code, you need to rebuild your application.
6. Verify integration: Go to your app's page on Vexo and you should see your first event!

Compatibility
-------------

* Expo: Vexo is compatible with [Development builds](/development/introduction) and does not require additional configuration plugins.
* Expo Go: Not supported, as Vexo requires custom native code.

Learn more about Vexo
---------------------

To learn more about using Vexo with Expo, check out the [Vexo documentation](https://docs.vexo.co/).

[Previous (More - Integrations)

Using BugSnag](/guides/using-bugsnag)[Next (More - Integrations)

Build apps for TV](/guides/building-for-tv)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/using-vexo.mdx)
* Last updated on February 21, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Features](/guides/using-vexo/#features)[Getting started](/guides/using-vexo/#getting-started)[Compatibility](/guides/using-vexo/#compatibility)[Learn more about Vexo](/guides/using-vexo/#learn-more-about-vexo)