How to Run and Write Tests · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [Contributing to React Native](/contributing/overview)

  + [Contributing Overview](/contributing/overview)+ [Versioning Policy](/contributing/versioning-policy)+ [How to Report a Bug](/contributing/how-to-report-a-bug)+ [How to Contribute Code](/contributing/how-to-contribute-code)+ [How to Build from Source](/contributing/how-to-build-from-source)+ [How to Run and Write Tests](/contributing/how-to-run-and-write-tests)+ [How to Open a Pull Request](/contributing/how-to-open-a-pull-request)+ [Changelogs in Pull Requests](/contributing/changelogs-in-pull-requests)+ [Contribution License Agreement](/contributing/contribution-license-agreement)+ Managing repository

                      - [Triaging GitHub Issues](/contributing/triaging-github-issues)- [Labeling GitHub Issues](/contributing/labeling-github-issues)- [Managing Pull Requests](/contributing/managing-pull-requests)- [Bots Reference](/contributing/bots-reference)

On this page

How to Run and Write Tests
==========================

Running Tests[​](#running-tests "Direct link to Running Tests")
---------------------------------------------------------------

This section is about testing your changes to React Native as a contributor. If you haven't yet, go through the steps to set up your development environment for [building projects with native code](/docs/environment-setup).

### JavaScript Tests[​](#javascript-tests "Direct link to JavaScript Tests")

The simplest way to run the JavaScript test suite is by using the following command at the root of your React Native checkout:

bash

```
yarn test  

```

This will run tests using [Jest](https://jestjs.io).

You should also make sure your code passes [Flow](https://flowtype.org/) and lint tests:

bash

```
yarn flow  
yarn lint  

```

### iOS Tests[​](#ios-tests "Direct link to iOS Tests")

Follow the [README.md](https://github.com/facebook/react-native/blob/main/packages/rn-tester/README.md) instructions in the `packages/rn-tester` directory.

Then, go back to the root of your React Native checkout and run `yarn`. This will set up your JavaScript dependencies.

At this point, you can run iOS tests by invoking the following script from the root of your React Native checkout:

bash

```
./scripts/objc-test.sh test  

```

You can also use Xcode to run iOS tests. Open `RNTester/RNTesterPods.xcworkspace` and run tests locally by pressing `Command + U` or selecting `Product` then `Test` from the menubar.

Xcode also allows running individual tests through its Test Navigator. You can also use `Command + 6` shortcut.

note

`objc-test.sh` ensures your test environment is set up to run all tests. It also disables tests that are known to be flaky or broken. Keep this in mind when running tests using Xcode. If you see an unexpected failure, see if it's disabled in `objc-test.sh` first.

#### iOS Podfile/Ruby tests[​](#ios-podfileruby-tests "Direct link to iOS Podfile/Ruby tests")

If you are making modifications to `Podfile` configurations then there are Ruby tests that can verify these.

To run the ruby tests:

bash

```
cd scripts  
sh run_ruby_tests.sh  

```

### Android Tests[​](#android-tests "Direct link to Android Tests")

The Android Unit tests do not run in an emulator, but they run on the JVM on your local machine.

To run the Android Unit tests, invoke the following script from the root of your React Native checkout:

bash

```
./gradlew test  

```

Writing Tests[​](#writing-tests "Direct link to Writing Tests")
---------------------------------------------------------------

Whenever you are fixing a bug or adding new functionality to React Native, it is a good idea to add a test that covers it. Depending on the change you're making, there are different types of tests that may be appropriate.

### JavaScript Tests[​](#javascript-tests-1 "Direct link to JavaScript Tests")

The JavaScript tests can be found inside `__test__` directories, colocated next to the files that are being tested. See [`TouchableHighlight-test.js`](https://github.com/facebook/react-native/blob/main/Libraries/Components/Touchable/__tests__/TouchableHighlight-test.js) for a basic example. You can also follow Jest's [Testing React Native Apps](https://jestjs.io/docs/en/tutorial-react-native) tutorial to learn more.

### iOS Integration Tests[​](#ios-integration-tests "Direct link to iOS Integration Tests")

React Native provides facilities to make it easier to test integrated components that require both native and JS components to communicate across the bridge.

The two main components are `RCTTestRunner` and `RCTTestModule`. `RCTTestRunner` sets up the React Native environment and provides facilities to run the tests as `XCTestCase`s in Xcode (`runTest:module` is the simplest method). `RCTTestModule` is exported to JavaScript as `NativeModules.TestModule`.

The tests themselves are written in JS, and must call `TestModule.markTestCompleted()` when they are done, otherwise the test will timeout and fail.

Test failures are primarily indicated by throwing a JS exception. It is also possible to test error conditions with `runTest:module:initialProps:expectErrorRegex:` or `runTest:module:initialProps:expectErrorBlock:` which will expect an error to be thrown and verify the error matches the provided criteria.

See the following for example usage and integration points:

* [`IntegrationTestHarnessTest.js`](https://github.com/facebook/react-native/blob/main/IntegrationTests/IntegrationTestHarnessTest.js)
* [`RNTesterIntegrationTests.m`](https://github.com/facebook/react-native/blob/main/RNTester/RNTesterIntegrationTests/RNTesterIntegrationTests.m)
* [`IntegrationTestsApp.js`](https://github.com/facebook/react-native/blob/main/IntegrationTests/IntegrationTestsApp.js)

### iOS Snapshot Tests[​](#ios-snapshot-tests "Direct link to iOS Snapshot Tests")

A common type of integration test is the snapshot test. These tests render a component, and verify snapshots of the screen against reference images using `TestModule.verifySnapshot()`, using the [`FBSnapshotTestCase`](https://github.com/facebook/ios-snapshot-test-case) library behind the scenes. Reference images are recorded by setting `recordMode = YES` on the `RCTTestRunner`, then running the tests.

Snapshots will differ slightly between 32 and 64 bit, and various OS versions, so it's recommended that you enforce tests are run with the [correct configuration](https://github.com/facebook/react-native/blob/main/scripts/.tests.env).

It's also highly recommended that all network data be mocked out, along with other potentially troublesome dependencies. See [`SimpleSnapshotTest`](https://github.com/facebook/react-native/blob/main/IntegrationTests/SimpleSnapshotTest.js) for a basic example.

If you make a change that affects a snapshot test in a pull request, such as adding a new example case to one of the examples that is snapshotted, you'll need to re-record the snapshot reference image.

To do this, change `recordMode` flag to `_runner.recordMode = YES;` in [RNTester/RNTesterSnapshotTests.m](https://github.com/facebook/react-native/blob/136666e2e7d2bb8d3d51d599fc1384a2f68c43d3/RNTester/RNTesterIntegrationTests/RNTesterSnapshotTests.m#L29), re-run the failing tests, then flip record back to `NO` and submit/update your pull request and wait to see if the CircleCI build passes.

### Android Unit Tests[​](#android-unit-tests "Direct link to Android Unit Tests")

It's a good idea to add an Android unit test whenever you are working on code that can be tested by Java/Kotlin code alone. The Android unit tests are located in `packages/react-native/ReactAndroid/src/test/`.

We recommend browsing through these to get an idea of what a good unit test might look like.

Continuous Testing[​](#continuous-testing "Direct link to Continuous Testing")
------------------------------------------------------------------------------

We use [CircleCI](https://github.com/facebook/react-native/blob/main/.circleci/config.yml) to automatically run our open source tests. CircleCI will run these tests whenever a commit is added to a pull request, as a way to help maintainers understand whether a code change introduces a regression. The tests also run on commits to the `main` and `*-stable` branches in order to keep track of the health of these branches.

There's another set of tests that run within Meta's internal test infrastructure. Some of these tests are integration tests defined by internal consumers of React Native (e.g. unit tests for a React Native surface in the Facebook app).

These tests run on every commit to the copy of React Native hosted on Facebook's source control. They also run when a pull request is imported to Facebook's source control.

If one of these tests fail, you'll need someone at Meta to take a look. Since pull requests can only be imported by Meta employees, whoever imported the pull request should be able to facilitate any details.

note

**Running CI tests locally:**
Most open source collaborators rely on CircleCI to see the results of these tests. If you'd rather verify your changes locally using the same configuration as CircleCI, CircleCI provides a [command line interface](https://circleci.com/docs/local-cli) with the ability to run jobs locally.

### F.A.Q.[​](#faq "Direct link to F.A.Q.")

#### How do I upgrade the Xcode version used in CI tests?[​](#how-do-i-upgrade-the-xcode-version-used-in-ci-tests "Direct link to How do I upgrade the Xcode version used in CI tests?")

When upgrading to a new version of Xcode, first make sure it is [supported by CircleCI](https://circleci.com/docs/testing-ios#supported-xcode-versions).

You will also need to update the test environment config to make sure tests run on an iOS Simulator that comes installed in the CircleCI machine.

This can also be found in [CircleCI's Xcode version reference](https://circleci.com/docs/2.0/testing-ios/#supported-xcode-versions) by clicking the desired version and looking under Runtimes.

You can then edit these two files:

* `.circleci/config.yml`

  Edit the `xcode:` line under `macos:` (search for `_XCODE_VERSION`).
* `scripts/.tests.env`

  Edit the `IOS_TARGET_OS` envvar to match the desired iOS Runtime.

If you intend to merge this change on GitHub, please make sure to notify a Meta employee as they'll need to update the value of `_XCODE_VERSION` used in the internal Sandcastle RN OSS iOS test in `react_native_oss.py` when they import your pull request.

[Edit this page](https://github.com/facebook/react-native-website/edit/main/docs/how-to-run-and-write-tests.md)

Last updated on **Jan 23, 2024**

[Previous

How to Build from Source](/contributing/how-to-build-from-source)[Next

How to Open a Pull Request](/contributing/how-to-open-a-pull-request)

* [Running Tests](#running-tests)
  + [JavaScript Tests](#javascript-tests)+ [iOS Tests](#ios-tests)+ [Android Tests](#android-tests)* [Writing Tests](#writing-tests)
    + [JavaScript Tests](#javascript-tests-1)+ [iOS Integration Tests](#ios-integration-tests)+ [iOS Snapshot Tests](#ios-snapshot-tests)+ [Android Unit Tests](#android-unit-tests)* [Continuous Testing](#continuous-testing)
      + [F.A.Q.](#faq)

Develop

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

Participate

* [Showcase](/showcase)* [Contributing](/contributing/overview)* [Community](/community/overview)* [Directory](https://reactnative.directory/)* [Stack Overflow](https://stackoverflow.com/questions/tagged/react-native)

Find us

* [Blog](/blog)* [X](https://x.com/reactnative)* [Bluesky](https://bsky.app/profile/reactnative.dev)* [GitHub](https://github.com/facebook/react-native)

Explore More

* [ReactJS](https://react.dev/)* [Privacy Policy](https://opensource.fb.com/legal/privacy/)* [Terms of Service](https://opensource.fb.com/legal/terms/)

[![Meta Open Source Logo](/img/oss_logo.svg)![Meta Open Source Logo](/img/oss_logo.svg)](https://opensource.fb.com/)

Copyright © 2025 Meta Platforms, Inc.