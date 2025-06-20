Testing configuration for Expo Router - Expo Documentation

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

[Error handling](/router/error-handling)[URL parameters](/router/reference/url-parameters)[Redirects](/router/reference/redirects)[Static Rendering](/router/reference/static-rendering)[Async routes](/router/reference/async-routes)[API Routes](/router/reference/api-routes)[Sitemap](/router/reference/sitemap)[Typed routes](/router/reference/typed-routes)[Screen tracking for analytics](/router/reference/screen-tracking)[Top-level src directory](/router/reference/src-directory)[Testing](/router/reference/testing)[Troubleshooting](/router/reference/troubleshooting)

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

Testing configuration for Expo Router
=====================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/reference/testing.mdx)

Learn how to create integration tests for your app when using Expo Router.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/reference/testing.mdx)

---

Expo Router relies on your file system, which can present challenges when setting up mocks for integration tests. Expo Router's submodule, `expo-router/testing-library`, is a set of testing utilities built on top of the popular [`@testing-library/react-native`](https://callstack.github.io/react-native-testing-library/) and allows you to quickly create in-memory Expo Router apps that are pre-configured for testing.

Configuration
-------------

Before you proceed, ensure you have set up `jest-expo` according to the [Unit testing with Jest](/develop/unit-testing) and [`@testing-library/react-native`](https://callstack.github.io/react-native-testing-library/docs/start/quick-start) in your project.

> Note: When using Expo Router, do not put your test files inside the app directory. All files inside your app directory must be either routes or layout files. Instead, use the \_\_tests\_\_ directory or a separate directory. This approach is explained in [Unit testing with Jest](/develop/unit-testing#structure-your-tests).

### Jest Native Matchers (optional)

[`@testing-library/jest-native`](https://testing-library.com/docs/ecosystem-jest-native/) provides custom Jest matchers that can be used to extend the functionality of `@testing-library/react-native`. If installed, Expo Router will automatically perform the `@testing-library/jest-native` setup.

`renderRouter`
--------------

`renderRouter` extends the functionality of [`render`](https://callstack.github.io/react-native-testing-library/docs/api#render) to simplify testing with Expo Router. It returns the same query object as [`render`](https://callstack.github.io/react-native-testing-library/docs/api#render), and is compatible with [`screen`](https://callstack.github.io/react-native-testing-library/docs/api#screen), allowing you to use the standard [query API](https://callstack.github.io/react-native-testing-library/docs/api/queries) to locate components.

`renderRouter` accepts the same [options](https://callstack.github.io/react-native-testing-library/docs/api#render-options) as `render` and introduces an additional option `initialUrl`, which sets an initial route for simulating deep-linking.

### `Inline file system`

`renderRouter(mock: Record<string, ReactComponent>, options: RenderOptions)`

`renderRouter` can provide inline-mocking of a file system by passing an object to this function as the first parameter. The keys of the object are the mock filesystem paths. Do not use leading relative (`./`) or absolute (`/`) notation when defining these paths and exclude file extension.

app.test.tsx

Copy

```
import { renderRouter, screen } from 'expo-router/testing-library';

it('my-test', async () => {
  const MockComponent = jest.fn(() => <View />);

  renderRouter(
    {
      index: MockComponent,
      'directory/a': MockComponent,
      '(group)/b': MockComponent,
    },
    {
      initialUrl: '/directory/a',
    }
  );

  expect(screen).toHavePathname('/directory/a');
});

```

### `Inline file system with `null` components`

`renderRouter(mock: string[], options: RenderOptions)`

Providing an array of strings to `renderRouter` will create an inline mock filesystem with `null` components (`{ default: () => null }`). This is useful for testing scenarios where you do not need to test the output of a route.

app.test.tsx

Copy

```
import { renderRouter, screen } from 'expo-router/testing-library';

it('my-test', async () => {
  renderRouter(['index', 'directory/a', '(group)/b'], {
    initialUrl: '/directory/a',
  });

  expect(screen).toHavePathname('/directory/a');
});

```

### `Path to fixture`

`renderRouter(fixturePath: string, options: RenderOptions)`

`renderRouter` can accept a directory path to mock an existing fixture. Ensure that the provided path is relative to the current test file.

app.test.js

Copy

```
it('my-test', async () => {
  const MockComponent = jest.fn(() => <View />);
  renderRouter('./my-test-fixture');
});

```

### `Path to the fixture with overrides`

`renderRouter({ appDir: string, overrides: Record<string, ReactComponent>}, options: RenderOptions)`

For more intricate testing scenarios, `renderRouter` can leverage both directory path and inline-mocking methods simultaneously. The `appDir` parameter takes a string representing a pathname to a directory. The overrides parameter is an inline mock that can be used to override specific paths within the `appDir`. This combination allows for fine-tuned control over the mock environment.

app.test.js

Copy

```
it('my-test', async () => {
  const MockAuthLayout = jest.fn(() => <View />);
  renderRouter({
    appDir: './my-test-fixture',
    overrides: {
      'directory/(auth)/_layout': MockAuthLayout,
    },
  });
});

```

Jest matchers
-------------

The following matches have been added to `expect` and can be used to assert values on `screen`.

### `toHavePathname()`

Assert the current pathname against a given string. The matcher uses the value of the [`usePathname`](/router/reference/hooks#usepathname) hook on the current `screen`.

app.test.ts

Copy

```
expect(screen).toHavePathname('/my-router');

```

### `toHavePathnameWithParams()`

Assert the current pathname, including URL parameters, against a given string. This is useful to assert the appearance of URL in a web browser.

app.test.ts

Copy

```
expect(screen).toHavePathnameWithParams('/my-router?hello=world');

```

### `toHaveSegments()`

Assert the current segments against an array of strings. The matcher uses the value of the [`useSegments`](/router/reference/hooks#usesegments) hook on the current `screen`.

app.test.ts

Copy

```
expect(screen).toHaveSegments(['[id]']);

```

### `useLocalSearchParams()`

Assert the current local URL parameters against an object. The matcher uses the value of the [`useLocalSearchParams`](/router/reference/hooks#uselocalsearchparams) hook on the current `screen`.

app.test.ts

Copy

```
expect(screen).useLocalSearchParams({ first: 'abc' });

```

### `useGlobalSearchParams()`

Assert the current screen's pathname that matches a value. Compares using the value of [`useGlobalSearchParams`](/router/reference/hooks#useglobalsearchparams) hook.

Assert the current global URL parameters against an object. The matcher uses the value of the [`useGlobalSearchParams`](/router/reference/hooks#useglobalsearchparams) hook on the current `screen`.

app.test.ts

Copy

```
expect(screen).useGlobalSearchParams({ first: 'abc' });

```

### `toHaveRouterState()`

An advanced matcher that asserts the current router state against an object.

app.test.ts

Copy

```
expect(screen).toHaveRouterState({
  routes: [{ name: 'index', path: '/' }],
});

```

[Previous (Expo Router - Reference)

Top-level src directory](/router/reference/src-directory)[Next (Expo Router - Reference)

Troubleshooting](/router/reference/troubleshooting)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/reference/testing.mdx)
* Last updated on December 30, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Configuration](/router/reference/testing/#configuration)[Jest Native Matchers (optional)](/router/reference/testing/#jest-native-matchers-optional)[renderRouter](/router/reference/testing/#renderrouter)[`Inline file system`](/router/reference/testing/#inline-file-system)[`Inline file system with `null` components`](/router/reference/testing/#inline-file-system-with-null-components)[`Path to fixture`](/router/reference/testing/#path-to-fixture)[`Path to the fixture with overrides`](/router/reference/testing/#path-to-the-fixture-with-overrides)[Jest matchers](/router/reference/testing/#jest-matchers)[`toHavePathname()`](/router/reference/testing/#tohavepathname)[`toHavePathnameWithParams()`](/router/reference/testing/#tohavepathnamewithparams)[`toHaveSegments()`](/router/reference/testing/#tohavesegments)[`useLocalSearchParams()`](/router/reference/testing/#uselocalsearchparams)[`useGlobalSearchParams()`](/router/reference/testing/#useglobalsearchparams)[`toHaveRouterState()`](/router/reference/testing/#tohaverouterstate)