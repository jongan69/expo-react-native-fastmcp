Color Reference · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/colors)

* [Next](/docs/next/colors)* [0.79](/docs/colors)* [0.78](/docs/0.78/colors)* [0.77](/docs/0.77/colors)* [0.76](/docs/0.76/colors)* [0.75](/docs/0.75/colors)* [0.74](/docs/0.74/colors)* [0.73](/docs/0.73/colors)* [0.72](/docs/0.72/colors)* [0.71](/docs/0.71/colors)* [0.70](/docs/0.70/colors)* [All versions](/versions)

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

Color Reference
===============

Components in React Native are [styled using JavaScript](/docs/style). Color properties usually match how [CSS works on the web](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value). General guides on the color usage on each platform could be found below:

* [Android](https://material.io/design/color/color-usage.html)
* [iOS](https://developer.apple.com/design/human-interface-guidelines/ios/visual-design/color/)

Color APIs[​](#color-apis "Direct link to Color APIs")
------------------------------------------------------

React Native has several color APIs designed to allow you to take full advantage of your platform's design and user preferences.

* [PlatformColor](/docs/platformcolor) lets you reference the platform's color system.
* [DynamicColorIOS](/docs/dynamiccolorios) is iOS specific and allows you to specify which colors should be used in light or Dark Mode.

Color representations[​](#color-representations "Direct link to Color representations")
---------------------------------------------------------------------------------------

### Red Green Blue (RGB)[​](#red-green-blue-rgb "Direct link to Red Green Blue (RGB)")

React Native supports `rgb()` and `rgba()` in both hexadecimal and functional notation:

* `'#f0f'` (#rgb)
* `'#ff00ff'` (#rrggbb)
* `'#f0ff'` (#rgba)
* `'#ff00ff00'` (#rrggbbaa)
* `'rgb(255, 0, 255)'`
* `'rgb(255 0 255)'`
* `'rgba(255, 0, 255, 1.0)'`
* `'rgba(255 0 255 / 1.0)'`

### Hue Saturation Lightness (HSL)[​](#hue-saturation-lightness-hsl "Direct link to Hue Saturation Lightness (HSL)")

React Native supports `hsl()` and `hsla()` in functional notation:

* `'hsl(360, 100%, 100%)'`
* `'hsl(360 100% 100%)'`
* `'hsla(360, 100%, 100%, 1.0)'`
* `'hsla(360 100% 100% / 1.0)'`

### Hue Whiteness Blackness (HWB)[​](#hue-whiteness-blackness-hwb "Direct link to Hue Whiteness Blackness (HWB)")

React Native supports `hwb()` in functional notation:

* `'hwb(0, 0%, 100%)'`
* `'hwb(360, 100%, 100%)'`
* `'hwb(0 0% 0%)'`
* `'hwb(70 50% 0%)'`

### Color ints[​](#color-ints "Direct link to Color ints")

React Native supports also colors as an `int` values (in RGB color mode):

* `0xff00ff00` (0xrrggbbaa)

caution

This might appear similar to the Android [Color](https://developer.android.com/reference/android/graphics/Color) ints representation but on Android values are stored in SRGB color mode (0xaarrggbb).

### Named colors[​](#named-colors "Direct link to Named colors")

In React Native you can also use color name strings as values.

info

React Native only supports lowercase color names. Uppercase color names are not supported.

#### `transparent`[​](#transparent "Direct link to transparent")

This is a shortcut for `rgba(0,0,0,0)`, same like in [CSS3](https://www.w3.org/TR/css-color-3/#transparent).

#### Color keywords[​](#color-keywords "Direct link to Color keywords")

Named colors implementation follows the [CSS3/SVG specification](https://www.w3.org/TR/css-color-3/#svg-color):

* aliceblue (`#f0f8ff`)
* antiquewhite (`#faebd7`)
* aqua (`#00ffff`)
* aquamarine (`#7fffd4`)
* azure (`#f0ffff`)
* beige (`#f5f5dc`)
* bisque (`#ffe4c4`)
* black (`#000000`)
* blanchedalmond (`#ffebcd`)
* blue (`#0000ff`)
* blueviolet (`#8a2be2`)
* brown (`#a52a2a`)
* burlywood (`#deb887`)
* cadetblue (`#5f9ea0`)
* chartreuse (`#7fff00`)
* chocolate (`#d2691e`)
* coral (`#ff7f50`)
* cornflowerblue (`#6495ed`)
* cornsilk (`#fff8dc`)
* crimson (`#dc143c`)
* cyan (`#00ffff`)
* darkblue (`#00008b`)
* darkcyan (`#008b8b`)
* darkgoldenrod (`#b8860b`)
* darkgray (`#a9a9a9`)
* darkgreen (`#006400`)
* darkgrey (`#a9a9a9`)
* darkkhaki (`#bdb76b`)
* darkmagenta (`#8b008b`)
* darkolivegreen (`#556b2f`)
* darkorange (`#ff8c00`)
* darkorchid (`#9932cc`)
* darkred (`#8b0000`)
* darksalmon (`#e9967a`)
* darkseagreen (`#8fbc8f`)
* darkslateblue (`#483d8b`)
* darkslategrey (`#2f4f4f`)
* darkturquoise (`#00ced1`)
* darkviolet (`#9400d3`)
* deeppink (`#ff1493`)
* deepskyblue (`#00bfff`)
* dimgray (`#696969`)
* dimgrey (`#696969`)
* dodgerblue (`#1e90ff`)
* firebrick (`#b22222`)
* floralwhite (`#fffaf0`)
* forestgreen (`#228b22`)
* fuchsia (`#ff00ff`)
* gainsboro (`#dcdcdc`)
* ghostwhite (`#f8f8ff`)
* gold (`#ffd700`)
* goldenrod (`#daa520`)
* gray (`#808080`)
* green (`#008000`)
* greenyellow (`#adff2f`)
* grey (`#808080`)
* honeydew (`#f0fff0`)
* hotpink (`#ff69b4`)
* indianred (`#cd5c5c`)
* indigo (`#4b0082`)
* ivory (`#fffff0`)
* khaki (`#f0e68c`)
* lavender (`#e6e6fa`)
* lavenderblush (`#fff0f5`)
* lawngreen (`#7cfc00`)
* lemonchiffon (`#fffacd`)
* lightblue (`#add8e6`)
* lightcoral (`#f08080`)
* lightcyan (`#e0ffff`)
* lightgoldenrodyellow (`#fafad2`)
* lightgray (`#d3d3d3`)
* lightgreen (`#90ee90`)
* lightgrey (`#d3d3d3`)
* lightpink (`#ffb6c1`)
* lightsalmon (`#ffa07a`)
* lightseagreen (`#20b2aa`)
* lightskyblue (`#87cefa`)
* lightslategrey (`#778899`)
* lightsteelblue (`#b0c4de`)
* lightyellow (`#ffffe0`)
* lime (`#00ff00`)
* limegreen (`#32cd32`)
* linen (`#faf0e6`)
* magenta (`#ff00ff`)
* maroon (`#800000`)
* mediumaquamarine (`#66cdaa`)
* mediumblue (`#0000cd`)
* mediumorchid (`#ba55d3`)
* mediumpurple (`#9370db`)
* mediumseagreen (`#3cb371`)
* mediumslateblue (`#7b68ee`)
* mediumspringgreen (`#00fa9a`)
* mediumturquoise (`#48d1cc`)
* mediumvioletred (`#c71585`)
* midnightblue (`#191970`)
* mintcream (`#f5fffa`)
* mistyrose (`#ffe4e1`)
* moccasin (`#ffe4b5`)
* navajowhite (`#ffdead`)
* navy (`#000080`)
* oldlace (`#fdf5e6`)
* olive (`#808000`)
* olivedrab (`#6b8e23`)
* orange (`#ffa500`)
* orangered (`#ff4500`)
* orchid (`#da70d6`)
* palegoldenrod (`#eee8aa`)
* palegreen (`#98fb98`)
* paleturquoise (`#afeeee`)
* palevioletred (`#db7093`)
* papayawhip (`#ffefd5`)
* peachpuff (`#ffdab9`)
* peru (`#cd853f`)
* pink (`#ffc0cb`)
* plum (`#dda0dd`)
* powderblue (`#b0e0e6`)
* purple (`#800080`)
* rebeccapurple (`#663399`)
* red (`#ff0000`)
* rosybrown (`#bc8f8f`)
* royalblue (`#4169e1`)
* saddlebrown (`#8b4513`)
* salmon (`#fa8072`)
* sandybrown (`#f4a460`)
* seagreen (`#2e8b57`)
* seashell (`#fff5ee`)
* sienna (`#a0522d`)
* silver (`#c0c0c0`)
* skyblue (`#87ceeb`)
* slateblue (`#6a5acd`)
* slategray (`#708090`)
* snow (`#fffafa`)
* springgreen (`#00ff7f`)
* steelblue (`#4682b4`)
* tan (`#d2b48c`)
* teal (`#008080`)
* thistle (`#d8bfd8`)
* tomato (`#ff6347`)
* turquoise (`#40e0d0`)
* violet (`#ee82ee`)
* wheat (`#f5deb3`)
* white (`#ffffff`)
* whitesmoke (`#f5f5f5`)
* yellow (`#ffff00`)
* yellowgreen (`#9acd32`)

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/colors.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/colors.md)

Last updated on **Apr 14, 2025**

[Previous

Images](/docs/images)[Next

Handling Touches](/docs/handling-touches)

* [Color APIs](#color-apis)* [Color representations](#color-representations)
    + [Red Green Blue (RGB)](#red-green-blue-rgb)+ [Hue Saturation Lightness (HSL)](#hue-saturation-lightness-hsl)+ [Hue Whiteness Blackness (HWB)](#hue-whiteness-blackness-hwb)+ [Color ints](#color-ints)+ [Named colors](#named-colors)

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