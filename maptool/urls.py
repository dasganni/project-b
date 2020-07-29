from django.urls import path

from . import views

app_name = "maptool"

urlpatterns = [
    path("", views.mapView.as_view(), name="map"),
    path("delete/<int:map_id>", views.mapView.as_view(), name="map"),

] 
