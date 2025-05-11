Using TypeScript · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/typescript)

* [Next](/docs/next/typescript)* [0.79](/docs/typescript)* [0.78](/docs/0.78/typescript)* [0.77](/docs/0.77/typescript)* [0.76](/docs/0.76/typescript)* [0.75](/docs/0.75/typescript)* [0.74](/docs/0.74/typescript)* [0.73](/docs/0.73/typescript)* [0.72](/docs/0.72/typescript)* [0.71](/docs/0.71/typescript)* [0.70](/docs/0.70/typescript)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [The Basics](/docs/getting-started)

  * [Environment setup](/docs/environment-setup)

    * [Workflow](/docs/running-on-device)

      + [Running On Device](/docs/running-on-device)+ [Fast Refresh](/docs/fast-refresh)+ [Metro](/docs/metro)+ [Using Libraries](/docs/libraries)+ [Using TypeScript](/docs/typescript)+ [Upgrading to new versions](/docs/upgrading)* [UI & Interaction](/docs/style)

        * [Debugging](/docs/debugging)

          * [Testing](/docs/testing-overview)

            * [Performance](/docs/performance)

              * [JavaScript Runtime](/docs/javascript-environment)

                * [Codegen](/docs/the-new-architecture/what-is-codegen)

                  * [Native Development](/docs/native-platform)

                    * [Android and iOS guides](/docs/headless-js-android)

                      * [Legacy Architecture](/docs/legacy/native-modules-intro)

On this page

Using TypeScript
================

