🚧 AlertIOS · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/alertios)

* [Next](/docs/next/alertios)* [0.79](/docs/alertios)* [0.78](/docs/0.78/alertios)* [0.77](/docs/0.77/alertios)* [0.76](/docs/0.76/alertios)* [0.75](/docs/0.75/alertios)* [0.74](/docs/0.74/alertios)* [0.73](/docs/0.73/alertios)* [0.72](/docs/0.72/alertios)* [0.71](/docs/0.71/alertios)* [0.70](/docs/0.70/alertios)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

On this page

🚧 AlertIOS
==========

> **Removed.** Use [`Alert`](/docs/alert) instead.

`AlertIOS` provides functionality to create an iOS alert dialog with a message or create a prompt for user input.

Creating an iOS alert:

jsx

```
AlertIOS.alert(  
  'Sync Complete',  
  'All your data are belong to us.',  
);  

```

Creating an iOS prompt:

jsx

```
AlertIOS.prompt('Enter a value', null, text =>  
  console.log('You entered ' + text),  
);  

```

We recommend using the [`Alert.alert`](/docs/alert) method for cross-platform support if you don't need to create iOS-only prompts.

---

Reference
=========

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### `alert()`[​](#alert "Direct link to alert")

jsx

```
static alert(title: string, [message]: string, [callbackOrButtons]: ?(() => void), ButtonsArray, [type]: AlertType): [object Object]  

```

Create and display a popup alert.

**Parameters:**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | title string Yes The dialog's title. Passing null or '' will hide the title.|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | message string No An optional message that appears below the dialog's title.|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | callbackOrButtons ?(() => void),[ButtonsArray](/docs/alertios#buttonsarray) No This optional argument should be either a single-argument function or an array of buttons. If passed a function, it will be called when the user taps 'OK'. If passed an array of button configurations, each button should include a `text` key, as well as optional `onPress` and `style` keys. `style` should be one of 'default', 'cancel' or 'destructive'.| type [AlertType](/docs/alertios#alerttype) No Deprecated, do not use. | | | | | | | | | | | | | | | | | | | |

Example with custom buttons:

jsx

```
AlertIOS.alert(  
  'Update available',  
  'Keep your app up to date to enjoy the latest features',  
  [  
    {  
      text: 'Cancel',  
      onPress: () => console.log('Cancel Pressed'),  
      style: 'cancel',  
    },  
    {  
      text: 'Install',  
      onPress: () => console.log('Install Pressed'),  
    },  
  ],  
);  

```

---

### `prompt()`[​](#prompt "Direct link to prompt")

jsx

```
static prompt(title: string, [message]: string, [callbackOrButtons]: ?((text: string) => void), ButtonsArray, [type]: AlertType, [defaultValue]: string, [keyboardType]: string): [object Object]  

```

Create and display a prompt to enter some text.

**Parameters:**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | title string Yes The dialog's title.|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | message string No An optional message that appears above the text input.|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | callbackOrButtons ?((text: string) => void),[ButtonsArray](/docs/alertios#buttonsarray) No This optional argument should be either a single-argument function or an array of buttons. If passed a function, it will be called with the prompt's value when the user taps 'OK'. If passed an array of button configurations, each button should include a `text` key, as well as optional `onPress` and `style` keys (see example). `style` should be one of 'default', 'cancel' or 'destructive'.| type [AlertType](/docs/alertios#alerttype) No This configures the text input. One of 'plain-text', 'secure-text' or 'login-password'.|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | defaultValue string No The default text in text input.|  |  |  |  | | --- | --- | --- | --- | | keyboardType string No The keyboard type of first text field(if exists). One of 'default', 'email-address', 'numeric', 'phone-pad', 'ascii-capable', 'numbers-and-punctuation', 'url', 'number-pad', 'name-phone-pad', 'decimal-pad', 'twitter' or 'web-search'. | | | | | | | | | | | | | | | | | | | | | | | | | | | |

Example with custom buttons:

jsx

```
AlertIOS.prompt(  
  'Enter password',  
  'Enter your password to claim your $1.5B in lottery winnings',  
  [  
    {  
      text: 'Cancel',  
      onPress: () => console.log('Cancel Pressed'),  
      style: 'cancel',  
    },  
    {  
      text: 'OK',  
      onPress: password =>  
        console.log('OK Pressed, password: ' + password),  
    },  
  ],  
  'secure-text',  
);  

```

,

Example with the default button and a custom callback:

jsx

```
AlertIOS.prompt(  
  'Update username',  
  null,  
  text => console.log('Your username is ' + text),  
  null,  
  'default',  
);  

```

Type Definitions[​](#type-definitions "Direct link to Type Definitions")
------------------------------------------------------------------------

### AlertType[​](#alerttype "Direct link to AlertType")

An Alert button type

|  |  |
| --- | --- |
| Type|  | | --- | | $Enum | |

**Constants:**

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Value Description|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | default Default alert with no inputs|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | plain-text Plain text input alert|  |  |  |  | | --- | --- | --- | --- | | secure-text Secure text input alert|  |  | | --- | --- | | login-password Login and password alert | | | | | | | | | |

---

### AlertButtonStyle[​](#alertbuttonstyle "Direct link to AlertButtonStyle")

An Alert button style

|  |  |
| --- | --- |
| Type|  | | --- | | $Enum | |

**Constants:**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Value Description|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | default Default button style|  |  |  |  | | --- | --- | --- | --- | | cancel Cancel button style|  |  | | --- | --- | | destructive Destructive button style | | | | | | | |

---

### ButtonsArray[​](#buttonsarray "Direct link to ButtonsArray")

Array or buttons

|  |  |
| --- | --- |
| Type|  | | --- | | Array | |

**Properties:**

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Description|  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | [text] string Button label|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | [onPress] function Callback function when button pressed|  |  |  | | --- | --- | --- | | [style] [AlertButtonStyle](/docs/alertios#alertbuttonstyle) Button style | | | | | | | | | | | |

**Constants:**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Value Description|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | text Button label|  |  |  |  | | --- | --- | --- | --- | | onPress Callback function when button pressed|  |  | | --- | --- | | style Button style | | | | | | | |

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/alertios.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/alertios.md)

Last updated on **Apr 14, 2025**

* [Methods](#methods)
  + [`alert()`](#alert)+ [`prompt()`](#prompt)* [Type Definitions](#type-definitions)
    + [AlertType](#alerttype)+ [AlertButtonStyle](#alertbuttonstyle)+ [ButtonsArray](#buttonsarray)

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