from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'settings'

urlpatterns = [
    url('', views.settingsView.as_view(), name='settings'),
]
