from django.shortcuts import render
from django.http import HttpResponse

# STEP1:  Import models
from first_app.models import Topic, Webpage, AccessRecord

# Create your views here.

# This index is a "view"
def index(request):

    # STEP 2:  Get the data from the model
    webpages_list = AccessRecord.objects.order_by("date")
    date_dict = {"access_records":  webpages_list}

    # STEP 3:  Pass the data to the template
    return render(request, "first_app/index.html", context=date_dict)