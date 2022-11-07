from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView
from ..models.track import Track, TrackInAlbum
from ..serializers import TrackSerializers, TrackInAlbumSerializers


class AllTrackList(ListModelMixin, CreateModelMixin, GenericAPIView):
    """
    Представление для получения списка всех песен.
    """
    serializer_class = TrackSerializers

    def get_queryset(self):
        queryset = Track.objects.all()
        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class AllTrackInAlbumList(ListModelMixin, CreateModelMixin, GenericAPIView):
    """
    Представление для получения списка песен в альбомах.
    """
    serializer_class = TrackInAlbumSerializers

    def get_queryset(self):
        queryset = TrackInAlbum.objects.all()
        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