[TypeScript](https://www.typescriptlang.org/) is a language which extends JavaScript by adding type definitions. New React Native projects target TypeScript by default, but also support JavaScript and Flow.

Getting Started with TypeScript[​](#getting-started-with-typescript "Direct link to Getting Started with TypeScript")
---------------------------------------------------------------------------------------------------------------------

New projects created by the [React Native CLI](/docs/getting-started-without-a-framework#step-1-creating-a-new-application) or popular templates like [Ignite](https://github.com/infinitered/ignite) will use TypeScript by default.

TypeScript may also be used with [Expo](https://expo.io), which maintains TypeScript templates, or will prompt you to automatically install and configure TypeScript when a `.ts` or `.tsx` file is added to your project.

shell

```
npx create-expo-app --template  

```

Adding TypeScript to an Existing Project[​](#adding-typescript-to-an-existing-project "Direct link to Adding TypeScript to an Existing Project")
------------------------------------------------------------------------------------------------------------------------------------------------

1. Add TypeScript, types, and ESLint plugins to your project.

* npm* Yarn

shell

```
npm install -D @tsconfig/react-native @types/jest @types/react @types/react-test-renderer typescript  

```

shell

```
yarn add --dev @tsconfig/react-native @types/jest @types/react @types/react-test-renderer typescript  

```

note

This command adds the latest version of every dependency. The versions may need to be changed to match the existing packages used by your project. You can use a tool like [React Native Upgrade Helper](https://react-native-community.github.io/upgrade-helper/) to see the versions shipped by React Native.

2. Add a TypeScript config file. Create a `tsconfig.json` in the root of your project:

json

```
{  
  "extends": "@tsconfig/react-native/tsconfig.json"  
}  

```

3. Rename a JavaScript file to be `*.tsx`

> You should leave the `./index.js` entrypoint file as it is otherwise you may run into an issue when it comes to bundling a production build.

4. Run `tsc` to type-check your new TypeScript files.

* npm* Yarn

shell

```
npx tsc  

```

shell

```
yarn tsc  

```

Using JavaScript Instead of TypeScript[​](#using-javascript-instead-of-typescript "Direct link to Using JavaScript Instead of TypeScript")
------------------------------------------------------------------------------------------------------------------------------------------

React Native defaults new applications to TypeScript, but JavaScript may still be used. Files with a `.jsx` extension are treated as JavaScript instead of TypeScript, and will not be typechecked. JavaScript modules may still be imported by TypeScript modules, along with the reverse.

How TypeScript and React Native works[​](#how-typescript-and-react-native-works "Direct link to How TypeScript and React Native works")
---------------------------------------------------------------------------------------------------------------------------------------

Out of the box, TypeScript sources are transformed by [Babel](/docs/javascript-environment#javascript-syntax-transformers) during bundling. We recommend that you use the TypeScript compiler only for type checking. This is the default behavior of `tsc` for newly created applications. If you have existing TypeScript code being ported to React Native, there are [one or two caveats](https://babeljs.io/docs/en/next/babel-plugin-transform-typescript) to using Babel instead of TypeScript.

What does React Native + TypeScript look like[​](#what-does-react-native--typescript-look-like "Direct link to What does React Native + TypeScript look like")
--------------------------------------------------------------------------------------------------------------------------------------------------------------

You can provide an interface for a React Component's [Props](/docs/props) and [State](/docs/state) via `React.Component<Props, State>` which will provide type-checking and editor auto-completing when working with that component in JSX.

components/Hello.tsx

```
import React from 'react';  
import {Button, StyleSheet, Text, View} from 'react-native';  
  
export type Props = {  
  name: string;  
  baseEnthusiasmLevel?: number;  
};  
  
const Hello: React.FC<Props> = ({  
  name,  
  baseEnthusiasmLevel = 0,  
}) => {  
  const [enthusiasmLevel, setEnthusiasmLevel] = React.useState(  
    baseEnthusiasmLevel,  
  );  
  
  const onIncrement = () =>  
    setEnthusiasmLevel(enthusiasmLevel + 1);  
  const onDecrement = () =>  
    setEnthusiasmLevel(  
      enthusiasmLevel > 0 ? enthusiasmLevel - 1 : 0,  
    );  
  
  const getExclamationMarks = (numChars: number) =>  
    numChars > 0 ? Array(numChars + 1).join('!') : '';  
  
  return (  
    <View style={styles.container}>  
      <Text style={styles.greeting}>  
        Hello {name}  
        {getExclamationMarks(enthusiasmLevel)}  
      </Text>  
      <View>  
        <Button  
          title="Increase enthusiasm"  
          accessibilityLabel="increment"  
          onPress={onIncrement}  
          color="blue"  
        />  
        <Button  
          title="Decrease enthusiasm"  
          accessibilityLabel="decrement"  
          onPress={onDecrement}  
          color="red"  
        />  
      </View>  
    </View>  
  );  
};  
  
const styles = StyleSheet.create({  
  container: {  
    flex: 1,  
    alignItems: 'center',  
    justifyContent: 'center',  
  },  
  greeting: {  
    fontSize: 20,  
    fontWeight: 'bold',  
    margin: 16,  
  },  
});  
  
export default Hello;  

```

You can explore the syntax more in the [TypeScript playground](https://www.typescriptlang.org/play?strictNullChecks=false&jsx=3#code/JYWwDg9gTgLgBAJQKYEMDG8BmUIjgcilQ3wG4BYAKFEljgG8AhAVxhggDsAaOAZRgCeAGyS8AFkiQweAFSQAPaXABqwJAHcAvnGy4CRdDAC0HFDGAA3JGSpUFteILBI4ABRxgAznAC8DKnBwpiBIAFxwnjBQwBwA5hSUgQBGKJ5IAKIcMGLMnsCpIAAySFZCAPzhHMwgSUhQCZq2lGickXAAEkhCQhDhyIYAdABiAMIAPO4QXgB8vnAAFPRBKCE8KWmZ2bn5nkUlXXMADHCaAJS+s-QBcC0cbQDaSFk5eQXFpTxpMJsvO3ulAF05v0MANcqIYGYkPN1hlnts3vshKcEtdbm1OABJDhoIghLJzebnHyzL4-BG7d5deZPLavSlIuAAajgAEYUWjWvBOAARJC4pD4+B+IkXCJScn0-7U2m-RGlOCzY5lOCyinSoRwIxsuDhQ4cyicu7wWIS+RoIQrMzATgAWRQUAA1t4RVUQCMxA7PJVqrUoMTZm6PV7FXBlXAAIJQKAoATzIOeqDeFnsgYAKwgMXm+AAhPhzuF8DZDYk4EQYMwoBwFtdAmNVBoIoIRD56JFhEhPANbpCYnVNNNa4E4GM5Iomx3W+2RF3YkQpDFYgOh8OOl0evR8ARGqXV4F6MEkDu98P6KbvubLSBrXaHc6afCpVTkce92MAPRjmCD3fD+tqdQfxPOsWDYTgVz3cwYBbAAibEBVSFw1SlGCINXdA0E7PIkmAIRgEEQoUFqIQfBgmIBSFVDfxPTh3Cw1ssRxPFaVfYCbggHooFIpIhGYJAqLY98gOAsZQPYDg0OHKDYL5BC0lVR8-gEti4AwrDgBwvCCKIrpSIAE35ZismUtjaKITxPAYjhZKMmBWOAlpONIog9JMvchIgj8G0AocvIA4SDU0VFmi5CcZzmfgO3ESQYG7AwYGhK5Sx7FA+ygcIktXTARHkcJWS4IcUDw2IOExBKQG9OAYMwrI6hggrfzTXJzEwAQRk4BKsnCaraTq65NAawI5xixcMqHTAOt4YAAC8wjgAAmQ5BuHCasgAdSQYBYjEGBCySDi9PwZbAmvKBYhiPKADZloGqgzmC+xoHgAzMBQZghHgTpuggBIgA).

Where to Find Useful Advice[​](#where-to-find-useful-advice "Direct link to Where to Find Useful Advice")
---------------------------------------------------------------------------------------------------------

* [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
* [React's documentation on TypeScript](https://react.dev/learn/typescript)
* [React + TypeScript Cheatsheets](https://github.com/typescript-cheatsheets/react-typescript-cheatsheet#reacttypescript-cheatsheets) has a good overview on how to use React with TypeScript

Using Custom Path Aliases with TypeScript[​](#using-custom-path-aliases-with-typescript "Direct link to Using Custom Path Aliases with TypeScript")
---------------------------------------------------------------------------------------------------------------------------------------------------

To use custom path aliases with TypeScript, you need to set the path aliases to work from both Babel and TypeScript. Here's how:

1. Edit your `tsconfig.json` to have your [custom path mappings](https://www.typescriptlang.org/docs/handbook/module-resolution.html#path-mapping). Set anything in the root of `src` to be available with no preceding path reference, and allow any test file to be accessed by using `tests/File.tsx`:

diff

```
{  
-  "extends": "@tsconfig/react-native/tsconfig.json"  
+  "extends": "@tsconfig/react-native/tsconfig.json",  
+  "compilerOptions": {  
+    "baseUrl": ".",  
+    "paths": {  
+      "*": ["src/*"],  
+      "tests": ["tests/*"],  
+      "@components/*": ["src/components/*"],  
+    },  
+  }  
}  

```

2. Add [`babel-plugin-module-resolver`](https://github.com/tleunen/babel-plugin-module-resolver) as a development package to your project:

* npm* Yarn

shell

```
npm install --save-dev babel-plugin-module-resolver  

```

shell

```
yarn add --dev babel-plugin-module-resolver  

```

3. Finally, configure your `babel.config.js` (note that the syntax for your `babel.config.js` is different from your `tsconfig.json`):

diff

```
{  
   presets: ['module:metro-react-native-babel-preset'],  
+  plugins: [  
+    [  
+       'module-resolver',  
+       {  
+         root: ['./src'],  
+         extensions: ['.ios.js', '.android.js', '.js', '.ts', '.tsx', '.json'],  
+         alias: {  
+           tests: ['./tests/'],  
+           "@components": "./src/components",  
+         }  
+       }  
+    ]  
+  ]  
}  

```

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/typescript.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/typescript.md)

Last updated on **Apr 14, 2025**

[Previous

Using Libraries](/docs/libraries)[Next

Upgrading to new versions](/docs/upgrading)

* [Getting Started with TypeScript](#getting-started-with-typescript)* [Adding TypeScript to an Existing Project](#adding-typescript-to-an-existing-project)* [Using JavaScript Instead of TypeScript](#using-javascript-instead-of-typescript)* [How TypeScript and React Native works](#how-typescript-and-react-native-works)* [What does React Native + TypeScript look like](#what-does-react-native--typescript-look-like)* [Where to Find Useful Advice](#where-to-find-useful-advice)* [Using Custom Path Aliases with TypeScript](#using-custom-path-aliases-with-typescript)

Develop

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

Participate

* [Showcase](/showcase)* [Contributing](/contributing/overview)* [Community](/community/overview)* [Directory](https://reactnative.directory/)* [Stack Overflow](https://stackoverflow.com/questions/tagged/react-native)

Find us

* [Blog](/blog)* [X](https://x.com/reactnative)* [Bluesky](https://bsky.app/profile/reactnative.dev)* [GitHub](https://github.com/facebook/react-native)

Explore More

* [ReactJS](https://react.dev/)* [Privacy Policy](https://opensource.fb.com/legal/privacy/)* [Terms of Service](https://opensource.fb.com/legal/terms/)

[![Meta Open Source Logo](/img/oss_logo.svg)![Meta Open Source Logo](/img/oss_logo.svg)](https://opensource.fb.com/)

Copyright © 2025 Meta Platforms, Inc.