from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# This index is a "view"
def index(request):

    # Views must return HttpResponse object
    my_dict = {'insert_me':  "now I am coming from first_app/index.html"}
    return render(request, "first_app/index.html", context=my_dict)