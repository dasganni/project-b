import configparser
import os

print("Using development environment!")
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# Access configparser to load variable values
config = configparser.ConfigParser(allow_no_value=True)
config.read([os.path.join(BASE_DIR, "django_server/default.cfg"), os.path.join(BASE_DIR, "configs/settings.cfg")])


###########DEV SETTINGS##############



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

WSGI_APPLICATION = "django_server.wsgi.application"
