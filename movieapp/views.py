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
@api_view(['GET', 'POST'])

def directors_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        data = DirectorSerializer(instance=directors, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        name = request.data.get('name')

        directors = Director.objects.create(name=name)
        return Response(data=DirectorSerializer(directors).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])

def detail_directors_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = DirectorSerializer(instance=director, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        director.name = request.data.get('name')
        director.save()
        return Response(data=DirectorSerializer(director).data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#Movie
@api_view(['GET', 'POST'])

def movies_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        data = MovieSerializer(instance=movies, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        movies = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
        return Response(data=MovieSerializer(movies).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])

def detail_movies_view(request, id):
    try:
        movies = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = MovieSerializer(instance=movies, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        movies.title = request.data.get('title')
        movies.description = request.data.get('description')
        movies.duration = request.data.get('duration')
        movies.director_id = request.data.get('director_id')
        movies.save()
        return Response(data=MovieSerializer(movies).data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Review
@api_view(['GET', 'POST'])

def reviews_view(request):
    if request.method == 'GET':
        rewiews = Review.objects.all()
        data = ReviewSerializer(instance=rewiews, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.data.get('text')
        stars = request.data.get('stars')
        movie_id = request.data.get('movie_id')
        reviews = Review.objects.create(text=text, stars=stars, movie_id=movie_id)
        return Response(data=ReviewSerializer(reviews).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])

def detail_reviews_view(request, id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ReviewSerializer(instance=reviews, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        reviews.text = request.data.get('text')
        reviews.stars = request.data.get('stars')
        reviews.movie_id = request.data.get('movie_id')
        reviews.save()
        return Response(data=ReviewSerializer(reviews).data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        reviews.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
