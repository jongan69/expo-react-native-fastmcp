Edit rich text - Expo Documentation

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

Edit rich text
==============

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/editing-richtext.mdx)

Learn about current approaches to preview and edit rich text in React Native.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/editing-richtext.mdx)

---

A lot of applications need to allow users to type in text. For example, if you want to build a messaging or social media app, you will probably rely heavily on text inputs. React Native has a built-in `<TextInput>` component to implement this without much effort for many simple cases.

However, sometimes you need to be more flexible. Think of long social media posts, note apps, or document editors. Ideally, you need to allow different text styles, lists, headings, embedded images, and more. This is called a rich text editor, and it's a difficult problem to solve everywhere, including in React Native.

There is currently no default solution for that in the React Native ecosystem. However, this guide explores some options and promising approaches, each with its own tradeoffs.

[![Watch: How to implement a Rich Text Editor using DOM components](https://i3.ytimg.com/vi/CxORa1tXMjw/maxresdefault.jpg)

Watch: How to implement a Rich Text Editor using DOM components](https://www.youtube.com/watch?v=CxORa1tXMjw)

Render rich text
----------------

There are a lot of good options to display rich text:

* For markdown content, you can use a markdown renderer such as [`react-native-markdown-display`](https://www.npmjs.com/package/react-native-markdown-display) or another.
* For HTML content, you can use [`@expo/html-elements`](https://www.npmjs.com/package/@expo/html-elements) or a webview ([`react-native-webview`](/versions/latest/sdk/webview)).
* To have a custom format and more control, you can take advantage of nesting `<Text>` components to render styles and layouts.

  ```
  <TextInput>
    <Text>
      <Text style={{ fontWeight: 900 }}>Some bold text</Text>Some regular text
    </Text>
  </TextInput>

  ```
* You can also use [Expo Modules](/modules/overview) to write a custom renderer component with native platform primitives using third-party libraries such as [Markwon](https://github.com/noties/Markwon) on Android and `AttributedString` on iOS.

Approaches to edit rich text
----------------------------

There are a few approaches to get rich text rendering to work. However, all have different limitations.

### Webview-based editors

While most React Native UI components wrap native platform primitives and are fast, performant, and native feeling as a result, the webview-based rich text editors use a different approach.

They wrap an existing rich text editor built for web with JavaScript inside a [`react-native-webview`](/versions/latest/sdk/webview). It works on all platforms (Android, iOS, Web) and can take advantage of popular rich text editors available for the Web platform, but it has a performance and UX penalty.

You will not be able to use native UI components inside the editor. Any implementation of features like mentions or image embedding will duplicate features and require significant effort to implement.

### Existing webview-based React Native libraries

There are a couple of existing React Native libraries to allow rich-text editing. These are the easiest options to get started if you need a basic rich text editor with limited configuration and don't have strict performance or UX requirements:

* [`react-native-rich-editor`](https://github.com/wxik/react-native-rich-editor)
* [`react-native-cn-quill`](https://github.com/imnapo/react-native-cn-quill)
* [`@10play/tentap-editor`](https://github.com/10play/10Tap-Editor)

### Custom webview-based editor

If you need more configurability, you can build a similar library with an existing web-only editor. However, you have to handle the message passing and web implementation yourself. This gives you all the options that the underlying editor offers and lets you implement more features.

* [Quill](https://quilljs.com/)
* [lexical](https://github.com/facebook/lexical)
* [slate](https://github.com/ianstormtaylor/slate)

You will need to use message passing to pass text and `onChange` events to and from the webview. Since rich texts often end up long, it's better to model it as an uncontrolled component to prevent lag on each keystroke. Also, if you can avoid serializing and sending the entire state on each keystroke that also improves performance.

Building on top of React Native TextInput
-----------------------------------------

In this section, let's discuss if it is possible to have a feature complete rich text input for general purposes.

React Native allows nested `<Text>` components and allows them to be used as children of `<TextInput>` to render and edit styled text. It is synchronous with the new React Native architecture (the `onChange` event fires immediately after a new character is typed into the text input field).

Unfortunately, the `<TextInput>` component is built towards working with regular text, and it only returns a string in it's `onTextChange` callback. This is a significant limitation.

Here is a quick example. Let's start by rendering a text input with the following bold text:

```
<TextInput>
  <Text>
    {/* The following will render a bold text in this format: **aa**aa */}
    <Text style={{ fontWeight: 900 }}>aa</Text>aa
  </Text>
</TextInput>

```

Then, let's append a fifth letter `a` to the text input. The position of your cursor should determine if the new letter is a part of the bold string or not. Unfortunately, the callback only returns `aaaaa`.

There is an additional `onSelectionChange` prop that can be used to get that information. However, it makes the task significantly harder. Inserting additional characters (such as newlines for lists or bullet points) also desynchronizes the selection.

There are some attempts to build such an editor, such as [`markdown-editor`](https://github.com/shakogegia/markdown-editor) (not actively maintained) and [`rn-text-editor`](https://github.com/amjadbouhouch/rn-text-editor) (in beta), but no widely used packages exist.

Markdown editors with visible styling markers
---------------------------------------------

If using a markdown to style text fulfills your requirement, you can render the markdown in a separate, non-editable view while editing. It is not complex to build on your own using any markdown renderer. You can also use a third-party library such as [`react-native-markdown-editor`](https://github.com/kunall17/react-native-markdown-editor).

This editing experience suits power users or programming/tech applications. You can also explore rendering rich text while showing markdown only in the selected chunk of text or other hybrid approaches.

Native editors
--------------

You can use a native Android or iOS rich text editor wrapped into a React Native module. There are a few options:

* [`react-native-aztec`](https://github.com/WordPress/gutenberg/tree/trunk/packages/react-native-aztec)
* [`gutenberg-mobile`](https://github.com/wordpress-mobile/gutenberg-mobile)
* [`react-native-live-markdown`](https://github.com/Expensify/react-native-live-markdown)

You can also wrap any native rich text editor using [Expo Modules](/modules/overview), but if you use different ones on each platform, you need to unify their APIs and input formats.

> Rich text is usually represented using [abstract syntax trees](https://en.wikipedia.org/wiki/Abstract_syntax_tree). For example, a bullet list can be a node of type `bulleted-list` with several children of type `list-item`. You can convert both HTML and markdown to a suitable AST format.

There is also an effort to port the lexical editor to Android and iOS and provide a React Native wrapper, [track it here](https://github.com/facebook/lexical/discussions/2410).

Summary
-------

While there are many great options for showing rich text, there is no one-size-fits-all solution for rich text editing in React Native. There's no popular solution that is sufficient in most use cases. Further contribution from the community is needed to improve existing solutions or add new ones.

For now, you need to carefully choose between a more complex, native editor that offers more features but may be harder to maintain, or an editor built on top of react-native primitives. This depends on how core the feature is to your app, how many features you need in your editor, and how much effort you are willing to spend on building it out.

[Previous (More - Assorted)

Using Bun](/guides/using-bun)[Next (More - Assorted)

App store assets](/guides/store-assets)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/editing-richtext.mdx)
* Last updated on December 30, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Render rich text](/guides/editing-richtext/#render-rich-text)[Approaches to edit rich text](/guides/editing-richtext/#approaches-to-edit-rich-text)[Webview-based editors](/guides/editing-richtext/#webview-based-editors)[Existing webview-based React Native libraries](/guides/editing-richtext/#existing-webview-based-react-native-libraries)[Custom webview-based editor](/guides/editing-richtext/#custom-webview-based-editor)[Building on top of React Native TextInput](/guides/editing-richtext/#building-on-top-of-react-native-textinput)[Markdown editors with visible styling markers](/guides/editing-richtext/#markdown-editors-with-visible-styling-markers)[Native editors](/guides/editing-richtext/#native-editors)[Summary](/guides/editing-richtext/#summary)