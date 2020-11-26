from django.shortcuts import render


def index(request):
    """ A view to go to contact page """

    return render(request, 'contact/contact.html')
