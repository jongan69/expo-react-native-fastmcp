Expo Updates v1 - Expo Documentation

[Docs](/)

[Blog](https://expo.dev/blog)[Changelog](https://expo.dev/changelog)[Star Us on GitHub](https://github.com/expo/expo)

Search

[Home](/)[Guides](/guides/overview)[EAS](/eas)[Reference](/versions/latest)[Learn](/tutorial/overview)

Configuration files

[app.json / app.config.js](/versions/latest/config/app)[babel.config.js](/versions/latest/config/babel)[metro.config.js](/versions/latest/config/metro)[package.json](/versions/latest/config/package-json)

Expo SDK

[Expo](/versions/latest/sdk/expo)[Accelerometer](/versions/latest/sdk/accelerometer)[AppleAuthentication](/versions/latest/sdk/apple-authentication)[Application](/versions/latest/sdk/application)[Asset](/versions/latest/sdk/asset)[Audio (expo-audio)](/versions/latest/sdk/audio)[Audio (expo-av)](/versions/latest/sdk/audio-av)[AuthSession](/versions/latest/sdk/auth-session)[AV](/versions/latest/sdk/av)[BackgroundFetch](/versions/latest/sdk/background-fetch)[BackgroundTask

NEW](/versions/latest/sdk/background-task)[Barometer](/versions/latest/sdk/barometer)[Battery](/versions/latest/sdk/battery)[BlurView](/versions/latest/sdk/blur-view)[Brightness](/versions/latest/sdk/brightness)[BuildProperties](/versions/latest/sdk/build-properties)[Calendar](/versions/latest/sdk/calendar)[Camera](/versions/latest/sdk/camera)[Cellular](/versions/latest/sdk/cellular)[Checkbox](/versions/latest/sdk/checkbox)[Clipboard](/versions/latest/sdk/clipboard)[Constants](/versions/latest/sdk/constants)[Contacts](/versions/latest/sdk/contacts)[Crypto](/versions/latest/sdk/crypto)[DevClient](/versions/latest/sdk/dev-client)[Device](/versions/latest/sdk/device)[DeviceMotion](/versions/latest/sdk/devicemotion)[DocumentPicker](/versions/latest/sdk/document-picker)[FileSystem](/versions/latest/sdk/filesystem)[FileSystem (next)](/versions/latest/sdk/filesystem-next)[Fingerprint

NEW](/versions/latest/sdk/fingerprint)[Font](/versions/latest/sdk/font)[GLView](/versions/latest/sdk/gl-view)[Gyroscope](/versions/latest/sdk/gyroscope)[Haptics](/versions/latest/sdk/haptics)[Image](/versions/latest/sdk/image)[ImageManipulator](/versions/latest/sdk/imagemanipulator)[ImagePicker](/versions/latest/sdk/imagepicker)[IntentLauncher](/versions/latest/sdk/intent-launcher)[KeepAwake](/versions/latest/sdk/keep-awake)[LightSensor](/versions/latest/sdk/light-sensor)[LinearGradient](/versions/latest/sdk/linear-gradient)[Linking](/versions/latest/sdk/linking)[LivePhoto](/versions/latest/sdk/live-photo)[LocalAuthentication](/versions/latest/sdk/local-authentication)[Localization](/versions/latest/sdk/localization)[Location](/versions/latest/sdk/location)[Magnetometer](/versions/latest/sdk/magnetometer)[MailComposer](/versions/latest/sdk/mail-composer)[Manifests](/versions/latest/sdk/manifests)[Maps

ALPHA](/versions/latest/sdk/maps)[MediaLibrary](/versions/latest/sdk/media-library)[MeshGradient

NEW](/versions/latest/sdk/mesh-gradient)[NavigationBar](/versions/latest/sdk/navigation-bar)[Network](/versions/latest/sdk/network)[Notifications](/versions/latest/sdk/notifications)[Pedometer](/versions/latest/sdk/pedometer)[Print](/versions/latest/sdk/print)[Router](/versions/latest/sdk/router)[Router UI](/versions/latest/sdk/router-ui)[ScreenCapture](/versions/latest/sdk/screen-capture)[ScreenOrientation](/versions/latest/sdk/screen-orientation)[SecureStore](/versions/latest/sdk/securestore)[Sensors](/versions/latest/sdk/sensors)[Sharing](/versions/latest/sdk/sharing)[SMS](/versions/latest/sdk/sms)[Speech](/versions/latest/sdk/speech)[SplashScreen](/versions/latest/sdk/splash-screen)[SQLite](/versions/latest/sdk/sqlite)[StatusBar](/versions/latest/sdk/status-bar)[StoreReview](/versions/latest/sdk/storereview)[Symbols](/versions/latest/sdk/symbols)[SystemUI](/versions/latest/sdk/system-ui)[TaskManager](/versions/latest/sdk/task-manager)[TrackingTransparency](/versions/latest/sdk/tracking-transparency)[UI

ALPHA](/versions/latest/sdk/ui)[Updates](/versions/latest/sdk/updates)[Video (expo-av)](/versions/latest/sdk/video-av)[Video (expo-video)](/versions/latest/sdk/video)[VideoThumbnails](/versions/latest/sdk/video-thumbnails)[WebBrowser](/versions/latest/sdk/webbrowser)

Third-party libraries

[Overview](/versions/latest/sdk/third-party-overview)[@react-native-async-storage/async-storage](/versions/latest/sdk/async-storage)[@react-native-community/datetimepicker](/versions/latest/sdk/date-time-picker)[@react-native-community/netinfo](/versions/latest/sdk/netinfo)[@react-native-community/slider](/versions/latest/sdk/slider)[@react-native-masked-view/masked-view](/versions/latest/sdk/masked-view)[@react-native-picker/picker](/versions/latest/sdk/picker)[@react-native-segmented-control/segmented-control](/versions/latest/sdk/segmented-control)[@shopify/flash-list](/versions/latest/sdk/flash-list)[@shopify/react-native-skia](/versions/latest/sdk/skia)[@stripe/stripe-react-native](/versions/latest/sdk/stripe)[lottie-react-native](/versions/latest/sdk/lottie)[react-native-gesture-handler](/versions/latest/sdk/gesture-handler)[react-native-maps](/versions/latest/sdk/map-view)[react-native-pager-view](/versions/latest/sdk/view-pager)[react-native-reanimated](/versions/latest/sdk/reanimated)[react-native-safe-area-context](/versions/latest/sdk/safe-area-context)[react-native-screens](/versions/latest/sdk/screens)[react-native-svg](/versions/latest/sdk/svg)[react-native-view-shot](/versions/latest/sdk/captureRef)[react-native-webview](/versions/latest/sdk/webview)

Technical specs

[Expo Updates v1](/technical-specs/expo-updates-1)[Expo Structured Field Values](/technical-specs/expo-sfv-0)

More

[Expo CLI](/more/expo-cli)[create-expo-app](/more/create-expo)[qr.expo.dev](/more/qr-codes)[Glossary of terms](/more/glossary-of-terms)

React Native

[Visit documentation](https://reactnative.dev/docs/components-and-apis)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Expo Updates v1
===============

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/technical-specs/expo-updates-1.mdx)

Version 1

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/technical-specs/expo-updates-1.mdx)

