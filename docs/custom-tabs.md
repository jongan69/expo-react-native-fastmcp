Custom tab layouts - Expo Documentation

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

[Platform-specific Modules](/router/advanced/platform-specific-modules)[Customizing links](/router/advanced/native-intent)[Settings](/router/advanced/router-settings)[Apple Handoff](/router/advanced/apple-handoff)[Custom tabs](/router/advanced/custom-tabs)

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

Custom tab layouts
==================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/advanced/custom-tabs.mdx)

Learn how to use headless tab components to create custom tab layouts in Expo Router.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/advanced/custom-tabs.mdx)

---

> Experimentally available in SDK 52 and above. For the React Navigation styled tabs layout that are commonly used in native apps, see [Tabs](/router/advanced/tabs).

Expo Router offers a set of components to create custom tab layouts via the submodule [`expo-router/ui`](/versions/latest/sdk/router-ui). Unlike the React Navigation styled `Tabs`, these components are unstyled and flexible. They are designed to allow you build complex UI patterns from scratch in your project.

Anatomy of custom Tabs components
---------------------------------

There are four components offered by `expo-router/ui` to create custom tab layouts:

| Component | Description |
| --- | --- |
| `Tabs` | Wrapper component which contains the `<View>` for the tabs. |
| `TabList` | The containing `<View>` for the list of `TabTrigger` components. |
| `TabTrigger` | A trigger component to switch to the specified tab. It is used to define the route using `href` prop and a `name` for each tab. |
| `TabSlot` | A slot to render the currently selected tab. |

A bare minimum structure of a custom tab layout would consist of a `TabList` (containing `TabTrigger` components for each tab) and a`TabSlot`, all within the `Tabs` component, as shown here:

app/(tabs)/\_layout.tsx

Copy

```
import { Tabs, TabList, TabTrigger, TabSlot } from 'expo-router/ui';

// Defining the layout of the custom tab navigator
export default function Layout() {
  return (
    <Tabs>
      <TabSlot />
      <TabList>
        <TabTrigger name="home" href="/">
          <Text>Home</Text>
        </TabTrigger>
        <TabTrigger name="article" href="/article">
          <Text>Article</Text>
        </TabTrigger>
      </TabList>
    </Tabs>
  );
}

```

Creating routes
---------------

The `TabList` contains all the routes available within the tab navigator. It must be an immediate child of `Tabs`. Each route is defined by a `TabTrigger` within the `TabList`. A `TabTrigger` within a `TabList` must include a `name` and a `href` prop.

Typically, the `TabList` defines both the available tab routes and the appearance of the tabs, with the children of each `TabTrigger` defining the appearance of each tab button.

> Note: A `name` can be any `string`. This is a user-defined name for the Tab.

### Dynamic routes

Dynamic routes are allowed and can be provided with values via the `href`.

`_layout.tsx`

`[slug].tsx`

The trigger `<TabTrigger name="dynamic page" href="/hello-world" />` will create a tab for [slug].tsx with the params `{ slug: 'hello-world' }`. This setup can be useful for displaying an arbitrary number of tabs in the tab bar, based on end-user data, such as showing a separate tab for each user profile in an app.

### Ambiguous routes

`_layout.tsx`

`(one,two)`

â`route.tsx``A route within a shared group`

The `href` values provided to `TabTrigger` must always point to a single route. In the above example of a shared route, href `/route` is not allowed, as it could refer to either `/(one)/route` or `/(two)/route`. However, specifying the route group within the href would work (for example,`href="/(one)/route"`).

### Nested routes

`_layout.tsx`

`(stack-one)`

â`_layout.tsx``A <Stack> layout`

â`(stack-two)`

ââ`_layout.tsx``Nested <Stack> layout`

ââ`route.tsx`

A `TabTrigger` can link to a deeply nested route. `<TabTrigger name="route" href="/route" />` will show the (stack-one)/(stack-two)/route.tsx route. This tab will be controlled by that route's parent navigator (that is, the navigator within stack-two\_layout.tsx). This navigation is similar to a deep link.

Rendering routes
----------------

The `TabSlot` component renders the current route. `TabSlot` can be nested inside other components within `Tabs` but cannot be within the `TabList`.

app/\_layout.tsx

Copy

