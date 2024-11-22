from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from . serializers import UserCreateSerializer, UserAuthSerializer, ConfirmationSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import ConfirmationCode
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView


# Create your views here.

class RegistrationAPIView(APIView):
    def post(self, request):

        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        user = serializer.save(is_active=False)

        confirmation_code = ConfirmationCode(user=user)
        confirmation_code.generate_code()
        print(confirmation_code)

        return Response(data={'user_id': user.id}, status=status.HTTP_201_CREATED)



#@api_view(['POST'])
# def registration_api_view(request):
#     serializer = UserCreateSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#
#     username = serializer.validated_data.get('username')
#     password = serializer.validated_data.get('password')
#
#     user = User.objects.create_user(username=username, password=password, is_active=False)
#     # create code (6 symbol)
#     confirmation_code = ConfirmationCode(user=user)
#     confirmation_code.generate_code()
#     print(confirmation_code)
#     return Response(data={'user_id': user.id}, status=status.HTTP_201_CREATED)



class AuthorizationAPIView(APIView):
    def post(self, request):
        serializer = UserAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(**serializer.validated_data)
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(data={'key': token.key})
        return Response(data={'error': 'User not valid!'}, status=status.HTTP_401_UNAUTHORIZED)


# @api_view(['POST'])
# def authorization_api_view(request):
#     serializer = UserAuthSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = authenticate(**serializer.validated_data)  # username='admin', password='admin'
#     if user is not None:
#         token, _ = Token.objects.get_or_create(user=user)
#         return Response(data={'key': token.key})
#     return Response(data={'error': 'User not valid!'},
#                     status=status.HTTP_401_UNAUTHORIZED)



class ConfirmationAPIView(APIView):
    def post(self, request):
        serializer = ConfirmationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data.get('code')

        try:
            confirmation_code = ConfirmationCode.objects.get(code=code)
            user = confirmation_code.user
            user.is_active = True
            user.save()
            confirmation_code.delete()
            return Response({"message": "Пользователь успешно подтвержден."}, status=status.HTTP_200_OK)
        except ConfirmationCode.DoesNotExist:
            return Response({"detail": "Неверный код подтверждения."}, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['POST'])
# def confirmation_api_view(request):
#     serializer = ConfirmationSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     code = serializer.validated_data.get('code')
#
#     try:
#         confirmation_code = ConfirmationCode.objects.get(code=code)
#         user = confirmation_code.user
#         user.is_active = True
#         user.save()
#         confirmation_code.delete()
#         return Response({"message": "Пользователь успешно подтвержден."}, status=status.HTTP_200_OK)
#     except ConfirmationCode.DoesNotExist:
#         return Response({"detail": "Неверный код подтверждения."}, status=status.HTTP_400_BAD_REQUEST)
