End-to-end code signing with EAS Update - Expo Documentation

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

[Code signing](/eas-update/code-signing)[Asset selection and exclusion](/eas-update/asset-selection)[Using without other EAS services](/eas-update/standalone-service)[Migrate from CodePush](/eas-update/codepush)[Migrate from Classic Updates](/eas-update/migrate-from-classic-updates)[Trace update ID back to the Expo Dashboard](/eas-update/trace-update-id-expo-dashboard)[Estimate bandwidth usage](/eas-update/estimate-bandwidth)[Integrate in existing native apps](/eas-update/integration-in-existing-native-apps)[FAQ](/eas-update/faq)

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

End-to-end code signing with EAS Update
=======================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/code-signing.mdx)

Learn how code signing and key rotation work in EAS Update.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/code-signing.mdx)

---

> EAS Update Code Signing is only available to accounts subscribed to the EAS Production or Enterprise plans. [Learn more](https://expo.dev/pricing).

The `expo-updates` library supports end-to-end code signing using [public-key cryptography](https://en.wikipedia.org/wiki/Public-key_cryptography). Code signing allows developers to cryptographically sign their updates with their own keys. The signatures are then verified on the client before the update is applied, which ensures ISPs, CDNs, cloud providers, and even EAS itself cannot tamper with updates run by apps.

The following steps will guide you through the process of generating a private key and corresponding certificate, configuring your project to use code signing, and publishing a signed update for your app.

1

Generate a private key and corresponding certificate
----------------------------------------------------

In this step, we will generate a key pair and corresponding code signing certificate for your app. Specify a directory outside of your source control for the `--key-output-directory` flag to ensure the generated private key isn't accidentally added to source control.

Terminal

Copy

`-Â``npx expo-updates codesigning:generate \`

 `--key-output-directory ../keys \` `--certificate-output-directory certs \` `--certificate-validity-duration-years 10 \` `--certificate-common-name "Your Organization Name"`

This command generated a key pair along with a code signing certificate to be included in the app:

* `../keys/private-key.pem`: the private key of the key pair.
* `../keys/public-key.pem`: the public key of the key pair.
* `certs/certificate.pem`: the code signing certificate configured to be valid for 10 years. This file should be added to source control (if applicable).
* The generated private key must be kept private and secure. The command above suggests generating and storing these keys in a directory outside of your source control to ensure they are not accidentally checked into source control. We recommend storing the private key in the same way you would store other sensitive information (KMS, password manager, and so on), and how you store it will vary the steps needed to publish an update in step (3).
* The public key may be stored alongside the private key, but isn't sensitive.
* The certificate should be included in the project (checked into source control). It contains the public key and a method for verifying code signatures. When a signed update is downloaded, the update's signature is verified using this certificate.
* The certificate validity duration is a setting that may vary based on the security needs of your app.

  + A shorter validity duration will require [key rotation](/eas-update/code-signing#key-rotation) more frequently but is considered better practice since a compromised private key will have a sooner expiration which limits exposure.
  + Shorter validity durations add overhead to your app's release process as the key must be rotated more frequently. Binaries with expired certificates won't apply new updates.
  + For example, Expo sets this value to 20 years for the public Expo Go app, but only 1 year for internal apps with binaries that are distributed more frequently. We plan to rotate our keys every 10 years.

2

Configure your project to use code signing
------------------------------------------

Terminal

Copy

`-Â``npx expo-updates codesigning:configure \`

 `--certificate-input-directory certs \` `--key-input-directory ../keys`

  

If you are using Continuous Native Generation (CNG) to generate your native projects, then the app.json configuration generated by the `npx expo-updates codesigning configure` command is all that you need. The changes will be applied to the native projects the next time they are generated.

Configure code signing in app.json

After running the above command, your app.json will include additional configuration for code signing:

app.json

Copy

```
{
  "expo": {
    "updates": {
      "codeSigningCertificate": "./certs/certificate.pem",
      "codeSigningMetadata": {
        "keyid": "main",
        "alg": "rsa-v1_5-sha256"
      }
    }
  }
}

```

  

If you are not using Continuous Native Generation (CNG) to generate your native projects, then you will need to configure code signing in your app AndroidManifest.xml and/or Expo.plist files.

Configure code signing in an Android native project

You will need to add two fields to the `<application>` element in android/app/src/main/AndroidManifest.xml

Before doing that, we need to generate an XML-escaped version of your certificate. You can either copy the contents of certs/certificate.pem and replace all of the `\r` characters with `&#xD;` and `\n` with `&#xA;` manually, or run the following script to do that for you:

Terminal

Copy

`-Â``node -e "console.log(require('fs').readFileSync('./certs/certificate.pem', 'utf8')\`

`.replace(/\r/g, '&#xD;').replace(/\n/g, '&#xA;'));"`

Now add the following two fields, and replace the `android:value` for the `expo.modules.updates.CODE_SIGNING_CERTIFICATE` field with the XML-escaped certificate. You do not need to modify the value for `expo.modules.updates.CODE_SIGNING_METADATA` entry.

android/app/src/main/AndroidManifest.xml

Copy

```
<meta-data
  android:name="expo.modules.updates.CODE_SIGNING_CERTIFICATE"
  android:value="(insert XML-escaped certificate here)"
  />
<meta-data
  android:name="expo.modules.updates.CODE_SIGNING_METADATA"
  android:value="{&quot;keyid&quot;:&quot;main&quot;,&quot;alg&quot;:&quot;rsa-v1_5-sha256&quot;}"
  />

```

Configure code signing in an iOS native project

You will need to add two fields to the `<dict>` element in ios/project-name/Supporting/Expo.plist.

Before doing that, we need to generate an XML-escaped version of your certificate. You can either copy the contents of certs/certificate.pem and replace all of the `\r` characters with `&#xD;`, or run the following script to do that for you:

Terminal

Copy

`-Â``node -e "console.log(require('fs').readFileSync('./certs/certificate.pem', 'utf8')\`

`.replace(/\r/g, '&#xD;'));"`

