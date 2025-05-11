Build server infrastructure - Expo Documentation

[Docs](/)

[Blog](https://expo.dev/blog)[Changelog](https://expo.dev/changelog)[Star Us on GitHub](https://github.com/expo/expo)

Search

[Home](/)[Guides](/guides/overview)[EAS](/eas)[Reference](/versions/latest)[Learn](/tutorial/overview)

[Introduction](/eas)[Configuration with eas.json](/eas/json)[Environment variables](/eas/environment-variables)

EAS Workflows

[Get started](/eas/workflows/get-started)[Example CI/CD workflows](/eas/workflows/examples)[Syntax for EAS Workflows](/eas/workflows/syntax)[Automating EAS CLI commands](/eas/workflows/automating-eas-cli)

Reference

EAS Build

[Introduction](/build/introduction)[Create your first build](/build/setup)[Configure with eas.json](/build/eas-json)[Internal distribution](/build/internal-distribution)[Automate submissions](/build/automate-submissions)[Using EAS Update](/build/updates)[Trigger builds from CI](/build/building-on-ci)[Trigger builds from GitHub App](/build/building-from-github)[Expo Orbit](/build/orbit)

App signing

Custom builds

Reference

[Build lifecycle hooks](/build-reference/npm-hooks)[Using private npm packages](/build-reference/private-npm-packages)[Git submodules](/build-reference/git-submodules)[Using npm cache with Yarn 1 (Classic)](/build-reference/npm-cache-with-yarn)[Set up EAS Build with a monorepo](/build-reference/build-with-monorepos)[Build APKs for Android Emulators and devices](/build-reference/apk)[Build for iOS Simulators](/build-reference/simulators)[App version management](/build-reference/app-versions)[Troubleshoot build errors and crashes](/build-reference/troubleshooting)[Install app variants on the same device](/build-reference/variants)[iOS capabilities](/build-reference/ios-capabilities)[Run EAS Build locally](/build-reference/local-builds)[Cache dependencies](/build-reference/caching)[Android build process](/build-reference/android-builds)[iOS build process](/build-reference/ios-builds)[Configuration process](/build-reference/build-configuration)[Server infrastructure](/build-reference/infrastructure)[iOS App Extensions](/build-reference/app-extensions)[Ignore files via .easignore](/build-reference/easignore)[Limitations](/build-reference/limitations)

EAS Hosting

[Introduction](/eas/hosting/introduction)[Get started](/eas/hosting/get-started)[Deployments and aliases](/eas/hosting/deployments-and-aliases)[Environment variables](/eas/hosting/environment-variables)[Custom domain](/eas/hosting/custom-domain)[Monitoring API routes](/eas/hosting/api-routes)[Workflows](/eas/hosting/workflows)

Reference

EAS Submit

[Introduction](/submit/introduction)[Submit to the Google Play Store](/submit/android)[Submit to the Apple App Store](/submit/ios)[Configure with eas.json](/submit/eas-json)

EAS Update

[Introduction](/eas-update/introduction)[Get started](/eas-update/getting-started)

Preview

Deployment

Concepts

Troubleshooting

Reference

EAS Metadata

[Introduction](/eas/metadata)[Get started](/eas/metadata/getting-started)

Reference

EAS Insights

[Introduction](/eas-insights/introduction)

Distribution

[Overview](/distribution/introduction)[App stores best practices](/distribution/app-stores)[App transfers](/distribution/app-transfers)[Understanding app size](/distribution/app-size)

Reference

[Webhooks](/eas/webhooks)

Expo accounts

Billing

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Build server infrastructure
===========================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/infrastructure.mdx)

Learn about the current build server infrastructure when using EAS.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/infrastructure.mdx)

---

Builder IP addresses
--------------------

