from django.shortcuts import render
from django.template.context_processors import request
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Director, Review, Movie
from movieapp.serializers import DirectorSerializer, ReviewSerializer, MovieSerializer


# Create your views here.
#directors
@api_view(['GET'])

def directors_view(request):
    directors = Director.objects.all()
    data = DirectorSerializer(instance=directors, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])

def detail_directors_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = DirectorSerializer(instance=director, many=False).data
    return Response(data=data, status=status.HTTP_200_OK)

#Movie
@api_view(['GET'])

def movies_view(request):
    movies = Movie.objects.all()
    data = MovieSerializer(instance=movies, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])

def detail_movies_view(request, id):
    try:
        movies = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = MovieSerializer(instance=movies, many=False).data
    return Response(data=data, status=status.HTTP_200_OK)

#Review
@api_view(['GET'])

def reviews_view(request):
    rewiews = Review.objects.all()
    data = ReviewSerializer(instance=rewiews, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])

def detail_reviews_view(request, id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = ReviewSerializer(instance=reviews, many=False).data
    return Response(data=data, status=status.HTTP_200_OK)
