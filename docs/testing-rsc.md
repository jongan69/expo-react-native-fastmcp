Testing React Server Components - Expo Documentation

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

Troubleshooting

Regulatory compliance

[Data and Privacy protection](/regulatory-compliance/data-and-privacy-protection)[GDPR compliance](/regulatory-compliance/gdpr)[HIPAA compliance](/regulatory-compliance/hipaa)[Privacy Shield](/regulatory-compliance/privacy-shield)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Testing React Server Components
===============================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/testing-rsc.mdx)

Learn about writing unit tests for React Server Components in Expo.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/testing-rsc.mdx)

Android

iOS

Web

---

> This guide refers to the experimental feature React Server Components which is still in development.

React Server Components (RSC) is a new feature in React that allows you to build components that render on the server and can be hydrated on the client. This guide provides details on how to write unit tests for RSC in your project.

Jest testing
------------

React Server Components run on Node.js. This means Jest on its own can closely emulate the server-side rendering environment, in contrast with client-based tests that require a Jest preset to communicate between Node.js and a web browser.

### Setup

While standard server rendering is web-only, Expo's universal RSC bundles custom server renderers for each platform. This means platform-specific file extensions are supported. For example, when writing Server Components for an iOS app, platform-specific extensions such as \*.ios.js and \*.native.ts will be resolved.

`jest-expo` provides a couple different presets for testing Server Components:

| Runner | Description |
| --- | --- |
| `jest-expo/rsc/android` | An Android-only runner for RSC. Uses \*.android.js, \*.native.js, and \*.js files. |
| `jest-expo/rsc/ios` | An iOS-only runner for RSC. Uses \*.ios.js, \*.native.js, and \*.js files. |
| `jest-expo/rsc/web` | A web-only runner for RSC. Uses \*.web.js and \*.js files. |
| `jest-expo/rsc` | A multi-runner that combines the above runners. |

To configure Jest for RSC, create a jest-rsc.config.js file in your project's root:

jest-rsc.config.js

Copy

```
module.exports = require('jest-expo/rsc/jest-preset');

```

Then, you can add a script such as `test:rsc` to your package.json:

package.json

Copy

```
{
  "scripts": {
    "test:rsc": "jest --config jest-rsc.config.js"
  }
}

```

### Writing tests

Tests should be written in a \_\_rsc\_tests\_\_ directory to prevent Jest from running your client tests on the server.

\_\_rsc\_tests\_\_/my-component.test.ts

Copy

```
/// <reference types="jest-expo/rsc/expect" />

import { LinearGradient } from 'expo-linear-gradient';

it(`renders to RSC`, async () => {
  const jsx = (
    <LinearGradient
      colors={['cyan', '#ff00ff', 'rgba(0,0,0,0)', 'rgba(0,255,255,0.5)']}
      testID="gradient"
    />
  );

  await expect(jsx).toMatchFlight(`1:I["src/LinearGradient.tsx",[],"LinearGradient"]
0:["$","$L1",null,{"colors":["cyan","#ff00ff","rgba(0,0,0,0)","rgba(0,255,255,0.5)"],"testID":"gradient"},null]`);
});

```

Any code you import in your test files will run in the server environment. You can import server-only modules like `react-server` and `server-only`. This is useful for determining if a library is compatible with RSC.

### Custom expect matchers

`jest-expo` for RSC adds a couple of custom matchers to Jest's `expect`:

* `toMatchFlight`: Render a JSX element using a pseudo-implementation of the render in Expo CLI and compare to a flight string.
* `toMatchFlightSnapshot`: Same as `toMatchFlight` but saves the flight string to a snapshot file.

Behind the scenes, these methods handle a part of the framework operation needed to render RSC. The component's render stream is buffered to a string and compared all at once. You can alternatively stream it manually to observe the rendering progress.

If a component fails to render, the matcher will throw an error to fail the test. In practice, the server renderer will generate an `E:` line, which will sent to the client to be thrown locally for the user.

### Running tests

You can run your tests with the `test:rsc` script:

Terminal

Copy

`-Â``yarn test:rsc --watch`

If you're using the multi-runner, you can select a specific project using the `--selectProjects` flag. The following example only runs the web platform:

Terminal

Copy

`-Â``yarn test:rsc --watch --selectProjects rsc/web`

### Environments

In an RSC bundling environment, you can import files like

Tips
----

Use the `server-only` and `client-only` modules to assert that a module should not be imported on the client or server:

my-module.js

Copy

```
import 'server-only';

```

RSC supports package exports by default. You can use the `react-server` condition to change what file is imported from a module:

package.json

Copy

```
{
  "exports": {
    ".": {
      "react-server": "./index.react-server.js",
      "default": "./index.js"
    }
  }
}

```

When bundling for RSC, all modules are bundled in React Server mode and you can opt out with the `"use client"` directive. When `"use client"` is found, the module becomes an async reference to the client module.

`"use server"` is not the opposite of `"use client"`. It is instead used to define a React Server Functions file.

[Next

Overview](/guides/overview)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/testing-rsc.mdx)
* Last updated on April 29, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Jest testing](/guides/testing-rsc/#jest-testing)[Setup](/guides/testing-rsc/#setup)[Writing tests](/guides/testing-rsc/#writing-tests)[Custom expect matchers](/guides/testing-rsc/#custom-expect-matchers)[Running tests](/guides/testing-rsc/#running-tests)[Environments](/guides/testing-rsc/#environments)[Tips](/guides/testing-rsc/#tips)