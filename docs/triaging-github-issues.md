Triaging GitHub Issues · React Native

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

Triaging GitHub Issues
======================

Start out by looking at issues that need triage, as identified by the ["Needs: Triage" label](https://github.com/facebook/react-native/issues?q=is%3Aissue+is%3Aopen+label%3A%22Needs%3A+Triage+%3Amag%3A%22).

* Is this a request for code-level help with an individual app? Would this be a better fit for Stack Overflow? If so, apply the "Resolution: For Stack Overflow" label.
* Does this issue make appropriate use of the template? If not, apply the "Needs: Template" label.
* Does this issue mention the React Native version that was used? If not, apply the "Needs: Environment Info" label.
* Does this issue include a Snack, a code example, OR a list of steps to reproduce the issue? If not, apply the "Needs: Repro" label.

note

We sometimes get issues that are quite not appropriate for the GitHub issue tracker. Add the "Type: Invalid" label, and a bot will close the issue automatically.

Once you get to this point, you can transition to parsing the content of the issue itself. Does this issue include a **clear description** of the problem?

If not, *politely* ask the issue author to update their issue with the necessary information, and apply a "Needs: Author Feedback" label.

We aim to always be friendly and helpful and expect the same from every member of our community.

Improving an Issue[​](#improving-an-issue "Direct link to Improving an Issue")
------------------------------------------------------------------------------

If the issue contains all the necessary information, take a moment to consider if the issue can still be improved in some way. Is the formatting alright? You may lightly edit the issue to improve readability as needed.

If the issue contains an unformatted block of code, surround it with three back ticks (```) to convert it into a markdown code block.

Are there any labels you can add to help categorize it better? If the issue only affects Android apps, you may add a "Platform: Android" label. Perhaps the issue only manifests itself when developing on Windows, in which case you might add the "Platform: Windows" label.

We have a long list of [labels](https://github.com/facebook/react-native/issues/labels), please take a look and see if anything might apply!

Handling Duplicates[​](#handling-duplicates "Direct link to Handling Duplicates")
---------------------------------------------------------------------------------

As you work through these issues, you will start to get a better understanding of the type of problems that get reported. You may even start noticing the same issue gets reported.

In these cases, you can close the issue and add a comment that says "Duplicate of #issue". By following this convention, GitHub will automatically mark the issue as a duplicate.

Assessing Impact[​](#assessing-impact "Direct link to Assessing Impact")
------------------------------------------------------------------------

Next up, we need to determine how severe the issue is.

### Is this a potential **release blocker**?[​](#is-this-a-potential-release-blocker "Direct link to is-this-a-potential-release-blocker")

These issues should be addressed within the next week or two, as they may prevent release coordinators from cutting a clean release candidate.

Issues that might be labeled as such could be regressions that break one of our pre-commit tests. Avoid flagging an issue as a release blocker if it has been around for some time (if the issue is already present in one or more releases, it cannot be a RC blocker by definition).

### Does this cause the app to **crash**?[​](#does-this-cause-the-app-to-crash "Direct link to does-this-cause-the-app-to-crash")

These are issues that cause a React Native to crash unexpectedly. These may lead to a poor user experience if not caught early.

### Is this a **bug**?[​](#is-this-a-bug "Direct link to is-this-a-bug")

Describes something that is not working as expected. It'd be nice to get it fixed at some point, but it's not serious enough to block the release train. Even if the issue causes a crash, if there's a reasonable workaround available, it can be classified as a regular bug.

### Is this a **good first issue**?[​](#is-this-a-good-first-issue "Direct link to is-this-a-good-first-issue")

These are issues that do not require a deep understanding and familiarity with the repo. GitHub will surface these issues to folks interested in becoming contributors. Keep in mind that issues labeled this way may not end up getting fixed right away.

[Edit this page](https://github.com/facebook/react-native-website/edit/main/docs/triaging-github-issues.md)

Last updated on **Jul 2, 2023**

[Previous

Contribution License Agreement](/contributing/contribution-license-agreement)[Next

Labeling GitHub Issues](/contributing/labeling-github-issues)

* [Improving an Issue](#improving-an-issue)* [Handling Duplicates](#handling-duplicates)* [Assessing Impact](#assessing-impact)
      + [Is this a potential **release blocker**?](#is-this-a-potential-release-blocker)+ [Does this cause the app to **crash**?](#does-this-cause-the-app-to-crash)+ [Is this a **bug**?](#is-this-a-bug)+ [Is this a **good first issue**?](#is-this-a-good-first-issue)

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