Create app store assets - Expo Documentation

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

Create app store assets
=======================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/store-assets.mdx)

Learn how to create screenshots and previews for your app's store pages.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/store-assets.mdx)

---

Before submitting your app to the Google Play Store and Apple App Store, you need to provide some assets for your store listing page. The goal of these images and videos is to give your prospective users an idea of what your app experience is going to be like.

You will need to upload app screenshots for both app stores. Even though they are called "app screenshots" on both stores, they *do* have to include accurate visuals of your app. There is no rule citing that these images have to be screenshots taken on specific devices.

Both app stores have requirements on image format and size. However, within these restrictions, you can be creative. For example, a common approach is to design the assets using a design tool such as Figma and incorporate actual app screenshots (or designs) with supplementary messaging.

Different approaches for creating "screenshots"
-----------------------------------------------

There are three commonly used approaches to creating your store screenshots. You can choose whichever approach works best for your app's needs and resources.

### Option 1: actual screenshots

The most straightforward option â open up your app on a real device and take screenshots.

Pros: Straightforward to do. Most accurate representation of your app.

Cons: Need to load the app on different devices for a full range of screenshots.

![Screenshots of the Expo Go Apple App Store Listing Page](/static/images/guides/expo-go-screenshots.png)

Screenshots of the Expo Go Apple App Store Listing Page.

### Option 2: screenshots within a design

The majority of apps use this approach. It involves taking screenshots of the app (or in some cases, using existing designs instead of actual screenshots) and embedding them in the store assets along with appropriate messaging.

Pros: Allows to convey additional messaging within the assets.

Cons: The assets need to be created using a design program.

![Screenshots of the Brex Apple App Store Listing Page](/static/images/guides/brex-screenshots.png)

Screenshots of the Brex Apple App Store Listing Page.

### Option 3: make it fancy

In this option, on the app store pages, you can incorporate elements of your app design and creative messaging to highlight your product.

Pros: You can make your store page creative and fun.

Cons: Need an experienced designer to create and maintain the assets.

![Screenshots of the MS Office Apple Store Listing Page](/static/images/guides/office-screenshots.png)

Screenshots of the MS Office Apple Store Listing Page.

Google Play Store Asset Requirements
------------------------------------

Google has specific requirements for the store asset format and dimensions, which are different from Apple's. For the most up-to-date specifications, see [official documentation](https://support.google.com/googleplay/android-developer/answer/9866151) for detailed requirements for your Google Play Store assets.

[Store assets Figma template

See our template for a summary of the minimum asset requirements.](https://www.figma.com/community/file/1352686667495694112)

### App icon

Unlike on the Apple App Store, where the app icon is always taken automatically from the app bundle, on the Google Play Store, you must also upload a separate App Icon for your store listing.

### Feature graphic

A feature graphic must be provided to publish your Store Listing. It is a banner that is displayed at the top of your store listing page.

### Screenshots

You need to upload at least four screenshots to publish your app.

### Video (optional)

You can add one preview video to your Store Listing. The video needs to be uploaded to YouTube, and you can add it by entering a YouTube URL in the preview video field.

iOS App Store Asset Requirements
--------------------------------

For the iOS App Store, you can upload screenshots (images) and previews (videos). For each, Apple requires specific widths and heights. Make sure to reference the [Screenshot specifications from Apple](https://developer.apple.com/help/app-store-connect/reference/screenshot-specifications/) for the exact sizing. Even a single pixel-off will mean you cannot submit the images.

[Store assets Figma template

See our template for a summary of the minimum asset requirements.](https://www.figma.com/community/file/1352686667495694112)

### Screenshots

At a minimum, Apple requires you to upload screenshots for iPhone with the dynamic island (6.9 inch). You can optionally upload additional screenshots for other screen sizes. If specific screenshots are not provided, scaled down screenshots from the closest uploaded size will be used instead.

If your app runs on iPad, you must also provide one set of iPad screenshots (13 inch).

You can upload up to ten screenshots per localization. If your app is available in multiple languages and your screenshots include text, you should upload screenshots with the appropriate language for each localization.

Screenshots can be portrait or landscape.

### Preview (optional)

You can include An app preview video to demonstrate how your app works. You can add up to three app previews for each screen size.

See [App Preview Specifications](https://developer.apple.com/help/app-store-connect/reference/app-preview-specifications/) from Apple documentation for a summary of video size and format.

Bare minimum
------------

Below is the bare minimum needed to publish your apps.

### Play Store - Android

| Type | Amount | Dimensions | Requirements |
| --- | --- | --- | --- |
| App Icon | 1 | 512 Ã 512 | 32-bit PNG (with alpha); Maximum file size: 1024 KB |
| Feature Graphic | 1 | 1024 Ã 500 | JPEG or 24-bit PNG (no alpha) |
| Screenshots | 4-10 | minimum: 1024 Ã 500 maximum width: 3840px 9:16 aspect ratio | JPEG or 24-bit PNG (no alpha) |

### App Store - iPhone

| Type | Amount | Dimensions (coose one) | Requirements |
| --- | --- | --- | --- |
| Screenshots (iPhone with the dynamic island) | 2-10 | 1320 Ã 2868 1290 Ã 2796 | JPG or PNG (no alpha) |

### App Store - iPad

If your app also runs on an iPad, you need to supply additional screenshots.

| Type | Amount | Dimensions (choose one) | Requirements |
| --- | --- | --- | --- |
| Screenshots | 2-10 | 2064 Ã 2752 2048 Ã 2732 | JPG or PNG (no alpha) |

[Previous (More - Assorted)

Edit rich text](/guides/editing-richtext)[Next (More - Assorted)

Local-first](/guides/local-first)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/store-assets.mdx)
* Last updated on November 14, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Different approaches for creating "screenshots"](/guides/store-assets/#different-approaches-for-creating-screenshots)[Option 1: actual screenshots](/guides/store-assets/#option-1-actual-screenshots)[Option 2: screenshots within a design](/guides/store-assets/#option-2-screenshots-within-a-design)[Option 3: make it fancy](/guides/store-assets/#option-3-make-it-fancy)[Google Play Store Asset Requirements](/guides/store-assets/#google-play-store-asset-requirements)[App icon](/guides/store-assets/#app-icon)[Feature graphic](/guides/store-assets/#feature-graphic)[Screenshots](/guides/store-assets/#screenshots)[Video (optional)](/guides/store-assets/#video-optional)[iOS App Store Asset Requirements](/guides/store-assets/#ios-app-store-asset-requirements)[Screenshots](/guides/store-assets/#screenshots-1)[Preview (optional)](/guides/store-assets/#preview-optional)[Bare minimum](/guides/store-assets/#bare-minimum)[Play Store - Android](/guides/store-assets/#play-store---android)[App Store - iPhone](/guides/store-assets/#app-store---iphone)[App Store - iPad](/guides/store-assets/#app-store---ipad)