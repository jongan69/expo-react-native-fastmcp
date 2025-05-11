Wrap third-party native libraries - Expo Documentation

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

[Create a native module](/modules/native-module-tutorial)[Create a native view](/modules/native-view-tutorial)[Create a module with a config plugin](/modules/config-plugin-and-native-module-tutorial)[How to use a standalone Expo module](/modules/use-standalone-expo-module-in-your-project)[Wrap third-party native libraries](/modules/third-party-library)[Integrate in an existing library](/modules/existing-library)[Additional platform support](/modules/additional-platform-support)

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

Wrap third-party native libraries
=================================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/modules/third-party-library.mdx)

Learn how to create a simple wrapper around two separate native libraries using Expo Modules API.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/modules/third-party-library.mdx)

---

Expo modules make it possible to easily use native, external libraries built for Android and iOS in React Native projects. This tutorial focuses on utilizing the Expo Modules API to create radial charts using two similar libraries accessible on both native platforms.

* [MPAndroidChart by PhilJay](https://github.com/PhilJay/MPAndroidChart)
* [Charts by Daniel Cohen Gindi](https://github.com/danielgindi/Charts)

The iOS library is inspired by the Android library, so they both have similar API and functionality. This makes them a good example for this tutorial.

[![How to wrap native libraries](https://i3.ytimg.com/vi/M8eNfH1o0eE/maxresdefault.jpg)

How to wrap native libraries

In this video you will learn how to wrap native libraries using Expo Modules API.](https://www.youtube.com/watch?v=M8eNfH1o0eE)


---

1

Create a new module
-------------------

The following steps assume that the new module is created inside a new Expo project. However, you can create a new module inside an existing project by following the alternative instructions.

### Start with a new project

Create a new empty Expo module that can be published on npm and utilized in any Expo app by running the following command:

Terminal

Copy

`-Â``npx create-expo-module expo-radial-chart`

> Tip: If you aren't going to ship this library, press `return` for all the prompts to accept the default values in the terminal window.

Now, open the newly created `expo-radial-chart` directory to start editing the native code.

### Start with an existing project

Alternatively, you can use the new module as a view inside the existing project. Run the following command in your project's directory:

Terminal

Copy

`-Â``npx create-expo-module --local expo-radial-chart`

Now, open the newly created `modules/expo-radial-chart` directory to start editing the native code.

2

Run the example project
-----------------------

To verify that everything is functioning correctly, let's run the example project. In a terminal window, start the TypeScript compiler to watch for changes and rebuild the module JavaScript:

Terminal

Copy

`# Run this in the root of the project to start the TypeScript compiler`

`-Â``npm run build`

In another terminal window, compile and run the example app:

Terminal

`-Â``cd example`

`# Run the example app on Android`

`-Â``npx expo run:android`

`# Run the example app on iOS`

`-Â``npx expo run:ios`

3

Add native dependencies
-----------------------

Add the native dependencies to the module by editing the android/build.gradle and ios/ExpoRadialChart.podspec files:

android/build.gradle

Copy

```
dependencies {
  implementation project(':expo-modules-core')
  implementation "org.jetbrains.kotlin:kotlin-stdlib-jdk7:${getKotlinVersion()}"
+ implementation 'com.github.PhilJay:MPAndroidChart:v3.1.0'
}

```

ios/ExpoRadialChart.podspec

Copy

```
  s.static_framework = true

  s.dependency 'ExpoModulesCore'
+ s.dependency 'DGCharts', '~> 5.1.0'

  # Swift/Objective-C compatibility

```

Are you trying to use a `.aar` dependency?

SDK 52 and above

SDK 51 and below

Inside the android directory, create another directory called libs and place the .aar file inside it. Then, add the file as a Gradle project from autolinking:

expo-module.config.json

Copy

```
    "android": {
+     "gradleAarProjects": [
+       {
+         "name": "test-aar",
+         "aarFilePath": "android/libs/test.aar"
+       }
+     ],
    "modules": [

```

Finally, add the dependency to the `dependencies` list in the android/build.gradle file, using the dependency's specified name with `${project.name}$` prefix:

android/build.gradle

Copy

```
dependencies {
  implementation project(':expo-modules-core')
  implementation "org.jetbrains.kotlin:kotlin-stdlib-jdk7:${getKotlinVersion()}"
+ implementation project(":${project.name}\$test-aar")
}

```

Inside the android directory, create another directory called libs and place the .aar file inside it. Then, add the directory as a repository:

android/build.gradle

Copy

```
  repositories {
    mavenCentral()
+   flatDir {
+       dirs 'libs'
+   }
  }

```

Finally, add the dependency to the `dependencies` list. Instead of the filename, use the package path, which includes the `@aar` at the end:

android/build.gradle

Copy

```
dependencies {
  implementation project(':expo-modules-core')
  implementation "org.jetbrains.kotlin:kotlin-stdlib-jdk7:${getKotlinVersion()}"
+ implementation 'com.github.PhilJay:MPAndroidChart:v3.1.0@aar'
}

```

Are you trying to use an `.xcframework` or `.framework` dependency?

On iOS, you can also use dependencies bundled as a framework by using the `vendored_frameworks` config option.

ios/ExpoRadialChart.podspec

Copy

```
    s.static_framework = true
    s.dependency 'ExpoModulesCore'
+   s.vendored_frameworks = 'Frameworks/MyFramework.framework'
    # Swift/Objective-C compatibility

```

> Note: The file pattern used to specify the path to the framework is relative to the podspec file,
> and doesn't support traversing the parent directory (`..`), meaning you need to place the framework inside the ios directory
> (or a subdirectory of ios).

Once the framework is added, make sure that the `source_files` option file pattern doesn't match any files inside the framework. One way to achieve this is to move your iOS source Swift files (that is `ExpoRadialChartView.swift` and `ExpoRadialChartModule.swift`) into a src directory separate from where you placed your framework(s) and update the `source_files` option to only match the src directory:

ios/ExpoRadialChart.podspec

Copy

```
- s.source_files = '**/*.{h,m,mm,swift,hpp,cpp}'
+ s.source_files = 'src/**/*.{h,m,mm,swift,hpp,cpp}'

```

Your ios directory should end up with a file structure similar to this:

`Frameworks`

â`MyFramework.framework`

`src`

â`ExpoRadialChartView.swift`

â`ExpoRadialChartModule.swift`

`ExpoRadialChart.podspec`

4

Define an API
-------------

To use the module in the app, define the types for the props. It accepts a list of series â each with a color and a percentage value.

src/ExpoRadialChart.types.ts

Copy

```
import { ViewStyle } from 'react-native/types';

export type ChangeEventPayload = {
  value: string;
};

type Series = {
  color: string;
  percentage: number;
};

export type ExpoRadialChartViewProps = {
  style?: ViewStyle;
  data: Series[];
};

```

Since the module isn't implemented for web in this example, let's replace the src/ExpoRadialChartView.web.tsx file:

src/ExpoRadialChartView.web.tsx

Copy

```
import * as React from 'react';

export default function ExpoRadialChartView() {
  return <div>Not implemented</div>;
}

```

5

Implement the module on Android
-------------------------------

Now you can implement the native functionality by editing the placeholder files with the following changes:

1. Create a `PieChart` instance and set its `layoutParams` to match the parent view. Then, add it to the view hierarchy using the `addView` function.
2. Define a `setChartData` function that accepts a list of `Series` objects. You can iterate over the list, create a `PieEntry` for each series and store the colors in a separate list.
3. Create a `PieDataSet`, use it to create a `PieData` object, and set it as data on the `PieChart` instance.

android/src/main/java/expo/modules/radialchart/ExpoRadialChartView.kt

Copy

```
package expo.modules.radialchart

import android.content.Context
import android.graphics.Color
import androidx.annotation.ColorInt
import com.github.mikephil.charting.charts.PieChart
import com.github.mikephil.charting.data.PieData
import com.github.mikephil.charting.data.PieDataSet
import com.github.mikephil.charting.data.PieEntry
import expo.modules.kotlin.AppContext
import expo.modules.kotlin.records.Field
import expo.modules.kotlin.records.Record
import expo.modules.kotlin.views.ExpoView


class Series : Record {
  @Field
  val color: String = "#ff0000"

  @Field
  val percentage: Float = 0.0f
}

class ExpoRadialChartView(context: Context, appContext: AppContext) : ExpoView(context, appContext) {
  internal val chartView = PieChart(context).also {
    it.layoutParams = LayoutParams(LayoutParams.MATCH_PARENT, LayoutParams.MATCH_PARENT)
    addView(it)
  }

  fun setChartData(data: ArrayList<Series>) {
    val entries: ArrayList<PieEntry> = ArrayList()
    val colors: ArrayList<Int> = ArrayList()
    for (series in data) {
      entries.add(PieEntry(series.percentage))
      colors.add(Color.parseColor(series.color))
    }
    val dataSet = PieDataSet(entries, "DataSet");
    dataSet.colors = colors;
    val pieData = PieData(dataSet);
    chartView.data = pieData;
    chartView.invalidate();

  }
}

```

You also need to use the [`Prop`](/modules/module-api#prop) function to define the `data` prop and call the native `setChartData` function when the prop changes:

android/src/main/java/expo/modules/radialchart/ExpoRadialChartModule.kt

Copy

```
package expo.modules.radialchart

import expo.modules.kotlin.modules.Module
import expo.modules.kotlin.modules.ModuleDefinition

class ExpoRadialChartModule : Module() {
  override fun definition() = ModuleDefinition {
    Name("ExpoRadialChart")

    View(ExpoRadialChartView::class) {
      Prop("data") { view: ExpoRadialChartView, prop: ArrayList<Series> ->
        view.setChartData(prop);
      }
    }
  }
}

```

6

Implement the module on iOS
---------------------------

Now you can implement the native functionality by editing the placeholder files with the following changes:

1. Create a new `PieChartView` instance and use the `addSubview` function to add it to the view hierarchy.
2. Set the `clipsToBounds` property and override the `layoutSubviews` function to make sure the chart view is always the same size as the parent view.
3. Create a `setChartData` function that accepts a list of series, creates a `PieChartDataSet` instance with the data, and assigns it to the `data` property of the `PieChartView` instance.

ios/ExpoRadialChartView.swift

Copy

```
import ExpoModulesCore
import DGCharts

struct Series: Record {
  @Field
  var color: UIColor = UIColor.black

  @Field
  var percentage: Double = 0
}

class ExpoRadialChartView: ExpoView {
  let chartView = PieChartView()

  required init(appContext: AppContext? = nil) {
    super.init(appContext: appContext)
    clipsToBounds = true
    addSubview(chartView)
  }

  override func layoutSubviews() {
    chartView.frame = bounds
  }

  func setChartData(data: [Series]) {
    let set1 = PieChartDataSet(entries: data.map({ (series: Series) -> PieChartDataEntry in
      return PieChartDataEntry(value: series.percentage)
    }))
    set1.colors = data.map({ (series: Series) -> UIColor in
      return series.color
    })
    let chartData: PieChartData = [set1]
    chartView.data = chartData
  }
}

```

You also need to use the [`Prop`](/modules/module-api#prop) function to define the `data` prop and call the native `setChartData` function when the prop changes:

ios/ExpoRadialChartModule.swift

Copy

```
import ExpoModulesCore

public class ExpoRadialChartModule: Module {
  public func definition() -> ModuleDefinition {
    Name("ExpoRadialChart")

    View(ExpoRadialChartView.self) {
      Prop("data") { (view: ExpoRadialChartView, prop: [Series]) in
        view.setChartData(data: prop)
      }
    }
  }
}

```

7

Write an example app to use the module
--------------------------------------

You can update the app inside the example directory to test the module. Use the `ExpoRadialChartView` component to render a pie chart with three slices:

example/App.tsx

Copy

```
import { ExpoRadialChartView } from 'expo-radial-chart';
import { StyleSheet } from 'react-native';

export default function App() {
  return (
    <ExpoRadialChartView
      style={styles.container}
      data={[
        {
          color: '#ff0000',
          percentage: 0.5,
        },
        {
          color: '#00ff00',
          percentage: 0.2,
        },
        {
          color: '#0000ff',
          percentage: 0.3,
        },
      ]}
    />
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
});

```

> Tip: If you created the module inside an existing app, make sure to import it directly from your modules directory by using a relative import: `import { ExpoRadialChartView } from '../modules/expo-radial-chart';`

8

Rebuild and launch your application
-----------------------------------

To make sure your app builds successfully on both platforms, rerun the build commands from step 2. After the app is successfully built on any of the platform you'll see a pie chart with three slices:

![A PieChart module on Android and iOS](/static/images/modules/third-party-library/result.webp)

Congratulations! You have created your first simple wrapper around two separate third-party native libraries using Expo Modules API.

Next step
---------

[Expo Modules API Reference

A reference to create native modules using Kotlin and Swift.](/modules/module-api)

[Previous (Expo Modules API - Tutorials)

How to use a standalone Expo module](/modules/use-standalone-expo-module-in-your-project)[Next (Expo Modules API - Tutorials)

Integrate in an existing library](/modules/existing-library)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/modules/third-party-library.mdx)
* Last updated on April 03, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Create a new module](/modules/third-party-library/#create-a-new-module)[Start with a new project](/modules/third-party-library/#start-with-a-new-project)[Start with an existing project](/modules/third-party-library/#start-with-an-existing-project)[Run the example project](/modules/third-party-library/#run-the-example-project)[Add native dependencies](/modules/third-party-library/#add-native-dependencies)[Define an API](/modules/third-party-library/#define-an-api)[Implement the module on Android](/modules/third-party-library/#implement-the-module-on-android)[Implement the module on iOS](/modules/third-party-library/#implement-the-module-on-ios)[Write an example app to use the module](/modules/third-party-library/#write-an-example-app-to-use-the-module)[Rebuild and launch your application](/modules/third-party-library/#rebuild-and-launch-your-application)[Next step](/modules/third-party-library/#next-step)