Integration with an Android Fragment · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/integration-with-android-fragment)

* [Next](/docs/next/integration-with-android-fragment)* [0.79](/docs/integration-with-android-fragment)* [0.78](/docs/0.78/integration-with-android-fragment)* [0.77](/docs/0.77/integration-with-android-fragment)* [0.76](/docs/0.76/integration-with-android-fragment)* [0.75](/docs/0.75/integration-with-android-fragment)* [0.74](/docs/0.74/integration-with-android-fragment)* [0.73](/docs/0.73/integration-with-android-fragment)* [0.72](/docs/0.72/integration-with-android-fragment)* [0.71](/docs/0.71/integration-with-android-fragment)* [0.70](/docs/0.70/integration-with-android-fragment)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [The Basics](/docs/getting-started)

  * [Environment setup](/docs/environment-setup)

    + [Get Started with React Native](/docs/environment-setup)+ [Set Up Your Environment](/docs/set-up-your-environment)+ [Integration with Existing Apps](/docs/integration-with-existing-apps)+ [Integration with an Android Fragment](/docs/integration-with-android-fragment)+ [Building For TV Devices](/docs/building-for-tv)+ [Out-of-Tree Platforms](/docs/out-of-tree-platforms)* [Workflow](/docs/running-on-device)

      * [UI & Interaction](/docs/style)

        * [Debugging](/docs/debugging)

          * [Testing](/docs/testing-overview)

            * [Performance](/docs/performance)

              * [JavaScript Runtime](/docs/javascript-environment)

                * [Codegen](/docs/the-new-architecture/what-is-codegen)

                  * [Native Development](/docs/native-platform)

                    * [Android and iOS guides](/docs/headless-js-android)

                      * [Legacy Architecture](/docs/legacy/native-modules-intro)

On this page

Integration with an Android Fragment
====================================

