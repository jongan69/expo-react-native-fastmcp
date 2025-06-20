TypeScript functions - Expo Documentation

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

TypeScript functions
====================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/custom-builds/functions.mdx)

Learn how to create and use EAS Build functions in your custom build configurations.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/custom-builds/functions.mdx)

---

EAS Build functions are a great way to extend the functionality of custom builds. You can use them to create reusable steps, and to write your logic in JavaScript, TypeScript, or Bash (more information in [`command` in the config schema](/custom-builds/schema#functionsfunction_namecommand)). This guide provides a walkthrough of creating a function in TypeScript.

1

Initialize an EAS Build function module
---------------------------------------

The easiest way to create an EAS Build function is to use the `create-eas-build-function` CLI tool. By running the following command from the same directory as your eas.json file, you can create a new custom TypeScript function:

Terminal

Copy

`-Â``npx create-eas-build-function@latest ./.eas/build/myFunction`

This creates a new module called `myFunction` in the .eas/build directory. The module will contain a pre-generated module configuration and the src directory with the index.ts file containing the default TypeScript function template.

.eas/build/myFunction/src/index.ts

Copy

```
// This file was autogenerated by `create-eas-build-function` command.
// Go to README.md to learn more about how to write your own custom build functions.

import { BuildStepContext } from '@expo/steps';

// interface FunctionInputs {
//   // specify the type of the inputs value and whether they are required here
//   // example: name: BuildStepInput<BuildStepInputValueTypeName.STRING, true>;
// }

// interface FunctionOutputs {
//   // specify the function outputs and whether they are required here
//   // example: name: BuildStepOutput<true>;
// }

async function myFunction(
  ctx: BuildStepContext
  // {
  //   inputs,
  //   outputs,
  //   env,
  // }: {
  //   inputs: FunctionInputs;
  //   outputs: FunctionOutputs;
  //   env: BuildStepEnv;
  // }
): Promise<void> {
  ctx.logger.info('Hello from my TypeScript function!');
}

export default myFunction;

```

2

Compile the function
--------------------

Functions must be compiled to a single JavaScript file that can be run without installing any dependencies. The default `build` script for generated functions uses [ncc](https://github.com/vercel/ncc) to compile your function into a single file with all its dependencies. If you don't have the `ncc` installed globally on your machine, run `npm install -g @vercel/ncc` to install it. Next, run the build script in the .eas/build/myFunction directory:

Terminal

Copy

`-Â``npm run build`

This command triggers the `build` script placed in the package.json file of your custom function module.

package.json

Copy

```
{
  ...
  "scripts": {
    ...
    "build": "ncc build ./src/index.ts -o build/ --minify --no-cache --no-source-map-register"
    ...
  },
  ...
}

```

The `build` script generates build/index.js. This file must be uploaded to EAS Build as a part of your project archive, so that the builder can run your function. Ensure that the file is not excluded by a .gitignore file or .easignore file.

3

Expose the function to the custom build config
----------------------------------------------

> Note: The following example assumes that you have already set up a custom build workflow and configured it in your eas.json. If not, see [Get started with custom builds](/custom-builds/get-started#create-a-workflow) before proceeding.

Let's assume that you have a config.yml file in the .eas/build directory. It contains the following content:

.eas/build/config.yml

Copy

```
build:
  name: My example config
  steps:
    - eas/checkout
    - eas/install_node_modules
    - run:
        name: Finished
        command: echo Finished

```

To add your function to the config, you need to add the following lines to the config.yml file:

.eas/build/config.yml

Copy

```
build:
  name: My example config
  steps:
    - eas/checkout
    - eas/install_node_modules
    - run:
        name: Finished
        command: echo Finished

functions:
  my_function:
    name: My function
    path: ./myFunction

```

The `path` property should be a relative path from the config file to your function directory. In this case, it's just `./myFunction`.

Now, add a call to the `my_function` function in the config.yml file:

.eas/build/config.yml

Copy

```
build:
  name: My example config
  steps:
    - eas/checkout
    - eas/install_node_modules
    - my_function
    - run:
        name: Finished
        command: echo Finished

functions:
  my_function:
    name: My function
    path: ./myFunction

```

![Example of a custom build config using a JavaScript/TypeScript function.](/static/images/eas-build/custom-build-function.png)

4

Working on the function
-----------------------

For a more advanced example, let's say you want to make a function calculate the sum of two numbers and print the result to the console, and then output that value from the function. To do this, modify the config.yml and index.ts files to make the function accept two inputs called `num1` and `num2` and return their sum as an output called `sum`.

.eas/build/config.yml

Copy

```
build:
  name: My example config
  steps:
    - eas/checkout
    - eas/install_node_modules
    - my_function:
        inputs:
          num1: 1
          num2: 2
        id: sum_function
    - run:
        name: Print the sum
        inputs:
          sum: ${ steps.sum_function.sum }
        command: echo ${ inputs.sum }
    - run:
        name: Finished
        command: echo Finished

functions:
  my_function:
    name: My function
    inputs:
      - name: num1
        type: number
      - name: num2
        type: number
    outputs:
      - name: sum
    path: ./myFunction

```

.eas/build/myFunction/src/index.ts

Copy

```
// This file was autogenerated by `create-eas-build-function` command.
// Go to README.md to learn more about how to write your own custom build functions.

import {
  BuildStepContext,
  BuildStepInput,
  BuildStepInputValueTypeName,
  BuildStepOutput,
} from '@expo/steps';

interface FunctionInputs {
  // first template argument is the type of the input value, second template argument is a boolean indicating if the input is required
  num1: BuildStepInput<BuildStepInputValueTypeName.NUMBER, true>;
  num2: BuildStepInput<BuildStepInputValueTypeName.NUMBER, true>;
}

interface FunctionOutputs {
  // template argument is a boolean indicating if the output is required
  sum: BuildStepOutput<true>;
}

async function myFunction(
  ctx: BuildStepContext,
  {
    inputs,
    outputs,
  }: // env,
  {
    inputs: FunctionInputs;
    outputs: FunctionOutputs;
    // env: BuildStepEnv;
  }
): Promise<void> {
  ctx.logger.info(`num1: ${inputs.num1.value}`);
  ctx.logger.info(`num2: ${inputs.num2.value}`);

  const sum = inputs.num1.value + inputs.num2.value;

  ctx.logger.info(`sum: ${sum}`);

  outputs.sum.set(sum.toString()); // Currently, outputs must be strings. This will improve in the future.
}

export default myFunction;

```

![Example of a custom build config using custom JavaScript/TypeScript function.](/static/images/eas-build/custom-build-function-advanced.png)
> Remember to compile your function each time you make changes to it: `npm run build`.

Summary
-------

* Writing functions is a great way to extend the functionality of custom builds with your own logic.
* EAS Build functions are reusable â you can use them in multiple custom build configurations.
* Using EAS Build functions is a great option for more advanced use cases that are not easy to do by writing shell scripts.
* Most of the [built-in functions](/custom-builds/schema#built-in-eas-functions) are open-source and can be forked or used as a reference for writing your own functions.

Check out the example repository for more detailed examples:

[Custom build example repository

A custom EAS Build example that includes examples for custom builds such as setting up functions, using environment variables, uploading artifacts, and more.](https://github.com/expo/eas-custom-builds-example/tree/main)

[Previous (EAS Build - Custom builds)

Config schema](/custom-builds/schema)[Next (EAS Build - Reference)

Build lifecycle hooks](/build-reference/npm-hooks)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/custom-builds/functions.mdx)
* Last updated on February 05, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Initialize an EAS Build function module](/custom-builds/functions/#initialize-an-eas-build-function-module)[Compile the function](/custom-builds/functions/#compile-the-function)[Expose the function to the custom build config](/custom-builds/functions/#expose-the-function-to-the-custom-build-config)[Working on the function](/custom-builds/functions/#working-on-the-function)[Summary](/custom-builds/functions/#summary)