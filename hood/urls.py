"""hood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views
from registration.backends.simple.views import RegistrationView
from neighborhood.forms import RegisterForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('neighborhood.urls')),
    url(r'^accounts/register/$',RegistrationView.as_view(form_class=RegisterForm),name='registration_register'),
    url(r'^logout/', views.LogoutView, name='logout'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
]
