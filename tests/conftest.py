import os
import django
from django.conf import settings


# `pytest` automatically calls this function once when tests are run.
def pytest_configure():
    settings.DEBUG = True
    django.setup()
