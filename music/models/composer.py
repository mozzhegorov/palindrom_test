from django.db import models


class Composer(models.Model):
    """Модель исполнителя"""
    title = models.CharField(
        verbose_name="title",
        max_length=150,
        help_text="Composer title",
        unique=True,
    )

    class Meta:
        verbose_name = "сomposer"
        verbose_name_plural = "сomposers"

    objects = models.Manager()

    def __str__(self) -> str:
        return "{title}".format(
            title=self.title
        )
