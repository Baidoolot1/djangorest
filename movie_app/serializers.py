from rest_framework import serializers
from .models import Movie, Director, Review

class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name'.split()

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'title'.split()


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text review'.split()