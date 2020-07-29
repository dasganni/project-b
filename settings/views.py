import configparser
import os

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.edit import FormView

from settings.models import *

from . import forms


# Create your views here.
class settingsView(LoginRequiredMixin, FormView):
    template_name = "settings/settings.html"
    form_class = forms.settingsForm
    success_url = "/settings/"

    def form_valid(self, form):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Access configparser to load variable values from cfg file
        config = configparser.ConfigParser(allow_no_value=True)

        config.read([os.path.join(BASE_DIR, "django_server/default.cfg"), os.path.join(BASE_DIR, "configs/settings.cfg")])


        config.set("default", "publichostname", form.cleaned_data["publicHost"])

        # user-registration-config
        if form.cleaned_data["enableNewUserRegistration"]:
            enableNewUserRegistration = "yes"
        else:
            enableNewUserRegistration = "no"
        config.set(
            "authentication", "enableNewUserRegistration", enableNewUserRegistration
        )

        # facebook-config
        if form.cleaned_data["usefacebookauth"]:
            usefacebookauth = "yes"
        else:
            usefacebookauth = "no"
        config.set("authentication", "usefacebookauth", usefacebookauth)
        config.set(
            "authentication", "facebookappid", form.cleaned_data["facebookappid"]
        )
        config.set(
            "authentication", "facebookappkey", form.cleaned_data["facebookappkey"]
        )

        # google-config
        if form.cleaned_data["useGoogleAuth"]:
            useGoogleAuth = "yes"
        else:
            useGoogleAuth = "no"
        config.set("authentication", "useGoogleAuth", useGoogleAuth)
        config.set(
            "authentication", "googleClientID", form.cleaned_data["googleClientID"]
        )
        config.set(
            "authentication",
            "googleClientSecret",
            form.cleaned_data["googleClientSecret"],
        )

        #mailsending-config
        if form.cleaned_data["emailUseTLS"]:
            emailUseTLS = "yes"
        else:
            emailUseTLS = "no"

        if form.cleaned_data["useMailSending"]:
            usemailSending = "yes"
        else:
            usemailSending = "no"


        config.set("mailserver", "usemailSending", usemailSending)
        config.set("mailserver", "emailUseTLS", emailUseTLS)

        config.set("mailserver", "emailHost", form.cleaned_data["emailHost"])
        config.set("mailserver", "emailPort", str(form.cleaned_data["emailPort"]))
        config.set("mailserver", "emailHostUser", form.cleaned_data["emailHostUser"])
        config.set("mailserver", "emailHostUserPassword", form.cleaned_data["emailHostUserPassword"])
        config.set("mailserver", "defaultFromEmail", form.cleaned_data["defaultFromEmail"])

        # write config into config-file
        with open(
            os.path.join(BASE_DIR, "configs/settings.cfg"), "w"
        ) as configfile:
            config.write(configfile)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(settingsView, self).get_context_data(**kwargs)
        context["allowedHosts"] = settings.ALLOWED_HOSTS
        return context
