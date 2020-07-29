from django.urls import path

from . import views

app_name = "servererrors"

urlpatterns = [
    path("internalServerError/", views.internalServerErrorView.as_view(), name="internalServerError"),
] 
