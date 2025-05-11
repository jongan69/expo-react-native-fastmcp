Troubleshooting Proxies - Expo Documentation

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

Integrations

Troubleshooting

[Overview](/troubleshooting/overview)["Application has not been registered" error](/troubleshooting/application-has-not-been-registered)[Clear bundler caches on macOS and Linux](/troubleshooting/clear-cache-macos-linux)[Clear bundler caches on Windows](/troubleshooting/clear-cache-windows)["React Native version mismatch" errors](/troubleshooting/react-native-version-mismatch)[Proxies](/troubleshooting/proxies)

Regulatory compliance

[Data and Privacy protection](/regulatory-compliance/data-and-privacy-protection)[GDPR compliance](/regulatory-compliance/gdpr)[HIPAA compliance](/regulatory-compliance/hipaa)[Privacy Shield](/regulatory-compliance/privacy-shield)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Troubleshooting Proxies
=======================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/troubleshooting/proxies.mdx)

Learn about troubleshooting proxies with a set of recommended tools.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/troubleshooting/proxies.mdx)

---

macOS proxy configuration (Sierra)
----------------------------------

> If anything goes wrong, you can revert to the "Automatic Proxy settings" in System Network Preferences using Automatic Proxy Configuration `your-corporate-proxy-uri:port-number/proxy.pac`.

### Overview

To run this in the local iOS Simulator while on your corporate Wi-Fi network, a local proxy manager is required. You can use a local proxy application such as [Charles](http://charlesproxy.com).

#### Open macOS network preferences

1. Open `System Preferences` for your Mac (Apple Menu > System Preferences).
2. Go to Network.
3. Be sure your `Location` is set to your proxy network, and not "Automatic".
4. With Wi-Fi selected on the left and/or ethernet connection, click `Advanced...` on the bottom right side of the window.

#### Configure proxy address

1. Disable/uncheck "Automatic Proxy Configuration" if it is set.
2. Check "Web Proxy (HTTP)" and set "Web Proxy Server" to 127.0.0.1 : 8888
3. Check "Secure Web Proxy (HTTPS)" and set "Secure Web Proxy Server" to 127.0.0.1 : 8888

### Configure `Charles`

1. Open Charles
2. If it asks, don't allow it to manage your macOS Network Configuration, the previous steps do that. (If you change Charles port, update the previous step to the correct port instead of default 8888)
3. In the menu of Charles go to `Proxy > External Proxy Settings`, check `Use external proxy servers`
4. Check `Web Proxy (HTTP)`, and enter `your-corporate-proxy-uri:port-number`
5. Check `Proxy server requires a password`
6. Domain: YOUR DOMAIN,
   Username: YOUR USERNAME
   Password: YOUR PASSWORD
7. Same for Secure Web Proxy (HTTPS). *Be sure to fill in the same proxy, username, and password address* fields.
8. In the text area for `Bypass external proxies for the following hosts:` enter:

   ```
   localhost
   *.local

   ```

   You may need to include your mail server or other corporate network addresses.
9. Check "Always bypass external proxies for localhost"

### iOS Simulator configuration

If you have an existing iOS Simulator custom setup going that is not working, "Simulator > Reset Content and Settings" from the menu.

If you have the Simulator open still, quit it.

Now, in Charles under the "Help" menu > Install Charles Root Certificate, and then again for Install Charles Root Certificate in iOS Simulators

> Technical note: This whole process is required because the iOS Simulator is served a bum proxy certificate instead of the actual certificate, and doesn't allow it, for <https://exp.host/> which is required to run Expo.   
>  Also note: Configure applications that need internet access, such as Spotify, to use <http://localhost:8888> as your proxy. Some apps, such as Chrome and Firefox, you can configure in the settings to use your "System Network Preferences" which will use Charles : 8888, or no proxy, depending on how you have your "Location" set in the Apple menu/network preferences. If you are set to "Automatic" no proxy is used, if it is set to "your proxy network" the proxy is used and Charles will need to be running.

Command line application proxy configuration
--------------------------------------------

npm, git, Brew, Curl, and any other command line applications need proxy access too.

#### For npm

Open `~/.npmrc` and set:

.npmrc

Copy

```
http_proxy=http://localhost:8888
https_proxy=http://localhost:8888

```

### For git

Open `~/.gitconfig` and set

.gitconfig

Copy

```
[http]
  proxy = http://localhost:8888
[https]
  proxy = http://localhost:8888

```

### For command line applications

Depending on your shell, and config, Open `~/.bashrc`, `~/.bash_profile`, or `~/.zshrc` or wherever you set your shell variables and set:

```
export HTTP_PROXY="http://localhost:8888"
export http_proxy="http://localhost:8888"
export ALL_PROXY="http://localhost:8888"
export all_proxy="http://localhost:8888"
export HTTPS_PROXY="http://localhost:8888"
export https_proxy="http://localhost:8888"

```

> If you switch your network location back to "Automatic" to use npm or git, you will need to comment these lines out using a `#` before the line you wish to disable. You could alternatively use a command-line proxy manager if you prefer.

[Previous (More - Troubleshooting)

"React Native version mismatch" errors](/troubleshooting/react-native-version-mismatch)[Next (Regulatory compliance)

Data and Privacy protection](/regulatory-compliance/data-and-privacy-protection)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/troubleshooting/proxies.mdx)
* Last updated on July 04, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[macOS proxy configuration (Sierra)](/troubleshooting/proxies/#macos-proxy-configuration-sierra)[Overview](/troubleshooting/proxies/#overview)[Configure Charles](/troubleshooting/proxies/#configure-charles)[iOS Simulator configuration](/troubleshooting/proxies/#ios-simulator-configuration)[Command line application proxy configuration](/troubleshooting/proxies/#command-line-application-proxy-configuration)[For git](/troubleshooting/proxies/#for-git)[For command line applications](/troubleshooting/proxies/#for-command-line-applications)