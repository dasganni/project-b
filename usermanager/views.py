from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from . import forms
from .models import User
    
class changeUser(LoginRequiredMixin, UpdateView):
    form_class = forms.UserEditForm
    success_url = reverse_lazy("settings:settings")
    template_name = "usermanager/changeuser.html"
    model = User

    def get(self, request, **kwargs):
        self.object = User.objects.get(username=self.request.user)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def get_object(self):
        return self.request.user

