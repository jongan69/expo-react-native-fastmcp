Default responses and headers - Expo Documentation

[Docs](/)

[Blog](https://expo.dev/blog)[Changelog](https://expo.dev/changelog)[Star Us on GitHub](https://github.com/expo/expo)

Search

[Home](/)[Guides](/guides/overview)[EAS](/eas)[Reference](/versions/latest)[Learn](/tutorial/overview)

[Introduction](/eas)[Configuration with eas.json](/eas/json)[Environment variables](/eas/environment-variables)

EAS Workflows

[Get started](/eas/workflows/get-started)[Example CI/CD workflows](/eas/workflows/examples)[Syntax for EAS Workflows](/eas/workflows/syntax)[Automating EAS CLI commands](/eas/workflows/automating-eas-cli)

Reference

EAS Build

[Introduction](/build/introduction)[Create your first build](/build/setup)[Configure with eas.json](/build/eas-json)[Internal distribution](/build/internal-distribution)[Automate submissions](/build/automate-submissions)[Using EAS Update](/build/updates)[Trigger builds from CI](/build/building-on-ci)[Trigger builds from GitHub App](/build/building-from-github)[Expo Orbit](/build/orbit)

App signing

Custom builds

Reference

EAS Hosting

[Introduction](/eas/hosting/introduction)[Get started](/eas/hosting/get-started)[Deployments and aliases](/eas/hosting/deployments-and-aliases)[Environment variables](/eas/hosting/environment-variables)[Custom domain](/eas/hosting/custom-domain)[Monitoring API routes](/eas/hosting/api-routes)[Workflows](/eas/hosting/workflows)

Reference

[Caching](/eas/hosting/reference/caching)[Responses and headers](/eas/hosting/reference/responses-and-headers)[Worker runtime](/eas/hosting/reference/worker-runtime)

EAS Submit

[Introduction](/submit/introduction)[Submit to the Google Play Store](/submit/android)[Submit to the Apple App Store](/submit/ios)[Configure with eas.json](/submit/eas-json)

EAS Update

[Introduction](/eas-update/introduction)[Get started](/eas-update/getting-started)

Preview

Deployment

Concepts

Troubleshooting

Reference

EAS Metadata

[Introduction](/eas/metadata)[Get started](/eas/metadata/getting-started)

Reference

EAS Insights

[Introduction](/eas-insights/introduction)

Distribution

[Overview](/distribution/introduction)[App stores best practices](/distribution/app-stores)[App transfers](/distribution/app-transfers)[Understanding app size](/distribution/app-size)

Reference

[Webhooks](/eas/webhooks)

Expo accounts

Billing

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

Default responses and headers
=============================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas/hosting/reference/responses-and-headers.mdx)

Defaults that are added automatically on requests when using EAS Hosting.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas/hosting/reference/responses-and-headers.mdx)

---

EAS Hosting applies several defaults to your deployment that are supposed to help you and reduce the amount of code you have to add yourself for simple API routes.

Asset responses
---------------

An asset response contains additional metadata headers for browsers, mostly for caching.

A default `ETag` header is added to all asset responses to allow browsers to re-validate their caches using `if-none-match` request headers.

CORS responses
--------------

By default, if an API route does not handle `OPTIONS` requests, EAS Hosting will automatically respond with a default CORS response.

This default is very permissible and generally allows all browsers to make requests to the API route. If you don't want this, handle `OPTIONS` requests in API routes yourself.

The following headers will be sent by default:

```
Access-Control-Allow-Origin: <origin || '*'>
Access-Control-Allow-Headers: <access-control-request-headers || '*'>
Access-Control-Allow-Methods: GET, POST, PUT, PATCH, DELETE
Access-Control-Allow-Credentials: true
Access-Control-Expose-Headers: *
Access-Control-Max-Age: 3600
Vary: Origin, Access-Control-Request-Headers

```

These headers will allow any client to make a request from any origin, with any headers, with credentials, and cache the `OPTIONS` response for 3600 seconds.

More information on [preflight `OPTIONS` requests can be found in the MDN documentation](https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request).

Strict-Transport-Security header
--------------------------------

This header tells browsers to only access a URL with the HTTPS protocol in the future. EAS Hosting automatically adds this header if it's missing.

Its default value is set to `max-age=31536000; includeSubDomains; preload`.

