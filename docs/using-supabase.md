Using Supabase - Expo Documentation

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

Using Supabase
==============

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/using-supabase.mdx)

Add a Postgres Database and user authentication to your React Native app with Supabase.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/using-supabase.mdx)

---

[Supabase](https://supabase.com/?utm_source=expo&utm_medium=referral&utm_term=expo-react-native) is a Backend-as-a-Service (BaaS) app development platform that provides hosted backend services such as a Postgres database, user authentication, file storage, edge functions, realtime syncing, and a vector and AI toolkit. It's an open-source alternative to Google's Firebase.

Supabase automatically [generates a REST API](https://supabase.com/docs/guides/api?utm_source=expo&utm_medium=referral&utm_term=expo-react-native) from your database and employs a concept called [row level security (RLS)](https://supabase.com/docs/guides/auth/row-level-security?utm_source=expo&utm_medium=referral&utm_term=expo-react-native) to secure your data, making it possible to directly interact with your database from your React Native application without needing to go through a server!

Supabase provides a TypeScript client library called [`supabase-js`](https://supabase.com/docs/reference/javascript/introduction?utm_source=expo&utm_medium=referral&utm_term=expo-react-native) to interact with the REST API. Alternatively, Supabase also exposes a [GraphQL API](https://supabase.com/docs/guides/database/extensions/pg_graphql?utm_source=expo&utm_medium=referral&utm_term=expo-react-native) allowing you to use your favorite GraphQL client (for example, [Apollo Client](https://supabase.github.io/pg_graphql/usage_with_apollo/)) should you wish to.

Prerequisites
-------------

Head over to [database.new](https://database.new?utm_source=expo&utm_medium=referral&utm_term=expo-react-native) to create a new Supabase project.

### Get the API Keys

Get the Project URL and `anon` key from the API settings.

1. Go to the [API Settings](https://supabase.com/dashboard/project/_/settings/api) page in the Dashboard.
2. Find your Project `URL`, `anon`, and `service_role` keys on this page.

Using the Supabase TypeScript SDK
---------------------------------

Using [`supabase-js`](https://supabase.com/docs/reference/javascript/introduction?utm_source=expo&utm_medium=referral&utm_term=expo-react-native) is the most convenient way of leveraging the full power of the Supabase stack as it conveniently combines all the different services (database, auth, realtime, storage, edge functions) together.

### Install and initialize the Supabase TypeScript SDK

1

After you have created your [Expo project](/get-started/create-a-project), install `@supabase/supabase-js` and the required dependencies using the following command:

Terminal

Copy

`-Â``npx expo install @supabase/supabase-js @react-native-async-storage/async-storage react-native-url-polyfill`

2

Create a helper file to initialize the Supabase client (`@supabase/supabase-js`). You need the API URL and the `anon` key copied [earlier](/guides/using-supabase#get-the-api-keys). These variables are safe to expose in your Expo app since Supabase has [Row Level Security](https://supabase.com/docs/guides/auth/row-level-security?utm_source=expo&utm_medium=referral&utm_term=expo-react-native) enabled in the Database.

utils/supabase.ts

Copy

```
import 'react-native-url-polyfill/auto';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { createClient } from '@supabase/supabase-js';

const supabaseUrl = YOUR_REACT_NATIVE_SUPABASE_URL;
const supabaseAnonKey = YOUR_REACT_NATIVE_SUPABASE_ANON_KEY;

export const supabase = createClient(supabaseUrl, supabaseAnonKey, {
  auth: {
    storage: AsyncStorage,
    autoRefreshToken: true,
    persistSession: true,
    detectSessionInUrl: false,
  },
});

```

Now you can `import { supabase } from '/utils/supabase'` throughout your application to leverage the full power of Supabase!

Next steps
----------

[Build a User Management App

Learn how to combine Supabase Auth and Database in this quickstart guide.](https://supabase.com/docs/guides/getting-started/tutorials/with-expo-react-native?utm_source=expo&utm_medium=referral&utm_term=expo-react-native)
[Sign in with Apple

Supabase Auth supports using Sign in with Apple on the web and in native apps for iOS, macOS, watchOS or tvOS.](https://supabase.com/docs/guides/auth/social-login/auth-apple?platform=react-native&utm_source=expo&utm_medium=referral&utm_term=expo-react-native)
[Sign in with Google

Supabase Auth supports Sign in with Google on the web, native Android applications, and Chrome extensions.](https://supabase.com/docs/guides/auth/social-login/auth-google?platform=react-native&utm_source=expo&utm_medium=referral&utm_term=expo-react-native)
[Deep Linking for OAuth and Magic Links

When performing OAuth or sending magic link emails from native mobile applications, learn how to configure deep linking for Android and iOS applications.](https://supabase.com/docs/guides/auth/native-mobile-deep-linking?utm_source=expo&utm_medium=referral&utm_term=expo-react-native)
[Offline-first React Native Apps with WatermelonDB

Learn how to store your data locally and sync it with Postgres using WatermelonDB.](https://supabase.com/blog/react-native-offline-first-watermelon-db?utm_source=expo&utm_medium=referral&utm_term=expo-react-native)
[React Native file upload with Supabase Storage

Learn how to implement authentication and file upload in a React Native app.](https://supabase.com/blog/react-native-storage?utm_source=expo&utm_medium=referral&utm_term=expo-react-native)

[Previous (More - Integrations)

Using Facebook authentication](/guides/facebook-authentication)[Next (More - Integrations)

Using Firebase](/guides/using-firebase)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/using-supabase.mdx)
* Last updated on December 18, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Prerequisites](/guides/using-supabase/#prerequisites)[Get the API Keys](/guides/using-supabase/#get-the-api-keys)[Using the Supabase TypeScript SDK](/guides/using-supabase/#using-the-supabase-typescript-sdk)[Install and initialize the Supabase TypeScript SDK](/guides/using-supabase/#install-and-initialize-the-supabase-typescript-sdk)[Next steps](/guides/using-supabase/#next-steps)