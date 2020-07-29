from django.forms import ModelForm

from .models import Map


class uploadMapForm(ModelForm):
    class Meta:
        model = Map
        fields = ["title", "map_image"]


class updateMapForm(ModelForm):
    class Meta:
        model = Map
        fields = ["title", "map_image"]
