Two-factor authentication - Expo Documentation

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

Two-factor authentication
=========================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/accounts/two-factor.mdx)

Learn about how you leverage two-factor authentication (2FA) to secure your Expo account.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/accounts/two-factor.mdx)

---

Two-factor authentication provides an extra layer of security when logging in to expo.dev, the Expo Go app, and command line tools. With two-factor authentication enabled, you will need to provide a short-lived code in addition to your username and password to access your account.

Enable two-factor authentication (2FA)
--------------------------------------

You can enable two-factor authentication from your [personal account settings](https://expo.dev/settings#two-factor-auth).

Two-factor authentication methods
---------------------------------

You can receive 2FA codes through an authenticator app.

### Authenticator apps

Expo accepts any authenticator app that supports Time-based One-time Passwords (TOTP) including:

* [Last Pass Authenticator](https://lastpass.com/auth/)
* [Authy](https://authy.com/)
* [1Password](https://support.1password.com/one-time-passwords/)
* [Google Authenticator](https://support.google.com/accounts/answer/1066447)
* [Microsoft Authenticator](https://www.microsoft.com/en-us/account/authenticator)

Expo will provide a QR code to scan with your authenticator app during setup. The app will provide a confirmation code to enter on Expo. Enter the code to finish activating 2FA via your authenticator app.

### SMS messages

> Deprecated: SMS is no longer supported for newly-added two-factor authentication methods. Existing SMS two-factor authentication methods will continue to work, though we suggest switching to an authenticator app as it provides better security.

Provide a mobile phone number to receive a short-lived token via SMS. Codes received via SMS will be valid for at least 10 minutes, so you may receive the same code multiple times within this window. If you set an SMS device as your default 2FA method, you will be sent a verification code automatically whenever you take an action that requires a 2FA code.

### Recovery codes

When you set up two-factor authentication for your account, you'll receive a set of recovery codes. These codes can be used instead of a one-time password if you lose access to your authenticator app or SMS device. Keep in mind that each recovery code is only valid for one use.

If you selected the option to download your recovery codes at the time they were created, you can locate them in a file labeled as expo-recovery-codes.txt.

> Store your recovery codes in a secure and memorable place to ensure you, and only you can access your account!

Change your two-factor settings
-------------------------------

You can make changes to your two-factor settings from your [personal account settings](https://expo.dev/settings). You can:

* add or remove authentication methods
* set your default method
* regenerate your recovery codes
* disable two-factor authentication for your account

You will need to provide a one-time password to make any changes to your 2FA settings.

Recover your account
--------------------

### Recovery codes

When you set up your account to use 2FA, Expo provides you with a list of recovery codes. In the event you lose your device(s), a recovery code may be used in place of a one-time password. Each of these codes may only be used once. You may regenerate your recovery codes, which will invalidate any existing codes, from your [personal account settings](https://expo.dev/settings/).

### Secondary 2FA methods

By setting up multiple authentication methods associated with different physical devices, you can ensure you will not lose access to your account in the event a device is reset or lost.

### Manual recovery

If you cannot access your account through any of the supplied methods, you may email Expo support from the email associated with your account. Unfortunately, we cannot guarantee we will be able to restore your access to your account in this scenario.

[Previous (Reference - Expo accounts)

Account types](/accounts/account-types)[Next (Reference - Expo accounts)

Programmatic access](/accounts/programmatic-access)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/accounts/two-factor.mdx)
* Last updated on November 24, 2023

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Enable two-factor authentication (2FA)](/accounts/two-factor/#enable-two-factor-authentication-2fa)[Two-factor authentication methods](/accounts/two-factor/#two-factor-authentication-methods)[Authenticator apps](/accounts/two-factor/#authenticator-apps)[SMS messages](/accounts/two-factor/#sms-messages)[Recovery codes](/accounts/two-factor/#recovery-codes)[Change your two-factor settings](/accounts/two-factor/#change-your-two-factor-settings)[Recover your account](/accounts/two-factor/#recover-your-account)[Recovery codes](/accounts/two-factor/#recovery-codes-1)[Secondary 2FA methods](/accounts/two-factor/#secondary-2fa-methods)[Manual recovery](/accounts/two-factor/#manual-recovery)