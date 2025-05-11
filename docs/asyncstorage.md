🚧 AsyncStorage · React Native

[Skip to main content](#__docusaurus_skipToContent_fallback)

Join us for React Conf on Oct 7-8. [Learn more](https://conf.react.dev).

[![React Native](/img/header_logo.svg)![React Native](/img/header_logo.svg)

**React Native**](/)

[0.79](/docs/asyncstorage)

* [Next](/docs/next/asyncstorage)* [0.79](/docs/asyncstorage)* [0.78](/docs/0.78/asyncstorage)* [0.77](/docs/0.77/asyncstorage)* [0.76](/docs/0.76/asyncstorage)* [0.75](/docs/0.75/asyncstorage)* [0.74](/docs/0.74/asyncstorage)* [0.73](/docs/0.73/asyncstorage)* [0.72](/docs/0.72/asyncstorage)* [0.71](/docs/0.71/asyncstorage)* [0.70](/docs/0.70/asyncstorage)* [All versions](/versions)

[Development](#)

* [Guides](/docs/getting-started)* [Components](/docs/components-and-apis)* [APIs](/docs/accessibilityinfo)* [Architecture](/architecture/overview)

[Contributing](/contributing/overview)[Community](/community/overview)[Showcase](/showcase)[Blog](/blog)

Search

On this page

🚧 AsyncStorage
==============

> **Removed.** Use one of the [community packages](https://reactnative.directory/?search=storage) instead.

`AsyncStorage` is an unencrypted, asynchronous, persistent, key-value storage system that is global to the app. It should be used instead of LocalStorage.

It is recommended that you use an abstraction on top of `AsyncStorage` instead of `AsyncStorage` directly for anything more than light usage since it operates globally.

On iOS, `AsyncStorage` is backed by native code that stores small values in a serialized dictionary and larger values in separate files. On Android, `AsyncStorage` will use either [RocksDB](https://rocksdb.org/) or SQLite based on what is available.

The `AsyncStorage` JavaScript code is a facade that provides a clear JavaScript API, real `Error` objects, and non-multi functions. Each method in the API returns a `Promise` object.

Importing the `AsyncStorage` library:

jsx

```
import {AsyncStorage} from 'react-native';  

```

Persisting data:

jsx

```
_storeData = async () => {  
  try {  
    await AsyncStorage.setItem(  
      '@MySuperStore:key',  
      'I like to save it.',  
    );  
  } catch (error) {  
    // Error saving data  
  }  
};  

```

Fetching data:

jsx

```
_retrieveData = async () => {  
  try {  
    const value = await AsyncStorage.getItem('TASKS');  
    if (value !== null) {  
      // We have data!!  
      console.log(value);  
    }  
  } catch (error) {  
    // Error retrieving data  
  }  
};  

```

---

Reference
=========

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### `getItem()`[​](#getitem "Direct link to getitem")

jsx

```
static getItem(key: string, [callback]: ?(error: ?Error, result: ?string) => void)  

```

Fetches an item for a `key` and invokes a callback upon completion. Returns a `Promise` object.

**Parameters:**

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | key string Yes Key of the item to fetch.|  |  |  |  | | --- | --- | --- | --- | | callback `?(error: ?Error, result: ?string) => void` No Function that will be called with a result if found or any error. | | | | | | | | | | | |

---

### `setItem()`[​](#setitem "Direct link to setitem")

jsx

```
static setItem(key: string, value: string, [callback]: ?(error: ?Error) => void)  

```

Sets the value for a `key` and invokes a callback upon completion. Returns a `Promise` object.

**Parameters:**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | key string Yes Key of the item to set.|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | value string Yes Value to set for the `key`.| callback `?(error: ?Error) => void` No Function that will be called with any error. | | | | | | | | | | | | | | | |

---

### `removeItem()`[​](#removeitem "Direct link to removeitem")

jsx

```
static removeItem(key: string, [callback]: ?(error: ?Error) => void)  

```

Removes an item for a `key` and invokes a callback upon completion. Returns a `Promise` object.

**Parameters:**

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | key string Yes Key of the item to remove.|  |  |  |  | | --- | --- | --- | --- | | callback `?(error: ?Error) => void` No Function that will be called with any error. | | | | | | | | | | | |

---

### `mergeItem()`[​](#mergeitem "Direct link to mergeitem")

jsx

```
static mergeItem(key: string, value: string, [callback]: ?(error: ?Error) => void)  

```

Merges an existing `key` value with an input value, assuming both values are stringified JSON. Returns a `Promise` object.

**NOTE:** This is not supported by all native implementations.

**Parameters:**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | key string Yes Key of the item to modify.|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | value string Yes New value to merge for the `key`.| callback `?(error: ?Error) => void` No Function that will be called with any error. | | | | | | | | | | | | | | | |

Example:

jsx

```
let UID123_object = {  
  name: 'Chris',  
  age: 30,  
  traits: {hair: 'brown', eyes: 'brown'},  
};  
// You only need to define what will be added or updated  
let UID123_delta = {  
  age: 31,  
  traits: {eyes: 'blue', shoe_size: 10},  
};  
  
AsyncStorage.setItem(  
  'UID123',  
  JSON.stringify(UID123_object),  
  () => {  
    AsyncStorage.mergeItem(  
      'UID123',  
      JSON.stringify(UID123_delta),  
      () => {  
        AsyncStorage.getItem('UID123', (err, result) => {  
          console.log(result);  
        });  
      },  
    );  
  },  
);  
  
// Console log result:  
// => {'name':'Chris','age':31,'traits':  
//    {'shoe_size':10,'hair':'brown','eyes':'blue'}}  

```

---

### `clear()`[​](#clear "Direct link to clear")

jsx

```
static clear([callback]: ?(error: ?Error) => void)  

```

Erases *all* `AsyncStorage` for all clients, libraries, etc. You probably don't want to call this; use `removeItem` or `multiRemove` to clear only your app's keys. Returns a `Promise` object.

**Parameters:**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  | | --- | --- | --- | --- | | callback `?(error: ?Error) => void` No Function that will be called with any error. | | | | | | | |

---

### `getAllKeys()`[​](#getallkeys "Direct link to getallkeys")

jsx

```
static getAllKeys([callback]: ?(error: ?Error, keys: ?Array<string>) => void)  

```

Gets *all* keys known to your app; for all callers, libraries, etc. Returns a `Promise` object.

**Parameters:**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  | | --- | --- | --- | --- | | callback `?(error: ?Error, keys: ?Array<string>) => void` No Function that will be called with all keys found and any error. | | | | | | | |

---

### `flushGetRequests()`[​](#flushgetrequests "Direct link to flushgetrequests")

jsx

```
static flushGetRequests(): [object Object]  

```

Flushes any pending requests using a single batch call to get the data.

---

### `multiGet()`[​](#multiget "Direct link to multiget")

jsx

```
static multiGet(keys: Array<string>, [callback]: ?(errors: ?Array<Error>, result: ?Array<Array<string>>) => void)  

```

This allows you to batch the fetching of items given an array of `key` inputs. Your callback will be invoked with an array of corresponding key-value pairs found:

```
multiGet(['k1', 'k2'], cb) -> cb([['k1', 'val1'], ['k2', 'val2']])  

```

The method returns a `Promise` object.

**Parameters:**

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | keys `Array<string>` Yes Array of key for the items to get.|  |  |  |  | | --- | --- | --- | --- | | callback `?(errors: ?Array<Error>, result: ?Array<Array<string>>) => void` No Function that will be called with a key-value array of the results, plus an array of any key-specific errors found. | | | | | | | | | | | |

Example:

jsx

```
AsyncStorage.getAllKeys((err, keys) => {  
  AsyncStorage.multiGet(keys, (err, stores) => {  
    stores.map((result, i, store) => {  
      // get at each store's key/value so you can work with it  
      let key = store[i][0];  
      let value = store[i][1];  
    });  
  });  
});  

```

---

### `multiSet()`[​](#multiset "Direct link to multiset")

jsx

```
static multiSet(keyValuePairs: Array<Array<string>>, [callback]: ?(errors: ?Array<Error>) => void)  

```

Use this as a batch operation for storing multiple key-value pairs. When the operation completes you'll get a single callback with any errors:

```
multiSet([['k1', 'val1'], ['k2', 'val2']], cb);  

```

The method returns a `Promise` object.

**Parameters:**

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | keyValuePairs `Array<Array<string>>` Yes Array of key-value array for the items to set.|  |  |  |  | | --- | --- | --- | --- | | callback `?(errors: ?Array<Error>) => void` No Function that will be called with an array of any key-specific errors found. | | | | | | | | | | | |

---

### `multiRemove()`[​](#multiremove "Direct link to multiremove")

jsx

```
static multiRemove(keys: Array<string>, [callback]: ?(errors: ?Array<Error>) => void)  

```

Call this to batch the deletion of all keys in the `keys` array. Returns a `Promise` object.

**Parameters:**

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | keys `Array<string>` Yes Array of key for the items to delete.|  |  |  |  | | --- | --- | --- | --- | | callback `?(errors: ?Array<Error>) => void` No Function that will be called an array of any key-specific errors found. | | | | | | | | | | | |

Example:

jsx

```
let keys = ['k1', 'k2'];  
AsyncStorage.multiRemove(keys, err => {  
  // keys k1 & k2 removed, if they existed  
  // do most stuff after removal (if you want)  
});  

```

---

### `multiMerge()`[​](#multimerge "Direct link to multimerge")

jsx

```
static multiMerge(keyValuePairs: Array<Array<string>>, [callback]: ?(errors: ?Array<Error>) => void)  

```

Batch operation to merge in existing and new values for a given set of keys. This assumes that the values are stringified JSON. Returns a `Promise` object.

**NOTE**: This is not supported by all native implementations.

**Parameters:**

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | keyValuePairs `Array<Array<string>>` Yes Array of key-value array for the items to merge.|  |  |  |  | | --- | --- | --- | --- | | callback `?(errors: ?Array<Error>) => void` No Function that will be called with an array of any key-specific errors found. | | | | | | | | | | | |

Example:

jsx

```
// first user, initial values  
let UID234_object = {  
  name: 'Chris',  
  age: 30,  
  traits: {hair: 'brown', eyes: 'brown'},  
};  
  
// first user, delta values  
let UID234_delta = {  
  age: 31,  
  traits: {eyes: 'blue', shoe_size: 10},  
};  
  
// second user, initial values  
let UID345_object = {  
  name: 'Marge',  
  age: 25,  
  traits: {hair: 'blonde', eyes: 'blue'},  
};  
  
// second user, delta values  
let UID345_delta = {  
  age: 26,  
  traits: {eyes: 'green', shoe_size: 6},  
};  
  
let multi_set_pairs = [  
  ['UID234', JSON.stringify(UID234_object)],  
  ['UID345', JSON.stringify(UID345_object)],  
];  
let multi_merge_pairs = [  
  ['UID234', JSON.stringify(UID234_delta)],  
  ['UID345', JSON.stringify(UID345_delta)],  
];  
  
AsyncStorage.multiSet(multi_set_pairs, err => {  
  AsyncStorage.multiMerge(multi_merge_pairs, err => {  
    AsyncStorage.multiGet(['UID234', 'UID345'], (err, stores) => {  
      stores.map((result, i, store) => {  
        let key = store[i][0];  
        let val = store[i][1];  
        console.log(key, val);  
      });  
    });  
  });  
});  
  
// Console log results:  
// => UID234 {"name":"Chris","age":31,"traits":{"shoe_size":10,"hair":"brown","eyes":"blue"}}  
// => UID345 {"name":"Marge","age":26,"traits":{"shoe_size":6,"hair":"blonde","eyes":"green"}}  

```

[Edit page for next release](https://github.com/facebook/react-native-website/edit/main/docs/asyncstorage.md)[Edit page for current release](https://github.com/facebook/react-native-website/edit/main/website/versioned_docs/version-0.79/asyncstorage.md)

Last updated on **Apr 14, 2025**

* [Methods](#methods)
  + [`getItem()`](#getitem)+ [`setItem()`](#setitem)+ [`removeItem()`](#removeitem)+ [`mergeItem()`](#mergeitem)+ [`clear()`](#clear)+ [`getAllKeys()`](#getallkeys)+ [`flushGetRequests()`](#flushgetrequests)+ [`multiGet()`](#multiget)+ [`multiSet()`](#multiset)+ [`multiRemove()`](#multiremove)+ [`multiMerge()`](#multimerge)

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