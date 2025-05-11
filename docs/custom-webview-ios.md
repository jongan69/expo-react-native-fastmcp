Custom WebView · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.75](/docs/0.75/custom-webview-ios)

* [Next](/docs/next/getting-started)* [0.79](/docs/getting-started)* [0.78](/docs/0.78/getting-started)* [0.77](/docs/0.77/getting-started)* [0.76](/docs/0.76/getting-started)* [0.75](/docs/0.75/custom-webview-ios)* [0.74](/docs/0.74/custom-webview-ios)* [0.73](/docs/0.73/custom-webview-ios)* [0.72](/docs/0.72/custom-webview-ios)* [0.71](/docs/0.71/custom-webview-ios)* [0.70](/docs/0.70/custom-webview-ios)* [All versions](/versions)

[Development](#)

* [Guides](/docs/0.75/getting-started)* [Components](/docs/0.75/components-and-apis)* [APIs](/docs/0.75/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

This is documentation for React Native **0.75**, which is no longer in active development.

For up-to-date documentation, see the **[latest version](/docs/getting-started)** (0.79).

Version: 0.75

On this page

Custom WebView
==============

While the built-in web view has a lot of features, it is not possible to handle every use-case in React Native. You can, however, extend the web view with native code without forking React Native or duplicating all the existing web view code.

Before you do this, you should be familiar with the concepts in [native UI components](/docs/0.75/native-components-ios). You should also familiarise yourself with the [native code for web views](https://github.com/react-native-webview/react-native-webview/blob/master/apple/RNCWebViewManager.mm), as you will have to use this as a reference when implementing new features—although a deep understanding is not required.

Native Code[​](#native-code "Direct link to Native Code")
---------------------------------------------------------

Like for regular native components, you need a view manager and a web view.

For the view, you'll need to make a subclass of `RCTWebView`.

objc

```
// RCTCustomWebView.h  
#import <React/RCTWebView.h>  
  
@interface RCTCustomWebView : RCTWebView  
  
@end  
  
// RCTCustomWebView.m  
#import "RCTCustomWebView.h"  
  
@interface RCTCustomWebView ()  
  
@end  
  
@implementation RCTCustomWebView { }  
  
@end  

```

For the view manager, you need to make a subclass `RCTWebViewManager`. You must still include:

* `(UIView *)view` that returns your custom view
* The `RCT_EXPORT_MODULE()` tag

objc

```
// RCTCustomWebViewManager.h  
#import <React/RCTWebViewManager.h>  
  
@interface RCTCustomWebViewManager : RCTWebViewManager  
  
@end  
  
// RCTCustomWebViewManager.m  
#import "RCTCustomWebViewManager.h"  
#import "RCTCustomWebView.h"  
  
@interface RCTCustomWebViewManager () <RCTWebViewDelegate>  
  
@end  
  
@implementation RCTCustomWebViewManager { }  
  
RCT_EXPORT_MODULE()  
  
- (UIView *)view  
{  
  RCTCustomWebView *webView = [RCTCustomWebView new];  
  webView.delegate = self;  
  return webView;  
}  
  
@end  

```

### Adding New Events and Properties[​](#adding-new-events-and-properties "Direct link to Adding New Events and Properties")

Adding new properties and events is the same as regular UI components. For properties, you define an `@property` in the header. For events, you define a `RCTDirectEventBlock` in the view's `@interface`.

objc

```
// RCTCustomWebView.h  
@property (nonatomic, copy) NSString *finalUrl;  
  
// RCTCustomWebView.m  
@interface RCTCustomWebView ()  
  
@property (nonatomic, copy) RCTDirectEventBlock onNavigationCompleted;  
  
@end  

```

Then expose it in the view manager's `@implementation`.

objc

```
// RCTCustomWebViewManager.m  
RCT_EXPORT_VIEW_PROPERTY(onNavigationCompleted, RCTDirectEventBlock)  
RCT_EXPORT_VIEW_PROPERTY(finalUrl, NSString)  

```

### Extending Existing Events[​](#extending-existing-events "Direct link to Extending Existing Events")

You should refer to [RCTWebView.mm](https://github.com/react-native-webview/react-native-webview/blob/master/apple/RNCWebView.mm) in the React Native WebView codebase to see what handlers are available and how they are implemented. You can extend any methods here to provide extra functionality.

By default, most methods aren't exposed from RCTWebView. If you need to expose them, you need to create an [Objective C category](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/CustomizingExistingClasses/CustomizingExistingClasses.html), and then expose all the methods you need to use.

objc

```
// RCTWebView+Custom.h  
#import <React/RCTWebView.h>  
  
@interface RCTWebView (Custom)  
- (BOOL)webView:(__unused UIWebView *)webView shouldStartLoadWithRequest:(NSURLRequest *)request navigationType:(UIWebViewNavigationType)navigationType;  
- (NSMutableDictionary<NSString *, id> *)baseEvent;  
@end  

```

Once these are exposed, you can reference them in your custom web view class.

objc

```
// RCTCustomWebView.m  
  
// Remember to import the category file.  
#import "RCTWebView+Custom.h"  
  
- (BOOL)webView:(__unused UIWebView *)webView shouldStartLoadWithRequest:(NSURLRequest *)request  
 navigationType:(UIWebViewNavigationType)navigationType  
{  
  BOOL allowed = [super webView:webView shouldStartLoadWithRequest:request navigationType:navigationType];  
  
  if (allowed) {  
    NSString* url = request.URL.absoluteString;  
    if (url && [url isEqualToString:_finalUrl]) {  
      if (_onNavigationCompleted) {  
        NSMutableDictionary<NSString *, id> *event = [self baseEvent];  
        _onNavigationCompleted(event);  
      }  
    }  
  }  
  
  return allowed;  
}  

```

JavaScript Interface[​](#javascript-interface "Direct link to JavaScript Interface")
------------------------------------------------------------------------------------

To use your custom web view, you'll need to create a class for it. Your class must:

* Export all the prop types from `WebView.propTypes`
* Return a `WebView` component with the prop `nativeConfig.component` set to your native component (see below)

To get your native component, you must use `requireNativeComponent`: the same as for regular custom components. However, you must pass in an extra third argument, `WebView.extraNativeComponentConfig`. This third argument contains prop types that are only required for native code.

jsx

```
import React, {Component, PropTypes} from 'react';  
import {  
  WebView,  
  requireNativeComponent,  
  NativeModules,  
} from 'react-native';  
const {CustomWebViewManager} = NativeModules;  
  
export default class CustomWebView extends Component {  
  static propTypes = WebView.propTypes;  
  
  render() {  
    return (  
      <WebView  
        {...this.props}  
        nativeConfig={{  
          component: RCTCustomWebView,  
          viewManager: CustomWebViewManager,  
        }}  
      />  
    );  
  }  
}  
  
const RCTCustomWebView = requireNativeComponent(  
  'RCTCustomWebView',  
  CustomWebView,  
  WebView.extraNativeComponentConfig,  
);  

```

If you want to add custom props to your native component, you can use `nativeConfig.props` on the web view. For iOS, you should also set the `nativeConfig.viewManager` prop with your custom WebView ViewManager as in the example above.

For events, the event handler must always be set to a function. This means it isn't safe to use the event handler directly from `this.props`, as the user might not have provided one. The standard approach is to create an event handler in your class, and then invoking the event handler given in `this.props` if it exists.

If you are unsure how something should be implemented from the JS side, look at [WebView.ios.tsx](https://github.com/react-native-webview/react-native-webview/blob/master/src/WebView.ios.tsx) in the React Native source.

jsx

```
export default class CustomWebView extends Component {  
  static propTypes = {  
    ...WebView.propTypes,  
    finalUrl: PropTypes.string,  
    onNavigationCompleted: PropTypes.func,  
  };  
  
  static defaultProps = {  
    finalUrl: 'about:blank',  
  };  
  
  _onNavigationCompleted = event => {  
    const {onNavigationCompleted} = this.props;  
    onNavigationCompleted && onNavigationCompleted(event);  
  };  
  
  render() {  
    return (  
      <WebView  
        {...this.props}  
        nativeConfig={{  
          component: RCTCustomWebView,  
          props: {  
            finalUrl: this.props.finalUrl,  
            onNavigationCompleted: this._onNavigationCompleted,  
          },  
          viewManager: CustomWebViewManager,  
        }}  
      />  
    );  
  }  
}  

```

Similar to regular native components, you must provide all your prop types in the component to have them forwarded on to the native component. However, if you have some prop types that are only used internally in component, you can add them to the `nativeOnly` property of the third argument previously mentioned. For event handlers, you have to use the value `true` instead of a regular prop type.

For example, if you wanted to add an internal event handler called `onScrollToBottom`, you would use,

jsx

```
const RCTCustomWebView = requireNativeComponent(  
  'RCTCustomWebView',  
  CustomWebView,  
  {  
    ...WebView.extraNativeComponentConfig,  
    nativeOnly: {  
      ...WebView.extraNativeComponentConfig.nativeOnly,  
      onScrollToBottom: true,  
    },  
  },  
);  

```

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/custom-webview-ios.md)[Edit page for 0.75 release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.75/custom-webview-ios.md)

Last updated on **Jan 4, 2025**

* [Native Code](#native-code)
  + [Adding New Events and Properties](#adding-new-events-and-properties)+ [Extending Existing Events](#extending-existing-events)* [JavaScript Interface](#javascript-interface)

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