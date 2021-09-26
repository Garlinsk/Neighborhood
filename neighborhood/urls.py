from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.index, name = 'index'),
    url(r'^search/', views.search_businesses, name='search_results'),
    url(r'^new/business$', views.new_business, name='new-business'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
