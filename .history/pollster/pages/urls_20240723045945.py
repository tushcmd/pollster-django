
from django.urls import path

from . import views  # import views from current directory

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
]