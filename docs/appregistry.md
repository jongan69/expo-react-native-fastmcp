AppRegistry · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/appregistry)

* [Next](/docs/next/appregistry)* [0.79](/docs/appregistry)* [0.78](/docs/0.78/appregistry)* [0.77](/docs/0.77/appregistry)* [0.76](/docs/0.76/appregistry)* [0.75](/docs/0.75/appregistry)* [0.74](/docs/0.74/appregistry)* [0.73](/docs/0.73/appregistry)* [0.72](/docs/0.72/appregistry)* [0.71](/docs/0.71/appregistry)* [0.70](/docs/0.70/appregistry)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [APIs](/docs/accessibilityinfo)

  + [AccessibilityInfo](/docs/accessibilityinfo)+ [Alert](/docs/alert)+ [Animated](/docs/animated)+ [Animated.Value](/docs/animatedvalue)+ [Animated.ValueXY](/docs/animatedvaluexy)+ [Appearance](/docs/appearance)+ [AppRegistry](/docs/appregistry)+ [AppState](/docs/appstate)+ [DevSettings](/docs/devsettings)+ [Dimensions](/docs/dimensions)+ [Easing](/docs/easing)+ [InteractionManager](/docs/interactionmanager)+ [Keyboard](/docs/keyboard)+ [LayoutAnimation](/docs/layoutanimation)+ [Linking](/docs/linking)+ [PanResponder](/docs/panresponder)+ [PixelRatio](/docs/pixelratio)+ [Platform](/docs/platform)+ [PlatformColor](/docs/platformcolor)+ [RootTag](/docs/roottag)+ [Share](/docs/share)+ [StyleSheet](/docs/stylesheet)+ [Systrace](/docs/systrace)+ [Transforms](/docs/transforms)+ [Vibration](/docs/vibration)+ [Hooks](/docs/usecolorscheme)

                                                      - [useColorScheme](/docs/usecolorscheme)- [useWindowDimensions](/docs/usewindowdimensions)+ [Android APIs](/docs/backhandler)

                                                        - [BackHandler](/docs/backhandler)- [PermissionsAndroid](/docs/permissionsandroid)- [ToastAndroid](/docs/toastandroid)+ [iOS APIs](/docs/actionsheetios)

                                                          - [ActionSheetIOS](/docs/actionsheetios)- [DynamicColorIOS](/docs/dynamiccolorios)- [Settings](/docs/settings)

On this page

AppRegistry
===========

### Project with Native Code Required

