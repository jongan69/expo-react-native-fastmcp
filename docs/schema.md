Custom build configuration schema - Expo Documentation

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

[Get started](/custom-builds/get-started)[Config schema](/custom-builds/schema)[TypeScript functions](/custom-builds/functions)

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

Custom build configuration schema
=================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/custom-builds/schema.mdx)

A reference of configuration options for custom builds with EAS Build.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/custom-builds/schema.mdx)

---

Creating custom builds for EAS Build helps customize the build process for your project.

YAML syntax for custom builds
-----------------------------

Custom build config files are stored inside the .eas/build directory path. They use YAML syntax and must have a `.yml` or `.yaml` file extension. If you are new to YAML or want to learn more about the syntax, see [Learn YAML in Y minutes](https://learnxinyminutes.com/docs/yaml/).

`build`
-------

Defined to describe a custom build configuration. All config options to create a custom build are specified under it.

### `name`

The name of your custom build that is used to identify it in the build logs. EAS Build uses this property to display the name of your build in the dashboard.

For example, the build name is `Run tests`:

```
build:
  name: Run tests
  steps:
    - eas/checkout
    - run:
        name: Install dependencies
        command: npm install

```

### `steps`

Steps are used to describe a list of actions, either in the form of commands or function calls. These actions are executed when a custom build runs on EAS Build. You can define single or multiple steps in a build config. However, it is required to define at least one step per build.

Each step is configured with the following properties:

#### `steps[].run`

The `run` key is used to trigger a set of instructions. For example, a `run` key is used to install dependencies using the `npm install` command:

```
build:
  name: Install npm dependencies
  steps:
    - eas/checkout
    - run:
        name: Install dependencies
        command: npm install

```

You can also use `steps[].run` to execute single or multiline shell commands:

```
build:
  name: Run inline shell commands
  steps:
    - run: echo "Hello world"
    - run: |
        echo "Multiline"
        echo "bash commands"

```

#### Use a single step

For example, a build config with the following `steps` will print "Hello world":

```
build:
  name: Greeting
  steps:
    - run: echo "Hello world"

```

> Note: `-` before `run` counts as indentation.

#### Use multiple steps

When multiple `steps` are defined, they are executed sequentially. For example, a build config with the following `steps` will first check out the project, install npm dependencies, and then run a command to run tests:

```
build:
  name: Run tests
  steps:
    - eas/checkout
    - run:
        name: Install dependencies
        command: npm install
    - run:
        name: Run tests
        command: |
          echo "Running tests..."
          npm test

```

#### Sharing environment variables with other steps

Environment variables exported (using `export`) in one step's `command` are not automatically exposed to other steps. To share an environment variable with other steps, use the `set-env` executable.

`set-env` expects to be called with two arguments: environment variable's name and value. For example, `set-env NPM_TOKEN "abcdef"` will expose `$NPM_TOKEN` variable with value `abcdef` to other steps.

> Note: Variables shared with `set-env` are not automatically exported locally. You need to call `export` yourself.

```
build:
  name: Shared environment variable example
  steps:
    - run:
        name: Set environment variables
        command: |
          set -x

          # Set variable
          ENV_TEST_LOCAL="present-only-in-current-shell-context"
          # Set and export variable
          export ENV_TEST_LOCAL_EXPORT="present-in-current-step"
          # Set shared variable
          set-env ENV_TEST_SET_ENV "present-in-following-steps"

          # Will print "ENV_TEST_LOCAL: present-only-in-current-shell-context"
          # because current shell has access to this local variable.
          echo "ENV_TEST_LOCAL: $ENV_TEST_LOCAL"

          # Will print "ENV_TEST_LOCAL_EXPORT: present-in-current-step"
          # because export also sets the local variable value.
          echo "ENV_TEST_LOCAL_EXPORT: $ENV_TEST_LOCAL_EXPORT"

          # Will "ENV_TEST_SET_ENV: "
          # because set-env does not set or export variables.
          echo "ENV_TEST_SET_ENV: $ENV_TEST_SET_ENV"

          # Will only print LOCALLY_EXPORTED_ENV,
          # because it is the only export-ed variable.
          env | grep ENV_TEST_
    - run:
        name: Check variables values in next step
        command: |
          set -x

          # Will print "ENV_TEST_LOCAL: ", because ENV_TEST_LOCAL
          # is only a local variable in previous step.
          echo "ENV_TEST_LOCAL: $ENV_TEST_LOCAL"

          # Will print "ENV_TEST_LOCAL_EXPORT: "
          # because export does not share a variable to other steps.
          echo "ENV_TEST_LOCAL_EXPORT: $ENV_TEST_LOCAL_EXPORT"

          # Will print "ENV_TEST_SET_ENV: present-in-following-steps"
          # because set-env "exported" variable to other steps.
          echo "ENV_TEST_SET_ENV: $ENV_TEST_SET_ENV"

          # Will only print ENV_TEST_SET_ENV,
          # because set-env "exported" it to other steps.
          env | grep ENV_TEST_

```

#### `steps[].run.name`

The name used in build logs to display the name of the step.

#### `steps[].run.command`

The `command` defines a custom shell command to run when a step is executed. It is required to define a command for each step. It can be a multiline shell command:

```
build:
  name: Run tests
  steps:
    - eas/checkout
    - run:
        name: Run tests
        command: |
          echo "Running tests..."
          npm test

```

#### `steps[].run.working_directory`

The `working_directory` is used to define an existing directory from the project's root directory. After an existing path is defined in a step, using it changes the current directory for that step. For example, a step is created to list all the assets inside the assets directory, which is a directory in your Expo project. The `working_directory` is set to `assets`:

```
build:
  name: Demo
  steps:
    - eas/checkout
    - run:
        name: List assets
        working_directory: assets
        command: ls -la

```

#### `steps[].run.shell`

Used to define the default executable shell for a step. For example, the step's shell is set to `/bin/sh`:

```
build:
  name: Demo
  steps:
    - run:
        shell: /bin/sh
        command: |
          echo "Steps can use another shell"
          ps -p $$

```

#### `steps[].run.inputs`

Input values are provided to a step. For example, you can use `input` to provide a value:

```
build:
  name: Demo
  steps:
    - run:
        name: Say Hi
        inputs:
          name: Expo
        command: echo "Hi, ${ inputs.name }!"

```

#### `steps[].run.outputs`

An output value is expected during a step. For example, a step has an output value of `Hello world`:

```
build:
  name: Demo
  steps:
    - run:
        name: Produce output
        outputs: [value]
        command: |
          echo "Producing output for another step"
          set-output value "Output from another step..."

```

#### `steps[].run.outputs.required`

An output value can use a boolean to indicate if the output value is required or not. For example, a function does not have a required output value:

```
build:
  name: Demo
  steps:
    - run:
        name: Produce another output
        id: id456
        outputs:
          - required_param
          - name: optional_param
            required: false
        command: |
          echo "Producing more output"
          set-output required_param "abc 123 456"

```

#### `steps[].run.id`

Defining an `id` for a step allows:

* Calling the same function that produces one or more outputs multiple times
* Using the output from one step to another

#### Call the same function one or more times

For example, the following function generates a random number:

```
functions:
  random:
    name: Generate random number
    outputs: [value]
    command: set-output value `random_number`

```

In a build config, let's use the `random` function to generate two random numbers and print them:

```
build:
  name: Functions Demo
  steps:
    - random:
        id: random_1
    - random:
        id: random_2
    - run:
        name: Print random numbers
        inputs:
          random_1: ${ steps.random_1.value }
          random_2: ${ steps.random_2.value }
        command: |
          echo "${ inputs.random_1 }"
          echo "${ inputs.random_2 }"

```

#### Use output from one step to another

For example, the following build config demonstrates how to use output from one step to another:

```
build:
  name: Outputs demo
  steps:
    - run:
        name: Produce output
        id: id123 # <---- !!!
        outputs: [foo]
        command: |
          echo "Producing output for another step"
          set-output foo bar
    - run:
        name: Use output from another step
        inputs:
          foo: ${ steps.id123.foo }
        command: |
          echo "foo = \"${ inputs.foo }\""

```

`functions`
-----------

Defined to describe a reusable function that can be used in a build config. All config options to create a function are specified with the following properties:

### `functions.[function_name]`

The `[function_name]` is the name of a function that you define to identify it in the `build.steps`. For example, you can define a function with the name `greetings`:

```
functions:
  greetings:
    name: Say Hi!

```

### `functions.[function_name].name`

The name that is used in build logs to display the name of the function. For example, a function with the display name `Say Hi!`:

```
functions:
  greetings:
    name: Say Hi!

```

### `functions.[function_name].inputs`

Input values are provided to a function.

#### `inputs[].name`

The name of the input value. It is used as an identifier to access the input value such as in bash command interpolation.

```
functions:
  greetings:
    name: Say Hi!
    inputs:
      - name: name
        default_value: Hello world
    command: echo "${ inputs.name }!"

```

#### `inputs[].required`

Boolean to indicate if the input value is required or not. For example, a function does not have a required value:

```
functions:
  greetings:
    name: Say Hi!
    inputs:
      - name: name
        required: false

```

#### `inputs[].type`

The type of the input value. It can be either `string`, `num` or `json`.

Input values set in the function call as well as `default_value` and `allowed_values` for the function are validated against the type.

The default input `type` is `string`.

For example, a function has an input value of type `string`:

```
functions:
  greetings:
    name: Say Hi!
    inputs:
      - name: name
        type: string
      - name: age
        type: num
      - name: other_data
        type: json

```

#### `inputs[].default_value`

You can use `default_value` to provide one default input. For example, a function has a default value of `Hello world`:

```
functions:
  greetings:
    name: Say Hi!
    inputs:
      - name: name
        default_value: Hello world

```

#### `inputs[].allowed_values`

You can use `allowed_values` to provide multiple values in an array. For example, a function has multiple allowed values:

```
functions:
  greetings:
    name: Say Hi!
    inputs:
      - name: name
        default_value: Hello world
        allowed_values: [Hi, Hello, Hey]
        type: string

```

#### Multiple input values

Multiple input values can be provided to a function.

```
functions:
  greetings:
    name: Say Hi!
    inputs:
      - name: name
        default_value: Expo
      - name: greeting
        default_value: Hi
        allowed_values: [Hi, Hello]
    command: echo "${ inputs.greeting }, ${ inputs.name }!"

```

### `functions.[function_name].outputs`

An output value is expected from a function. For example, a function has an output value of `Hello world`:

```
functions:
  greetings:
    name: Say Hi!
    outputs: [value]
    command: set-output value "Hello world"

```

#### `outputs[].name`

The name of the output value. It is used as an identifier to access the output value in another step:

```
functions:
  greetings:
    name: Say Hi!
    outputs:
      - name: name

```

#### `outputs[].required`

Boolean to indicate if the output value is required or not. For example, a function does not have a required output value:

```
functions:
  greetings:
    name: Say Hi!
    outputs:
      - name: value
        required: false

```

### `functions.[function_name].command`

Used to define the command to run when a function is executed, if you wish the function to be a simple shell script. Each function is required to define either a `command` or a `path` to JS/TS module implementing the function. For example, the command `echo "Hello world"` is used to print a message:

```
functions:
  greetings:
    name: Say Hi!
    command: echo "Hi!"

```

### `functions.[function_name].path`

Used to define the path to a JavaScript/TypeScript module implementing the function. Each function is required to define either a `command` or a `path` property. For example, the path `./greetings` is used to execute a `greetings` function declared in the `greetings` module:

```
functions:
  greetings:
    name: Say Hi!
    path: ./greetings

```

> [Learn more about building and using custom TypeScript/JavaScript functions](/custom-builds/functions).

### `functions.[function_name].shell`

Used to define the default executable shell for a step where a function is executed. For example, the step's shell is set to `/bin/sh`:

```
functions:
  greetings:
    name: Say Hi!
    shell: /bin/sh
    command: echo "Hi!"

```

### `functions.[function_name].supported_platforms`

Used to define the supported platforms for a function. Defaults to all platforms. Allowed platforms: `darwin`, `linux`.

For example, the function's supported platform is `darwin` (macOS):

```
functions:
  greetings:
    name: Say Hi!
    supported_platforms: [darwin]
    command: echo "Hi!"

```

`import`
--------

A config file path list used to import functions from other config files. Imported files cannot have the `build` section.

For example, the following build config imports two files and calls two imported functions - `say_hi` and `say_bye`.

build-and-test.yml

Copy

```
import:
  - common-functions.yml
  - another-file.yml

build:
  steps:
    - say_hi
    - say_bye

```

common-functions.yml

Copy

```
functions:
  say_hi:
    name: Say Hi!
    command: echo "Hi!"

```

another-file.yml

Copy

```
functions:
  say_bye:
    name: Say bye :(
    command: echo "Bye!"

```

Functions
---------

### Built-in EAS functions

EAS provides a set of built-in reusable functions that you can use in a build config without defining the function definition.

> Tip: Any function that is built-in and provided by EAS must start with the `eas/` prefix.

#### `eas/build`

The all-in-one function that encapsulates the entire EAS Build build process. It resolves the best build configuration based on your build profile's settings from [eas.json](/eas/json).

It's ideal for people who want to have the build done without worrying about altering and configuring the build process manually. It can be a great starting point for your custom build configuration if you are interested in using other custom steps before or after the build process and you don't want to change the build process itself.

example.yml

Copy

```
build:
  name: Run a build using a single command
  steps:
    - eas/build

```

To have more control over the build process and customize it as per your requirements, see the following custom functions and steps that run in the background by `eas/build`. They are executed as a build process based on your build profile's configuration.

##### Android

When a build configuration is using [`withoutCredentials`](/eas/json#withoutcredentials):

* [`eas/checkout`](/custom-builds/schema#eascheckout)
* [`eas/use_npm_token`](/custom-builds/schema#easuse_npm_token)
* [`eas/install_node_modules`](/custom-builds/schema#easinstall_node_modules)
* [`eas/resolve_build_config`](/custom-builds/schema#easresolve_build_config)
* [`eas/prebuild`](/custom-builds/schema#easprebuild)
* [`eas/configure_eas_update`](/custom-builds/schema#easconfigure_eas_update)
* [`eas/run_gradle`](/custom-builds/schema#easrun_gradle)
* [`eas/find_and_upload_build_artifacts`](/custom-builds/schema#easfind_and_upload_build_artifacts)

When a build configuration uses credentials (for both `internal` and `store` [distribution](/eas/json#distribution) builds):

* [`eas/checkout`](/custom-builds/schema#eascheckout)
* [`eas/use_npm_token`](/custom-builds/schema#easuse_npm_token)
* [`eas/install_node_modules`](/custom-builds/schema#easinstall_node_modules)
* [`eas/resolve_build_config`](/custom-builds/schema#easresolve_build_config)
* [`eas/prebuild`](/custom-builds/schema#easprebuild)
* [`eas/configure_eas_update`](/custom-builds/schema#easconfigure_eas_update)
* [`eas/inject_android_credentials`](/custom-builds/schema#easinject_android_credentials)
* [`eas/configure_android_version`](/custom-builds/schema#easconfigure_android_version)
* [`eas/run_gradle`](/custom-builds/schema#easrun_gradle)
* [`eas/find_and_upload_build_artifacts`](/custom-builds/schema#easfind_and_upload_build_artifacts)

##### iOS

When a build configuration is using [`withoutCredentials`](/eas/json#withoutcredentials) or [`simulator`](/eas/json#simulator):

* [`eas/checkout`](/custom-builds/schema#eascheckout)
* [`eas/use_npm_token`](/custom-builds/schema#easuse_npm_token)
* [`eas/install_node_modules`](/custom-builds/schema#easinstall_node_modules)
* [`eas/resolve_build_config`](/custom-builds/schema#easresolve_build_config)
* [`eas/prebuild`](/custom-builds/schema#easprebuild)
* Install pods using the `pod install` command
* [`eas/configure_eas_update`](/custom-builds/schema#easconfigure_eas_update)
* [`eas/generate_gymfile_from_template`](/custom-builds/schema#easgenerate_gymfile_from_template)
* [`eas/run_fastlane`](/custom-builds/schema#easrun_fastlane)
* [`eas/find_and_upload_build_artifacts`](/custom-builds/schema#easfind_and_upload_build_artifacts)

When a build configuration uses credentials (for both `internal` and `store` [distribution](/eas/json#distribution) builds):

* [`eas/checkout`](/custom-builds/schema#eascheckout)
* [`eas/use_npm_token`](/custom-builds/schema#easuse_npm_token)
* [`eas/install_node_modules`](/custom-builds/schema#easinstall_node_modules)
* [`eas/resolve_build_config`](/custom-builds/schema#easresolve_build_config)
* [`eas/resolve_apple_team_id_from_credentials`](/custom-builds/schema#easresolve_apple_team_id_from_credentials)
* [`eas/prebuild`](/custom-builds/schema#easprebuild)
* Install pods using the `pod install` command
* [`eas/configure_eas_update`](/custom-builds/schema#easconfigure_eas_update)
* [`eas/configure_ios_credentials`](/custom-builds/schema#easconfigure_ios_credentials)
* [`eas/configure_ios_version`](/custom-builds/schema#easconfigure_ios_version)
* [`eas/generate_gymfile_from_template`](/custom-builds/schema#easgenerate_gymfile_from_template)
* [`eas/run_fastlane`](/custom-builds/schema#easrun_fastlane)
* [`eas/find_and_upload_build_artifacts`](/custom-builds/schema#easfind_and_upload_build_artifacts)

You can replace the `eas/build` command call by using these steps in your YAML configuration file:

[ios-simulator-build.yml

View the steps executed behind the scenes by the `eas/build` function for an iOS simulator build in our example repository.](https://github.com/expo/eas-custom-builds-example/blob/main/.eas/build/ios-simulator-build.yml)
[ios-credentials-build.yml

View the steps executed behind the scenes by the `eas/build` function for an iOS build with credentials in our example repository.](https://github.com/expo/eas-custom-builds-example/blob/main/.eas/build/ios-build-with-credentials.yml)
[android-build-without-credentials.yml

View the steps executed behind the scenes by the `eas/build` function for an Android build without credentials in our example repository.](https://github.com/expo/eas-custom-builds-example/blob/main/.eas/build/android-build-without-credentials.yml)
[android-build-with-credentials.yml

View the steps executed behind the scenes by the `eas/build` function for an Android build with credentials in our example repository.](https://github.com/expo/eas-custom-builds-example/blob/main/.eas/build/android-build-with-credentials.yml)

##### Known limitations

* It doesn't accept any inputs, and the resolved build process will be configured based on your build profile from [eas.json](/eas/json).
* The build process produced by `eas/build` is not configurable and you can't customize it. If you need to customize the build process, use the subset of functions and steps that are executed behind the scenes by this function and configure them manually in the YAML configuration file, as shown in the examples above.

#### `eas/maestro_test`

All-in-one function that installs Maestro, prepares a testing environment (Android Emulator or iOS Simulator), and tests the app.

> Your project must be configured to use the old Build Infrastructure to start Android Emulator. Go to [Project settings](https://expo.dev/accounts/%5Baccount%5D/projects/%5Bproject%5D/settings) to configure. See [this changelog post](https://expo.dev/changelog/2024/08-29-c3d-default) for more information.

| Input | Type | Description |
| --- | --- | --- |
| `flow_path` | `string` | Path (or multiple paths, each in a separate line) to [Maestro flows](https://maestro.mobile.dev/getting-started/writing-your-first-flow) to run. |
| `app_path` | `string` | Path (or regex pattern) to the emulator/simulator app that should be tested. If not provided, it defaults to android/app/build/outputs/\*\*/\*.apk for Android and to ios/build/Build/Products/\*simulator/\*.app for iOS. |

build-and-test.yml

Copy

```
build:
  name: Build and test
  steps:
    - eas/build
    - eas/maestro_test:
        inputs:
          flow_path: |
            maestro/sign_in.yml
            maestro/create_post.yml
            maestro/sign_out.yml

```

test-ios-simulator-app.yml

Copy

```
build:
  name: Build and test iOS simulator app
  steps:
    - eas/checkout
    - eas/maestro_test:
        app_path: ./fixtures/my_app.app
        inputs:
          flow_path: |
            maestro/sign_in.yml
            maestro/create_post.yml
            maestro/sign_out.yml

```

test-android-emulator-app.yml

Copy

```
build:
  name: Build and test Android emulator app
  steps:
    - eas/checkout
    - eas/maestro_test:
        app_path: ./fixtures/my_app.apk
        inputs:
          flow_path: |
            maestro/sign_in.yml
            maestro/create_post.yml
            maestro/sign_out.yml

```

Behind the scenes, it uses:

* [`eas/install_maestro`](/custom-builds/schema#easinstall_maestro) to install Maestro
* [`eas/start_android_emulator`](/custom-builds/schema#easstart_android_emulator) to start an Android Emulator if needed
* [`eas/start_ios_simulator`](/custom-builds/schema#easstart_ios_simulator) to start an iOS Simulator if needed
* Custom `run` to install .apk to the running Android Emulator and .app to iOS Simulator
* Series of `run` to execute `maestro test` for each of the provided flows
* [`eas/upload_artifact`](/custom-builds/schema#easupload_artifact) to upload Maestro test artifacts as build artifact

> We have observed that Maestro tests often time out if run on images with Xcode 15.0 or 15.2. Use the `latest` image to avoid any issues.

If you need to customize the Maestro version, run a specific Android Emulator or iOS Simulator, or upload multiple build artifacts you will need to write this series of steps yourself.

An example Android build config with `eas/maestro_test` expanded

build-and-test-android-expanded.yml

Copy

```
build:
  name: Build and test (Android, expanded)
  steps:
    - eas/build
    - eas/install_maestro
    - eas/start_android_emulator:
        inputs:
          system_package_name: system-images;android-34;default;x86_64
    - run:
        command: |
          # shopt -s globstar is necessary to add /**/ support
          shopt -s globstar
          # shopt -s nullglob is necessary not to try to install
          # SEARCH_PATH literally if there are no matching files.
          shopt -s nullglob

          SEARCH_PATH="android/app/build/outputs/**/*.apk"
          FILES_FOUND=false

          for APP_PATH in $SEARCH_PATH; do
            FILES_FOUND=true
            echo "Installing \\"$APP_PATH\\""
            adb install "$APP_PATH"
          done

          if ! $FILES_FOUND; then
            echo "No files found matching \\"$SEARCH_PATH\\". Are you sure you've built an Emulator app?"
            exit 1
          fi
    - run:
        command: |
          maestro test maestro/flow.yml
    - eas/upload_artifact:
        name: Upload test artifact
        if: ${ always() }
        inputs:
          type: build-artifact
          path: ${ eas.env.HOME }/.maestro/tests

```

An example iOS build config with `eas/maestro_test` expanded

build-and-test-ios-expanded.yml

Copy

```
build:
name: Build and test (iOS, expanded)
steps:
  - eas/build
  - eas/install_maestro
  - eas/start_ios_simulator
  - run:
      command: |
        # shopt -s nullglob is necessary not to try to install
        # SEARCH_PATH literally if there are no matching files.
        shopt -s nullglob

        SEARCH_PATH="ios/build/Build/Products/*simulator/*.app"
        FILES_FOUND=false

        for APP_PATH in $SEARCH_PATH; do
          FILES_FOUND=true
          echo "Installing \\"$APP_PATH\\""
          xcrun simctl install booted "$APP_PATH"
        done

        if ! $FILES_FOUND; then
          echo "No files found matching \\"$SEARCH_PATH\\". Are you sure you've built a Simulator app?"
          exit 1
        fi
  - run:
      command: |
        maestro test maestro/flow.yml
  - eas/upload_artifact:
      name: Upload test artifact
      if: ${ always() }
      inputs:
        type: build-artifact
        path: ${ eas.env.HOME }/.maestro/tests

```

[eas/maestro\_test source code

View the source code for the eas/maestro\_test function on GitHub.](https://github.com/expo/eas-build/blob/main/packages/build-tools/src/steps/functionGroups/maestroTest.ts)

#### `eas/checkout`

Checks out your project source files.

For example, a build config with the following `steps` will check out the project and list the files in the assets directory:

upload.yml

Copy

```
build:
  name: List files
  steps:
    - eas/checkout
    - run:
        name: List assets
        run: ls assets

```

[eas/checkout source code

View the source code for the eas/checkout function on GitHub.](https://github.com/expo/eas-build/blob/main/packages/build-tools/src/steps/functions/checkout.ts)

#### `eas/use_npm_token`

Configures node package managers (npm, pnpm, or Yarn) for use with private packages, published either to npm or a private registry.
Set `NPM_TOKEN` in your project's secrets, and this function will configure the build environment by creating .npmrc with the token.

example.yml

Copy

```
build:
  name: Install private npm modules
  steps:
    - eas/checkout
    - eas/use_npm_token
    - run:
        name: Install dependencies
        run: npm install # <---- Can now install private packages

```

[eas/use\_npm\_token source code

View the source code for the eas/use\_npm\_token function on GitHub.](https://github.com/expo/eas-build/blob/main/packages/build-tools/src/steps/functions/useNpmToken.ts)

#### `eas/install_node_modules`

Installs node modules using the package manager (npm, pnpm, or Yarn) detected based on your project. Works with monorepos.

example.yml

Copy

```
build:
  name: Install node modules
  steps:
    - eas/checkout
    - eas/install_node_modules

```

[eas/install\_node\_modules source code

View the source code for the eas/install\_node\_modules function on GitHub.](https://github.com/expo/eas-build/blob/main/packages/build-tools/src/steps/functions/installNodeModules.ts)

#### `eas/resolve_build_config`

Resolves and prints the build configuration. If the build has been triggered by the GitHub integration, it will update the current `job` and `metadata` context values. It should be called after installing the dependencies because the config may be influenced by config plugins.

This function is automatically executed by the [`eas/build`](/custom-builds/schema#easbuild) function group.

[eas/resolve\_build\_config source code

View the source code for the eas/resolve\_build\_config function on GitHub.](https://github.com/expo/eas-build/blob/main/packages/build-tools/src/steps/functions/resolveBuildConfig.ts)

#### `eas/get_credentials_for_build_triggered_by_github_integration`

> Deprecated: Replace this step with [`eas/resolve_build_config`](/custom-builds/schema#easresolve_build_config).

#### `eas/resolve_apple_team_id_from_credentials`

> This function is only available for iOS builds.

Resolves the Apple team ID value based on build credentials provided in the `inputs.credentials`. The resolved Apple team ID is stored in the `outputs.apple_team_id` output value.

example.yml

Copy

```
build:
  name: Run prebuild script
  steps:
    - eas/checkout
    - eas/install_node_modules
    - eas/resolve_apple_team_id_from_credentials:
        id: resolve_apple_team_id_from_credentials
    - eas/prebuild:
        inputs:
          apple_team_id: ${ steps.resolve_apple_team_id_from_credentials.apple_team_id }

```

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | The name of the step in the reusable function that shows in the build logs. Defaults to `Resolve Apple team ID from credentials`. |
| `inputs.credentials` | `json` | Optional input defining the app credentials for your iOS build. Defaults to `${ eas.job.secrets.buildCredentials }`. Needs to comply to `${ eas.job.secrets.buildCredentials }` schema for iOS. |

[eas/resolve\_apple\_team\_id\_from\_credentials source code

View the source code for the eas/resolve\_apple\_team\_id\_from\_credentials function on GitHub.](https://github.com/expo/eas-build/blob/main/packages/build-tools/src/steps/functions/resolveAppleTeamIdFromCredentials.ts)

#### `eas/prebuild`

Runs the `expo prebuild` command using the package manager (npm, pnpm, or Yarn) detected based on your project with the command best suited for your build type and build environment.

example.yml

Copy

```
build:
  name: Run prebuild script
  steps:
    - eas/checkout
    - eas/install_node_modules
    - eas/resolve_apple_team_id_from_credentials:
        id: resolve_apple_team_id_from_credentials
    - eas/prebuild:
        inputs:
          clean: false
          apple_team_id: ${ steps.resolve_apple_team_id_from_credentials.apple_team_id }

```

example.yml

Copy

```
build:
  name: Run prebuild script
  steps:
    - eas/checkout
    - eas/install_node_modules
    - eas/prebuild

```

| Property | Type | Description |
| --- | --- | --- |
| `name` | - | The name of the step in the reusable function that shows in the build logs. Defaults to `Prebuild`. |
| `inputs.clean` | `boolean` | Optional input defining whether the function should use `--clean` flag when running the command. Defaults to false |
| `inputs.apple_team_id` | `boolean` | Optional input defining Apple team ID which should be used when doing prebuild. It should be specified for iOS builds using credentials. |

[eas/prebuild source code

View the source code for the eas/resolve\_apple\_team\_id\_from\_credentials function on GitHub.](https://github.com/expo/eas-build/blob/main/packages/build-tools/src/steps/functions/prebuild.ts)

#### `eas/configure_eas_update`

> To use this function you need to have EAS Update configured for your project.

Configures runtime version and release channel for your build.

example.yml

Copy

```
build:
  name: Configure EAS Update
  steps:
    - eas/checkout
    - eas/install_node_modules
    - eas/prebuild
    - eas/configure_eas_update

```

example.yml

Copy

```
build:
  name: Configure EAS Update
  steps:
    - eas/checkout
    - eas/install_node_modules
    - eas/prebuild
    - eas/configure_eas_update:
        inputs:
          runtime_version: 1.0.0
          channel: mychannel

```

| Property | Type | Description |
| --- | --- | --- |
| `name` | - | The name of the step in the reusable function that shows in the build logs. Defaults to `Configure EAS Update`. |
| `inputs.runtime_version` | `string` | Optional input defining runtime version which should be configured for the build. Defaults to `${ eas.job.version.runtimeVersion }` or natively defined runtime version. |
| `inputs.channel` | `string` | Optional input defining channel which should be configured for the build. Defaults to `${ eas.job.updates.channel }`. |

[eas/configure\_eas\_update source code

View the source code for the eas/configure\_eas\_update function on GitHub.](https://github.com/expo/eas-build/blob/main/packages/build-tools/src/steps/functions/configureEASUpdateIfInstalled.ts)

#### `eas/inject_android_credentials`

> This function is only available for Android builds.

Configures Android keystore with credentials on the builder and injects app signing config using these credentials into gradle config.

example.yml

Copy

```
build:
  name: Android credentials
  steps:
    - eas/checkout
    - eas/install_node_modules
    - eas/prebuild
    - eas/inject_android_credentials

```

| Property | Type | Description |
| --- | --- | --- |
| `name` | - | The name of the step in the reusable function that shows in the build logs. Defaults to `Inject Android credentials`. |
| `inputs.credentials` | `json` | Optional input defining the app credentials for your Android build. Defaults to `${ eas.job.secrets.buildCredentials }`. Needs to comply to `${ eas.job.secrets.buildCredentials }` schema for Android. |

[eas/inject\_android\_credentials source code

View the source code for the eas/inject\_android\_credentials function on GitHub.](https://github.com/expo/eas-build/blob/main/packages/build-tools/src/steps/functions/injectAndroidCredentials.ts)

#### `eas/configure_ios_credentials`

> This function is only available for iOS builds.

Configures iOS credentials on the builder. Modifies the configuration of the Xcode project by assigning provisioning profiles to the targets.

example.yml

Copy

```
build:
  name: iOS credentials
  steps:
    - eas/checkout
    - eas/install_node_modules
    - eas/resolve_apple_team_id_from_credentials:
        id: resolve_apple_team_id_from_credentials
    - eas/prebuild:
        inputs:
          clean: false
          apple_team_id: ${ steps.resolve_apple_team_id_from_credentials.apple_team_id }
    - eas/configure_ios_credentials

```

| Property | Type | Description |
| --- | --- | --- |
| `name` | - | The name of the step in the reusable function that shows in the build logs. Defaults to `Configure iOS credentials`. |
| `inputs.build_configuration` | `string` | Optional input defining the Xcode project's Build Configuration. Defaults to `${ eas.job.buildConfiguration }` or if not specified is resolved to `Debug` for development client or `Release` for other builds. |
| `inputs.credentials` | `json` | Optional input defining the app credentials for your iOS build. Defaults to `${ eas.job.secrets.buildCredentials }`. Needs to comply to `${ eas.job.secrets.buildCredentials }` schema for iOS. |

[eas/configure\_ios\_credentials source code

View the source code for the eas/configure\_ios\_credentials function on GitHub.](https://github.com/expo/eas-build/blob/main/packages/build-tools/src/steps/functions/configureIosCredentials.ts)

#### `eas/configure_android_version`

> This function is only available for Android builds.

Configures the version of your Android app. It's used to set a version when using [remote app version management](/build-reference/app-versions).

It's not mandatory to use this function, if it's not used the version from native code generated during the prebuild phase will be used.

example.yml

Copy

```
build:
  name: Configure Android version
  steps:
    - eas/checkout
    - eas/install_node_modules
    - eas/prebuild
    - eas/configure_eas_update
    - eas/inject_android_credentials
    - eas/configure_android_version

```

example.yml

Copy

```
build:
  name: Configure Android version
  steps:
    - eas/checkout
    - eas/install_node_modules
    - eas/prebuild
    - eas/configure_eas_update
    - eas/inject_android_credentials
    - eas/configure_android_version:
        inputs:
          version_code: '123'
          version_name: '1.0.0'

```

| Property | Type | Description |
| --- | --- | --- |
| `name` | - | The name of the step in the reusable function that shows in the build logs. Defaults to `Configure Android version`. |
| `inputs.version_code` | `string` | Optional input defining `versionCode` of your Android build. Defaults to `${ eas.job.version.versionCode }` |
| `inputs.version_name` | `string` | Optional input defining `versionName` of your Android build. Defaults to `${ eas.job.version.versionName }`. |

[eas/configure\_android\_version source code

View the source code for the eas/configure\_android\_version function on GitHub.](https://github.com/expo/eas-build/blob/main/packages/build-tools/src/steps/functions/configureAndroidVersion.ts)

#### `eas/configure_ios_version`

> This function is only available for iOS builds.

Configures the version of your iOS app. It's used to set a version when using [remote app version management](/build-reference/app-versions).

It's not mandatory to use this function, if it's not used the version from native code generated during the prebuild phase will be used.

example.yml

Copy

```
build:
  name: Configure iOS version
  steps:
    - eas/checkout
    - eas/install_node_modules
    - eas/resolve_apple_team_id_from_credentials:
        id: resolve_apple_team_id_from_credentials
    - eas/prebuild:
        inputs:
          clean: false
          apple_team_id: ${ steps.resolve_apple_team_id_from_credentials.apple_team_id }
    - eas/configure_eas_update
    - eas/configure_ios_credentials
    - eas/configure_ios_version

```

example.yml

Copy

```
build:
  name: Configure iOS version
  steps:
    - eas/checkout
    - eas/install_node_modules
    - eas/resolve_apple_team_id_from_credentials:
        id: resolve_apple_team_id_from_credentials
    - eas/prebuild:
        inputs:
          clean: false
          apple_team_id: ${ steps.resolve_apple_team_id_from_credentials.apple_team_id }
    - eas/configure_eas_update
    - eas/configure_ios_credentials
    - eas/configure_ios_version:
        inputs:
          build_number: '123'
          app_version: '1.0.0'

```

| Property | Type | Description |
| --- | --- | --- |
| `name` | - | The name of the step in the reusable function that shows in the build logs. Defaults to `Configure iOS version`. |
| `inputs.build_number` | `string` | Optional input defining the build number (`CFBundleVersion`) of your iOS build. Defaults to `${ eas.job.version.buildNumber }` |
| `inputs.app_version` | `string` | Optional input defining the app version (`CFBundleShortVersionString`) of your iOS build. Defaults to `${ eas.job.version.appVersion }`. |
| `inputs.build_configuration` | `string` | Optional input defining the Xcode project's Build Configuration. Defaults to `${ eas.job.buildConfiguration }` or if not specified is resolved to `Debug` for development client or `Release` for other builds. |
| `inputs.credentials` | `json` | Optional input defining the app credentials for your iOS build. Defaults to `${ eas.job.secrets.buildCredentials }`. Needs to comply to `${ eas.job.secrets.buildCredentials }` schema for iOS. |

[eas/configure\_ios\_version source code

View the source code for the eas/configure\_ios\_version function on GitHub.](https://github.com/expo/eas-build/blob/main/packages/build-tools/src/steps/functions/configureIosVersion.ts)

#### `eas/run_gradle`

> This function is only available for Android builds.

Runs a Gradle command to build an Android app.

example.yml

Copy

```
build:
  name: Build Android app
  steps:
    - eas/checkout
    - eas/install_node_modules
    - eas/prebuild
    - eas/configure_eas_update
    - eas/inject_android_credentials
    - eas/run_gradle

```

example.yml

Copy

```
build:
  name: Build Android app
  steps:
    - eas/checkout
    - eas/install_node_modules
    - eas/prebuild
    - eas/configure_eas_update
    - eas/inject_android_credentials
    - eas/run_gradle:
        inputs:
          command: :app:bundleRelease

```

| Property | Type | Description |
| --- | --- | --- |
| `name` | - | The name of the step in the reusable function that shows in the build logs. Defaults to `Run gradle`. |
| `inputs.command` | `string` | Optional input defining the Gradle command to run to build the Android app. If not specified it is resolved based on the build configuration and contents of the `${ eas.job }` object. |

[eas/run\_gradle source code

View the source code for the eas/run\_gradle function on GitHub.](https://github.com/expo/eas-build/blob/main/packages/build-tools/src/steps/functions/runGradle.ts)

#### `eas/generate_gymfile_from_template`

> This function is only available for iOS builds.

Generates a [`Gymfile`](https://docs.fastlane.tools/actions/gym/#gymfile) used to build the iOS app using Fastlane from a template.

Default template used when credentials are passed:

Gymfile

Copy

```
suppress_xcode_output(true)
clean(<%- CLEAN %>)

scheme("<%- SCHEME %>")
<% if (BUILD_CONFIGURATION) { %>
configuration("<%- BUILD_CONFIGURATION %>")
<% } %>

export_options({
method: "<%- EXPORT_METHOD %>",
provisioningProfiles: {<% _.forEach(PROFILES, function(profile) { %>
    "<%- profile.BUNDLE_ID %>" => "<%- profile.UUID %>",<% }); %>
}<% if (ICLOUD_CONTAINER_ENVIRONMENT) { %>,
iCloudContainerEnvironment: "<%- ICLOUD_CONTAINER_ENVIRONMENT %>"
<% } %>
})

export_xcargs "OTHER_CODE_SIGN_FLAGS=\\"--keychain <%- KEYCHAIN_PATH %>\\""

disable_xcpretty(true)
buildlog_path("<%- LOGS_DIRECTORY %>")

output_directory("<%- OUTPUT_DIRECTORY %>")

```

Default template used when credentials are not passed (simulator build):

Gymfile

Copy

```
suppress_xcode_output(true)
clean(<%- CLEAN %>)

scheme("<%- SCHEME %>")
<% if (BUILD_CONFIGURATION) { %>
configuration("<%- BUILD_CONFIGURATION %>")
<% } %>

derived_data_path("<%- DERIVED_DATA_PATH %>")
skip_package_ipa(true)
skip_archive(true)
destination("<%- SCHEME_SIMULATOR_DESTINATION %>")

disable_xcpretty(true)
buildlog_path("<%- LOGS_DIRECTORY %>")

```

`CLEAN`, `SCHEME`, `BUILD_CONFIGURATION`, `EXPORT_METHOD`, `PROFILES`, `ICLOUD_CONTAINER_ENVIRONMENT`, `KEYCHAIN_PATH`, `LOGS_DIRECTORY`, `OUTPUT_DIRECTORY`, `DERIVED_DATA_PATH`and `SCHEME_SIMULATOR_DESTINATION` values are provided to the template based on the inputs and default internal configuration of EAS Build.

example.yml

Copy

```
build:
  name: Generate Gymfile template
  steps:
    - eas/checkout
    - eas/install_node_modules
    - eas/resolve_apple_team_id_from_credentials:
        id: resolve_apple_team_id_from_credentials
    - eas/prebuild:
        inputs:
          clean: false
          apple_team_id: ${ steps.resolve_apple_team_id_from_credentials.apple_team_id }
    - eas/configure_eas_update
    - eas/configure_ios_credentials
    - eas/generate_gymfile_from_template:
        inputs:
          credentials: ${ eas.job.secrets.buildCredentials }

```

example.yml

Copy

```
build:
  name: Generate Gymfile template
  steps:
    - eas/checkout
    - eas/install_node_modules
    - eas/prebuild
    - eas/generate_gymfile_from_template

```

However, you can also use other custom properties in the template, by specifying your custom template in `inputs.template` and providing the values for the custom properties in the `inputs.extra` object.

example.yml

Copy

```
build:
  name: Generate Gymfile template
  steps:
    - eas/checkout
    - eas/install_node_modules
    - eas/resolve_apple_team_id_from_credentials:
        id: resolve_apple_team_id_from_credentials
    - eas/prebuild:
        inputs:
          clean: false
          apple_team_id: ${ steps.resolve_apple_team_id_from_credentials.apple_team_id }
    - eas/configure_eas_update
    - eas/configure_ios_credentials
    - eas/generate_gymfile_from_template:
        inputs:
          credentials: ${ eas.job.secrets.buildCredentials }
          extra:
            MY_VALUE: my value
          template: |
            suppress_xcode_output(true)
            clean(<%- CLEAN %>)

            scheme("<%- SCHEME %>")
            <% if (BUILD_CONFIGURATION) { %>
            configuration("<%- BUILD_CONFIGURATION %>")
            <% } %>

            export_options({
            method: "<%- EXPORT_METHOD %>",
            provisioningProfiles: {<% _.forEach(PROFILES, function(profile) { %>
                "<%- profile.BUNDLE_ID %>" => "<%- profile.UUID %>",<% }); %>
            }<% if (ICLOUD_CONTAINER_ENVIRONMENT) { %>,
            iCloudContainerEnvironment: "<%- ICLOUD_CONTAINER_ENVIRONMENT %>"
            <% } %>
            })

            export_xcargs "OTHER_CODE_SIGN_FLAGS=\"--keychain <%- KEYCHAIN_PATH %>\""

            disable_xcpretty(true)
            buildlog_path("<%- LOGS_DIRECTORY %>")

            output_directory("<%- OUTPUT_DIRECTORY %>")

            sth_else("<%- MY_VALUE %>")

```

| Property | Type | Description |
| --- | --- | --- |
| `name` | - | The name of the step in the reusable function that shows in the build logs. Defaults to `Generate Gymfile from template`. |
| `inputs.template` | `string` | Optional input defining the Gymfile template which should be used. If not specified one out of two default templates will be used depending on whether the `inputs.credentials` value is specified. |
| `inputs.credentials` | `json` | Optional input defining the app credentials for your iOS build. If specified `KEYCHAIN_PATH`, `EXPORT_METHOD`, and `PROFILES` values will be provided to the template. |
| `inputs.build_configuration` | `string` | Optional input defining the Xcode project's Build Configuration. Defaults to `${ eas.job.buildConfiguration }` or if not specified is resolved to `Debug` for development client or `Release` for other builds. Corresponds to the `BUILD_CONFIGURATION` template value. |
| `inputs.scheme` | `string` | Optional input defining the Xcode project's scheme which should be used for the build. Defaults to `${ eas.job.scheme }` or if not specified is resolved to the first scheme found in the Xcode project. Corresponds to the `SCHEME` template value. |
| `inputs.clean` | `boolean` | Optional input defining whether the Xcode project should be cleaned before the build. Defaults to `true`. Corresponds to `CLEAN` template variable. |
| `inputs.extra` | `json` | Optional input defining extra values which should be provided to the template. |

[eas/generate\_gymfile\_from\_template source code

View the source code for the eas/generate\_gymfile\_from\_template function on GitHub.](https://github.com/expo/eas-build/blob/main/packages/build-tools/src/steps/functions/generateGymfileFromTemplate.ts)

#### `eas/run_fastlane`

> This function is only available for iOS builds.

Runs [`fastlane gym`](https://docs.fastlane.tools/actions/gym/#gym) command against the [`Gymfile`](https://docs.fastlane.tools/actions/gym/#gymfile) located in the `ios` project directory to build the iOS app.

example.yml

Copy

```
build:
  name: Build iOS app
  steps:
    - eas/checkout
    - eas/install_node_modules
    - eas/resolve_apple_team_id_from_credentials:
        id: resolve_apple_team_id_from_credentials
    - eas/prebuild:
        inputs:
          clean: false
          apple_team_id: ${ steps.resolve_apple_team_id_from_credentials.apple_team_id }
    - eas/configure_eas_update
    - eas/configure_ios_credentials
    - eas/generate_gymfile_from_template:
        inputs:
          credentials: ${ eas.job.secrets.buildCredentials }
    - eas/run_fastlane

```

example.yml

Copy

```
build:
  name: Build iOS app
  steps:
    - eas/checkout
    - eas/install_node_modules
    - eas/prebuild
    - eas/configure_eas_update
    - eas/generate_gymfile_from_template
    - eas/run_fastlane

```

[eas/run\_fastlane source code

View the source code for the eas/run\_fastlane function on GitHub.](https://github.com/expo/eas-build/blob/main/packages/build-tools/src/steps/functions/runFastlane.ts)

#### `eas/find_and_upload_build_artifacts`

> You can currently upload each artifact type only once per build job.  
> If you use [`eas/find_and_upload_build_artifacts`](/custom-builds/schema#easfind_and_upload_build_artifacts) while having [`buildArtifactPaths`](/eas/json#buildartifactpaths) configured in your build profile and the step finds and uploads some build artifacts, any following `eas/upload_artifact` step will fail.  
> To solve this, for now, we recommend removing `buildArtifactPaths` from custom build's profiles and uploading artifacts manually with `eas/upload_artifact` in the YAML if you need to call it there.

Automatically finds and uploads application archive, additional build artifacts, and Xcode logs from the default locations and using the [`buildArtifactPaths`](/eas/json#buildartifactpaths) configuration. Uploads found artifacts to the EAS servers.

example.yml

Copy

```
build:
  name: Build iOS app
  steps:
    - eas/checkout
    - eas/install_node_modules
    - eas/resolve_apple_team_id_from_credentials:
        id: resolve_apple_team_id_from_credentials
    - eas/prebuild:
        inputs:
          clean: false
          apple_team_id: ${ steps.resolve_apple_team_id_from_credentials.apple_team_id }
    - eas/configure_eas_update
    - eas/configure_ios_credentials
    - eas/generate_gymfile_from_template:
        inputs:
          credentials: ${ eas.job.secrets.buildCredentials }
    - eas/run_fastlane
    - eas/find_and_upload_build_artifacts

```

example.yml

Copy

```
build:
  name: Build iOS app
  steps:
    - eas/checkout
    - eas/install_node_modules
    - eas/prebuild
    - eas/configure_eas_update
    - eas/generate_gymfile_from_template
    - eas/run_fastlane
    - eas/find_and_upload_build_artifacts

```

example.yml

Copy

```
build:
  name: Build Android app
  steps:
    - eas/checkout
    - eas/install_node_modules
    - eas/prebuild
    - eas/configure_eas_update
    - eas/inject_android_credentials
    - eas/run_gradle
    - eas/find_and_upload_build_artifacts

```

[eas/find\_and\_upload\_build\_artifacts source code

View the source code for the eas/find\_and\_upload\_build\_artifacts function on GitHub.](https://github.com/expo/eas-build/blob/main/packages/build-tools/src/steps/functions/findAndUploadBuildArtifacts.ts)

#### `eas/upload_artifact`

Uploads build artifacts from provided paths.

> You can currently upload each artifact type only once per build job.  
> If you use [`eas/find_and_upload_build_artifacts`](/custom-builds/schema#easfind_and_upload_build_artifacts) while having [`buildArtifactPaths`](/eas/json#buildartifactpaths) configured in your build profile and the step finds and uploads some build artifacts, any following `eas/upload_artifact` step will fail.  
> To solve this, for now, we recommend removing `buildArtifactPaths` from custom build's profiles and uploading artifacts manually with `eas/upload_artifact` in the YAML if you need to call it there.

For example, a build config with the following `steps` will upload an artifact to the EAS servers:

upload.yml

Copy

```
build:
  name: Upload artifacts
  steps:
    - eas/checkout
    # - ...
    - eas/upload_artifact:
        name: Upload application archive
        inputs:
          path: fixtures/app-debug.apk
    - eas/upload_artifact:
        name: Upload artifacts
        inputs:
          type: build-artifact
          path: |
            assets/*.jpg
            assets/*.png

```

| Input | Type | Description |
| --- | --- | --- |
| `path` | `string` | Required. Path or newline-delimited list of paths to the artifacts to upload to EAS servers. You can use `*` wildcard and other [glob patterns that `fast-glob` supports](https://github.com/mrmlnc/fast-glob#pattern-syntax). |
| `type` | `string` | The type of artifact that is uploaded to the EAS servers. Allowed values are `application-archive` and `build-artifact`. Defaults to `application-archive`. |

[eas/upload\_artifact source code

View the source code for the eas/upload\_artifact function on GitHub.](https://github.com/expo/eas-build/blob/main/packages/build-tools/src/steps/functions/uploadArtifact.ts)

#### `eas/install_maestro`

Makes sure [Maestro](https://maestro.mobile.dev), the mobile UI testing framework, is installed along with all its dependencies.

build-and-test.yml

Copy

```
build:
  name: Build and test
  steps:
    - eas/build
    # ... simulator/emulator setup
    - eas/install_maestro:
        inputs:
          maestro_version: 1.35.0
    - run:
        command: maestro test flows/signin.yml
    - eas/upload_artifact:
        name: Upload Maestro artifacts
        inputs:
          type: build-artifact
          path: ${ eas.env.HOME }/.maestro/tests

```

| Input | Type | Description |
| --- | --- | --- |
| `maestro_version` | `string` | Maestro version to install (for example, 1.35.0). If not provided, `install_maestro` will install the latest version. |

[eas/install\_maestro source code

View the source code for the eas/install\_maestro function on GitHub.](https://github.com/expo/eas-build/blob/main/packages/build-tools/src/steps/functions/installMaestro.ts)

#### `eas/start_android_emulator`

Starts an Android Emulator you can use to test your apps on. Only available when running a build for Android.

> Your project must be configured to use the old Build Infrastructure to start Android Emulator. Go to [Project settings](https://expo.dev/accounts/%5Baccount%5D/projects/%5Bproject%5D/settings) to configure. See [this changelog post](https://expo.dev/changelog/2024/08-29-c3d-default) for more information.

build-and-test.yml

Copy

```
build:
  name: Build and test
  steps:
    - eas/build
    - eas/start_android_emulator:
        inputs:
          system_image_package: system-images;android-30;default;x86_64
    # ... Maestro setup and tests

```

| Input | Type | Description |
| --- | --- | --- |
| `device_name` | `string` | Name for the created device. You can customize it if starting multiple emulators. |
| `system_image_package` | `string` | Android package path to use for the emulator. For example, `system-images;android-30;default;x86_64`. To get a list of available system images, run [`sdkmanager --list`](https://developer.android.com/tools/sdkmanager#list) on a local computer. VMs run on x86\_64 architecture, so always choose `x86_64` package variants. The [`sdkmanager` tool](https://developer.android.com/tools/sdkmanager) comes from Android SDK command-line tools. |

[eas/start\_android\_emulator source code

View the source code for the eas/start\_android\_emulator function on GitHub.](https://github.com/expo/eas-build/blob/main/packages/build-tools/src/steps/functions/startAndroidEmulator.ts)

#### `eas/start_ios_simulator`

Starts an iOS Simulator you can use to test your apps on. Only available when running a build for iOS.

build-and-test.yml

Copy

```
build:
  name: Build and test
  steps:
    - eas/build
    - eas/start_ios_simulator
    # ... Maestro setup and tests

```

| Input | Type | Description |
| --- | --- | --- |
| `device_identifier` | `string` | Name or UDID of the Simulator you want to start. Examples include `iPhone [XY] Pro`, `AEF997BB-222C-4379-89BA-D21070B1D787`. Note: Available Simulators are different for every image. If you change the image, the Simulator for a given name may become unavailable. For instance, an Xcode 14 image will have iPhone 14 Simulators, while an Xcode 15 image will have iPhone 15 simulators. In general, we encourage not providing this input. See [runner images](/build/eas-json#selecting-a-base-image) for more information. |

[eas/start\_ios\_simulator source code

View the source code for the eas/start\_ios\_simulator function on GitHub.](https://github.com/expo/eas-build/blob/main/packages/build-tools/src/steps/functions/startIosSimulator.ts)

#### `eas/send_slack_message`

Sends a specified message to a configured [Slack webhook URL](https://api.slack.com/messaging/webhooks), which then posts it in the related Slack channel.
The message can be specified as plain text or as a [Slack Block Kit](https://api.slack.com/block-kit) message.
With both cases, you can reference build job properties and [use other steps outputs](/custom-builds/schema#use-output-from-one-step-to-another) in the message for dynamic evaluation.
For example, `'Build URL: ${ eas.job.expoBuildUrl }'`, `Build finished with status: ${ steps.run_fastlane.status_text }`, `Build failed with error: ${ steps.run_gradle.error_text }`.
Either "message" or "payload" has to be specified, but not both.

send-slack-message.yml

Copy

```
build:
  name: Slack your team from custom build
  steps:
    - eas/send_slack_message:
        name: Send Slack message to a given webhook URL
        inputs:
          message: 'This is a message to plain input URL'
          slack_hook_url: 'https://hooks.slack.com/services/[rest_of_hook_url]'
    - eas/send_slack_message:
        name: Send Slack message to a default webhook URL from SLACK_HOOK_URL secret
        inputs:
          message: 'This is a test message to default URL from SLACK_HOOK_URL secret'
    - eas/send_slack_message:
        name: Send Slack message to a webhook URL from specified secret
        inputs:
          message: 'This is a test message to a URL from specified secret'
          slack_hook_url: ${ eas.env.ANOTHER_SLACK_HOOK_URL }

    - eas/build
    - eas/send_slack_message:
        if: ${ always() }
        name: Send Slack message when the build finishes (Android)
        inputs:
          message: |
            This is a test message when Android build finishes
            Status: `${ steps.run_gradle.status_text }`
            Link: `${ eas.job.expoBuildUrl }`
    - eas/send_slack_message:
        if: ${ always() }
        name: Send Slack message when the build finishes (iOS)
        inputs:
          message: |
            This is a test message when iOS build finishes
            Status: `${ steps.run_fastlane.status_text }`
            Link: `${ eas.job.expoBuildUrl }`
    - eas/send_slack_message:
        if: ${ failure() }
        name: Send Slack message when the build fails (Android)
        inputs:
          message: |
            This is a test message when Android build fails
            Error: `${ steps.run_gradle.error_text }`
    - eas/send_slack_message:
        if: ${ failure() }
        name: Send Slack message when the build fails (iOS)
        inputs:
          message: |
            This is a test message when iOS build fails
            Error: `${ steps.run_fastlane.error_text }`
    - eas/send_slack_message:
        if: ${ success() }
        name: Send Slack message when the build succeeds
        inputs:
          message: |
            This is a test message when build succeeds
    - eas/send_slack_message:
        if: ${ always() }
        name: Send Slack message with Slack Block Kit layout
        inputs:
          payload:
            blocks:
              - type: section
                text:
                  type: mrkdwn
                  text: |-
                    Hello, Sir Developer

                     *Your build has finished!*
              - type: divider
              - type: section
                text:
                  type: mrkdwn
                  text: |-
                    *${ eas.env.EAS_BUILD_ID }*
                    *Status:* `${ steps.run_gradle.status_text }`
                    *Link:* `${ eas.job.expoBuildUrl }`
                accessory:
                  type: image
                  image_url: [your_image_url]
                  alt_text: alt text for image
              - type: divider
              - type: actions
                elements:
                  - type: button
                    text:
                      type: plain_text
                      text: 'Do a thing :rocket:'
                      emoji: true
                    value: a_thing
                  - type: button
                    text:
                      type: plain_text
                      text: 'Do another thing :x:'
                      emoji: true
                    value: another_thing

```

| Input | Type | Description |
| --- | --- | --- |
| `message` | `string` | The text of the message you want to send. For example, `'This is the content of the message'`.   Note: Either `message` or `payload` needs to be provided, but not both. |
| `payload` | `string` | The contents of the message you want to send defined using [Slack Block Kit](https://api.slack.com/block-kit) layout.   Note: Either `message` or `payload` needs to be provided, but not both. |
| `slack_hook_url` | `string` | The URL of the previously configured Slack webhook URL, which will post your message to the specified channel. You can provide the plain URL like `slack_hook_url: 'https://hooks.slack.com/services/[rest_of_hook_url]'`, use EAS secrets like `slack_hook_url: ${ eas.env.ANOTHER_SLACK_HOOK_URL }`, or set the `SLACK_HOOK_URL` secret, which will serve as a default webhook URL (in this last case, there is no need to provide `slack_hook_url` input). |

[eas/send\_slack\_message source code

View the source code for the eas/send\_slack\_message function on GitHub.](https://github.com/expo/eas-build/blob/main/packages/build-tools/src/steps/functions/sendSlackMessage.ts)

### Using built-in EAS functions to build an app

Using the built-in EAS functions you can recreate the default EAS Build process for different build types.

For example, to trigger a build that creates internal distribution build for Android and a simulator build for iOS you can use the following configuration:

eas.json

Copy

```
{
  %%placeholder-start%%... %%placeholder-end%%
  "build": {
    %%placeholder-start%%... %%placeholder-end%%
    "developmentBuild": {
      "distribution": "internal",
      "android": {
        "config": "development-build-android.yml"
      },
      "ios": {
        "simulator": true,
        "config": "development-build-ios.yml"
      }
    }
    %%placeholder-start%%... %%placeholder-end%%
  }
  %%placeholder-start%%... %%placeholder-end%%
}

```

.eas/build/development-build-android.yml

Copy

```
build:
  name: Simple internal distribution Android build
  steps:
    - eas/checkout

    - eas/install_node_modules

    - eas/prebuild

    - eas/inject_android_credentials

    - eas/run_gradle

    - eas/find_and_upload_build_artifacts

```

.eas/build/development-build-ios.yml

Copy

```
build:
  name: Simple simulator iOS build
  steps:
    - eas/checkout

    - eas/install_node_modules

    - eas/prebuild

    - run:
        name: Install pods
        working_directory: ./ios
        command: pod install

    - eas/generate_gymfile_from_template

    - eas/run_fastlane

    - eas/find_and_upload_build_artifacts

```

To create a Google Play Store build for Android and an Apple App Store build for iOS you can use the following configuration:

eas.json

Copy

```
{
  %%placeholder-start%%... %%placeholder-end%%
  "build": {
    %%placeholder-start%%... %%placeholder-end%%
    "productionBuild": {
      "android": {
        "config": "production-build-android.yml"
      },
      "ios": {
        "config": "production-build-ios.yml"
      }
    }
    %%placeholder-start%%... %%placeholder-end%%
  }
  %%placeholder-start%%... %%placeholder-end%%
}

```

.eas/build/production-build-android.yml

Copy

```
build:
  name: Customized Android Play Store build example
  steps:
    - eas/checkout

    - eas/install_node_modules

    - eas/prebuild

    - eas/inject_android_credentials

    - eas/run_gradle

    - eas/find_and_upload_build_artifacts

```

.eas/build/production-build-ios.yml

Copy

```
build:
  name: Customized iOS App Store build example
  steps:
    - eas/checkout

    - eas/install_node_modules

    - eas/resolve_apple_team_id_from_credentials:
        id: resolve_apple_team_id_from_credentials

    - eas/prebuild:
        inputs:
          apple_team_id: ${ steps.resolve_apple_team_id_from_credentials.apple_team_id }

    - run:
        name: Install pods
        working_directory: ./ios
        command: pod install

    - eas/configure_ios_credentials

    - eas/generate_gymfile_from_template:
        inputs:
          credentials: ${ eas.job.secrets.buildCredentials }

    - eas/run_fastlane

    - eas/find_and_upload_build_artifacts

```

Check out the example repository for more detailed examples:

[Custom build example repository

A custom EAS Build example that includes examples for custom builds such as setting up functions, using environment variables, uploading artifacts, and more.](https://github.com/expo/eas-custom-builds-example/tree/main)

### Use a reusable function in a `build`

For example, a custom build config with the following reusable function contains a single command to print a message that is echoed.

```
functions:
  greetings:
    - name: name
      default_value: Hello world
    inputs: [value]
    command: echo "${ inputs.name }, { inputs.value }"

```

The above function can be used in a `build` as follows:

```
build:
  name: Functions Demo
  steps:
    - greetings:
        inputs:
          value: Expo

```

> Tip: `build.steps` can execute multiple reusable `functions` sequentially.

Override values in a `build`
----------------------------

You can override values for the following properties:

* `working_directory`
* `name`
* `shell`

For example, a reusable function called `list_files`:

```
functions:
  list_files:
    name: List files
    command: ls -la

```

When `list_files` is called in a build config, it lists all files in the root directory of a project:

```
build:
  name: List files
  steps:
    - eas/checkout
    - list_files

```

You can use the `working_directory` property to override the behavior in the function call to list the files in a different directory by specifying the path to that directory:

```
build:
  name: List files
    steps:
      - eas/checkout
      - list_files:
          working_directory: /a/b/c

```

[Previous (EAS Build - Custom builds)

Get started](/custom-builds/get-started)[Next (EAS Build - Custom builds)

TypeScript functions](/custom-builds/functions)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/custom-builds/schema.mdx)
* Last updated on February 18, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[YAML syntax for custom builds](/custom-builds/schema/#yaml-syntax-for-custom-builds)[build](/custom-builds/schema/#build)[name](/custom-builds/schema/#name)[steps](/custom-builds/schema/#steps)[steps[].run](/custom-builds/schema/#stepsrun)[Use a single step](/custom-builds/schema/#use-a-single-step)[Use multiple steps](/custom-builds/schema/#use-multiple-steps)[Sharing environment variables with other steps](/custom-builds/schema/#sharing-environment-variables-with-other-steps)[steps[].run.name](/custom-builds/schema/#stepsrunname)[steps[].run.command](/custom-builds/schema/#stepsruncommand)[steps[].run.working\_directory](/custom-builds/schema/#stepsrunworking_directory)[steps[].run.shell](/custom-builds/schema/#stepsrunshell)[steps[].run.inputs](/custom-builds/schema/#stepsruninputs)[steps[].run.outputs](/custom-builds/schema/#stepsrunoutputs)[steps[].run.outputs.required](/custom-builds/schema/#stepsrunoutputsrequired)[steps[].run.id](/custom-builds/schema/#stepsrunid)[Call the same function one or more times](/custom-builds/schema/#call-the-same-function-one-or-more-times)[Use output from one step to another](/custom-builds/schema/#use-output-from-one-step-to-another)[functions](/custom-builds/schema/#functions)[functions.[function\_name]](/custom-builds/schema/#functionsfunction_name)[functions.[function\_name].name](/custom-builds/schema/#functionsfunction_namename)[functions.[function\_name].inputs](/custom-builds/schema/#functionsfunction_nameinputs)[inputs[].name](/custom-builds/schema/#inputsname)[inputs[].required](/custom-builds/schema/#inputsrequired)[inputs[].type](/custom-builds/schema/#inputstype)[inputs[].default\_value](/custom-builds/schema/#inputsdefault_value)[inputs[].allowed\_values](/custom-builds/schema/#inputsallowed_values)[Multiple input values](/custom-builds/schema/#multiple-input-values)[functions.[function\_name].outputs](/custom-builds/schema/#functionsfunction_nameoutputs)[outputs[].name](/custom-builds/schema/#outputsname)[outputs[].required](/custom-builds/schema/#outputsrequired)[functions.[function\_name].command](/custom-builds/schema/#functionsfunction_namecommand)[functions.[function\_name].path](/custom-builds/schema/#functionsfunction_namepath)[functions.[function\_name].shell](/custom-builds/schema/#functionsfunction_nameshell)[functions.[function\_name].supported\_platforms](/custom-builds/schema/#functionsfunction_namesupported_platforms)[import](/custom-builds/schema/#import)[Functions](/custom-builds/schema/#functions-1)[Built-in EAS functions](/custom-builds/schema/#built-in-eas-functions)[eas/build](/custom-builds/schema/#easbuild)[Android](/custom-builds/schema/#android)[iOS](/custom-builds/schema/#ios)[Known limitations](/custom-builds/schema/#known-limitations)[eas/maestro\_test](/custom-builds/schema/#easmaestro_test)[eas/checkout](/custom-builds/schema/#eascheckout)[eas/use\_npm\_token](/custom-builds/schema/#easuse_npm_token)[eas/install\_node\_modules](/custom-builds/schema/#easinstall_node_modules)[eas/resolve\_build\_config](/custom-builds/schema/#easresolve_build_config)[eas/get\_credentials\_for\_build\_triggered\_by\_github\_integration](/custom-builds/schema/#easget_credentials_for_build_triggered_by_github_integration)[eas/resolve\_apple\_team\_id\_from\_credentials](/custom-builds/schema/#easresolve_apple_team_id_from_credentials)[eas/prebuild](/custom-builds/schema/#easprebuild)[eas/configure\_eas\_update](/custom-builds/schema/#easconfigure_eas_update)[eas/inject\_android\_credentials](/custom-builds/schema/#easinject_android_credentials)[eas/configure\_ios\_credentials](/custom-builds/schema/#easconfigure_ios_credentials)[eas/configure\_android\_version](/custom-builds/schema/#easconfigure_android_version)[eas/configure\_ios\_version](/custom-builds/schema/#easconfigure_ios_version)[eas/run\_gradle](/custom-builds/schema/#easrun_gradle)[eas/generate\_gymfile\_from\_template](/custom-builds/schema/#easgenerate_gymfile_from_template)[eas/run\_fastlane](/custom-builds/schema/#easrun_fastlane)[eas/find\_and\_upload\_build\_artifacts](/custom-builds/schema/#easfind_and_upload_build_artifacts)[eas/upload\_artifact](/custom-builds/schema/#easupload_artifact)[eas/install\_maestro](/custom-builds/schema/#easinstall_maestro)[eas/start\_android\_emulator](/custom-builds/schema/#easstart_android_emulator)[eas/start\_ios\_simulator](/custom-builds/schema/#easstart_ios_simulator)[eas/send\_slack\_message](/custom-builds/schema/#eassend_slack_message)[Using built-in EAS functions to build an app](/custom-builds/schema/#using-built-in-eas-functions-to-build-an-app)[Use a reusable function in a build](/custom-builds/schema/#use-a-reusable-function-in-a-build)[Override values in a build](/custom-builds/schema/#override-values-in-a-build)