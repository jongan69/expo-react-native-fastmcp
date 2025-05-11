TouchableWithoutFeedback · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/touchablewithoutfeedback)

* [Next](/docs/next/touchablewithoutfeedback)* [0.79](/docs/touchablewithoutfeedback)* [0.78](/docs/0.78/touchablewithoutfeedback)* [0.77](/docs/0.77/touchablewithoutfeedback)* [0.76](/docs/0.76/touchablewithoutfeedback)* [0.75](/docs/0.75/touchablewithoutfeedback)* [0.74](/docs/0.74/touchablewithoutfeedback)* [0.73](/docs/0.73/touchablewithoutfeedback)* [0.72](/docs/0.72/touchablewithoutfeedback)* [0.71](/docs/0.71/touchablewithoutfeedback)* [0.70](/docs/0.70/touchablewithoutfeedback)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

* [Core Components](/docs/components-and-apis)

  + [Core Components and APIs](/docs/components-and-apis)+ [ActivityIndicator](/docs/activityindicator)+ [Button](/docs/button)+ [FlatList](/docs/flatlist)+ [Image](/docs/image)+ [ImageBackground](/docs/imagebackground)+ [KeyboardAvoidingView](/docs/keyboardavoidingview)+ [Modal](/docs/modal)+ [Pressable](/docs/pressable)+ [RefreshControl](/docs/refreshcontrol)+ [ScrollView](/docs/scrollview)+ [SectionList](/docs/sectionlist)+ [StatusBar](/docs/statusbar)+ [Switch](/docs/switch)+ [Text](/docs/text)+ [TextInput](/docs/textinput)+ [TouchableHighlight](/docs/touchablehighlight)+ [TouchableOpacity](/docs/touchableopacity)+ [TouchableWithoutFeedback](/docs/touchablewithoutfeedback)+ [View](/docs/view)+ [VirtualizedList](/docs/virtualizedlist)+ [Android Components](/docs/drawerlayoutandroid)

                                              - [DrawerLayoutAndroid](/docs/drawerlayoutandroid)- [TouchableNativeFeedback](/docs/touchablenativefeedback)+ [iOS Components](/docs/inputaccessoryview)

                                                - [InputAccessoryView](/docs/inputaccessoryview)- [SafeAreaView](/docs/safeareaview)* [Props](/docs/image-style-props)

    * [Object Types](/docs/boxshadowvalue)

On this page

TouchableWithoutFeedback
========================

> If you're looking for a more extensive and future-proof way to handle touch-based input, check out the [Pressable](/docs/pressable) API.

Do not use unless you have a very good reason. All elements that respond to press should have a visual feedback when touched.

`TouchableWithoutFeedback` supports only one child. If you wish to have several child components, wrap them in a View. Importantly, `TouchableWithoutFeedback` works by cloning its child and applying responder props to it. It is therefore required that any intermediary components pass through those props to the underlying React Native component.

