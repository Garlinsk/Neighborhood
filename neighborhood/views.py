from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
import datetime as dt
from .models import *
from django.contrib import messages
from django.conf import settings
from django.templatetags.static import static
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404
# Create your views here.


def index(request):
    date = dt.date.today()
    # all_neighborhoods = Neighborhood.get_neighborhoods()
    if 'neighborhood' in request.GET and request.GET["neighborhood"]:
        neighborhoods = request.GET.get("neighborhood")
        searched_neighborhood = Business.get_by_neighborhood(neighborhoods)
        all_posts = Posts.get_by_neighborhood(neighborhoods)
        message = f"{neighborhoods}"
        all_neighborhoods = Neighborhood.get_neighborhoods()

        return render(request, 'index.html', {"message": message, "location": searched_neighborhood,
                                              "all_neighborhoods": all_neighborhoods, "all_posts": all_posts})

    else:
        message = "No Neighborhood Found!"

    return render(request, 'index.html', {"date": date, "all_neighborhoods": all_neighborhoods, })

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('/')

    else:
        form = RegisterForm()
    return render(request, 'registration/registration_form.html', {'form': form})
