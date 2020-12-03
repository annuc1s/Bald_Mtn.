from django.shortcuts import render


def index(request):
    """ A view to go to main shop page """

    return render(request, 'shop/shop.html')
