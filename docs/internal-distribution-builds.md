Create and share internal distribution build - Expo Documentation

[Docs](/)

[Blog](https://expo.dev/blog)[Changelog](https://expo.dev/changelog)[Star Us on GitHub](https://github.com/expo/expo)

Search

[Home](/)[Guides](/guides/overview)[EAS](/eas)[Reference](/versions/latest)[Learn](/tutorial/overview)

[Overview](/tutorial/overview)

Expo tutorial

0 of 9

[Introduction](/tutorial/introduction)[Create your first app](/tutorial/create-your-first-app)[Add navigation](/tutorial/add-navigation)[Build a screen](/tutorial/build-a-screen)[Use an image picker](/tutorial/image-picker)[Create a modal](/tutorial/create-a-modal)[Add gestures](/tutorial/gestures)[Take a screenshot](/tutorial/screenshot)[Handle platform differences](/tutorial/platform-differences)[Configure status bar, splash screen and app icon](/tutorial/configuration)[Learning resources](/tutorial/follow-up)

EAS tutorial

0 of 11

[Introduction](/tutorial/eas/introduction)[Configure development build](/tutorial/eas/configure-development-build)[Android development build](/tutorial/eas/android-development-build)[iOS development build for simulators](/tutorial/eas/ios-development-build-for-simulators)[iOS development build for devices](/tutorial/eas/ios-development-build-for-devices)[Multiple app variants](/tutorial/eas/multiple-app-variants)[Internal distribution build](/tutorial/eas/internal-distribution-builds)[Manage app versions](/tutorial/eas/manage-app-versions)[Android production build](/tutorial/eas/android-production-build)[iOS production build](/tutorial/eas/ios-production-build)[Share previews](/tutorial/eas/team-development)[Builds from GitHub](/tutorial/eas/using-github)[Next steps](/tutorial/eas/next-steps)

More

[Additional resources](/additional-resources)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Create and share internal distribution build
============================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/tutorial/eas/internal-distribution-builds.mdx)

Learn about internal distribution builds, why we need them, and how to create them.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/tutorial/eas/internal-distribution-builds.mdx)

---

In this chapter, we'll learn how to set up [internal distribution builds](/build/internal-distribution#internal-distribution).

