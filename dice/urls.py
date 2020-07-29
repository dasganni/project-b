from django.urls import path
from . import views
from django.conf.urls import url


app_name = 'dice'


urlpatterns = [
    path('', views.dice, name='dice'),
]
