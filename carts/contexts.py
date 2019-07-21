from django.shortcuts import get_object_or_404
from main.models import Ticket


def cart_contents(request):
    
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    
    for pk, payment in cart.items():
        ticket = get_object_or_404(Ticket, pk=pk)
        total += payment
        cart_items.append({'id': pk, 'payment': payment, 'ticket': ticket})
    
    return {'cart_items': cart_items, 'total': total}