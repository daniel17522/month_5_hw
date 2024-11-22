from django.urls import path
from . import views
from .views import DirectorsView

urlpatterns = [
    path('v1/directors/', DirectorsView.as_view()),
    path('v1/directors/<int:id>/', views.DetailDirectorView.as_view()),
    path('v1/movies/', views.MoviesView.as_view()),
    path('v1/movies/<int:id>/', views.DetailMovieView.as_view()),
    path('v1/reviews/', views.ReviewsView.as_view()),
    path('v1/reviews/<int:id>/', views.DetailReviewView.as_view()),
]