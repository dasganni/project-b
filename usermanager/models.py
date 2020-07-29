from django.contrib import auth
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username_slug = models.SlugField(
        default='',
        editable=False,
        max_length=255,
        unique=True,
    )

    def save(self, *args, **kwargs):
        self.username_slug = slugify(AbstractUser.get_username(self))
        super(User, self).save(*args, **kwargs) # Call the real save() method

    def __str__(self):
        return self.username
