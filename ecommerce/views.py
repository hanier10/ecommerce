from django.shortcuts import render
from store.models import Product
#funcion render que permite mostrar mi view

def home(request):
    products = Product.objects.all().filter(is_available=True)
    
    context = {
        'products': products,
    }
    
    return render(request, 'home.html', context)
