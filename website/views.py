from django.shortcuts import render, reverse
from website.models import Materias, Usuario, Comb_materias
import random
from django.http import HttpResponse, HttpResponseRedirect, Http404
import numpy as np


def index(request):
    """View function for home page of site."""

    # Render the HTML template index.html with the data in the context variable
    return render(request,'index.html')

def registrar(request):
    '''função para registrar usuários'''
    
    materias = list(Materias.objects.all())
    
    
    #escolher materias
    num_materias = random.randint(1, 10)
    
    
    #criando usuario
    for num in range(1, 201):
        sexos = [Usuario.MALE, Usuario.FEMALE]
        
        idade = random.randint(10, 40)
        sexo = random.choice(sexos)
        
        
        user = Usuario(nome=num, idade=idade, sexo=sexo)
        user.save()
        
        num_materias = random.randint(0, 10)
        
        grade = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan ]
        
        for i in range(0, num_materias):
            materia = random.choice(materias)
            user.comb_materia.add(materia)
            
            if materia not in grade:
                grade[i] = materia
        combinacao = Comb_materias(
                                   mat1 = grade[0], 
                                   mat2 = grade[1], 
                                   mat3 = grade[2], 
                                   mat4 = grade[3], 
                                   mat5 = grade[4], 
                                   mat6 = grade[5], 
                                   mat7 = grade[6],
                                   mat8 = grade[7],
                                   mat9 = grade[8],
                                   mat10 = grade[9])
    
        combinacao.save()   
    return render(request,'index.html')
            
def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)          





def main(request):
    materias = Materias.objects.filter(pk__in=[1,2,3,4,5])
    
    context = {'materias': materias}

    # Render the HTML template index.html with the data in the context variable
    return render(request,'main.html', context=context)

def nota(request):
    """View function for home page of site."""
    materias = Materias.objects.filter(pk__in=[1,2,3,4,5])
    context = {'materias': materias}
    # Render the HTML template index.html with the data in the context variable
    return render(request,'nota.html', context=context)


def forum(request):
    """View function for home page of site."""

    # Render the HTML template index.html with the data in the context variable
    return render(request,'forum.html')

def edit_profile(request):
    """View function for home page of site."""

    # Render the HTML template index.html with the data in the context variable
    return render(request,'edit-profile.html')


def profile(request):
    """View function for home page of site."""

    # Render the HTML template index.html with the data in the context variable
    return render(request,'profile.html')