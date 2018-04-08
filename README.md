# djangoProject
This is a test Django project for learning.

This project uses Python 3.4.8. pyenv is used to manage the python version for this project.

```bash
pyenv install 3.4.8
pyenv local 3.4.8
```

In addition, pipenv is used to manage the python dependencies.

```bash
pipenv install django
pipenv shell
django-admin startproject mysite
python manage.py runserver
```

Building the polls app.

```python
python manage.py startapp polls
```
