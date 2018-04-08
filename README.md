# djangoProject
This is a test Django project for learning.

This project uses Python 3.4.8.

pyenv is used to manage the python version.

```bash
pyenv install 3.4.8
pyenv local 3.4.8
```

In addition, pipenv is used to manage the python dependencies.

```bash
pipenv install django
pipenv shell
```

Start the django server using
```bash
python manage.py runserver
```

Building a new app in the project.

```bash
python manage.py startapp {app}
```

Take a look at the /admin settings. Django ships with the several apps, all of which are defined in settings.py/INSTALLED_APPS.
To setup the database for these apps:
```bash
python manage.py migrate
```

After building the app models, setup the database with
```bash
python manage.py makemigrations {app}
python manage.py migrate
```

This project maintains unit tests using pytest and pytest-django. Run tests using the make rule:
```bash
make test
```