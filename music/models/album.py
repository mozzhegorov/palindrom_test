from django.db import models
from .composer import Composer


class Album(models.Model):
    """Модель альбома"""
    title = models.CharField(
        verbose_name="title",
        max_length=150,
        help_text="Album title",
    )

    composer = models.ManyToManyField(
        Composer,
        verbose_name="composers"
    )
    year = models.IntegerField(
        verbose_name="year",
    )

    class Meta:
        verbose_name = "album"
        verbose_name_plural = "albums"

    objects = models.Manager()

    def __str__(self) -> str:
        return "{title}".format(
            title=self.title
        )
