Dev tools plugins - Expo Documentation

[Docs](/)

[Blog](https://expo.dev/blog)[Changelog](https://expo.dev/changelog)[Star Us on GitHub](https://github.com/expo/expo)

Search

[Home](/)[Guides](/guides/overview)[EAS](/eas)[Reference](/versions/latest)[Learn](/tutorial/overview)

Get started

[Introduction](/get-started/introduction)[Create a project](/get-started/create-a-project)[Set up your environment](/get-started/set-up-your-environment)[Start developing](/get-started/start-developing)[Next steps](/get-started/next-steps)

Develop

[Tools for development](/develop/tools)

Navigation

User interface

Development builds

Config plugins

Debugging

[Errors and warnings](/debugging/errors-and-warnings)[Runtime issues](/debugging/runtime-issues)[Tools](/debugging/tools)[Dev tools plugins](/debugging/devtools-plugins)[Create a dev tools plugin](/debugging/create-devtools-plugins)

[Authentication](/develop/authentication)[Unit testing](/develop/unit-testing)

Review

[Distributing apps for review](/review/overview)[Share previews with your team](/review/share-previews-with-your-team)[Open updates with Orbit](/review/with-orbit)

Deploy

[Build project for app stores](/deploy/build-project)[Submit to app stores](/deploy/submit-to-app-stores)[App stores metadata](/deploy/app-stores-metadata)[Send over-the-air updates](/deploy/send-over-the-air-updates)[Deploy web apps](/deploy/web)

Monitor

[Monitoring services](/monitoring/services)

More

[Core concepts](/core-concepts)[FAQ](/faq)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Dev tools plugins
=================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/debugging/devtools-plugins.mdx)

Learn about using dev tools plugins to inspect and debug your Expo project.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/debugging/devtools-plugins.mdx)

---

Dev tools plugins are available in your local development environment to help you debug your app. They consist of a small amount of code you add to a project that enables two-way communication between the app and an external Chrome window. This setup provides display tools to inspect the app, trigger certain behaviors for testing, and more.

Dev tools plugins are similar to Flipper plugins that are available in Development builds and Expo Go, and do not require adding native modules or config plugins to your project.

Add a dev tools plugin to a project
-----------------------------------

To add a dev tool plugin to your app, install it as a package and add a small snippet to connect the code to your app. This code is invoked from the app's root component to establish a two-way communication between your app and the plugin. Then, the plugin can inspect aspects of your app for the entire time your app runs in development mode.

