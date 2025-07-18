Fabric Native Components: iOS · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/fabric-native-components-ios)

* [Next](/docs/next/fabric-native-components-ios)* [0.79](/docs/fabric-native-components-ios)* [0.78](/docs/0.78/fabric-native-components-ios)* [0.77](/docs/0.77/fabric-native-components-ios)* [0.76](/docs/0.76/fabric-native-components-ios)* [0.75](/docs/0.75/getting-started)* [0.74](/docs/0.74/getting-started)* [0.73](/docs/0.73/getting-started)* [0.72](/docs/0.72/getting-started)* [0.71](/docs/0.71/getting-started)* [0.70](/docs/0.70/getting-started)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

On this page

Fabric Native Components: iOS
=============================

Now it's time to write some iOS platform code to be able to render the web view. The steps you need to follow are:

* Run Codegen.
* Write the code for the `RCTWebView`
* Register the `RCTWebView` in the application

### 1. Run Codegen[​](#1-run-codegen "Direct link to 1. Run Codegen")

You can [manually run](/docs/the-new-architecture/codegen-cli) the Codegen, however it's simpler to use the application you're going to demo the component in to do this for you.

bash

```
cd ios  
bundle install  
bundle exec pod install  

```

Importantly you will see logging output from Codegen, which we're going to use in Xcode to build our WebView native component.

warning

