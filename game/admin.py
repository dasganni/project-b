from django.contrib import admin
from django.contrib.auth.decorators import login_required
from guardian.admin import GuardedModelAdmin

from .models import Game

# Register your models here.
admin.site.login = login_required(admin.site.login)

# Register your models here.
admin.site.register(Game, GuardedModelAdmin)
