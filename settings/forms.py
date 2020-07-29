import configparser
import os

from django import forms
from django.core import validators
from django.forms.utils import ErrorList

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config = configparser.ConfigParser(allow_no_value=True)
config.read([os.path.join(BASE_DIR, "django_server/default.cfg"), os.path.join(BASE_DIR, "configs/settings.cfg")])

# custom validator

# classes


class settingsForm(forms.Form):
    # fill in public host to reach a host from outside via given domainname
    publicHost = forms.CharField(
        label="Enter your public hostnames",
        required=False,
        help_text="This needs to be used, when the server should be reachable from outside. Seperated with spaces. localhost, 127.0.0.1, 0.0.0.0 and your default IP Address of your network card is reachable always",
        initial=config.get("default", "publichostname"),
    )
    verify_publicHost = forms.CharField(
        label="Enter your public hostnames again:",
        required=False,
        initial=config.get("default", "publichostname"),
    )

    #Enable User Registration?
    enableNewUserRegistration = forms.BooleanField(
        label="Enable registration for new users?",
        help_text="No new users can register at the website, if deactivated",
        required=False,
        initial=config.getboolean("authentication", "enableNewUserRegistration"),
    )


    #Facebook Authentication
    usefacebookauth = forms.BooleanField(
        label="Enable Facebook for Authentication?",
        help_text="Needs App configured in Facebook Development to make authentication to Facebook work!",
        required=False,
        initial=config.getboolean("authentication", "useFacebookAuth"),
    )
    facebookappid = forms.CharField(
        label="Facebook App ID (Required when Facebook Authentication used):",
        help_text="Can be found on developers.facebook.com under settings/general as App ID",
        required=False,
        initial=config.get("authentication", "facebookappid"),
    )
    facebookappkey = forms.CharField(
        label="Facebook App Key (Required when Facebookauth used):",
        help_text="Can be found on developers.facebook.com under settings/general as App Secret",
        required=False,
        initial=config.get("authentication", "facebookappkey"),
    )

    #Google Authentication
    useGoogleAuth = forms.BooleanField(
        label="Enable Google for Authentication?",
        help_text="Needs App configured in Google Developer Console to make authentication to Google work!",
        required=False,
        initial=config.getboolean("authentication", "useGoogleAuth"),
    )
    googleClientID = forms.CharField(
        label="Google Client ID (Required when Google Authentication used):",
        help_text="Can be found on console.developers.google.com under apis/credentials as Client ID",
        required=False,
        initial=config.get("authentication", "googleClientID"),
    )
    googleClientSecret = forms.CharField(
        label="Google Client Secret (Required when Google Authentication used):",
        help_text="Can be found on console.developers.google.com under apis/credentials as Client Secret",
        required=False,
        initial=config.get("authentication", "googleClientSecret"),
    )


    #Mail Server Config
    useMailSending = forms.BooleanField(
        label="Enable sending of emails by the server? (Recommended)",
        help_text="Needed for for example the password reset! You can also use your own Gmail-Address as Sender for example. If not working, try to disable secure application check at your provider.",
        required=False,
        initial=config.getboolean("mailserver", "useMailSending"),
    )
    emailHost = forms.CharField(
        label="Email SMTP Host:",
        help_text="Can be found on your Mail Providers page (For example smtp.gmail.com)",
        required=False,
        initial=config.get("mailserver", "emailHost"),
    )
    emailPort = forms.IntegerField(
        label="Email SMTP Port:",
        help_text="Can be found on your Mail Providers page (For example 587)",
        required=False,
        initial=config.get("mailserver", "emailPort"),
        max_value = 65535,
        min_value = 1,
    )
    emailHostUser = forms.CharField(
        label="Username at Email-Host:",
        help_text="Your used username at the specified Email-Host",
        required=False,
        initial=config.get("mailserver", "emailHostUser"),
    )
    emailHostUserPassword = forms.CharField(
        label="Password at Email-Host:",
        help_text="Your used password at the specified Email-Host",
        required=False,
        initial=config.get("mailserver", "emailHostUserPassword"),
        max_length=32, 
        widget=forms.TextInput(attrs={'type' : 'password'}),
    )
    emailUseTLS = forms.BooleanField(
        label="Use secured connection (TLS) to the Email Host?",
        help_text="Can be found on your Mail Providers page (Should be used by default if Host allows it)",
        required=False,
        initial=config.getboolean("mailserver", "emailUseTLS"),
    )
    defaultFromEmail = forms.CharField(
        label="Sender-Name in the Mail itself",
        required=False,
        initial=config.get("mailserver", "defaultFromEmail"),
    )


    # check all input alltogether
    def clean(self):
        # publichost and vpublichost must be the same
        all_clean_data = super().clean()

        publicHost = all_clean_data["publicHost"]
        vPublicHost = all_clean_data["verify_publicHost"]

        enableNewUserRegistration = all_clean_data["enableNewUserRegistration"]

        usefacebookauth = all_clean_data["usefacebookauth"]
        facebookappid = all_clean_data["facebookappid"]
        facebookappkey = all_clean_data["facebookappkey"]

        useGoogleAuth = all_clean_data["useGoogleAuth"]
        googleClientID = all_clean_data["googleClientID"]
        googleClientSecret = all_clean_data["googleClientSecret"]

        useMailSending = all_clean_data["useMailSending"]
        emailHost = all_clean_data["emailHost"]
        emailPort = all_clean_data["emailPort"]
        emailHostUser = all_clean_data["emailHostUser"]
        emailHostUserPassword = all_clean_data["emailHostUserPassword"]
        emailUseTLS = all_clean_data["emailUseTLS"]
        defaultFromEmail = all_clean_data["defaultFromEmail"]



        if publicHost != vPublicHost:
            self._errors["verify_publicHost"] = ErrorList([u"Hostnames must match!"])

        if usefacebookauth:
            if not facebookappid:
                self._errors["facebookappid"] = ErrorList(
                    [
                        u"If Facebook Auth should be used, the Facebook App ID and Secret must be given"
                    ]
                )
            if not facebookappkey:
                self._errors["facebookappkey"] = ErrorList(
                    [
                        u"If Facebook Auth should be used, the Facebook App ID and Secret must be given"
                    ]
                )
        
        if useGoogleAuth:
            if not googleClientID:
                self._errors["googleClientID"] = ErrorList(
                    [
                        u"If Google Auth should be used, the Google Client ID and Secret must be given"
                    ]
                )
            if not googleClientSecret:
                self._errors["googleClientSecret"] = ErrorList(
                    [
                        u"If Google Auth should be used, the Google Client ID and Secret must be given"
                    ]
                )

        if useMailSending:
            if not emailHost:
                self._errors["emailHost"] = ErrorList(
                    [
                        u"If mailsending should be used, all configs for it must be given"
                    ]
                )
            if not emailPort:
                self._errors["emailPort"] = ErrorList(
                    [
                        u"If mailsending should be used, all configs for it must be given"
                    ]
                )
            if not emailHostUser:
                self._errors["emailHostUser"] = ErrorList(
                    [
                        u"If mailsending should be used, all configs for it must be given"
                    ]
                )
            if not emailHostUserPassword:
                self._errors["emailHostUserPassword"] = ErrorList(
                    [
                        u"If mailsending should be used, all configs for it must be given"
                    ]
                )
            if not defaultFromEmail:
                self._errors["defaultFromEmail"] = ErrorList(
                    [
                        u"If mailsending should be used, all configs for it must be given"
                    ]
                )
            


        
