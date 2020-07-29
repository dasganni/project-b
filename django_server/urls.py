"""django_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from guardian.admin import GuardedModelAdmin

# Register your models here.
admin.site.login = login_required(admin.site.login)
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user-management/', include("usermanager.urls", namespace="usermanager")),
    #path('accounts/', include("django.contrib.auth.urls")),
    path('accounts/', include('allauth.urls')),
    path('dice/', include('dice.urls')),
    path('character/', include('character.urls')),
    path('settings/', include('settings.urls')),
    path('game/', include('game.urls')),
    path('', include('index.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #only in debug=true - For production nginx or apache must serve the media files

handler500 = 'servererrors.views.internalServerErrorView'

