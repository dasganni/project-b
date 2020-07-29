from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView

from game.models import Game

from .forms import uploadMapForm
from .models import Map

# Create your views here.


class mapView(LoginRequiredMixin, CreateView):
    template_name = "maptool/ZoomTest.html"
    # success_url = reverse_lazy("maptool:map")
    model = Map
    form_class = uploadMapForm

    def form_valid(self, form):
        form.instance.in_game = Game.objects.get(id=self.kwargs["game_id"])
        return super(mapView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(mapView, self).get_context_data(**kwargs)
        context["map_images"] = Map.objects.filter(in_game__id=self.kwargs["game_id"])
        return context
    # must use games pk to determine used maps

class deleteMap(LoginRequiredMixin, DeleteView):
    model = Map
    pk_url_kwarg = 'map_id'
