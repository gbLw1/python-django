# First DJANGO project

## What is Django?

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel.

---

## Design patterns

Django follows the MVT (Model View Template) design pattern. The MVT pattern is a software design pattern that is a collection of three important components: Models, Views, and Templates.

- **Models**: Manages the data of the application. It is the logical data structure behind the entire application and is represented by a database (generally relational databases such as MySQL, PostgreSQL, etc.).
- **Views**: Manages the process, logic, and data access of the application as python functions. It serves as an intermediary between models and templates.
- **Templates**: Determines how the user interface looks and interacts with the user (frontend). It describes how the data received from the views should be changed or formatted for display on the page.

---

## About this project

This project is a simple Django project that demonstrates the basic concepts of Django. It includes a single app with a single view that saves a user from a HTML form template into the database (SQLite).

---

## Step by step guide to create a Django project

1. Install Django

   ```bash
   pip install django
   ```

2. Create a Django project

   ```bash
   django-admin startproject <project_name>
   ```

   `project_name` is the name of the project you want to create.

3. Run the Django project

   ```bash
   python manage.py runserver
   ```

4. Create a Django app

   ```bash
   python manage.py startapp <app_name>
   ```

   `app_name` is the name of the app you want to create.

5. Update the `INSTALLED_APPS` in `settings.py`

   Make sure to add the app to the `INSTALLED_APPS` in the `settings.py` file like this:

   ```python
   INSTALLED_APPS = [
       ...
       '<app_name>',
   ]
   ```

6. Create a model

   Define the model in the `models.py` file of the app you created.

   ```python
   from django.db import models

   class ModelName(models.Model):
       field_name = models.CharField(max_length=100)
       ...
   ```

7. Create a migration

   Run the following command to create a migration for the model you created:

   ```bash
   python manage.py makemigrations
   ```

8. Apply the migration

   Run the following command to apply the migration to the database:

   ```bash
   python manage.py migrate
   ```

9. Create a view

   Define the view in the `views.py` file of the app you created.

   ```python
   from django.http import HttpResponse

   def view_name(request):
       return HttpResponse("Hello, World!")
   ```

10. Create a URL pattern

    Define the URL pattern in the `urls.py` file of the app you created.

    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        ...
        path('home', views.home),
    ]
    ```

    `path('home', views.home)` is the URL pattern that maps the view to the URL `/home`.
    `views.home` is a reference to the `home` function defined in the `views.py` file.

11. Run the server

    Run the Django server using the following command:

    ```bash
    python manage.py runserver
    ```

    Visit `http://127.0.0.1:8000/home` in your browser to see the output of the view.

12. Generate dependencies

    Run the following command to generate the dependencies of the project:

    ```bash
    pip freeze > requirements.txt
    ```

    This will create a `requirements.txt` file that contains the list of dependencies of the project.

---

## Installation guide

1. Clone the repository

   ```bash
   git clone
   ```

2. Install the dependencies

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Django project

   ```bash
   python manage.py runserver
   ```

4. Visit `http://127.0.0.1:8000/home` in your browser to see the output of the view.
