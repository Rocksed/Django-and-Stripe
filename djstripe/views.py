from django.http import JsonResponse
from django.shortcuts import render
import stripe

from config.settings import STRIPE_SECRET_KEY
from .models import Item

stripe.api_key = STRIPE_SECRET_KEY


def get_buy_session(request, id):
    item = Item.objects.get(pk=id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(item.get_absolute_url()),
        cancel_url=request.build_absolute_uri(item.get_absolute_url()),
    )
    return JsonResponse({'session_id': session.id})


def get_item(request, id):
    item = Item.objects.get(pk=id)
    return render(request, 'item_detail.html', {'item': item})
