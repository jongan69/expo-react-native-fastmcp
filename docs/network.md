Networking · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/network)

* [Next](/docs/next/network)* [0.79](/docs/network)* [0.78](/docs/0.78/network)* [0.77](/docs/0.77/network)* [0.76](/docs/0.76/network)* [0.75](/docs/0.75/network)* [0.74](/docs/0.74/network)* [0.73](/docs/0.73/network)* [0.72](/docs/0.72/network)* [0.71](/docs/0.71/network)* [0.70](/docs/0.70/network)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [The Basics](/docs/getting-started)

  * [Environment setup](/docs/environment-setup)

    * [Workflow](/docs/running-on-device)

      * [UI & Interaction](/docs/style)

        + [Style](/docs/style)+ [Height and Width](/docs/height-and-width)+ [Layout with Flexbox](/docs/flexbox)+ [Images](/docs/images)+ [Color Reference](/docs/colors)+ Interaction

                    - [Handling Touches](/docs/handling-touches)- [Navigating Between Screens](/docs/navigation)- [Animations](/docs/animations)- [Gesture Responder System](/docs/gesture-responder-system)+ Connectivity

                      - [Networking](/docs/network)- [Security](/docs/security)+ Inclusion

                        - [Accessibility](/docs/accessibility)* [Debugging](/docs/debugging)

          * [Testing](/docs/testing-overview)

            * [Performance](/docs/performance)

              * [JavaScript Runtime](/docs/javascript-environment)

                * [Codegen](/docs/the-new-architecture/what-is-codegen)

                  * [Native Development](/docs/native-platform)

                    * [Android and iOS guides](/docs/headless-js-android)

                      * [Legacy Architecture](/docs/legacy/native-modules-intro)

On this page

Networking
==========

Many mobile apps need to load resources from a remote URL. You may want to make a POST request to a REST API, or you may need to fetch a chunk of static content from another server.

