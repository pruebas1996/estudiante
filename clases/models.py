from django.db import models


# Create your models here.
class Clase(models.Model):
    name = models.CharField(max_length=200)
    theme = models.CharField(max_length=500)
    active = models.BooleanField(default=False)
    schedule = models.CharField(max_length=200)
