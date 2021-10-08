from django.db import models


# Create your models here.
class Etudiantes(models.Model):
    identification = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    DateOfBirth = models.DateField()
