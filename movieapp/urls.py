from django.urls import path
from . import views

urlpatterns = [
    path('v1/directors/', views.directors_view),
    path('v1/directors/<int:id>/', views.detail_directors_view),
    path('v1/movies/', views.movies_view),
    path('v1/movies/<int:id>/', views.detail_movies_view),
    path('v1/reviews/', views.reviews_view),
    path('v1/reviews/<int:id>/', views.detail_reviews_view),
]