For more information on why this header is a good default, improves security, and performance, [read this article on `web.dev`](https://web.dev/blog/bbc-hsts) and read more about [Strict-Transport-Security](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security) header in the MDN documentation.

Common version headers
----------------------

By default, EAS Hosting will remove and not forward any `X-Powered-By` and `X-Aspnet-Version` headers. With API routes, this header does not serve much of a purpose and we don't recommend you add alternative headers like `X-Powered-By` to your API routes as it unnecessarily exposes internal information on the code you're running.

Frame Content-Security Policy (CSP)
-----------------------------------

By default, browsers allow any webpage to render in an iframe. Unfortunately, this allows phishing attacks such as clickjacking which is used by malicious actors to overlay a page with their own controls and inputs, to steal credentials or coerce users to perform certain actions.

To prevent this, EAS Hosting adds a `frame-ancestors 'self'` directive by default, telling browsers to not embed EAS Hosting in iframes on other domains that you don't control.

This is equivalent to setting the (older) `X-Frame-Options` header to `SAMEORIGIN`.This default directive is only applied to responses with `text/html` content types, so it will only be applied to HTML pages.

If your API routes respond with custom `X-Frame-Options` headers, these headers will automatically be converted to `Content-Security-Policy` directives in your response.

Crash pages
-----------

If your API route throws an unhandled JavaScript error, this is treated as a "crash" since your API route was unable to deliver an error.

EAS Hosting will respond with an error page in these cases. The error page will be rendered as an HTML response, if the `Accept: text/html` request header was sent. Otherwise, it will only respond with a plaintext response.

Request headers
---------------

EAS Hosting will add a couple of headers to every request, before it's forwarded to your API routes. These headers generally add more information about who made the request.

### IP headers

The request contains several headers to identify the IP address of the user's device that made the request:

* `Forwarded` is a standard header that delivers a comma-separated list of forwarder IPs for the given request. See MDN documentation on [HTTP `Forwarded` header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Forwarded) for more information.
* `X-Forwarded-For` is a de-facto standard header that is set to a comma-separated list of the forwarder IPs for a given request without any added information.
* `X-Forwarded-For` contains a list of protocols used to forward the request, typically it's set to `https`
* `X-Real-IP` contains only the original request's IP address

For example, to retrieve the IP address of the user's browser that is calling your API route, read the `X-Real-IP` header from the request:

```
export async function GET(request) {
  const ip = request.headers.get('X-Real-IP');
}

```

### Geo headers

The request also contains several headers containing geographical information about where the request came from:

* `eas-colo` contains the Cloudflare code for the data center that handled your request. For example, `lhr`.
* `eas-ip-continent` contains the continent code of the current request:
  + `AF` for Africa
  + `AN` for Antarctica
  + `AS` for Asia
  + `EU` for Europe
  + `NA` for North America
  + `OC` for Oceania
  + `SA` for South America.
* `eas-ip-country` contains the ISO-3166 Alpha 2 country code. This is at most two letters long. For example, `US` or `JP`.
* `eas-ip-region` contains the ISO-3166-2 region code for the request. This value is a maximum of three characters long. However, it can vary based on how region codes in a specific country work for the requested origin.. It could comprise one to three digits, one to three letters, or any other combination.
* `eas-ip-city` may contain a human-readable name of a city. For example `London` or `Chicago`.
* `eas-ip-latitude` and `eas-ip-longitude` contain an approximate latitude and longitude for the request.
* `eas-ip-timezone` contains a best guess of the timezone the request originated in. For example, `Europe/London`
* `eas-ip-eu` is set to `1` when the request likely originated in the jurisdictional area of the European Union.

[Previous (EAS Hosting - Reference)

Caching](/eas/hosting/reference/caching)[Next (EAS Hosting - Reference)

Worker runtime](/eas/hosting/reference/worker-runtime)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/eas/hosting/reference/responses-and-headers.mdx)
* Last updated on April 29, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Asset responses](/eas/hosting/reference/responses-and-headers/#asset-responses)[CORS responses](/eas/hosting/reference/responses-and-headers/#cors-responses)[Strict-Transport-Security header](/eas/hosting/reference/responses-and-headers/#strict-transport-security-header)[Common version headers](/eas/hosting/reference/responses-and-headers/#common-version-headers)[Frame Content-Security Policy (CSP)](/eas/hosting/reference/responses-and-headers/#frame-content-security-policy-csp)[Crash pages](/eas/hosting/reference/responses-and-headers/#crash-pages)[Request headers](/eas/hosting/reference/responses-and-headers/#request-headers)[IP headers](/eas/hosting/reference/responses-and-headers/#ip-headers)[Geo headers](/eas/hosting/reference/responses-and-headers/#geo-headers)