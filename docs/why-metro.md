Why Metro? - Expo Documentation

[Docs](/)

[Blog](https://expo.dev/blog)[Changelog](https://expo.dev/changelog)[Star Us on GitHub](https://github.com/expo/expo)

Search

[Home](/)[Guides](/guides/overview)[EAS](/eas)[Reference](/versions/latest)[Learn](/tutorial/overview)

[Overview](/guides/overview)

Development process

[Develop an app with Expo](/workflow/overview)[Configure with app config](/workflow/configuration)[Continuous Native Generation](/workflow/continuous-native-generation)[Using libraries](/workflow/using-libraries)[Privacy manifests](/guides/apple-privacy)[Permissions](/guides/permissions)[Environment variables](/guides/environment-variables)

Linking

Write native code

Compile locally

Web

Bundling

[Bundle with Metro](/guides/customizing-metro)[Analyzing JavaScript bundles](/guides/analyzing-bundles)[Tree shaking](/guides/tree-shaking)[Minification](/guides/minify)[Why Metro?](/guides/why-metro)

Existing React Native apps

Existing native apps

Reference

Expo Router

[Introduction](/router/introduction)[Installation](/router/installation)

Router 101

Navigation patterns

Advanced

Reference

Migration

Expo Modules API

[Overview](/modules/overview)[Get started](/modules/get-started)

Tutorials

Reference

Push notifications

[Overview](/push-notifications/overview)[About notification types](/push-notifications/what-you-need-to-know)[Expo push notifications setup](/push-notifications/push-notifications-setup)[Send notifications with the Expo Push Service](/push-notifications/sending-notifications)[Handle incoming notifications](/push-notifications/receiving-notifications)

Reference

More

[Upgrade Expo SDK](/workflow/upgrading-expo-sdk-walkthrough)

Assorted

Integrations

Troubleshooting

Regulatory compliance

[Data and Privacy protection](/regulatory-compliance/data-and-privacy-protection)[GDPR compliance](/regulatory-compliance/gdpr)[HIPAA compliance](/regulatory-compliance/hipaa)[Privacy Shield](/regulatory-compliance/privacy-shield)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Why Metro?
==========

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/why-metro.mdx)

Learn why Metro is the future of universal bundling in React Native and how it benefits developers.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/why-metro.mdx)

---

