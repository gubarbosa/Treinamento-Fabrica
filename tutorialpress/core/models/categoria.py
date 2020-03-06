from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_lenght=255)
    
