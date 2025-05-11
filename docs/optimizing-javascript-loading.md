Optimizing JavaScript loading · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/optimizing-javascript-loading)

* [Next](/docs/next/optimizing-javascript-loading)* [0.79](/docs/optimizing-javascript-loading)* [0.78](/docs/0.78/optimizing-javascript-loading)* [0.77](/docs/0.77/optimizing-javascript-loading)* [0.76](/docs/0.76/optimizing-javascript-loading)* [0.75](/docs/0.75/optimizing-javascript-loading)* [0.74](/docs/0.74/optimizing-javascript-loading)* [0.73](/docs/0.73/getting-started)* [0.72](/docs/0.72/getting-started)* [0.71](/docs/0.71/getting-started)* [0.70](/docs/0.70/getting-started)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [The Basics](/docs/getting-started)

  * [Environment setup](/docs/environment-setup)

    * [Workflow](/docs/running-on-device)

      * [UI & Interaction](/docs/style)

        * [Debugging](/docs/debugging)

          * [Testing](/docs/testing-overview)

            * [Performance](/docs/performance)

              + [Performance Overview](/docs/performance)+ [Speeding up your Build phase](/docs/build-speed)+ [Optimizing Flatlist Configuration](/docs/optimizing-flatlist-configuration)+ [Optimizing JavaScript loading](/docs/optimizing-javascript-loading)+ [Profiling](/docs/profiling)* [JavaScript Runtime](/docs/javascript-environment)

                * [Codegen](/docs/the-new-architecture/what-is-codegen)

                  * [Native Development](/docs/native-platform)

                    * [Android and iOS guides](/docs/headless-js-android)

                      * [Legacy Architecture](/docs/legacy/native-modules-intro)

On this page

Optimizing JavaScript loading
=============================

Parsing and running JavaScript code requires memory and time. Because of this, as your app grows, it's often useful to delay loading code until it's needed for the first time. React Native comes with some standard optimizations that are on by default, and there are techniques you can adopt in your own code to help React load your app more efficiently. There are also some advanced automatic optimizations (with their own tradeoffs) that are suitable for very large apps.