Using Fetch[​](#using-fetch "Direct link to Using Fetch")
---------------------------------------------------------

React Native provides the [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) for your networking needs. Fetch will seem familiar if you have used `XMLHttpRequest` or other networking APIs before. You may refer to MDN's guide on [Using Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) for additional information.

### Making requests[​](#making-requests "Direct link to Making requests")

In order to fetch content from an arbitrary URL, you can pass the URL to fetch:

tsx

```
fetch('https://mywebsite.com/mydata.json');  

```

Fetch also takes an optional second argument that allows you to customize the HTTP request. You may want to specify additional headers, or make a POST request:

tsx

```
fetch('https://mywebsite.com/endpoint/', {  
  method: 'POST',  
  headers: {  
    Accept: 'application/json',  
    'Content-Type': 'application/json',  
  },  
  body: JSON.stringify({  
    firstParam: 'yourValue',  
    secondParam: 'yourOtherValue',  
  }),  
});  

```

Take a look at the [Fetch Request docs](https://developer.mozilla.org/en-US/docs/Web/API/Request) for a full list of properties.

### Handling the response[​](#handling-the-response "Direct link to Handling the response")

The above examples show how you can make a request. In many cases, you will want to do something with the response.

Networking is an inherently asynchronous operation. Fetch method will return a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) that makes it straightforward to write code that works in an asynchronous manner:

tsx

```
const getMoviesFromApi = () => {  
  return fetch('https://reactnative.dev/movies.json')  
    .then(response => response.json())  
    .then(json => {  
      return json.movies;  
    })  
    .catch(error => {  
      console.error(error);  
    });  
};  

```

You can also use the `async` / `await` syntax in a React Native app:

tsx

```
const getMoviesFromApiAsync = async () => {  
  try {  
    const response = await fetch(  
      'https://reactnative.dev/movies.json',  
    );  
    const json = await response.json();  
    return json.movies;  
  } catch (error) {  
    console.error(error);  
  }  
};  

```

Don't forget to catch any errors that may be thrown by `fetch`, otherwise they will be dropped silently.

* TypeScript* JavaScript

> By default, iOS 9.0 or later enforce App Transport Security (ATS). ATS requires any HTTP connection to use HTTPS. If you need to fetch from a cleartext URL (one that begins with `http`) you will first need to [add an ATS exception](/docs/integration-with-existing-apps#test-your-integration). If you know ahead of time what domains you will need access to, it is more secure to add exceptions only for those domains; if the domains are not known until runtime you can [disable ATS completely](/docs/publishing-to-app-store#1-enable-app-transport-security). Note however that from January 2017, [Apple's App Store review will require reasonable justification for disabling ATS](https://forums.developer.apple.com/thread/48979). See [Apple's documentation](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW33) for more information.

> On Android, as of API Level 28, clear text traffic is also blocked by default. This behaviour can be overridden by setting [`android:usesCleartextTraffic`](https://developer.android.com/guide/topics/manifest/application-element#usesCleartextTraffic) in the app manifest file.

Using Other Networking Libraries[​](#using-other-networking-libraries "Direct link to Using Other Networking Libraries")
------------------------------------------------------------------------------------------------------------------------

The [XMLHttpRequest API](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest) is built into React Native. This means that you can use third party libraries such as [frisbee](https://github.com/niftylettuce/frisbee) or [axios](https://github.com/axios/axios) that depend on it, or you can use the XMLHttpRequest API directly if you prefer.

tsx

```
const request = new XMLHttpRequest();  
request.onreadystatechange = e => {  
  if (request.readyState !== 4) {  
    return;  
  }  
  
  if (request.status === 200) {  
    console.log('success', request.responseText);  
  } else {  
    console.warn('error');  
  }  
};  
  
request.open('GET', 'https://mywebsite.com/endpoint/');  
request.send();  

```

> The security model for XMLHttpRequest is different than on web as there is no concept of [CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) in native apps.

WebSocket Support[​](#websocket-support "Direct link to WebSocket Support")
---------------------------------------------------------------------------

React Native also supports [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket), a protocol which provides full-duplex communication channels over a single TCP connection.

tsx

```
const ws = new WebSocket('ws://host.com/path');  
  
ws.onopen = () => {  
  // connection opened  
  ws.send('something'); // send a message  
};  
  
ws.onmessage = e => {  
  // a message was received  
  console.log(e.data);  
};  
  
ws.onerror = e => {  
  // an error occurred  
  console.log(e.message);  
};  
  
ws.onclose = e => {  
  // connection closed  
  console.log(e.code, e.reason);  
};  

```

Known Issues with `fetch` and cookie based authentication[​](#known-issues-with-fetch-and-cookie-based-authentication "Direct link to known-issues-with-fetch-and-cookie-based-authentication")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following options are currently not working with `fetch`

* `redirect:manual`
* `credentials:omit`

* Having same name headers on Android will result in only the latest one being present. A temporary solution can be found here: <https://github.com/facebook/react-native/issues/18837#issuecomment-398779994>.
* Cookie based authentication is currently unstable. You can view some of the issues raised here: <https://github.com/facebook/react-native/issues/23185>
* As a minimum on iOS, when redirected through a `302`, if a `Set-Cookie` header is present, the cookie is not set properly. Since the redirect cannot be handled manually this might cause a scenario where infinite requests occur if the redirect is the result of an expired session.

Configuring NSURLSession on iOS[​](#configuring-nsurlsession-on-ios "Direct link to Configuring NSURLSession on iOS")
---------------------------------------------------------------------------------------------------------------------

For some applications it may be appropriate to provide a custom `NSURLSessionConfiguration` for the underlying `NSURLSession` that is used for network requests in a React Native application running on iOS. For instance, one may need to set a custom user agent string for all network requests coming from the app or supply `NSURLSession` with an ephemeral `NSURLSessionConfiguration`. The function `RCTSetCustomNSURLSessionConfigurationProvider` allows for such customization. Remember to add the following import to the file in which `RCTSetCustomNSURLSessionConfigurationProvider` will be called:

objectivec

```
#import <React/RCTHTTPRequestHandler.h>  

```

`RCTSetCustomNSURLSessionConfigurationProvider` should be called early in the application life cycle such that it is readily available when needed by React, for instance:

objectivec

```
-(void)application:(__unused UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {  
  
  // set RCTSetCustomNSURLSessionConfigurationProvider  
  RCTSetCustomNSURLSessionConfigurationProvider(^NSURLSessionConfiguration *{  
     NSURLSessionConfiguration *configuration = [NSURLSessionConfiguration defaultSessionConfiguration];  
     // configure the session  
     return configuration;  
  });  
  
  // set up React  
  _bridge = [[RCTBridge alloc] initWithDelegate:self launchOptions:launchOptions];  
}  

```

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/network.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/network.md)

Last updated on **Apr 14, 2025**

[Previous

Gesture Responder System](/docs/gesture-responder-system)[Next

Security](/docs/security)

* [Using Fetch](#using-fetch)
  + [Making requests](#making-requests)+ [Handling the response](#handling-the-response)* [Using Other Networking Libraries](#using-other-networking-libraries)* [WebSocket Support](#websocket-support)* [Known Issues with `fetch` and cookie based authentication](#known-issues-with-fetch-and-cookie-based-authentication)* [Configuring NSURLSession on iOS](#configuring-nsurlsession-on-ios)

Develop

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

Participate

* [Showcase](/showcase)* [Contributing](/contributing/overview)* [Community](/community/overview)* [Directory](https://reactnative.directory/)* [Stack Overflow](https://stackoverflow.com/questions/tagged/react-native)

Find us

* [Blog](/blog)* [X](https://x.com/reactnative)* [Bluesky](https://bsky.app/profile/reactnative.dev)* [GitHub](https://github.com/facebook/react-native)

Explore More

* [ReactJS](https://react.dev/)* [Privacy Policy](https://opensource.fb.com/legal/privacy/)* [Terms of Service](https://opensource.fb.com/legal/terms/)

[![Meta Open Source Logo](/img/oss_logo.svg)![Meta Open Source Logo](/img/oss_logo.svg)](https://opensource.fb.com/)

Copyright © 2025 Meta Platforms, Inc.