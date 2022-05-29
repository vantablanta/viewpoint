from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Category, Image
from django.db.models import Q


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


# def copy_image(request, pk):
#     image = Image.objects.get(id=pk)
#     image_url = Image.objects.filter(image=image)
#     clipboard.copy(image_url) 
#     return HttpResponse('Copied!')
