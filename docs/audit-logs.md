Audit logs - Expo Documentation

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

Audit logs
==========

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/accounts/audit-logs.mdx)

Learn how to track and analyze your account's activities by using the audit logs.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/accounts/audit-logs.mdx)

---

> Audit logs are available for [Enterprise plan](https://expo.dev/pricing) customers.

Audit logs record actions made with Expo Application Services (EAS) by accounts. Recorded data includes information about the affected entities, the type of modification made to them, who performed the action, and when the activity occurred.

Key points
----------

* Audit logs can only be created and never modified or deleted, they serve as a source of truth to help monitor events and debug issues occurring within accounts.
* Audit logs are available to Enterprise plan customers. When subscribed, some of the logs used internally by Expo are immediately available, while other types of logs are starting to be collected after the subscription is activated.
* Audit logs are stored for 1.5 years. If an account is deleted, its audit logs will be deleted after 90 days.
* To access them, go to Account settings > [Audit logs](https://expo.dev/accounts/%5Baccount%5D/settings/audit-logs).

![Screenshot showing the audit logs page for an account.](/static/images/accounts/audit-logs.png)

Use cases
---------

### Permission monitoring

Audit logs can track user invitations and permission changes within your organization. An example security event could include a compromised employee account that invites an attacker into an organization and changes their permission to [Admin](/accounts/account-types#manage-access).

In this scenario, audit logs would record which employee account invited the attacker and modified permissions. Since audit logs are immutable, the attacker would not be able to delete this recorded history. Other organization members will be able to review the audit logs to determine which account was compromised, take action to revoke the attacker's permissions and secure the employee's account.

### Access history

An Expo organization account can include many projects where development access is controlled by distribution certificates assigned to individual teams. When devices are granted to join these teams, it is important to track when access is granted and removed for historical record keeping. While a device may not currently be included in an Apple team, it may be useful to see who previously had access to the team in the event of an internal security incident.

The Apple devices listed within the Expo team's settings will only show devices that are currently registered to an account, but with the creation of audit logs, historical modifications of Apple teams and devices can be viewed.

Audit log entities
------------------

While we are working on adding more entities in future, the following entities are already enabled:

* Accounts
* Android App Credentials
* Android Keystore
* Apple devices
* Apple Distribution Certificate
* Apple Provisioning Profile
* Apple Team
* App Store Connect API key
* Google Service Account key
* iOS App Credentials
* Project
* User Invitations
* User Permissions

### Structure

Audit log entries include the following fields:

| Field | Description |
| --- | --- |
| Actor | The account actor that performed the particular action. |
| Entity Type | The object that was modified with one of the modification types: `CREATE`, `UPDATE`, `DELETE`. |
| Mutation Type | The type of modification: `CREATE`, `UPDATE`, `DELETE`. |
| Created At | When the particular action was performed. |

Additionally, clicking on an Audit log row, you can view the metadata relevant to that log.

![Screenshot showing the details drawer for an audit log.](/static/images/accounts/audit-logs-details.png)

Export
------

* Audit logs are available to Enterprise plan customers. When subscribed, some of the logs used internally by Expo are immediately available, while other types of logs will be collected after the subscription is activated.

Export is available with a time range of up to 30 days. The exported file will include all the fields shown on the Audit logs page except for the Message field.

[Previous (Reference - Expo accounts)

Single Sign-On (SSO)](/accounts/sso)[Next (Reference - Billing)

Overview](/billing/overview)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/accounts/audit-logs.mdx)
* Last updated on December 18, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Key points](/accounts/audit-logs/#key-points)[Use cases](/accounts/audit-logs/#use-cases)[Permission monitoring](/accounts/audit-logs/#permission-monitoring)[Access history](/accounts/audit-logs/#access-history)[Audit log entities](/accounts/audit-logs/#audit-log-entities)[Structure](/accounts/audit-logs/#structure)[Export](/accounts/audit-logs/#export)