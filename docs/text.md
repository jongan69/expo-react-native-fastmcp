Text · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/text)

* [Next](/docs/next/text)* [0.79](/docs/text)* [0.78](/docs/0.78/text)* [0.77](/docs/0.77/text)* [0.76](/docs/0.76/text)* [0.75](/docs/0.75/text)* [0.74](/docs/0.74/text)* [0.73](/docs/0.73/text)* [0.72](/docs/0.72/text)* [0.71](/docs/0.71/text)* [0.70](/docs/0.70/text)* [All versions](/versions)

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

Text
====

A React component for displaying text.

`Text` supports nesting, styling, and touch handling.

In the following example, the nested title and body text will inherit the `fontFamily` from `styles.baseText`, but the title provides its own additional styles. The title and body will stack on top of each other on account of the literal newlines:

Nested text[​](#nested-text "Direct link to Nested text")
---------------------------------------------------------

Both Android and iOS allow you to display formatted text by annotating ranges of a string with specific formatting like bold or colored text (`NSAttributedString` on iOS, `SpannableString` on Android). In practice, this is very tedious. For React Native, we decided to use the web paradigm for this, where you can nest text to achieve the same effect.

Behind the scenes, React Native converts this to a flat `NSAttributedString` or `SpannableString` that contains the following information:

```
"I am bold and red"  
0-9: bold  
9-17: bold, red  

```

Containers[​](#containers "Direct link to Containers")
------------------------------------------------------

The `<Text>` element is unique relative to layout: everything inside is no longer using the Flexbox layout but using text layout. This means that elements inside of a `<Text>` are no longer rectangles, but wrap when they see the end of the line.

tsx

```
<Text>  
  <Text>First part and </Text>  
  <Text>second part</Text>  
</Text>  
// Text container: the text will be inline, if the space allows it  
// |First part and second part|  
  
// otherwise, the text will flow as if it was one  
// |First part |  
// |and second |  
// |part       |  
  
<View>  
  <Text>First part and </Text>  
  <Text>second part</Text>  
</View>  
// View container: each text is its own block  
// |First part and|  
// |second part   |  
  
// otherwise, the text will flow in its own block  
// |First part |  
// |and        |  
// |second part|  

```

Limited Style Inheritance[​](#limited-style-inheritance "Direct link to Limited Style Inheritance")
---------------------------------------------------------------------------------------------------

On the web, the usual way to set a font family and size for the entire document is to take advantage of inherited CSS properties like so:

css

```
html {  
  font-family:  
    'lucida grande', tahoma, verdana, arial, sans-serif;  
  font-size: 11px;  
  color: #141823;  
}  

```

All elements in the document will inherit this font unless they or one of their parents specifies a new rule.

In React Native, we are more strict about it: **you must wrap all the text nodes inside of a `<Text>` component**. You cannot have a text node directly under a `<View>`.

tsx

```
// BAD: will raise exception, can't have a text node as child of a <View>  
<View>  
  Some text  
</View>  
  
// GOOD  
<View>  
  <Text>  
    Some text  
  </Text>  
</View>  

```

You also lose the ability to set up a default font for an entire subtree. Meanwhile, `fontFamily` only accepts a single font name, which is different from `font-family` in CSS. The recommended way to use consistent fonts and sizes across your application is to create a component `MyAppText` that includes them and use this component across your app. You can also use this component to make more specific components like `MyAppHeaderText` for other kinds of text.

tsx

```
<View>  
  <MyAppText>  
    Text styled with the default font for the entire application  
  </MyAppText>  
  <MyAppHeaderText>Text styled as a header</MyAppHeaderText>  
</View>  

```

Assuming that `MyAppText` is a component that only renders out its children into a `Text` component with styling, then `MyAppHeaderText` can be defined as follows:

tsx

```
const MyAppHeaderText = ({children}) => {  
  return (  
    <MyAppText>  
      <Text style={{fontSize: 20}}>{children}</Text>  
    </MyAppText>  
  );  
};  

```

Composing `MyAppText` in this way ensures that we get the styles from a top-level component, but leaves us the ability to add/override them in specific use cases.

React Native still has the concept of style inheritance, but limited to text subtrees. In this case, the second part will be both bold and red.

tsx

```
<Text style={{fontWeight: 'bold'}}>  
  I am bold  
  <Text style={{color: 'red'}}>and red</Text>  
</Text>  

```

We believe that this more constrained way to style text will yield better apps:

* (Developer) React components are designed with strong isolation in mind: You should be able to drop a component anywhere in your application, trusting that as long as the props are the same, it will look and behave the same way. Text properties that could inherit from outside of the props would break this isolation.
* (Implementor) The implementation of React Native is also simplified. We do not need to have a `fontFamily` field on every single element, and we do not need to potentially traverse the tree up to the root every time we display a text node. The style inheritance is only encoded inside of the native Text component and doesn't leak to other components or the system itself.

---

Reference
=========

Props[​](#props "Direct link to Props")
---------------------------------------

### `accessibilityHint`[​](#accessibilityhint "Direct link to accessibilityhint")

An accessibility hint helps users understand what will happen when they perform an action on the accessibility element when that result is not clear from the accessibility label.

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

### `accessibilityLabel`[​](#accessibilitylabel "Direct link to accessibilitylabel")

Overrides the text that's read by the screen reader when the user interacts with the element. By default, the label is constructed by traversing all the children and accumulating all the `Text` nodes separated by space.

|  |  |
| --- | --- |
| Type|  | | --- | | string | |

---

### `accessibilityRole`[​](#accessibilityrole "Direct link to accessibilityrole")

Tells the screen reader to treat the currently focused on element as having a specific role.

On iOS, these roles map to corresponding Accessibility Traits. Image button has the same functionality as if the trait was set to both 'image' and 'button'. See the [Accessibility guide](/docs/accessibility#accessibilitytraits-ios) for more information.

On Android, these roles have similar functionality on TalkBack as adding Accessibility Traits does on Voiceover in iOS

|  |  |
| --- | --- |
| Type|  | | --- | | [AccessibilityRole](/docs/accessibility#accessibilityrole) | |

---

### `accessibilityState`[​](#accessibilitystate "Direct link to accessibilitystate")

Tells the screen reader to treat the currently focused on element as being in a specific state.

You can provide one state, no state, or multiple states. The states must be passed in through an object, e.g. `{selected: true, disabled: true}`.

|  |  |
| --- | --- |
| Type|  | | --- | | [AccessibilityState](/docs/accessibility#accessibilitystate) | |

---

### `accessibilityActions`[​](#accessibilityactions "Direct link to accessibilityactions")

Accessibility actions allow an assistive technology to programmatically invoke the actions of a component. The `accessibilityActions` property should contain a list of action objects. Each action object should contain the field name and label.

See the [Accessibility guide](/docs/accessibility#accessibility-actions) for more information.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | array No | | | |

---

### `onAccessibilityAction`[​](#onaccessibilityaction "Direct link to onaccessibilityaction")

Invoked when the user performs the accessibility actions. The only argument to this function is an event containing the name of the action to perform.

See the [Accessibility guide](/docs/accessibility#accessibility-actions) for more information.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Required|  |  | | --- | --- | | function No | | | |

---

### `accessible`[​](#accessible "Direct link to accessible")

When set to `true`, indicates that the view is an accessibility element.

See the [Accessibility guide](/docs/accessibility#accessible-ios-android) for more information.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | boolean `true` | | | |

---

### `adjustsFontSizeToFit`[​](#adjustsfontsizetofit "Direct link to adjustsfontsizetofit")

Specifies whether fonts should be scaled down automatically to fit given style constraints.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | boolean `false` | | | |

---

### `allowFontScaling`[​](#allowfontscaling "Direct link to allowfontscaling")

Specifies whether fonts should scale to respect Text Size accessibility settings.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | boolean `true` | | | |

---

### `android_hyphenationFrequency` Android [​](#android_hyphenationfrequency-android "Direct link to android_hyphenationfrequency-android")

Sets the frequency of automatic hyphenation to use when determining word breaks on Android API Level 23+.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | enum(`'none'`, `'normal'`,`'full'`) `'none'` | | | |

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

### `aria-label`[​](#aria-label "Direct link to aria-label")

Defines a string value that labels an interactive element.

|  |  |
| --- | --- |
| Type|  | | --- | | string | |

---

### `aria-selected`[​](#aria-selected "Direct link to aria-selected")

Indicates whether a selectable element is currently selected or not.

|  |  |
| --- | --- |
| Type|  | | --- | | boolean | |

### `dataDetectorType` Android [​](#datadetectortype-android "Direct link to datadetectortype-android")

Determines the types of data converted to clickable URLs in the text element. By default, no data types are detected.

You can provide only one type.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | enum(`'phoneNumber'`, `'link'`, `'email'`, `'none'`, `'all'`) `'none'` | | | |

---

### `disabled` Android [​](#disabled-android "Direct link to disabled-android")

Specifies the disabled state of the text view for testing purposes.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | bool `false` | | | |

---

### `dynamicTypeRamp` iOS [​](#dynamictyperamp-ios "Direct link to dynamictyperamp-ios")

The [Dynamic Type](https://developer.apple.com/documentation/uikit/uifont/scaling_fonts_automatically) ramp to apply to this element on iOS.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | enum(`'caption2'`, `'caption1'`, `'footnote'`, `'subheadline'`, `'callout'`, `'body'`, `'headline'`, `'title3'`, `'title2'`, `'title1'`, `'largeTitle'`) `'body'` | | | |

---

### `ellipsizeMode`[​](#ellipsizemode "Direct link to ellipsizemode")

When `numberOfLines` is set, this prop defines how the text will be truncated. `numberOfLines` must be set in conjunction with this prop.

This can be one of the following values:

* `head` - The line is displayed so that the end fits in the container and the missing text at the beginning of the line is indicated by an ellipsis glyph. e.g., "...wxyz"
* `middle` - The line is displayed so that the beginning and end fit in the container and the missing text in the middle is indicated by an ellipsis glyph. "ab...yz"
* `tail` - The line is displayed so that the beginning fits in the container and the missing text at the end of the line is indicated by an ellipsis glyph. e.g., "abcd..."
* `clip` - Lines are not drawn past the edge of the text container.

> On Android, when `numberOfLines` is set to a value higher than `1`, only `tail` value will work correctly.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | enum(`'head'`, `'middle'`, `'tail'`, `'clip'`) `tail` | | | |

---

### `id`[​](#id "Direct link to id")

Used to locate this view from native code. Has precedence over `nativeID` prop.

|  |  |
| --- | --- |
| Type|  | | --- | | string | |

---

### `maxFontSizeMultiplier`[​](#maxfontsizemultiplier "Direct link to maxfontsizemultiplier")

Specifies the largest possible scale a font can reach when `allowFontScaling` is enabled. Possible values:

* `null/undefined`: inherit from the parent node or the global default (0)
* `0`: no max, ignore parent/global default
* `>= 1`: sets the `maxFontSizeMultiplier` of this node to this value

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | number `undefined` | | | |

---

### `minimumFontScale` iOS [​](#minimumfontscale-ios "Direct link to minimumfontscale-ios")

Specifies the smallest possible scale a font can reach when `adjustsFontSizeToFit` is enabled. (values 0.01-1.0).

|  |  |
| --- | --- |
| Type|  | | --- | | number | |

---

### `nativeID`[​](#nativeid "Direct link to nativeid")

Used to locate this view from native code.

|  |  |
| --- | --- |
| Type|  | | --- | | string | |

---

### `numberOfLines`[​](#numberoflines "Direct link to numberoflines")

Used to truncate the text with an ellipsis after computing the text layout, including line wrapping, such that the total number of lines does not exceed this number. Setting this property to `0` will result in unsetting this value, which means that no lines restriction will be applied.

This prop is commonly used with `ellipsizeMode`.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | number `0` | | | |

---

### `onLayout`[​](#onlayout "Direct link to onlayout")

Invoked on mount and on layout changes.

|  |  |
| --- | --- |
| Type|  | | --- | | `({nativeEvent: LayoutEvent}) => void` | |

---

### `onLongPress`[​](#onlongpress "Direct link to onlongpress")

This function is called on long press.

|  |  |
| --- | --- |
| Type|  | | --- | | `({nativeEvent: PressEvent}) => void` | |

---

### `onMoveShouldSetResponder`[​](#onmoveshouldsetresponder "Direct link to onmoveshouldsetresponder")

Does this view want to "claim" touch responsiveness? This is called for every touch move on the `View` when it is not the responder.

|  |  |
| --- | --- |
| Type|  | | --- | | `({nativeEvent: PressEvent}) => boolean` | |

---

### `onPress`[​](#onpress "Direct link to onpress")

Function called on user press, triggered after `onPressOut`.

|  |  |
| --- | --- |
| Type|  | | --- | | `({nativeEvent: PressEvent}) => void` | |

---

### `onPressIn`[​](#onpressin "Direct link to onpressin")

Called immediately when a touch is engaged, before `onPressOut` and `onPress`.

|  |  |
| --- | --- |
| Type|  | | --- | | `({nativeEvent: PressEvent}) => void` | |

---

### `onPressOut`[​](#onpressout "Direct link to onpressout")

Called when a touch is released.

|  |  |
| --- | --- |
| Type|  | | --- | | `({nativeEvent: PressEvent}) => void` | |

---

### `onResponderGrant`[​](#onrespondergrant "Direct link to onrespondergrant")

The View is now responding to touch events. This is the time to highlight and show the user what is happening.

On Android, return true from this callback to prevent any other native components from becoming responder until this responder terminates.

|  |  |
| --- | --- |
| Type|  | | --- | | `({nativeEvent: PressEvent}) => void ｜ boolean` | |

---

### `onResponderMove`[​](#onrespondermove "Direct link to onrespondermove")

The user is moving their finger.

|  |  |
| --- | --- |
| Type|  | | --- | | `({nativeEvent: PressEvent}) => void` | |

---

### `onResponderRelease`[​](#onresponderrelease "Direct link to onresponderrelease")

Fired at the end of the touch.

|  |  |
| --- | --- |
| Type|  | | --- | | `({nativeEvent: PressEvent}) => void` | |

---

### `onResponderTerminate`[​](#onresponderterminate "Direct link to onresponderterminate")

The responder has been taken from the `View`. Might be taken by other views after a call to `onResponderTerminationRequest`, or might be taken by the OS without asking (e.g., happens with control center/ notification center on iOS)

|  |  |
| --- | --- |
| Type|  | | --- | | `({nativeEvent: PressEvent}) => void` | |

---

### `onResponderTerminationRequest`[​](#onresponderterminationrequest "Direct link to onresponderterminationrequest")

Some other `View` wants to become a responder and is asking this `View` to release its responder. Returning `true` allows its release.

|  |  |
| --- | --- |
| Type|  | | --- | | `({nativeEvent: PressEvent}) => boolean` | |

---

### `onStartShouldSetResponderCapture`[​](#onstartshouldsetrespondercapture "Direct link to onstartshouldsetrespondercapture")

If a parent `View` wants to prevent a child `View` from becoming a responder on a touch start, it should have this handler which returns `true`.

|  |  |
| --- | --- |
| Type|  | | --- | | `({nativeEvent: PressEvent}) => boolean` | |

---

### `onTextLayout`[​](#ontextlayout "Direct link to ontextlayout")

Invoked on Text layout change.

|  |  |
| --- | --- |
| Type|  | | --- | | ([`TextLayoutEvent`](/docs/text#textlayoutevent)) => mixed | |

---

### `pressRetentionOffset`[​](#pressretentionoffset "Direct link to pressretentionoffset")

When the scroll view is disabled, this defines how far your touch may move off of the button, before deactivating the button. Once deactivated, try moving it back and you'll see that the button is once again reactivated! Move it back and forth several times while the scroll view is disabled. Ensure you pass in a constant to reduce memory allocations.

|  |  |
| --- | --- |
| Type|  | | --- | | [Rect](/docs/rect), number | |

---

### `role`[​](#role "Direct link to role")

`role` communicates the purpose of a component to the user of an assistive technology. Has precedence over the [`accessibilityRole`](/docs/text#accessibilityrole) prop.

|  |  |
| --- | --- |
| Type|  | | --- | | [Role](/docs/accessibility#role) | |

---

### `selectable`[​](#selectable "Direct link to selectable")

Lets the user select text, to use the native copy and paste functionality.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | boolean `false` | | | |

---

### `selectionColor` Android [​](#selectioncolor-android "Direct link to selectioncolor-android")

The highlight color of the text.

|  |  |
| --- | --- |
| Type|  | | --- | | [color](/docs/colors) | |

---

### `style`[​](#style "Direct link to style")

|  |  |
| --- | --- |
| Type|  | | --- | | [Text Style](/docs/text-style-props), [View Style Props](/docs/view-style-props) | |

---

### `suppressHighlighting` iOS [​](#suppresshighlighting-ios "Direct link to suppresshighlighting-ios")

When `true`, no visual change is made when text is pressed down. By default, a gray oval highlights the text on press down.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | boolean `false` | | | |

---

### `testID`[​](#testid "Direct link to testid")

Used to locate this view in end-to-end tests.

|  |  |
| --- | --- |
| Type|  | | --- | | string | |

---

### `textBreakStrategy` Android [​](#textbreakstrategy-android "Direct link to textbreakstrategy-android")

Set text break strategy on Android API Level 23+, possible values are `simple`, `highQuality`, `balanced`.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | enum(`'simple'`, `'highQuality'`, `'balanced'`) `highQuality` | | | |

---

### `lineBreakStrategyIOS` iOS [​](#linebreakstrategyios-ios "Direct link to linebreakstrategyios-ios")

Set line break strategy on iOS 14+. Possible values are `none`, `standard`, `hangul-word` and `push-out`.

|  |  |  |  |
| --- | --- | --- | --- |
| Type Default|  |  | | --- | --- | | enum(`'none'`, `'standard'`, `'hangul-word'`, `'push-out'`) `'none'` | | | |

Type Definitions[​](#type-definitions "Direct link to Type Definitions")
------------------------------------------------------------------------

### TextLayout[​](#textlayout "Direct link to TextLayout")

`TextLayout` object is a part of [`TextLayoutEvent`](/docs/text#textlayoutevent) callback and contains the measurement data for `Text` line.

#### Example[​](#example "Direct link to Example")

js

```
{  
    capHeight: 10.496,  
    ascender: 14.624,  
    descender: 4,  
    width: 28.224,  
    height: 18.624,  
    xHeight: 6.048,  
    x: 0,  
    y: 0  
}  

```

#### Properties[​](#properties "Direct link to Properties")

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Optional Description|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | ascender number No The line ascender height after the text layout changes.|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | capHeight number No Height of capital letter above the baseline.|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | descender number No The line descender height after the text layout changes.|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | height number No Height of the line after the text layout changes.|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | width number No Width of the line after the text layout changes.|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | x number No Line X coordinate inside the Text component.|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | xHeight number No Distance between the baseline and median of the line (corpus size).|  |  |  |  | | --- | --- | --- | --- | | y number No Line Y coordinate inside the Text component. | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

### TextLayoutEvent[​](#textlayoutevent "Direct link to TextLayoutEvent")

`TextLayoutEvent` object is returned in the callback as a result of a component layout change. It contains a key called `lines` with a value which is an array containing [`TextLayout`](/docs/text#textlayout) object corresponded to every rendered text line.

#### Example[​](#example-1 "Direct link to Example")

js

```
{  
  lines: [  
    TextLayout,  
    TextLayout,  
    // ...  
  ];  
  target: 1127;  
}  

```

#### Properties[​](#properties-1 "Direct link to Properties")

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Optional Description|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | lines array of [TextLayout](/docs/text#textlayout)s No Provides the TextLayout data for every rendered line.|  |  |  |  | | --- | --- | --- | --- | | target number No The node id of the element. | | | | | | | | | | | |

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/text.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/text.md)

Last updated on **Apr 14, 2025**

[Previous

Switch](/docs/switch)[Next

TextInput](/docs/textinput)

* [Nested text](#nested-text)* [Containers](#containers)* [Limited Style Inheritance](#limited-style-inheritance)* [Props](#props)
        + [`accessibilityHint`](#accessibilityhint)+ [`accessibilityLanguage`

            iOS](#accessibilitylanguage-ios)+ [`accessibilityLabel`](#accessibilitylabel)+ [`accessibilityRole`](#accessibilityrole)+ [`accessibilityState`](#accessibilitystate)+ [`accessibilityActions`](#accessibilityactions)+ [`onAccessibilityAction`](#onaccessibilityaction)+ [`accessible`](#accessible)+ [`adjustsFontSizeToFit`](#adjustsfontsizetofit)+ [`allowFontScaling`](#allowfontscaling)+ [`android_hyphenationFrequency`

                              Android](#android_hyphenationfrequency-android)+ [`aria-busy`](#aria-busy)+ [`aria-checked`](#aria-checked)+ [`aria-disabled`](#aria-disabled)+ [`aria-expanded`](#aria-expanded)+ [`aria-label`](#aria-label)+ [`aria-selected`](#aria-selected)+ [`dataDetectorType`

                                            Android](#datadetectortype-android)+ [`disabled`

                                              Android](#disabled-android)+ [`dynamicTypeRamp`

                                                iOS](#dynamictyperamp-ios)+ [`ellipsizeMode`](#ellipsizemode)+ [`id`](#id)+ [`maxFontSizeMultiplier`](#maxfontsizemultiplier)+ [`minimumFontScale`

                                                        iOS](#minimumfontscale-ios)+ [`nativeID`](#nativeid)+ [`numberOfLines`](#numberoflines)+ [`onLayout`](#onlayout)+ [`onLongPress`](#onlongpress)+ [`onMoveShouldSetResponder`](#onmoveshouldsetresponder)+ [`onPress`](#onpress)+ [`onPressIn`](#onpressin)+ [`onPressOut`](#onpressout)+ [`onResponderGrant`](#onrespondergrant)+ [`onResponderMove`](#onrespondermove)+ [`onResponderRelease`](#onresponderrelease)+ [`onResponderTerminate`](#onresponderterminate)+ [`onResponderTerminationRequest`](#onresponderterminationrequest)+ [`onStartShouldSetResponderCapture`](#onstartshouldsetrespondercapture)+ [`onTextLayout`](#ontextlayout)+ [`pressRetentionOffset`](#pressretentionoffset)+ [`role`](#role)+ [`selectable`](#selectable)+ [`selectionColor`

                                                                                              Android](#selectioncolor-android)+ [`style`](#style)+ [`suppressHighlighting`

                                                                                                  iOS](#suppresshighlighting-ios)+ [`testID`](#testid)+ [`textBreakStrategy`

                                                                                                      Android](#textbreakstrategy-android)+ [`lineBreakStrategyIOS`

                                                                                                        iOS](#linebreakstrategyios-ios)* [Type Definitions](#type-definitions)
          + [TextLayout](#textlayout)+ [TextLayoutEvent](#textlayoutevent)

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