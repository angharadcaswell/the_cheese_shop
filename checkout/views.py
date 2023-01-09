from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MOPMQEElqczpmTtWlIn8couJrucw4nQsQA4LZXSm8T9TPvjiQY0FylEh2dNHEUMlNyW9URWVGh1GTKSPkbWw7Q100LoydwWRd',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
    