All [Expo dev tools plugins](/debugging/devtools-plugins#expo-dev-tools-plugins) and plugins created with [our creation tool](/debugging/create-devtools-plugins) export a hook that you can use to connect the plugin to your app. The hook and any functions returned from it will no-op when the app is not running in development mode.

Some plugin hooks require parameters that relate to how the plugin inspects your app. For instance, a plugin for inspecting the React Navigation state might require a reference to the navigation root.

To start using the plugin, use the hook in your app's root component:

App.js

Copy

```
import { useMyDevToolsPlugin } from 'my-devtools-plugin';

export default App() {
  useMyDevToolsPlugin();
  return (/* rest of your app */)
}

```

In some cases, you may need to interact with a plugin directly. All plugins communicate through exports from `expo/devtools`, and you can send and listen to messages through `useDevToolsPluginClient`. Be sure to pass the same plugin name to `useDevToolsPluginClient` as is used by the plugin's web user interface:

App.js

Copy

```
import { useDevToolsPluginClient } from 'expo/devtools';

export default App() {
  const client = useDevToolsPluginClient('my-devtools-plugin');
   useEffect(() => {
    // receive messages
    client?.addMessageListener("ping", (data) => {
      alert(`Received ping from ${data.from}`);
    });
    // send messages
    client?.sendMessage("ping", { from: "app" });
   }, []);

  return (/* rest of your app */)
}

```

### Compatibility with Expo Go and Development builds

Dev tools plugins should only include JavaScript code. They are generally compatible with Expo Go and [Development builds](/develop/development-builds/introduction) and should not require creating a new development build to add the plugin. If a package's underlying module that the plugin inspects includes native code and is not part of Expo Go, create a new development build to use both the component and the plugin from that package.

For example, a dev tools plugin that inspects [React Native Firebase](/guides/using-firebase#using-react-native-firebase) will not work with Expo Go. React Native Firebase includes native code that is not part of Expo Go. To use the dev tools plugin and React Native Firebase, create a development build.

Using a dev tools plugin
------------------------

After installing the dev tools plugin and adding the connecting required code to your project, you can start the dev server up with `npx expo start`. Then press `shift` + `m` to open the list of available dev tools plugins. Select the plugin you want to use, and it will open in a new Chrome window.

> When starting the dev server with the Expo CLI, there is an option to press `?` to show all commands. This shows additional commands, including the shortcut to open more tools. Dev tools plugins can also be selected in this menu.

Expo dev tools plugins
----------------------

Expo provides some dev tools plugins for common debugging tasks. Follow the instructions below to start using them in your app.

> Note: Each of the following dev tools plugin hooks will only enable the plugin in development mode. It doesn't affect your production bundle.

### React Navigation

Inspired by [`@react-navigation/devtools`](https://github.com/react-navigation/react-navigation/tree/main/packages/devtools), the React Navigation dev tools plugin allows seeing the history of [React Navigation](https://reactnavigation.org/) actions and state. You can also rewind to previous points in your navigation history and send deep links to your app. Since Expo Router is built upon React Navigation, this plugin is fully compatible with [Expo Router](/router/introduction).

To use the plugin, start by installing the package:

Terminal

Copy

`-Â``npx expo install @dev-plugins/react-navigation`

Pass the navigation root to the plugin in your app's entry point:

Expo Router

React Navigation

app/\_layout.js

Copy

```
import { useEffect, useRef } from 'react';
import { useNavigationContainerRef, Slot } from 'expo-router';
import { useReactNavigationDevTools } from '@dev-plugins/react-navigation';

export default Layout() {
  const navigationRef = useNavigationContainerRef();

  useReactNavigationDevTools(navigationRef);

  return <Slot />;
}

```

App.js

Copy

```
import { NavigationContainer, useNavigationContainerRef } from '@react-navigation/native';
import { useReactNavigationDevTools } from '@dev-plugins/react-navigation';

export default function App() {
  const navigationRef = useNavigationContainerRef();

  useReactNavigationDevTools(navigationRef);

return (
    <NavigationContainer ref={navigationRef}>{/* ... */}</NavigationContainer>
  );
}


```

In the terminal, run `npx expo start`, press `shift` + `m` to open the list of dev tools, and then select the React Navigation plugin. This will open the plugin's web interface, showing your navigation history as you navigate through your app.

### Apollo Client

Inspired by [`react-native-apollo-devtools`](https://github.com/razorpay/react-native-apollo-devtools), the Apollo Client dev tools plugin allows inspecting cache, query, and mutation for the Apollo Client.

To use the plugin, start by installing the package:

Terminal

Copy

`-Â``npx expo install @dev-plugins/apollo-client`

Then pass your client instance to the plugin in your app's root component or where you wrap the rest of your app in the `ApolloProvider`:

App.js

Copy

```
import { ApolloProvider, ApolloClient, InMemoryCache } from '@apollo/client';
import { useApolloClientDevTools } from '@dev-plugins/apollo-client';

const client = new ApolloClient({
  uri: 'https://demo.test.com/',
  cache: new InMemoryCache(),
});

export default function App() {
  useApolloClientDevTools(client);

  return <ApolloProvider>{/* ... */}</ApolloProvider>;
}

```

In the terminal, run `npx expo start`, press `shift` + `m` to open the list of dev tools, and then select the Apollo Client plugin. This will open the plugin's web interface, showing your query history, cache, and mutations as your app performs Apollo Client operations.

### React Query

Inspired by [`react-query-native-devtools`](https://github.com/bgaleotti/react-query-native-devtools), the React Query dev tools plugin lets you explore data and queries, cache status, and refetch and remove queries from the cache from [TanStack Query](https://tanstack.com/query/latest/).

To use the plugin, start by installing the package:

Terminal

Copy

`-Â``npx expo install @dev-plugins/react-query`

Then pass your client instance to the plugin in your app's root component or where you wrap the rest of your app in the `QueryClientProvider`:

App.js

Copy

```
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { useReactQueryDevTools } from '@dev-plugins/react-query';

const queryClient = new QueryClient({});

export default function App() {
  useReactQueryDevTools(queryClient);

  return <QueryClientProvider client={queryClient}>{/* ... */}</QueryClientProvider>;
}

```

In the terminal, run `npx expo start`, press `shift` + `m` to open the list of dev tools, and then select the React Query plugin. This will open the plugin's web interface, displaying queries as they are used in your app.

### Redux

The `redux-devtools-expo-dev-plugin` is based on the [Redux DevTools](https://github.com/reduxjs/redux-devtools/) (from the Chrome extension). It provides a live list of actions and how they affect the state, and the ability to rewind, replay, and dispatch actions from the DevTools.

To use the plugin, start by installing the package:

Terminal

Copy

`-Â``npx expo install redux-devtools-expo-dev-plugin`

If you're using `@reduxjs/toolkit`, modify the `configureStore` call to disable the built-in dev tools by passing in `devTools: false`. Then, add in the Expo DevTools plugin enhancer by concatenating the `devToolsEnhancer()`. The `configureStore` call is going to look like the following:

store.js

Copy

```
import devToolsEnhancer from 'redux-devtools-expo-dev-plugin';

const store = configureStore({
  reducer: rootReducer,
  devTools: false,
  enhancers: getDefaultEnhancers => getDefaultEnhancers().concat(devToolsEnhancer()),
});

```

In the terminal, run `npx expo start`, press `shift` + `m` to open the list of dev tools, and then select `redux-devtools-expo-dev-plugin`. This will open the plugin's web interface, displaying the actions and contents of your store as actions are dispatched.

For complete installation and usage instructions, including if you're using `redux` directly rather than `@reduxjs/toolkit`, [see the project's README](https://github.com/matt-oakes/redux-devtools-expo-dev-plugin).

### TinyBase

The TinyBase dev tools plugin connects the TinyBase Store Inspector to your app, allowing you to view and update the contents of your app's store.

To use the plugin, start by installing the package:

Terminal

Copy

`-Â``npx expo install @dev-plugins/tinybase`

Then pass your client instance to the plugin in your app's root component or where you wrap the rest of your app with the store's `Provider`:

App.js

Copy

```
import { createStore } from 'tinybase';
import { useValue, Provider } from 'tinybase/lib/ui-react';
import { useTinyBaseDevTools } from '@dev-plugins/tinybase';

const store = createStore().setValue('counter', 0);

export default function App() {
  useTinyBaseDevTools(store);

  return <Provider store={store}>{/* ... */}</Provider>;
}

```

In the terminal, run `npx expo start`, press `shift` + `m` to open the list of dev tools, and then select the Tinybase plugin. This will open the plugin's web interface, displaying the contents of your store as it is modified.

[Previous (Develop - Debugging)

Tools](/debugging/tools)[Next (Develop - Debugging)

Create a dev tools plugin](/debugging/create-devtools-plugins)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/debugging/devtools-plugins.mdx)
* Last updated on May 01, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Add a dev tools plugin to a project](/debugging/devtools-plugins/#add-a-dev-tools-plugin-to-a-project)[Compatibility with Expo Go and Development builds](/debugging/devtools-plugins/#compatibility-with-expo-go-and-development-builds)[Using a dev tools plugin](/debugging/devtools-plugins/#using-a-dev-tools-plugin)[Expo dev tools plugins](/debugging/devtools-plugins/#expo-dev-tools-plugins)[React Navigation](/debugging/devtools-plugins/#react-navigation)[Apollo Client](/debugging/devtools-plugins/#apollo-client)[React Query](/debugging/devtools-plugins/#react-query)[Redux](/debugging/devtools-plugins/#redux)[TinyBase](/debugging/devtools-plugins/#tinybase)