```
<Tabs>
  <TabList>
    <TabTrigger name="home" href="/">
      <Text>Home</Text>
    </TabTrigger>
  </TabList>
  {/* Customize how `<TabSlot />` is rendered. */}
  <View>
    <View>
      <TabSlot />
    </View>
  </View>
</Tabs>

```

Switching tabs
--------------

Tabs can be switched via a `Link` or using the imperative APIs. However, these APIs will always perform a navigation action (they will switch tabs and might change the URL). To switch tabs without performing any navigation, you should use a `TabTrigger`. A `TabTrigger` is an unstyled `<View>` that will switch tabs when pressed, much like how text and components can be wrapped in `Link` to make them pressable navigation elements.

### Resetting navigation

The `reset` prop from `TabTrigger` can be used to control when a tab resets its navigation state. The options are `always`, `onLongPress` and `never`. This is particularly useful for a stack navigator nested inside a tab. For example, `<TabTrigger name="home" reset="always" />` will return the user to the index route inside a tab's nested stack navigator.

TabTrigger
----------

The `TabTrigger` is used to switch tabs, but also has a dual role of defining what routes are available as a tab.

### Within TabList

When a `TabTrigger` is used as a child of `TabList`, that defines what routes are available within the tab navigator. These `TabTrigger` need to include both the `name` and `href` props, as they define the URL for that tab and a custom name that can be used to refer to the tab. If the `TabTrigger` components also contain text or other components as children, then those will also render as the tab buttons. However, you can define the `TabTrigger`'s within the `TabList` without any UI, and they can then be invoked by `TabTrigger`'s outside of the `TabList`.

### Outside TabList

An additional `TabTrigger` can be defined outside of a `TabList`, allowing you to perform the same action as the `TabTrigger` that is defined in the `TabList`. In this case, the `TabTrigger` will not have an `href` prop. Rather, it will perform the same action as the primary `TabTrigger` with the same `name` prop. This allows you to create components that can switch tabs and be agnostic to your current navigation state. Note that all `TabTrigger`'s need to at least be descendants of the `Tabs` component, or else they will be considered to be outside the tab navigator and unable to invoke it.

Customizing appearance
----------------------

All components are rendered unstyled as a `<View>`, except `TabTrigger` which renders as a `<Pressable>`. This allows you to provide a custom `style` prop to customize their appearance. Styling `TabList` is similar to customizing the tab bar in React Navigation, while styling `TabTrigger` affects the appearance of tab buttons.

If you need to change the structure of a component, you can override its underlying component by using the `asChild` props. The component then acts as a slot, and will forward its props to its immediate child.

Custom TabList

Copy

```
<Tabs>
  <TabSlot />
  <TabList asChild>
    {/* Render a custom TabList */}
    <CustomTabList>
      <TabTrigger name="home" href="/">
        <Text>Home</Text>
      </TabTrigger>
    </CustomTabList>
  </TabList>
</Tabs>

```

Custom Button

Copy

```
<Tabs>
  <TabSlot />
  <TabList asChild>
    <TabTrigger name="home" href="/" asChild>
      {/* Render a custom button */}
      <CustomButton>
        <Text>Home</Text>
      </CustomButton>
    </TabTrigger>
  </TabList>
</Tabs>

```

### Multiple tab bars

The `TabList` is both the configuration and default appearance of the `Tabs`, but it is not the only way to render a tab bar. By hiding the `TabList`, you can construct custom tab bars using `TabTrigger`.

Multiple tab bars example

Copy

```
<Tabs>
  <TabSlot />
  {/* A custom tab bar */}
  <View>
    <View>
      <TabTrigger name="home">
        <Text>Home</Text>
      </TabTrigger>
      <TabTrigger name="article">
        <Text>article</Text>
      </TabTrigger>
    </View>
  </View>
  <TabList style={{ display: 'none' }}>
    <TabTrigger name="home" href="/">
      <Text>Home</Text>
    </TabTrigger>
    <TabTrigger name="article" href="/article">
      <Text>article</Text>
    </TabTrigger>
  </TabList>
</Tabs>

```

`TabTrigger` will forward an `isFocused` prop, so you can create a separate tab button component that reacts to focused status.

TabButton.tsx

Copy

