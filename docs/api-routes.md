API Routes - Expo Documentation

[Docs](/)

[Blog](https://expo.dev/blog)[Changelog](https://expo.dev/changelog)[Star Us on GitHub](https://github.com/expo/expo)

Search

[Home](/)[Guides](/guides/overview)[EAS](/eas)[Reference](/versions/latest)[Learn](/tutorial/overview)

[Overview](/guides/overview)

Development process

[Develop an app with Expo](/workflow/overview)[Configure with app config](/workflow/configuration)[Continuous Native Generation](/workflow/continuous-native-generation)[Using libraries](/workflow/using-libraries)[Privacy manifests](/guides/apple-privacy)[Permissions](/guides/permissions)[Environment variables](/guides/environment-variables)

Linking

Write native code

Compile locally

Web

Bundling

Existing React Native apps

Existing native apps

Reference

Expo Router

[Introduction](/router/introduction)[Installation](/router/installation)

Router 101

Navigation patterns

Advanced

Reference

[Error handling](/router/error-handling)[URL parameters](/router/reference/url-parameters)[Redirects](/router/reference/redirects)[Static Rendering](/router/reference/static-rendering)[Async routes](/router/reference/async-routes)[API Routes](/router/reference/api-routes)[Sitemap](/router/reference/sitemap)[Typed routes](/router/reference/typed-routes)[Screen tracking for analytics](/router/reference/screen-tracking)[Top-level src directory](/router/reference/src-directory)[Testing](/router/reference/testing)[Troubleshooting](/router/reference/troubleshooting)

Migration

Expo Modules API

[Overview](/modules/overview)[Get started](/modules/get-started)

Tutorials

Reference

Push notifications

[Overview](/push-notifications/overview)[About notification types](/push-notifications/what-you-need-to-know)[Expo push notifications setup](/push-notifications/push-notifications-setup)[Send notifications with the Expo Push Service](/push-notifications/sending-notifications)[Handle incoming notifications](/push-notifications/receiving-notifications)

Reference

More

[Upgrade Expo SDK](/workflow/upgrading-expo-sdk-walkthrough)

Assorted

Integrations

Troubleshooting

Regulatory compliance

[Data and Privacy protection](/regulatory-compliance/data-and-privacy-protection)[GDPR compliance](/regulatory-compliance/gdpr)[HIPAA compliance](/regulatory-compliance/hipaa)[Privacy Shield](/regulatory-compliance/privacy-shield)

[Archive](/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

API Routes
==========

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/reference/api-routes.mdx)

Learn how to create server endpoints with Expo Router.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/reference/api-routes.mdx)

---

Expo Router enables you to write secure server code for all platforms, right in your app directory.

app/hello+api.ts

Copy

```
export function GET(request: Request) {
  return Response.json({ hello: 'world' });
}

```

