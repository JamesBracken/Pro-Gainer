from django.shortcuts import render


def index(request):
    """ Returns the index page"""
    return render(request, 'index.html')