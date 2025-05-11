Bots Reference · React Native

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

Bots Reference
==============

pull-bot[​](#pull-bot "Direct link to pull-bot")
------------------------------------------------

This pull request linter bot performs basic sanity checks whenever a pull request is created. It might leave a comment on a pull request if it is unable to find a test plan or a changelog in the description, or if it notices that the pull request was not opened against the `main` branch. This bot uses [Danger](https://danger.systems), and its configuration can be found in the [`dangerfile.js`](https://github.com/facebook/react-native/blob/main/packages/react-native-bots/dangerfile.js).

analysis-bot[​](#analysis-bot "Direct link to analysis-bot")
------------------------------------------------------------

The code analysis bot collects feedback from tools such as Prettier, eslint, and Flow whenever a commit is added to a pull request. If any of these tools finds issues with the code, the bot will add these as inline review comments on the pull request. Its configuration can be found in the [`analyze_code.sh`](https://github.com/facebook/react-native/blob/main/scripts/circleci/analyze_code.sh) file in core repository.

label-actions[​](#label-actions "Direct link to label-actions")
---------------------------------------------------------------

A bot that acts on an issue or pull request based on a label. Configured in [`.github/workflows/on-issue-labeled.yml`](https://github.com/facebook/react-native/blob/main/.github/workflows/on-issue-labeled.yml).

github-actions[​](#github-actions "Direct link to github-actions")
------------------------------------------------------------------

A bot that performs actions defined in a GitHub workflow. Workflows are configured in [`.github/workflows`](https://github.com/facebook/react-native/tree/main/.github/workflows).

facebook-github-bot[​](#facebook-github-bot "Direct link to facebook-github-bot")
---------------------------------------------------------------------------------

The Facebook GitHub Bot is used across several open source projects at Meta. In the case of React Native, you will most likely encounter it when it pushes a merge commit to `main` after a pull request is successfully imported to Facebook's internal source control. It will also let authors know if they are missing a Contributor License Agreement.

react-native-bot[​](#react-native-bot "Direct link to react-native-bot")
------------------------------------------------------------------------

The React Native bot is a tool that helps us automate several processes described in this wiki. Configured in [`hramos/react-native-bot`](https://github.com/hramos/react-native-bot).

[Edit this page](https://github.com/facebook/react-native-website/edit/main/docs/bots-reference.md)

Last updated on **Sep 1, 2023**

[Previous

Managing Pull Requests](/contributing/managing-pull-requests)

* [pull-bot](#pull-bot)* [analysis-bot](#analysis-bot)* [label-actions](#label-actions)* [github-actions](#github-actions)* [facebook-github-bot](#facebook-github-bot)* [react-native-bot](#react-native-bot)

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