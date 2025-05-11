Programmatic access - Expo Documentation

[Docs](/)

[Blog](https://expo.dev/blog)[Changelog](https://expo.dev/changelog)[Star Us on GitHub](https://github.com/expo/expo)

Search

[Home](/)[Guides](/guides/overview)[EAS](/eas)[Reference](/versions/latest)[Learn](/tutorial/overview)

[Introduction](/eas)[Configuration with eas.json](/eas/json)[Environment variables](/eas/environment-variables)

EAS Workflows

[Get started](/eas/workflows/get-started)[Example CI/CD workflows](/eas/workflows/examples)[Syntax for EAS Workflows](/eas/workflows/syntax)[Automating EAS CLI commands](/eas/workflows/automating-eas-cli)

Reference

EAS Build

[Introduction](/build/introduction)[Create your first build](/build/setup)[Configure with eas.json](/build/eas-json)[Internal distribution](/build/internal-distribution)[Automate submissions](/build/automate-submissions)[Using EAS Update](/build/updates)[Trigger builds from CI](/build/building-on-ci)[Trigger builds from GitHub App](/build/building-from-github)[Expo Orbit](/build/orbit)

App signing

Custom builds

Reference

EAS Hosting

[Introduction](/eas/hosting/introduction)[Get started](/eas/hosting/get-started)[Deployments and aliases](/eas/hosting/deployments-and-aliases)[Environment variables](/eas/hosting/environment-variables)[Custom domain](/eas/hosting/custom-domain)[Monitoring API routes](/eas/hosting/api-routes)[Workflows](/eas/hosting/workflows)

Reference

EAS Submit

[Introduction](/submit/introduction)[Submit to the Google Play Store](/submit/android)[Submit to the Apple App Store](/submit/ios)[Configure with eas.json](/submit/eas-json)

EAS Update

[Introduction](/eas-update/introduction)[Get started](/eas-update/getting-started)

Preview

Deployment

Concepts

Troubleshooting

Reference

EAS Metadata

[Introduction](/eas/metadata)[Get started](/eas/metadata/getting-started)

Reference

EAS Insights

[Introduction](/eas-insights/introduction)

Distribution

[Overview](/distribution/introduction)[App stores best practices](/distribution/app-stores)[App transfers](/distribution/app-transfers)[Understanding app size](/distribution/app-size)

Reference

[Webhooks](/eas/webhooks)

Expo accounts

[Account types](/accounts/account-types)[Two-factor authentication](/accounts/two-factor)[Programmatic access](/accounts/programmatic-access)[Single Sign-On (SSO)](/accounts/sso)[Audit logs](/accounts/audit-logs)

Billing

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Programmatic access
===================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/accounts/programmatic-access.mdx)

Learn about types of access tokens and how to use them.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/accounts/programmatic-access.mdx)

---

When setting up CI or writing a script to help manage your projects, we recommend avoiding using your username and password to authenticate. With these credentials, anyone will be able to log in and use your account.

Instead of providing credentials, you can generate tokens that will allow you to manage each integration point separately. Anyone who has access to these tokens will be able to perform actions against your account. Treat them with the same care as a user password. In case something is leaked, you can revoke these tokens to block access.

Personal access tokens
----------------------

You can create Personal access tokens from the [Access tokens](https://expo.dev/settings/access-tokens) on your dashboard. Anyone with this token can perform actions on your behalf. That applies to all content on your Personal Account, as well as any Personal Accounts or Organizations that you have been granted access to.

Robot users and access tokens
-----------------------------

Accounts can create Robot users to take actions on resources owned by the Account. Bot Users can be assigned [a role](/accounts/account-types#manage-access) to limit the actions they are authorized to perform. Bot users cannot sign in to any Expo products, cannot own any projects themselves, and can only authenticate via an access token.

Access tokens usage
-------------------

You can use any tokens you have created to perform actions with the EAS CLI. To use tokens, you need to define an environment variable, like `EXPO_TOKEN="token"`, before running commands.

Once you set the `EXPO_TOKEN` environment variable, you can run any EAS CLI command authenticated with the token without running the `eas login` command. The `eas login` command is only used for username and password authentication. The `EXPO_TOKEN` auth method takes precedence over the username and password if both are configured.

For example, once you obtain a token, you can run the following EAS CLI command to trigger a build:

Terminal

Copy

`EXPO_TOKEN=my_token eas build`

If you are using GitHub Actions, [you can configure the `token` property](https://github.com/expo/expo-github-action#configuration-options) to include this environment variable in all the job steps.

Common situations where access tokens are useful:

* Publish or build from CI without providing your Expo username and password
* Renew a token to keep it as secure as possible; no need to reset your password and sign out of all sessions
* Give someone (or a script) one-time access to your project with limited permissions

Revoke access tokens
--------------------

In case a token is accidentally leaked, you can revoke it without changing your username and password. When you revoke the access token, you block all access to your account using this token. To do this, go to the [Access Token page](https://expo.dev/settings/access-tokens) on your dashboard and delete the token you want to revoke.

[Previous (Reference - Expo accounts)

Two-factor authentication](/accounts/two-factor)[Next (Reference - Expo accounts)

Single Sign-On (SSO)](/accounts/sso)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/accounts/programmatic-access.mdx)
* Last updated on December 27, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Personal access tokens](/accounts/programmatic-access/#personal-access-tokens)[Robot users and access tokens](/accounts/programmatic-access/#robot-users-and-access-tokens)[Access tokens usage](/accounts/programmatic-access/#access-tokens-usage)[Revoke access tokens](/accounts/programmatic-access/#revoke-access-tokens)