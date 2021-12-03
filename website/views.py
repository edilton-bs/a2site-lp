from django.shortcuts import render, reverse
from website.models import Materias
from django.http import HttpResponse, HttpResponseRedirect, Http404

def index(request):
    """View function for home page of site."""

    # Render the HTML template index.html with the data in the context variable
    return render(request,'index.html')


def main(request):
    materias = Materias.objects.filter(pk__in=[1,2,3,4,5])
    
    context = {'materias': materias}

    # Render the HTML template index.html with the data in the context variable
    return render(request,'main.html', context=context)

def nota(request):
    """View function for home page of site."""

    # Render the HTML template index.html with the data in the context variable
    return render(request,'nota.html')


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