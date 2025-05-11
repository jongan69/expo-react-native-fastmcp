Unit testing with Jest - Expo Documentation

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

Unit testing with Jest
======================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/unit-testing.mdx)

Learn how to set up and configure the jest-expo library to write unit and snapshot tests for a project with Jest.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/unit-testing.mdx)

---

[Jest](https://jestjs.io) is the most widely used unit and snapshot JavaScript testing framework. In this guide, you will learn how to set up Jest in your project, write a unit test, write a snapshot test, and best practices for structuring your tests when using Jest with React Native.

You will also use the [`jest-expo`](https://github.com/expo/expo/tree/main/packages/jest-expo) library, which is a Jest preset that mocks the native part of the Expo SDK and handles most of the configuration required for your Expo project.

Installation and configuration
------------------------------

If you have created your project using the [default Expo template](/get-started/create-a-project), you can skip this section. The `jest-expo` and other required dev dependencies are already installed and configured.

Manual installation instructions for `jest-expo`

If you have created your project using [different template](/more/create-expo#--template), follow the instructions below to install and configure `jest-expo` in your project.

1

Install `jest-expo` and other required dev dependencies in your project. Run the following command from your project's root directory:

macOS/Linux

Windows

Terminal

Copy

`-Â``npx expo install jest-expo jest @types/jest --dev`

Terminal

Copy

`-Â``npx expo install jest-expo jest @types/jest "--" --dev`

> Note: If your project is not using TypeScript, you can skip installing `@types/jest`.

2

Open package.json, add a script for running tests, and add the preset for using the base configuration from `jest-expo`:

package.json

Copy

```
{
  "scripts": {
    "test": "jest --watchAll"
    %%placeholder-start%%... %%placeholder-end%%},
  "jest": {
    "preset": "jest-expo"
  }
}

```

Additional configuration for using `transformIgnorePatterns`

You can transpile node modules your project uses by configuring [`transformIgnorePatterns`](https://jestjs.io/docs/configuration#transformignorepatterns-arraystring) in your package.json. This property takes a regex pattern as its value:

npm/Yarn

pnpm

package.json

Copy

```
"jest": {
  "preset": "jest-expo",
  "transformIgnorePatterns": [
    "node_modules/(?!((jest-)?react-native|@react-native(-community)?)|expo(nent)?|@expo(nent)?/.*|@expo-google-fonts/.*|react-navigation|@react-navigation/.*|@sentry/react-native|native-base|react-native-svg)"
  ]
}

```

package.json

Copy

```
"jest": {
  "preset": "jest-expo",
  "transformIgnorePatterns": [
    "node_modules/(?!(?:.pnpm/)?((jest-)?react-native|@react-native(-community)?|expo(nent)?|@expo(nent)?/.*|@expo-google-fonts/.*|react-navigation|@react-navigation/.*|@sentry/react-native|native-base|react-native-svg))"
  ]
}

```

Jest has many configuration options, but the above configuration should cover most of your needs. However, you can always add to this pattern list. For more details, see [Configuring Jest](https://jestjs.io/docs/configuration).

Install React Native Testing Library
------------------------------------

The [React Native Testing Library (`@testing-library/react-native`)](https://callstack.github.io/react-native-testing-library/) is a lightweight solution for testing React Native components. It provides utility functions and works with Jest.

To install it, run the following command:

macOS/Linux

Windows

Terminal

Copy

`-Â``npx expo install @testing-library/react-native --dev`

Terminal

Copy

`-Â``npx expo install @testing-library/react-native "--" --dev`

> Deprecated: If you are using the default Expo template, after installing this library, you can uninstall the `react-test-renderer` and `@types/react-test-renderer` from your project's dev dependencies. The `react-test-renderer` has been deprecated and will no longer be maintained in the future. See [React's documentation for more information](https://react.dev/warnings/react-test-renderer).

Unit test
---------

A unit test checks the smallest unit of code, usually a function. To write your first unit test, take a look at the following example:

1

Inside the app directory of your project, create a new file called index.tsx, and the following code to render a simple component:

index.tsx

Copy

```
import { PropsWithChildren } from 'react';
import { StyleSheet, Text, View } from 'react-native';

export const CustomText = ({ children }: PropsWithChildren) => <Text>{children}</Text>;

export default function HomeScreen() {
  return (
    <View style={styles.container}>
      <CustomText>Welcome!</CustomText>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});

```

2

Create a \_\_tests\_\_ directory at the root of your project's directory. If this directory already exists in your project, use that. Then, create a new file called HomeScreen-test.tsx. The `jest-expo` preset customizes the Jest configuration to also identify files with -test.ts|tsx extensions as tests.

Add the following example code in HomeScreen-test.tsx:

HomeScreen-test.tsx

Copy

```
import { render } from '@testing-library/react-native';

import HomeScreen, { CustomText } from '@/app/index';

describe('<HomeScreen />', () => {
  test('Text renders correctly on HomeScreen', () => {
    const { getByText } = render(<HomeScreen />);

    getByText('Welcome!');
  });
});

```

In the above example, the `getByText` query helps your tests find relevant element in your app's user interface and make assertion whether or not the certain element exists. The React Native Testing Library provides this query, and each [query variant](https://callstack.github.io/react-native-testing-library/docs/api/queries#query-variant) differs in its return type. For more examples and detailed API information, see the React Native Testing Library's [Queries API reference](https://callstack.github.io/react-native-testing-library/docs/api/queries).

3

Run the following command in a terminal window to execute the test:

Terminal

Copy

`-Â``npm run test`

You will see one test being passed.

Structure your tests
--------------------

Organizing your test files is important to make them easier to maintain. A common pattern is creating a \_\_tests\_\_ directory and putting all your tests inside.

An example structure of tests next to the components directory is shown below:

`__tests__`

â`ThemedText-test.tsx`

`components`

â`ThemedText.tsx`

â`ThemedView.tsx`

Alternatively, you can have multiple \_\_tests\_\_ sub-directories for different areas of your project. For example, create a separate test directory for components, and so on:

`components`

â`ThemedText.tsx`

â`__tests__`

ââ`ThemedText-test.tsx`

`utils`

â`index.tsx`

â`__tests__`

ââ`index-test.tsx`

It's all about preferences, and it is up to you to decide how you want to organize your project directory.

Snapshot test
-------------

A [snapshot test](https://jestjs.io/docs/en/snapshot-testing) is used to make sure that UI stays consistent, especially when a project is working with global styles that are potentially shared across components.

To add a snapshot test for `<HomeScreen />`, add the following code snippet in the `describe()` in HomeScreen-test.tsx:

HomeScreen-test.tsx

Copy

```
describe('<HomeScreen />', () => {
  %%placeholder-start%%... %%placeholder-end%%

  test('CustomText renders correctly', () => {
    const tree = render(<CustomText>Some text</CustomText>).toJSON();

    expect(tree).toMatchSnapshot();
  });
});

```

Run `npm run test` command, and you will see a snapshot created inside \_\_tests\_\_\\_\_snapshots\_\_ directory, and two tests passed.

Code coverage reports
---------------------

Code coverage reports can help you understand how much of your code is tested. To see the code coverage report in your project using the HTML format, in package.json, under `jest`, set the `collectCoverage` to true and use `collectCoverageFrom` to specify a list of files to ignore when collecting the coverage.

package.json

Copy

```
"jest": {
  ...
  "collectCoverage": true,
  "collectCoverageFrom": [
    "**/*.{ts,tsx,js,jsx}",
    "!**/coverage/**",
    "!**/node_modules/**",
    "!**/babel.config.js",
    "!**/expo-env.d.ts",
    "!**/.expo/**"
  ]
}

```

Run `npm run test`. You will see a coverage directory created in your project. Find the lcov-report/index.html and open it in a browser to see the coverage report.

> Usually, we don't recommend uploading index.html file to git. Add `coverage/**/*` in the .gitignore file to prevent it from being tracked.

Jest flows (optional)
---------------------

You can also use different flows to run your tests. Below are a few example scripts that you can try:

package.json

Copy

```
"scripts": {
  "test": "jest --watch --coverage=false --changedSince=origin/main",
  "testDebug": "jest -o --watch --coverage=false",
  "testFinal": "jest",
  "updateSnapshots": "jest -u --coverage=false"
  %%placeholder-start%%... %%placeholder-end%%
}

```

For more information, see [CLI Options](https://jestjs.io/docs/en/cli) in Jest documentation.

Additional information
----------------------

[React Native Testing library documentation

See React Native Testing Library documentation, which provides testing utilities and encourages good testing practices and work with Jest.](https://callstack.github.io/react-native-testing-library/docs/start/quick-start)[Testing configuration for Expo Router

Learn how to create integration tests for your app when using Expo Router.](/router/reference/testing)[E2E tests with EAS Workflows

Learn how to set up and run E2E tests on EAS Workflows with Maestro.](/eas/workflows/reference/e2e-tests)

[Previous (Develop)

Authentication](/develop/authentication)[Next (Review)

Distributing apps for review](/review/overview)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/unit-testing.mdx)
* Last updated on April 04, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Installation and configuration](/develop/unit-testing/#installation-and-configuration)[Install React Native Testing Library](/develop/unit-testing/#install-react-native-testing-library)[Unit test](/develop/unit-testing/#unit-test)[Structure your tests](/develop/unit-testing/#structure-your-tests)[Snapshot test](/develop/unit-testing/#snapshot-test)[Code coverage reports](/develop/unit-testing/#code-coverage-reports)[Jest flows (optional)](/develop/unit-testing/#jest-flows-optional)[Additional information](/develop/unit-testing/#additional-information)