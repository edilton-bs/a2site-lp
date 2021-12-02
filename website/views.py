from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404

def index(request):
    """View function for home page of site."""

    # Render the HTML template index.html with the data in the context variable
    return render(request,'index.html')


def main(request):
    """View function for home page of site."""

    # Render the HTML template index.html with the data in the context variable
    return render(request,'main.html')

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