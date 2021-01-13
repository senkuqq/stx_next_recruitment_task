from abc import ABC

from rest_framework import serializers
from .models import *


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.StringRelatedField(many=True)
    categories = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = ['id','title', 'authors', 'published_date', 'average_rating', 'ratings_count', 'thumbnail', 'categories']


class DatabaseSerializer(serializers.Serializer):
    q = serializers.CharField(required=True)
