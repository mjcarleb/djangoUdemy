from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# This index is a "view"
def index(request):

    # Views must return HttpResponse object
    return HttpResponse("<em>My Second App</em>")