Recommended: Use Hermes[​](#recommended-use-hermes "Direct link to Recommended: Use Hermes")
--------------------------------------------------------------------------------------------

Hermes is the default engine for new React Native apps, and is highly optimized for efficient code loading. In release builds, JavaScript code is fully compiled to bytecode ahead of time. Bytecode is loaded to memory on-demand and does not need to be parsed like plain JavaScript does.

info

Read more about using Hermes in React Native [here](/docs/hermes).

Recommended: Lazy-load large components[​](#recommended-lazy-load-large-components "Direct link to Recommended: Lazy-load large components")
--------------------------------------------------------------------------------------------------------------------------------------------

If a component with a lot of code/dependencies is not likely to be used when initially rendering your app, you can use React's [`lazy`](https://react.dev/reference/react/lazy) API to defer loading its code until it's rendered for the first time. Typically, you should consider lazy-loading screen-level components in your app, so that adding new screens to your app does not increase its startup time.

info

Read more about [lazy-loading components with Suspense](https://react.dev/reference/react/lazy#suspense-for-code-splitting), including code examples, in React's documentation.

### Tip: Avoid module side effects[​](#tip-avoid-module-side-effects "Direct link to Tip: Avoid module side effects")

Lazy-loading components can change the behavior of your app if your component modules (or their dependencies) have *side effects*, such as modifying global variables or subscribing to events outside of a component. Most modules in React apps should not have any side effects.

SideEffects.tsx

```
import Logger from './utils/Logger';  
  
//  🚩 🚩 🚩 Side effect! This must be executed before React can even begin to  
// render the SplashScreen component, and can unexpectedly break code elsewhere  
// in your app if you later decide to lazy-load SplashScreen.  
global.logger = new Logger();  
  
export function SplashScreen() {  
  // ...  
}  

```

Advanced: Call `require` inline[​](#advanced-call-require-inline "Direct link to advanced-call-require-inline")
---------------------------------------------------------------------------------------------------------------

Sometimes you may want to defer loading some code until you use it for the first time, without using `lazy` or an asynchronous `import()`. You can do this by using the [`require()`](https://metrobundler.dev/docs/module-api/#require) function where you would otherwise use a static `import` at the top of the file.

VeryExpensive.tsx

```
import {Component} from 'react';  
import {Text} from 'react-native';  
// ... import some very expensive modules  
  
export default function VeryExpensive() {  
  // ... lots and lots of rendering logic  
  return <Text>Very Expensive Component</Text>;  
}  

```

Optimized.tsx

```
import {useCallback, useState} from 'react';  
import {TouchableOpacity, View, Text} from 'react-native';  
// Usually we would write a static import:  
// import VeryExpensive from './VeryExpensive';  
  
let VeryExpensive = null;  
  
export default function Optimize() {  
  const [needsExpensive, setNeedsExpensive] = useState(false);  
  const didPress = useCallback(() => {  
    if (VeryExpensive == null) {  
      VeryExpensive = require('./VeryExpensive').default;  
    }  
  
    setNeedsExpensive(true);  
  }, []);  
  
  return (  
    <View style={{marginTop: 20}}>  
      <TouchableOpacity onPress={didPress}>  
        <Text>Load</Text>  
      </TouchableOpacity>  
      {needsExpensive ? <VeryExpensive /> : null}  
    </View>  
  );  
}  

```

Advanced: Automatically inline `require` calls[​](#advanced-automatically-inline-require-calls "Direct link to advanced-automatically-inline-require-calls")
------------------------------------------------------------------------------------------------------------------------------------------------------------

If you use the React Native CLI to build your app, `require` calls (but not `import`s) will automatically be inlined for you, both in your code and inside any third-party packages (`node_modules`) you use.

tsx

```
import {useCallback, useState} from 'react';  
import {TouchableOpacity, View, Text} from 'react-native';  
  
// This top-level require call will be evaluated lazily as part of the component below.  
const VeryExpensive = require('./VeryExpensive').default;  
  
export default function Optimize() {  
  const [needsExpensive, setNeedsExpensive] = useState(false);  
  const didPress = useCallback(() => {  
    setNeedsExpensive(true);  
  }, []);  
  
  return (  
    <View style={{marginTop: 20}}>  
      <TouchableOpacity onPress={didPress}>  
        <Text>Load</Text>  
      </TouchableOpacity>  
      {needsExpensive ? <VeryExpensive /> : null}  
    </View>  
  );  
}  

```

info

Some React Native frameworks disable this behavior. In particular, in Expo projects, `require` calls are not inlined by default. You can enable this optimization by editing your project's Metro config and setting `inlineRequires: true` in [`getTransformOptions`](https://metrobundler.dev/docs/configuration#gettransformoptions).

### Pitfalls of inline `require`s[​](#pitfalls-of-inline-requires "Direct link to pitfalls-of-inline-requires")

Inlining `require` calls changes the order in which modules are evaluated, and can even cause some modules to *never* be evaluated. This is usually safe to do automatically, because JavaScript modules are often written to be side-effect-free.

If one of your modules does have side effects - for example, if it initializes some logging mechanism, or patches a global API used by the rest of your code - then you might see unexpected behavior or even crashes. In those cases, you may want to exclude certain modules from this optimization, or disable it entirely.

To **disable all automatic inlining of `require` calls:**

Update your `metro.config.js` to set the `inlineRequires` transformer option to `false`:

metro.config.js

```
module.exports = {  
  transformer: {  
    async getTransformOptions() {  
      return {  
        transform: {  
          inlineRequires: false,  
        },  
      };  
    },  
  },  
};  

```

To only **exclude certain modules from `require` inlining:**

There are two relevant transformer options: `inlineRequires.blockList` and `nonInlinedRequires`. See the code snippet for examples of how to use each one.

metro.config.js

```
module.exports = {  
  transformer: {  
    async getTransformOptions() {  
      return {  
        transform: {  
          inlineRequires: {  
            blockList: {  
              // require() calls in `DoNotInlineHere.js` will not be inlined.  
              [require.resolve('./src/DoNotInlineHere.js')]: true,  
  
              // require() calls anywhere else will be inlined, unless they  
              // match any entry nonInlinedRequires (see below).  
            },  
          },  
          nonInlinedRequires: [  
            // require('react') calls will not be inlined anywhere  
            'react',  
          ],  
        },  
      };  
    },  
  },  
};  

```

See the documentation for [`getTransformOptions` in Metro](https://metrobundler.dev/docs/configuration#gettransformoptions) for more details on setting up and fine-tuning your inline `require`s.

Advanced: Use random access module bundles (non-Hermes)[​](#advanced-use-random-access-module-bundles-non-hermes "Direct link to Advanced: Use random access module bundles (non-Hermes)")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

info

**Not supported when [using Hermes](#use-hermes).** Hermes bytecode is not compatible with the RAM bundle format, and provides the same (or better) performance in all use cases.

Random access module bundles (also known as RAM bundles) work in conjunction with the techniques mentioned above to limit the amount of JavaScript code that needs to be parsed and loaded into memory. Each module is stored as a separate string (or file) which is only parsed when the module needs to be executed.

RAM bundles may be physically split into separate files, or they may use the *indexed* format, consisting of a lookup table of multiple modules in a single file.

* Android* iOS

On Android enable the RAM format by editing your `android/app/build.gradle` file. Before the line `apply from: "../../node_modules/react-native/react.gradle"` add or amend the `project.ext.react` block:

```
project.ext.react = [  
  bundleCommand: "ram-bundle",  
]  

```

Use the following lines on Android if you want to use a single indexed file:

```
project.ext.react = [  
  bundleCommand: "ram-bundle",  
  extraPackagerArgs: ["--indexed-ram-bundle"]  
]  

```

On iOS, RAM bundles are always indexed ( = single file).

Enable the RAM format in Xcode by editing the build phase "Bundle React Native code and images". Before `../node_modules/react-native/scripts/react-native-xcode.sh` add `export BUNDLE_COMMAND="ram-bundle"`:

```
export BUNDLE_COMMAND="ram-bundle"  
export NODE_BINARY=node  
../node_modules/react-native/scripts/react-native-xcode.sh  

```

See the documentation for [`getTransformOptions` in Metro](https://metrobundler.dev/docs/configuration#gettransformoptions) for more details on setting up and fine-tuning your RAM bundle build.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/optimizing-javascript-loading.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/optimizing-javascript-loading.md)

Last updated on **Apr 14, 2025**

[Previous

Optimizing Flatlist Configuration](/docs/optimizing-flatlist-configuration)[Next

Profiling](/docs/profiling)

* [Recommended: Use Hermes](#recommended-use-hermes)* [Recommended: Lazy-load large components](#recommended-lazy-load-large-components)
    + [Tip: Avoid module side effects](#tip-avoid-module-side-effects)* [Advanced: Call `require` inline](#advanced-call-require-inline)* [Advanced: Automatically inline `require` calls](#advanced-automatically-inline-require-calls)
        + [Pitfalls of inline `require`s](#pitfalls-of-inline-requires)* [Advanced: Use random access module bundles (non-Hermes)](#advanced-use-random-access-module-bundles-non-hermes)

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