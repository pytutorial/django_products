from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('list_category', listCategory),
    path('add_category', addCategory),
]