If you are using the managed Expo workflow there is only ever one entry component registered with `AppRegistry` and it is handled automatically (or through [registerRootComponent](https://docs.expo.dev/versions/latest/sdk/register-root-component/)). You do not need to use this API.

`AppRegistry` is the JS entry point to running all React Native apps. App root components should register themselves with `AppRegistry.registerComponent`, then the native system can load the bundle for the app and then actually run the app when it's ready by invoking `AppRegistry.runApplication`.

tsx

```
import {Text, AppRegistry} from 'react-native';  
  
const App = () => (  
  <View>  
    <Text>App1</Text>  
  </View>  
);  
  
AppRegistry.registerComponent('Appname', () => App);  

```

To "stop" an application when a view should be destroyed, call `AppRegistry.unmountApplicationComponentAtRootTag` with the tag that was passed into `runApplication`. These should always be used as a pair.

`AppRegistry` should be required early in the `require` sequence to make sure the JS execution environment is setup before other modules are required.

---

Reference
=========

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### `getAppKeys()`[​](#getappkeys "Direct link to getappkeys")

tsx

```
static getAppKeys(): string[];  

```

Returns an array of strings.

---

### `getRegistry()`[​](#getregistry "Direct link to getregistry")

tsx

```
static getRegistry(): {sections: string[]; runnables: Runnable[]};  

```

Returns a [Registry](/docs/appregistry#registry) object.

---

### `getRunnable()`[​](#getrunnable "Direct link to getrunnable")

tsx

```
static getRunnable(appKey: string): : Runnable | undefined;  

```

Returns a [Runnable](/docs/appregistry#runnable) object.

**Parameters:**

|  |  |  |  |
| --- | --- | --- | --- |
| Name Type|  |  | | --- | --- | | appKey Required  string | | | |

---

### `getSectionKeys()`[​](#getsectionkeys "Direct link to getsectionkeys")

tsx

```
static getSectionKeys(): string[];  

```

Returns an array of strings.

---

### `getSections()`[​](#getsections "Direct link to getsections")

tsx

```
static getSections(): Record<string, Runnable>;  

```

Returns a [Runnables](/docs/appregistry#runnables) object.

---

### `registerCancellableHeadlessTask()`[​](#registercancellableheadlesstask "Direct link to registercancellableheadlesstask")

tsx

```
static registerCancellableHeadlessTask(  
  taskKey: string,  
  taskProvider: TaskProvider,  
  taskCancelProvider: TaskCancelProvider,  
);  

```

Register a headless task which can be cancelled. A headless task is a bit of code that runs without a UI.

**Parameters:**

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Description|  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | taskKey  Required  string The native id for this task instance that was used when startHeadlessTask was called.|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | taskProvider  Required  [TaskProvider](/docs/appregistry#taskprovider) A promise returning function that takes some data passed from the native side as the only argument. When the promise is resolved or rejected the native side is notified of this event and it may decide to destroy the JS context.|  |  |  | | --- | --- | --- | | taskCancelProvider  Required  [TaskCancelProvider](/docs/appregistry#taskcancelprovider) a void returning function that takes no arguments; when a cancellation is requested, the function being executed by taskProvider should wrap up and return ASAP. | | | | | | | | | | | |

---

### `registerComponent()`[​](#registercomponent "Direct link to registercomponent")

tsx

```
static registerComponent(  
  appKey: string,  
  getComponentFunc: ComponentProvider,  
  section?: boolean,  
): string;  

```

**Parameters:**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | appKey Required  string|  |  |  |  | | --- | --- | --- | --- | | componentProvider Required  ComponentProvider|  |  | | --- | --- | | section boolean | | | | | | | |

---

### `registerConfig()`[​](#registerconfig "Direct link to registerconfig")

tsx

```
static registerConfig(config: AppConfig[]);  

```

**Parameters:**

|  |  |  |  |
| --- | --- | --- | --- |
| Name Type|  |  | | --- | --- | | config Required  [AppConfig](/docs/appregistry#appconfig)[] | | | |

---

### `registerHeadlessTask()`[​](#registerheadlesstask "Direct link to registerheadlesstask")

tsx

```
static registerHeadlessTask(  
  taskKey: string,  
  taskProvider: TaskProvider,  
);  

```

Register a headless task. A headless task is a bit of code that runs without a UI.

This is a way to run tasks in JavaScript while your app is in the background. It can be used, for example, to sync fresh data, handle push notifications, or play music.

**Parameters:**

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Description|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | taskKey Required  string The native id for this task instance that was used when startHeadlessTask was called.|  |  |  | | --- | --- | --- | | taskProvider Required  [TaskProvider](/docs/appregistry#taskprovider) A promise returning function that takes some data passed from the native side as the only argument. When the promise is resolved or rejected the native side is notified of this event and it may decide to destroy the JS context. | | | | | | | | |

---

### `registerRunnable()`[​](#registerrunnable "Direct link to registerrunnable")

tsx

```
static registerRunnable(appKey: string, func: Runnable): string;  

```

**Parameters:**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Name Type|  |  |  |  | | --- | --- | --- | --- | | appKey Required  string|  |  | | --- | --- | | run Required  function | | | | | |

---

### `registerSection()`[​](#registersection "Direct link to registersection")

tsx

```
static registerSection(  
  appKey: string,  
  component: ComponentProvider,  
);  

```

**Parameters:**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Name Type|  |  |  |  | | --- | --- | --- | --- | | appKey Required  string|  |  | | --- | --- | | component Required  ComponentProvider | | | | | |

---

### `runApplication()`[​](#runapplication "Direct link to runapplication")

tsx

```
static runApplication(appKey: string, appParameters: any): void;  

```

Loads the JavaScript bundle and runs the app.

**Parameters:**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Name Type|  |  |  |  | | --- | --- | --- | --- | | appKey Required  string|  |  | | --- | --- | | appParameters Required  any | | | | | |

---

### `setComponentProviderInstrumentationHook()`[​](#setcomponentproviderinstrumentationhook "Direct link to setcomponentproviderinstrumentationhook")

tsx

```
static setComponentProviderInstrumentationHook(  
  hook: ComponentProviderInstrumentationHook,  
);  

```

**Parameters:**

|  |  |  |  |
| --- | --- | --- | --- |
| Name Type|  |  | | --- | --- | | hook Required  function | | | |

A valid `hook` function accepts the following as arguments:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Name Type|  |  |  |  | | --- | --- | --- | --- | | component Required  ComponentProvider|  |  | | --- | --- | | scopedPerformanceLogger Required  IPerformanceLogger | | | | | |

The function must also return a React Component.

---

### `setWrapperComponentProvider()`[​](#setwrappercomponentprovider "Direct link to setwrappercomponentprovider")

tsx

```
static setWrapperComponentProvider(  
  provider: WrapperComponentProvider,  
);  

```

**Parameters:**

|  |  |  |  |
| --- | --- | --- | --- |
| Name Type|  |  | | --- | --- | | provider Required  ComponentProvider | | | |

---

### `startHeadlessTask()`[​](#startheadlesstask "Direct link to startheadlesstask")

tsx

```
static startHeadlessTask(  
  taskId: number,  
  taskKey: string,  
  data: any,  
);  

```

Only called from native code. Starts a headless task.

**Parameters:**

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Description|  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | taskId Required  number The native id for this task instance to keep track of its execution.|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | taskKey Required  string The key for the task to start.|  |  |  | | --- | --- | --- | | data Required  any The data to pass to the task. | | | | | | | | | | | |

---

### `unmountApplicationComponentAtRootTag()`[​](#unmountapplicationcomponentatroottag "Direct link to unmountapplicationcomponentatroottag")

tsx

```
static unmountApplicationComponentAtRootTag(rootTag: number);  

```

Stops an application when a view should be destroyed.

**Parameters:**

|  |  |  |  |
| --- | --- | --- | --- |
| Name Type|  |  | | --- | --- | | rootTag Required  number | | | |

Type Definitions[​](#type-definitions "Direct link to Type Definitions")
------------------------------------------------------------------------

### AppConfig[​](#appconfig "Direct link to AppConfig")

Application configuration for the `registerConfig` method.

|  |  |
| --- | --- |
| Type|  | | --- | | object | |

**Properties:**

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | appKey Required  string|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | component ComponentProvider|  |  |  |  | | --- | --- | --- | --- | | run function|  |  | | --- | --- | | section boolean | | | | | | | | | |

> **Note:** Every config is expected to set either `component` or `run` function.

### Registry[​](#registry "Direct link to Registry")

|  |  |
| --- | --- |
| Type|  | | --- | | object | |

**Properties:**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Name Type|  |  |  |  | | --- | --- | --- | --- | | runnables array of [Runnables](/docs/appregistry#runnable)| sections array of strings | | | | | |

### Runnable[​](#runnable "Direct link to Runnable")

|  |  |
| --- | --- |
| Type|  | | --- | | object | |

**Properties:**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Name Type|  |  |  |  | | --- | --- | --- | --- | | component ComponentProvider|  |  | | --- | --- | | run function | | | | | |

### Runnables[​](#runnables "Direct link to Runnables")

An object with key of `appKey` and value of type of [`Runnable`](/docs/appregistry#runnable).

|  |  |
| --- | --- |
| Type|  | | --- | | object | |

### Task[​](#task "Direct link to Task")

A `Task` is a function that accepts any data as argument and returns a Promise that resolves to `undefined`.

|  |  |
| --- | --- |
| Type|  | | --- | | function | |

### TaskCanceller[​](#taskcanceller "Direct link to TaskCanceller")

A `TaskCanceller` is a function that accepts no argument and returns void.

|  |  |
| --- | --- |
| Type|  | | --- | | function | |

### TaskCancelProvider[​](#taskcancelprovider "Direct link to TaskCancelProvider")

A valid `TaskCancelProvider` is a function that returns a [`TaskCanceller`](/docs/appregistry#taskcanceller).

|  |  |
| --- | --- |
| Type|  | | --- | | function | |

### TaskProvider[​](#taskprovider "Direct link to TaskProvider")

A valid `TaskProvider` is a function that returns a [`Task`](/docs/appregistry#task).

|  |  |
| --- | --- |
| Type|  | | --- | | function | |

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/appregistry.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/appregistry.md)

Last updated on **Apr 14, 2025**

[Previous

Appearance](/docs/appearance)[Next

AppState](/docs/appstate)

* [Methods](#methods)
  + [`getAppKeys()`](#getappkeys)+ [`getRegistry()`](#getregistry)+ [`getRunnable()`](#getrunnable)+ [`getSectionKeys()`](#getsectionkeys)+ [`getSections()`](#getsections)+ [`registerCancellableHeadlessTask()`](#registercancellableheadlesstask)+ [`registerComponent()`](#registercomponent)+ [`registerConfig()`](#registerconfig)+ [`registerHeadlessTask()`](#registerheadlesstask)+ [`registerRunnable()`](#registerrunnable)+ [`registerSection()`](#registersection)+ [`runApplication()`](#runapplication)+ [`setComponentProviderInstrumentationHook()`](#setcomponentproviderinstrumentationhook)+ [`setWrapperComponentProvider()`](#setwrappercomponentprovider)+ [`startHeadlessTask()`](#startheadlesstask)+ [`unmountApplicationComponentAtRootTag()`](#unmountapplicationcomponentatroottag)* [Type Definitions](#type-definitions)
    + [AppConfig](#appconfig)+ [Registry](#registry)+ [Runnable](#runnable)+ [Runnables](#runnables)+ [Task](#task)+ [TaskCanceller](#taskcanceller)+ [TaskCancelProvider](#taskcancelprovider)+ [TaskProvider](#taskprovider)

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