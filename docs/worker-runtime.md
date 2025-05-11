EAS Hosting worker runtime - Expo Documentation

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

[Caching](/eas/hosting/reference/caching)[Responses and headers](/eas/hosting/reference/responses-and-headers)[Worker runtime](/eas/hosting/reference/worker-runtime)

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

EAS Hosting worker runtime
==========================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas/hosting/reference/worker-runtime.mdx)

Learn about EAS Hosting worker runtime and Node.js compatibility.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas/hosting/reference/worker-runtime.mdx)

---

EAS Hosting is built on [Cloudflare Workers](https://developers.cloudflare.com/workers/), a modern and powerful platform for serverless APIs that's been built for seamless scalability, high reliability, and exceptional performance globally.

The Cloudflare Workers runtime runs on the V8 JavaScript engine, the same powering JavaScript in Node.js and Chromium. However, its runtime has a few key differences from what you might be used to in traditional serverless Node.js deployments.

Instead of each request running in a full JavaScript process, Workers are designed to run them in small V8 isolates, a feature of the V8 runtime. Think of them as micro-containers in a single JavaScript process.

For more information on how Workers work, see [Cloudflare Workers](https://developers.cloudflare.com/workers/reference/how-workers-works/) documentation.

Node.js compatibility
---------------------

Cloudflare is part of [Winter TC](https://wintertc.org/), is more similar to the JavaScript environments in browsers and service workers rather than in Node.js. Restrictions like these provide a leaner runtime than Node.js, which is still familiar. This common runtime is a minimal standard supported by many JavaScript runtime these days.

This means, many Node.js APIs that you might be used to or some dependencies you utilize, aren't directly available in the EAS Hosting runtime. To ease this transition, as not all dependencies will have first-class support for Web APIs yet, Node.js compatibility modules exist and can be used in your API routes.

| Node.js built-in module | Supported | Implementation notes |
| --- | --- | --- |
| `node:assert` |  |  |
| `node:async_hooks` |  |  |
| `node:buffer` |  |  |
| `node:crypto` |  | Select deprecated algorithms are not available |
| `node:console` |  | Provided as partially functional JS shims |
| `node:constants` |  |  |
| `node:diagnostics_channel` |  | Select deprecated algorithms are not implemented |
| `node:dns` |  | `Resolver` is unimplemented, all DNS requests are sent to Cloudflare |
| `node:dns/promises` |  | All DNS requests are sent to Cloudflare |
| `node:events` |  |  |
| `node:fs` |  | Provided as JS stubs, since workers have no file system |
| `node:fs/promises` |  | Provided as JS stubs, since workers have no file system |
| `node:http` |  | Provided as partially functional JS shims based on `fetch` |
| `node:https` |  | Provided as partially functional JS shims based on `fetch` |
| `node:module` |  | `SourceMap` is unimplemented, partially supported otherwise |
| `node:net` |  | `Server` and `BlockList` are unimplemented, client sockets are partially supported |
| `node:os` |  | Provided as JS stubs that provide mock values matching Node.js on Linux |
| `node:path` |  |  |
| `node:path/posix` |  |  |
| `node:path/win32` |  |  |
| `node:process` |  | Provided as JS stubs |
| `node:punycode` |  |  |
| `node:querystring` |  |  |
| `node:readline` |  | Provided as non-functional JS stubs, since workers have no `stdin` |
| `node:readline/promises` |  | Provided as non-functional JS stubs, since workers have no `stdin` |
| `node:stream` |  |  |
| `node:stream/consumers` |  |  |
| `node:stream/promises` |  |  |
| `node:stream/web` |  |  |
| `node:string_decoder` |  |  |
| `node:timers` |  |  |
| `node:timers/promises` |  |  |
| `node:tls` |  | Provides JS stubs but is unimplemented |
| `node:trace_events` |  | Provided as non-functional JS stubs |
| `node:tty` |  | Provided as JS shims redirecting output to the Console API |
| `node:url` |  |  |
| `node:util` |  |  |
| `node:util/types` |  |  |
| `node:worker_threads` |  | Provided as non-functional JS stubs, since workers don't support threading |
| `node:zlib` |  |  |

These modules generally provide a lower-accuracy polyfill or approximation of their Node.js counterparts.
For example, the `http` and `https` modules only provide thin Node.js compatibility wrappers around the `fetch` API and cannot be used to make arbitrary HTTP requests.

Any of the above listed Node.js modules can be used in API routes or dependencies of your API routes as usual and will use appropriate compatibility modules. However, some of these modules may not provide any practical functionality and only exist to shim APIs to prevent runtime crashes.

Any modules that aren't mentioned here are unavailable or unsupported, and your code and none of your dependencies should rely on them being provided.

> More Node.js compatibility shims may be added in the future, but all Node.js APIs that are not documented in this non-exhaustive list are not expected to work.

Globals
-------

| JavaScript runtime globals | Supported | Implementation notes |
| --- | --- | --- |
| `process` |  |  |
| `process.env` |  | Populated with EAS Hosting environment variables |
| `process.stdout` |  | Will redirect output to the Console API (`console.log`) for logging |
| `process.stderr` |  | Will redirect output to the Console API (`console.error`) for logging |
| `setImmediate` |  |  |
| `clearImmediate` |  |  |
| `Buffer` |  | Set to `Buffer` from `node:buffer` |
| `EventEmitter` |  | Set to `EventEmitter` from `node:events` |
| `global` |  | Set to `globalThis` |
| `WeakRef` |  | Shim that resets references after each request |
| `FinalizationRegistry` |  | Garbage collection is not observable within workers |
| `require` |  | External requires are supported but limited to deployed JS files and built-in modules. Node module resolution is unsupported. |
| `require.cache` |  |  |

[Previous (EAS Hosting - Reference)

Responses and headers](/eas/hosting/reference/responses-and-headers)[Next (EAS Submit)

Introduction](/submit/introduction)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas/hosting/reference/worker-runtime.mdx)
* Last updated on April 07, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Node.js compatibility](/eas/hosting/reference/worker-runtime/#nodejs-compatibility)[Globals](/eas/hosting/reference/worker-runtime/#globals)