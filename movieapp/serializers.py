from rest_framework import serializers
from .models import Movie, Director, Review

class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()
    class Meta:
        model = Director
        fields = ['name', 'movies_count']
    def get_movies_count(self, obj):
        return obj.movies.count()

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text','stars']


class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    rating = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = ['title', 'description', 'duration', 'director',
                  'reviews', 'rating']

    def get_rating(self, obj):
        reviews = Review.objects.all()
        if reviews:
            return sum(review.stars for review in reviews) / len(reviews)
        return 0