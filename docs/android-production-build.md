Create a production build for Android - Expo Documentation

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

Create a production build for Android
=====================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/tutorial/eas/android-production-build.mdx)

Learn about the process of creating a production build for Android and automating the release process.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/tutorial/eas/android-production-build.mdx)

---

In this chapter, we'll create our example app's production version and submit it to the Google Play Store. We'll also explore how to automate the creation and release of new app versions.

[![Watch: Creating and releasing a production build for Android](https://i3.ytimg.com/vi/nxlt8uwqhpE/maxresdefault.jpg)

Watch: Creating and releasing a production build for Android](https://www.youtube.com/watch?v=nxlt8uwqhpE)


---

Prerequisites
-------------

To publish and distribute an app on the Google Play Store, we need:

* Google Play Developer Account: Must have a paid developer account. For details on setting one up, visit the [Google Play sign-up page](https://play.google.com/apps/publish/signup/).
* Google Service Account key: We'll need a Google Service Account email and JSON key to automate the app submission process. Follow the detailed instructions in our guide on [creating a Google Service Account key or downloading it from an existing account](https://expo.fyi/creating-google-service-account) , then return to this guide. This is optional but required for [automating the release process](/tutorial/eas/android-production-build#automated-release).
* Production build profile: Ensure that a `production` build profile is present in your eas.json, which is added by default.

Production build for Android
----------------------------

A [production Android build](/build/eas-json#production-builds) has a .aab format which is optimized for distribution on the Google Play Store. Unlike .apk builds, .aab files can only be distributed and installed through the Google Play Store.

1

Create a production build
-------------------------

To create an Android production build using the default `production` profile, open your terminal and execute the following command. Since `production` is set as the default profile in the EAS configuration, there is no need to specify it explicitly with the `--profile` flag.

Terminal

Copy

`-Â``eas build --platform android`

The above command will queue the build. Notice in the Expo dashboard that the Version Code is auto-incremented.

2

Create an app on the Google Play Console
----------------------------------------

To upload the app to the Google Play Store for the first time, we need to:

* Go to the Google Play dashboard.
* On the Home page, click Create app to make a new app.

![Create app on Google Play Console](/static/images/tutorial/eas/play-store-01.png)

* Fill out our app details and click the Create app button.

![Create app form on Google Play Console](/static/images/tutorial/eas/play-store-02.png)

3

Release an internal testing version
-----------------------------------

After the app is created on Google Play Console, it redirects us to the app's Dashboard screen. We need to prepare an internal test version of our app.

* Click Start testing now on the Dashboard.

![Steps under start testing now on Google Play Console](/static/images/tutorial/eas/play-store-03.png)

* Create an email list of users under Internal Testing > Testers for the internal testing release.

![Create an email list for internal testers](/static/images/tutorial/eas/play-store-04.png)

* Google Play Console prompts us to create a Release.
* To create a new release, go to Releases and click Create new release.

![Selecting the signing key for the app bundle](/static/images/tutorial/eas/play-store-05.png)

* To store the signing key, go to App integrity > App bundles and click Choose signing key > Use Google-generated key.

![Creating a new internal release](/static/images/tutorial/eas/play-store-06.png)

4

Upload the app binary
---------------------

After EAS has created a production build:

* Open the EAS dashboard and click on Download to get the .aab file.

![Downloading the aab file](/static/images/tutorial/eas/play-store-07.png)

* Return to the Google Play Console and go to App bundles. Click on Upload to add the .aab.
* Provide the release details for our app and click on Next.
* On the following screen, click on Save and publish.

![Uploading aab file to Google Play Console](/static/images/tutorial/eas/play-store-08.png)

5

Share the internal release version
----------------------------------

Under Track Summary, we see that the latest release shows a temporary app name. This is because our app is not reviewed yet.

![App pending review on Google Play Console](/static/images/tutorial/eas/play-store-09.png)

Under Releases, we see that the app is available to internal testers. To share the app with a team of testers:

* Open the Internal testing dashboard, then click on View release details.
* Click on copy link under How testers join your test.

![Sharing the internal release version](/static/images/tutorial/eas/play-store-14.png)

* On the device, open the test email and follow the steps to download the app.

![Downloading app on the device as an internal tester](/static/images/tutorial/eas/play-store-15.png)

* The testing email holder needs to accept the invite, and once accepted, the app can be installed on the device.

![On accepting the invite, the app can be installed on the device](/static/images/tutorial/eas/play-store-16.png)![App installed on the device as an internal tester](/static/images/tutorial/eas/play-store-17.png)
> Tip: To publish an app on the Play Store, in the Google Dashboard, finish the steps under Set up your app. These steps are required before releasing the app on the Play Store for the first time. You'll have to provide details like a link to a privacy policy, a target audience, data safety and so on.

> Complete app store listing: To prepare the app for store listing, see [Create app store assets](/guides/store-assets) on how to create screenshots and previews.

Promoting a testing release

To promote our internal test release version to alpha, in Google Play Store Console:

* Go to internal testing and click Promote release.
* Open the dropdown menu and click Closes testing > Closed testing - Alpha.

6

Add Google Service Account permissions key
------------------------------------------

> Tip: Before following the steps in this section, see the instructions on [creating a Google Service Account key or downloading it from an existing account](https://expo.fyi/creating-google-service-account)  guide.

From now on, we can use [EAS Submit](/submit/introduction) to automate releases and avoid the manual process. To do that, we need to add the service account key to our project's eas.json.

After following the Google Service Account guide steps, we can use the downloaded JSON key:

* Open our project and copy the JSON file from the Google Service Account to the project's root directory.
* To secure sensitive data, ensure this file is excluded from version control by listing it in our .gitignore.

7

Internal release
----------------

Let's add the path to the Google Service Account file path in eas.json.

* Under `submit.production` profile, add `android.serviceAccountKeyPath` and the relative file path as its value:

```
{
  %%placeholder-start%%... %%placeholder-end%%
  "submit": {
    "production": {
      "android": {
        "serviceAccountKeyPath": "./service-account-file.json",
        "track": "internal"
      }
    }
  }
}

```

In the above snippet, we're also adding [`track`](/eas/json#track) property and setting its value to `internal`. This will enable the `eas submit` command to upload our production build and release it for internal testing on the Google Play Store.

* Now run the `eas submit` command to release a new internal testing version:

Terminal

Copy

`-Â``eas submit --platform android`

* This command will automatically create a new internal release version in Google Play Console:

![Automatic internal release version created in Google Play Console by EAS Submit](/static/images/tutorial/eas/play-store-18.png)

8

Production release
------------------

To release the app for production:

* Change the value for `track` to `production` in eas.json:

```
{
  %%placeholder-start%%... %%placeholder-end%%
  "submit": {
    "production": {
      "android": {
        "serviceAccountKeyPath": "./service-account-file.json",
        "track": "production"
      }
    }
  }
}

```

* We can also use the same EAS Build we did for the internal testing release. Run the `eas submit` command to release to the Play Store:

Terminal

Copy

`-Â``eas submit --platform android`

* To create a track and submit our app to the Google Play Store's review process, we need to Release > Production and under Releases, select the build we want to send for review.

![Submitting app for Google Play Store review process](/static/images/tutorial/eas/play-store-19.png)

9

Automated release
-----------------

For subsequent releases in future, we can streamline the process by combining build creation and Play Store submission into a single step by using the [`--auto-submit`](/build/automate-submissions) flag with `eas build`:

Terminal

Copy

`-Â``eas build --platform android --auto-submit`

Summary
-------

Chapter 8: Create a production build for Android

We successfully created a production-ready Android build, discussed manual and automated uploading to Google Play Store using `eas submit`, and automated the release process with the `--auto-submit`.

Mark this chapter as read

In the next chapter, learn about the process of creating a production build for iOS.

[Next: Create a production build for iOS](/tutorial/eas/ios-production-build)

[Previous (EAS tutorial)

Manage app versions](/tutorial/eas/manage-app-versions)[Next (EAS tutorial)

iOS production build](/tutorial/eas/ios-production-build)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/tutorial/eas/android-production-build.mdx)

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Prerequisites](/tutorial/eas/android-production-build/#prerequisites)[Production build for Android](/tutorial/eas/android-production-build/#production-build-for-android)[Create a production build](/tutorial/eas/android-production-build/#create-a-production-build)[Create an app on the Google Play Console](/tutorial/eas/android-production-build/#create-an-app-on-the-google-play-console)[Release an internal testing version](/tutorial/eas/android-production-build/#release-an-internal-testing-version)[Upload the app binary](/tutorial/eas/android-production-build/#upload-the-app-binary)[Share the internal release version](/tutorial/eas/android-production-build/#share-the-internal-release-version)[Add Google Service Account permissions key](/tutorial/eas/android-production-build/#add-google-service-account-permissions-key)[Internal release](/tutorial/eas/android-production-build/#internal-release)[Production release](/tutorial/eas/android-production-build/#production-release)[Automated release](/tutorial/eas/android-production-build/#automated-release)[Summary](/tutorial/eas/android-production-build/#summary)