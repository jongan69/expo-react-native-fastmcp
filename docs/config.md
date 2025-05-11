Configuring EAS Metadata - Expo Documentation

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

[store.config.json](/eas/metadata/config)[Metadata schema](/eas/metadata/schema)[FAQ](/eas/metadata/faq)

EAS Insights

[Introduction](/eas-insights/introduction)

Distribution

[Overview](/distribution/introduction)[App stores best practices](/distribution/app-stores)[App transfers](/distribution/app-transfers)[Understanding app size](/distribution/app-size)

Reference

[Webhooks](/eas/webhooks)

Expo accounts

Billing

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Configuring EAS Metadata
========================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas/metadata/config.mdx)

Learn about different ways to configure EAS Metadata.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas/metadata/config.mdx)

---

> EAS Metadata is in preview and subject to breaking changes.

EAS Metadata is configured by a store.config.json file at the *root of your project*.

You can configure the path or name of the store config file with the eas.json [`metadataPath`](/submit/eas-json#metadatapath) property.
Besides the default JSON format, EAS Metadata also supports more dynamic config using JavaScript files.

Static store config
-------------------

The default store config type for EAS Metadata is a simple JSON file.
The code snippet below shows an example store config with basic App Store information written in English (U.S.).

You can find all configuration options in the [store config schema](/eas/metadata/schema).

> If you have the [VS Code Expo Tools extension](https://github.com/expo/vscode-expo#readme) installed, you get auto-complete, suggestions, and warnings for store.config.json files.

store.config.json

Copy

```
{
  "configVersion": 0,
  "apple": {
    "info": {
      "en-US": {
        "title": "Awesome App",
        "subtitle": "Your self-made awesome app",
        "description": "The most awesome app you have ever seen",
        "keywords": ["awesome", "app"],
        "marketingUrl": "https://example.com/en/promo",
        "supportUrl": "https://example.com/en/support",
        "privacyPolicyUrl": "https://example.com/en/privacy"
      }
    }
  }
}

```

Dynamic store config
--------------------

At times, Metadata properties can benefit from dynamic values. For example, the Metadata copyright notice should contain the current year. This can be automated with EAS Metadata.

To generate content dynamically, start by creating a JavaScript config file store.config.js. Then, use the [`metadataPath`](/eas/json#metadatapath) property in the eas.json file to pick the JS config file.

> `eas metadata:pull` can't update dynamic store config files. Instead, it creates a JSON file with the same name as the configured file. You can import the JSON file to reuse the data from `eas metadata:pull`.

store.config.js

Copy

```
// Use the data from `eas metadata:pull`
const config = require('./store.config.json');

const year = new Date().getFullYear();
config.apple.copyright = `${year} Acme, Inc.`;

module.exports = config;

```

eas.json

Copy

```
{
  "submit": {
    "production": {
      "ios": {
        "metadataPath": "./store.config.js"
      }
    }
  }
}

```

Store config with external content
----------------------------------

When using external services for localizations, you have to fetch external content.
EAS Metadata supports synchronous and asynchronous functions exported from dynamic store config files.
The function results are awaited before validating and syncing with the stores.

> The store.config.js function is evaluated in Node.js. If you need special values, like secrets, use environment variables.

store.config.js

Copy

```
// Use the data from `eas metadata:pull`
const config = require('./store.config.json');

module.exports = async () => {
  const year = new Date().getFullYear();
  const info = await fetchLocalizations('...').then(response => response.json());

  config.apple.copyright = `${year} Acme, Inc.`;
  config.apple.info = info;

  return config;
};

```

eas.json

Copy

```
{
  "submit": {
    "production": {
      "ios": {
        "metadataPath": "./store.config.js"
      }
    }
  }
}

```

[Previous (EAS Metadata)

Get started](/eas/metadata/getting-started)[Next (EAS Metadata - Reference)

Metadata schema](/eas/metadata/schema)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas/metadata/config.mdx)
* Last updated on April 29, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Static store config](/eas/metadata/config/#static-store-config)[Dynamic store config](/eas/metadata/config/#dynamic-store-config)[Store config with external content](/eas/metadata/config/#store-config-with-external-content)