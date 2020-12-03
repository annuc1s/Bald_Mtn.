from django.shortcuts import render
from .models import Product

def all_products(request):
    """ A view to go to main shop page """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'shop/shop.html', context)
