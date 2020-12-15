from django.shortcuts import render
from shop.models import Product


def index(request):
    """ A view to return the index page """

    products = Product.objects.order_by('sku').all()[:8]
    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)
