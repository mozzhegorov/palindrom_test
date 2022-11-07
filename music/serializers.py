from django.db import IntegrityError
from rest_framework import serializers
from .models.track import Track, TrackInAlbum
from .models.composer import Composer
from .models.album import Album


class ComposerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Composer
        fields = "__all__"


class TrackSerializers(serializers.ModelSerializer):
    
    def create(self, validated_data):
        instance, _ = Track.objects.get_or_create(**validated_data)
        return instance

    class Meta:
        model = Track
        fields = (
            "title",
        )
        extra_kwargs = {
            "id": {"read_only": False},
            "title": {"validators": []},
        }


class AlbumTitleSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        instance, _ = Album.objects.get_or_create(**validated_data)
        return instance

    class Meta:
        model = Album
        fields = (
            "title",
        )


class TrackInAlbumSerializers(serializers.ModelSerializer):
    track = TrackSerializers()
    album = AlbumTitleSerializer()

    class Meta:
        model = TrackInAlbum
        fields = (
            "track",
            "album",
            "number",
        )

    def create(self, validated_data):
        track, _ = Track.objects.get_or_create(title=validated_data["track"]["title"])
        album, _ = Album.objects.get_or_create(title=validated_data["album"]["title"])
        validated_data["track"]: Track = track
        validated_data["album"]: Album = album
        try:
            instance = TrackInAlbum.objects.create(**validated_data)
        except IntegrityError:
            error_msg = {"error": "IntegrityError message, "
                                  "maybe this number in album already exists"}
            raise serializers.ValidationError(error_msg)
        return instance


class AlbumSerializers(serializers.ModelSerializer):
    tracks = TrackInAlbumSerializers(
        source="albums", 
        read_only=True, 
        many=True,
    )
    composer = ComposerSerializers(
        read_only=True, 
        many=True,
    )

    class Meta:
        model = Album
        fields = "__all__"
