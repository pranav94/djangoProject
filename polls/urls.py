"""
To call the view, we need to map it to a URL - and for this we need a URLconf.

To create a URLconf in the polls directory, create a file called urls.py
"""
from django.urls import path

from . import views


app_name = 'polls'
urlpatterns = [
    # ex: /polls
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail')
]