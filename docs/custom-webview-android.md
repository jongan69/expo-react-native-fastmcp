Custom WebView · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.75](/docs/0.75/custom-webview-android)

* [Next](/docs/next/getting-started)* [0.79](/docs/getting-started)* [0.78](/docs/0.78/getting-started)* [0.77](/docs/0.77/getting-started)* [0.76](/docs/0.76/getting-started)* [0.75](/docs/0.75/custom-webview-android)* [0.74](/docs/0.74/custom-webview-android)* [0.73](/docs/0.73/custom-webview-android)* [0.72](/docs/0.72/custom-webview-android)* [0.71](/docs/0.71/custom-webview-android)* [0.70](/docs/0.70/custom-webview-android)* [All versions](/versions)

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

info

The React Native WebView component has been extracted to [`react-native-webview`](https://github.com/react-native-webview/react-native-webview) package as part of the [Lean Core effort](https://github.com/facebook/react-native/issues/23313).
That is the recommended way to use WebView in React Native as of today. You should not use the [WebView](https://reactnative-archive-august-2023.netlify.app/docs/0.61/webview) component as that was deprecated and removed from React Native.

Before you do this, you should be familiar with the concepts in [native UI components](/docs/0.75/native-components-android). You should also familiarise yourself with the [native code for web views](https://github.com/react-native-webview/react-native-webview/blob/master/android/src/main/java/com/reactnativecommunity/webview/RNCWebViewManagerImpl.kt), as you will have to use this as a reference when implementing new features—although a deep understanding is not required.

Native Code[​](#native-code "Direct link to Native Code")
---------------------------------------------------------

info

This example assumes you already have [`react-native-webview`](https://github.com/react-native-webview/react-native-webview) installed, if not please follow their [Getting Started guide](https://github.com/react-native-webview/react-native-webview/blob/master/docs/Getting-Started.md) first.

To get started, you'll need to create a subclass of `RNCWebViewManager`, `RNCWebView`, and `RNCWebViewClient`. In your view manager, you'll then need to override:

* `createRNCWebViewInstance`
* `getName`
* `addEventEmitters`

* Java* Kotlin

java

```
@ReactModule(name = CustomWebViewManager.REACT_CLASS)  
public class CustomWebViewManager extends RNCWebViewManager {  
  /* This name must match what we're referring to in JS */  
  protected static final String REACT_CLASS = "RCTCustomWebView";  
  
  protected static class CustomWebViewClient extends RNCWebViewClient { }  
  
  protected static class CustomWebView extends RNCWebView {  
    public CustomWebView(ThemedReactContext reactContext) {  
      super(reactContext);  
    }  
  }  
  
  @Override  
  protected RNCWebView createRNCWebViewInstance(ThemedReactContext reactContext) {  
    return new CustomWebView(reactContext);  
  }  
  
  @Override  
  public String getName() {  
    return REACT_CLASS;  
  }  
  
  @Override  
  protected void addEventEmitters(ThemedReactContext reactContext, WebView view) {  
    view.setWebViewClient(new CustomWebViewClient());  
  }  
}  

```

kotlin

```
@ReactModule(name = CustomWebViewManager.REACT_CLASS)  
class CustomWebViewManager : RNCWebViewManager() {  
    protected class CustomWebViewClient : RNCWebViewClient()  
    protected inner class CustomWebView(reactContext: ThemedReactContext?) :  
        RNCWebView(reactContext)  
  
    override fun createRNCWebViewInstance(reactContext: ThemedReactContext?): RNCWebView {  
        return CustomWebView(reactContext)  
    }  
  
    override fun addEventEmitters(reactContext: ThemedReactContext, view: WebView) {  
        view.webViewClient = CustomWebViewClient()  
    }  
  
    companion object {  
        /* This name must match what we're referring to in JS */  
        const val REACT_CLASS = "RCTCustomWebView"  
    }  
}  

```

You'll need to follow the usual steps to [register the module](/docs/0.75/native-modules-android#register-the-module).

### Adding New Properties[​](#adding-new-properties "Direct link to Adding New Properties")

To add a new property, you'll need to add it to `CustomWebView`, and then expose it in `CustomWebViewManager`.

* Java* Kotlin

java

```
public class CustomWebViewManager extends RNCWebViewManager {  
  ...  
  protected static class CustomWebView extends RNCWebView {  
    public CustomWebView(ThemedReactContext reactContext) {  
      super(reactContext);  
    }  
  
    protected @Nullable String mFinalUrl;  
  
    public void setFinalUrl(String url) {  
        mFinalUrl = url;  
    }  
  
    public String getFinalUrl() {  
        return mFinalUrl;  
    }  
  }  
  
  ...  
  
  @ReactProp(name = "finalUrl")  
  public void setFinalUrl(WebView view, String url) {  
    ((CustomWebView) view).setFinalUrl(url);  
  }  
}  

```

kotlin

```
class CustomWebViewManager : RNCWebViewManager() {  
    protected inner class CustomWebView(  
        reactContext: ThemedReactContext?,  
        var finalUrl: String? = null  
    ) : RNCWebView(reactContext)  
  
    @ReactProp(name = "finalUrl")  
    fun setFinalUrl(view: WebView, url: String?) {  
        (view as CustomWebView).finalUrl = url  
    }  
}  

```

### Adding New Events[​](#adding-new-events "Direct link to Adding New Events")

For events, you'll first need to make create event subclass.

* Java* Kotlin

java

```
// NavigationCompletedEvent.java  
public class NavigationCompletedEvent extends Event<NavigationCompletedEvent> {  
  private WritableMap mParams;  
  
  public NavigationCompletedEvent(int viewTag, WritableMap params) {  
    super(viewTag);  
    this.mParams = params;  
  }  
  
  @Override  
  public String getEventName() {  
    return "navigationCompleted";  
  }  
  
  @Override  
  public void dispatch(RCTEventEmitter rctEventEmitter) {  
    init(getViewTag());  
    rctEventEmitter.receiveEvent(getViewTag(), getEventName(), mParams);  
  }  
}  

```

kotlin

```
// NavigationCompletedEvent.kt  
class NavigationCompletedEvent(viewTag: Int, val params: WritableMap) :  
    Event<NavigationCompletedEvent>(viewTag) {  
    override fun getEventName(): String = "navigationCompleted"  
  
    override fun dispatch(rctEventEmitter: RCTEventEmitter) {  
        init(viewTag)  
        rctEventEmitter.receiveEvent(viewTag, eventName, params)  
    }  
}  

```

You can trigger the event in your web view client. You can hook existing handlers if your events are based on them.

You should refer to [RNCWebViewManagerImpl.kt](https://github.com/react-native-webview/react-native-webview/blob/master/android/src/main/java/com/reactnativecommunity/webview/RNCWebViewManagerImpl.kt) in the React Native WebView codebase to see what handlers are available and how they are implemented. You can extend any methods here to provide extra functionality.

* Java* Kotlin

java

```
public class NavigationCompletedEvent extends Event<NavigationCompletedEvent> {  
  private WritableMap mParams;  
  
  public NavigationCompletedEvent(int viewTag, WritableMap params) {  
    super(viewTag);  
    this.mParams = params;  
  }  
  
  @Override  
  public String getEventName() {  
    return "navigationCompleted";  
  }  
  
  @Override  
  public void dispatch(RCTEventEmitter rctEventEmitter) {  
    init(getViewTag());  
    rctEventEmitter.receiveEvent(getViewTag(), getEventName(), mParams);  
  }  
}  
  
// CustomWebViewManager.java  
protected static class CustomWebViewClient extends RNCWebViewClient {  
  @Override  
  public boolean shouldOverrideUrlLoading(WebView view, String url) {  
    boolean shouldOverride = super.shouldOverrideUrlLoading(view, url);  
    String finalUrl = ((CustomWebView) view).getFinalUrl();  
  
    if (!shouldOverride && url != null && finalUrl != null && new String(url).equals(finalUrl)) {  
      final WritableMap params = Arguments.createMap();  
      dispatchEvent(view, new NavigationCompletedEvent(view.getId(), params));  
    }  
  
    return shouldOverride;  
  }  
}  

```

kotlin

```
class NavigationCompletedEvent(viewTag: Int, val params: WritableMap) :  
    Event<NavigationCompletedEvent>(viewTag) {  
  
    override fun getEventName(): String = "navigationCompleted"  
  
    override fun dispatch(rctEventEmitter: RCTEventEmitter) {  
        init(viewTag)  
        rctEventEmitter.receiveEvent(viewTag, eventName, params)  
    }  
}  
  
// CustomWebViewManager.kt  
  
protected class CustomWebViewClient : RNCWebViewClient() {  
    override fun shouldOverrideUrlLoading(view: WebView, url: String?): Boolean {  
        val shouldOverride: Boolean = super.shouldOverrideUrlLoading(view, url)  
        val finalUrl: String? = (view as CustomWebView).finalUrl  
        if (!shouldOverride && url != null && finalUrl != null && url == finalUrl) {  
            val params: WritableMap = Arguments.createMap()  
            dispatchEvent(view, NavigationCompletedEvent(view.getId(), params))  
        }  
        return shouldOverride  
    }  
}  

```

Finally, you'll need to expose the events in `CustomWebViewManager` through `getExportedCustomDirectEventTypeConstants`. Note that currently, the default implementation returns `null`, but this may change in the future.

* Java* Kotlin

java

```
public class CustomWebViewManager extends RNCWebViewManager {  
  ...  
  
  @Override  
  public @Nullable  
  Map getExportedCustomDirectEventTypeConstants() {  
    Map<String, Object> export = super.getExportedCustomDirectEventTypeConstants();  
    if (export == null) {  
      export = MapBuilder.newHashMap();  
    }  
    export.put("navigationCompleted", MapBuilder.of("registrationName", "onNavigationCompleted"));  
    return export;  
  }  
}  

```

kotlin

```
class CustomWebViewManager : RNCWebViewManager() {  
    override fun getExportedCustomDirectEventTypeConstants(): MutableMap<Any?, Any?>? {  
        val superTypeConstants = super.getExportedCustomDirectEventTypeConstants()  
        val export = superTypeConstants ?: MapBuilder.newHashMap<Any, Any?>()  
        export["navigationCompleted"] = MapBuilder.of("registrationName", "onNavigationCompleted")  
        return export  
    }  
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
import {WebView, requireNativeComponent} from 'react-native';  
  
export default class CustomWebView extends Component {  
  static propTypes = WebView.propTypes;  
  
  render() {  
    return (  
      <WebView  
        {...this.props}  
        nativeConfig={{component: RCTCustomWebView}}  
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

If you want to add custom props to your native component, you can use `nativeConfig.props` on the web view.

For events, the event handler must always be set to a function. This means it isn't safe to use the event handler directly from `this.props`, as the user might not have provided one. The standard approach is to create an event handler in your class, and then invoking the event handler given in `this.props` if it exists.

If you are unsure how something should be implemented from the JS side, look at [WebView.android.js](https://github.com/react-native-webview/react-native-webview/blob/master/src/WebView.android.tsx) in the React Native WebView source.

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

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/custom-webview-android.md)[Edit page for 0.75 release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.75/custom-webview-android.md)

Last updated on **Jan 4, 2025**

* [Native Code](#native-code)
  + [Adding New Properties](#adding-new-properties)+ [Adding New Events](#adding-new-events)* [JavaScript Interface](#javascript-interface)

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