from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404

def index(request):
    """View function for home page of site."""

    # Render the HTML template index.html with the data in the context variable
    return render(request,'index.html')
