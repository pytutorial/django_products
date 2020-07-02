#views_user.py
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import *
from .forms import *

def index(request):
    productName = request.GET.get('product_name', '')
    categoryId = request.GET.get('category_id', '')
    categoryId = int(categoryId) if categoryId != '' else 0
    priceRange = request.GET.get('price_range', '')
    priceRange = int(priceRange) if priceRange != '' else 0

    productList = Product.objects.all()
    categoryList = Category.objects.all()
    context = {
        'categoryList': categoryList,
        'productList': productList
    }
    return render(request, 'user/index.html',
                    context)