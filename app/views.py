from django.shortcuts import render
from .models import *
from .forms import *

def index(request):
    return render(request, 'index.html')

def listCategory(request):
    categoryList = Category.objects.all()
    return render(request, 'category/list.html', {'categoryList': categoryList})

def addCategory(request):
    form = CategoryForm()
    return render(request, 'category/form.html', {'form': form})

