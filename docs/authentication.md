Authentication in Expo Router - Expo Documentation

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

[Stack](/router/advanced/stack)[Tabs](/router/advanced/tabs)[Drawer](/router/advanced/drawer)[Authentication](/router/advanced/authentication)[Nesting navigators](/router/advanced/nesting-navigators)[Modals](/router/advanced/modals)[Shared routes](/router/advanced/shared-routes)[Protected routes](/router/advanced/protected)

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

Authentication in Expo Router
=============================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/advanced/authentication.mdx)

How to implement authentication and protect routes with Expo Router.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/advanced/authentication.mdx)

---

[![Building an Auth Flow with Expo Router](https://i3.ytimg.com/vi/yNaOaR2kIa0/maxresdefault.jpg)

Building an Auth Flow with Expo Router

Learn how to implement an auth flow in your Expo Router project.](https://www.youtube.com/watch?v=yNaOaR2kIa0)

With Expo Router, all routes are always defined and accessible. You can use runtime logic to redirect users away from specific screens depending on whether they are authenticated. There are two different techniques for authenticating users within routes. This guide provides an example that demonstrates the functionality of standard native apps.

Using React Context and Route Groups
------------------------------------

It's common to restrict specific routes to users who are not authenticated. This is achievable in an organized way by using React Context and Route Groups. Consider the following project structure that has a `/sign-in` route that is always accessible and a `(app)` group that requires authentication:

`app`

â`_layout.tsx`

â`sign-in.tsx``Always accessible`

â`(app)`

ââ`_layout.tsx``Protects child routes`

ââ`index.tsx``Requires authorization`

1

To follow the above example, set up a [React Context provider](https://react.dev/reference/react/createContext) that can expose an authentication session to the entire app. You can implement your custom authentication session provider or use the one from the Example authentication context below.

Example authentication context

This provider uses a mock implementation. You can replace it with your own [authentication provider](/guides/authentication).

ctx.tsx

Copy

```
import { use, createContext, type PropsWithChildren } from 'react';
import { useStorageState } from './useStorageState';

const AuthContext = createContext<{
  signIn: () => void;
  signOut: () => void;
  session?: string | null;
  isLoading: boolean;
}>({
  signIn: () => null,
  signOut: () => null,
  session: null,
  isLoading: false,
});

// This hook can be used to access the user info.
export function useSession() {
  const value = use(AuthContext);
  if (!value) {
    throw new Error('useSession must be wrapped in a <SessionProvider />');
  }

  return value;
}

export function SessionProvider({ children }: PropsWithChildren) {
  const [[isLoading, session], setSession] = useStorageState('session');

  return (
    <AuthContext
      value={{
        signIn: () => {
          // Perform sign-in logic here
          setSession('xxx');
        },
        signOut: () => {
          setSession(null);
        },
        session,
        isLoading,
      }}>
      {children}
    </AuthContext>
  );
}

```

The following code snippet is a basic hook that persists tokens securely on native with [`expo-secure-store`](/versions/latest/sdk/securestore) and in local storage on web.

useStorageState.ts

Copy

```
import  { useEffect, useCallback, useReducer } from 'react';
import * as SecureStore from 'expo-secure-store';
import { Platform } from 'react-native';

type UseStateHook<T> = [[boolean, T | null], (value: T | null) => void];

function useAsyncState<T>(
  initialValue: [boolean, T | null] = [true, null],
): UseStateHook<T> {
  return useReducer(
    (state: [boolean, T | null], action: T | null = null): [boolean, T | null] => [false, action],
    initialValue
  ) as UseStateHook<T>;
}

export async function setStorageItemAsync(key: string, value: string | null) {
  if (Platform.OS === 'web') {
    try {
      if (value === null) {
        localStorage.removeItem(key);
      } else {
        localStorage.setItem(key, value);
      }
    } catch (e) {
      console.error('Local storage is unavailable:', e);
    }
  } else {
    if (value == null) {
      await SecureStore.deleteItemAsync(key);
    } else {
      await SecureStore.setItemAsync(key, value);
    }
  }
}

export function useStorageState(key: string): UseStateHook<string> {
  // Public
  const [state, setState] = useAsyncState<string>();

  // Get
  useEffect(() => {
    if (Platform.OS === 'web') {
      try {
        if (typeof localStorage !== 'undefined') {
          setState(localStorage.getItem(key));
        }
      } catch (e) {
        console.error('Local storage is unavailable:', e);
      }
    } else {
      SecureStore.getItemAsync(key).then(value => {
        setState(value);
      });
    }
  }, [key]);

  // Set
  const setValue = useCallback(
    (value: string | null) => {
      setState(value);
      setStorageItemAsync(key, value);
    },
    [key]
  );

  return [state, setValue];
}

```

2

Use the `SessionProvider` in the root layout to provide the authentication context to the entire app. It's imperative that the `<Slot />` is mounted before any navigation events are triggered. Otherwise, a runtime error will be thrown.

app/\_layout.tsx

Copy

```
import { Slot } from 'expo-router';
import { SessionProvider } from '../ctx';

export default function Root() {
  // Set up the auth context and render our layout inside of it.
  return (
    <SessionProvider>
      <Slot />
    </SessionProvider>
  );
}

```

3

Create a nested [layout route](/router/basics/layout) that checks whether users are authenticated before rendering the child route components. This layout route redirects users to the sign-in screen if they are not authenticated.

app/(app)/\_layout.tsx

Copy

```
import { Text } from 'react-native';
import { Redirect, Stack } from 'expo-router';

import { useSession } from '../../ctx';

export default function AppLayout() {
  const { session, isLoading } = useSession();

  // You can keep the splash screen open, or render a loading screen like we do here.
  if (isLoading) {
    return <Text>Loading...</Text>;
  }

  // Only require authentication within the (app) group's layout as users
  // need to be able to access the (auth) group and sign in again.
  if (!session) {
    // On web, static rendering will stop here as the user is not authenticated
    // in the headless Node process that the pages are rendered in.
    return <Redirect href="/sign-in" />;
  }

  // This layout can be deferred because it's not the root layout.
  return <Stack />;
}

```

4

Create the `/sign-in` screen. It can toggle the authentication using `signIn()`. Since this screen is outside the `(app)` group, the group's layout and authentication check do not run when rendering this screen. This lets logged-out users see this screen.

app/sign-in.tsx

Copy

```
import { router } from 'expo-router';
import { Text, View } from 'react-native';

import { useSession } from '../ctx';

export default function SignIn() {
  const { signIn } = useSession();
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text
        onPress={() => {
          signIn();
          // Navigate after signing in. You may want to tweak this to ensure sign-in is
          // successful before navigating.
          router.replace('/');
        }}>
        Sign In
      </Text>
    </View>
  );
}

```

5

Implement an authenticated screen that lets users sign out.

app/(app)/index.tsx

Copy

```
import { Text, View } from 'react-native';

import { useSession } from '../../ctx';

export default function Index() {
  const { signOut } = useSession();
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text
        onPress={() => {
          // The `app/(app)/_layout.tsx` will redirect to the sign-in screen.
          signOut();
        }}>
        Sign Out
      </Text>
    </View>
  );
}

```

You now have an app that can present a loading state while it checks the initial authentication state and redirects to the sign-in screen if the user is not authenticated. If a user visits a deep link to any routes with the authentication check, they'll be redirected to the sign-in screen.

Alternative loading states
--------------------------

With Expo Router, something must be rendered to the screen while loading the initial auth state. In the example above, the app layout renders a loading message. Alternatively, you can make the `index` route a loading state and move the initial route to something such as `/home`, which is similar to how X works.

Modals and per-route authentication
-----------------------------------

Another common pattern is to render a sign-in modal over the top of the app. This enables you to dismiss and partially preserve deep links when the authentication is complete. However, this pattern requires routes to be rendered in the background as these routes require handling data loading without authentication.

`app`

â`_layout.tsx``Declares global session context`

â`(app)`

ââ`_layout.tsx`

ââ`sign-in.tsx``Modal presented over the root`

ââ`(root)`

âââ`_layout.tsx``Protects child routes`

âââ`index.tsx``Requires authorization`

app/(app)/\_layout.tsx

Copy

```
import { Stack } from 'expo-router';

export const unstable_settings = {
  initialRouteName: '(root)',
};

export default function AppLayout() {
  return (
    <Stack>
      <Stack.Screen name="(root)" />
      <Stack.Screen
        name="sign-in"
        options={{
          presentation: 'modal',
        }}
      />
    </Stack>
  );
}

```

Navigating without navigation
-----------------------------

You may encounter the following error when the app attempts to perform navigation without a navigator mounted in the [root layout](/router/basics/layout#root-layout).

```
Error: Attempted to navigate before mounting the Root Layout component. Ensure the Root Layout component is rendering a Slot, or other navigator on the first render.

```

To fix this, add a group and move conditional logic down a level.

### Before

`app`

â`_layout.tsx`

â`about.tsx`

app/\_layout.tsx

Copy

```
export default function RootLayout() {
  React.useEffect(() => {
    // This navigation event will trigger the error above.
    router.push('/about');
  }, []);

  // This conditional statement creates a problem since the root layout's
  // content (the Slot) must be mounted before any navigation events occur.
  if (isLoading) {
    return <Text>Loading...</Text>;
  }

  return <Slot />;
}

```

### After

`app`

â`_layout.tsx`

â`(app)`

ââ`_layout.tsx``Move conditional logic down a level`

ââ`about.tsx`

app/\_layout.tsx

Copy

```
export default function RootLayout() {
  return <Slot />;
}

```

app/(app)/\_layout.tsx

Copy

```
export default function RootLayout() {
  React.useEffect(() => {
    router.push('/about');
  }, []);

  // It is OK to defer rendering this nested layout's content. We couldn't
  // defer rendering the root layout's content since a navigation event (the
  // redirect) would have been triggered before the root layout's content had
  // been mounted.
  if (isLoading) {
    return <Text>Loading...</Text>;
  }

  return <Slot />;
}

```

Middleware
----------

Traditionally, websites may leverage some form of server-side redirection to protect routes. Expo Router on the web currently only supports build-time static generation and has no support for custom middleware or serving. This can be added in the future to provide a more optimal web experience. In the meantime, authentication can be implemented by using client-side redirects and a loading state.

[Previous (Expo Router - Navigation patterns)

Drawer](/router/advanced/drawer)[Next (Expo Router - Navigation patterns)

Nesting navigators](/router/advanced/nesting-navigators)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/advanced/authentication.mdx)
* Last updated on April 26, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Using React Context and Route Groups](/router/advanced/authentication/#using-react-context-and-route-groups)[Alternative loading states](/router/advanced/authentication/#alternative-loading-states)[Modals and per-route authentication](/router/advanced/authentication/#modals-and-per-route-authentication)[Navigating without navigation](/router/advanced/authentication/#navigating-without-navigation)[Before](/router/advanced/authentication/#before)[After](/router/advanced/authentication/#after)[Middleware](/router/advanced/authentication/#middleware)