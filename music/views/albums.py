from typing import List

from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView
from ..models.album import Album
from ..serializers import AlbumSerializers


class AllAlbumList(ListModelMixin, CreateModelMixin, GenericAPIView):
    """
    Представление для получения списка всех альбомов.
    """
    serializer_class = AlbumSerializers

    def get_queryset(self):
        queryset: List[Album] = Album.objects.all()
        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
