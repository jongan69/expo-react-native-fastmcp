Account types - Expo Documentation

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

Account types
=============

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/accounts/account-types.mdx)

Learn about the different types of Expo accounts and how to use them.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/accounts/account-types.mdx)

---

An Expo account is a container that holds Expo projects and allows for different amounts of collaboration. There are two types of Expo accounts: Personal, and Organization.

The type of account you choose to put a new project depends on the nature of the project. If you are looking to collaborate or set up a workflow for your development team, always create an Organization account. For personal or hobby projects, a Personal account is sufficient.

Personal accounts
-----------------

When you [sign up for an account](https://expo.dev/signup) with Expo, a Personal account is automatically created for you. This account is a good place to work on your personal projects.

> Do not share authentication credentials for your Personal account with anyone for any reason.

Organizations
-------------

An Organization account is best used to hold projects that you wish to share with other members of a company or a group of developers. It serves as a shared container where your team can collaborate on one or multiple projects and have access to shared credentials.

You can invite other members to your Organization account, and then give these members different roles that grant a level of access within the organization. For more information, see [role privileges in Manage access](/accounts/account-types#manage-access).

Creating an organization account is useful when:

* You think you may need to transfer control of that Organization's projects in the future.
* Sharing one or multiple projects with a team of collaborators.
* More than one [Owner](/accounts/account-types#manage-access) needs to be assigned.
* Expenses need to be isolated.
* Granting different levels of access by assigning a role to each member of the organization.
* Structuring projects for different contexts. For example, when working for different clients, a new organization may be created for each client.
* Sharing an [EAS Subscription](/eas).

### Create a new Organization

If you are logged in to your Personal account, you can create a new Organization from the dashboard:

* Select your account's username in the navigation menu to open the dropdown menu.
* Select Create Organization under Organizations in the dropdown menu.

![Open the dropdown menu on the dashboard to create a new organization.](/static/images/accounts/create-an-organization.png)

* Add a name for your Organization and select the Create button.

![Enter the name of your new organization.](/static/images/accounts/enter-name-org.png)

After creating a new Organization, you are redirected to the new dashboard page for the organization. To associate a new project with the Organization, you have to add the [`owner` key](/versions/latest/config/app#owner) under the `expo` key to your project's app.json.

### Convert a Personal account into an Organization

You can convert your Personal account into an Organization when you want to share access to projects with other members and assign each member a role-based privilege.

From the User settings of your Personal account, go to [Convert your account into an organization](https://expo.dev/settings#convert-account) section to start the process.

When you are going through this process, we take a lot of care to make sure that all of the functionality that you and your users rely on will continue to work as expected:

* You can continue to deliver updates and push notifications to your users.
* You can still use any Android or iOS credentials stored on Expo's servers.
* Any integrations using your personal access token or webhooks will continue to operate and are transferred to the new designated owner.
* Your EAS subscription will continue without interruption.
* Your production apps will continue to operate without interruption.

### Invite a member

Other Expo users can be invited to join your Organization. To invite a new member:

* Navigate to [Members](https://expo.dev/settings/members) under Organization settings in the Expo dashboard.
* Click the button Invite. This will open a form to invite a member to the organization.
* In the form, enter the email of the user you want to invite and select the role they should have upon joining the organization. For more information, see [role privileges in Manage access](/accounts/account-types#manage-access).

![Example demonstrating multiple members in an organization.](/static/images/accounts/members.png)

When inviting a new member, keep in mind:

* Only members with an Owner or an Admin role can invite others.
* Members with an Owner role can grant members and invitees any role.
* Members with an Admin role can only give members and invitees up to and including Admin role (every role but Owner).

### Change the role of a member

To change the role privileges of a member, make sure you have either an [Owner or Admin role](/accounts/account-types#manage-access) and follow the steps below:

* Navigate to [Members](https://expo.dev/settings/members) under Organization settings in the Expo dashboard.
* Next to the member whose role you want to change, click on the three-dotted menu icon and change the role.

### Remove a member

To remove a member, make sure you have either an [Owner or Admin role](/accounts/account-types#manage-access) and follow the steps below:

* Navigate to [Members](https://expo.dev/settings/members) under Organization settings in the Expo dashboard.
* Next to the member you want to remove, click on the three-dotted menu icon.
* Click Remove member.

### Rename an account

Accounts can be renamed a limited number of times. Only Owners can rename accounts. To rename an account, visit Organization settings > [Overview](https://expo.dev/accounts/%5Baccount%5D/settings) and follow the steps under [Rename account](https://expo.dev/accounts/%5Baccount%5D/settings#rename-account).

![Rename Account settings panel.](/static/images/accounts/rename-account.png)

### Transfer projects between accounts

Projects can be transferred a limited number of times. A user must be an Owner or Admin on both source and destination accounts to transfer projects between them. Visit Project > Configuration > [Project settings](https://expo.dev/accounts/%5Baccount%5D/projects/%5Bproject%5D/settings) and follow the steps under Transfer project.

![Transfer Projects settings panel.](/static/images/accounts/transfer-project.png)

#### Caveats

> If you want to transfer the ownership of a project from your Personal or Organization account (source) to another person or company (destination), and you are not allowed "Owner" or "Admin" permissions on the destination account, you can create an escrow account (a new Organization account). This solves the problem that a user must be an "Owner" on the source account and either an "Owner" or "Admin" on the destination account to transfer projects between them. Once the escrow account is created, you can grant the ultimate destination account member the Owner role on the escrow account and safely transfer the project to the escrow account. The receiving person or company can then transfer it to their destination account from the escrow account without having had access to the destination account itself.

### Manage access

Access for members is managed through a role-based system. Users can have the *owner*, *admin*, *developer*, or *viewer* roles within an Organization account.

| Role | Description |
| --- | --- |
| Owner | Can take any action on an account or any projects, including deleting them. |
| Admin | Can control most settings on your account, including signing up for paid services, changing permissions of other users, and managing programmatic access. |
| Developer | Can create new projects, make new builds, release updates, and manage credentials. |
| Viewer | Can only view your projects through Expo Go but cannot modify your projects in any way. |

### Security activity

Security activity is a list of changes that happened to an account's profile. It includes changes to password, email, and 2FA authentication setup, among others.

It can be found under Overview > [User settings](https://expo.dev/settings).

[Previous (Reference)

Webhooks](/eas/webhooks)[Next (Reference - Expo accounts)

Two-factor authentication](/accounts/two-factor)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/accounts/account-types.mdx)
* Last updated on December 18, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Personal accounts](/accounts/account-types/#personal-accounts)[Organizations](/accounts/account-types/#organizations)[Create a new Organization](/accounts/account-types/#create-a-new-organization)[Convert a Personal account into an Organization](/accounts/account-types/#convert-a-personal-account-into-an-organization)[Invite a member](/accounts/account-types/#invite-a-member)[Change the role of a member](/accounts/account-types/#change-the-role-of-a-member)[Remove a member](/accounts/account-types/#remove-a-member)[Rename an account](/accounts/account-types/#rename-an-account)[Transfer projects between accounts](/accounts/account-types/#transfer-projects-between-accounts)[Manage access](/accounts/account-types/#manage-access)[Security activity](/accounts/account-types/#security-activity)