from django import template

""" Allows to calculate subtoatal within bag view """

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
