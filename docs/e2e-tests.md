Run E2E tests on EAS Workflows - Expo Documentation

[Docs](/)

[Blog](https://expo.dev/blog)[Changelog](https://expo.dev/changelog)[Star Us on GitHub](https://github.com/expo/expo)

Search

[Home](/)[Guides](/guides/overview)[EAS](/eas)[Reference](/versions/latest)[Learn](/tutorial/overview)

[Introduction](/eas)[Configuration with eas.json](/eas/json)[Environment variables](/eas/environment-variables)

EAS Workflows

[Get started](/eas/workflows/get-started)[Example CI/CD workflows](/eas/workflows/examples)[Syntax for EAS Workflows](/eas/workflows/syntax)[Automating EAS CLI commands](/eas/workflows/automating-eas-cli)

Reference

[Run E2E tests](/eas/workflows/reference/e2e-tests)

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

Run E2E tests on EAS Workflows
==============================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas/workflows/reference/e2e-tests.mdx)

Learn how to set up and run E2E tests on EAS Workflows with Maestro.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas/workflows/reference/e2e-tests.mdx)

---

In this guide, you'll learn how to run end-to-end (E2E) tests on EAS Workflows using [Maestro](https://maestro.mobile.dev/). The example demonstrates how to configure your E2E tests workflow using the [default Expo template](/more/create-expo#--template). For your own app, you'll need to adjust the flows to match your app's UI.

1

Set up your project
-------------------

If you haven't already, create a new project and sync it with EAS.

Follow the [Get started with EAS Workflows guide](/eas/workflows/get-started#set-up-your-project) to create a new project and sync it with EAS. Then, [configure your project](/eas/workflows/get-started#configure-your-project) and link your GitHub repository.

2

Add example Maestro test cases
------------------------------

This is what the UI of the app created from the default Expo template looks like:

![](/static/images/eas-build/tests/01-home.png)![](/static/images/eas-build/tests/02-explore.png)

Let's create two simple Maestro flows for the example app. Start by creating a directory called .maestro in the root of your project directory. This directory will contain the flows you'll configure and should be at the same level as eas.json.

Inside, create a new file called home.yml. This flow will launch the app and assert that the text "Welcome!" is visible on the home screen.

.maestro/home.yml

Copy

```
appId: dev.expo.eastestsexample # This is an example app id. Replace it with your app id.
---
- launchApp
- assertVisible: 'Welcome!'

```

Next, create a new flow called expand\_test.yml. This flow will open the "Explore" screen in the example app, click on the "File-based routing" collapsible, and assert that the text "This app has two screens." is visible on the screen.

.maestro/expand\_test.yml

Copy

```
appId: dev.expo.eastestsexample # This is an example app id. Replace it with your app id.
---
- launchApp
- tapOn: 'Explore.*'
- tapOn: '.*File-based routing'
- assertVisible: 'This app has two screens.*'

```

3

Run Maestro tests locally (optional)
------------------------------------

To run Maestro tests locally, install the Maestro CLI by following the instructions in [Installing Maestro](https://maestro.mobile.dev/getting-started/installing-maestro).

[Install your app on a local Android Emulator or iOS Simulator](/more/expo-cli#compiling). Open a terminal, navigate to the Maestro directory, and run the following commands to start the tests with the Maestro CLI:

Terminal

`-Â``maestro test .maestro/expand_test.yml`

  

`-Â``maestro test .maestro/home.yml`

The video below shows a successful run of the .maestro/expand\_test.yml flow:

4

Build profile for E2E tests
---------------------------

E2E tests require a built app file: .apk for Android or .app for iOS â that EAS can install and test on an emulator/simulator.

In your eas.json file, create a build profile for E2E tests. If the file doesn't exist, run `eas build:configure` to generate it.

eas.json

Copy

```
{
  "build": {
    "e2e-test": {
      "withoutCredentials": true,
      "ios": {
        "simulator": true
      },
      "android": {
        "buildType": "apk"
      }
    }
  }
}

```

The above build profile creates an .apk for Android and an .app for iOS. The workflow uses this profile to build the app on EAS servers.

5

Create an E2E test workflow
---------------------------

At the root of your project, create an .eas/workflows directory. Then, add a YAML file for your E2E test workflow, such as .eas/workflows/e2e-test-android.yml.

.eas/workflows/e2e-test-android.yml

Copy

```
name: e2e-test-android

on:
  pull_request:
    branches: ['*'] # Run the E2E test workflow on every pull request.
jobs:
  build_android_for_e2e:
    type: build
    params:
      platform: android
      profile: e2e-test # your eas build profile for E2E test

  maestro_test:
    needs: [build_android_for_e2e]
    type: maestro
    params:
      build_id: ${{ needs.build_android_for_e2e.outputs.build_id }}
      flow_path: ['.maestro/home.yml']

```

This workflow builds an .apk for Android using the `e2e-test` build profile from the previous step. Then it runs the .maestro/home.yml flow on the built APK.

Here's an example of the same test workflow for iOS:

.eas/workflows/e2e-test.yml

Copy

```
name: e2e-test-ios

on:
  pull_request:
    branches: ['*']

jobs:
  build_ios_for_e2e:
    type: build
    params:
      platform: ios
      profile: e2e-test # your eas build profile for E2E test

  maestro_test:
    needs: [build_ios_for_e2e]
    type: maestro
    params:
      build_id: ${{ needs.build_ios_for_e2e.outputs.build_id }}
      flow_path: ['.maestro/home.yml']

```

Learn more about [Syntax for EAS Workflows](/eas/workflows/syntax).

6

Run the E2E test workflow
-------------------------

You can run the E2E test workflow in two ways:

1. Manually using the EAS CLI

Terminal

Copy

`-Â``npx eas-cli@latest workflow:run .eas/workflows/e2e-test-android.yml`

2. Automatically when you open a pull request

The workflow uses a `pull_request` trigger to run automatically when someone opens a pull request to your repository. Learn more about [EAS Workflow triggers](/eas/workflows/syntax#on).

After the workflow starts, you can track its progress and view the results in the Expo Dashboard. Here's a screenshot of a completed workflow run:

![](/static/images/eas-build/tests/e2e-workflow.png)

More
----

[Syntax for EAS Workflows

Learn more about the syntax for EAS Workflows.](/eas/workflows/syntax)
[Example CI/CD workflows

Learn more about example CI/CD workflows for EAS Workflows.](/eas/workflows/examples)
[Maestro documentation

Learn more about Maestro flows and how to write them.](https://maestro.mobile.dev)

[Previous (EAS Workflows)

Automating EAS CLI commands](/eas/workflows/automating-eas-cli)[Next (EAS Build)

Introduction](/build/introduction)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas/workflows/reference/e2e-tests.mdx)
* Last updated on April 21, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Set up your project](/eas/workflows/reference/e2e-tests/#set-up-your-project)[Add example Maestro test cases](/eas/workflows/reference/e2e-tests/#add-example-maestro-test-cases)[Run Maestro tests locally (optional)](/eas/workflows/reference/e2e-tests/#run-maestro-tests-locally-optional)[Build profile for E2E tests](/eas/workflows/reference/e2e-tests/#build-profile-for-e2e-tests)[Create an E2E test workflow](/eas/workflows/reference/e2e-tests/#create-an-e2e-test-workflow)[Run the E2E test workflow](/eas/workflows/reference/e2e-tests/#run-the-e2e-test-workflow)[More](/eas/workflows/reference/e2e-tests/#more)