A list of the IP addresses of the build servers is available [in this file](https://expo.dev/eas-build-worker-ips.txt). We do not expect to change the list often. The list includes "Last-Modified" and "Expires" ISO 8601 timestamps that respectively specify the last time the list was updated and the time until which we commit to not change the list.

Linux runners are hosted in Google Cloud Platform. macOS runners are hosted in our own macOS cloud.

Configuring build environment
-----------------------------

Images for each platform have one specific version of Node.js, Yarn, CocoaPods, Xcode, Ruby, Fastlane, and so on. You can override some of the versions in [eas.json](/build/eas-json). If there is no dedicated configuration option you are looking for, you can use [npm hooks](/build-reference/npm-hooks) to install or update any system dependencies with `apt-get` or `brew`. Consider that those customizations are applied during the build and will increase your build times.

When selecting an image for the build you can use the full name provided below or one of the aliases: `auto`, `latest`, or for a particular SDK such as `sdk-53`.

* The use of a specific name guarantees a consistent environment with only minor updates.
* When using the `auto` alias, the build image will be selected based on the project configuration, Expo SDK version, and React Native version. You can check what image is used for a build in the Spin up build environment build logs section.
* The `latest` alias will be assigned to the image with the most up-to-date versions of the software.
* The `sdk-53` alias will be assigned to the image best suited for SDK 53 builds.
* The `sdk-52` alias will be assigned to the image best suited for SDK 52 builds.
* The `sdk-51` alias will be assigned to the image best suited for SDK 51 builds.
* SDK aliases will be updated with every new SDK release.
* The `latest` alias will be updated with every new image release.

> Note: If you do not provide `image` in eas.json, your build by default will use the `auto` alias.

Android build server configurations
-----------------------------------

Android builders run on virtual machines in an isolated environment. Every build gets its own dedicated VM instance.

* Build resources:

  + `medium`: 4 vCPUs, 16 GB RAM ([n2-standard-4](https://cloud.google.com/compute/docs/general-purpose-machines#n2_machine_types) or [c3d-standard-4](https://cloud.google.com/compute/docs/general-purpose-machines#c3d_machine_types) (default) Google Cloud machine type, depending on the "New Android Builds Infrastructure" setting in project settings)
  + `large`: 8 vCPUs, 32 GB RAM ([n2-standard-8](https://cloud.google.com/compute/docs/general-purpose-machines#n2_machine_types) or [c3d-standard-8](https://cloud.google.com/compute/docs/general-purpose-machines#c3d_machine_types) (default) Google Cloud machine type, depending on the "New Android Builds Infrastructure" setting in project settings)
* [npm cache deployed with Kubernetes](/build-reference/caching#javascript-dependencies)
* [Maven cache deployed with Kubernetes](/build-reference/caching#android-dependencies)
* Global Gradle configuration in ~/.gradle/gradle.properties:

  ~/.gradle/gradle.properties

  Copy

  ```
  org.gradle.jvmargs=-Xmx14g -XX:MaxPermSize=512m -XX:+HeapDumpOnOutOfMemoryError -Dfile.encoding=UTF-8
  org.gradle.parallel=true
  org.gradle.configureondemand=true
  org.gradle.daemon=false

  ```
* Global npm configuration in ~/.npmrc:

  ~/.npmrc

  Copy

  ```
  registry=http://10.4.0.19:4873

  ```
* Global Yarn configuration in ~/.yarnrc.yml:

  ~/.yarnrc.yml

  Copy

  ```
  unsafeHttpWhitelist:
    - '*'
  npmRegistryServer: 'http://10.4.0.19:4873'
  enableImmutableInstalls: false

  ```

### Android server images

#### `ubuntu-22.04-jdk-17-ndk-r26b` (`latest`, `sdk-51`, `sdk-52`, `sdk-53`)

Details

* Docker image: `ubuntu:jammy-v20250112`
* NDK 26.1.10909125
* Node.js 20.18.3
* Bun 1.2.4
* Yarn 1.22.22
* pnpm 9.15.5
* npm 10.8.2
* Java 17
* node-gyp 11.1.0

#### `ubuntu-22.04-jdk-17-ndk-r25b` (`sdk-50`)

Details

* Docker image: `ubuntu:jammy-20220810`
* NDK 25.1.8937393
* Node.js 18.18.0
* Bun 1.0.14
* Yarn 1.22.19
* pnpm 8.9.2
* npm 9.8.1
* Java 17
* node-gyp 10.0.1

#### `ubuntu-22.04-jdk-11-ndk-r23b` (`sdk-49`)

Details

* Docker image: `ubuntu:jammy-20220810`
* NDK 23.1.7779620
* Node.js 18.18.0
* Bun 1.0.14
* Yarn 1.22.19
* pnpm 8.7.5
* npm 9.8.1
* Java 11
* node-gyp 10.0.1

#### `ubuntu-22.04-jdk-17-ndk-r21e`

Details

* Docker image: `ubuntu:jammy-20220810`
* NDK 21.4.7075529
* Node.js 18.18.0
* Bun 1.0.14
* Yarn 1.22.19
* pnpm 8.9.2
* npm 9.8.1
* Java 17
* node-gyp 10.0.1

#### `ubuntu-22.04-jdk-11-ndk-r21e`

Details

* Docker image: `ubuntu:jammy-20220810`
* NDK 21.4.7075529
* Node.js 18.18.0
* Bun 1.0.14
* Yarn 1.22.19
* pnpm 8.7.5
* npm 9.8.1
* Java 11
* node-gyp 10.0.1

#### `ubuntu-22.04-jdk-8-ndk-r21e` (deprecated)

Details

* Docker image: `ubuntu:jammy-20220810`
* NDK 21.4.7075529
* Node.js 18.18.0
* Bun 1.0.14
* Yarn 1.22.19
* pnpm 7.0.0
* npm 9.8.1
* Java 8
* node-gyp 10.0.1

#### `ubuntu-20.04-jdk-11-ndk-r23b` (deprecated)

Details

* Docker image: `ubuntu:focal-20220823`
* NDK 23.1.7779620
* Node.js 18.18.0
* Bun 1.0.14
* Yarn 1.22.19
* pnpm 7.0.0
* npm 9.8.1
* Java 11
* node-gyp 10.0.1

#### `ubuntu-20.04-jdk-11-ndk-r21e` (deprecated)

Details

* Docker image: `ubuntu:focal-20220823`
* NDK 21.4.7075529
* Node.js 18.18.0
* Bun 1.0.14
* Yarn 1.22.19
* pnpm 7.0.0
* npm 9.8.1
* Java 11
* node-gyp 10.0.1

#### `ubuntu-20.04-jdk-8-ndk-r21e` (deprecated)

Details

* Docker image: `ubuntu:focal-20220823`
* NDK 21.4.7075529
* Node.js 18.18.0
* Bun 1.0.14
* Yarn 1.22.19
* pnpm 7.0.0
* npm 9.8.1
* Java 8
* node-gyp 10.0.1

#### `ubuntu-20.04-jdk-11-ndk-r19c` (deprecated)

Details

* Docker image: `ubuntu:focal-20220823`
* NDK 19.2.5345600
* Node.js 18.18.0
* Bun 1.0.14
* Yarn 1.22.19
* pnpm 7.0.0
* npm 9.8.1
* Java 11
* node-gyp 10.0.1

#### `ubuntu-20.04-jdk-8-ndk-r19c` (deprecated)

Details

* Docker image: `ubuntu:focal-20220823`
* NDK 19.2.5345600
* Node.js 18.18.0
* Bun 1.0.14
* Yarn 1.22.19
* pnpm 7.0.0
* npm 9.8.1
* Java 8
* node-gyp 10.0.1

iOS build server configurations
-------------------------------

iOS builder VMs run on Mac mini hosts in an isolated environment. Every build gets its own fresh macOS VM. For more information, see [iOS-specific resource classes](/eas/json#resourceclass-2).

* Build resources:

  + `medium`: 5 performance cores, 20 GiB RAM, 110 GB SSD
  + `large`: 10 performance cores, 40 GiB RAM, 110 GB SSD
* [npm cache](/build-reference/caching#javascript-dependencies)
* [CocoaPods cache](/build-reference/caching#ios-dependencies)
* [`cocoapods-nexus-plugin`](https://github.com/expo/eas-build/tree/main/packages/cocoapods-nexus-plugin)
* Global npm configuration in ~/.npmrc:

  ~/.npmrc

  Copy

  ```
  registry=http://10.94.183.70:4873

  ```
* Global Yarn configuration in ~/.yarnrc.yml:

  ~/.yarnrc.yml

  Copy

  ```
  unsafeHttpWhitelist:
    - '*'
  npmRegistryServer: 'http://10.94.183.70:4873'
  enableImmutableInstalls: false

  ```

### iOS server images

#### `macos-sequoia-15.4-xcode-16.3` (`latest`, `sdk-53`)

Details

* macOS Sequoia 15.4.1
* Xcode 16.3 (16E140)
* Node.js 20.19.1
* Bun 1.2.11
* Yarn 1.22.22
* pnpm 9.15.9
* npm 9.8.1
* fastlane 2.227.1
* CocoaPods 1.16.2
* Ruby 3.2
* node-gyp 11.2.0
* jq 1.7.1
* Azul Zulu JDK 17.58.21 (OpenJDK 17.0.15)
* Git 2.49.0
* Git LFS 3.6.1
* applesimutils 0.9.10
* idb-companion 1.1.8

#### `macos-sequoia-15.3-xcode-16.2` (`sdk-52`)

Details

* macOS Sequoia 15.3
* Xcode 16.2 (16C5032a)
* Node.js 20.18.3
* Bun 1.2.4
* Yarn 1.22.22
* pnpm 9.15.5
* npm 9.8.1
* fastlane 2.226.0
* CocoaPods 1.16.2
* Ruby 3.2
* node-gyp 11.1.0

#### `macos-sonoma-14.6-xcode-16.1`

Details

* macOS Sonoma 14.6
* Xcode 16.1 (16B40)
* Node.js 18.18.0
* Bun 1.1.33
* Yarn 1.22.21
* pnpm 9.12.3
* npm 9.8.1
* fastlane 2.225.0
* CocoaPods 1.16.2
* Ruby 3.2
* node-gyp 10.2.0

#### `macos-sonoma-14.6-xcode-16.0`

Details

* macOS Sonoma 14.6
* Xcode 16.0 (16A242d)
* Node.js 18.18.0
* Bun 1.1.27
* Yarn 1.22.21
* pnpm 9.10.0
* npm 9.8.1
* fastlane 2.222.0
* CocoaPods 1.15.2
* Ruby 3.2
* node-gyp 10.2.0

#### `macos-sonoma-14.5-xcode-15.4` (`sdk-51`, `sdk-50`, `sdk-49`)

Details

* macOS Sonoma 14.5
* Xcode 15.4 (15F31d)
* Node.js 18.18.0
* Bun 1.1.13
* Yarn 1.22.21
* pnpm 9.3.0
* npm 9.8.1
* fastlane 2.220.0
* CocoaPods 1.14.3
* Ruby 2.7
* node-gyp 10.1.0

#### `macos-sonoma-14.4-xcode-15.3`

Details

* macOS Sonoma 14.4.1
* Xcode 15.3 (15E204a)
* Node.js 18.18.0
* Bun 1.0.35
* Yarn 1.22.21
* pnpm 8.14.1
* npm 9.8.1
* fastlane 2.219.0
* CocoaPods 1.14.3
* Ruby 2.7
* node-gyp 10.0.1

#### `macos-ventura-13.6-xcode-15.2`

Details

* macOS Ventura 13.6
* Xcode 15.2 (15C500b)
* Node.js 18.18.0
* Bun 1.0.23
* Yarn 1.22.21
* pnpm 8.14.1
* npm 9.8.1
* fastlane 2.219.0
* CocoaPods 1.14.3
* Ruby 2.7
* node-gyp 10.0.1

#### `macos-ventura-13.6-xcode-15.1`

Details

* macOS Ventura 13.6
* Xcode 15.1 (15C65)
* Node.js 18.18.0
* Bun 1.0.14
* Yarn 1.22.19
* pnpm 8.12.1
* npm 9.8.1
* fastlane 2.217.0
* CocoaPods 1.14.3
* Ruby 2.7
* node-gyp 10.0.1

#### `macos-ventura-13.6-xcode-15.0`

Details

* macOS Ventura 13.6
* Xcode 15.0 (15A240d)
* Node.js 18.18.0
* Bun 1.0.14
* Yarn 1.22.19
* pnpm 8.7.6
* npm 9.8.1
* fastlane 2.216.0
* CocoaPods 1.13.0
* Ruby 2.7
* node-gyp 10.0.1

### Supported Xcode versions

We aim to support all stable Xcode releases that allow you to submit your app to the App Store Connect when used during the build process.

This usually means that we support the latest stable Xcode version and the previous one (until the new [minimal Xcode version requirement](https://developer.apple.com/news/upcoming-requirements/?id=04292024a) is introduced by Apple).

[Previous (EAS Build - Reference)

Configuration process](/build-reference/build-configuration)[Next (EAS Build - Reference)

iOS App Extensions](/build-reference/app-extensions)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/build-reference/infrastructure.mdx)
* Last updated on October 31st, 2024

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Builder IP addresses](/build-reference/infrastructure/#builder-ip-addresses)[Configuring build environment](/build-reference/infrastructure/#configuring-build-environment)[Android build server configurations](/build-reference/infrastructure/#android-build-server-configurations)[Android server images](/build-reference/infrastructure/#android-server-images)[ubuntu-22.04-jdk-17-ndk-r26b ( latest , sdk-51 , sdk-52 , sdk-53 )](/build-reference/infrastructure/#ubuntu-2204-jdk-17-ndk-r26b-latest-sdk-51-sdk-52-sdk-53)[ubuntu-22.04-jdk-17-ndk-r25b ( sdk-50 )](/build-reference/infrastructure/#ubuntu-2204-jdk-17-ndk-r25b-sdk-50)[ubuntu-22.04-jdk-11-ndk-r23b ( sdk-49 )](/build-reference/infrastructure/#ubuntu-2204-jdk-11-ndk-r23b-sdk-49)[ubuntu-22.04-jdk-17-ndk-r21e](/build-reference/infrastructure/#ubuntu-2204-jdk-17-ndk-r21e)[ubuntu-22.04-jdk-11-ndk-r21e](/build-reference/infrastructure/#ubuntu-2204-jdk-11-ndk-r21e)[ubuntu-22.04-jdk-8-ndk-r21e (deprecated)](/build-reference/infrastructure/#ubuntu-2204-jdk-8-ndk-r21e-deprecated)[ubuntu-20.04-jdk-11-ndk-r23b (deprecated)](/build-reference/infrastructure/#ubuntu-2004-jdk-11-ndk-r23b-deprecated)[ubuntu-20.04-jdk-11-ndk-r21e (deprecated)](/build-reference/infrastructure/#ubuntu-2004-jdk-11-ndk-r21e-deprecated)[ubuntu-20.04-jdk-8-ndk-r21e (deprecated)](/build-reference/infrastructure/#ubuntu-2004-jdk-8-ndk-r21e-deprecated)[ubuntu-20.04-jdk-11-ndk-r19c (deprecated)](/build-reference/infrastructure/#ubuntu-2004-jdk-11-ndk-r19c-deprecated)[ubuntu-20.04-jdk-8-ndk-r19c (deprecated)](/build-reference/infrastructure/#ubuntu-2004-jdk-8-ndk-r19c-deprecated)[iOS build server configurations](/build-reference/infrastructure/#ios-build-server-configurations)[iOS server images](/build-reference/infrastructure/#ios-server-images)[macos-sequoia-15.4-xcode-16.3 ( latest , sdk-53 )](/build-reference/infrastructure/#macos-sequoia-154-xcode-163-latest-sdk-53)[macos-sequoia-15.3-xcode-16.2 ( sdk-52 )](/build-reference/infrastructure/#macos-sequoia-153-xcode-162-sdk-52)[macos-sonoma-14.6-xcode-16.1](/build-reference/infrastructure/#macos-sonoma-146-xcode-161)[macos-sonoma-14.6-xcode-16.0](/build-reference/infrastructure/#macos-sonoma-146-xcode-160)[macos-sonoma-14.5-xcode-15.4 ( sdk-51 , sdk-50 , sdk-49 )](/build-reference/infrastructure/#macos-sonoma-145-xcode-154-sdk-51-sdk-50-sdk-49)[macos-sonoma-14.4-xcode-15.3](/build-reference/infrastructure/#macos-sonoma-144-xcode-153)[macos-ventura-13.6-xcode-15.2](/build-reference/infrastructure/#macos-ventura-136-xcode-152)[macos-ventura-13.6-xcode-15.1](/build-reference/infrastructure/#macos-ventura-136-xcode-151)[macos-ventura-13.6-xcode-15.0](/build-reference/infrastructure/#macos-ventura-136-xcode-150)[Supported Xcode versions](/build-reference/infrastructure/#supported-xcode-versions)