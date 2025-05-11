Automate submissions - Expo Documentation

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

Billing

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Automate submissions
====================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build/automate-submissions.mdx)

Learn how to enable automatic submissions with EAS Build.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build/automate-submissions.mdx)

---

Many mobile deployment processes eventually evolve to the point where the app is automatically submitted to the respective store once an appropriate build is completed. This saves developers from having to wait around for the build to complete, avoids a bit of manual work, and eliminates the need to coordinate providing app store credentials to the team.

EAS Build gives you automatic submissions out of the box with the `--auto-submit` flag. This flag tells EAS Build to pass the build along to EAS Submit with the appropriate submission profile upon completion. Refer to the [EAS Submit documentation](/submit/introduction) for more information on how to set up and configure submissions.

When you run `eas build --auto-submit` you will be provided with a link to a submission details page, where you can track the progress of the submission. You can also find this page at any time on the [submissions dashboard for your project](https://expo.dev/accounts/%5Baccount%5D/projects/%5Bproject%5D/submissions), and it is linked from your build details page.

### Selecting a submission profile

By default, `--auto-submit` will try to use a submission profile with the same name as the selected build profile. If this does not exist, or if you prefer to use a different profile, you can use `--auto-submit-with-profile=<profile-name>` instead.

### Build profile environment variables and submissions

When running `eas build --profile <profile-name> --auto-submit`, the project's app.config.js will be evaluated using any environment variables associated with the build profile `<profile-name>`. For example, suppose we ran `eas build -p ios --profile production --auto-submit` with the following configuration:

eas.json

Copy

```
{
  "build": {
    "production": {
      "env": {
        "APP_ENV": "production"
      }
    },
    "development": {
      "env": {
        "APP_ENV": "development"
      }
    }
  }
}

```

app.config.js

Copy

```
export default () => {
  return {
    name: process.env.APP_ENV === 'production' ? 'My App' : 'My App (DEV)',
    ios: {
      bundleIdentifier: process.env.APP_ENV === 'production' ? 'com.my.app' : 'com.my.app-dev',
    },
    // ... other config here
  };
};

```

The `APP_ENV` variable from the `production` profile will be used when evaluating app.config.js for the submission, and therefore the name will be `My App` and the bundle identifier will be `com.my.app`.

[Previous (EAS Build)

Internal distribution](/build/internal-distribution)[Next (EAS Build)

Using EAS Update](/build/updates)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build/automate-submissions.mdx)
* Last updated on April 02, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Selecting a submission profile](/build/automate-submissions/#selecting-a-submission-profile)[Build profile environment variables and submissions](/build/automate-submissions/#build-profile-environment-variables-and-submissions)