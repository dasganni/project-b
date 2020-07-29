from django.shortcuts import render
from . import models
from django.views.generic import View, TemplateView, ListView, DetailView

#login and authentication
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from guardian.admin import GuardedModelAdmin
from django.utils.decorators import method_decorator
# Create your views here.


class indexView(TemplateView):
    template_name = 'index/index.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        variable_insert = "Per Django eingefügter String!"
        return render(request, self.template_name, context)


