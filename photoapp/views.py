from django.shortcuts import render
from .models import Category

# Create your views here.
def home(request):

    categories = Category.objects.all()
    context={'categories': categories}
    return render(request, 'photoapp/index.html', context)