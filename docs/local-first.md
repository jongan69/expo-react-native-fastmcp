Local-first architecture with Expo - Expo Documentation

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

[Authentication with OAuth or OpenID providers](/guides/authentication)[Using Hermes](/guides/using-hermes)[iOS Developer Mode](/guides/ios-developer-mode)[Expo Vector Icons](/guides/icons)[Localization](/guides/localization)[Configure JS engines](/guides/configuring-js-engines)[Using Bun](/guides/using-bun)[Edit rich text](/guides/editing-richtext)[App store assets](/guides/store-assets)[Local-first](/guides/local-first)[Keyboard handling](/guides/keyboard-handling)

Integrations

Troubleshooting

Regulatory compliance

[Data and Privacy protection](/regulatory-compliance/data-and-privacy-protection)[GDPR compliance](/regulatory-compliance/gdpr)[HIPAA compliance](/regulatory-compliance/hipaa)[Privacy Shield](/regulatory-compliance/privacy-shield)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Local-first architecture with Expo
==================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/local-first.mdx)

An introduction to the emerging local-first software movement, including links to relevant learning resources and tools.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/local-first.mdx)

---

> This guide is a work in progress. If you have any feedback, [open an issue](https://github.com/expo/expo/issues/new/choose) in our GitHub repository.

The term "local-first" was first coined in the paper ["Local-first software"](https://www.inkandswitch.com/local-first/), written by the research lab [Ink & Switch](https://www.inkandswitch.com/), but the ideas behind it have been around for a long time. It's the architecture that powers some of our favorite apps, like [Linear](https://linear.app/), [Superhuman](https://superhuman.com/), [Excalidraw](https://excalidraw.com/), and even [Apple Notes](https://en.wikipedia.org/wiki/Notes_(Apple)).

In local-first software, "the availability of another computer should never prevent you from working" ([via Martin Kleppmann](https://www.youtube.com/watch?v=NMq0vncHJvU)). When you are offline, you can still read and write directly from/to a database on your device. You can trust the software to work offline, and you know that when you are connected to the internet, your data will be seamlessly synced and available on any of your devices running the app. When you're online, this architecture is well suited for "multiplayer" apps, [as popularized by Figma](https://www.figma.com/blog/how-figmas-multiplayer-technology-works/).

To dig deeper into what local-first is and how it works, refer to the [additional resources](/guides/local-first#additional-resources) below.

Why use local-first architecture?
---------------------------------

### User experience benefits

Local-first software feels fast because interactions are no longer network-bound, you can read and write directly from/to a database on your device.

You can trust the software to work offline, and you know that when you are connected to the internet, your data will be seamlessly synced and available on any of your devices running the app.

Another characteristic of local-first software is that it is collaborative â multiple devices can work on the same data, and changes are synced across all of them. This can happen in real-time when you collaborate on a design in [Figma](https://www.figma.com/) or asynchronously when you create a task while offline in Linear and it is synced when you are online again.

### Developer experience benefits

You no longer have to manage various states of your app for each network request â "loaded", "loading", "error", and so on, with their corresponding UI states and other logic. Write to a local database, and the app will automatically sync the changes to the server. This means that you can focus on building the app, and not worry as much about the networking and offline states.

Your server availability may still be important, but in the event of an outage your users can still access the app and continue working. You may even provide a mechanism to sync the data without going through your server.

Challenges in building local-first apps
---------------------------------------

The tools available today are still in their early stages, and so you may find yourself solving problems that you would expect to be solved by the tools you are using today. For example, you may need to implement a custom sync layer, or you may have to figure out how to handle permissions for multiple users operating on the same data. As the ecosystem evolves, we expect it to become easier to build local-first apps. If you're not prepared to be an early adopter, and everything that comes with that, you might want to wait for the tools to mature before you start building your app with local-first tools.

Tools for building local-first apps
-----------------------------------

A comprehensive list of tools is available on the ["Local-first software" community website](https://localfirstweb.dev/). The following is a shorter list of tools that we at Expo have had direct experience working with.

One way to think of local-first tools is to group them by the following categories: persistence, state management, and syncing. Some tools will fit into multiple categories if they handle multiple aspects of the problem. Syncing can be further subdivided into syncable data structures and transport layers.

### Legend-State

[Legend-State](https://legendapp.com/open-source/state/v3/) is a super fast all-in-one state and sync library that lets you write less code to make faster apps. It has the following primary goals:

* Faster state management for React apps
* Fine-grained reactivity for minimal renders
* Powerful sync and persistence (with Supabase support built-in)

It works with Expo and React Native (via [`react-native-async-storage`](https://github.com/react-native-async-storage/async-storage?tab=readme-ov-file#react-native-async-storage)). This makes it a perfect match for building local-first mobile and web apps. Get started by using the [Legend-State Supabase example](https://github.com/expo/examples/tree/master/with-legend-state-supabase):

Terminal

Copy

`-Â``npx create-expo-app --example with-legend-state-supabase`

### TinyBase

[TinyBase](https://tinybase.org/) calls itself "the reactive data store for local-first apps". It is a state management library that plugs in to many of the most popular syncing and persistence layers, such as [Yjs](/guides/local-first#yjs) and [SQLite](/guides/local-first#sqlite). It's a great choice for building local-first apps that need to persist and sync data. Get started by using the [TinyBase example](https://github.com/expo/examples/tree/master/with-tinybase):

Terminal

Copy

`-Â``npx create-expo-app --example with-tinybase`

TinyBase works seamlessly with Expo Go, allowing you to develop quickly. On Android and iOS, it uses the [`expo-sqlite`](/versions/latest/sdk/sqlite) library to persist data. On the web, it relies on the [`localStorage`](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage) API. [Beto Moedano](https://github.com/betomoedano) demonstrates how to build a [Universal Local-first Shopping List App](https://github.com/betomoedano/groceries-shopping-list-app) in the following video:

[![Watch: Build a Local-First Real-Time Shopping List App with Expo and TinyBase](https://i3.ytimg.com/vi/HqOiB2tDM8Q/maxresdefault.jpg)

Watch: Build a Local-First Real-Time Shopping List App with Expo and TinyBase](https://www.youtube.com/watch?v=HqOiB2tDM8Q)

### SQLite

[Expo SQLite](/versions/latest/sdk/sqlite) is a SQLite library that is a great choice for persistence for local-first apps. You can use SQLite with different state management and syncing layers in front of it, such as [`y-expo-sqlite`](https://github.com/brentvatne/y-expo-sqlite) to persist [Yjs](/guides/local-first#yjs) documents, and [TinyBase](/guides/local-first#tinybase) as a state management layer. Using SQLite is flexible, but you will need to combine it with other tools or build your own tools to get a complete local-first solution. See [Expo SQLite API reference](/versions/latest/sdk/sqlite) for more information.

### Yjs

[Yjs](https://github.com/yjs/yjs) is a [CRDT implementation](https://github.com/yjs/yjs?tab=readme-ov-file#yjs-crdt-algorithm) that provides data types that can be synced across multiple clients. When building an app with Yjs and working with data that you would like to be able to sync, then you would use `Y.Array` and `Y.Map` to represent your data rather than `Array` and `Object`. You may use a library like [TinyBase](/guides/local-first#tinybase) for state management on top of Yjs, and persistence can be handled by a variety of tools, from a JSON file on your filesystem to a full-fledged database (such as [`y-expo-sqlite`](https://github.com/brentvatne/y-expo-sqlite)) and everything in between. See [Yjs's GitHub repository](https://github.com/yjs/yjs) for more information.

### Prisma

[Prisma](https://prisma.io) is well known as the most popular ORM for Node.js and TypeScript backends, and it's now available for [Expo and React Native in early access](https://www.prisma.io/blog/bringing-prisma-orm-to-react-native-and-expo). Prisma aims to provide a complete local-first solution, with state management, syncing, and persistence all covered for you. While it's still early, [Beto Moedano](https://github.com/betomoedano) has put together a full walkthrough of using Prisma with Expo to build a local-first Notion clone, [check out the code on GitHub](https://github.com/betomoedano/React-Native-Notion-Clone).

[![Watch: Building a Local-first Notion Clone with React Native Expo and Prisma](https://i3.ytimg.com/vi/uTrPte0sCiw/maxresdefault.jpg)

Watch: Building a Local-first Notion Clone with React Native Expo and Prisma](https://www.youtube.com/watch?v=uTrPte0sCiw)

### Jazz

[Jazz.tools](https://jazz.tools/docs/react-native) is a framework for building local-first apps. It is open source, provides first-class support for Expo and you can self-host it or use [Jazz Cloud](https://jazz.tools/cloud) to start quickly. [Jazz](https://jazz.tools). To learn more, check out the [examples](https://jazz.tools/examples#react-native) or see the [Getting Started Guide](https://jazz.tools/docs/react-native) for detailed instructions.

### LiveStore

[LiveStore](https://livestore.dev/getting-started/expo/) is a client-centric local-first data layer for high-performance applications. It provides first-class support for Expo, and it's a great choice for building local-first apps. See the blog post on [LiveStore: SQLite-based data layer for local-first apps](https://expo.dev/blog/local-first-application-development-with-livestore).

[![Watch: How to build local-first native apps with LiveStore and Expo](https://i3.ytimg.com/vi/zQIhJqYU1Qw/maxresdefault.jpg)

Watch: How to build local-first native apps with LiveStore and Expo](https://www.youtube.com/watch?v=zQIhJqYU1Qw)

### Turso

[Turso](https://turso.tech) is a modern database service built on SQLite. It now supports [Offline Sync](https://turso.tech/blog/turso-offline-sync-public-beta), which enables true local-first experiences. You can sync databases between local and remote sources with bidirectional sync and built-in conflict detection. While automatic conflict resolution isn't available yet, this feature is still a major step forward. You can use Turso today with [expo-sqlite](/versions/latest/sdk/sqlite). To learn more, read the [Turso: Offline Sync Public Beta](https://turso.tech/blog/turso-offline-sync-public-beta) blog post. For an example integration, check out the [Notes App](https://github.com/betomoedano/notes-app).

[![Watch: How to build a local-first Notes App with Turso and Expo](https://i3.ytimg.com/vi/SBv32tmyb3k/maxresdefault.jpg)

Watch: How to build a local-first Notes App with Turso and Expo](https://www.youtube.com/watch?v=SBv32tmyb3k)

### Other tools

The following list, far from being comprehensive, provides other tools that have caught our attention and that you may find interesting to explore. For a more thorough list of tools, see ["Local-first software" community website](https://localfirstweb.dev/).

* [Automerge](https://automerge.org/)
* [ElectricSQL](https://electric-sql.com/)
* [Instant](https://www.instantdb.com/)
* [PowerSync](https://www.powersync.com/)

Additional resources
--------------------

* ["The past, present, and future of local-first"](https://www.youtube.com/watch?v=NMq0vncHJvU) by Martin Kleppmann
* ["Local-first software"](https://www.inkandswitch.com/local-first/) by Ink & Switch
* ["Local-first software" community website](https://localfirstweb.dev/) and [meetup playlist on YouTube](https://www.youtube.com/playlist?list=PLTbD2QA-VMnXFsLbuPGz1H-Najv9MD2-H)
* [localfirst.fm podcast](https://localfirst.fm/) by Johannes Schickling

[Previous (More - Assorted)

App store assets](/guides/store-assets)[Next (More - Assorted)

Keyboard handling](/guides/keyboard-handling)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/local-first.mdx)
* Last updated on April 10, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Why use local-first architecture?](/guides/local-first/#why-use-local-first-architecture)[User experience benefits](/guides/local-first/#user-experience-benefits)[Developer experience benefits](/guides/local-first/#developer-experience-benefits)[Challenges in building local-first apps](/guides/local-first/#challenges-in-building-local-first-apps)[Tools for building local-first apps](/guides/local-first/#tools-for-building-local-first-apps)[Legend-State](/guides/local-first/#legend-state)[TinyBase](/guides/local-first/#tinybase)[SQLite](/guides/local-first/#sqlite)[Yjs](/guides/local-first/#yjs)[Prisma](/guides/local-first/#prisma)[Jazz](/guides/local-first/#jazz)[LiveStore](/guides/local-first/#livestore)[Turso](/guides/local-first/#turso)[Other tools](/guides/local-first/#other-tools)[Additional resources](/guides/local-first/#additional-resources)