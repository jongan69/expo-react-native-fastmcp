Tailwind CSS - Expo Documentation

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

[Develop websites](/workflow/web)[Publish websites](/guides/publishing-websites)[DOM components](/guides/dom-components)[Progressive web apps](/guides/progressive-web-apps)[Tailwind CSS](/guides/tailwind)

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

Troubleshooting

Regulatory compliance

[Data and Privacy protection](/regulatory-compliance/data-and-privacy-protection)[GDPR compliance](/regulatory-compliance/gdpr)[HIPAA compliance](/regulatory-compliance/hipaa)[Privacy Shield](/regulatory-compliance/privacy-shield)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Tailwind CSS
============

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/tailwind.mdx)

Learn how to configure and use Tailwind CSS in your Expo project.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/tailwind.mdx)

---

> Standard Tailwind CSS supports only web platform. For universal support, use a library such as [NativeWind](https://www.nativewind.dev/), which allows creating styled React Native components with Tailwind CSS.

[Tailwind CSS](https://tailwindcss.com/) is a utility-first CSS framework and can be used with Metro for web projects. This guide explains how to configure your Expo project to use the framework.

Prerequisites
-------------

The following files will be modified to set the Tailwind CSS configuration:

`app.json`

`package.json`

`global.css`

`index.js`

Ensure that your project is using Metro for web. You can verify this by checking the `web.bundler` field which is set to `metro` in the app.json file.

app.json

Copy

```
{
  "expo": {
    "web": {
      "bundler": "metro"
    }
  }
}

```

Configuration
-------------

Configure Tailwind CSS in your Expo project according to the [Tailwind PostCSS documentation](https://tailwindcss.com/docs/installation/using-postcss).

v3

v4

1

Install `tailwindcss` and its required peer dependencies. Then, the run initialization command to create tailwind.config.js and post.config.js files in the root of your project.

Terminal

`# Install Tailwind and its peer dependencies`

`-Â``npx expo install tailwindcss@3 postcss autoprefixer --dev`

  
`# Create a Tailwind config file`

`-Â``npx tailwindcss init -p`

2

Add paths to all of your template files inside tailwind.config.js.

tailwind.config.js

Copy

```
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    // Ensure this points to your source code
    './app/**/*.{js,tsx,ts,jsx}',
    // If you use a `src` directory, add: './src/**/*.{js,tsx,ts,jsx}'
    // Do the same with `components`, `hooks`, `styles`, or any other top-level directories
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};

```

> If you are using Expo Router, consider using a root src directory to simplify this step. Learn more about [top-level src directory](/router/reference/src-directory).

3

Create a global.css file in the root of your project and directives for each of Tailwind's layers:

global.css

Copy

```
/* This file adds the requisite utility classes for Tailwind to work. */
@tailwind base;
@tailwind components;
@tailwind utilities;

```

4

Import the global.css file in your app/\_layout.tsx (if using Expo Router) or index.js file:

app/\_layout.tsx

Copy

```
import '../global.css';

```

index.js

Copy

```
// Import the global.css file in the index.js file:
import './global.css';

```

> If you are using [DOM components](/guides/dom-components), add this file import to each module using the `"use dom"` directive since they don't share globals.

5

You now start your project and use Tailwind CSS classes in your components.

Terminal

Copy

`-Â``npx expo start`

1

Install `tailwindcss` and its required peer dependencies:

Terminal

Copy

`# Install Tailwind and its peer dependencies`

`-Â``npx expo install tailwindcss @tailwindcss/postcss postcss --dev`

2

Add Tailwind to your PostCSS configuration

postcss.config.mjs

Copy

```
export default {
  plugins: {
    '@tailwindcss/postcss': {},
  },
};

```

3

Create a global CSS file that imports Tailwind CSS.

You can choose any name for this file. Using global.css is common practice.

global.css

Copy

```
@import 'tailwindcss';

```

4

Import your CSS file in your app/\_layout.tsx (if using Expo Router) or index.js file:

app/\_layout.tsx

Copy

```
// If using Expo Router, import your CSS file in the app/_layout.tsx file
import '../global.css';

```

index.js

Copy

```
// Otherwise import your CSS file in the index.js file:
import './global.css';

```

> If you are using [DOM components](/guides/dom-components), add this file import to each module using the `"use dom"` directive since they don't share globals.

5

You now start your project and use Tailwind CSS classes in your components.

Terminal

Copy

`-Â``npx expo start`

Usage
-----

You can use Tailwind with React DOM elements as-is:

app/index.tsx

Copy

```
export default function Index() {
  return (
    <div className="bg-slate-100 rounded-xl">
      <p className="text-lg font-medium">Welcome to Tailwind</p>
    </div>
  );
}

```

You can use the `{ $$css: true }` syntax to use Tailwind with React Native web elements:

app/index.tsx

Copy

```
import { View, Text } from 'react-native';

export default function Index() {
  return (
    <View style={{ $$css: true, _: 'bg-slate-100 rounded-xl' }}>
      <Text style={{ $$css: true, _: 'text-lg font-medium' }}>Welcome to Tailwind</Text>
    </View>
  );
}

```

Tailwind for Android and iOS
----------------------------

Tailwind does not support Android and iOS platforms. You can use a compatibility library such as [NativeWind](https://www.nativewind.dev/) for universal support.

Alternative for Android and iOS
-------------------------------

Alternatively, you can use [DOM components](/guides/dom-components) to render your Tailwind web code in a `WebView` on native.

app/index.tsx

Copy

```
'use dom';

// Remember to import the global.css file in each DOM component.
import '../global.css';

export default function Page() {
  return (
    <div className="bg-slate-100 rounded-xl">
      <p className="text-lg font-medium">Welcome to Tailwind</p>
    </div>
  );
}

```

Troubleshooting
---------------

If you have a custom `config.cacheStores` in your metro.config.js, you need to extend the Expo superclass of `FileStore`:

metro.config.js

Copy

```
// Import the Expo superclass which has support for PostCSS.
const { FileStore } = require('@expo/metro-config/file-store');

config.cacheStores = [
  new FileStore({
    root: '/path/to/custom/cache',
  }),
];

module.exports = config;

```

Ensure you don't have CSS disabled in your metro.config.js:

metro.config.js

Copy

```
/** @type {import('expo/metro-config').MetroConfig} */
const config = getDefaultConfig(__dirname, {
  // Do not disable CSS support when using Tailwind.
  isCSSEnabled: true,
});

```

[Previous (Development process - Web)

Progressive web apps](/guides/progressive-web-apps)[Next (Development process - Bundling)

Bundle with Metro](/guides/customizing-metro)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/tailwind.mdx)
* Last updated on March 26, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Prerequisites](/guides/tailwind/#prerequisites)[Configuration](/guides/tailwind/#configuration)[Usage](/guides/tailwind/#usage)[Tailwind for Android and iOS](/guides/tailwind/#tailwind-for-android-and-ios)[Alternative for Android and iOS](/guides/tailwind/#alternative-for-android-and-ios)[Troubleshooting](/guides/tailwind/#troubleshooting)