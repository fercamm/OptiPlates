from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    peso = models.FloatField()
    estatura = models.FloatField()
    # Otros campos
