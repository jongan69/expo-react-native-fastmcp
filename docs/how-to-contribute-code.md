How to Contribute Code · React Native

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

How to Contribute Code
======================

Thank you for your interest in contributing to React Native! From commenting on and triaging issues, to reviewing and sending PRs, [all contributions are welcome](/contributing/overview). In this document, we'll cover the steps to contributing code to React Native.

If you are eager to start contributing code right away, we have a list of [`good first issues`](https://github.com/facebook/react-native/labels/good%20first%20issue) that contain bugs which have a relatively limited scope.
Issues labeled [`help wanted`](https://github.com/facebook/react-native/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+label%3A%22help+wanted+%3Aoctocat%3A%22+sort%3Aupdated-desc+) are good issues to submit a PR for.

Prerequisites[​](#prerequisites "Direct link to Prerequisites")
---------------------------------------------------------------

info

Please refer to the [Environment Setup](/docs/environment-setup) guide to setup required tools and the development environment based on the platform us use and platform which you want to develop for.

Development Workflow[​](#development-workflow "Direct link to Development Workflow")
------------------------------------------------------------------------------------

After cloning React Native, open the directory and run `yarn` to install its dependencies.

Now you are set up to run several commands:

* `yarn start` starts the Metro packager server.
* `yarn lint` checks the code style.
* `yarn format` automatically formats your code.
* `yarn test` runs the Jest-based JavaScript test suite.
  + `yarn test --watch` runs an interactive JavaScript test watcher.
  + `yarn test <pattern>` runs JavaScript tests with matching filenames.
* `yarn flow` runs the [Flow](https://flowtype.org/) typechecks.
  + `yarn flow-check-android` does a full Flow check over `*.android.js` files.
  + `yarn flow-check-ios` does a full Flow check over `*.ios.js` files.
* `yarn test-typescript` runs the [TypeScript](https://www.typescriptlang.org/) typechecks.
* `yarn test-ios` runs the iOS test suite (macOS required).
* `yarn build` builds all configured packages — in general, this command only needs to be run by CI ahead of publishing.
  + Packages which require a build are configured in [scripts/build/config.js](https://github.com/facebook/react-native/blob/main/scripts/build/config.js).

Testing your Changes[​](#testing-your-changes "Direct link to Testing your Changes")
------------------------------------------------------------------------------------

Tests help us prevent regressions from being introduced to the codebase. We recommend running `yarn test` or the platform-specific scripts above to make sure you don't introduce any regressions as you work on your change.

The GitHub repository is [continuously tested](/contributing/how-to-run-and-write-tests#continuous-testing) using CircleCI, the results of which are available through the Checks functionality on [commits](https://github.com/facebook/react-native/commits/main) and pull requests.

You can learn more about running and writing tests on the [How to Run and Write Tests](/contributing/how-to-run-and-write-tests) page.

Coding Style[​](#coding-style "Direct link to Coding Style")
------------------------------------------------------------

We use Prettier to format our JavaScript code. This saves you time and energy as you can let Prettier fix up any formatting issues automatically through its editor integrations, or by manually running `yarn run prettier`. We also use a linter to catch styling issues that may exist in your code. You can check the status of your code styling by running `yarn run lint`.

However, there are still some styles that the linter cannot pick up, notably in Java or Objective-C code.

### Objective-C[​](#objective-c "Direct link to Objective-C")

* Space after `@property` declarations
* Brackets on *every* `if`, on the *same* line
* `- method`, `@interface`, and `@implementation` brackets on the following line
* *Try* to keep it around 80 characters line length (sometimes it's not possible...)
* `*` operator goes with the variable name (e.g. `NSObject *variableName;`)

### Java[​](#java "Direct link to Java")

* If a method call spans multiple lines closing bracket is on the same line as the last argument.
* If a method header doesn't fit on one line each argument goes on a separate line.
* 100 character line length

Sending a Pull Request[​](#sending-a-pull-request "Direct link to Sending a Pull Request")
------------------------------------------------------------------------------------------

Code-level contributions to React Native generally come in the form of [a pull request](https://help.github.com/en/articles/about-pull-requests). The process of proposing a change to React Native can be summarized as follows:

1. Fork the React Native repository and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes, either locally or on CI once you opened a pull request.
5. Make sure your code lints (for example via `yarn lint --fix`).
6. Push the changes to your fork.
7. Create a pull request to the React Native repository.
8. Review and address comments on your pull request.
9. A bot may comment with suggestions. Generally we ask you to resolve these first before a maintainer will review your code.
10. If you haven't already, submit the [Contributor License Agreement ("CLA")](#contributor-license-agreement).

If all goes well, your pull request will be merged. If it is not merged, maintainers will do their best to explain their reasoning.

If this is your first time sending a pull request, we have created a [step-by-step guide to help you get started](/contributing/how-to-open-a-pull-request). For more detailed information on how pull requests are handled, see the [Managing Pull Requests page](/contributing/managing-pull-requests).

### Contributor License Agreement[​](#contributor-license-agreement "Direct link to Contributor License Agreement")

In order to accept your pull request, we need you to submit a [Contributor License Agreement (CLA)](/contributing/contribution-license-agreement). You only need to do this once to work on any of Meta's open source projects. It only takes a minute, so you can do it while you wait for your dependencies to install.

License[​](#license "Direct link to License")
---------------------------------------------

By contributing to React Native, you agree that your contributions will be licensed under the [LICENSE](https://github.com/facebook/react-native/blob/main/LICENSE) file in the root directory of the React Native repository.

[Edit this page](https://github.com/facebook/react-native-website/edit/main/docs/how-to-contribute-code.md)

Last updated on **Apr 5, 2024**

[Previous

How to Report a Bug](/contributing/how-to-report-a-bug)[Next

How to Build from Source](/contributing/how-to-build-from-source)

* [Prerequisites](#prerequisites)* [Development Workflow](#development-workflow)* [Testing your Changes](#testing-your-changes)* [Coding Style](#coding-style)
        + [Objective-C](#objective-c)+ [Java](#java)* [Sending a Pull Request](#sending-a-pull-request)
          + [Contributor License Agreement](#contributor-license-agreement)* [License](#license)

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