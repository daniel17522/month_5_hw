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
        serializer = DirectorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # This automatically creates the Director instance.
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_directors_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = DirectorSerializer(instance=director).data
        return Response(data=data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = DirectorSerializer(instance=director, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#Movie
@api_view(['GET', 'POST'])
def movies_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_movies_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response({"detail": "Movie not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data,
                                     partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Review
@api_view(['GET', 'POST'])
def reviews_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_reviews_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response({"detail": "Review not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data,
                                      partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