Server features require a custom server, which can be deployed to EAS or most [other hosting providers](/router/reference/api-routes#deployment).

[![Watch: Expo Router API Routes Handle Requests & Stream Data](https://i3.ytimg.com/vi/2_UzR1wdimI/maxresdefault.jpg)

Watch: Expo Router API Routes Handle Requests & Stream Data](https://www.youtube.com/watch?v=2_UzR1wdimI)

What are API Routes
-------------------

API Routes are functions that are executed on a server when a route is matched. They can be used to handle sensitive data, such as API keys securely, or implement custom server logic, such as exchanging auth codes for access tokens. API Routes should be executed in a [WinterCG](https://wintercg.org/)-compliant environment.

In Expo, API Routes are defined by creating files in the app directory with the `+api.ts` extension. For example, the following API route is executed when the route `/hello` is matched.

`app`

â`index.tsx`

â`hello+api.ts``API Route`

Create an API route
-------------------

1

Ensure your project is using server output, this will configure the export and production builds to generate a server bundle as well as the client bundle.

app.json

Copy

```
{
  "web": {
    "output": "server"
  }
}

```

2

An API route is created in the app directory. For example, add the following route handler. It is executed when the route `/hello` is matched.

app/hello+api.ts

Copy

```
export function GET(request: Request) {
  return Response.json({ hello: 'world' });
}

```

You can export any of the following functions `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, and `OPTIONS` from a server route. The function executes when the corresponding HTTP method is matched. Unsupported methods will automatically return `405: Method not allowed`.

3

Start the development server with Expo CLI:

Terminal

Copy

`-Â``npx expo`

4

You can make a network request to the route to access the data. Run the following command to test the route:

Terminal

Copy

`-Â``curl http://localhost:8081/hello`

You can also make a request from the client code:

app/index.tsx

Copy

```
import { Button } from 'react-native';

async function fetchHello() {
  const response = await fetch('/hello');
  const data = await response.json();
  alert('Hello ' + data.hello);
}

export default function App() {
  return <Button onPress={() => fetchHello()} title="Fetch hello" />;
}

```

Relative fetch requests automatically fetch relative to the dev server origin in development, and can be configured in production using the `origin` field in the app.json:

app.json

Copy

```
{
  "plugins": [
    [
      "expo-router",
      {
        "origin": "https://evanbacon.dev/"
      }
    ]
  ]
}

```

This URL can be automatically configured during EAS Builds by setting the `EXPO_UNSTABLE_DEPLOY_SERVER=1` environment variable. This will trigger a versioned server deployment which sets the origin to a preview deploy URL automatically.

5

Deploy the website and server to a [hosting provider](/router/reference/api-routes#deployment) to access the routes in production on both native and web.

> API route filenames cannot have platform-specific extensions. For example, hello+api.web.ts will not work.

Requests
--------

Requests use the global, standard [`Request`](https://fetch.spec.whatwg.org/#request) object.

app/blog/[post]+api.ts

Copy

```
export async function GET(request: Request, { post }: Record<string, string>) {
  // const postId = new URL(request.url).searchParams.get('post')
  // fetch data for 'post'
  return Response.json({ ... });
}

```

### Request body

Use the `request.json()` function to access the request body. It automatically parses the body and returns the result.

app/validate+api.ts

Copy

```
export async function POST(request: Request) {
  const body = await request.json();

  return Response.json({ ... });
}

```

### Request query parameters

Query parameters can be accessed by parsing the request URL:

app/endpoint+api.ts

Copy

```
export async function GET(request: Request) {
  const url = new URL(request.url);
  const post = url.searchParams.get('post');

  // fetch data for 'post'
  return Response.json({ ... });
}

```

Response
--------

Responses use the global, standard [`Response`](https://fetch.spec.whatwg.org/#response) object.

app/demo+api.ts

Copy

```
export function GET() {
  return Response.json({ hello: 'universe' });
}

```

Errors
------

You can respond to server errors by using the `Response` object.

app/blog/[post].ts

Copy

```
import { Request, Response } from 'expo-router/server';

export async function GET(request: Request, { post }: Record<string, string>) {
  if (!post) {
    return new Response('No post found', {
      status: 404,
      headers: {
        'Content-Type': 'text/plain',
      },
    });
  }
  // fetch data for `post`
  return Response.json({ ... });
}

```

Making requests with an undefined method will automatically return `405: Method not allowed`. If an error is thrown during the request, it will automatically return `500: Internal server error`.

Bundling
--------

API Routes are bundled with Expo CLI and [Metro bundler](/guides/customizing-metro). They have access to all of the language features as your client code:

* [TypeScript](/guides/typescript) â types and [tsconfig.json paths](/guides/typescript#path-aliases-optional).
* [Environment variables](/guides/environment-variables) â server routes have access to all environment variables, not just the ones prefixed with `EXPO_PUBLIC_`.
* Node.js standard library â ensure that you are using the correct version of Node.js locally for your server environment.
* babel.config.js and metro.config.js support â settings work across both client and server code.

Security
--------

Route handlers are executed in a sandboxed environment that is isolated from the client code. It means you can safely store sensitive data in the route handlers without exposing it to the client.

* Client code that imports code with a secret is included in the client bundle. It applies to all files in the app directory even though they are not a route handler file (such as suffixed with +api.ts).
* If the secret is in a <...>+api.ts file, it is not included in the client bundle. It applies to all files that are imported in the route handler.
* The secret stripping takes place in `expo/metro-config` and requires it to be used in the metro.config.js.

Deployment
----------

When you're ready to deploy to production, run [`npx expo export --platform web`](/more/expo-cli#exporting) to create the server bundle in the dist directory. This server can be tested locally with `npx expo serve` (available in Expo SDK 52 and higher), visit the URL in a web browser or create a native build with the `origin` set to the local server URL.
You can deploy the server for production using [EAS Hosting](/eas/hosting/get-started) or another third-party service.

[Deploy instantly with EAS

EAS Hosting is the best way to deploy your Expo API routes and servers.](/eas/hosting/get-started)

### Native deployment

> This is an experimental feature starting in SDK 52 and above. The process will be more automated and have better support in future versions.

Server features (API routes, and React Server Components) in Expo Router are centered around native implementations of `window.location` and `fetch` which point to the remote server. In development, we automatically point to the dev server running with `npx expo start`, but for production native builds to work you'll need to deploy the server to a secure host and set the `origin` property of the Expo Router Config Plugin.

When configured, features like relative fetch requests `fetch('/my-endpoint')` will automatically point to the server origin.

This deployment process can experimentally be automated to ensure correct versioning during native builds with the `EXPO_UNSTABLE_DEPLOY_SERVER=1` environment variable.

Here's how to configure your native app to automatically deploy and link a versioned production server on build:

1

Ensure the `origin` field is NOT set in the app.json or in the `expo.extra.router.origin` field. Also, ensure you aren't using app.config.js as this is not supported with automatically linked deployments yet.

2

Setup [EAS Hosting](/eas/hosting/get-started) for the project by deploying once locally first.

Terminal

`-Â``npx expo export -p web`

`-Â``eas deploy`

3

Set the `EXPO_UNSTABLE_DEPLOY_SERVER` environment variable in your `.env` file. This will be used to enable the experimental server deployment functionality during EAS Build.

.env

Copy

```
EXPO_UNSTABLE_DEPLOY_SERVER=1

```

4

You're now ready to use automatic server deployment! Run the build command to start the process.

Terminal

Copy

`-Â``eas build`

You can also run this locally with:

Terminal

`# Android`

`-Â``npx expo run:android --variant release`

  
`# iOS`

`-Â``npx expo run:ios --configuration Release`

Notes about automatic server deployment for native apps:

* Server failures may occur during the `Bundle JavaScript` phase of EAS Build if something was not setup correctly.
* You can manually deploy the server and set the `origin` URL before building the app if you'd like.
* Automatic deployment can be force skipped with the environment variable `EXPO_NO_DEPLOY=1`.
* Automatic deployment does not support [dynamic app config](/workflow/configuration#dynamic-configuration) (app.config.js and app.config.ts) files yet.
* Logs from the deployment will be written to `.expo/logs/deploy.log`.
* Deployment will not run in `EXPO_OFFLINE` mode.

### Testing the native production app locally

It can often be useful to test the production build against a local dev server to ensure everything is working as expected. This can speed up the debugging process substantially.

1

Export the production server:

Terminal

Copy

`-Â``npx expo export`

2

Host the production server locally:

Terminal

Copy

`-Â``npx expo serve`

3

Set the origin in the app.json's `origin` field. Ensure no generated value is in `expo.extra.router.origin`. This should be `http://localhost:8081` (assuming `npx expo serve` is running on the default port).

app.json

Copy

```
{
  "expo": {
    "plugins": [
      [
        "expo-router",
        {
          "origin": "http://localhost:8081"
        }
      ]
    ]
  }
}

```

Remember to remove this `origin` value when deploying to production.

4

Build the app in release mode on to a simulator:

Terminal

Copy

`-Â``EXPO_NO_DEPLOY=1 npx expo run:ios --configuration Release`

You should now see requests coming in to the local server. Use a tool like [Proxyman](https://proxyman.com/) to inspect network traffic for the simulator and gain better insight.

You can experimentally change the URL and quickly rebuild for iOS using the `--unstable-rebundle` flag. This will swap out the app.json and client assets for new ones, skipping the native rebuild.

For example, you can run `eas deploy` to get a new deployment URL, add it to the app.json, then run `npx expo run:ios --unstable-rebundle --configuration Release` to quickly rebuild the app with the new URL.

You will want to make a clean build before sending to the store to ensure no transient issues are present.

Hosting on third-party services
-------------------------------

> This is experimental and subject to breaking changes. We have no continuous tests against this configuration.

Every cloud hosting provider needs a custom adapter to support the Expo server runtime. The following third-party providers have unofficial or experimental support from the Expo team.

Before deploying to these providers, it may be good to be familiar with the basics of [`npx expo export`](/more/expo-cli#exporting) command:

* dist is the default export directory for Expo CLI.
* Files in public directory are copied to dist on export.
* The `@expo/server` package is included with `expo` and delegates requests to the server routes.
* `@expo/server` does not inflate environment variables from .env files. They are expected to load either by the hosting provider or the user.
* Metro is not included in the server.

### Express

1

Install the required dependencies:

Terminal

Copy

`-Â``npm i -D express compression morgan`

2

Export the website for production:

Terminal

Copy

`-Â``npx expo export -p web`

3

Write a server entry file that serves the static files and delegates requests to the server routes:

server.ts

Copy

```
#!/usr/bin/env node

const path = require('path');
const { createRequestHandler } = require('@expo/server/adapter/express');

const express = require('express');
const compression = require('compression');
const morgan = require('morgan');

const CLIENT_BUILD_DIR = path.join(process.cwd(), 'dist/client');
const SERVER_BUILD_DIR = path.join(process.cwd(), 'dist/server');

const app = express();

app.use(compression());

// http://expressjs.com/en/advanced/best-practice-security.html#at-a-minimum-disable-x-powered-by-header
app.disable('x-powered-by');

process.env.NODE_ENV = 'production';

app.use(
  express.static(CLIENT_BUILD_DIR, {
    maxAge: '1h',
    extensions: ['html'],
  })
);

app.use(morgan('tiny'));

app.all(
  '*',
  createRequestHandler({
    build: SERVER_BUILD_DIR,
  })
);
const port = process.env.PORT || 3000;

app.listen(port, () => {
  console.log(`Express server listening on port ${port}`);
});

```

4

Start the server with `node` command:

Terminal

Copy

`-Â``node server.ts`

### Netlify

> This is experimental and subject to breaking changes. We have no continuous tests against this configuration.

1

Create a server entry file. All requests will be delegated through this middleware. The exact file location is important.

netlify/functions/server.ts

Copy

```
const { createRequestHandler } = require('@expo/server/adapter/netlify');

const handler = createRequestHandler({
  build: require('path').join(__dirname, '../../dist/server'),
});

module.exports = { handler };

```

2

Create a Netlify configuration file at the root of your project to redirect all requests to the server function.

netlify.toml

Copy

```
[build]
  command = "expo export -p web"
  functions = "netlify/functions"
  publish = "dist/client"

[[redirects]]
  from = "/*"
  to = "/.netlify/functions/server"
  status = 404

[functions]
  # Include everything to ensure dynamic routes can be used.
  included_files = ["dist/server/**/*"]

[[headers]]
  for = "/dist/server/_expo/functions/*"
  [headers.values]
    # Set to 60 seconds as an example.
    "Cache-Control" = "public, max-age=60, s-maxage=60"

```

3

After you have created the configuration files, you can build the website and functions with Expo CLI:

Terminal

Copy

`-Â``npx expo export -p web`

4

Deploy to Netlify with the [Netlify CLI](https://docs.netlify.com/cli/get-started/).

Terminal

`# Install the Netlify CLI globally if needed.`

`-Â``npm install netlify-cli -g`

`# Deploy the website.`

`-Â``netlify deploy`

You can now visit your website at the URL provided by Netlify CLI. Running `netlify deploy --prod` will publish to the production URL.

5

If you're using any environment variables or .env files, add them to Netlify. You can do this by going to the Site settings and adding them to the Build & deploy section.

### Vercel

> This is experimental and subject to breaking changes. We have no continuous tests against this configuration.

1

Create a server entry file. All requests will be delegated through this middleware. The exact file location is important.

api/index.ts

Copy

```
const { createRequestHandler } = require('@expo/server/adapter/vercel');

module.exports = createRequestHandler({
  build: require('path').join(__dirname, '../dist/server'),
});

```

2

Create a Vercel configuration file (vercel.json) at the root of your project to redirect all requests to the server function.

vercel.json v3

vercel.json v2

vercel.json

Copy

```
{
  "buildCommand": "expo export -p web",
  "outputDirectory": "dist/client",
  "functions": {
    "api/index.ts": {
      "runtime": "@vercel/node@5.1.8",
      "includeFiles": "dist/server/**"
    }
  },
  "rewrites": [
    {
      "source": "/(.*)",
      "destination": "/api/index"
    }
  ]
}

```

The newer version of the vercel.json does not use `routes` and `builds` configuration options anymore, and serves your public assets from the dist/client output directory automatically.

vercel.json

Copy

```
{
  "version": 2,
  "outputDirectory": "dist",
  "builds": [
    {
      "src": "package.json",
      "use": "@vercel/static-build",
      "config": {
        "distDir": "dist/client"
      }
    },
    {
      "src": "api/index.ts",
      "use": "@vercel/node",
      "config": {
        "includeFiles": ["dist/server/**"]
      }
    }
  ],
  "routes": [
    {
      "handle": "filesystem"
    },
    {
      "src": "/(.*)",
      "dest": "/api/index.ts"
    }
  ]
}

```

The legacy version of the vercel.json needs a `@vercel/static-build` runtime to serve your assets from the dist/client output directory.

3

> Note: This step only applies to users of the legacy version of the vercel.json. If you're using v3, you can skip this step.

After you have created the configuration files, add a `vercel-build` script to your package.json file and set it to `expo export -p web`.

4

Deploy to Vercel with the [Vercel CLI](https://vercel.com/docs/cli).

Terminal

`# Install the Vercel CLI globally if needed.`

`-Â``npm install vercel -g`

`# Build the website.`

`-Â``vercel build`

`# Deploy the website.`

`-Â``vercel deploy --prebuilt`

You can now visit your website at the URL provided by the Vercel CLI.

Known limitations
-----------------

Several known features are not currently supported in the API Routes beta release.

### No dynamic imports

API Routes currently work by bundling all code (minus the Node.js built-ins) into a single file. This means that you cannot use any external dependencies that are not bundled with the server. For example, a library such as `sharp`, which includes multiple platform binaries, cannot be used. This will be addressed in a future version.

### ESM not supported

The current bundling implementation opts to be more unified than flexible. This means the limitation of native not supporting ESM is carried over to API Routes. All code will be transpiled down to Common JS (`require`/`module.exports`). However, we recommend you write API Routes using ESM regardless. This will be addressed in a future version.

[Previous (Expo Router - Reference)

Async routes](/router/reference/async-routes)[Next (Expo Router - Reference)

Sitemap](/router/reference/sitemap)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/router/reference/api-routes.mdx)
* Last updated on February 24, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[What are API Routes](/router/reference/api-routes/#what-are-api-routes)[Create an API route](/router/reference/api-routes/#create-an-api-route)[Requests](/router/reference/api-routes/#requests)[Request body](/router/reference/api-routes/#request-body)[Request query parameters](/router/reference/api-routes/#request-query-parameters)[Response](/router/reference/api-routes/#response)[Errors](/router/reference/api-routes/#errors)[Bundling](/router/reference/api-routes/#bundling)[Security](/router/reference/api-routes/#security)[Deployment](/router/reference/api-routes/#deployment)[Native deployment](/router/reference/api-routes/#native-deployment)[Testing the native production app locally](/router/reference/api-routes/#testing-the-native-production-app-locally)[Hosting on third-party services](/router/reference/api-routes/#hosting-on-third-party-services)[Express](/router/reference/api-routes/#express)[Netlify](/router/reference/api-routes/#netlify)[Vercel](/router/reference/api-routes/#vercel)[Known limitations](/router/reference/api-routes/#known-limitations)[No dynamic imports](/router/reference/api-routes/#no-dynamic-imports)[ESM not supported](/router/reference/api-routes/#esm-not-supported)