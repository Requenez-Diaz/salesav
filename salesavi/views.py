from typing import ContextManager
from django.shortcuts import render
from store.models import Product
#funcion parwa mstrar mis views

def home (request):
    products = Product.objects.all().filter(is_available=True)

    context = {
        'products': products,
    }

    return render(request, 'home.html', context)