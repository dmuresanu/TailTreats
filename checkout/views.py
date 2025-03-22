from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51R5XksCpP0dbs1R9fBh7qccnm8yfWyUOjLy1zHVcVUWhDLpujSwc5J1I3AWaLicAh3WbhywhpUrYDyL6vgZ4QxAC00Lxs1N05n',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)