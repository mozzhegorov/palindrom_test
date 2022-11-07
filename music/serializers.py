from rest_framework import serializers
from .models.track import Track, TrackInAlbum
from .models.composer import Composer
from .models.album import Album


class ComposerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Composer
        fields = [
            "title",
        ]


class TrackSerializers(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = [
            "title",
        ]


class AlbumTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = [
            "title",
        ]


class TrackInAlbumSerializers(serializers.ModelSerializer):
    track = TrackSerializers()
    album = AlbumTitleSerializer()

    class Meta:
        model = TrackInAlbum
        fields = [
            "track",
            "album",
            "number",
        ]


class AlbumSerializers(serializers.ModelSerializer):
    tracks = TrackInAlbumSerializers(source='albums', read_only=True, many=True)
    # track = serializers.PrimaryKeyRelatedField(queryset=Track.objects.all(), many=True)
    # authors = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), many=True)

    composer = ComposerSerializers(read_only=True, many=True)

    class Meta:
        model = Album
        fields = ('__all__')
