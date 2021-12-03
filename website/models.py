from django.db import models

class Materias(models.Model):
    name = models.CharField(max_length=100)
    url_image = models.URLField(max_length=200)
    summary = models.TextField(max_length=1000)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name