```
import FontAwesome from '@expo/vector-icons/FontAwesome';
import { TabTriggerSlotProps } from 'expo-router/ui';
import { ComponentProps, Ref, forwardRef } from 'react';
import { Text, Pressable, View } from 'react-native';

type Icon = ComponentProps<typeof FontAwesome>['name'];

export type TabButtonProps = TabTriggerSlotProps & {
  icon?: Icon;
  ref: Ref<View>;
};

export function TabButton({ icon, children, isFocused, ...props }: TabButtonProps) {
  return (
    <Pressable
      {...props}
      style={[
        {
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          flexDirection: 'column',
          gap: 5,
          padding: 10,
        },
        isFocused ? { backgroundColor: 'white' } : undefined,
      ]}>
      <FontAwesome name={icon} />
      <Text style={[{ fontSize: 16 }, isFocused ? { color: 'white' } : undefined]}>{children}</Text>
    </Pressable>
  );
}

```

Expo SDK 52 / React 18 and below

In Expo SDK 52 and below (React 18), use the legacy `forwardRef` function to access the `ref` handle.

```
- export function TabButton({ ref }) {
+ export const TabButton = forwardRef((props: TabButtonProps, ref: Ref<View>) => {

```

### Hooks

All components also have a hook version giving you control over the render tree. See the [Router UI Reference](/versions/latest/sdk/router-ui) for a full list of the hooks available.

Using hooks is considered advanced usage of this library. For most use-cases, using the components with `asChild` should give you enough control over the render tree.

If you are developing a custom `<TabTrigger />`, you may also need to develop a custom `<TabList />` as `<TabList />` uses the [`useTabsWithChildren()`](/versions/latest/sdk/router-ui#usetabswithchildrenoptions) which requires using the exported `<TabTrigger />` component.

### Customizing how tab screens are rendered

The `TabSlot` accepts a `renderFn` property. This function can be used to override how your screen is rendered, allowing you to implement advanced functionality such as animations or persisting/unmounting screens. See the [Router UI Reference](/versions/latest/sdk/router-ui) for more information.

Common questions
----------------

How do I create multiple tabs for the same route?

`_layout.tsx``Tabs layout`

`(movie,tv)`

â`[id].tsx`

You should add the route to a shared group and create a separate `TabTrigger` for each group `group`.

How do I hide a tab?

Not rendering the `TabTrigger` will remove that tab (and its navigation state) from your app.

How do I create animated tabs?

You can provide a custom renderer to `TabSlot` to customize how it renders a screen. You can use this to detect when screen is focused an animate appropriately.

Can I use relative hrefs?

`directory`

â`_layout.tsx``The local pathname is /directory`

â`page.tsx``The pathname is /directory/page`

â`profile.tsx``The pathname is /directory/page`

A `TabTrigger` with a relative href is relative to the local path name `Tabs` was rendered on. This is different from normal relative hrefs which are relative to the current displayed route. For example, the `<TabTrigger href="./profile" />` will resolve to `/directory/profile`, even when the `/directory/page` route is showing. Expo recommends against using relative hrefs.

[Previous (Expo Router - Advanced)

Apple Handoff](/router/advanced/apple-handoff)[Next (Expo Router - Reference)

Error handling](/router/error-handling)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/advanced/custom-tabs.mdx)
* Last updated on April 26, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Anatomy of custom Tabs components](/router/advanced/custom-tabs/#anatomy-of-custom-tabs-components)[Creating routes](/router/advanced/custom-tabs/#creating-routes)[Dynamic routes](/router/advanced/custom-tabs/#dynamic-routes)[Ambiguous routes](/router/advanced/custom-tabs/#ambiguous-routes)[Nested routes](/router/advanced/custom-tabs/#nested-routes)[Rendering routes](/router/advanced/custom-tabs/#rendering-routes)[Switching tabs](/router/advanced/custom-tabs/#switching-tabs)[Resetting navigation](/router/advanced/custom-tabs/#resetting-navigation)[TabTrigger](/router/advanced/custom-tabs/#tabtrigger)[Within TabList](/router/advanced/custom-tabs/#within-tablist)[Outside TabList](/router/advanced/custom-tabs/#outside-tablist)[Customizing appearance](/router/advanced/custom-tabs/#customizing-appearance)[Multiple tab bars](/router/advanced/custom-tabs/#multiple-tab-bars)[Hooks](/router/advanced/custom-tabs/#hooks)[Customizing how tab screens are rendered](/router/advanced/custom-tabs/#customizing-how-tab-screens-are-rendered)[Common questions](/router/advanced/custom-tabs/#common-questions)