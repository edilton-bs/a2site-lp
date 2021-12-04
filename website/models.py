from django.db import models

class Materias(models.Model):
    name = models.CharField(max_length=100)
    url_image = models.URLField(max_length=200)
    summary = models.TextField(max_length=1000)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    


class Usuario(models.Model):
    
    FEMALE = "F"
    MALE = "M"
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
    )
    
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False)
    comb_materia = models.ManyToManyField('Materias')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.nome