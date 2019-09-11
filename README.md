1. show the python version installed\

    $ python -V\
    Python 3.6.8\
  
 2. create a working directory for your API and then setup a virtual environment.

    $ mkdir todolist && cd todolist
 
3. creates virtual enviroment named venv & activate it
  
    todolist$ virtualenv --python=python3 venv
    todolist$ . venv/bin/activate

    and your working directory sould looks like following bellow
    (venv) todolist$
  
 4. Install django & Install djangorestframework
 
    (venv) todolist$ pip install Django
    (venv) todolist$ pip install djangorestframework
    
5. go ahead and create a django project & 

    (venv) todolist$ django-admin.py startproject todos
    (venv) todolist$ cd todos
    
6. create a django app, deactivate env from main folder, creates virtual enviroment for this app & activate it
    
    (venv) todolist$ deactivate
    todolist$ django-admin.py startapp list
    todolist$ virtualenv --python=python3 venv
    todolist$ . venv/bin/activate
    
7. sync your database for the first time and create an initial user and set a password for that user

    (venv) todolist$ python manage.py migrate
    (venv) todolist$ python manage.py createsuperuser --email admin@example.com --username admin
    
8. open the todos/settings.py file and add the rest_framework and list apps to INSTALLED_APPS

    INSTALLED_APPS = [
    ...
    'rest_framework',
    'list'
    ]

9. open the todos/urls.py file and add urls for the list app

    ...
    from django.contrib import admin
    from django.urls import path, include
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('list.urls'))
    ]
