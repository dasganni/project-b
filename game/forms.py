from django.forms import ModelForm
from django.forms.widgets import CheckboxSelectMultiple

from .models import Game


class createGameForm(ModelForm):
    class Meta:
        model = Game
        fields = ["title", "access_restricted", "allowed_players"]

        widgets = {"allowed_players": CheckboxSelectMultiple()}


class updateGameForm(ModelForm):
    class Meta:
        model = Game
        fields = ["title", "access_restricted", "allowed_players"]

        widgets = {"allowed_players": CheckboxSelectMultiple()}
