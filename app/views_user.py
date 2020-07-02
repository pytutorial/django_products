#views_user.py
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import *
from .forms import *

def findProducts(productName, categoryId, priceRange):
    prices = {
        0:{'min':None, 'max':None},
        1:{'min':None, 'max':10},
        2:{'min':10,   'max': 15},
        3:{'min':15,   'max': 20},
        4:{'min':20,   'max': None},
    }
    minPrice, maxPrice = prices[priceRange]['min'], prices[priceRange]['max']
    productList = Product.objects.all()
    if productName != '':
        productList = productList.filter(name__contains=productName)
    if minPrice != None:
        productList = productList.filter(price__gte=minPrice)
    if maxPrice:
        productList = productList.filter(price__lte=maxPrice)
    if categoryId:
        productList = productList.filter(category__id=categoryId)
    return productList

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