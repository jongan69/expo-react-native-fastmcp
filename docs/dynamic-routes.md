Dynamic routes - Expo Documentation

[Docs](/)

[Blog](https://expo.dev/blog)[Changelog](https://expo.dev/changelog)[Star Us on GitHub](https://github.com/expo/expo)

Search

[Home](/)[Guides](/guides/overview)[EAS](/eas)[Reference](/versions/latest)[Learn](/tutorial/overview)

Get started

[Introduction](/get-started/introduction)[Create a project](/get-started/create-a-project)[Set up your environment](/get-started/set-up-your-environment)[Start developing](/get-started/start-developing)[Next steps](/get-started/next-steps)

Develop

[Tools for development](/develop/tools)

Navigation

[File-based routing](/develop/file-based-routing)[Dynamic routes](/develop/dynamic-routes)[Next steps](/develop/next-steps)

User interface

Development builds

Config plugins

Debugging

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

Dynamic routes
==============

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/dynamic-routes.mdx)

Learn about dynamic routes and how you can create them using Expo Router library.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/dynamic-routes.mdx)

---

A dynamic route allows matching one or multiple paths based on a dynamic segment embedded in the URL. This segment is in the form of a variable, such as a unique identifier, and your app doesn't know the exact segment ahead of time.

This guide explains how to handle dynamic routes with Expo Router.

> This guide continues to build on top of the example and the app directory structure used in the previous [File-based routing](/develop/file-based-routing).

Dynamic route convention
------------------------

A dynamic segment of a route is created by wrapping a file's name in square brackets. For example, [id].tsx.

> What is a dynamic segment? Any segment of a path in a URL that is dynamic. For example, in an app screen where it displays a users list, you might have a path such as `/details/[id]` where the `[id]` is the dynamic segment and displays details based on the `id` of the user.

Create a dynamic route
----------------------

Let's consider the following app directory structure:

`app`

â`_layout.tsx``Root layout`

â`(tabs)`

ââ`_layout.tsx``Tab layout`

ââ`settings.tsx``matches '/settings'`

ââ`(home)`

âââ`_layout.tsx``Home layout`

âââ`index.tsx``matches '/'`

âââ`details`

ââââ`[id].tsx``matches '/details/1'`

In the above file structure, the `[id]` is used to display information for the route details/[id].tsx. The same route will display unique information based on the value of the `id`:

| Route | Matched URL |
| --- | --- |
| details/[id].tsx | `/details/1` |
| details/[id].tsx | `/details/2` |

This dynamic segment convention makes sure that when an app user navigates from the home screen to the details screen, they view the correct information for the dynamic segment of the route.

Use `Link` to navigate to a dynamic route
-----------------------------------------

Navigating from one route to a dynamic route is done by providing query parameters to the `Link` component either statically or using the `href` object.

For example, the following code allows you to navigate to the dynamic route statically using query parameters:

app/(home)/index.tsx

Copy

```
import { Link } from 'expo-router';
import { View, Text, StyleSheet } from 'react-native';

export default function HomeScreen() {
  return (
    <View style={styles.container}>
      <Text>Home</Text>
      <Link href="/details/1">View first user details</Link>
      <Link href="/details/2">View second user details</Link>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

```

You can also use the `href` object to provide a `pathname` which takes the value of the dynamic route and passes `params`:

app/(home)/index.tsx

Copy

```
import { Link } from 'expo-router';
import { View, Text, StyleSheet } from 'react-native';

export default function HomeScreen() {
  return (
    <View style={styles.container}>
      <Text>Home</Text>
      <Link
        href={{
          pathname: '/details/[id]',
          params: { id: 'bacon' },
        }}>
        View user details
      </Link>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

```

Access parameters from dynamic segments
---------------------------------------

Dynamic segments of a URL are accessible with a [route parameter](/router/reference/url-parameters) in the route component. For example, you can use the [`useLocalSearchParams`](/router/reference/hooks#uselocalsearchparams) hook which returns the URL parameters for the selected route.

app/(home)/details/[id].tsx

Copy

```
import { useLocalSearchParams } from 'expo-router';
import { View, Text, StyleSheet } from 'react-native';

export default function DetailsScreen() {
  const { id } = useLocalSearchParams();

  return (
    <View style={styles.container}>
      <Text>Details of user {id} </Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

```

When `/` pushes `/details/1`, the `useLocalSearchParams` returns `{ id: '1' }` because `/details/1` is the selected route.

[Previous (Develop - Navigation)

File-based routing](/develop/file-based-routing)[Next (Develop - Navigation)

Next steps](/develop/next-steps)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/develop/dynamic-routes.mdx)
* Last updated on July 30, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Dynamic route convention](/develop/dynamic-routes/#dynamic-route-convention)[Create a dynamic route](/develop/dynamic-routes/#create-a-dynamic-route)[Use Link to navigate to a dynamic route](/develop/dynamic-routes/#use-link-to-navigate-to-a-dynamic-route)[Access parameters from dynamic segments](/develop/dynamic-routes/#access-parameters-from-dynamic-segments)