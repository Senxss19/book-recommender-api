from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:

        model = Book

        fields = "__all__"


class RatingStatsSerializer(serializers.Serializer):

    rating = serializers.FloatField()

    count = serializers.IntegerField()


class PublisherStatsSerializer(serializers.Serializer):

    publisher = serializers.CharField()

    count = serializers.IntegerField()