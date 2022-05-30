from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('images/', views.images, name='images'),
    path('search/', views.search_image, name='search'),
    path('location/', views.all_locations, name='all_location'),
    path('location/<str:pk>/', views.locations, name='location'),
    path('category/<str:pk>/', views.categories, name='category'), 
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)