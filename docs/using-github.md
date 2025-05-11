Trigger builds from a GitHub repository - Expo Documentation

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

Trigger builds from a GitHub repository
=======================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/tutorial/eas/using-github.mdx)

Learn about the process of triggering builds from a GitHub repository.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/tutorial/eas/using-github.mdx)

---

[Expo GitHub App](/build/building-from-github) automatically triggers builds from our GitHub projects with EAS. We can trigger builds for any build profile based on our development team's preferences. It also allows triggering builds for `git` push committed directly to a repository or a pull request.

In this chapter, we'll configure this functionality. We already have a GitHub repository for our example app to demonstrate this.

[![Watch: How to trigger builds from a GitHub repository](https://i3.ytimg.com/vi/fBLFEFC0ip0/maxresdefault.jpg)

Watch: How to trigger builds from a GitHub repository](https://www.youtube.com/watch?v=fBLFEFC0ip0)


---

1

Configure Expo GitHub app
-------------------------

To use this functionality, we need to connect our GitHub account:

* In the Expo dashboard, go to [expo.dev/settings](https://expo.dev/settings#connections), and under Connections > GitHub, click Connect. This opens the Connect GitHub accounts page.
* Click the Get started button which opens a popup to authorize the Expo GitHub app. Click Install and Authorize.
* Once the app is installed on our GitHub account, we need to link it to our Expo account. In the next popup, click Link installation.
* Once the account is linked, it will show under GitHub.

![Linked GitHub account shows in Expo dashboard](/static/images/tutorial/eas/github-01.png)

2

Connect the GitHub repository
-----------------------------

To enable triggering builds from a GitHub repository, we need to connect it to our project in the Expo dashboard:

* In Expo dashboard, go to Project > Configuration > GitHub.
* Under Connect a GitHub repository, we'll see a list of our GitHub repos. We need to connect the right one. In the example, we're searching for our repo sticker-smash.
* Click Connect for the project repository.

![List of GitHub repositories to connect to the project in Expo dashboard](/static/images/tutorial/eas/github-02.png)

3

Use default repository settings
-------------------------------

The Expo GitHub app needs to know where to find the source code of our project. By default, it selects the root directory using `/`. In our example project, the source code is also available in the root repository. We can leave this to default in the Expo dashboard.

4

Trigger a build using a GitHub PR label
---------------------------------------

The Expo GitHub app provides us [multiple options](/build/building-from-github#trigger-a-build-from-github) to trigger a build, such as:

* Manually from the Builds page for a specific platform
* Automatically when new code is pushed to the repository
* Automatically using GitHub PR labels

To automatically trigger a build using a GitHub PR label, we're going to utilize the third option from the list above:

* We need to specify the build image that we will be using. Open eas.json, and under the `development` profile, add [`android.image`](/eas/json#image) and [`ios.image`](/eas/json#image-1) properties and set their value to [`latest`](/build-reference/infrastructure#configuring-build-environment).

  eas.json

  Copy

  ```
  {
    "build": {
      "development": {
        %%placeholder-start%%... %%placeholder-end%%
        "android": {
          "image": "latest"
        },
        "ios": {
          "image": "latest"
        }
      }
    }
    %%placeholder-start%%... %%placeholder-end%%
  }

  ```
* Next, let's create a new branch called `dev`, and make a change in our app's JavaScript code. Then, commit the change, push the branch, and create a PR from that branch.
* In the PR link, under Labels, create a label called `eas-build-all:development`.

![Creating a label in a GitHub PR](/static/images/tutorial/eas/github-04.png)

* Click Create pull request button to create the PR. The Expo GitHub app will start the process of creating a development build.
* In the Expo dashboard, on the Builds page, we can verify that the builds for both Android and iOS are triggered.

![Builds triggered in the Expo dashboard for Android and iOS platforms](/static/images/tutorial/eas/github-06.png)

* If we check the details of an individual build, we can see under Created by that the build is created by the GitHub app.

![Individual build details in the Expo dashboard](/static/images/tutorial/eas/github-07.png)

Summary
-------

Chapter 11: Trigger builds from a GitHub repository

We successfully linked our GitHub account with Expo, connected our repository to our EAS project, and learned about automated development build creation using GitHub PR labels.

Mark this chapter as read

Learn about the next steps to use EAS.

[Next: Next steps in your journey with EAS](/tutorial/eas/next-steps)

[Previous (EAS tutorial)

Share previews](/tutorial/eas/team-development)[Next (EAS tutorial)

Next steps](/tutorial/eas/next-steps)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/tutorial/eas/using-github.mdx)

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Configure Expo GitHub app](/tutorial/eas/using-github/#configure-expo-github-app)[Connect the GitHub repository](/tutorial/eas/using-github/#connect-the-github-repository)[Use default repository settings](/tutorial/eas/using-github/#use-default-repository-settings)[Trigger a build using a GitHub PR label](/tutorial/eas/using-github/#trigger-a-build-using-a-github-pr-label)[Summary](/tutorial/eas/using-github/#summary)