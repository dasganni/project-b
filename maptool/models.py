from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse_lazy


def validate_image(image):
    file_size = image.file.size
    limit_mb = 8
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError(
            "Max size of file is %s MB. Your uploaded image is %s MB"
            % limit_mb
            % file_size
        )

    # limit_mb = 8
    # if file_size > limit_mb * 1024 * 1024:
    #    raise ValidationError("Max size of file is %s MB" % limit_mb)


class Map(models.Model):

    title = models.CharField(
        max_length=60, default="", blank=False, verbose_name="map title"
    )
    image_height = models.PositiveIntegerField(blank=True, null=True)
    image_width = models.PositiveIntegerField(blank=True, null=True)
    map_image = models.ImageField(
        upload_to="maps/",
        height_field="image_height",
        width_field="image_width",
        max_length=255,
        blank=False,
        null=True,
        validators=[validate_image]
    )
    in_game = models.ForeignKey(
        "game.Game", related_name="maps", on_delete=models.CASCADE, null=True
    )
    creation_date = models.DateTimeField(
        auto_now=True, editable=False, auto_now_add=False
    )

    class Meta:
        indexes = [models.Index(fields=["creation_date"])]
        verbose_name = "map"
        verbose_name_plural = "maps"
        ordering = ["-creation_date"]

    def get_absolute_url(self):
        return reverse_lazy("game:maptool:map", kwargs={"game_id": self.in_game.id})
    # moeglicherweise map in game integrieren und damit die maps dem game zuordnen

