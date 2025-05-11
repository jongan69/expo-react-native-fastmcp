Changelogs in Pull Requests · React Native

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

Changelogs in Pull Requests
===========================

The changelog entry in your pull request serves as a sort of "tl;dr:" for your changes: do they affect Android? are these breaking changes? is something new being added?

Providing a changelog using a standardized format helps release coordinators write release notes. Please include a changelog as part of your pull request description. Your pull request description will be used as the commit message should the pull request get merged.

### Format[​](#format "Direct link to Format")

A changelog entry has the following format

```
## Changelog:  
  
[Category] [Type] - Message  

```

The "Category" field may be one of:

* **Android**, for changes that affect Android.
* **iOS**, for changes that affect iOS.
* **General**, for changes that do not fit any of the other categories.
* **Internal**, for changes that would not be relevant to developers consuming the release notes.

The "Type" field may be one of:

* **Breaking**, for breaking changes.
* **Added**, for new features.
* **Changed**, for changes in existing functionality.
* **Deprecated**, for soon-to-be removed features.
* **Removed**, for now removed features.
* **Fixed**, for any bug fixes.
* **Security**, in case of vulnerabilities.

Finally, the "Message" field may answer "what and why" on a feature level. Use this to briefly tell React Native users about notable changes.

For more detail, see [How do I make a good changelog?](https://keepachangelog.com/en/1.0.0/#how) and [Why keep a changelog?](https://keepachangelog.com/en/1.0.0/#why)

### Examples[​](#examples "Direct link to Examples")

* `[General] [Added] - Add snapToOffsets prop to ScrollView component`
* `[General] [Fixed] - Fix various issues in snapToInterval on ScrollView component`
* `[iOS] [Fixed] - Fix crash in RCTImagePicker`

### FAQ[​](#faq "Direct link to FAQ")

#### What if my pull request contains changes to both Android and JavaScript?[​](#what-if-my-pull-request-contains-changes-to-both-android-and-javascript "Direct link to What if my pull request contains changes to both Android and JavaScript?")

Use the Android category.

#### What if my pull request contains changes to both Android and iOS?[​](#what-if-my-pull-request-contains-changes-to-both-android-and-ios "Direct link to What if my pull request contains changes to both Android and iOS?")

Use the General category if the change is made in a single pull request.

#### What if my pull request contains changes to Android, iOS, and JavaScript?[​](#what-if-my-pull-request-contains-changes-to-android-ios-and-javascript "Direct link to What if my pull request contains changes to Android, iOS, and JavaScript?")

Use the General category if the change is made in a single pull request.

#### What if...?[​](#what-if "Direct link to What if...?")

Any changelog entry is better than none. If you are unsure if you have picked the right category, use the "message" field to succinctly describe your change.

These entries are used by the [`@rnx-kit/rn-changelog-generator`](https://github.com/microsoft/rnx-kit/tree/main/incubator/rn-changelog-generator) script to build a rough draft, which is then edited by a release coordinator.

Your notes will be used to add your change to the correct location in the final release notes.

[Edit this page](https://github.com/facebook/react-native-website/edit/main/docs/changelogs-in-pull-requests.md)

Last updated on **Dec 2, 2022**

[Previous

How to Open a Pull Request](/contributing/how-to-open-a-pull-request)[Next

Contribution License Agreement](/contributing/contribution-license-agreement)

* [Format](#format)* [Examples](#examples)* [FAQ](#faq)

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