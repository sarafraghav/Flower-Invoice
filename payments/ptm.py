import urllib
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import View
from django.conf import settings
from django.shortcuts import redirect
import requests
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import stripe

    
@login_required 
def StripeAuthorizeView(request):
        if not business_auth.objects.filter(user=request.user).exists():
            return HttpResponseRedirect(reverse('bizsignup'))
        url = 'https://connect.stripe.com/oauth/authorize'
        params = {
            'response_type': 'code',
            'scope': 'read_write',
            'client_id': settings.STRIPE_CONNECT_CLIENT_ID,
            'redirect_uri': f'https://app.flowerapps.io/oauth/callback'
        }
        url = f'{url}?{urllib.parse.urlencode(params)}'
        return redirect(url)



@login_required
def StripeAuthorizeCallbackView(request):
        code = request.GET.get('code')
        if code:
            data = {
                'client_secret': settings.STRIPE_SECRET_KEY,
                'grant_type': 'authorization_code',
                'client_id': settings.STRIPE_CONNECT_CLIENT_ID,
                'code': code
            }
            url = 'https://connect.stripe.com/oauth/token'
            resp = requests.post(url, params=data)
            # add stripe info to the seller
            if Seller.objects.filter(user=request.user).exists():
               user = Seller.objects.get(user = request.user)
            else:
                user = Seller(user = request.user)
            user.stripe_access_token = resp.json()['access_token']
            user.stripe_user_id = resp.json()['stripe_user_id']
            user.stripe_authentication = True
            user.save()
            business = business_auth.objects.get(user=request.user)
            stripe.api_key =  settings.STRIPE_SECRET_KEY
            x = stripe.billing_portal.Configuration.create(
                    features={
                          "customer_update": {
                          "allowed_updates": ["email", "tax_id"],
                          "enabled": True,
      
                             },
                           "invoice_history": {"enabled": True},
                           "payment_method_update": {"enabled": True},
                              },
                             business_profile={
                             "privacy_policy_url":
                              business.priv_url,
                                    "terms_of_service_url":
                             business.tos_url,
                               },
                               stripe_account = user.stripe_user_id
                            )
            business.stripe_id = x





        url = reverse('home')
        response = redirect(url)
        return response
