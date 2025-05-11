Progressive web apps - Expo Documentation

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

Progressive web apps
====================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/progressive-web-apps.mdx)

Learn how to add progressive web app support to Expo websites.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/progressive-web-apps.mdx)

---

A progressive web app (or PWA for short) is a website that can be installed on the user's device and used offline. We recommend building native apps whenever possible as they have the best offline support, but PWAs are a great option for desktop users.

Favicons
--------

Expo CLI automatically generates the favicon.ico file based on the `web.favicon` field in the app.json.

```
{
  "web": {
    "favicon": "./assets/favicon.png"
  }
}

```

Alternatively, you can create a favicon.ico file in the public directory to manually specify the icon.

Manifest file
-------------

PWAs can be [configured with a manifest file](https://developer.mozilla.org/en-US/docs/Web/Manifest) that describes the app's name, icon, and other metadata.

1

Create a PWA manifest in public/manifest.json:

```
{
  "short_name": "Expo App",
  "name": "Expo Router Sample",
  "icons": [
    {
      "src": "favicon.ico",
      "sizes": "64x64 32x32 24x24 16x16",
      "type": "image/x-icon"
    },
    {
      "src": "logo192.png",
      "type": "image/png",
      "sizes": "192x192"
    },
    {
      "src": "logo512.png",
      "type": "image/png",
      "sizes": "512x512"
    }
  ],
  "start_url": ".",
  "display": "standalone",
  "theme_color": "#000000",
  "background_color": "#ffffff"
}

```

2

The files logo192.png and logo512.png are the icons that will be used when the app is installed on the user's device. These should be added to the public directory too.

`public`

â`manifest.json``PWA Manifest`

â`logo192.png``192x192 icon`

â`logo512.png``512x512 icon`

3

Now link the manifest in your HTML file. The method here depends on the output mode of your website (indicated in `web.output` in the app.jsonââdefaults to `single`).

single

static & server

If you're using a single-page app, you can link the manifest in your HTML file by first creating a template HTML in public/index.html:

Terminal

Copy

`-Â``npx expo customize public/index.html`

Then add the manifest to the `<head>` tag:

```
<link rel="manifest" href="/manifest.json" />

```

If you're using static or server rendering, the HTML entry can be dynamically created in app/+html.tsx. Here we'll link the manifest by adding a `<link>` tag to the `<head>` component:

app/+html.tsx

Copy

```
import { ScrollViewStyleReset } from 'expo-router/html';
import type { PropsWithChildren } from 'react';

// This file is web-only and used to configure the root HTML for every
// web page during static rendering.
// The contents of this function only run in Node.js environments and
// do not have access to the DOM or browser APIs.
export default function Root({ children }: PropsWithChildren) {
  return (
    <html lang="en">
      <head>
        <meta charSet="utf-8" />
        <meta httpEquiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />

        {/* Link the PWA manifest file. */}
        <link rel="manifest" href="/manifest.json" />

        {/*
          Disable body scrolling on web. This makes ScrollView components work closer to how they do on native.
          However, body scrolling is often nice to have for mobile web. If you want to enable it, remove this line.
        */}
        <ScrollViewStyleReset />

        {/* Add any additional <head> elements that you want globally available on web... */}
      </head>
      <body>{children}</body>
    </html>
  );
}

```

Service workers
---------------

Service workers are primarily used to add offline support to websites. Google's Workbox is the best way to add service workers to a website. Follow the guide for [using Workbox CLI](https://developer.chrome.com/docs/workbox/modules/workbox-cli/), and wherever it refers to a "build script" use `npx expo export -p web` instead.

> Be careful adding service workers as they are known to cause unexpected behavior on web. If you accidentally ship a service worker that aggressively caches your website, users cannot request updates easily. For the best offline mobile experience, create a native app with Expo. Unlike websites with service workers, native apps can be updated through the app store to clear the cached experience. This would be similar to resetting the user's native browser (which they may have to do if the service worker is aggressive enough). See [why service workers are suboptimal](https://github.com/facebook/create-react-app/issues/2398) for more information.

For example, here's a possible flow for setting up Workbox:

1

Create a new project with the following command:

Terminal

Copy

`-Â``npm create expo -t tabs my-app`

  

`-Â``cd my-app`

2

Now register the service worker in the HTML file. The method here depends on the output mode of your website (indicated in `web.output` in the app.jsonââdefaults to `single`).

single

static & server

Next add a service worker registration script to the root index.html.

First create a template HTML in public/index.html if one does not already exist:

Terminal

Copy

`-Â``npx expo customize public/index.html`

Then create the service worker registration script in the `<head>` tag:

```
<script>
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      navigator.serviceWorker
        .register('/sw.js')
        .then(registration => {
          console.log('Service Worker registered with scope:', registration.scope);
        })
        .catch(error => {
          console.error('Service Worker registration failed:', error);
        });
    });
  }
</script>

```

Next, create a root HTML file for the app and add the service worker registration script:

app/+html.tsx

Copy

```
import { ScrollViewStyleReset } from 'expo-router/html';
import type { PropsWithChildren } from 'react';

// This file is web-only and used to configure the root HTML for every
// web page during static rendering.
// The contents of this function only run in Node.js environments and
// do not have access to the DOM or browser APIs.
export default function Root({ children }: PropsWithChildren) {
  return (
    <html lang="en">
      <head>
        <meta charSet="utf-8" />
        <meta httpEquiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />

        {/* Bootstrap the service worker. */}
        <script dangerouslySetInnerHTML={{ __html: sw }} />

        {/*
          Disable body scrolling on web. This makes ScrollView components work closer to how they do on native.
          However, body scrolling is often nice to have for mobile web. If you want to enable it, remove this line.
        */}
        <ScrollViewStyleReset />

        {/* Add any additional <head> elements that you want globally available on web... */}
      </head>
      <body>{children}</body>
    </html>
  );
}

const sw = `
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js').then(registration => {
            console.log('Service Worker registered with scope:', registration.scope);
        }).catch(error => {
            console.error('Service Worker registration failed:', error);
        });
    });
}
`;

```

3

Now build the website before running the wizard:

Terminal

Copy

`-Â``npx expo export -p web`

4

Run the wizard command, select `dist` as the root of the app, and the defaults for everything else:

Terminal

`-Â``npx workbox-cli wizard`

  
`? What is the root of your web app (that is which directory do you deploy)? dist/``? Which file types would you like to precache? js, html, ttf, ico, json``? Where would you like your service worker file to be saved? dist/sw.js``? Where would you like to save these configuration options? workbox-config.js``? Does your web app manifest include search parameter(s) in the 'start_url', other than 'utm_' or 'fbclid' (like '?source=pwa')? No`

5

Finally, run `npx workbox-cli generateSW workbox-config.js` to generate the service worker config.

Going forward, you can add a build script in package.json to run both scripts in the correct order:

package.json

Copy

```
{
  "scripts": {
    "build:web": "expo export -p web && npx workbox-cli generateSW workbox-config.js"
  }
}

```

6

If you host your website and visit with Chrome, you can inspect the service worker by going to Application > Service Workers in the Chrome DevTools.

[Previous (Development process - Web)

DOM components](/guides/dom-components)[Next (Development process - Web)

Tailwind CSS](/guides/tailwind)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/progressive-web-apps.mdx)
* Last updated on April 28, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Favicons](/guides/progressive-web-apps/#favicons)[Manifest file](/guides/progressive-web-apps/#manifest-file)[Service workers](/guides/progressive-web-apps/#service-workers)