Apple Developer Program roles and permissions for EAS Build - Expo Documentation

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

[App credentials](/app-signing/app-credentials)[Automatically managed credentials](/app-signing/managed-credentials)[Local credentials](/app-signing/local-credentials)[Existing credentials](/app-signing/existing-credentials)[Sync credentials between remote and local sources](/app-signing/syncing-credentials)[Security](/app-signing/security)[Apple Developer Program roles and permissions](/app-signing/apple-developer-program-roles-and-permissions)

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

Billing

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Apple Developer Program roles and permissions for EAS Build
===========================================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/app-signing/apple-developer-program-roles-and-permissions.mdx)

Learn about the Apple Developer account membership requirements for creating an EAS Build.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/app-signing/apple-developer-program-roles-and-permissions.mdx)

---

An Apple Developer account with permissions to create [app signing credentials](/app-signing/managed-credentials#generating-app-signing-credentials), such as certificates, identifiers, and provisioning profiles, is required when using EAS Build to create iOS device builds. These credentials can be generated when submitting the build by logging into your Apple Account from the EAS CLI, or they can be uploaded to your Expo account by an authorized user, so users without Apple Developer account access can create builds using the uploaded credentials.

On individual Apple Developer accounts, only the Account Holder role can generate app signing credentials. On an organization Apple Developer account, the Account Holder and Admin roles can always generate app signing credentials, and the App Manager role can generate credentials when a user with this role has Access to Certificates, Identifiers, and Profiles enabled in their App Store Connect user permissions.

![Access to Certificates, Identifiers, and Profiles settings in App Store Connect.](/static/images/apple-access-settings.png)

Access to Certificates, Identifiers, and Profiles settings in App Store Connect.

This guide provides steps that an authorized user can follow to ensure app signing credentials are generated and available to their team members who use EAS. It also provides steps for the team developer to create an EAS Build by using pre-generated credentials.

> See [Apple's documentation on Program Roles](https://developer.apple.com/support/roles/) for details on the different roles and their permissions based on the type of Developer account and the permissions that are required for each role.

Steps for Apple Developer account's authorized user
---------------------------------------------------

The authorized user of the Apple Developer account needs to generate the following credentials:

* Distribution signing certificate: Required to sign development and release builds that are installed on an iOS device.
* Ad hoc provisioning profile: Required to sign builds that are installed on a device outside of the Apple App Store.
* Distribution provisioning profile: Required to sign the build that is submitted to the Apple App Store.
* Push key: Required when using a push notification service.

For details on Distribution certificate, Provision profiles, and Push keys, see [required iOS app credentials](/app-signing/app-credentials#ios).

With EAS CLI, all of the above credentials can be created and synced automatically with the Apple Developer account. Once the authorized user logs in to their [Expo account](/accounts/account-types), they can create or update the provisioning profile by running `eas credentials` using the EAS CLI.

Terminal

`-Â``eas login`

  

`-Â``eas credentials`

The CLI will prompt for selecting a [build profile](/build/eas-json#build-profiles) to use for the EAS Build. If the Apple Developer account's authorized user is creating a production build, follow these steps to [create a distribution provisioning profile](/tutorial/eas/ios-production-build#create-a-distribution-provisioning-profile). To create a developer build, follow these steps to [create an ad hoc provisioning profile](/tutorial/eas/ios-development-build-for-devices#provisioning-profile).

This ensures that the provisioning profile associated with the Expo account has necessary permissions.

> For projects with existing credentials, see [Using existing credentials](/app-signing/existing-credentials) for details on how to sync these to EAS or manage them manually.

Steps for the team developer
----------------------------

As a developer on the team, when running `eas build -p ios` in the terminal window, the EAS CLI asks you to login to an Apple Developer account.

Terminal

`? Do you want to log in to your Apple account? > (Y/n)`  
`No problem! ð If any of the next steps will require Apple account access we will ask you again about it.`

Press `n` to skip logging into Apple Developer account if you don't have access (and avoid logging into your personal Apple Developer account, if any). The CLI displays message about skipping provisioning profile validation and other app signing credential validation and will continue creating the EAS Build with existing credentials

The EAS CLI needs to use the provisioning profile associated with the Expo account to create a build for iOS. When you skip login, the EAS Build will use the last provisioning profile and other credentials that were updated by the Apple Developer account's authorized user in your organization's Expo account.

Additional information
----------------------

### Uploading pre-generated Apple credentials

Some development teams may choose to generate distribution certificates and provisioning profiles outside of EAS. These credentials can be added by any EAS user with Developer or higher permissions using `eas credentials` or under Project > Configuration > Credentials using the Expo dashboard.

When uploading the credentials, you will need the .p12 and .mobileprovision files, and any passwords set when generating the distribution certificate.

### Provisioning profile expiry and updates

The associated provisioning profile needs to be updated if certain [iOS capabilities](/build-reference/ios-capabilities) (such as, entitlements) are added or removed, or at the annual expiry of the profile. This step is handled by the Apple Developer account's authorized user.

### Federated Apple Developer accounts

#### EAS Build

EAS CLI can only accept an Apple account's email and password to login into your Apple Developer account. You cannot login into [Federated Apple Developer account](https://support.apple.com/en-in/guide/apple-business-manager/axmb19317543/web) and make updates to the distribution certificate or provisioning profile. If your build credentials do not require any changes, you can skip logging in. Then, you can proceed with the build and EAS CLI will continue using your current uploaded credentials.

However, you can provide an Apple Store Connect (ASC) API token with Admin access to check and update Apple credentials when running `eas build` command. Follow the steps in [Provide an ASC API Token for your Apple Team](/build/building-on-ci#optional-provide-an-asc-api-token-for-your-apple-team) to create a build by passing the required token value to the `eas build` command.

#### EAS Submit

EAS Submit uses the ASC API token for submitting to TestFlight. If you have a Federated Apple Developer account, you can follow the standard EAS Submit setup. It lets you automatically submit your builds using `eas build --auto-submit`.

[Previous (EAS Build - App signing)

Security](/app-signing/security)[Next (EAS Build - Custom builds)

Get started](/custom-builds/get-started)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/app-signing/apple-developer-program-roles-and-permissions.mdx)
* Last updated on November 26, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Steps for Apple Developer account's authorized user](/app-signing/apple-developer-program-roles-and-permissions/#steps-for-apple-developer-accounts-authorized-user)[Steps for the team developer](/app-signing/apple-developer-program-roles-and-permissions/#steps-for-the-team-developer)[Additional information](/app-signing/apple-developer-program-roles-and-permissions/#additional-information)[Uploading pre-generated Apple credentials](/app-signing/apple-developer-program-roles-and-permissions/#uploading-pre-generated-apple-credentials)[Provisioning profile expiry and updates](/app-signing/apple-developer-program-roles-and-permissions/#provisioning-profile-expiry-and-updates)[Federated Apple Developer accounts](/app-signing/apple-developer-program-roles-and-permissions/#federated-apple-developer-accounts)