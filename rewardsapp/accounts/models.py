from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    coins = models.IntegerField(default=0)

    @classmethod
    def profile(cl, user_id: int):
        return cl.objects.filter(id=user_id).first()

