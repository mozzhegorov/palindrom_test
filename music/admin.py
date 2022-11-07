from django.contrib import admin
from .models.album import Album
from .models.composer import Composer
from .models.track import Track, TrackInAlbum


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "year",
    )
    list_display_links = (
        "title",
        "year",
    )
    search_fields = (
        "title",
        "year",
        "composer",
    )
    fields = (
        "title",
        "year",
        "composer",
    )
    list_filter = (
        "title",
        "year",
        "composer",
    )


@admin.register(Composer)
class ComposerAdmin(admin.ModelAdmin):
    list_display = (
        "title",
    )
    list_display_links = (
        "title",
    )
    search_fields = (
        "title",
    )
    fields = (
        "title",
    )
    list_filter = (
        "title",
    )


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = (
        "title",
    )
    list_display_links = (
        "title",
    )
    search_fields = (
        "title",
    )
    fields = (
        "title",
    )
    list_filter = (
        "title",
    )


@admin.register(TrackInAlbum)
class TrackInAlbumAdmin(admin.ModelAdmin):
    list_display = (
        "album",
        "track",
        "number",
    )
    list_display_links = (
        "album",
        "track",
        "number",
    )
    search_fields = (
        "album",
        "track",
        "number",
    )
    fields = (
        "album",
        "track",
        "number",
    )
    list_filter = (
        "album",
        "track",
        "number",
    )
