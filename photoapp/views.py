from django.shortcuts import render
from .models import Category, Image

def home(request):
    categories = Category.objects.all()
    images = Image.objects.all()
    context={'categories': categories, 'images': images}
    return render(request, 'photoapp/index.html', context)

def categories(request, pk):
    category_id = Category.objects.get(id=pk)
    images = Image.objects.filter(image_category=category_id)
    context = {'category_id':category_id, 'images':images}
    return render(request, 'photoapp/category.html', context)


def images(request):
    images = Image.objects.all()
    context = {'images':images}
    return render(request, 'photoapp/images.html', context )

def search_image(request):
    context={}
    return render(request, 'photoapp/search.html', context)