You should be careful about committing generated code to your repository. Generated code is specific to each version of React Native. Use npm [peerDependencies](https://nodejs.org/en/blog/npm/peer-dependencies) to restrict compatibility with version of React Native.

### 3. Write the `RCTWebView`[​](#3-write-the-rctwebview "Direct link to 3-write-the-rctwebview")

We need to prepare your iOS project using Xcode by completing these **5 steps**:

1. Open the CocoPods generated Xcode Workspace:

bash

```
cd ios  
open Demo.xcworkspace  

```

![Open Xcode Workspace](/docs/assets/fabric-native-components/1.webp)

2. Right click on app and select `New Group`, call the new group `WebView`.

![Right click on app and select New Group](/docs/assets/fabric-native-components/2.webp)

3. In the `WebView` group, create `New`→`File from Template`.

![Create a new file using the Cocoa Touch Classs template](/docs/assets/fabric-native-components/3.webp)

4. Use the `Objective-C File` template, and name it `RCTWebView`.

![Create an Objective-C RCTWebView class](/docs/assets/fabric-native-components/4.webp)

5. Repeat step 4 and create a header file named `RCTWebView.h`.
6. Rename `RCTWebView.m` → `RCTWebView.mm` making it an Objective-C++ file.

Demo/ios

```
Podfile  
...  
Demo  
├── AppDelegate.swift  
...  
├── RCTWebView.h  
└── RCTWebView.mm  

```

After creating the header file and the implementation file, you can start implementing them.

This is the code for the `RCTWebView.h` file, which declares the component interface.

Demo/RCTWebView/RCTWebView.h

```
#import <React/RCTViewComponentView.h>  
#import <UIKit/UIKit.h>  
  
NS_ASSUME_NONNULL_BEGIN  
  
@interface RCTWebView : RCTViewComponentView  
  
// You would declare native methods you'd want to access from the view here  
  
@end  
  
NS_ASSUME_NONNULL_END  

```

This class defines an `RCTWebView` which extends the `RCTViewComponentView` class. This is the base class for all the native components and it is provided by React Native.

The code for the implementation file (`RCTWebView.mm`) is the following:

Demo/RCTWebView/RCTWebView.mm

```
#import "RCTWebView.h"  
  
#import <react/renderer/components/AppSpec/ComponentDescriptors.h>  
#import <react/renderer/components/AppSpec/EventEmitters.h>  
#import <react/renderer/components/AppSpec/Props.h>  
#import <react/renderer/components/AppSpec/RCTComponentViewHelpers.h>  
#import <WebKit/WebKit.h>  
  
using namespace facebook::react;  
  
@interface RCTWebView () <RCTCustomWebViewViewProtocol, WKNavigationDelegate>  
@end  
  
@implementation RCTWebView {  
  NSURL * _sourceURL;  
  WKWebView * _webView;  
}  
  
-(instancetype)init  
{  
  if(self = [super init]) {  
    _webView = [WKWebView new];  
    _webView.navigationDelegate = self;  
    [self addSubview:_webView];  
  }  
  return self;  
}  
  
- (void)updateProps:(Props::Shared const &)props oldProps:(Props::Shared const &)oldProps  
{  
  const auto &oldViewProps = *std::static_pointer_cast<CustomWebViewProps const>(_props);  
  const auto &newViewProps = *std::static_pointer_cast<CustomWebViewProps const>(props);  
  
  // Handle your props here  
  if (oldViewProps.sourceURL != newViewProps.sourceURL) {  
    NSString *urlString = [NSString stringWithCString:newViewProps.sourceURL.c_str() encoding:NSUTF8StringEncoding];  
    _sourceURL = [NSURL URLWithString:urlString];  
    if ([self urlIsValid:newViewProps.sourceURL]) {  
      [_webView loadRequest:[NSURLRequest requestWithURL:_sourceURL]];  
    }  
  }  
  
  [super updateProps:props oldProps:oldProps];  
}  
  
-(void)layoutSubviews  
{  
  [super layoutSubviews];  
  _webView.frame = self.bounds;  
  
}  
  
#pragma mark - WKNavigationDelegate  
  
-(void)webView:(WKWebView *)webView didFinishNavigation:(WKNavigation *)navigation  
{  
  CustomWebViewEventEmitter::OnScriptLoaded result = CustomWebViewEventEmitter::OnScriptLoaded{CustomWebViewEventEmitter::OnScriptLoadedResult::Success};  
  self.eventEmitter.onScriptLoaded(result);  
}  
  
- (BOOL)urlIsValid:(std::string)propString  
{  
  if (propString.length() > 0 && !_sourceURL) {  
    CustomWebViewEventEmitter::OnScriptLoaded result = CustomWebViewEventEmitter::OnScriptLoaded{CustomWebViewEventEmitter::OnScriptLoadedResult::Error};  
  
    self.eventEmitter.onScriptLoaded(result);  
    return NO;  
  }  
  return YES;  
}  
  
// Event emitter convenience method  
- (const CustomWebViewEventEmitter &)eventEmitter  
{  
  return static_cast<const CustomWebViewEventEmitter &>(*_eventEmitter);  
}  
  
+ (ComponentDescriptorProvider)componentDescriptorProvider  
{  
  return concreteComponentDescriptorProvider<CustomWebViewComponentDescriptor>();  
}  
  
@end  

```

This code is written in Objective-C++ and contains various details:

* the `@interface` implements two protocols:
  + `RCTCustomWebViewViewProtocol`, generated by Codegen;
  + `WKNavigationDelegate`, provided by the WebKit framework to handle the web view navigation events;
* the `init` method that instantiates the `WKWebView`, adds it to the subviews and that sets the `navigationDelegate`;
* the `updateProps` method that is called by React Native when the component's props change;
* the `layoutSubviews` method that describes how the custom view needs to be laid out;
* the `webView:didFinishNavigation:` method that lets you handle what to do when the `WKWebView` finishes loading the page;
* the `urlIsValid:(std::string)propString` method that checks whether the URL received as prop is valid;
* the `eventEmitter` method which is a utility to retrieve a strongly typed `eventEmitter` instance
* the `componentDescriptorProvider` which returns the `ComponentDescriptor` generated by Codegen;

#### Add WebKit framework[​](#add-webkit-framework "Direct link to Add WebKit framework")

note

This step is only required because we are creating a Web view. Web components on iOS needs to be linked against the WebKit framework provided by Apple. If your component doesn't need to access web-specific features, you can skip this step.

A web view requires access to some features that Apple provides through one of the frameworks shipped with Xcode and the devices: WebKit.
You can see it in the native code by the `#import <WebKit/WebKit.h>` line added in the `RCTWebView.mm`.

To link the WebKit framework in your app, follow these steps:

1. In Xcode, Click on your project
2. Select the app target
3. Select the General tab
4. Scroll down until you find the *"Frameworks, Libraries, and Embedded Contents"* section, and press the `+` button

![Add webkit framework to your app 1](/docs/assets/AddWebKitFramework1.png)

5. In the search bar, filter for WebKit
6. Select the WebKit framework
7. Click on Add.

![Add webkit framework to your app 2](/docs/assets/AddWebKitFramework2.png)

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/fabric-native-components-ios.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/fabric-native-components-ios.md)

Last updated on **Apr 14, 2025**

* [1. Run Codegen](#1-run-codegen)* [3. Write the `RCTWebView`](#3-write-the-rctwebview)

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