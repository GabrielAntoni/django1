from django.db import models

# Create your models here.

class Visitas(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)
    Numero = models.BigIntegerField('e-mail',max_length=14)
