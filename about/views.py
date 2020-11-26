from django.shortcuts import render

def index(request):
    """ A view to go to about page """

    return render(request, 'about/about.html')
