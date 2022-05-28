from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def home(request):
    context={}
    return render(request, 'photoapp/index.html', context)