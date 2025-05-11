Android Studio Emulator - Expo Documentation

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

[Work with monorepos](/guides/monorepos)[View logs](/workflow/logging)[Development and production modes](/workflow/development-mode)[Common development errors](/workflow/common-development-errors)[Android Studio Emulator](/workflow/android-studio-emulator)[iOS Simulator](/workflow/ios-simulator)[New Architecture](/guides/new-architecture)[React Compiler](/guides/react-compiler)

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

Integrations

Troubleshooting

Regulatory compliance

[Data and Privacy protection](/regulatory-compliance/data-and-privacy-protection)[GDPR compliance](/regulatory-compliance/gdpr)[HIPAA compliance](/regulatory-compliance/hipaa)[Privacy Shield](/regulatory-compliance/privacy-shield)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Android Studio Emulator
=======================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/workflow/android-studio-emulator.mdx)

Learn how to set up the Android Emulator to test your app on a virtual Android device.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/workflow/android-studio-emulator.mdx)

---

If you don't have an Android device available to test with, we recommend using the default emulator that comes with Android Studio. If you run into any problems setting it up, follow the steps in this guide.

Install Watchman and JDK
------------------------

macOS

Windows

Linux

#### Prerequisites

Use a package manager such as [Homebrew](https://brew.sh/) to install the following dependency.

#### Install dependencies

1

[Install Watchman](https://facebook.github.io/watchman/docs/install#macos) using a tool such as Homebrew:

Terminal

Copy

`-Â``brew install watchman`

2

Install OpenJDK distribution called Azul Zulu using Homebrew. This distribution offers JDKs for both Apple Silicon and Intel Macs.

Run the following commands in a terminal:

Terminal

Copy

`-Â``brew install --cask zulu@17`

After you install the JDK, add the `JAVA_HOME` environment variable in ~/.bash\_profile (or ~/.zshrc if you use Zsh):

```
export JAVA_HOME=/Library/Java/JavaVirtualMachines/zulu-17.jdk/Contents/Home

```

#### Prerequisites

Use a package manager such as [Chocolatey](https://chocolatey.org/) to install the following dependencies.

#### Install dependencies

Install [Java SE Development Kit (JDK)](https://openjdk.org/):

Terminal

Copy

`-Â``choco install -y microsoft-openjdk17`

#### Install dependencies

1

Follow [instructions from the Watchman documentation](https://facebook.github.io/watchman/docs/install#linux) to compile and install it from the source.

2

Install [Java SE Development Kit (JDK)](https://openjdk.org/):

You can download and install [OpenJDK](http://openjdk.java.net/) from [AdoptOpenJDK](https://adoptopenjdk.net/) or your system packager.

Set up Android Studio
---------------------

macOS

Windows

1

Download and install [Android Studio](https://developer.android.com/studio).

2

Open the Android Studio app, click More Actions and select SDK Manager.

3

Open Android Studio, go to Settings > Languages & Frameworks > Android SDK. From the SDK Platforms tab, select the latest Android version (API level).

![Android SDK Platforms](/static/images/android-studio/sdk-platforms.png)

Then, click on the SDK Tools tab and make sure you have at least one version of the Android SDK Build-Tools and Android Emulator installed.

![Android SDK build tools.](/static/images/android-studio/build-tools.png)

4

Copy or remember the path listed in the box that says Android SDK Location.

![Android SDK location.](/static/images/android-studio/sdk-location.png)

5

Click Apply and OK to install the Android SDK and related build tools.

6

If you are on macOS or Linux, add an [environment variable](https://developer.android.com/studio/command-line/variables#envar) pointing to the Android SDK location in ~/.bash\_profile (or ~/.zshrc if you use Zsh). For example: `export ANDROID_HOME=/your/path/here`.

Add the following lines to your /.zprofile or ~/.zshrc (if you are using bash, then ~/.bash\_profile or ~/.bashrc) config file:

Terminal

Copy

`-Â``export ANDROID_HOME=$HOME/Library/Android/sdk`

`-Â``export PATH=$PATH:$ANDROID_HOME/emulator`

`-Â``export PATH=$PATH:$ANDROID_HOME/platform-tools`

7

Reload the path environment variables in your current shell:

Terminal

`# for zsh`

`-Â``source $HOME/.zshrc`

  
`# for bash`

`-Â``source $HOME/.bashrc`

8

Finally, make sure that you can run `adb` from your terminal.

1

Download [Android Studio](https://developer.android.com/studio).

2

Open Android Studio Setup. Under Select components to install, select Android Studio and Android Virtual Device. Then, click Next.

3

In the Android Studio Setup Wizard, under Install Type, select Standard and click Next.

![Android Studio Setup Wizard asks for the type of installation.](/static/images/android-studio/windows-install-type.png)

4

The Android Studio Setup Wizard will ask you to verify the settings, such as the version of Android SDK, platform-tools, and so on. Click Next after you have verified.

5

In the next window, accept licenses for all available components.

![Android Studio Setup Wizard asks to accept various licenses to install the tools.](/static/images/android-studio/windows-licenses.png)

6

After the tools installation is complete, configure the `ANDROID_HOME` environment variable. Go to Windows Control Panel > User Accounts > User Accounts (again) > Change my environment variables and click New to create a new `ANDROID_HOME` user variable. The value of this variable will point to the path to your Android SDK:

![Setting up ANDROID_HOME user variable.](/static/images/android-studio/windows-android-home-variable.png)How to find installed SDK location?

By default, the Android SDK is installed at the following location:

```
%LOCALAPPDATA%\Android\Sdk

```

To find the location of the SDK in Android Studio manually, go to Settings > Languages & Frameworks > Android SDK. See the location next to Android SDK Location.

![Android SDK location in Android Studio Settings.](/static/images/android-studio/windows-android-sdk-location.png)

7

To verify that the new environment variable is loaded, open PowerShell, and copy and paste the following command:

Terminal

Copy

`-Â``Get-ChildItem -Path Env:`

The command will output all user environment variables. In this list, see if `ANDROID_HOME` has been added.

8

To add platform-tools to the Path, go to Windows Control Panel > User Accounts > User Accounts (again) > Change my environment variables > Path > Edit > New and add the path to the platform-tools to the list as shown below:

![Setting up platform-tools user variable.](/static/images/android-studio/windows-platform-tools-path.png)How to find installed platform-tools location

By default, the platform-tools are installed at the following location:

```
%LOCALAPPDATA%\Android\Sdk\platform-tools

```

9

Finally, make sure that you can run `adb` from the PowerShell. For example, run the `adb --version` to see which version of the `adb` your system is running.

Set up an emulator
------------------

1

On the Android Studio main screen, click More Actions, then Virtual Device Manager in the dropdown.

![Android Studio configure.](/static/images/android-studio/virtual-device.png)

2

Click the Create device button.

![Android Studio create virtual device.](/static/images/android-studio/create-device.png)

3

Under Select Hardware, choose the type of hardware you'd like to emulate. We recommend testing against a variety of devices, but if you're unsure where to start, the newest device in the Pixel line could be a good choice.

![Android Studio create virtual device hardware selection.](/static/images/android-studio/select-hardware.png)

4

Select an OS version to load on the emulator (probably one of the system images in the Recommended tab), and download the image.

![Android Studio create virtual device os selection.](/static/images/android-studio/select-os.png)

5

Change any other settings you'd like, and press Finish to create the emulator. You can now run this emulator anytime by pressing the Play button in the AVD Manager window.

Troubleshooting
---------------

### Multiple `adb` versions

Having multiple `adb` versions on your system can result in the following error:

Terminal

Copy

`-Â``adb server version (xx) doesn't match this client (xx); killing...`

This is because the `adb` version on your system is different from the `adb` version on the Android SDK platform-tools.

1

Open the terminal and check the `adb` version on the system:

Terminal

Copy

`-Â``adb version`

2

And from the Android SDK platform-tool directory:

Terminal

Copy

`-Â``cd ~/Library/Android/sdk/platform-tools`

`-Â``./adb version`

3

Copy `adb` from Android SDK directory to `usr/bin` directory:

Terminal

Copy

`-Â``sudo cp ~/Library/Android/sdk/platform-tools/adb /usr/bin`

[Previous (Development process - Reference)

Common development errors](/workflow/common-development-errors)[Next (Development process - Reference)

iOS Simulator](/workflow/ios-simulator)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/workflow/android-studio-emulator.mdx)
* Last updated on April 24, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Install Watchman and JDK](/workflow/android-studio-emulator/#install-watchman-and-jdk)[Set up Android Studio](/workflow/android-studio-emulator/#set-up-android-studio)[Set up an emulator](/workflow/android-studio-emulator/#set-up-an-emulator)[Troubleshooting](/workflow/android-studio-emulator/#troubleshooting)[Multiple adb versions](/workflow/android-studio-emulator/#multiple-adb-versions)