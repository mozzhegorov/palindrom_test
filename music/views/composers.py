from typing import List

from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView
from ..models.composer import Composer
from ..serializers import ComposerSerializers


class AllComposerList(ListModelMixin, CreateModelMixin, GenericAPIView):
    """
    Представление для получения списка всех исполнителей песен.
    """
    serializer_class = ComposerSerializers

    def get_queryset(self):
        queryset: List[Composer] = Composer.objects.all()
        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
