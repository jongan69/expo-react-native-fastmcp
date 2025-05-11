Publish websites - Expo Documentation

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

[Develop websites](/workflow/web)[Publish websites](/guides/publishing-websites)[DOM components](/guides/dom-components)[Progressive web apps](/guides/progressive-web-apps)[Tailwind CSS](/guides/tailwind)

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

Publish websites
================

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/publishing-websites.mdx)

Learn how to deploy Expo websites for production.

[Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/publishing-websites.mdx)

---

An Expo web app can be served locally for testing the production behavior, and deployed to a hosting service. We recommend deploying to [EAS Hosting](/eas/hosting) for the best feature support. You can also self-host or use a third-party service.

[Deploying instantly with EAS

EAS Hosting is the best way to deploy your web app with support for custom domains, SSL, and more.](/eas/hosting/get-started)
> For SDK 49 and below, you may need the [guide for publishing `webpack` builds](/archive/publishing-websites-webpack).

Output targets
--------------

The [`web.output`](/versions/latest/config/app#output) target can be configured in the [app config](/workflow/configuration) to set the export method for the web app:

app.json

Copy

```
{
  "expo": {
    "web": {
      "output": "server",
      "bundler": "metro"
    }
  }
}

```

Expo Router supports three output targets for web apps.

| Output | Expo Router | API Routes | Description |
| --- | --- | --- | --- |
| `single` (default) |  |  | Outputs a Single Page Application (SPA) with a single index.html in the output directory and has no statically indexable HTML. |
| `server` |  |  | Creates client and server directories. Client files are output as separate HTML files. API routes as separate JavaScript files for hosting with a custom Node.js server. |
| `static` |  |  | Outputs separate HTML files for every route in the app directory. |

Create a build
--------------

Creating a build of the project is the first step to publishing a web app. Whether you want to serve it locally or deploy to a hosting service, you'll need to export all JavaScript and assets of a project. This is known as a static bundle. It can be exported by running the following command:

Run the universal export command to compile the project for web:

Terminal

Copy

`-Â``npx expo export -p web`

The resulting project files are located in the dist directory. Any files inside the public directory are also copied to the dist directory.

Serve locally
-------------

Use `npx expo serve` to quickly test locally how your website will be hosted in production. Run the following command to serve the static bundle:

Terminal

Copy

`-Â``npx expo serve`

Open [`http://localhost:8081`](http://localhost:8081) to see your project in action. This is HTTP only, so permissions, camera, location, and many other secure features may not work as expected.

Hosting with EAS
----------------

When you're ready to go to production, you can instantly deploy your website with EAS CLI.

[Deploying instantly with EAS

EAS Hosting is the best way to deploy your web app with support for custom domains, SSL, and more.](/eas/hosting/get-started)

Hosting on third-party services
-------------------------------

### Netlify

[Netlify](https://www.netlify.com/) is a mostly-unopinionated platform for deploying web apps. This has the highest compatibility with Expo web apps as it makes few assumptions about the framework.

#### Manual deployment with the Netlify CDN

1

Install the Netlify CLI by running the following command:

Terminal

Copy

`-Â``npm install -g netlify-cli`

2

Configure redirects for single-page applications.

> If your app uses [static rendering](/router/reference/static-rendering), then you can skip this step.

`expo.web.output: 'single'` generates a single-page application. It means there's only one dist/index.html file to which all requests must be redirected. This can be done in Netlify by creating a ./public/\_redirects file and redirecting all requests to /index.html.

public/\_redirects

Copy

```
/*    /index.html   200

```

If you modify this file, you must rebuild your project with `npx expo export -p web` to have it safely copied into the dist directory.

3

Deploy the web build directory by running the following command:

Terminal

Copy

`-Â``netlify deploy --dir dist`

You'll see a URL that you can use to view your project online.

#### Continuous delivery

Netlify can also build and deploy when you push to git or open a new pull request:

* [Start a new Netlify project](https://app.netlify.com/signup).
* Pick your Git hosting service and select your repository.
* Click Build your site.

### Vercel

[Vercel](https://vercel.com/) has a single-command deployment flow.

1

Install the [Vercel CLI](https://vercel.com/docs/cli).

Terminal

Copy

`-Â``npm install -g vercel@latest`

2

Configure redirects for single-page applications.

Create a vercel.json file at the root of your app and add the following configuration:

vercel.json

Copy

```
{
  "buildCommand": "expo export -p web",
  "outputDirectory": "dist",
  "devCommand": "expo",
  "cleanUrls": true,
  "framework": null,
  "rewrites": [
    {
      "source": "/:path*",
      "destination": "/"
    }
  ]
}

```

If your app uses [static rendering](/router/reference/static-rendering), then you may want to add additional [dynamic route configuration](/router/reference/static-rendering#dynamic-routes).

3

Deploy the website.

Terminal

Copy

`-Â``vercel`

You'll now see a URL that you can use to view your project online. Paste that URL into your browser when the build is complete, and you'll see your deployed app.

### AWS Amplify Console

The [AWS Amplify Console](https://console.amplify.aws) provides a Git-based workflow for continuously deploying and hosting full-stack serverless web apps. Amplify deploys your PWA from a repository instead of from your computer. In this guide, we'll use a GitHub repository. Before starting, [create a new repo on GitHub](https://github.com/new).

1

Add the [amplify-explicit.yml](https://github.com/expo/amplify-demo/blob/master/amplify-explicit.yml) file to the root of your repository. Ensure you have removed the generated dist directory from the .gitignore file and committed those changes.

2

Push your local Expo project to a GitHub repository. If you haven't pushed to GitHub yet, follow [GitHub's guide to add an existing project to GitHub](https://docs.github.com/en/get-started/importing-your-projects-to-github/importing-source-code-to-github/adding-locally-hosted-code-to-github).

3

Login to the [Amplify Console](https://console.aws.amazon.com/amplify/home) and select an existing app or create a new app. Grant Amplify permission to read from your GitHub account or the organization that owns your repo.

4

Add your repo, select the branch, and select Connecting a monorepo? to enter the path to your app's dist directory and choose Next.

The Amplify Console will detect the amplify.yml file in your project. Select Allow AWS Amplify to automatically deploy all files hosted in your project root directory and choose Next.

5

Review your settings and choose Save and deploy. Your app will now be deployed to a `https://branchname.xxxxxx.amplifyapp.com` URL. You can now visit your web app, deploy another branch, or add a unified backend environment across your Expo mobile and web apps.

Follow the steps in the Learn how to get the most out of Amplify Hosting drop-down to Add a custom domain with a free SSL certificate and more information.

### Firebase hosting

[Firebase Hosting](https://console.firebase.google.com/) is production-grade web content hosting for web projects.

1

Create a firebase project with the [Firebase Console](https://console.firebase.google.com) and install the Firebase CLI by following these [instructions](https://firebase.google.com/docs/hosting).

2

Using the CLI, login to your Firebase account by running the command:

Terminal

Copy

`-Â``firebase login`

3

Then, initialize your firebase project to host by running the command:

Terminal

Copy

`-Â``firebase init`

The settings will depend on how you built your Expo website:

1. When asked about the public path, make sure to specify the dist directory.
2. When prompted Configure as a single-page app (rewrite all urls to /index.html), only select Yes if you used `web.output: "single"` (default). Otherwise, select No.

4

In the existing `scripts` property of package.json, add `predeploy` and `deploy` properties. Each has the following values:

package.json

Copy

```
"scripts": {
  %%placeholder-start%%... %%placeholder-end%%
  "predeploy": "expo export -p web",
  "deploy-hosting": "npm run predeploy && firebase deploy --only hosting",
}

```

5

To deploy, run the following command:

Terminal

Copy

`-Â``npm run deploy-hosting`

Open the URL from the console output to check your deployment, for example: `https://project-name.firebaseapp.com`.

In case you want to change the header for hosting add the following config for `hosting` section in firebase.json:

firebase.json

Copy

```
  "hosting": [
    {
      %%placeholder-start%%... %%placeholder-end%%
      "headers": [
        {
          "source": "/**",
          "headers": [
            {
              "key": "Cache-Control",
              "value": "no-cache, no-store, must-revalidate"
            }
          ]
        },
        {
          "source": "**/*.@(jpg|jpeg|gif|png|svg|webp|js|css|eot|otf|ttf|ttc|woff|woff2|font.css)",
          "headers": [
            {
              "key": "Cache-Control",
              "value": "max-age=604800"
            }
          ]
        }
      ],
    }
  ]

```

### GitHub Pages

[GitHub Pages](https://pages.github.com/) allows you to publish a website directly from a GitHub repository.

> GitHub Pages deployment uses experimental `baseUrl` functionality that may not work as intended.

1

Start by initializing a new git repository in your project and configuring it to push to a GitHub repository. If you are already syncing your changes with a GitHub repository, skip this step.

Create a repository on the GitHub website. Then, run the following commands in your project's root directory:

Terminal

`-Â``git init`

  

`-Â``git remote add origin https://github.com/username/expo-gh-pages.git`

The above commands initialize a new Git repository and configure it to push your source code to the specified GitHub repository.

2

Install the `gh-pages` package as a development dependency in your project:

npm

Yarn

Terminal

Copy

`-Â``npm install --save-dev gh-pages`

Terminal

Copy

`-Â``yarn add -D gh-pages`

3

To deploy the project, configure it to a subdomain with the [`baseUrl`](/versions/latest/config/app#baseurl) property in [app config](/workflow/configuration). Set its value to the string `/repo-name`.

For example, if the GitHub repository is `expo-gh-pages`, the following will be the value of the [experimental `baseUrl` property](/more/expo-cli#hosting-with-sub-paths):

app.json

Copy

```
{
  "expo": {
    "experiments": {
      "baseUrl": "/expo-gh-pages"
    }
  }
}

```

4

Modify the `scripts` in the package.json file by adding `predeploy` and `deploy` scripts. Each has its own value:

package.json

Copy

```
"scripts": {
 %%placeholder-start%%... %%placeholder-end%%
  "deploy": "gh-pages --nojekyll -d dist",
  "predeploy": "expo export -p web"
}

```

Since Expo uses underscores in generated files, you need to disable Jekyll with the `--nojekyll` flag.

5

To generate a production build of the web app and deploy it to GitHub Pages, run the following command:

npm

Yarn

Terminal

Copy

`-Â``npm run deploy`

Terminal

Copy

`-Â``yarn deploy`

This publishes a build of the web app to the `gh-pages` branch of your GitHub repository. This branch only contains build artifacts from the dist directory, plus the .nojekyll file generated by `gh-pages`. It does not include development source code.

6

Now that the web app is published to the `gh-pages` branch, configure GitHub Pages to serve the app from that branch.

* Navigate to the Settings tab of the GitHub repository.
* Scroll down to Pages section.
* Ensure the Source is set to Deploy from a branch.
* Under Branch section, select gh-pages and the root directory.
* Click Save.

![GitHub Pages configuration in repository settings](/static/images/distribution/publishing-websites-github-pages-config.png)

7

Once the web app is published and the GitHub Pages configuration is set, a GitHub action will deploy your website. You can monitor its progress by navigating to your repository's Actions tab. Upon completion, your web app will be available at the URL `http://username-on-github.github.io/repo-name`.

For subsequent deployments and updates, run the `deploy` command and the GitHub action will start automatically to update your web app.

[Previous (Development process - Web)

Develop websites](/workflow/web)[Next (Development process - Web)

DOM components](/guides/dom-components)

Was this doc helpful?

* Share your feedback
* [Ask a question on the forums](https://chat.expo.dev/)
* [Edit this page](https://github.com/expo/expo/edit/main/docs/pages/guides/publishing-websites.mdx)
* Last updated on May 01, 2025

Sign up for the Expo Newsletter

Sign Up

Unsubscribe at any time. Read our [privacy policy](https://expo.dev/privacy).

On this page

[Output targets](/guides/publishing-websites/#output-targets)[Create a build](/guides/publishing-websites/#create-a-build)[Serve locally](/guides/publishing-websites/#serve-locally)[Hosting with EAS](/guides/publishing-websites/#hosting-with-eas)[Hosting on third-party services](/guides/publishing-websites/#hosting-on-third-party-services)[Netlify](/guides/publishing-websites/#netlify)[Vercel](/guides/publishing-websites/#vercel)[AWS Amplify Console](/guides/publishing-websites/#aws-amplify-console)[Firebase hosting](/guides/publishing-websites/#firebase-hosting)[GitHub Pages](/guides/publishing-websites/#github-pages)