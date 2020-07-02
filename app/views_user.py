#views_user.py
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import *
from .forms import *

def index(request):
    productList = Product.objects.all()
    categoryList = Category.objects.all()
    context = {
        'categoryList': categoryList,
        'productList': productList
    }
    return render(request, 'user/index.html',
                    context)