from rest_framework import serializers
from .models import Movie, Director, Review
from rest_framework.exceptions import ValidationError

class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()
    class Meta:
        model = Director
        fields = ['name', 'movies_count']
    def validate_name(self, name):
        if len(name) < 2:
            raise ValidationError('имя должно иметь не менее 2 символов!')

    def get_movies_count(self, obj):
        return obj.movies.count()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text','stars', 'movie']
    def Validate_reviews_id(self, review_id):
        try:
            Review.objects.get(id=review_id)
        except:
            raise ValidationError('review does not exist!')


class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    rating = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = ['title', 'description', 'duration', 'director', 'reviews',
                'rating']
    def Validate_Movie_id(self, movie_id):
        try:
            Movie.objects.get(id=movie_id)
        except:
            raise ValidationError('movie does not exist!')

    def validate_name(self, title):
        if len(title) < 2:
            raise ValidationError('название фильма должно иметь не менее 2 символов!')

    def get_rating(self, obj):
        reviews = Review.objects.all()
        if reviews:
            return sum(review.stars for review in reviews) / len(reviews)
        return 0

