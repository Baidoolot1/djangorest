from rest_framework import serializers
from .models import Movie, Director, Review


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name'.split()


class DirectorListSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()
    class Meta:
        model = Director
        fields = 'id name movies_count'.split()

    def get_movies_count(self, director):
        return director.movies.count()


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'title reviews duration description'.split()


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'review_name text stars_str '.split()


# class Moview_ReviewSerializer(serializers.ModelSerializer):
#     reviews = ReviewSerializers(many=True)
#     class Meta:
#         model = Movie
#         fields = 'title reviews'.split()

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()

    def to_representation(self, instance):
        show = super().to_representation(instance)
        #show['movie'] = instance.movie.title

        return show


class MoviesReviewsListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'title duration description reviews rating'.split()

    def get_rating(self, obj_movie):
        sum_ = 0
        for i in obj_movie.reviews.all():
            sum_ += int(i.stars)
        return round(sum_ / obj_movie.reviews.count(), 1) if obj_movie.reviews.count() else "This movie has no rating"


