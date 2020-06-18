from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import *
from .forms import *

def index(request):
    return render(request, 'index.html')

def listCategory(request):
    categoryList = Category.objects.all()
    return render(request, 'category/list.html', {'categoryList': categoryList})

def addCategory(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-category')
    return render(request, 'category/form.html', {'form': form})

def editCategory(request, pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('list-category')
    return render(request, 'category/form.html', {'form': form})

def deleteCategory(request, pk):    
    category = get_object_or_404(Category,pk=pk) 
    category.delete()
    return redirect('list-category')

def listProduct(request):
    productList = Product.objects.all()
    return render(request, 'product/list.html', {'productList': productList})

def addProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-product')
    return render(request, 'product/form.html', {'form': form})

def editProduct(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('list-product')
    return render(request, 'product/form.html', {'form': form})

def deleteProduct(request, pk):    
    product = get_object_or_404(Product,pk=pk) 
    product.delete()
    return redirect('list-productd')    