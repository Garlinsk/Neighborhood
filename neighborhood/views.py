from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
import datetime as dt
from .models import *

# Create your views here.


def index(request):
    date = dt.date.today()
    # all_neighborhoods = Neighborhood.get_neighborhoods()
    return render(request, 'index.html', {"date": date})