[![Watch: How to create and share an internal distribution build](https://i3.ytimg.com/vi/1fQuGLHxWks/maxresdefault.jpg)

Watch: How to create and share an internal distribution build](https://www.youtube.com/watch?v=1fQuGLHxWks)


---

Internal distribution build
---------------------------

Internal distribution builds are ideal for sharing updates with team members, allowing both technical and non-technical stakeholders to provide feedback directly. Unlike development builds, these do not require running a development server, simplifying the testing process.

### Ways to distribute an app internally

Both Google and Apple provide built-in mechanisms for sharing apps internally:

* Android: Using Google Play beta
* iOS: Using TestFlight

However, both of these traditional methods have their limitations. For example, TestFlight limits to one active build at a time.

### EAS Build for faster distribution

EAS Build speeds up the process. It creates shareable links for our builds and provides instructions on using them. It has a default configuration designed to facilitate internal distribution, offering a more efficient alternative to traditional methods.

Create an internal distribution build
-------------------------------------

To create and distribute a build with EAS Build, we need to follow these steps:

1

### Configure preview build profile

From our initial setup in eas.json, we already have a default configuration that includes a `preview` build profile designed for internal distribution:

eas.json

Copy

```
{
  "build": {
    "preview": {
      "distribution": "internal"
    }
  }
}

```

This is all we need to create our first internal distribution build. The `preview` build profile from the above snippet has a `distribution` property whose value is set to `internal`. This value allows us to share our build URLs with anyone so they can install it on their device and do not require a development server to run the app.

As discussed in the previous chapters, for non-app store builds, Android requires .apk and iOS needs .ipa formats. This applies to internal distribution builds as well. The `distribution` when set to `internal`, automatically creates the app binary in these file formats for devices.

2

### Create

Creating an internal distribution build requires [app signing credentials](/app-signing/app-credentials).

Android app signing is non-restrictive and allows installing any compatible .apk file. When a development build was created, a new Android Keystore was generated for it. Hence, there is no need to generate a new keystore for preview builds.

On the other hand, Apple has stricter rules for app distribution on iOS devices. We need an ad hoc provisioning profile that explicitly lists the devices allowed to run the app. Some organizations whose apps meet specific requirements may be able to use the [Apple Developer Enterprise Program](https://developer.apple.com/programs/enterprise/) to distribute apps internally to a larger audience.

Android

iOS

* Use the `preview` profile to initiate an Android build:

Terminal

Copy

`-Â``eas build --platform android --profile preview`

* This command triggers the EAS Build, and on the Expo dashboard, we can see the build's progress:

![Android preview build details and progress in Expo dashboard](/static/images/tutorial/eas/android-preview-build.png)

Apps signed with an ad hoc provisioning profile can be installed by an iOS device whose UDID is registered with the provisioning profile.

* To register more devices, use `eas device:create`. This command registers an iOS device and gives us a URL or QR code to share for device registration:

Terminal

Copy

`-Â``eas device:create`

* This command registers an iOS device for app installation, generating a shareable URL (or QR code) for device registration.

  > Tip: This command enables device registration at any time. However, only builds created post-registration will work on the newly added device.
* To create the preview build, we need to use the `preview` profile with the `eas build` command:

Terminal

Copy

`-Â``eas build --platform ios --profile preview`

* This command triggers the EAS Build, and on the Expo dashboard, we can see the build's progress:

![iOS preview build details and progress in Expo dashboard](/static/images/tutorial/eas/ios-preview-build.png)Alternative method to register devices using `eas build:resign`

[`eas build:resign`](/app-signing/app-credentials#re-signing-new-credentials) command can be used to re-sign an existing iOS .ipa with a new ad hoc provisioning profile, eliminating the need for a full rebuild.

Are you setting up enterprise provisioning?

Apple Enterprise Program membership costs $299 USD per year and [not all organizations will be eligible](https://developer.apple.com/programs/enterprise/), so you will likely be using ad hoc provisioning, which works with any normal paid Apple Developer account.

If you have an [Apple Developer Enterprise Program membership](https://developer.apple.com/programs/enterprise/) users can install your app to their device without pre-registering their UDID. They just need to install the profile to their device and they can then access existing builds. You will need to sign in using your Apple Developer Enterprise account during the `eas build` process to set up the correct provisioning.

If you distribute your app both through enterprise provisioning and the App Store, you will need to have a distinct bundle identifier for each context. We recommend either:

* In projects generated with Expo CLI, use [app.config.js to dynamically switch identifiers](/tutorial/eas/multiple-app-variants).
* In [existing React Native projects](/bare/overview), create a separate `scheme` for each bundle identifier and specify the scheme name in separate build profiles.

Are you using manual local credentials?

If so, make sure to point your credentials.json to an ad hoc or enterprise provisioning profile that you generate through the Apple Developer Portal (either update an existing credentials.json used for another type of distribution or replace it with a new one that points to the appropriate provisioning profile). Beware that EAS CLI does only a limited validation of your local credentials, and you will have to handle device UDID registration manually. Read more about [using local credentials](/app-signing/local-credentials).

3

### Install

Once the build finishes, the Build artifact section gets updated, indicating that the build is complete. This section provides the methods available for running the development build on an iOS device: Expo Orbit and Install button.

* Open the build's detail page. If you are sharing the build with someone else, you can send them the link to the build. They'll be able to open the build's detail page or build artifact details which include Expo Orbit.
* Connect the Android or iOS device to our machine using USB.
* Open the Orbit menu bar app.
* Select the Device in the Orbit app.
* Under Build artifact, click the Open with Orbit.

Alternate: Use Install and QR code

* Open the build's detail page. If you are sharing the build with someone else, you can send them the link to the build page. They'll be able to open it and see build artifact details which includes Expo Orbit.
* Click Install under the Build artifact section to display the Install on a test device popup.
* Copy the link from Send a link to a device section and send it to the test device.

![Internal distribution build details and install link in Expo dashboard](/static/images/tutorial/eas/distribution-link.png)

4

### Run

Tap the app icon on your device to start the preview build. There is no need for a development server.

Since we have already set up multiple app variants, we can see both the development and preview variants installed separately on our devices. For example:

* On Android:

![Internal distribution build details and install link in Expo dashboard for Android](/static/images/tutorial/eas/android-multi-variants-installed.png)

* On iOS:

![Internal distribution build details and install link in Expo dashboard for iOS](/static/images/tutorial/eas/ios-multi-variants-installed.png)

Summary
-------

Chapter 6: Create and share internal distribution build

We successfully created internal distribution builds for Android and iOS, used ad hoc provisioning for iOS, and installed multiple app variants on the same device.

Mark this chapter as read

In the next chapter, learn about developer-facing and user-facing app versions and how to manage them automatically.

[Next: Manage different app versions](/tutorial/eas/manage-app-versions)

[Previous (EAS tutorial)

Multiple app variants](/tutorial/eas/multiple-app-variants)[Next (EAS tutorial)

Manage app versions](/tutorial/eas/manage-app-versions)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/tutorial/eas/internal-distribution-builds.mdx)

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Internal distribution build](/tutorial/eas/internal-distribution-builds/#internal-distribution-build)[Ways to distribute an app internally](/tutorial/eas/internal-distribution-builds/#ways-to-distribute-an-app-internally)[EAS Build for faster distribution](/tutorial/eas/internal-distribution-builds/#eas-build-for-faster-distribution)[Create an internal distribution build](/tutorial/eas/internal-distribution-builds/#create-an-internal-distribution-build)[Configure preview build profile](/tutorial/eas/internal-distribution-builds/#configure-preview-build-profile)[Create](/tutorial/eas/internal-distribution-builds/#create)[Install](/tutorial/eas/internal-distribution-builds/#install)[Run](/tutorial/eas/internal-distribution-builds/#run)[Summary](/tutorial/eas/internal-distribution-builds/#summary)