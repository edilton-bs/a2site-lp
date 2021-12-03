from django.db import models

class Materias(models.Model):
    name = models.CharField(max_length=100)
    url_image = models.CharField(max_length=300)
    summary = models.TextField(max_length=1000)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title