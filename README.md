# Django + Svelte Template

This repository is a simple configuration of a Django project combined with a Svelte project that allows for easy integration between the Svelte frontend and Django backend, while maintaining the normal workflow for both frameworks as much as possible.

This repository is based on the basic Django project structure that is created by running the `django-admin startproject django_server` command (if you are unfamiliar with Django please have a look at the Django website first: https://www.djangoproject.com/ and follow their excellent tutorial). Next to this, it is based on the Svelte project template as found here: https://github.com/sveltejs/template. If you are unfamiliar with Svelte, please also first have a look at their website: https://svelte.dev/ and follow their equally excellent tutorial.

Please note that I have adapted both the basic Django project structure and the Svelte template in order to provide a template that connects them together. These changes are entirely my own and are not supported by the developers of Django, Svelte, and the Svelte template I linked to in the previous section or by anybody else.

# Quickstart

Note: before you get started, you need to have Node.js and Python installed on your computer.

## Start the Svelte frontend

- Clone or download the repository, or create your own Git repository by using this own as a template.
- `cd` into the `svelte_frontend` directory: `cd svelte_frontend/`
- Install the required NPM packages: `npm install`
- Run the frontend in development mode: `npm run dev`

## Start the Django backend

- Open a new terminal in the main directory of the repository
- It is recommended to create a new virtual environment before installing the
Python dependencies, e.g. using Anaconda.
- Install the Python dependencies (Django is the only required dependency): `pip install Django`
- Start the Django development server: `python manage.py runserver`

# How does it work?

Svelte compiles your frontend code and bundles all the components that you create into a single `.js` and a single `.css` file. This makes it easy to load these files from an HTML template that can be served by Django. This template can be found in `svelte_frontend/template/svelte_template.html`. This HTML file uses the Django template language to insert a few variables like the title of the page and the path to the `.js` and `.css` file it needs to use.

Because the `.js` and `.css` files the template uses are variables, this templates can be reused for different pages. In `hello_world/views.py` you can see an example of how this could work. You can create multiple Django apps, with multiple pages each, and they can each include different bundled Svelte applications.

The next question is how to create these different Svelte applications. The standard Svelte template is configured to create just one single application, so some changes were made to this configuration. First of all, the Svelte project structure: in `svelte_frontend/src/` you will find a directory called `apps/`. It is suggested to create a subdirectory in `apps/` for each new Django app that you define. Then, inside this subdirectory you can define different `.js` files for each page that you make in this app. Note that pages can reuse Svelte components, so even though you have to define a separate `.js` file for each page, you don't need to rewrite code if you define the content of your application in `.Svelte` component files. Javascript modules can also be shared between apps and pages. It is suggested to use the `svelte_frontend/src/shared/` directory for sharing code between apps.

The other change that was made with respect to the original Svelte template is in the `svelte_frontend/rollup.config.js` file. This file had to adapted to build multiple Svelte applications (one for each page). This also means that when you add a new page to your project you have to add an entry in the rollup configuration. This is very easy, you can have a look at the `svelte_frontend/rollup.config.js` file, and at the bottom of the file you can see how the current pages for the `hello_world` application are defined. And let's say that you created a new Django app using `python manage.py startapp todo` and that you defined a page `home`, all you need to do is create a `home.js` file in `svelte_frontend/src/apps/` and create your Svelte app there, and add the following line to `svelte_frontend/rollup.config.js` right before the `export ...` line at the end of the file:

```
appsConfig.push(getAppConfig('todo', 'home'));
```

Then in order to render your frontend page using Django, add the following view to your `views.py` file in the `todo` app directory:

```
def home(request):
    context = {
        'svelte_js': 'build/todo/home.js', 
        'svelte_css': 'build/todo/home.css', 
        'title': 'Todo | Home'
    }
    return render(request, 'svelte_template.html', context=context)
```

Now build the frontend by running either `npm run dev` (this will enable hot-reloading) or `npm run build` (which optimizes the code for production) in the `svelte_frontend/` directory. Then start your Django project by running `python manage.py runserver` in the main repository directory, and you should see your page! Of course you can add any code you want to the view function in the Django app to customize the behaviour of your website.

# Repository Structure

What follows is a short description of the repository structure, to make it easier to understand the template and adapt it to your needs.

- `django_server/`: The main Django project folder, as created by `django-admin startproject django_server` (this is the inner directory with that name). This directory contains the settings of your Django project, URL configuration etc..
- `hello_world/`: A Django app as created by `python manage.py startapp hello_world`. This is a simple Django app that is included here just so you can quickly start the project and see how a Django app can be organized to use a Svelte frontend.
- `svelte_frontend/`: This directory contains all the frontend code related to Svelte. Its content is based on the official Svelte template: https://github.com/sveltejs/template.
- `manage.py`: Created by Django by running `django-admin startproject django_server` and is used to manage the Django project.
