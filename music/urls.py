from django.urls import path
from .views.tracks import AllTrackList, AllTrackInAlbumList
from .views.albums import AllAlbumList
from .views.composers import AllComposerList

app_name = "order"

urlpatterns = [
    path("track/", AllTrackList.as_view(), name="tracks"),
    path("album/", AllAlbumList.as_view(), name="albums"),
    path("composer/", AllComposerList.as_view(), name="composers"),
    path("trackinalbum/", AllTrackInAlbumList.as_view(), name="tracks in albums"),
]
