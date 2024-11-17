from django.db import models
from django.contrib.auth.models import User
import random
import string

class ConfirmationCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)

    def generate_code(self):
        self.code = ''.join(random.choices(string.digits, k=6))
        self.save()

    def __str__(self):
        return f"Код подтверждения: - {self.code}"