The guide for [Integration with Existing Apps](https://reactnative.dev/docs/integration-with-existing-apps) details how to integrate a full-screen React Native app into an existing Android app as an **Activity**.

To use React Native components within **Fragments** in an existing app requires some additional setup.

### 1. Add React Native to your app[​](#1-add-react-native-to-your-app "Direct link to 1. Add React Native to your app")

Follow the guide for [Integration with Existing Apps](https://reactnative.dev/docs/integration-with-existing-apps) until the end to make sure you can safely run your React Native app in a full screen Activity.

### 2. Add a FrameLayout for the React Native Fragment[​](#2-add-a-framelayout-for-the-react-native-fragment "Direct link to 2. Add a FrameLayout for the React Native Fragment")

In this example, we're going to use a `FrameLayout` to add a React Native Fragment to an Activity. This approach is flexible enough and can be adapted to use React Native in other layouts such as Bottom Sheets or Tab Layouts.

First add a `<FrameLayout>` with an id, width and height to your Activity's layout (e.g. `main_activity.xml` in the `res/layouts` folder). This is the layout you will find to render your React Native Fragment.

xml

```
<FrameLayout  
    android:id="@+id/react_native_fragment"  
    android:layout_width="match_parent"  
    android:layout_height="match_parent" />  

```

### 3. Make your host Activity implement `DefaultHardwareBackBtnHandler`[​](#3-make-your-host-activity-implement-defaulthardwarebackbtnhandler "Direct link to 3-make-your-host-activity-implement-defaulthardwarebackbtnhandler")

As your host activity is not a `ReactActivity`, you need to implement the `DefaultHardwareBackBtnHandler` interface to handle the back button press event.
This is required by React Native to handle the back button press event.

Go into your host activity and make sure it implements the `DefaultHardwareBackBtnHandler` interface:

* Java* Kotlin

diff

```
package <your-package-here>  
  
import android.os.Bundle  
import androidx.appcompat.app.AppCompatActivity  
+import com.facebook.react.modules.core.DefaultHardwareBackBtnHandler  
  
+class MainActivity : AppCompatActivity() {  
+class MainActivity : AppCompatActivity(), DefaultHardwareBackBtnHandler {  
  
    override fun onCreate(savedInstanceState: Bundle?) {  
        super.onCreate(savedInstanceState)  
        setContentView(R.layout.main_activity)  
  
        findViewById<Button>(R.id.sample_button).setOnClickListener {  
            // Handle button click  
        }  
    }  
  
+   override fun invokeDefaultOnBackPressed() {  
+       super.onBackPressed()  
+   }  
}  

```

diff

```
package <your-package-here>;  
  
import android.os.Bundle;  
import androidx.appcompat.app.AppCompatActivity;  
+import com.facebook.react.modules.core.DefaultHardwareBackBtnHandler;  
  
-class MainActivity extends AppCompatActivity {  
+class MainActivity extends AppCompatActivity implements DefaultHardwareBackBtnHandler {  
  
    @Override  
    protected void onCreate(@Nullable Bundle savedInstanceState) {  
        super.onCreate(savedInstanceState);  
        setContentView(R.layout.main_activity);  
  
        findViewById(R.id.button_appcompose).setOnClickListener(button -> {  
            // Handle button click  
        });  
    }  
  
+   @Override  
+   public void invokeDefaultOnBackPressed() {  
+       super.onBackPressed();  
+   }  
}  

```

### 4. Add a React Native Fragment to the FrameLayout[​](#4-add-a-react-native-fragment-to-the-framelayout "Direct link to 4. Add a React Native Fragment to the FrameLayout")

Finally, we can update the Activity to add a React Native Fragment to the FrameLayout.
In this specific example, we're going to assume that your Activity has a button with id `sample_button` that when clicked will render a React Native Fragment into the FrameLayout.

Update your Activity's `onCreate` method as follows:

* Java* Kotlin

diff

```
package <your-package-here>  
  
import android.os.Bundle  
import androidx.appcompat.app.AppCompatActivity  
+import com.facebook.react.ReactFragment  
import com.facebook.react.modules.core.DefaultHardwareBackBtnHandler  
  
public class MainActivity : AppCompatActivity(), DefaultHardwareBackBtnHandler {  
  
    override fun onCreate(savedInstanceState: Bundle?) {  
        super.onCreate(savedInstanceState)  
        setContentView(R.layout.main_activity)  
  
        findViewById<Button>(R.id.sample_button).setOnClickListener {  
+           val reactNativeFragment = ReactFragment.Builder()  
+               .setComponentName("HelloWorld")  
+               .setLaunchOptions(Bundle().apply { putString("message", "my value") })  
+               .build()  
+           supportFragmentManager  
+               .beginTransaction()  
+               .add(R.id.react_native_fragment, reactNativeFragment)  
+               .commit()  
        }  
    }  
  
   override fun invokeDefaultOnBackPressed() {  
       super.onBackPressed()  
   }  
}  

```

diff

```
package <your-package-here>;  
  
import android.os.Bundle;  
import androidx.appcompat.app.AppCompatActivity;  
+import com.facebook.react.ReactFragment;  
import com.facebook.react.modules.core.DefaultHardwareBackBtnHandler;  
  
public class MainActivity extends AppCompatActivity implements DefaultHardwareBackBtnHandler {  
  
    @Override  
    protected void onCreate(@Nullable Bundle savedInstanceState) {  
        super.onCreate(savedInstanceState);  
        setContentView(R.layout.main_activity);  
  
        findViewById(R.id.button_appcompose).setOnClickListener(button -> {  
+           Bundle launchOptions = new Bundle();  
+           launchOptions.putString("message", "my value");  
+  
+           ReactFragment fragment = new ReactFragment.Builder()  
+                   .setComponentName("HelloWorld")  
+                   .setLaunchOptions(launchOptions)  
+                   .build();  
+           getSupportFragmentManager()  
+                   .beginTransaction()  
+                   .add(R.id.react_native_fragment, fragment)  
+                   .commit();  
        });  
    }  
  
    @Override  
    public void invokeDefaultOnBackPressed() {  
        super.onBackPressed();  
    }  
}  

```

Let's look at the code above.

The `ReactFragment.Builder()` is used to create a new `ReactFragment` and then we use the `supportFragmentManager` to add that Fragment to the `FrameLayout`.

Inside the builder you can customize how the fragment is created:

* `setComponentName` is the name of the component you want to render. It's the same string specified in your `index.js` inside the `registerComponent` method.
* `setLaunchOptions` is an optional method to pass initial props to your component. This is optional and you can remove it if you don't use it.

### 5. Test your integration[​](#5-test-your-integration "Direct link to 5. Test your integration")

Make sure you run `yarn start` to run the bundler and then run your android app in Android Studio. The app should load the JavaScript/TypeScript code from the development server and display it in your React Native Fragment in the Activity.

Your app should look like this one:

![Screenshot](/assets/images/EmbeddedAppAndroidFragmentVideo-82fb8da16f6e27f6ce948561c0185589.gif)

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/integration-with-android-fragment.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/integration-with-android-fragment.md)

Last updated on **Apr 14, 2025**

[Previous

Integration with Existing Apps](/docs/integration-with-existing-apps)[Next

Building For TV Devices](/docs/building-for-tv)

* [1. Add React Native to your app](#1-add-react-native-to-your-app)* [2. Add a FrameLayout for the React Native Fragment](#2-add-a-framelayout-for-the-react-native-fragment)* [3. Make your host Activity implement `DefaultHardwareBackBtnHandler`](#3-make-your-host-activity-implement-defaulthardwarebackbtnhandler)* [4. Add a React Native Fragment to the FrameLayout](#4-add-a-react-native-fragment-to-the-framelayout)* [5. Test your integration](#5-test-your-integration)

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