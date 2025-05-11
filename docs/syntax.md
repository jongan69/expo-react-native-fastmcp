Syntax for EAS Workflows - Expo Documentation

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

Syntax for EAS Workflows
========================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas/workflows/syntax.mdx)

Reference guide for the EAS Workflows configuration file syntax.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas/workflows/syntax.mdx)

---

A workflow is a configurable automated process made up of one or more jobs. You must create a YAML file to define your workflow configuration.

To get started with workflows, see [Get Started with EAS Workflows](/eas/workflows/get-started) or see [Examples](/eas/workflows/examples) for complete workflow configurations.

Workflow files
--------------

Workflow files use YAML syntax and must have either a `.yml` or `.yaml` file extension. If you're new to YAML and want to learn more, see [Learn YAML in Y minutes](https://learnxinyminutes.com/docs/yaml/).

Workflow files are located in the .eas/workflows directory in your project. The .eas directory should be at the same level as your [eas.json](/build/eas-json) file.

For example:

`my-app`

â`.eas`

ââ`workflows`

âââ`create-development-builds.yml`

âââ`publish-preview-update.yml`

âââ`deploy-to-production.yml`

â`eas.json`

Configuration Reference
-----------------------

Below is a reference for the syntax of the workflow configuration file.

`name`
------

The human-friendly name of the workflow. This is displayed on the Expo dashboard on the workflows list page and is the title of the workflow's detail page.

```
name: My workflow

```

`on`
----

The `on` key defines which GitHub events trigger the workflow. Any workflow can be triggered with the `eas workflow:run` command, regardless of the `on` key.

```
on:
  # Trigger on pushes to main branch
  push:
    branches:
      - main
  # And on pull requests starting with 'version-'
  pull_request:
    branches:
      - version-*

```

### `on.push`

Runs your workflow when you push a commit to matching branches and/or tags.

With the `branches` list, you can trigger the workflow only when those specified branches are pushed to. For example, if you use `branches: ['main']`, only pushes to the `main` branch will trigger the workflow. Supports globs. By using the `!` prefix you can specify branches to ignore (you still need to provide at least one branch pattern without it).

With the `tags` list, you can trigger the workflow only when those specified tags are pushed. For example, if you use `tags: ['v1']`, only the `v1` tag being pushed will trigger the workflow. Supports globs. By using the `!` prefix you can specify tags to ignore (you still need to provide at least one tag pattern without it).

When neither `branches` nor `tags` are provided, `branches` defaults to `['*']` and `tags` defaults to `[]`, which means the workflow will trigger on push events to all branches and will not trigger on tag pushes. If only one of the two lists is provided the other defaults to `[]`.

```
on:
  push:
    branches:
      - main
      - feature/**
      - !feature/test-** # other branch names and globs


    tags:
      - v1
      - v2*
      - !v2-preview** # other tag names and globs


```

### `on.pull_request`

Runs your workflow when you create or update a pull request that targets one of the matching branches.

With the `branches` list, you can trigger the workflow only when those specified branches are the target of the pull request. For example, if you use `branches: ['main']`, only pull requests to merge into the main branch will trigger the workflow. Supports globs. Defaults to `['*']` when not provided, which means the workflow will trigger on pull request events to all branches. By using the `!` prefix you can specify branches to ignore (you still need to provide at least one branch pattern without it).

With the `types` list, you can trigger the workflow only on the specified pull request event types. For example, if you use `types: ['opened']`, only the `pull_request.opened` event (sent when a pull request is first opened) will trigger the workflow. Defaults to `['opened', 'reopened', 'synchronize']` when not provided. Supported event types:

* `opened`
* `reopened`
* `synchronize`
* `labeled`

```
on:
  pull_request:
    branches:
      - main
      - feature/**
      - !feature/test-** # other branch names and globs


    types:
      - opened
      # other event types

```

### `on.pull_request_labeled`

