from django.shortcuts import render
from django.http import HttpResponse

# This index is a "view"
def index(request):

    # Views must return HttpResponse object
    return HttpResponse("<h1>Index</h1>")\


# This index is a "view"
def help(request):

    my_dict = {'insert_me':  "now I am coming from AppTwo/templante/AppTwo/help.html with injection"}
    return render(request, "AppTwo/help.html", context=my_dict)