---

Introduction
------------

This is the specification for Expo Updates, a protocol for delivering updates to Expo apps running on multiple platforms.

### Conformance

Conforming servers and client libraries must fulfill all normative requirements. Conformance requirements are described in this document by both descriptive assertions and key words with clearly defined meanings.

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in the normative portions of this document are to be interpreted as described in [IETF RFC 2119](https://tools.ietf.org/html/rfc2119). These key words may appear in lowercase and still retain their meaning unless explicitly declared as non-normative.

A conforming implementation of this protocol MAY provide additional functionality, but MUST NOT where explicitly disallowed or would otherwise result in non-conformance. Where relevant, unknown fields should be allowed and ignored by conforming clients.

### Overview

Conforming servers and client libraries MUST follow the HTTP spec as described in [RFC 7231](https://tools.ietf.org/html/rfc7231) as well as the more precise guidance described in this spec.

* An *update* is defined as a [*manifest*](/technical-specs/expo-updates-1#manifest-body) together with the assets referenced inside the manifest.
* A [*directive*](/technical-specs/expo-updates-1#directive-body) is defined as a message from the server that instructs clients to perform an action.

Expo Updates is a protocol for assembling and delivering updates and directives to clients.

The primary audiences of this spec are Expo Application Services and organizations that wish to manage their own update server to satisfy internal requirements.

Client
------

> See the [reference client library](https://github.com/expo/expo/tree/main/packages/expo-updates).

An app running a conformant Expo Updates client library MUST load the most recent *update* saved in the client library's update database, possibly after filtering by the contents of the update's manifest [*metadata*](/technical-specs/expo-updates-1#manifest-body).

The following describes how a conformant Expo Updates client library MUST retrieve a new update from a conformant server:

1. The client library MUST make a [request](/technical-specs/expo-updates-1#request) for the most recent update and directive, with constraints specified in the headers.
2. If a [response](/technical-specs/expo-updates-1#response) is received, the client library MUST process its contents:
   * For a response containing an *update*, the client library SHALL proceed to make additional requests to download and store any new assets specified in the manifest. The manifest and assets together are considered a new *update*. The client library will edit its local state to reflect that a new update has been added to the local storage. It will also update the local state with the new `expo-manifest-filters` and `expo-server-defined-headers` found in the response [headers](/technical-specs/expo-updates-1#manifest-response-headers).
   * For a response containing a *directive*, the client library will consume the directive depending on the directive type and edit its local state accordingly.

Request
-------

A conformant client library MUST make a GET request with the headers:

1. `expo-protocol-version: 1`, to specify version 1 of this Expo Updates specification.
2. `expo-platform`, to specify the platform type the client is running on.
   * iOS MUST be `expo-platform: ios`.
   * Android MUST be `expo-platform: android`.
   * If it is not one of these platforms, the server SHOULD return a 400 or a 404
3. `expo-runtime-version` MUST be a runtime version compatible with the client. A runtime version stipulates the native code setup a client is running. It should be set when the client is built. For example, in an iOS client, the value may be set in a plist file.
4. Any headers stipulated by a previous responses' [server defined headers](/technical-specs/expo-updates-1#response).

A conformant client library MAY send one of `accept: application/expo+json`, `accept: application/json`, or `accept: multipart/mixed` based on the [supported response structures](/technical-specs/expo-updates-1#response), though it SHOULD send `accept: application/expo+json, application/json, multipart/mixed`. A conformant client library MAY express preference using "q" parameters as specified in [RFC 7231](https://datatracker.ietf.org/doc/html/rfc7231#section-5.3.1), which default to `1`.

A conformant client library configured to perform [code signing](/technical-specs/expo-updates-1#code-signing) verification MUST send a `expo-expect-signature` header to indicate that it expects the conformant server to include the `expo-signature` header in the manifest response. `expo-expect-signature` is an [Expo SFV](/technical-specs/expo-sfv-0) dictionary which MAY contain any of the following key value pairs:

* `sig` SHOULD contain the boolean `true` to indicate that it requires a conformant server to respond with the signature in the `sig` key.
* `keyid` SHOULD contain the keyId of the public key the client will use to verify the signature
* `alg` SHOULD contain the algorithm the client will use to verify the signature

Example:

```
expo-protocol-version: 1
accept: application/expo+json;q=0.9, application/json;q=0.8, multipart/mixed
expo-platform: *
expo-runtime-version: *
expo-expect-signature: sig, keyid="root", alg="rsa-v1_5-sha256"

```

Response
--------

A conformant server MUST return a response structured in at least one of the two following response structures, MAY support either or both response structures, and when an unsupported response structure is requested the server SHOULD respond with an HTTP `406` error status. A server that wishes to respond with an incompatible response for the requested protocol version SHOULD also respond with an HTTP `406` error status instead.

* For a response with `content-type: application/json` or `content-type: application/expo+json`, the [common response headers](/technical-specs/expo-updates-1#common-response-headers) and [other response headers](/technical-specs/expo-updates-1#other-response-headers) MUST be sent in the response headers and the [manifest body](/technical-specs/expo-updates-1#manifest-body) MUST be sent in the response body. This format of response does not support multiple response parts and therefore does not support *directives*, and SHOULD respond with an HTTP `406` error status when the most recent response to be served is not an *update*.
* For a response with `content-type: multipart/mixed`, the response MUST be structured as specified in the [multipart response](/technical-specs/expo-updates-1#multipart-response) section.
* A [multipart response](/technical-specs/expo-updates-1#multipart-response) with no parts MAY respond with an HTTP `204` status and no content, and thus no `content-type` response header.

The choice of update and headers are dependent on the values of the request headers. A conformant server MUST respond with the most recent update, ordered by creation time, satisfying all parameters and constraints imposed by the [request headers](/technical-specs/expo-updates-1#request). The server MAY use any properties of the request like its headers and source IP address to choose amongst several updates that all satisfy the request's constraints.

### Common response headers

```
expo-protocol-version: 1
expo-sfv-version: 0
expo-manifest-filters: &lt;expo-sfv&gt;
expo-server-defined-headers: &lt;expo-sfv&gt;
cache-control: *
content-type: *

```

* `expo-protocol-version` describes the version of the protocol defined in this spec and MUST be `1`.
* `expo-sfv-version` MUST be `0`.
* `expo-manifest-filters` is an [Expo SFV](/technical-specs/expo-sfv-0) dictionary. It is used to filter updates stored by the client library by the `metadata` attribute found in the [manifest](/technical-specs/expo-updates-1#manifest-body). If a field is mentioned in the filter, the corresponding field in the metadata must either be missing or equal for the update to be included. The client library MUST store the manifest filters until it is overwritten by a newer response.
* `expo-server-defined-headers` is an [Expo SFV](/technical-specs/expo-sfv-0) dictionary. It defines headers that a client library MUST store until overwritten by a newer dictionary, and they MUST be included in every subsequent [update request](/technical-specs/expo-updates-1#request).
* `cache-control` MUST be set to an appropriately short period of time. A value of `cache-control: private, max-age=0` is recommended to ensure the newest manifest is returned. Setting longer cache ages could result in stale updates.
* `content-type` MUST be determined by *proactive negotiation* as defined in [RFC 7231](https://tools.ietf.org/html/rfc7231#section-3.4.1). Since the client library is [required](/technical-specs/expo-updates-1#request) to send an `accept` header with each manifest request, this will always be either `application/expo+json`, `application/json`; otherwise the request would return a `406` error.

### Other response headers

```
expo-signature: *

```

* `expo-signature` SHOULD contain the signature of the manifest to be used during the validation step of [code signing](/technical-specs/expo-updates-1#code-signing) if the request for the manifest contained the `expo-expect-signature` header. This is an [Expo SFV](/technical-specs/expo-sfv-0) dictionary which MAY contain any of the following key value pairs:
  + `sig` MUST contain the signature of the manifest. The name of this field matches that of `expo-expect-signature`.
  + `keyid` MAY contain the keyId of the key the server used to sign the response. The client SHOULD use the certificate that matches this `keyid` to verify the signature.
  + `alg` MAY contain the algorithm the server used to sign the response. The client SHOULD use this field only if it matches the algorithm defined for the certificate matching `keyid`.

### Multipart response

An update response of this format is defined by the `multipart/mixed` MIME type as defined by [RFC 2046](https://tools.ietf.org/html/rfc2046#section-5.1).

Headers for this response format are the [common response headers](/technical-specs/expo-updates-1#common-response-headers), with the following exceptions:

* `content-type` SHOULD have a `multipart/mixed` value as defined by [RFC 2046](https://tools.ietf.org/html/rfc2046#section-5.1)

Part order is not strict. A multipart response with no parts (zero-length body) should be considered a no-op (no updates or directives available), though headers for the response SHOULD be sent nevertheless and processed by the client.

Each part is defined as follows:

1. OPTIONAL `"manifest"` part:
   * MUST have part header `content-disposition: form-data; name="manifest"`. The first parameter (`form-data`) does not need to be `form-data`, but the `name` parameter must have `manifest` as a value.
   * MUST have part header `content-type: application/json` or `application/expo+json`.
   * SHOULD have part header `expo-signature` as defined in [other response headers](/technical-specs/expo-updates-1#other-response-headers) if code signing is being used.
   * The [manifest body](/technical-specs/expo-updates-1#manifest-body) MUST be sent in the part body.
2. OPTIONAL `"extensions"` part:
   * MUST have part header `content-disposition: form-data; name="extensions"`. The first parameter (`form-data`) does not need to be `form-data`, but the `name` parameter must have `extensions` as a value.
   * MUST have part header `content-type: application/json`.
   * The [extensions-body](/technical-specs/expo-updates-1#extensions-body) MUST be sent in the part body.
3. OPTIONAL `"directive"` part:
   * MUST have part header `content-disposition: form-data; name="directive"`. The first parameter (`form-data`) does not need to be `form-data`, but the `name` parameter must have `directive` as a value.
   * MUST have part header `content-type: application/json` or `application/expo+json`.
   * SHOULD have part header `expo-signature` as defined in [other response headers](/technical-specs/expo-updates-1#other-response-headers) if code signing is being used.
   * The [directive body](/technical-specs/expo-updates-1#directive-body) MUST be sent in the part body.

### Manifest body

Defined as JSON conforming to both the following `Manifest` definition expressed in [TypeScript](https://www.typescriptlang.org/) and the detailed descriptions for each field:

```
type Manifest = {
  id: string;
  createdAt: string;
  runtimeVersion: string;
  launchAsset: Asset;
  assets: Asset[];
  metadata: { [key: string]: string };
  extra: { [key: string]: any };
};

type Asset = {
  hash?: string;
  key: string;
  contentType: string;
  fileExtension?: string;
  url: string;
};

```

* `id`: The ID MUST uniquely specify the manifest and MUST be a UUID.
* `createdAt`: The date and time at which the update was created is essential as the client library selects the most recent update (subject to any constraints supplied by the `expo-manifest-filters` header). The datetime should be formatted according to [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601).
* `runtimeVersion`: Can be any string defined by the developer. It stipulates what native code setup is required to run the associated update.
* `launchAsset`: A special asset that is the entry point of the application code. The `fileExtension` field will be ignored for this asset and SHOULD be omitted.
* `assets`: An array of assets used by the update bundle, such as JavaScript, pictures, and fonts. All assets (including the `launchAsset`) should be downloaded to disk before executing the update, and a mapping of asset `key`s to locations on disk should be provided to application code.
* Properties of each asset object:

  + `hash`: Base64URL-encoded SHA-256 hash of the file to guarantee integrity. Base64URL encoding is defined by [IETF RFC 4648](https://datatracker.ietf.org/doc/html/rfc4648#section-5).
  + `key`: Key used to reference this asset from the update's application code. This key, for example, may be generated by a separate build step that processes the application code, such as a bundler.
  + `contentType`: The MIME type of the file as defined by [RFC 2045](https://tools.ietf.org/html/rfc2045). For example, `application/javascript`, `image/jpeg`.
  + `fileExtension`: The suggested extension to use when a file is saved on a client. Some platforms, such as iOS, require certain file types to be saved with an extension. The extension MUST be prefixed with a `.`. For example, .jpeg. In some cases, such as the launchAsset, this field will be ignored in favor of a locally determined extension. If the field is omitted and there is no locally stipulated extension, the asset will be saved without an extension. For example, `./filename` with no `.` at the end.
    A conforming client SHOULD prefix a file extension with a `.` if a file extension is not empty and missing the `.` prefix.
  + `url`: Location at which the file may be fetched.
* `metadata`: The metadata associated with an update. It is a string-valued dictionary. The server MAY send back anything it wishes to be used for filtering the updates. The metadata MUST pass the filter defined in the accompanying `expo-manifest-filters` header.
* `extra`: For storage of optional "extra" information such as third-party configuration. For example, if the update is hosted on Expo Application Services (EAS), the EAS project ID may be included:

  ```
  "extra": {
    "eas": {
      "projectId": "00000000-0000-0000-0000-000000000000"
    }
  }

  ```

### Extensions body

Defined as JSON conforming to both the following `Extensions` definition expressed in [TypeScript](https://www.typescriptlang.org/) and the detailed descriptions for each field:

```
type Extensions = {
  assetRequestHeaders: ExpoAssetHeaderDictionary;
  ...
}

type ExpoAssetHeaderDictionary = {
  [assetKey: string]: {
    [headerName: string]: string,
  };
}

```

* `assetRequestHeaders`: MAY contain a dictionary of header (key, value) pairs to include with asset requests. Key and value MUST both be strings.

### Directive body

Defined as JSON conforming to both the following `Directive` definition expressed in [TypeScript](https://www.typescriptlang.org/) and the detailed descriptions for each field:

```
type Directive = {
  type: string;
  parameters?: { [key: string]: any };
  extra?: { [key: string]: any };
};

```

* `type`: The type of directive.
* `parameters`: MAY contain any extra information specific to the `type`.
* `extra`: For storage of optional "extra" information such as third-party information. For example, if the update is hosted on Expo Application Services (EAS), the EAS project ID may be included.

A conformant client library and server MAY specify and implement directive types specific to the needs of the application. For example, Expo Application Services makes use of one type thus far, `rollBackToEmbedded`, which directs the expo-updates library to use the update embedded in the host application instead of any other downloaded updates.

Asset request
-------------

A conformant client library MUST make a GET request to the asset URLs specified by the manifest. The client library SHOULD include a header accepting the asset's content type as specified in the manifest. Additionally, the client library SHOULD specify the compression encoding the client library is capable of handling.

Example headers:

```
accept: image/jpeg, */*
accept-encoding: br, gzip

```

A conformant client library MUST also include any header (key, value) pairs included in [`assetRequestHeaders`](/technical-specs/expo-updates-1#manifest-extensions) for this asset key.

Asset response
--------------

An asset located at a particular URL MUST NOT be changed or removed since client libraries may fetch assets for any update at any time. A conformant client MUST verify that the base64url-encoded SHA-256 hash of the asset matches the `hash` field for the asset from the manifest.

### Asset response headers

The asset MUST be encoded using a compression format that the client supports according to the request's `accept-encoding` header. The server MAY serve uncompressed assets. The response MUST include a `content-type` header with the MIME type of the asset.
For example:

```
content-encoding: br
content-type: application/javascript

```

An asset is RECOMMENDED to be served with a `cache-control` header set to a long duration as an asset located at a given URL must not change. For example:

```
cache-control: public, max-age=31536000, immutable

```

### Compression

Assets SHOULD be capable of being served with [Gzip](https://www.gnu.org/software/gzip/) and [Brotli](https://github.com/google/brotli) compression.

Code signing
------------

Expo Updates supports code signing the manifest and directive bodies. Code signing the manifest also transitively signs the assets since their hashes are present in the manifest and verified by a conformant client. A conformant client MAY request the manifest or directive be signed using a private key, and then MUST verify the signature of the manifest or directive using the corresponding code signing certificate before it is used or any corresponding manifest assets are downloaded. The client MUST verify that the signing certificate is either a self-signed, trusted root certificate or is in a certificate chain signed by a trusted root certificate. In either case, the root certificate MUST be embedded in the application or device's operating system.

[Previous (Third-party libraries)

react-native-webview](/versions/latest/sdk/webview)[Next (Technical specs)

Expo Structured Field Values](/technical-specs/expo-sfv-0)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/technical-specs/expo-updates-1.mdx)
* Last updated on March 13, 2023

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Introduction](/technical-specs/expo-updates-1/#introduction)[Conformance](/technical-specs/expo-updates-1/#conformance)[Overview](/technical-specs/expo-updates-1/#overview)[Client](/technical-specs/expo-updates-1/#client)[Request](/technical-specs/expo-updates-1/#request)[Response](/technical-specs/expo-updates-1/#response)[Common response headers](/technical-specs/expo-updates-1/#common-response-headers)[Other response headers](/technical-specs/expo-updates-1/#other-response-headers)[Multipart response](/technical-specs/expo-updates-1/#multipart-response)[Manifest body](/technical-specs/expo-updates-1/#manifest-body)[Extensions body](/technical-specs/expo-updates-1/#extensions-body)[Directive body](/technical-specs/expo-updates-1/#directive-body)[Asset request](/technical-specs/expo-updates-1/#asset-request)[Asset response](/technical-specs/expo-updates-1/#asset-response)[Asset response headers](/technical-specs/expo-updates-1/#asset-response-headers)[Compression](/technical-specs/expo-updates-1/#compression)[Code signing](/technical-specs/expo-updates-1/#code-signing)