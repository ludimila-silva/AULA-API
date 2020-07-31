from django.db import models

# Create your models here.
class Pessoa(models.Model):
    name = models.CharField(max_length=30)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=15)
    cpf = models.CharField(max_length=20)
