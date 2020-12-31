from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.context import bag_contents

import stripe


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty")
        return redirect(reverse('shop'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HhzTaK2nGVlkoiapPWp46S02IeZVjywnPa3BugLYM7qTTYN5g6C6CDvepgkoHiol6pJdspdob1EP3CD6rvFIQBS00sCLpjLTz',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