Usage Pattern[​](#usage-pattern "Direct link to Usage Pattern")
---------------------------------------------------------------

tsx

```
function MyComponent(props: MyComponentProps) {  
  return (  
    <View {...props} style={{flex: 1, backgroundColor: '#fff'}}>  
      <Text>My Component</Text>  
    </View>  
  );  
}  
  
<TouchableWithoutFeedback onPress={() => alert('Pressed!')}>  
  <MyComponent />  
</TouchableWithoutFeedback>;  

```

Example[​](#example "Direct link to Example")
---------------------------------------------

---

Reference
=========

Props[​](#props "Direct link to Props")
---------------------------------------

### `accessibilityIgnoresInvertColors` iOS [​](#accessibilityignoresinvertcolors-ios "Direct link to accessibilityignoresinvertcolors-ios")

A value indicating this view should or should not be inverted when color inversion is turned on. A value of `true` will tell the view to not be inverted even if color inversion is turned on.

See the [Accessibility guide](/docs/accessibility#accessibilityignoresinvertcolors) for more information.

|  |  |
| --- | --- |
| Type|  | | --- | | Boolean | |

---

### `accessible`[​](#accessible "Direct link to accessible")

When `true`, indicates that the view is an accessibility element. By default, all the touchable elements are accessible.

|  |  |
| --- | --- |
| Type|  | | --- | | bool | |

---

### `accessibilityLabel`[​](#accessibilitylabel "Direct link to accessibilitylabel")

Overrides the text that's read by the screen reader when the user interacts with the element. By default, the label is constructed by traversing all the children and accumulating all the `Text` nodes separated by space.

|  |  |
| --- | --- |
| Type|  | | --- | | string | |

---

### `accessibilityLanguage` iOS [​](#accessibilitylanguage-ios "Direct link to accessibilitylanguage-ios")

A value indicating which language should be used by the screen reader when the user interacts with the element. It should follow the [BCP 47 specification](https://www.rfc-editor.org/info/bcp47).

See the [iOS `accessibilityLanguage` doc](https://developer.apple.com/documentation/objectivec/nsobject/1615192-accessibilitylanguage) for more information.

|  |  |
| --- | --- |
| Type|  | | --- | | string | |

---

### `accessibilityHint`[​](#accessibilityhint "Direct link to accessibilityhint")

An accessibility hint helps users understand what will happen when they perform an action on the accessibility element when that result is not clear from the accessibility label.

|  |  |
| --- | --- |
| Type|  | | --- | | string | |

---

### `accessibilityRole`[​](#accessibilityrole "Direct link to accessibilityrole")

`accessibilityRole` communicates the purpose of a component to the user of an assistive technology.

`accessibilityRole` can be one of the following:

* `'none'` - Used when the element has no role.
* `'button'` - Used when the element should be treated as a button.
* `'link'` - Used when the element should be treated as a link.
* `'search'` - Used when the text field element should also be treated as a search field.
* `'image'` - Used when the element should be treated as an image. Can be combined with button or link, for example.
* `'keyboardkey'` - Used when the element acts as a keyboard key.
* `'text'` - Used when the element should be treated as static text that cannot change.
* `'adjustable'` - Used when an element can be "adjusted" (e.g. a slider).
* `'imagebutton'` - Used when the element should be treated as a button and is also an image.
* `'header'` - Used when an element acts as a header for a content section (e.g. the title of a navigation bar).
* `'summary'` - Used when an element can be used to provide a quick summary of current conditions in the app when the app first launches.
* `'alert'` - Used when an element contains important text to be presented to the user.
* `'checkbox'` - Used when an element represents a checkbox which can be checked, unchecked, or have mixed checked state.
* `'combobox'` - Used when an element represents a combo box, which allows the user to select among several choices.
* `'menu'` - Used when the component is a menu of choices.
* `'menubar'` - Used when a component is a container of multiple menus.
* `'menuitem'` - Used to represent an item within a menu.
* `'progressbar'` - Used to represent a component which indicates progress of a task.
* `'radio'` - Used to represent a radio button.
* `'radiogroup'` - Used to represent a group of radio buttons.
* `'scrollbar'` - Used to represent a scroll bar.
* `'spinbutton'` - Used to represent a button which opens a list of choices.
* `'switch'` - Used to represent a switch which can be turned on and off.
* `'tab'` - Used to represent a tab.
* `'tablist'` - Used to represent a list of tabs.
* `'timer'` - Used to represent a timer.
* `'toolbar'` - Used to represent a tool bar (a container of action buttons or components).

|  |  |
| --- | --- |
| Type|  | | --- | | string | |

---

### `accessibilityState`[​](#accessibilitystate "Direct link to accessibilitystate")

Describes the current state of a component to the user of an assistive technology.

See the [Accessibility guide](/docs/accessibility#accessibilitystate-ios-android) for more information.

|  |  |
| --- | --- |
| Type|  | | --- | | object: `{disabled: bool, selected: bool, checked: bool or 'mixed', busy: bool, expanded: bool}` | |

---

### `accessibilityActions`[​](#accessibilityactions "Direct link to accessibilityactions")

Accessibility actions allow an assistive technology to programmatically invoke the actions of a component. The `accessibilityActions` property should contain a list of action objects. Each action object should contain the field name and label.

See the [Accessibility guide](/docs/accessibility#accessibility-actions) for more information.

|  |  |
| --- | --- |
| Type|  | | --- | | array | |

---

### `aria-busy`[​](#aria-busy "Direct link to aria-busy")

Indicates an element is being modified and that assistive technologies may want to wait until the changes are complete before informing the user about the update.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | boolean false | | | |

---

### `aria-checked`[​](#aria-checked "Direct link to aria-checked")

Indicates the state of a checkable element. This field can either take a boolean or the "mixed" string to represent mixed checkboxes.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | boolean, 'mixed' false | | | |

---

### `aria-disabled`[​](#aria-disabled "Direct link to aria-disabled")

Indicates that the element is perceivable but disabled, so it is not editable or otherwise operable.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | boolean false | | | |

---

### `aria-expanded`[​](#aria-expanded "Direct link to aria-expanded")

Indicates whether an expandable element is currently expanded or collapsed.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | boolean false | | | |

---

### `aria-hidden`[​](#aria-hidden "Direct link to aria-hidden")

Indicates whether the accessibility elements contained within this accessibility element are hidden.

For example, in a window that contains sibling views `A` and `B`, setting `aria-hidden` to `true` on view `B` causes VoiceOver to ignore the elements in the view `B`.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | boolean false | | | |

---

### `aria-label`[​](#aria-label "Direct link to aria-label")

Defines a string value that labels an interactive element.

|  |  |
| --- | --- |
| Type|  | | --- | | string | |

---

### `aria-live` Android [​](#aria-live-android "Direct link to aria-live-android")

Indicates that an element will be updated, and describes the types of updates the user agents, assistive technologies, and user can expect from the live region.

* **off** Accessibility services should not announce changes to this view.
* **polite** Accessibility services should announce changes to this view.
* **assertive** Accessibility services should interrupt ongoing speech to immediately announce changes to this view.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | enum(`'assertive'`, `'off'`, `'polite'`) `'off'` | | | |

---

### `aria-modal` iOS [​](#aria-modal-ios "Direct link to aria-modal-ios")

Boolean value indicating whether VoiceOver should ignore the elements within views that are siblings of the receiver. Has precedence over the [`accessibilityViewIsModal`](#accessibilityviewismodal-ios) prop.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | boolean false | | | |

---

### `aria-selected`[​](#aria-selected "Direct link to aria-selected")

Indicates whether a selectable element is currently selected or not.

|  |  |
| --- | --- |
| Type|  | | --- | | boolean | |

### `onAccessibilityAction`[​](#onaccessibilityaction "Direct link to onaccessibilityaction")

Invoked when the user performs the accessibility actions. The only argument to this function is an event containing the name of the action to perform.

See the [Accessibility guide](/docs/accessibility#accessibility-actions) for more information.

|  |  |
| --- | --- |
| Type|  | | --- | | function | |

---

### `accessibilityValue`[​](#accessibilityvalue "Direct link to accessibilityvalue")

Represents the current value of a component. It can be a textual description of a component's value, or for range-based components, such as sliders and progress bars, it contains range information (minimum, current, and maximum).

See the [Accessibility guide](/docs/accessibility#accessibilityvalue-ios-android) for more information.

|  |  |
| --- | --- |
| Type|  | | --- | | object: `{min: number, max: number, now: number, text: string}` | |

---

### `aria-valuemax`[​](#aria-valuemax "Direct link to aria-valuemax")

Represents the maximum value for range-based components, such as sliders and progress bars. Has precedence over the `max` value in the `accessibilityValue` prop.

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

---

### `aria-valuemin`[​](#aria-valuemin "Direct link to aria-valuemin")

Represents the minimum value for range-based components, such as sliders and progress bars. Has precedence over the `min` value in the `accessibilityValue` prop.

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

---

### `aria-valuenow`[​](#aria-valuenow "Direct link to aria-valuenow")

Represents the current value for range-based components, such as sliders and progress bars. Has precedence over the `now` value in the `accessibilityValue` prop.

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

---

### `aria-valuetext`[​](#aria-valuetext "Direct link to aria-valuetext")

Represents the textual description of the component. Has precedence over the `text` value in the `accessibilityValue` prop.

|  |  |
| --- | --- |
| Type|  | | --- | | string | |

---

### `delayLongPress`[​](#delaylongpress "Direct link to delaylongpress")

Duration (in milliseconds) from `onPressIn` before `onLongPress` is called.

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

---

### `delayPressIn`[​](#delaypressin "Direct link to delaypressin")

Duration (in milliseconds), from the start of the touch, before `onPressIn` is called.

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

---

### `delayPressOut`[​](#delaypressout "Direct link to delaypressout")

Duration (in milliseconds), from the release of the touch, before `onPressOut` is called.

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

---

### `disabled`[​](#disabled "Direct link to disabled")

If true, disable all interactions for this component.

|  |  |
| --- | --- |
| Type|  | | --- | | bool | |

---

### `hitSlop`[​](#hitslop "Direct link to hitslop")

This defines how far your touch can start away from the button. This is added to `pressRetentionOffset` when moving off of the button.

> The touch area never extends past the parent view bounds and the Z-index of sibling views always takes precedence if a touch hits two overlapping views.

|  |  |
| --- | --- |
| Type|  | | --- | | [Rect](/docs/rect) or number | |

### `id`[​](#id "Direct link to id")

Used to locate this view from native code. Has precedence over `nativeID` prop.

|  |  |
| --- | --- |
| Type|  | | --- | | string | |

---

### `onBlur`[​](#onblur "Direct link to onblur")

Invoked when the item loses focus.

|  |  |
| --- | --- |
| Type|  | | --- | | function | |

---

### `onFocus`[​](#onfocus "Direct link to onfocus")

Invoked when the item receives focus.

|  |  |
| --- | --- |
| Type|  | | --- | | function | |

---

### `onLayout`[​](#onlayout "Direct link to onlayout")

Invoked on mount and on layout changes.

|  |  |
| --- | --- |
| Type|  | | --- | | `({nativeEvent: LayoutEvent}) => void` | |

---

### `onLongPress`[​](#onlongpress "Direct link to onlongpress")

Called if the time after `onPressIn` lasts longer than 370 milliseconds. This time period can be customized with [`delayLongPress`](#delaylongpress).

|  |  |
| --- | --- |
| Type|  | | --- | | function | |

---

### `onPress`[​](#onpress "Direct link to onpress")

Called when the touch is released, but not if cancelled (e.g. by a scroll that steals the responder lock). The first function argument is an event in form of [PressEvent](/docs/pressevent).

|  |  |
| --- | --- |
| Type|  | | --- | | function | |

---

### `onPressIn`[​](#onpressin "Direct link to onpressin")

Called as soon as the touchable element is pressed and invoked even before onPress. This can be useful when making network requests. The first function argument is an event in form of [PressEvent](/docs/pressevent).

|  |  |
| --- | --- |
| Type|  | | --- | | function | |

---

### `onPressOut`[​](#onpressout "Direct link to onpressout")

Called as soon as the touch is released even before onPress. The first function argument is an event in form of [PressEvent](/docs/pressevent).

|  |  |
| --- | --- |
| Type|  | | --- | | function | |

---

### `pressRetentionOffset`[​](#pressretentionoffset "Direct link to pressretentionoffset")

When the scroll view is disabled, this defines how far your touch may move off of the button, before deactivating the button. Once deactivated, try moving it back and you'll see that the button is once again reactivated! Move it back and forth several times while the scroll view is disabled. Ensure you pass in a constant to reduce memory allocations.

|  |  |
| --- | --- |
| Type|  | | --- | | [Rect](/docs/rect) or number | |

---

### `nativeID`[​](#nativeid "Direct link to nativeid")

|  |  |
| --- | --- |
| Type|  | | --- | | string | |

---

### `testID`[​](#testid "Direct link to testid")

Used to locate this view in end-to-end tests.

|  |  |
| --- | --- |
| Type|  | | --- | | string | |

---

### `touchSoundDisabled` Android [​](#touchsounddisabled-android "Direct link to touchsounddisabled-android")

If true, doesn't play a system sound on touch.

|  |  |
| --- | --- |
| Type|  | | --- | | Boolean | |

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/touchablewithoutfeedback.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/touchablewithoutfeedback.md)

Last updated on **Apr 14, 2025**

[Previous

TouchableOpacity](/docs/touchableopacity)[Next

View](/docs/view)

* [Usage Pattern](#usage-pattern)* [Example](#example)* [Props](#props)
      + [`accessibilityIgnoresInvertColors`

        iOS](#accessibilityignoresinvertcolors-ios)+ [`accessible`](#accessible)+ [`accessibilityLabel`](#accessibilitylabel)+ [`accessibilityLanguage`

              iOS](#accessibilitylanguage-ios)+ [`accessibilityHint`](#accessibilityhint)+ [`accessibilityRole`](#accessibilityrole)+ [`accessibilityState`](#accessibilitystate)+ [`accessibilityActions`](#accessibilityactions)+ [`aria-busy`](#aria-busy)+ [`aria-checked`](#aria-checked)+ [`aria-disabled`](#aria-disabled)+ [`aria-expanded`](#aria-expanded)+ [`aria-hidden`](#aria-hidden)+ [`aria-label`](#aria-label)+ [`aria-live`

                                    Android](#aria-live-android)+ [`aria-modal`

                                      iOS](#aria-modal-ios)+ [`aria-selected`](#aria-selected)+ [`onAccessibilityAction`](#onaccessibilityaction)+ [`accessibilityValue`](#accessibilityvalue)+ [`aria-valuemax`](#aria-valuemax)+ [`aria-valuemin`](#aria-valuemin)+ [`aria-valuenow`](#aria-valuenow)+ [`aria-valuetext`](#aria-valuetext)+ [`delayLongPress`](#delaylongpress)+ [`delayPressIn`](#delaypressin)+ [`delayPressOut`](#delaypressout)+ [`disabled`](#disabled)+ [`hitSlop`](#hitslop)+ [`id`](#id)+ [`onBlur`](#onblur)+ [`onFocus`](#onfocus)+ [`onLayout`](#onlayout)+ [`onLongPress`](#onlongpress)+ [`onPress`](#onpress)+ [`onPressIn`](#onpressin)+ [`onPressOut`](#onpressout)+ [`pressRetentionOffset`](#pressretentionoffset)+ [`nativeID`](#nativeid)+ [`testID`](#testid)+ [`touchSoundDisabled`

                                                                                      Android](#touchsounddisabled-android)

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