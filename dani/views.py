from django.shortcuts import render

def dani_index(request):
    """View function for home page of site."""

    # Render the HTML template index.html with the data in the context variable
    return render(request,'dani_index.html')
