from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.decorators import login_required
from guardian.admin import GuardedModelAdmin

from .models import User

# Register your models here.
admin.site.login = login_required(admin.site.login)

admin.site.register(User, UserAdmin)