[Metro](https://metrobundler.dev/) is the official bundler for Expo and React Native. It's a central build tool in the Expo framework. Bundlers comprise thousands of opinions and trade-offs. This document outlines the key reasons why Expo is developed around Metro and how it benefits developers.

Official Meta bundler
---------------------

Metro is maintained by Meta, the maintainers of React, React Native, Yoga, and Hermes. It's used for developing some of the world's largest apps, ranging across all categories in the app stores.

Meta engineers actively develop Metro with the express requirement of bundling all their apps, across 400k+ source files, while remaining fast and reliable.

By having first-class Metro support, we ensure Expo developers have continuity across Meta's tools and get instant access to emerging features. This includes:

* React Fast Refresh was [first introduced](https://reactnative.dev/blog/2019/09/18/version-0.61) as a Metro feature in 2019. The React web community adopted it the following year via Webpack.
* Transforming JavaScript to Hermes bytecode for instant native startup.
* React Native DevTools, including first-class support for [network and JS debugging](/debugging/tools#debugging-with-react-native-devtools), is exclusively available with Metro and Hermes.
* React Compiler was initially rolled out as a Metro-compatible Babel plugin.

New and upcoming features that are planned to come to Metro include:

* Compiling Flow code to native machine code with Static Hermes. Learn more in the [Static Hermes](https://www.youtube.com/watch?v=GUM64b-gAGg) talk by Tzvetan Mikov.
* Data fetching, streaming, React Suspense, server rendering, and build-time static rendering with universal React Server Components for all platforms. Learn more in the [Universal React Server Components](https://www.youtube.com/watch?v=djhEgxQf3Kw) talk at React Conf 2024.

The Expo team collaborates with Meta to develop Metro for Expo Router, adding features like [file-based routing](/develop/file-based-routing), [web support](/guides/customizing-metro#web-support), [bundle splitting](/guides/customizing-metro#bundle-splitting), [tree shaking](/guides/tree-shaking), [CSS](/versions/latest/config/metro#css), [DOM components](/guides/dom-components), server components, and [API routes](/router/reference/api-routes).

Battle-tested at scale
----------------------

Nearly every React Native app in the world uses Metro, making it a battle-tested solution optimized for large-scale projects. This makes it suitable for developers of all sizes, from hobbyists to large companies. Metro is designed specifically to handle large-scale Meta apps, which is why it has features such as native file watching with Watchman and [shared remote caches](https://metrobundler.dev/docs/caching).

On-demand processing
--------------------

In development, Metro doesn't perform any platform-specific work until requested. This allows developers to work on large projects without paying a performance cost for the number of platforms they support. In conjunction with aggressive caching and [async routes](/router/reference/async-routes), developers can incrementally bundle only the parts of the app that they're actively working on.

Multi-dimensional
-----------------

Unlike traditional bundlers, which create multiple instances to bundle server and client code, Metro maximizes resource reuse across platforms and environments (server, client, DOM components). This architecture is ideal for multiplatform and server development.

Reusable transform memoization
------------------------------

Metro is incremental and can create cached transform artifacts that can be used across machines. This enables large teams to reuse work from remote builders, a technique used at Meta for all large projects.

Optimized for custom runtimes
-----------------------------

While other bundlers are designed around the static specification of web browsers, Metro is optimized for the flexibility of React Native. This enables features like generating the specific set of supported language features required for Hermes bytecode compilation which enables faster app startup in production. This will also extend to Static Hermes, which will compile static type information into machine code for native apps.

Cross-technology support
------------------------

Expo leverages Metro's technology to create novel functionality like [DOM components](/guides/dom-components). This allows a React component in a native app to be dynamically bundled as an entire website with all the same defaults as the parent app, on-demand.

Native asset exports
--------------------

Unlike traditional bundlers, where the end result is a fully hosted app, Metro's configuration options support exporting bundles to embed as native artifacts in standalone app binaries. This leverages OS-specific optimizations such as `xcassets` on Apple platforms.

Concurrent processing
---------------------

All AST transformation in Metro is performed concurrently across all available threads, maximizing the use of hardware.

Comparison with other approaches
--------------------------------

While Metro is designed for universal app development, it's often compared to other web-only bundlers. Here are some key differences:

### Browser ESM versus bundling

While bundlers like Vite leverage built-in ESM support in the browser, this approach can lead to slower practical development times at medium to large scales due to thousands of cascading network requests. Metro performs bundling in local development, which aligns the development results much closer to the production results and is better suited for React Native's larger module count.

### JavaScript versus native languages

Several bundlers are opting to write their core in Rust for performance reasons, but this comes with some trade-offs, such as more challenging contributions, patches, and development. Metro uses a mix of technologies based on the operation:

* The core bundler and utilities are written in JS/Flow.
* File watching is written in C++ via Watchman, with a JS fallback. Watchman is then used across projects on your computer.
* AST is parsed with Hermes parser (WebAssembly) to a Babel-compatible format.
* AST transformation is done with Babel. This maximizes developer customization.
* Minification uses Hermes on native platforms and Terser (with optional ESBuild support) for web.
* CSS parsing and minification is performed with [LightningCSS](https://lightningcss.dev/) (Rust).

This approach aligns with Meta and community tools while allowing easier debugging, profiling, and patching for developers.

[Previous (Development process - Bundling)

Minification](/guides/minify)[Next (Development process - Existing React Native apps)

Overview](/bare/overview)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/why-metro.mdx)
* Last updated on March 11, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Official Meta bundler](/guides/why-metro/#official-meta-bundler)[Battle-tested at scale](/guides/why-metro/#battle-tested-at-scale)[On-demand processing](/guides/why-metro/#on-demand-processing)[Multi-dimensional](/guides/why-metro/#multi-dimensional)[Reusable transform memoization](/guides/why-metro/#reusable-transform-memoization)[Optimized for custom runtimes](/guides/why-metro/#optimized-for-custom-runtimes)[Cross-technology support](/guides/why-metro/#cross-technology-support)[Native asset exports](/guides/why-metro/#native-asset-exports)[Concurrent processing](/guides/why-metro/#concurrent-processing)[Comparison with other approaches](/guides/why-metro/#comparison-with-other-approaches)[Browser ESM versus bundling](/guides/why-metro/#browser-esm-versus-bundling)[JavaScript versus native languages](/guides/why-metro/#javascript-versus-native-languages)