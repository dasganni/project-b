from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'character'

urlpatterns = [
    url('', views.editCharacters, name='editCharacters'),
]
