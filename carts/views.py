from django.shortcuts import render, redirect, reverse
from django.contrib import messages

def view_cart(request):
    return render(request, "carts/cart.html")


def add_to_cart(request, pk):
    # Add a payment amount to the cart
    payment = int(request.POST.get('payment'))

    cart = request.session.get('cart', {})
    if pk in cart:
        cart[pk] = int(cart[pk]) + payment      
    else:
        cart[pk] = cart.get(pk, payment) 

    request.session['cart'] = cart
    messages.success(request, f'Amount added to the funding cart, ready for Chechout')
    return redirect('ticket-detail', pk)


def adjust_cart(request, pk):

    # Adjust the payment
    
    payment = int(request.POST.get('payment'))
    cart = request.session.get('cart', {})
    
    if payment > 0:
        cart[pk] = payment
    else:
        cart.pop(str(pk))
    
    request.session['cart'] = cart
    return redirect('cart')