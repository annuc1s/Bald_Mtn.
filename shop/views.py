from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product


def all_products(request):
    """ A view to go to main shop page """

    products = Product.objects.all()
    query = None
    sort = None
    direction = None

    """ Search query will return results if matched with
    name and/or description by using Django db model Q """
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Search field cannot be empty!")
                return redirect(reverse('shop'))

        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'shop/shop.html', context)


def product_detail(request, product_id):
    """ A view to go to a specific product details page """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'shop/product_detail.html', context)
