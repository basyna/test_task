import os

import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from dotenv import load_dotenv

from .models import Item

load_dotenv()
stripe.api_key = os.environ.get('SK_TEST_KEY')
PK_KEY = os.environ.get('PK_TEST_KEY')


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelView(TemplateView):
    template_name = 'cancel.html'


class ItemDetail(View):
    def get(self, request, *args, **kwargs):
        template = 'item_detail.html'
        item_detailed = Item.objects.get(id=self.kwargs['pk'])
        context = {
            'item': item_detailed,
            'PK_KEY': PK_KEY,
        }
        return render(request, template, context)


class CreateCheckoutSessionView(View):
    def get(self, request, *args, **kwargs):
        item = Item.objects.get(id=self.kwargs['pk'])
        domain = 'http://158.160.20.111'
        if settings.DEBUG:
            domain = 'http://lockalhost:8000'
        created_session = stripe.checkout.Session.create(
            line_items=[{
              'price_data': {
                'currency': item.currency,
                'product_data': {
                  'name': item.name,
                },
                'unit_amount': item.price,
              },
              'quantity': 1,
            }],
            mode='payment',
            success_url=domain + '/success/',
            cancel_url=domain + '/cancel/',
        )
        return JsonResponse({'Id': created_session['id']})
