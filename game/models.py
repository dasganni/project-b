from django.db import models
from django.urls import reverse_lazy
from django.utils.text import slugify
from guardian.models import GroupObjectPermissionBase, UserObjectPermissionBase
from django.forms.widgets import CheckboxSelectMultiple


# Create your models here.
class Game(models.Model):

    title = models.CharField(
        verbose_name="Titel", max_length=60, default="", blank=False, null=False
    )

    title_slug = models.SlugField(
        default="",
        editable=False,
        blank=False,
        null=False,
        max_length=60,
        unique=False,
    )

    creation_date = models.DateTimeField(
        auto_now=True, editable=False, auto_now_add=False, null=False
    )

    creator = models.ForeignKey(
        "usermanager.User",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name="creator",
    )

    access_restricted = models.BooleanField(default=False)

    allowed_players = models.ManyToManyField("usermanager.User", blank=True)

    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

    def save(self, *args, **kwargs):
        self.title_slug = slugify(self.title)
        super(Game, self).save(*args, **kwargs)  # Call the real save() method

    class Meta:
        indexes = [models.Index(fields=["creation_date"])]
        verbose_name = "game"
        verbose_name_plural = "games"
        ordering = ["-creation_date"]
        default_permissions = ("add", "change", "delete")
        permissions = (("view_game", "Can view game"),)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("game:games_list")


class GameUserObjectPermission(UserObjectPermissionBase):
    content_object = models.ForeignKey(Game, on_delete=models.CASCADE)


class GameGroupObjectPermission(GroupObjectPermissionBase):
    content_object = models.ForeignKey(Game, on_delete=models.CASCADE)
