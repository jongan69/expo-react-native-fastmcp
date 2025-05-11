Single Sign-On (SSO) - Expo Documentation

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

Single Sign-On (SSO)
====================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/accounts/sso.mdx)

Learn how your enterprise organization can use your identity provider to manage Expo users on your team.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/accounts/sso.mdx)

---

Single Sign-On (SSO) is available for [Enterprise plan](https://expo.dev/pricing) customers.

To get started, prepare your identity provider (IdP) for Expo SSO and gather information by following the [configuration guide for your IdP](/accounts/sso#identity-provider-support) below. Once you have done this, an owner of your Organization can follow instructions to [enable SSO](/accounts/sso#enable-sso).

If you have questions or issues, [contact us](https://expo.dev/contact) and we'll help you set up your organization.

Identity provider support
-------------------------

Expo SSO supports the following identity providers:

| Identity providers | Resources |
| --- | --- |
| [Okta](https://www.okta.com/) | [Configuration guide](https://expo.fyi/sso-setup-okta) |
| [OneLogin](https://www.onelogin.com/) | [Configuration guide](https://expo.fyi/sso-setup-onelogin) |
| [Microsoft Entra ID](https://www.microsoft.com/en-us/security/business/microsoft-entra) | [Configuration guide](https://expo.fyi/sso-setup-microsoft) |
| [Google Workspace](https://www.google.com/) | [Configuration guide](https://expo.fyi/sso-setup-google-ws) |

We implement the [OpenID Connect Discovery 1.0](https://openid.net/specs/openid-connect-discovery-1_0.html) specification and are working to verify additional compatible identity providers. If you use another identity provider and are interested in SSO, [let us know](https://expo.dev/contact).

Setting up SSO on an organization
---------------------------------

1

Log in as the Organization account owner, select the Organization, then go to Organization settings > Overview.

2

Click the Start button next to the Create SSO configuration for account option.

3

Enter the configuration details for your IdP using the information you collected during the IdP setup:

* Client ID
* Client secret
* IdP subdomain/tenant ID, if needed. Click the ? icon above the Issuer field for help with what to enter.

4

Click Create SSO Configuration.

5

The Organization settings > Overview page will now display an Update SSO configuration option. Use this option to update the client secret if it changes.

SSO user sign in
----------------

### Expo website

1

Navigate to [expo.dev/sso-login](https://expo.dev/sso-login) and enter the account name of your organization. You can create a link that pre-fills the organization name. For example, [expo.dev/sso-login/test-org](https://expo.dev/sso-login/test-org) pre-fills `test-org`.

2

Log in to your identity provider (IdP).

3

You'll be prompted to select an Expo username. This will be the username for your Expo account.

### Expo CLI

When using the Expo CLI, you can run the following command to log in to your Expo account.

Terminal

Copy

`-Â``npx expo login --sso`

You will be prompted to log in via the Expo website in a browser and will be redirected back to the CLI upon completion.

### EAS CLI

When using the EAS CLI, you can run the following command to log in to your Expo account.

Terminal

Copy

`-Â``eas login --sso`

You will be prompted to log in via the Expo website in a browser and will be redirected back to the CLI upon completion.

### Expo Go

1

Click the Continue with SSO button on the sign-in page when going through the sign-in flow.

2

Follow the [above steps](/accounts/sso#expo-website) to sign in to the Expo website.

SSO user restrictions
---------------------

SSO users are like regular users. However, there are a few known exceptions:

* SSO users can only belong to their SSO organization. They also cannot create additional organizations.
* SSO users cannot leave their SSO organization. Doing so deletes their SSO user.
* SSO users cannot log in to the Expo forums.
* SSO users cannot subscribe to EAS for their personal accounts.

SSO administration
------------------

Both new organizations and existing organizations can enable SSO as a sign in option. Organizations with existing non-SSO members can enable SSO and then direct new members to the SSO sign-in page, while existing users continue to use their current Expo credentials. To support external contributors, SSO-enabled organizations also allow inviting additional non-SSO users via email.

### Transitioning existing users to SSO

Regular users may be a member of one or many personal, team, and organization accounts while SSO users belong exclusively to their organization account. Thus, existing users cannot be directly converted into SSO users. However, a regular user who's already a member of your organization may create a second user by going to the [SSO login page](https://expo.dev/sso-login). Then, their regular user can be removed from the organization.

To transition from using a regular Expo account to an SSO account, follow these steps:

1

Check if you're already logged in at [expo.dev](https://expo.dev). If so, log out.

2

Go to the [SSO login page](https://expo.dev/sso-login) and follow the prompts, such as entering your organization name, creating a new Expo username, and logging in to your identity provider.

3

By default, your new SSO user will have the View Only role. If you need a different role, ask an Admin or Owner to update your role in [Member](https://expo.dev/accounts/%5Baccount%5D/settings/members) settings.

4

Run `eas login --sso` to switch to your new account on the CLI.

5

At this time, the Admin or Owner can remove your old user from the organization. In [Member](https://expo.dev/accounts/%5Baccount%5D/settings/members) settings, the list of organization members indicates whether a user is an SSO or non-SSO user. The Admin or Owner can click the dropdown next to the old user and click Remove member.

6

If you no longer need your old user account, log out of your new SSO account, then log in to your old account and go to [User settings](https://expo.dev/settings). Scroll down and click Delete Account. Note that this will delete any projects under your old user account. It will not affect any projects owned by the organization.

> If you wish to reuse your old username on your new SSO user account, you can go to [User settings](https://expo.dev/settings) under your old user and rename it before creating your SSO account. Alternatively, you can rename your SSO user account's Expo username after deleting your old user. While Expo usernames need to be unique, it is OK if your email address on your identity provider matches the email address of your old user.

### Remove SSO users

If someone has left your organization, remove or disable them in your IdP. Depending on the token refresh duration you configured with your IdP, the removed user will subsequently lose access to their Expo account.
If you wish to remove them ahead of that time or you wish to remove them to clean up users on your account, you may do so on the organization Member settings page:

1

Navigate to your [organization account Member settings](https://expo.dev/accounts/%5Baccount%5D/settings/members).

2

Click the dropdown next to the member you wish to delete, and click Delete SSO user.

> This will delete their personal account and all data associated with it. All data in your organization account will remain unaffected.

### Change billing or discontinue use of SSO

An active Enterprise Plan is required to continue using SSO. [Contact us](https://expo.dev/contact) if you wish to discontinue the use of SSO or change your plan.

To ensure uninterrupted access to your organization whether or not SSO is enabled, SSO organizations must keep at least one non-SSO user with the Owner role as a member.

### Delete SSO organization

Once SSO is configured for an organization, account deletion must be done manually by the Expo team. [Contact us](https://expo.dev/contact) for assistance.

[Previous (Reference - Expo accounts)

Programmatic access](/accounts/programmatic-access)[Next (Reference - Expo accounts)

Audit logs](/accounts/audit-logs)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/accounts/sso.mdx)
* Last updated on May 01, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Identity provider support](/accounts/sso/#identity-provider-support)[Setting up SSO on an organization](/accounts/sso/#setting-up-sso-on-an-organization)[SSO user sign in](/accounts/sso/#sso-user-sign-in)[Expo website](/accounts/sso/#expo-website)[Expo CLI](/accounts/sso/#expo-cli)[EAS CLI](/accounts/sso/#eas-cli)[Expo Go](/accounts/sso/#expo-go)[SSO user restrictions](/accounts/sso/#sso-user-restrictions)[SSO administration](/accounts/sso/#sso-administration)[Transitioning existing users to SSO](/accounts/sso/#transitioning-existing-users-to-sso)[Remove SSO users](/accounts/sso/#remove-sso-users)[Change billing or discontinue use of SSO](/accounts/sso/#change-billing-or-discontinue-use-of-sso)[Delete SSO organization](/accounts/sso/#delete-sso-organization)