from rest_framework import serializers
from rest_framework.exceptions import ValidationError

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


class MovieBaseValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(allow_null=True, allow_blank=True)
    duration = serializers.CharField(allow_blank=True, allow_null=True)
    director_id = serializers.IntegerField(min_value=1)


class MovieCreateSerializer(MovieBaseValidateSerializer):

    def valdiate_director_id(self, director_id):
        if Director.objects.filter(id=director_id):
            raise ValidationError('error')
        return director_id


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'movie_id text stars movie_name'.split()


# class Moview_ReviewSerializer(serializers.ModelSerializer):
#     reviews = ReviewSerializers(many=True)
#     class Meta:
#         model = Movie
#         fields = 'title reviews'.split()



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
