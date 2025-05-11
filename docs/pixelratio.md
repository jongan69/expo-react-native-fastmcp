PixelRatio · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/pixelratio)

* [Next](/docs/next/pixelratio)* [0.79](/docs/pixelratio)* [0.78](/docs/0.78/pixelratio)* [0.77](/docs/0.77/pixelratio)* [0.76](/docs/0.76/pixelratio)* [0.75](/docs/0.75/pixelratio)* [0.74](/docs/0.74/pixelratio)* [0.73](/docs/0.73/pixelratio)* [0.72](/docs/0.72/pixelratio)* [0.71](/docs/0.71/pixelratio)* [0.70](/docs/0.70/pixelratio)* [All versions](/versions)

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

PixelRatio
==========

`PixelRatio` gives you access to the device's pixel density and font scale.

Fetching a correctly sized image[​](#fetching-a-correctly-sized-image "Direct link to Fetching a correctly sized image")
------------------------------------------------------------------------------------------------------------------------

You should get a higher resolution image if you are on a high pixel density device. A good rule of thumb is to multiply the size of the image you display by the pixel ratio.

tsx

```
const image = getImage({  
  width: PixelRatio.getPixelSizeForLayoutSize(200),  
  height: PixelRatio.getPixelSizeForLayoutSize(100),  
});  
<Image source={image} style={{width: 200, height: 100}} />;  

```

Pixel grid snapping[​](#pixel-grid-snapping "Direct link to Pixel grid snapping")
---------------------------------------------------------------------------------

In iOS, you can specify positions and dimensions for elements with arbitrary precision, for example 29.674825. But, ultimately the physical display only have a fixed number of pixels, for example 640×1136 for iPhone SE (1st generation) or 828×1792 for iPhone 11. iOS tries to be as faithful as possible to the user value by spreading one original pixel into multiple ones to trick the eye. The downside of this technique is that it makes the resulting element look blurry.

In practice, we found out that developers do not want this feature and they have to work around it by doing manual rounding in order to avoid having blurry elements. In React Native, we are rounding all the pixels automatically.

We have to be careful when to do this rounding. You never want to work with rounded and unrounded values at the same time as you're going to accumulate rounding errors. Having even one rounding error is deadly because a one pixel border may vanish or be twice as big.

In React Native, everything in JavaScript and within the layout engine works with arbitrary precision numbers. It's only when we set the position and dimensions of the native element on the main thread that we round. Also, rounding is done relative to the root rather than the parent, again to avoid accumulating rounding errors.

Example[​](#example "Direct link to Example")
---------------------------------------------

---

Reference
=========

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### `get()`[​](#get "Direct link to get")

tsx

```
static get(): number;  

```

Returns the device pixel density. Some examples:

* `PixelRatio.get() === 1`
  + [mdpi Android devices](https://material.io/tools/devices/)
* `PixelRatio.get() === 1.5`
  + [hdpi Android devices](https://material.io/tools/devices/)
* `PixelRatio.get() === 2`
  + iPhone SE, 6S, 7, 8
  + iPhone XR
  + iPhone 11
  + [xhdpi Android devices](https://material.io/tools/devices/)
* `PixelRatio.get() === 3`
  + iPhone 6S Plus, 7 Plus, 8 Plus
  + iPhone X, XS, XS Max
  + iPhone 11 Pro, 11 Pro Max
  + Pixel, Pixel 2
  + [xxhdpi Android devices](https://material.io/tools/devices/)
* `PixelRatio.get() === 3.5`
  + Nexus 6
  + Pixel XL, Pixel 2 XL
  + [xxxhdpi Android devices](https://material.io/tools/devices/)

---

### `getFontScale()`[​](#getfontscale "Direct link to getfontscale")

tsx

```
static getFontScale(): number;  

```

Returns the scaling factor for font sizes. This is the ratio that is used to calculate the absolute font size, so any elements that heavily depend on that should use this to do calculations.

* on Android value reflects the user preference set in **Settings > Display > Font size**
* on iOS value reflects the user preference set in **Settings > Display & Brightness > Text Size**, value can also be updated in **Settings > Accessibility > Display & Text Size > Larger Text**

If a font scale is not set, this returns the device pixel ratio.

---

### `getPixelSizeForLayoutSize()`[​](#getpixelsizeforlayoutsize "Direct link to getpixelsizeforlayoutsize")

tsx

```
static getPixelSizeForLayoutSize(layoutSize: number): number;  

```

Converts a layout size (dp) to pixel size (px).

Guaranteed to return an integer number.

---

### `roundToNearestPixel()`[​](#roundtonearestpixel "Direct link to roundtonearestpixel")

tsx

```
static roundToNearestPixel(layoutSize: number): number;  

```

Rounds a layout size (dp) to the nearest layout size that corresponds to an integer number of pixels. For example, on a device with a PixelRatio of 3, `PixelRatio.roundToNearestPixel(8.4) = 8.33`, which corresponds to exactly (8.33 \* 3) = 25 pixels.

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/pixelratio.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/pixelratio.md)

Last updated on **Apr 14, 2025**

[Previous

PanResponder](/docs/panresponder)[Next

Platform](/docs/platform)

* [Fetching a correctly sized image](#fetching-a-correctly-sized-image)* [Pixel grid snapping](#pixel-grid-snapping)* [Example](#example)* [Methods](#methods)
        + [`get()`](#get)+ [`getFontScale()`](#getfontscale)+ [`getPixelSizeForLayoutSize()`](#getpixelsizeforlayoutsize)+ [`roundToNearestPixel()`](#roundtonearestpixel)

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