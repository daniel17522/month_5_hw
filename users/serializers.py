from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
import re
from .models import ConfirmationCode

class UserAuthSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField()



class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField()

    def validate_password(self, password):
        if len(password) < 6:
            raise ValidationError("пароль должен содержать минимум 6 значений")

        # Проверка на наличие хотя бы одной цифры, одного символа и одной заглавной буквы
        if not re.search(r'[A-Z]', password):
            raise ValidationError("пароль должен содержать хотя бы одну большую букву.")
        if not re.search(r'[0-9]', password):
            raise ValidationError("пароль должен содержать хотя бы одну цифру.")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>_]', password):
            raise ValidationError("пароль должен содержать хотя бы один символ.")

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('Юзер уже существует!')

class ConfirmationSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6)

    def validate_code(self, value):
        try:
            ConfirmationCode.objects.get(code=value)
        except ConfirmationCode.DoesNotExist:
            raise ValidationError('Неверный код')
        return value






