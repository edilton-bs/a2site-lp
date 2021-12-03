from django.db import models

class Materias(models.Model):
    name = models.CharField(max_length=100)
    url_image = models.CharField(max_length=300)
    summary = models.TextField(max_length=1000)
