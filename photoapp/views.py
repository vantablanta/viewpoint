from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Category, Image, Location
from django.db.models import Q


def home(request):
    categories = Category.objects.all()
    locations = Location.objects.all()
    images = Image.objects.all()
    context={'categories': categories, 'images': images, 'locations':locations}
    return render(request, 'photoapp/index.html', context)

def categories(request, pk):
    category_id = Category.objects.get(id=pk)
    images = Image.objects.filter(image_category=category_id)
    context = {'category_id':category_id, 'images':images}
    return render(request, 'photoapp/category.html', context)

def all_locations(request):
    locations = Location.objects.all()
    context ={'locations':locations}
    return render(request, 'navbar.html', context)

def locations(request, pk):
    location_id = Location.objects.get(id=pk)
    images = Image.objects.filter(image_location=location_id)
    context = {'location_id':location_id, 'images':images}
    return render(request, 'photoapp/locations.html', context)

def images(request):
    images = Image.objects.all()
    context = {'images':images}
    return render(request, 'photoapp/images.html', context)

def search_image(request):
    query = request.GET.get('q')
    if query:
        images = Image.objects.filter(
            Q(image_name__icontains=query)|
            Q(image_location__place__icontains=query)|
            Q(image_category__category__icontains=query)
        )
        context={'images':images}
        return render(request, 'photoapp/search.html', context)
    return HttpResponse('No search results found')
