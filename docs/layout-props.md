Layout Props · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/layout-props)

* [Next](/docs/next/layout-props)* [0.79](/docs/layout-props)* [0.78](/docs/0.78/layout-props)* [0.77](/docs/0.77/layout-props)* [0.76](/docs/0.76/layout-props)* [0.75](/docs/0.75/layout-props)* [0.74](/docs/0.74/layout-props)* [0.73](/docs/0.73/layout-props)* [0.72](/docs/0.72/layout-props)* [0.71](/docs/0.71/layout-props)* [0.70](/docs/0.70/layout-props)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [Core Components](/docs/components-and-apis)

  * [Props](/docs/image-style-props)

    + [Image Style Props](/docs/image-style-props)+ [Layout Props](/docs/layout-props)+ [Shadow Props](/docs/shadow-props)+ [Text Style Props](/docs/text-style-props)+ [View Style Props](/docs/view-style-props)* [Object Types](/docs/boxshadowvalue)

On this page

Layout Props
============

> More detailed examples about those properties can be found on the [Layout with Flexbox](/docs/flexbox) page.

### Example[​](#example "Direct link to Example")

The following example shows how different properties can affect or shape a React Native layout. You can try for example to add or remove squares from the UI while changing the values of the property `flexWrap`.

* TypeScript* JavaScript

---

Reference
=========

