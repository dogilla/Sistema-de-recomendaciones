from django.db import models

# Create your models here.

class Pagina(models.Model):
    recomendacion = models.CharField(max_length=300)
    resultado = models.TextField(default="")
    color = models.CharField(max_length=300)