Now add the following two fields, and replace the certificate value with the XML-escaped certificate. You do not need to update the `EXUpdatesCodeSigningMetadata` field.

ios/project-name/Supporting/Expo.plist

Copy

```
    <key>EXUpdatesCodeSigningCertificate</key>
    <string>-----BEGIN CERTIFICATE-----&#xD;
(insert XML-escaped certificate, it should look something like this)&#xD;
(spanning multiple lines with \r escaped but \n not escaped)&#xD;
+-----END CERTIFICATE-----&#xD;
</string>
    <key>EXUpdatesCodeSigningMetadata</key>
    <dict>
      <key>keyid</key>
      <string>main</string>
      <key>alg</key>
      <string>rsa-v1_5-sha256</string>
    </dict>

```

  

With code signing configured, create a new build with a new runtime version. The code signing certificate will be embedded in this new build.

3

Publish a signed update for your app
------------------------------------

Terminal

Copy

`-Â``eas update --private-key-path ../keys/private-key.pem`

During an EAS Update publish using `eas update`, the EAS CLI automatically detects that code signing is configured for your app. It then verifies the integrity of the update and creates a digital signature using your private key. This process is performed locally so that your private key never leaves your machine. The generated signature is automatically sent to EAS to store alongside the update.

4

Verify that the update is loaded
--------------------------------

Download the update on the client (this step is done automatically by the library). The build from step (2) that is configured for code signing checks if there is a new update available. The server responds with the update published in step (3) and its generated signature. After being downloaded but before being applied, the update is verified against the embedded certificate and included signature. The update is applied if the certificate and signature are valid, and rejected otherwise.

Additional information
----------------------

### Key rotation

Key rotation is the process by which the key pair used for signing updates is changed. This is most commonly done in a few cases:

* Key expiration. In step (1) from the section above, we set `certificate-validity-duration-years` to 10 years (though it can be configured to any value). This means that after 10 years, updates signed with the private key corresponding to the certificate will no longer be applied after being downloaded by the app. Updates downloaded before the expiration of their signing certificate will continue to function normally. Rotating keys well before the certificate expires helps to preempt any potential key expiration issues and helps to guarantee all users are using the new certificate before the old certificate expires.
* Private key compromise. If the private key used to sign updates is accidentally exposed to the public, it can no longer be considered secure and therefore the integrity of updates signed with it can no longer be guaranteed. For example, a malicious actor could craft a malicious update and sign it with the leaked private key.
* Key rotation for security best practices. It is best practice to rotate keys periodically to ensure that a system is resilient to manual key rotation in response to one of the other reasons above.

In any of these cases, the procedure is similar:

1. Back up the old keys and certificate that were generated in step (1) above.
2. Generate a new key by following the steps above starting from step (1). To assist in debugging, you may wish to change the `keyid` of the new key by modifying the `updates.codeSigningMetadata.keyid` field in your app config (app.json).
3. The code signing certificate is part of the app's runtime, so a new runtime version should be set for builds using this certificate to ensure that only updates signed with the new key run in the new build.
4. Publish signed updates using the new key by following step (3) above.

### Removing code signing

The process of removing code signing from an app is similar to [key rotation](/eas-update/code-signing#key-rotation) and can be thought of as a key rotation to a `null` key.

1. Backup the old key and certificate that were generated in step (1) above.
2. Remove the `updates.codeSigningMetadata` field from your app config (app.json).
3. The new certificate-less app is a new distinct runtime, so a new runtime version should be set for builds to ensure that only unsigned updates run in the new build.

[Previous (EAS Update - Troubleshooting)

Error recovery](/eas-update/error-recovery)[Next (EAS Update - Reference)

Asset selection and exclusion](/eas-update/asset-selection)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas-update/code-signing.mdx)
* Last updated on December 09, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Generate a private key and corresponding certificate](/eas-update/code-signing/#generate-a-private-key-and-corresponding-certificate)[Configure your project to use code signing](/eas-update/code-signing/#configure-your-project-to-use-code-signing)[Publish a signed update for your app](/eas-update/code-signing/#publish-a-signed-update-for-your-app)[Verify that the update is loaded](/eas-update/code-signing/#verify-that-the-update-is-loaded)[Additional information](/eas-update/code-signing/#additional-information)[Key rotation](/eas-update/code-signing/#key-rotation)[Removing code signing](/eas-update/code-signing/#removing-code-signing)