Props[​](#props "Direct link to Props")
---------------------------------------

### `alignContent`[​](#aligncontent "Direct link to aligncontent")

`alignContent` controls how rows align in the cross direction, overriding the `alignContent` of the parent. See <https://developer.mozilla.org/en-US/docs/Web/CSS/align-content> for more details.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | enum('flex-start', 'flex-end', 'center', 'stretch', 'space-between', 'space-around', 'space-evenly') No | | | |

---

### `alignItems`[​](#alignitems "Direct link to alignitems")

`alignItems` aligns children in the cross direction. For example, if children are flowing vertically, `alignItems` controls how they align horizontally. It works like `align-items` in CSS (default: stretch). See <https://developer.mozilla.org/en-US/docs/Web/CSS/align-items> for more details.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | enum('flex-start', 'flex-end', 'center', 'stretch', 'baseline') No | | | |

---

### `alignSelf`[​](#alignself "Direct link to alignself")

`alignSelf` controls how a child aligns in the cross direction, overriding the `alignItems` of the parent. It works like `align-self` in CSS (default: auto). See <https://developer.mozilla.org/en-US/docs/Web/CSS/align-self> for more details.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | enum('auto', 'flex-start', 'flex-end', 'center', 'stretch', 'baseline') No | | | |

---

### `aspectRatio`[​](#aspectratio "Direct link to aspectratio")

Aspect ratio controls the size of the undefined dimension of a node. See <https://developer.mozilla.org/en-US/docs/Web/CSS/aspect-ratio> for more details.

* On a node with a set width/height, aspect ratio controls the size of the unset dimension
* On a node with a set flex basis, aspect ratio controls the size of the node in the cross axis if unset
* On a node with a measure function, aspect ratio works as though the measure function measures the flex basis
* On a node with flex grow/shrink, aspect ratio controls the size of the node in the cross axis if unset
* Aspect ratio takes min/max dimensions into account

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number, string No | | | |

---

### `borderBottomWidth`[​](#borderbottomwidth "Direct link to borderbottomwidth")

`borderBottomWidth` works like `border-bottom-width` in CSS. See <https://developer.mozilla.org/en-US/docs/Web/CSS/border-bottom-width> for more details.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number No | | | |

---

### `borderEndWidth`[​](#borderendwidth "Direct link to borderendwidth")

When direction is `ltr`, `borderEndWidth` is equivalent to `borderRightWidth`. When direction is `rtl`, `borderEndWidth` is equivalent to `borderLeftWidth`.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number No | | | |

---

### `borderLeftWidth`[​](#borderleftwidth "Direct link to borderleftwidth")

`borderLeftWidth` works like `border-left-width` in CSS. See <https://developer.mozilla.org/en-US/docs/Web/CSS/border-left-width> for more details.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number No | | | |

---

### `borderRightWidth`[​](#borderrightwidth "Direct link to borderrightwidth")

`borderRightWidth` works like `border-right-width` in CSS. See <https://developer.mozilla.org/en-US/docs/Web/CSS/border-right-width> for more details.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number No | | | |

---

### `borderStartWidth`[​](#borderstartwidth "Direct link to borderstartwidth")

When direction is `ltr`, `borderStartWidth` is equivalent to `borderLeftWidth`. When direction is `rtl`, `borderStartWidth` is equivalent to `borderRightWidth`.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number No | | | |

---

### `borderTopWidth`[​](#bordertopwidth "Direct link to bordertopwidth")

`borderTopWidth` works like `border-top-width` in CSS. See <https://developer.mozilla.org/en-US/docs/Web/CSS/border-top-width> for more details.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number No | | | |

---

### `borderWidth`[​](#borderwidth "Direct link to borderwidth")

`borderWidth` works like `border-width` in CSS. See <https://developer.mozilla.org/en-US/docs/Web/CSS/border-width> for more details.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number No | | | |

---

### `bottom`[​](#bottom "Direct link to bottom")

`bottom` is the number of logical pixels to offset the bottom edge of this component.

It works similarly to `bottom` in CSS, but in React Native you must use points or percentages. Ems and other units are not supported.

See <https://developer.mozilla.org/en-US/docs/Web/CSS/bottom> for more details of how `bottom` affects layout.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number, string No | | | |

---

### `boxSizing`[​](#boxsizing "Direct link to boxsizing")

`boxSizing` defines how the element's various sizing props (`width`, `height`, `minWidth`, `minHeight`, etc.) are computed. If `boxSizing` is `border-box`, these sizes apply to the border box of the element. If it is `content-box`, they apply to the content box of the element. The default value is `border-box`. The [web documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing) is a good source of information if you wish to learn more about how this prop works.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | enum('border-box', 'content-box') No | | | |

---

### `columnGap`[​](#columngap "Direct link to columngap")

`columnGap` works like `column-gap` in CSS. Only pixel units are supported in React Native. See <https://developer.mozilla.org/en-US/docs/Web/CSS/column-gap> for more details.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number No | | | |

---

### `direction`[​](#direction "Direct link to direction")

`direction` specifies the directional flow of the user interface. The default is `inherit`, except for root node which will have value based on the current locale. See <https://www.yogalayout.dev/docs/styling/layout-direction> for more details.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Type Required Platform|  |  |  | | --- | --- | --- | | enum('inherit', 'ltr', 'rtl') No iOS | | | | | |

---

### `display`[​](#display "Direct link to display")

`display` sets the display type of this component.

It works similarly to `display` in CSS but only supports 'flex' and 'none'. 'flex' is the default.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | enum('none', 'flex') No | | | |

---

### `end`[​](#end "Direct link to end")

When the direction is `ltr`, `end` is equivalent to `right`. When the direction is `rtl`, `end` is equivalent to `left`.

This style takes precedence over the `left` and `right` styles.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number, string No | | | |

---

### `flex`[​](#flex "Direct link to flex")

In React Native `flex` does not work the same way that it does in CSS. `flex` is a number rather than a string, and it works according to the [Yoga](https://github.com/facebook/yoga) layout engine.

When `flex` is a positive number, it makes the component flexible, and it will be sized proportional to its flex value. So a component with `flex` set to 2 will take twice the space as a component with `flex` set to 1. `flex: <positive number>` equates to `flexGrow: <positive number>, flexShrink: 1, flexBasis: 0`.

When `flex` is 0, the component is sized according to `width` and `height`, and it is inflexible.

When `flex` is -1, the component is normally sized according to `width` and `height`. However, if there's not enough space, the component will shrink to its `minWidth` and `minHeight`.

`flexGrow`, `flexShrink`, and `flexBasis` work the same as in CSS.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number No | | | |

---

### `flexBasis`[​](#flexbasis "Direct link to flexbasis")

`flexBasis` is an axis-independent way of providing the default size of an item along the main axis. Setting the `flexBasis` of a child is similar to setting the `width` of that child if its parent is a container with `flexDirection: row` or setting the `height` of a child if its parent is a container with `flexDirection: column`. The `flexBasis` of an item is the default size of that item, the size of the item before any `flexGrow` and `flexShrink` calculations are performed.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number, string No | | | |

---

### `flexDirection`[​](#flexdirection "Direct link to flexdirection")

`flexDirection` controls which directions children of a container go. `row` goes left to right, `column` goes top to bottom, and you may be able to guess what the other two do. It works like `flex-direction` in CSS, except the default is `column`. See <https://developer.mozilla.org/en-US/docs/Web/CSS/flex-direction> for more details.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | enum('row', 'row-reverse', 'column', 'column-reverse') No | | | |

---

### `flexGrow`[​](#flexgrow "Direct link to flexgrow")

`flexGrow` describes how any space within a container should be distributed among its children along the main axis. After laying out its children, a container will distribute any remaining space according to the flex grow values specified by its children.

`flexGrow` accepts any floating point value >= 0, with 0 being the default value. A container will distribute any remaining space among its children weighted by the children’s `flexGrow` values.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number No | | | |

---

### `flexShrink`[​](#flexshrink "Direct link to flexshrink")

[`flexShrink`](/docs/layout-props#flexshrink) describes how to shrink children along the main axis in the case in which the total size of the children overflows the size of the container on the main axis. `flexShrink` is very similar to `flexGrow` and can be thought of in the same way if any overflowing size is considered to be negative remaining space. These two properties also work well together by allowing children to grow and shrink as needed.

`flexShrink` accepts any floating point value >= 0, with 0 being the default value. A container will shrink its children weighted by the children’s `flexShrink` values.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number No | | | |

---

### `flexWrap`[​](#flexwrap "Direct link to flexwrap")

`flexWrap` controls whether children can wrap around after they hit the end of a flex container. It works like `flex-wrap` in CSS (default: nowrap). See <https://developer.mozilla.org/en-US/docs/Web/CSS/flex-wrap> for more details. Note it does not work anymore with `alignItems: stretch` (the default), so you may want to use `alignItems: flex-start` for example (breaking change details: <https://github.com/facebook/react-native/releases/tag/v0.28.0>).

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | enum('wrap', 'nowrap', 'wrap-reverse') No | | | |

---

### `gap`[​](#gap "Direct link to gap")

`gap` works like `gap` in CSS. Only pixel units are supported in React Native. See <https://developer.mozilla.org/en-US/docs/Web/CSS/gap> for more details.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number No | | | |

---

### `height`[​](#height "Direct link to height")

`height` sets the height of this component.

It works similarly to `height` in CSS, but in React Native you must use points or percentages. Ems and other units are not supported. See <https://developer.mozilla.org/en-US/docs/Web/CSS/height> for more details.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number, string No | | | |

---

### `justifyContent`[​](#justifycontent "Direct link to justifycontent")

`justifyContent` aligns children in the main direction. For example, if children are flowing vertically, `justifyContent` controls how they align vertically. It works like `justify-content` in CSS (default: flex-start). See <https://developer.mozilla.org/en-US/docs/Web/CSS/justify-content> for more details.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | enum('flex-start', 'flex-end', 'center', 'space-between', 'space-around', 'space-evenly') No | | | |

---

### `left`[​](#left "Direct link to left")

`left` is the number of logical pixels to offset the left edge of this component.

It works similarly to `left` in CSS, but in React Native you must use points or percentages. Ems and other units are not supported.

See <https://developer.mozilla.org/en-US/docs/Web/CSS/left> for more details of how `left` affects layout.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number, string No | | | |

---

### `margin`[​](#margin "Direct link to margin")

Setting `margin` has the same effect as setting each of `marginTop`, `marginLeft`, `marginBottom`, and `marginRight`. See <https://developer.mozilla.org/en-US/docs/Web/CSS/margin> for more details.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number, string No | | | |

---

### `marginBottom`[​](#marginbottom "Direct link to marginbottom")

`marginBottom` works like `margin-bottom` in CSS. See <https://developer.mozilla.org/en-US/docs/Web/CSS/margin-bottom> for more details.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number, string No | | | |

---

### `marginEnd`[​](#marginend "Direct link to marginend")

When direction is `ltr`, `marginEnd` is equivalent to `marginRight`. When direction is `rtl`, `marginEnd` is equivalent to `marginLeft`.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number, string No | | | |

---

### `marginHorizontal`[​](#marginhorizontal "Direct link to marginhorizontal")

Setting `marginHorizontal` has the same effect as setting both `marginLeft` and `marginRight`.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number, string No | | | |

---

### `marginLeft`[​](#marginleft "Direct link to marginleft")

`marginLeft` works like `margin-left` in CSS. See <https://developer.mozilla.org/en-US/docs/Web/CSS/margin-left> for more details.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number, string No | | | |

---

### `marginRight`[​](#marginright "Direct link to marginright")

`marginRight` works like `margin-right` in CSS. See <https://developer.mozilla.org/en-US/docs/Web/CSS/margin-right> for more details.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number, string No | | | |

---

### `marginStart`[​](#marginstart "Direct link to marginstart")

When direction is `ltr`, `marginStart` is equivalent to `marginLeft`. When direction is `rtl`, `marginStart` is equivalent to `marginRight`.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number, string No | | | |

---

### `marginTop`[​](#margintop "Direct link to margintop")

`marginTop` works like `margin-top` in CSS. See <https://developer.mozilla.org/en-US/docs/Web/CSS/margin-top> for more details.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number, string No | | | |

---

### `marginVertical`[​](#marginvertical "Direct link to marginvertical")

Setting `marginVertical` has the same effect as setting both `marginTop` and `marginBottom`.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number, string No | | | |

---

### `maxHeight`[​](#maxheight "Direct link to maxheight")

`maxHeight` is the maximum height for this component, in logical pixels.

It works similarly to `max-height` in CSS, but in React Native you must use points or percentages. Ems and other units are not supported.

See <https://developer.mozilla.org/en-US/docs/Web/CSS/max-height> for more details.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number, string No | | | |

---

### `maxWidth`[​](#maxwidth "Direct link to maxwidth")

`maxWidth` is the maximum width for this component, in logical pixels.

It works similarly to `max-width` in CSS, but in React Native you must use points or percentages. Ems and other units are not supported.

See <https://developer.mozilla.org/en-US/docs/Web/CSS/max-width> for more details.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number, string No | | | |

---

### `minHeight`[​](#minheight "Direct link to minheight")

`minHeight` is the minimum height for this component, in logical pixels.

It works similarly to `min-height` in CSS, but in React Native you must use points or percentages. Ems and other units are not supported.

See <https://developer.mozilla.org/en-US/docs/Web/CSS/min-height> for more details.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number, string No | | | |

---

### `minWidth`[​](#minwidth "Direct link to minwidth")

`minWidth` is the minimum width for this component, in logical pixels.

It works similarly to `min-width` in CSS, but in React Native you must use points or percentages. Ems and other units are not supported.

See <https://developer.mozilla.org/en-US/docs/Web/CSS/min-width> for more details.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number, string No | | | |

---

### `overflow`[​](#overflow "Direct link to overflow")

`overflow` controls how children are measured and displayed. `overflow: hidden` causes views to be clipped while `overflow: scroll` causes views to be measured independently of their parents' main axis. It works like `overflow` in CSS (default: visible). See <https://developer.mozilla.org/en/docs/Web/CSS/overflow> for more details.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | enum('visible', 'hidden', 'scroll') No | | | |

---

### `padding`[​](#padding "Direct link to padding")

Setting `padding` has the same effect as setting each of `paddingTop`, `paddingBottom`, `paddingLeft`, and `paddingRight`. See <https://developer.mozilla.org/en-US/docs/Web/CSS/padding> for more details.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number, string No | | | |

---

### `paddingBottom`[​](#paddingbottom "Direct link to paddingbottom")

`paddingBottom` works like `padding-bottom` in CSS. See <https://developer.mozilla.org/en-US/docs/Web/CSS/padding-bottom> for more details.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number, string No | | | |

---

### `paddingEnd`[​](#paddingend "Direct link to paddingend")

When direction is `ltr`, `paddingEnd` is equivalent to `paddingRight`. When direction is `rtl`, `paddingEnd` is equivalent to `paddingLeft`.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number, string No | | | |

---

### `paddingHorizontal`[​](#paddinghorizontal "Direct link to paddinghorizontal")

Setting `paddingHorizontal` is like setting both of `paddingLeft` and `paddingRight`.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number, string No | | | |

---

### `paddingLeft`[​](#paddingleft "Direct link to paddingleft")

`paddingLeft` works like `padding-left` in CSS. See <https://developer.mozilla.org/en-US/docs/Web/CSS/padding-left> for more details.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number, string No | | | |

---

### `paddingRight`[​](#paddingright "Direct link to paddingright")

`paddingRight` works like `padding-right` in CSS. See <https://developer.mozilla.org/en-US/docs/Web/CSS/padding-right> for more details.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number, string No | | | |

---

### `paddingStart`[​](#paddingstart "Direct link to paddingstart")

When direction is `ltr`, `paddingStart` is equivalent to `paddingLeft`. When direction is `rtl`, `paddingStart` is equivalent to `paddingRight`.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number, string No | | | |

---

### `paddingTop`[​](#paddingtop "Direct link to paddingtop")

`paddingTop` works like `padding-top` in CSS. See <https://developer.mozilla.org/en-US/docs/Web/CSS/padding-top> for more details.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number, ,string No | | | |

---

### `paddingVertical`[​](#paddingvertical "Direct link to paddingvertical")

Setting `paddingVertical` is like setting both of `paddingTop` and `paddingBottom`.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number, string No | | | |

---

### `position`[​](#position "Direct link to position")

`position` in React Native is similar to [regular CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/position), but everything is set to `relative` by default.

`relative` will position an element according to the normal flow of the layout. Insets (`top`, `bottom`, `left`, `right`) will offset relative to this layout.

`absolute` takes the element out of the normal flow of the layout. Insets will offset relative to its [containing block](/docs/flexbox#the-containing-block).

`static` will position an element according to the normal flow of the layout. Insets will have no effect.
`static` elements do not form a containing block for absolute descendants.

For more information, see the [Layout with Flexbox docs](/docs/flexbox#position). Also, [the Yoga documentation](https://www.yogalayout.dev/docs/styling/position) has more details on how `position` differs between React Native and CSS.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | enum('absolute', 'relative', 'static') No | | | |

---

### `right`[​](#right "Direct link to right")

`right` is the number of logical pixels to offset the right edge of this component.

It works similarly to `right` in CSS, but in React Native you must use points or percentages. Ems and other units are not supported.

See <https://developer.mozilla.org/en-US/docs/Web/CSS/right> for more details of how `right` affects layout.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number, string No | | | |

---

### `rowGap`[​](#rowgap "Direct link to rowgap")

`rowGap` works like `row-gap` in CSS. Only pixel units are supported in React Native. See <https://developer.mozilla.org/en-US/docs/Web/CSS/row-gap> for more details.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number No | | | |

---

### `start`[​](#start "Direct link to start")

When the direction is `ltr`, `start` is equivalent to `left`. When the direction is `rtl`, `start` is equivalent to `right`.

This style takes precedence over the `left`, `right`, and `end` styles.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number, string No | | | |

---

### `top`[​](#top "Direct link to top")

`top` is the number of logical pixels to offset the top edge of this component.

It works similarly to `top` in CSS, but in React Native you must use points or percentages. Ems and other units are not supported.

See <https://developer.mozilla.org/en-US/docs/Web/CSS/top> for more details of how `top` affects layout.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number, string No | | | |

---

### `width`[​](#width "Direct link to width")

`width` sets the width of this component.

It works similarly to `width` in CSS, but in React Native you must use points or percentages. Ems and other units are not supported. See <https://developer.mozilla.org/en-US/docs/Web/CSS/width> for more details.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number, string No | | | |

---

### `zIndex`[​](#zindex "Direct link to zindex")

`zIndex` controls which components display on top of others. Normally, you don't use `zIndex`. Components render according to their order in the document tree, so later components draw over earlier ones. `zIndex` may be useful if you have animations or custom modal interfaces where you don't want this behavior.

It works like the CSS `z-index` property - components with a larger `zIndex` will render on top. Think of the z-direction like it's pointing from the phone into your eyeball. See <https://developer.mozilla.org/en-US/docs/Web/CSS/z-index> for more details.

On iOS, `zIndex` may require `View`s to be siblings of each other for it to work as expected.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | number No | | | |

---

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/layout-props.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/layout-props.md)

Last updated on **Apr 14, 2025**

[Previous

Image Style Props](/docs/image-style-props)[Next

Shadow Props](/docs/shadow-props)

* [Example](#example)* [Props](#props)
    + [`alignContent`](#aligncontent)+ [`alignItems`](#alignitems)+ [`alignSelf`](#alignself)+ [`aspectRatio`](#aspectratio)+ [`borderBottomWidth`](#borderbottomwidth)+ [`borderEndWidth`](#borderendwidth)+ [`borderLeftWidth`](#borderleftwidth)+ [`borderRightWidth`](#borderrightwidth)+ [`borderStartWidth`](#borderstartwidth)+ [`borderTopWidth`](#bordertopwidth)+ [`borderWidth`](#borderwidth)+ [`bottom`](#bottom)+ [`boxSizing`](#boxsizing)+ [`columnGap`](#columngap)+ [`direction`](#direction)+ [`display`](#display)+ [`end`](#end)+ [`flex`](#flex)+ [`flexBasis`](#flexbasis)+ [`flexDirection`](#flexdirection)+ [`flexGrow`](#flexgrow)+ [`flexShrink`](#flexshrink)+ [`flexWrap`](#flexwrap)+ [`gap`](#gap)+ [`height`](#height)+ [`justifyContent`](#justifycontent)+ [`left`](#left)+ [`margin`](#margin)+ [`marginBottom`](#marginbottom)+ [`marginEnd`](#marginend)+ [`marginHorizontal`](#marginhorizontal)+ [`marginLeft`](#marginleft)+ [`marginRight`](#marginright)+ [`marginStart`](#marginstart)+ [`marginTop`](#margintop)+ [`marginVertical`](#marginvertical)+ [`maxHeight`](#maxheight)+ [`maxWidth`](#maxwidth)+ [`minHeight`](#minheight)+ [`minWidth`](#minwidth)+ [`overflow`](#overflow)+ [`padding`](#padding)+ [`paddingBottom`](#paddingbottom)+ [`paddingEnd`](#paddingend)+ [`paddingHorizontal`](#paddinghorizontal)+ [`paddingLeft`](#paddingleft)+ [`paddingRight`](#paddingright)+ [`paddingStart`](#paddingstart)+ [`paddingTop`](#paddingtop)+ [`paddingVertical`](#paddingvertical)+ [`position`](#position)+ [`right`](#right)+ [`rowGap`](#rowgap)+ [`start`](#start)+ [`top`](#top)+ [`width`](#width)+ [`zIndex`](#zindex)

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