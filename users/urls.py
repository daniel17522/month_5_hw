from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.RegistrationAPIView.as_view()),
    path('authorization/', views.AuthorizationAPIView.as_view()),
    path('confirmation/', views.ConfirmationAPIView.as_view()),
]