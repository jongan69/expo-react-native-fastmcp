Transforms · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/transforms)

* [Next](/docs/next/transforms)* [0.79](/docs/transforms)* [0.78](/docs/0.78/transforms)* [0.77](/docs/0.77/transforms)* [0.76](/docs/0.76/transforms)* [0.75](/docs/0.75/transforms)* [0.74](/docs/0.74/transforms)* [0.73](/docs/0.73/transforms)* [0.72](/docs/0.72/transforms)* [0.71](/docs/0.71/transforms)* [0.70](/docs/0.70/transforms)* [All versions](/versions)

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

Transforms
==========

Transforms are style properties that will help you modify the appearance and position of your components using 2D or 3D transformations. However, once you apply transforms, the layouts remain the same around the transformed component hence it might overlap with the nearby components. You can apply margin to the transformed component, the nearby components or padding to the container to prevent such overlaps.

Example[​](#example "Direct link to Example")
---------------------------------------------

---

Reference
=========

Transform[​](#transform "Direct link to Transform")
---------------------------------------------------

`transform` accepts an array of transformation objects or space-separated string values. Each object specifies the property that will be transformed as the key, and the value to use in the transformation. Objects should not be combined. Use a single key/value pair per object.

The rotate transformations require a string so that the transform may be expressed in degrees (deg) or radians (rad). For example:

js

```
{  
  transform: [{rotateX: '45deg'}, {rotateZ: '0.785398rad'}],  
}  

```

The same could also be achieved using a space-separated string:

js

```
{  
  transform: 'rotateX(45deg) rotateZ(0.785398rad)',  
}  

```

The skew transformations require a string so that the transform may be expressed in degrees (deg). For example:

js

```
{  
  transform: [{skewX: '45deg'}],  
}  

```

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | array of objects: `{matrix: number[]}`, `{perspective: number}`, `{rotate: string}`, `{rotateX: string}`, `{rotateY: string}`, `{rotateZ: string}`, `{scale: number}`, `{scaleX: number}`, `{scaleY: number}`, `{translateX: number}`, `{translateY: number}`, `{skewX: string}`, `{skewY: string}` or string No | | | |

---

### `decomposedMatrix`, `rotation`, `scaleX`, `scaleY`, `transformMatrix`, `translateX`, `translateY`[​](#decomposedmatrix-rotation-scalex-scaley-transformmatrix-translatex-translatey "Direct link to decomposedmatrix-rotation-scalex-scaley-transformmatrix-translatex-translatey")

> **Deprecated.** Use the [`transform`](/docs/transforms#transform) prop instead.

Transform Origin[​](#transform-origin "Direct link to Transform Origin")
------------------------------------------------------------------------

The `transformOrigin` property sets the origin for a view's transformations. The transform origin is the point around which a transformation is applied. By default, the origin of a transform is `center`.

Example
=======

### Values[​](#values "Direct link to Values")

Transform origin supports `px`, `percentage` and keywords `top`, `left`, `right`, `bottom`, `center` values.

The `transformOrigin` property may be specified using one, two, or three values, where each value represents an offset.

#### One-value syntax:[​](#one-value-syntax "Direct link to One-value syntax:")

* The value must be a `px`, a `percentage`, or one of the keywords `left`, `center`, `right`, `top`, and `bottom`.

js

```
{  
  transformOrigin: '20px',  
  transformOrigin: 'bottom',  
}  

```

#### Two-value syntax:[​](#two-value-syntax "Direct link to Two-value syntax:")

* First value (x-offset) must be a `px`, a `percentage`, or one of the keywords `left`, `center`, and `right`.
* The second value (y-offset) must be a `px`, a `percentage`, or one of the keywords `top`, `center`, and `bottom`.

js

```
{  
  transformOrigin: '10px 2px',  
  transformOrigin: 'left top',  
  transformOrigin: 'top right',  
}  

```

#### Three-value syntax:[​](#three-value-syntax "Direct link to Three-value syntax:")

* The first two values are the same as for the two-value syntax.
* The third value (z-offset) must be a `px`. It always represents the Z offset.

js

```
{  
  transformOrigin: '2px 30% 10px',  
  transformOrigin: 'right bottom 20px',  
}  

```

#### Array syntax[​](#array-syntax "Direct link to Array syntax")

`transformOrigin` also supports an array syntax. It makes it convenient to use it with Animated APIs. It also avoids string parsing, so should be more efficient.

js

```
{  
  // Using numeric values  
  transformOrigin: [10, 30, 40],  
  // Mixing numeric and percentage values  
  transformOrigin: [10, '20%', 0],  
}  

```

You may refer to MDN's guide on [Transform origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin) for additional information.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/transforms.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/transforms.md)

Last updated on **Apr 14, 2025**

[Previous

Systrace](/docs/systrace)[Next

Vibration](/docs/vibration)

* [Example](#example)* [Transform](#transform)
    + [`decomposedMatrix`, `rotation`, `scaleX`, `scaleY`, `transformMatrix`, `translateX`, `translateY`](#decomposedmatrix-rotation-scalex-scaley-transformmatrix-translatex-translatey)* [Transform Origin](#transform-origin)
      + [Values](#values)

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