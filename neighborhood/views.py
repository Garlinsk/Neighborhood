from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

# Create your views here.


def index(request):
    date = dt.date.today()
    # all_neighborhoods = Neighborhood.get_neighborhoods()
    return HttpResponse(request,'index.html')
