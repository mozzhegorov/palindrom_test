from django.db import models
from .album import Album


class Track(models.Model):
    """Модель песни"""
    title = models.CharField(
        verbose_name="title",
        max_length=150,
        help_text="Track title",
        unique=True,
    )

    class Meta:
        verbose_name = "track"
        verbose_name_plural = "tracks"

    objects = models.Manager()

    def __str__(self) -> str:
        return "{title}".format(
            title=self.title
        )


class TrackInAlbum(models.Model):
    """Связь м2м между альбомами и песнями"""
    track = models.ForeignKey(
        Track,
        on_delete=models.CASCADE,
        related_name="tracks",
    )
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name="albums",
    )
    number = models.IntegerField()

    class Meta:
        unique_together = (
            'album',
            'number',
        )
