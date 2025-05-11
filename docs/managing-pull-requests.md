Managing Pull Requests · React Native

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

Managing Pull Requests
======================

Reviewing a pull request can take a considerable amount of time. In some cases, the review might require more time to perform than it took someone to write and submit their changes! It's therefore necessary to do some preliminary work to ensure each pull request is in a good state to be reviewed.

A pull request should consist of three main sections:

* A summary. This helps us understand the motivation behind the changes.
* A changelog. This helps us write the release notes. It also serves as a brief summary of your changes.
* A test plan. This might be the most important part of your pull request. A test plan should be a reproducible step-by-step guide so that a reviewer can verify your change is working as intended. It's also a good idea to attach screenshots or videos for user visible changes.

Any pull request may require a deeper understanding of some area of React Native that you may not be familiar with. Even if you don't feel like you are the right person to review a pull request, you may still help by adding labels or asking the author for more information.

Reviewing PRs[​](#reviewing-prs "Direct link to Reviewing PRs")
---------------------------------------------------------------

Pull Requests need to be reviewed and approved using GitHub's review feature before they can be merged. While anyone has the ability to review and approve a pull request, we typically only consider a pull request ready to be merged when the approval comes from one of the [contributors](https://github.com/facebook/react-native/blob/main/ECOSYSTEM.md).

So you've found a pull request that you feel confident reviewing. Please make use of the GitHub Review feature, and clearly and politely communicate any suggested changes.

Consider starting with pull requests that have been flagged as lacking a changelog or test plan.

* [PRs that appear to lack a changelog](https://github.com/facebook/react-native/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Aopen+label%3A%22Missing+Changelog%22+) - take a look and see if you can add the changelog yourself by editing the PR. After doing so, remove the "Missing Changelog" label.
* [PRs that are missing a test plan](https://github.com/facebook/react-native/pulls?q=is%3Apr+label%3A%22Missing+Test+Plan%22+is%3Aclosed) - open the pull request and look for a test plan. If the test plan looks sufficient, remove the "Missing Test Plan"" label. If there is no test plan, or it looks incomplete, add a comment politely asking the author to consider adding a test plan.

A pull request must pass all the tests before it can be merged. They run on every commit on `main` and pull request. A quick way to help us get pull requests ready for review is to [search for pull requests that are failing the pre-commit tests](https://github.com/facebook/react-native/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Aopen+label%3A%22CLA+Signed%22+status%3Afailure+) and determine if they need to be revised. The failing test is usually listed near the bottom of the thread, under "Some checks were not successful."

* Take a quick glance at the [latest tests runs on main](https://circleci.com/gh/facebook/react-native/tree/main). Is `main` green? If so,
  + Does it look like the failure may be related to the changes in this pull request? Ask the author to investigate.
  + Even if `main` is currently green, consider the possibility that the commits in the pull requests may be based off a commit from a point in time when `main` was broken. If you believe this may be the case, ask the author to rebase their changes on top of `main` in order to pull in any fixes that may have landed after they started working on the pull request.
* If `main` appears to be broken, look for any [issues labeled as "CI Test Failure"](https://github.com/facebook/react-native/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+label%3A%22%E2%9D%8CCI+Test+Failure%22+).
  + If you find an issue that seems related to the failure on `main`, go back to the pull request and thank the author for proposing these changes, and let them know that the test failure may be unrelated to their particular change (do not forget to link back to the CI Test Failure issue, as this will help the author know when they can try running tests again).
  + If you cannot find an existing CI Test Failure issue that describes the problem you've observed on `main`, please submit a new issue and use the "CI Test Failure" label to let others know that `main` is broken (see [this issue](https://github.com/facebook/react-native/issues/23108) for an example).

How we prioritize PRs[​](#how-we-prioritize-prs "Direct link to How we prioritize PRs")
---------------------------------------------------------------------------------------

Members of the React Native team at Meta aim to review pull requests quickly and most PRs will get a response within a week.

How does a PR get merged?[​](#how-does-a-pr-get-merged "Direct link to How does a PR get merged?")
--------------------------------------------------------------------------------------------------

The React Native GitHub repository is actually a mirror of a subdirectory from one of Meta's monorepos. Pull requests are therefore not merged in the traditional sense. Instead, they need to be imported into Meta's internal code review system as a ["diff"](https://www.phacility.com/phabricator/differential/).

Once imported, the changes will go through a suite of tests. Some of these tests are land-blocking, meaning they need to succeed before the contents of the diff can be merged. Meta always runs React Native from `main` and some changes may require a Facebook employee to attach internal changes to your pull request before it can be merged. For example, if you rename a module name, all Facebook internal callsites have to be updated in the same change in order to merge it. If the diff lands successfully, the changes will eventually get synced back to GitHub by [ShipIt](https://github.com/facebook/fbshipit) as a single commit.

Meta employees are using a custom browser extension for GitHub that can import a pull request in one of two ways: the pull request can be "landed to fbsource", meaning it will be imported and the resulting diff will be approved automatically, and barring any failures, the changes will eventually sync back to `main`. A pull request may also be "imported to Phabricator", meaning the changes will be copied to an internal diff that will require further review and approval before it can land.

![](/img/importing-pull-requests.png)

Screenshot of the custom browser extension. The button "Import to fbsource" is used to import a Pull Request internally.

Bots[​](#bots "Direct link to Bots")
------------------------------------

As you review and work on pull requests, you might encounter comments left by a handful of GitHub bot accounts. These bots have been set up to aid in the pull request review process. See the [Bots Reference](/contributing/bots-reference) to learn more.

Pull Request Labels[​](#pull-request-labels "Direct link to Pull Request Labels")
---------------------------------------------------------------------------------

* `Merged`: Applied to a closed PR to indicate that its changes have been incorporated into the core repository. This label is necessary because pull requests are not merged directly on GitHub. Instead, a patch with the PR's changes is imported and queued up for code review. Once approved, the result of applying those changes on top of Meta's internal monorepository gets synced out to GitHub as a new commit. GitHub does not attribute that commit back to the original PR, hence the need for a label that communicates the PR's true status.
* `Blocked on FB`: The PR has been imported, but the changes have not yet been applied.

[Edit this page](https://github.com/facebook/react-native-website/edit/main/docs/managing-pull-requests.md)

Last updated on **Jun 21, 2022**

[Previous

Labeling GitHub Issues](/contributing/labeling-github-issues)[Next

Bots Reference](/contributing/bots-reference)

* [Reviewing PRs](#reviewing-prs)* [How we prioritize PRs](#how-we-prioritize-prs)* [How does a PR get merged?](#how-does-a-pr-get-merged)* [Bots](#bots)* [Pull Request Labels](#pull-request-labels)

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