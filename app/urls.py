from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('signup', signup, name='signup'),
    path('staff', listCategory, name='list-category'),
    path('add_category', addCategory, name='add-category'),
    path('edit_category/<pk>', editCategory, name='edit-category'),
    path('delete_category/<pk>', deleteCategory, name='delete-category'),


    path('list_product', listProduct, name='list-product'),
    path('add_product', addProduct, name='add-product'),
    path('edit_product/<pk>', editProduct, name='edit-product'),
    path('delete_product/<pk>', deleteProduct, name='delete-product'),
]