Runs your workflow when a pull request is labeled with a matching label.

With the `labels` list, you can specify which labels, when assigned to your pull request, will trigger the workflow. For example, if you use `labels: ['Test']`, only labeling a pull request with the `Test` label will trigger the workflow. Defaults to `[]` when not provided, which means no labels will trigger the workflow.

You can also provide a list of matching labels directly to `on.pull_request_labeled` for simpler syntax.

```
on:
  pull_request_labeled:
    labels:
      - Test
      - Preview
      # other labels

```

Alternatively:

```
on:
  pull_request_labeled:
    - Test
    - Preview
    # other labels

```

### `on.schedule.cron`

Runs your workflow on a schedule using [unix-cron](https://www.ibm.com/docs/en/db2/11.5?topic=task-unix-cron-format) syntax. You can use [crontab guru](https://crontab.guru/) and their [examples](https://crontab.guru/examples.html) to generate cron strings.

* Scheduled workflows will only run on the default branch of the repository. In many cases, this means crons inside workflow files on the `main` branch will be scheduled, while crons inside workflow files in feature branches will not be scheduled.
* Scheduled workflows may be delayed during periods of high load. High load times include the start of every hour. In rare circumstances, jobs may be skipped or run multiple times. Make sure that your workflows are idempotent and do not have harmful side effects.
* A workflow can have multiple `cron` schedules.

```
on:
  schedule:
    - cron: '0 0 * * *' # Runs at midnight every day

```

`jobs`
------

A workflow run is made up of one or more jobs.

```
jobs:
  job_1:
    # ...
  job_2:
    # ...

```

### `jobs.<job_id>`

Each job must have an ID. The ID should be unique within the workflow and can contain alphanumeric characters and underscores. For example, `my_job` in the following YAML:

```
jobs:
  my_job:
    # ...

```

### `jobs.<job_id>.name`

The human-friendly name of the job displayed on the workflow's detail page.

```
jobs:
  my_job:
    name: Build app

```

### `jobs.<job_id>.environment`

Sets the [EAS environment variable](/eas/environment-variables) environment for the job. There are three possible values:

* `production` (default)
* `preview`
* `development`

The `environment` key is available on all jobs except for the pre-packaged `build`, `submit`, and `get-build` jobs.

```
jobs:
  my_job:
    environment: production | preview | development

```

### `jobs.<job_id>.defaults.run.working_directory`

Sets the directory to run commands in for all steps in the job.

```
jobs:
  my_job:
    defaults:
      run:
        working_directory: ./my-app
    steps:
      - name: My first step
        run: pwd # prints: /home/expo/workingdir/build/my-app

```

`defaults`
----------

Parameters to use as defaults for all jobs defined in the workflow configuration.

### `defaults.run.working_directory`

Default working directory to run the scripts in. Relative paths like "./assets" or "assets" are resolved from the app's base directory.

### `defaults.tools`

Specific versions of tools that should be used for jobs defined in this workflow configuration. Follow each tool's documentation for available values.

| Tool | Description |
| --- | --- |
| `node` | Version of Node.js installed via `nvm`. |
| `yarn` | Version of Yarn installed via `npm -g`. |
| `corepack` | If set to `true`, [corepack](https://nodejs.org/api/corepack.html) will be enabled at the beginning of build process. Defaults to false. |
| `pnpm` | Version of pnpm installed via `npm -g`. |
| `bun` | Version of Bun installed by passing `bun-v$VERSION` to Bun install script. |
| `ndk` | Version of Android NDK installed through `sdkmanager`. |
| `bundler` | Version of Bundler that will be passed to `gem install -v`. |
| `fastlane` | Version of fastlane that will be passed to `gem install -v`. |
| `cocoapods` | Version of CocoaPods that will be passed to `gem install -v`. |

Example of workflow using `defaults.tools`:

.eas/workflows/publish-update.yml

Copy

```
name: Set up custom versions
defaults:
  tools:
    node: latest
    yarn: '2'
    corepack: true
    pnpm: '8'
    bun: '1.0.0'
    fastlane: 2.224.0
    cocoapods: 1.12.0

on:
  push:
    branches: ['*']

jobs:
  setup:
    steps:
      - name: Check Node version
        run: node --version # should print a concrete version, like 23.9.0
      - name: Check Yarn version
        run: yarn --version # should print a concrete version, like 2.4.3

```

`concurrency`
-------------

Configuration for concurrency control. Currently only allows setting `cancel_in_progress` for same-branch workflows.

```
concurrency:
  cancel_in_progress: true
  group: ${{ workflow.filename }}-${{ github.ref }}

```

| Property | Type | Description |
| --- | --- | --- |
| `cancel_in_progress` | `boolean` | If true, new workflow runs started from GitHub will cancel current in-progress runs for the same branch. |
| `group` | `string` | We do not support custom concurrency groups yet. Set this placeholder value so that when we do support custom groups, your workflow remains compatible. |

Control flow
------------

You can control when a job runs with the `needs` and `after` keywords. In addition, you can use the `if` keyword to control whether a job should run based on a condition.

### `jobs.<job_id>.needs`

A list of job IDs whose jobs must complete successfully before this job will run.

```
jobs:
  test:
    steps:
      - uses: eas/checkout
      - uses: eas/use_npm_token
      - uses: eas/install_node_modules
      - name: tsc
        run: yarn tsc
  build:
    needs: [test] # This job will only run if the 'test' job succeeds
    type: build
    params:
      platform: ios

```

### `jobs.<job_id>.after`

A list of job IDs that must complete (successfully or not) before this job will run.

```
jobs:
  build:
    type: build
    params:
      platform: ios
  notify:
    after: [build] # This job will run after build completes (whether build succeeds or fails)

```

### `jobs.<job_id>.if`

The `if` conditional determines if a job should run. When an `if` condition is met, the job will run. When the condition is not met, the job will be skipped. A skipped job won't have completed successfully and any downstream jobs will not run that have this job in their `needs` list.

```
jobs:
  my_job:
    if: ${{ github.ref_name == 'main' }}

```

Interpolation
-------------

You can customize the behavior of a workflow â commands to execute, control flow, environment variables, build profile, app version, and more â based on the workflow run's context.

### `after` and `needs`

When you specify an upstream job in `after` or `needs`, you can use its outputs in a downstream job. All jobs expose a `status` property. Most pre-packaged jobs also expose some outputs. You can [set outputs in custom jobs using the `set-output` function](/eas/workflows/syntax#jobsjob_idoutputs).

```
{
  "status": "success" | "failure" | "skipped",
  "outputs": {}
}

```

Example usage:

```
jobs:
  setup:
    outputs:
      date: ${{ steps.current_date.outputs.date }}
    steps:
      - id: current_date
        run: |
          DATE=$(date +"%Y.%-m.%-d")
          set-output date "$DATE"

  build_ios:
    needs: [setup]
    type: build
    env:
      # You might use process.env.VERSION_SUFFIX to customize
      # app version in your dynamic app config.
      VERSION_SUFFIX: ${{ needs.setup.outputs.date }}
    params:
      platform: ios
      profile: development

```

### `github`

To ease the migration from GitHub Actions to EAS Workflows we expose some context fields you may find useful.

```
{
  "event_name": "pull_request" | "push" | "schedule" | "workflow_dispatch",
  "sha": string,
  "ref": string, // e.g. refs/heads/main
  "ref_name": string, // e.g. main
  "ref_type": "branch" | "tag" | "other"
}

```

If a workflow run is started from `eas workflow:run`, its `event_name` will be `workflow_dispatch` and all the rest of the properties will be empty.

Example usage:

```
jobs:
  build_ios:
    type: build
    if: ${{ github.ref_name == 'main' }}
    params:
      platform: ios
      profile: production

```

### `success()`, `failure()`

`success()` returns `true` only if no previous job has failed. `failure()` returns `true` if any previous job has failed.

### `fromJSON()`, `toJSON()`

`fromJSON()` is `JSON.parse()`, and `toJSON()` is `JSON.stringify()`. You can use them to consume or produce JSON outputs.

Example usage:

```
jobs:
  publish_update:
    type: update

  print_debug_info:
    needs: [publish_update]
    steps:
      - run: |
          echo "First update group: ${{ needs.publish_update.outputs.first_update_group_id }}"
          echo "Second update group: ${{ fromJSON(needs.publish_update.outputs.updates_json || '[]')[1].group }}"

```

Pre-packaged jobs
-----------------

### `jobs.<job_id>.type`

Specifies the type of pre-packaged job to run. Pre-packaged jobs produce specialized UI according to the type of job on the workflow's detail page.

```
jobs:
  my_job:
    type: build

```

Learn about the different pre-packaged jobs below.

#### `build`

Creates an Android or iOS build of your project using [EAS Build](/build/introduction).

```
jobs:
  my_job:
    type: build
    params:
      platform: ios | android # required
      profile: string # optional, default: production

```

This job outputs the following properties:

```
{
  "build_id": string,
  "app_build_version": string | null,
  "app_identifier": string | null,
  "app_version": string | null,
  "channel": string | null,
  "distribution": "internal" | "store" | null,
  "fingerprint_hash": string | null,
  "git_commit_hash": string | null,
  "platform": "ios" | "android" | null,
  "profile": string | null,
  "runtime_version": string | null,
  "sdk_version": string | null,
  "simulator": "true" | "false" | null
}

```

Build jobs can be customized so that you can execute custom commands during the build process. See [Custom builds](/custom-builds/get-started) for more information.

#### `deploy`

Deploys your application using [EAS Hosting](/eas/hosting/introduction).

```
jobs:
  my_job:
    type: deploy
    params:
      alias: string # optional
      prod: boolean # optional

```

#### `fingerprint`

Calculates fingerprint of Android and iOS builds.

```
jobs:
  my_job:
    type: fingerprint

```

> This job type only supports [CNG (managed)](/workflow/continuous-native-generation) workflows. If you commit your android or ios directories, the fingerprint job won't work.

This job outputs the following properties:

```
{
  "android_fingerprint_hash": string,
  "ios_fingerprint_hash": string,
}

```

#### `get-build`

Retrieves an existing build from EAS that matches the provided parameters.

```
jobs:
  my_job:
    type: get-build
    params:
      platform: ios | android # optional
      profile: string # optional
      distribution: store | internal | simulator # optional
      channel: string # optional
      app_identifier: string # optional
      app_build_version: string # optional
      app_version: string # optional
      git_commit_hash: string # optional
      fingerprint_hash: string # optional
      sdk_version: string # optional
      runtime_version: string # optional
      simulator: boolean # optional

```

This job outputs the following properties:

```
{
  "build_id": string,
  "app_build_version": string | null,
  "app_identifier": string | null,
  "app_version": string | null,
  "channel": string | null,
  "distribution": "internal" | "store" | null,
  "fingerprint_hash": string | null,
  "git_commit_hash": string | null,
  "platform": "ios" | "android" | null,
  "profile": string | null,
  "runtime_version": string | null,
  "sdk_version": string | null,
  "simulator": "true" | "false" | null
}

```

#### `submit`

Submits an Android or iOS build to the app store using [EAS Submit](/submit/introduction). For `environment`, it uses the same environment used to create the build referenced in `build_id`.

> Submission jobs require additional configuration to run within a CI/CD process. See our [Apple App Store CI/CD submission guide](/submit/ios#submitting-your-app-using-cicd-services) and [Google Play Store CI/CD submission guide](/submit/android#submitting-your-app-using-cicd-services) for more information.

```
jobs:
  my_job:
    type: submit
    params:
      build_id: string # required
      profile: string # optional, default: production

```

This job outputs the following properties:

```
{
  "apple_app_id": string | null, // Apple App ID. https://expo.fyi/asc-app-id
  "ios_bundle_identifier": string | null, // iOS bundle identifier of the submitted build. https://expo.fyi/bundle-identifier
  "android_package_id": string | null // Submitted Android package ID. https://expo.fyi/android-package
}

```

#### `update`

Publishes an update using [EAS Update](/eas-update/introduction).

```
jobs:
  my_job:
    type: update
    params:
      message: string # optional
      platform: string # optional - android | ios | all, defaults to all
      branch: string # optional
      channel: string # optional - cannot be used with branch

```

This job outputs the following properties:

```
{
  "first_update_group_id": string, // ID of the first update group. You can use it to e.g. construct the update URL for a development client deep link.
  "updates_json": string // Stringified JSON array of update groups. Output of `eas update --json`.
}

```

#### `maestro`

Runs [Maestro](https://maestro.mobile.dev/) tests on a build.

```
jobs:
  my_job:
    type: maestro
    environment: production | preview | development # optional, defaults to preview
    image: string # optional. See https://docs.expo.dev/build-reference/infrastructure/ for a list of available images.
    params:
      build_id: string # required
      flow_path: string | string[] # required
      shards: number # optional, defaults to 1
      retries: number # optional, defaults to 1

```

#### `slack`

Sends a message to a Slack channel using a webhook URL.

```
jobs:
  my_job:
    type: slack
    params:
      webhook_url: string # required
      message: string # required if payload is not provided
      payload: object # required if message is not provided

```

Custom jobs
-----------

Runs custom code and can use built-in EAS functions. Does not require a `type` field.

```
jobs:
  my_job:
    steps:
      # ...

```

### `jobs.<job_id>.steps`

A job contains a sequence of tasks called `steps`. Steps can run commands. `steps` may only be provided in custom jobs and `build` jobs.

```
jobs:
  my_job:
    steps:
      - name: My first step
        run: echo "Hello World"

```

### `jobs.<job_id>.outputs`

A list of outputs defined by the job. These outputs are accessible to all downstream jobs that depend on this job. To set outputs, use the `set-output` function within a job step.

Downstream jobs can access these outputs using the following expressions within [interpolation contexts](/eas/workflows/syntax#interpolation):

* `needs.<job_id>.outputs.<output_name>`
* `after.<job_id>.outputs.<output_name>`

Here, `<job_id>` refers to the identifier of the upstream job, and `<output_name>` refers to the specific output variable you want to access.

In the example below, the `set-output` function sets the output named `test` to the value `hello world` in `job_1`'s `step_1` step. Later in `job_2`, it's accessed in `step_2` using `needs.job_1.outputs.output_1`.

```
jobs:
  job_1:
    outputs:
      output_1: ${{ steps.step_1.outputs.test }}
    steps:
      - id: step_1
        run: set-output test "hello world"
  job_2:
    needs: [job_1]
    steps:
      - id: step_2
        run: echo ${{ needs.job_1.outputs.output_1 }}

```

### `jobs.<job_id>.image`

Specifies the VM image to use for the job. See [Infrastructure](/build-reference/infrastructure) for available images.

```
jobs:
  my_job:
    image: auto | string # optional, defaults to 'auto'

```

### `jobs.<job_id>.runs_on`

Specifies the worker that will execute the job. Available only on custom jobs.

```
jobs:
  my_job:
    runs_on: linux-medium | linux-large |
      linux-medium-nested-virtualization |
      linux-large-nested-virtualization |
      macos-medium | macos-large # optional, defaults to linux-medium

```

| Worker | vCPU | Memory (GiB RAM) | SSD (GiB) | Notes |
| --- | --- | --- | --- | --- |
| linux-medium | 4 | 16 | 14 | Default worker. |
| linux-large | 8 | 32 | 28 |  |
| linux-medium-nested-virtualization | 4 | 16 | 14 | Allows running Android Emulators. |
| linux-large-nested-virtualization | 4 | 32 | 28 | Allows running Android Emulators. |

| Worker | Efficiency cores | Unified memory (GiB RAM) | SSD (GiB) | Notes |
| --- | --- | --- | --- | --- |
| macos-medium | 5 | 20 | 125 | Runs iOS jobs, including simulators. |
| macos-large | 10 | 40 | 125 | Runs iOS jobs, including simulators. |

> Note: For Android Emulator jobs, you must use a `linux-*-nested-virtualization` worker. For iOS builds and iOS Simulator jobs, you must use a `macos-*` worker.

### `jobs.<job_id>.steps.<step>.id`

The `id` property is used to reference the step in the job. Useful for using the step's output in a downstream job.

```
jobs:
  my_job:
    outputs:
      test: ${{ steps.step_1.outputs.test }} # References the output from step_1
    steps:
      - id: step_1
        run: set-output test "hello world"

```

### `jobs.<job_id>.steps.<step>.name`

The human-friendly name of the step, which is displayed in the job's logs. When a step's name is not provided, the `run` command is used as the step name.

```
jobs:
  my_job:
    steps:
      - name: My first step
        run: echo "Hello World"

```

### `jobs.<job_id>.steps.<step>.run`

The shell command to run in the step.

```
jobs:
  my_job:
    steps:
      - run: echo "Hello World"

```

### `jobs.<job_id>.steps.<step>.working_directory`

The directory to run the command in. When defined at the step level, it overrides the `jobs.<job_id>.defaults.run.working_directory` setting on the job if it is also defined.

```
jobs:
  my_job:
    steps:
      - uses: eas/checkout
      - run: pwd # prints: /home/expo/workingdir/build/my-app
        working_directory: ./my-app

```

### `jobs.<job_id>.steps.<step>.uses`

EAS provides a set of built-in reusable functions that you can use in workflow steps. The `uses` keyword is used to specify the function to use. All built-in functions start with the `eas/` prefix.

```
jobs:
  my_job:
    steps:
      - uses: eas/checkout
      - uses: eas/install_node_modules
      - uses: eas/prebuild
      - name: List files
        run: ls -la

```

Below is a list of built-in functions you can use in your workflow steps.

#### `eas/checkout`

Checks out your project source files.

```
jobs:
  my_job:
    steps:
      - uses: eas/checkout

```

[eas/checkout source code

View the source code for the eas/checkout function on GitHub.](https://github.com/expo/eas-build/blob/main/packages/build-tools/src/steps/functions/checkout.ts)

#### `eas/install_node_modules`

Installs node\_modules using the package manager (bun, npm, pnpm, or Yarn) detected based on your project. Works with monorepos.

example.yml

Copy

```
jobs:
  my_job:
    steps:
      - uses: eas/checkout
      - uses: eas/install_node_modules

```

[eas/install\_node\_modules source code

View the source code for the eas/install\_node\_modules function on GitHub.](https://github.com/expo/eas-build/blob/main/packages/build-tools/src/steps/functions/installNodeModules.ts)

#### `eas/prebuild`

Runs the `expo prebuild` command using the package manager (bun, npm, pnpm, or Yarn) detected based on your project with the command best suited for your build type and build environment.

```
jobs:
  my_job:
    steps:
      - uses: eas/checkout
      - uses: eas/install_node_modules
      - uses: eas/prebuild

```

```
jobs:
  my_job:
    steps:
      - uses: eas/checkout
      - uses: eas/install_node_modules
      - uses: eas/resolve_apple_team_id_from_credentials
        id: resolve_apple_team_id_from_credentials
      - uses: eas/prebuild
        with:
          clean: false
          apple_team_id: ${{ steps.resolve_apple_team_id_from_credentials.outputs.apple_team_id }}

```

| Property | Type | Description |
| --- | --- | --- |
| `clean` | `boolean` | Optional property defining whether the function should use `--clean` flag when running the command. Defaults to false. |
| `apple_team_id` | `string` | Optional property defining Apple team ID which should be used when doing prebuild. It should be specified for iOS builds using credentials. |

[eas/prebuild source code

View the source code for the eas/prebuild function on GitHub.](https://github.com/expo/eas-build/blob/main/packages/build-tools/src/steps/functions/prebuild.ts)

#### `eas/send_slack_message`

Sends a specified message to a configured [Slack webhook URL](https://api.slack.com/messaging/webhooks), which then posts it in the related Slack channel. The message can be specified as plaintext or as a [Slack Block Kit](https://api.slack.com/block-kit) message.
With both cases, you can reference build job properties and [use other steps outputs](/eas/workflows/syntax#jobsjob_idoutputs) in the message for dynamic evaluation. For example, `Build URL: ${{ eas.job.expoBuildUrl }}`, `Build finished with status: ${{ steps.run_fastlane.status_text }}`, `Build failed with error: ${{ steps.run_gradle.error_text }}`.
Either "message" or "payload" has to be specified, but not both.

```
jobs:
  my_job:
    steps:
      - uses: eas/send_slack_message
        with:
          message: 'This is a message to plain input URL'
          slack_hook_url: 'https://hooks.slack.com/services/[rest_of_hook_url]'

```

| Property | Type | Description |
| --- | --- | --- |
| `message` | `string` | The text of the message you want to send. For example, `'This is the content of the message'`.   Note: Either `message` or `payload` needs to be provided, but not both. |
| `payload` | `json` | The contents of the message you want to send which are defined using [Slack Block Kit](https://api.slack.com/block-kit) layout.   Note: Either `message` or `payload` needs to be provided, but not both. |
| `slack_hook_url` | `string` | The previously configured Slack webhook URL, which will post your message to the specified channel. You can provide the plain URL like `slack_hook_url: 'https://hooks.slack.com/services/[rest_of_hook_url]'`, use EAS secrets like `slack_hook_url: ${{ eas.env.ANOTHER_SLACK_HOOK_URL }}`, or set the `SLACK_HOOK_URL` secret, which will serve as a default webhook URL (in this last case, there is no need to provide the `slack_hook_url` property). |

[eas/send\_slack\_message source code

View the source code for the eas/send\_slack\_message function on GitHub.](https://github.com/expo/eas-build/blob/main/packages/build-tools/src/steps/functions/sendSlackMessage.ts)

#### `eas/use_npm_token`

Configures Node package managers (bun, npm, pnpm, or Yarn) for use with private packages, published either to npm or a private registry.

Set `NPM_TOKEN` in your project's secrets, and this function will configure the build environment by creating .npmrc with the token.

example.yml

Copy

```
jobs:
  my_job:
    name: Install private npm modules
    steps:
      - uses: eas/checkout
      - uses: eas/use_npm_token
      - name: Install dependencies
        run: npm install # <---- Can now install private packages

```

[eas/use\_npm\_token source code

View the source code for the eas/use\_npm\_token function on GitHub.](https://github.com/expo/eas-build/blob/main/packages/build-tools/src/steps/functions/useNpmToken.ts)

[Previous (EAS Workflows)

Example CI/CD workflows](/eas/workflows/examples)[Next (EAS Workflows)

Automating EAS CLI commands](/eas/workflows/automating-eas-cli)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas/workflows/syntax.mdx)
* Last updated on May 10, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Workflow files](/eas/workflows/syntax/#workflow-files)[Configuration Reference](/eas/workflows/syntax/#configuration-reference)[name](/eas/workflows/syntax/#name)[on](/eas/workflows/syntax/#on)[on.push](/eas/workflows/syntax/#onpush)[on.pull\_request](/eas/workflows/syntax/#onpull_request)[on.pull\_request\_labeled](/eas/workflows/syntax/#onpull_request_labeled)[on.schedule.cron](/eas/workflows/syntax/#onschedulecron)[jobs](/eas/workflows/syntax/#jobs)[jobs.<job\_id>](/eas/workflows/syntax/#jobsjob_id)[jobs.<job\_id>.name](/eas/workflows/syntax/#jobsjob_idname)[jobs.<job\_id>.environment](/eas/workflows/syntax/#jobsjob_idenvironment)[jobs.<job\_id>.defaults.run.working\_directory](/eas/workflows/syntax/#jobsjob_iddefaultsrunworking_directory)[defaults](/eas/workflows/syntax/#defaults)[defaults.run.working\_directory](/eas/workflows/syntax/#defaultsrunworking_directory)[defaults.tools](/eas/workflows/syntax/#defaultstools)[concurrency](/eas/workflows/syntax/#concurrency)[Control flow](/eas/workflows/syntax/#control-flow)[jobs.<job\_id>.needs](/eas/workflows/syntax/#jobsjob_idneeds)[jobs.<job\_id>.after](/eas/workflows/syntax/#jobsjob_idafter)[jobs.<job\_id>.if](/eas/workflows/syntax/#jobsjob_idif)[Interpolation](/eas/workflows/syntax/#interpolation)[after and needs](/eas/workflows/syntax/#after-and-needs)[github](/eas/workflows/syntax/#github)[success() , failure()](/eas/workflows/syntax/#success-failure)[fromJSON() , toJSON()](/eas/workflows/syntax/#fromjson-tojson)[Pre-packaged jobs](/eas/workflows/syntax/#pre-packaged-jobs)[jobs.<job\_id>.type](/eas/workflows/syntax/#jobsjob_idtype)[build](/eas/workflows/syntax/#build)[deploy](/eas/workflows/syntax/#deploy)[fingerprint](/eas/workflows/syntax/#fingerprint)[get-build](/eas/workflows/syntax/#get-build)[submit](/eas/workflows/syntax/#submit)[update](/eas/workflows/syntax/#update)[maestro](/eas/workflows/syntax/#maestro)[slack](/eas/workflows/syntax/#slack)[Custom jobs](/eas/workflows/syntax/#custom-jobs)[jobs.<job\_id>.steps](/eas/workflows/syntax/#jobsjob_idsteps)[jobs.<job\_id>.outputs](/eas/workflows/syntax/#jobsjob_idoutputs)[jobs.<job\_id>.image](/eas/workflows/syntax/#jobsjob_idimage)[jobs.<job\_id>.runs\_on](/eas/workflows/syntax/#jobsjob_idruns_on)[jobs.<job\_id>.steps.<step>.id](/eas/workflows/syntax/#jobsjob_idstepsstepid)[jobs.<job\_id>.steps.<step>.name](/eas/workflows/syntax/#jobsjob_idstepsstepname)[jobs.<job\_id>.steps.<step>.run](/eas/workflows/syntax/#jobsjob_idstepssteprun)[jobs.<job\_id>.steps.<step>.working\_directory](/eas/workflows/syntax/#jobsjob_idstepsstepworking_directory)[jobs.<job\_id>.steps.<step>.uses](/eas/workflows/syntax/#jobsjob_idstepsstepuses)[eas/checkout](/eas/workflows/syntax/#eascheckout)[eas/install\_node\_modules](/eas/workflows/syntax/#easinstall_node_modules)[eas/prebuild](/eas/workflows/syntax/#easprebuild)[eas/send\_slack\_message](/eas/workflows/syntax/#eassend_slack_message)[eas/use\_npm\_token](/eas/workflows/syntax/#easuse_npm_token)