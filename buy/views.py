from django.shortcuts import render
from django.conf import settings # new
from django.http.response import JsonResponse , HttpResponse# new
from django.views.decorators.csrf import csrf_exempt # new
import stripe
from payments.models import subsplans,customer, Seller, transactions, ot_product, invoice_s, invoice_p
from django.contrib.auth.models import User
import json
from django.http import HttpResponseRedirect
# Create your views here.

def trigger_error(request):
    division_by_zero = 1 / 0



def buy(request, stockid):
    if subsplans.objects.filter(id=stockid).exists():
       i = subsplans.objects.get(id=stockid)
       context = {'obj':i}
       template = "buy/home.html"
       return render(request, template,context)
    else:
        from django.http import Http404
        raise Http404("Poll does not exist")

def buy_prod(request, stockid):
    if ot_product.objects.filter(id=stockid).exists():
       i = ot_product.objects.get(id=stockid)
       context = {'obj':i}
       template = "buy/prod.html"
       return render(request, template,context)
    else:
        from django.http import Http404
        raise Http404("Poll does not exist")       

def in_prod(request, stockid):
    print(stockid)
    if invoice_p.objects.filter(id=stockid).exists():
       i = invoice_p.objects.get(id=stockid)
       stripe.api_key = settings.STRIPE_SECRET_KEY
       prod = ot_product.objects.get(id=stockid)
       z = stripe.Price.retrieve(prod.stripe_price_id,stripe_account=prod.user.seller.stripe_user_id)
       r =  str(z['currency']).upper() +' '+ str(z['unit_amount']/100)
       context = {'obj':i,'pric':r}
       template = "buy/invoicep.html"
       return render(request , template,context)
    else:
        from django.http import Http404
        raise HttpResponse("Hello")    

def in_sub(request, stockid):
    if invoice_s.objects.filter(id=stockid).exists():
       i = invoice_s.objects.get(id=stockid)
       stripe.api_key = settings.STRIPE_SECRET_KEY
       prod = subsplans.objects.get(id=stockid)
       z = stripe.Price.retrieve(prod.stripe_price_id,stripe_account=prod.user.seller.stripe_user_id)
       r =  str(z['currency']).upper() +' '+ str(z['unit_amount']/100)
       e = stripe.Price.retrieve(prod.price_setupfees,stripe_account=prod.user.seller.stripe_user_id)
       p =  str(e['currency']).upper() +' '+ str(e['unit_amount']/100)
       o = z['unit_amount']/100 + e['unit_amount']/100
       context = {'obj':i,'pric':[r,p],'total':o}
       template = "buy/invoices.html"
       return render(request,template ,context)
    else:
        from django.http import Http404
        raise Http404("Poll does not exist")    

@csrf_exempt
def stripe_config(request,stockid):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY, 'stripe_account':subsplans.objects.get(id=stockid).user.seller.stripe_user_id,}
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def stripe_config_si(request,stockid):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY, 'stripe_account':invoice_s.objects.get(id=stockid).user.seller.stripe_user_id,}
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def stripe_config_p(request,stockid):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY, 'stripe_account':ot_product.objects.get(id=stockid).user.seller.stripe_user_id,}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request,stockid, limited):
    
    if request.method == 'GET':
        domain_url ="https://"+ request.META['HTTP_HOST']
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            if limited == "buy":
               prod = subsplans.objects.get(id=stockid)
            elif limited == "invoice":
                prod = invoice_s.objects.filter(product = stockid)[0].product
            if int(prod.trial) > 0:
             checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + '/success/{CHECKOUT_SESSION_ID}/'+prod.user.seller.stripe_user_id +"/"+str(prod.id),
                cancel_url=domain_url + '/buy/sub/'+stockid,
                payment_method_types=['card'],
                stripe_account=prod.user.seller.stripe_user_id,
                mode='subscription',
                subscription_data= {'trial_period_days' : int(prod.trial)},
                line_items=[
                    {
                        'price': prod.stripe_price_id,
                        'quantity': 1,

                        
                    },{
                      'price': prod.price_setupfees,
                       'quantity': 1,
                      }],

             )
            else:
                checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + '/success/{CHECKOUT_SESSION_ID}/'+prod.user.seller.stripe_user_id +"/"+str(prod.id),
                cancel_url=domain_url + '/buy/sub/'+stockid,
                payment_method_types=['card'],
                stripe_account=prod.user.seller.stripe_user_id,
                mode='subscription',
                line_items=[
                    {
                        'price': prod.stripe_price_id,
                        'quantity': 1,

                        
                    },{
                      'price': prod.price_setupfees,
                       'quantity': 1,
                      }],

             )
             


            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})

@csrf_exempt
def create_checkout_session_p(request,stockid):
    if request.method == 'GET':
        domain_url = "https://"+request.META['HTTP_HOST']
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            prod = ot_product.objects.get(id=stockid)
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + '/success/',
                cancel_url=domain_url + '/buy/sub/'+stockid,
                payment_method_types=['card'],
                stripe_account=prod.user.seller.stripe_user_id,
                mode='payment',
                line_items=[
                    {
                        'price': prod.stripe_price_id,
                        'quantity': 1,

                        
                    }],




            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})





def success(request):
  template = "buy/Success.html"
  return render(request, template)
  


def customer_portal(request,cust_id):
    # This is the URL to which the customer will be redirected after they are
    # done managing their billing with the portal.
    stripe.api_key = settings.STRIPE_SECRET_KEY
    acc = customer.objects.get(stripe_id = cust_id).user.seller.stripe_user_id
    session = stripe.billing_portal.Session.create(customer=cust_id,return_url='https://google.com',stripe_account=acc)
  #      return_url=return_url)
    return HttpResponseRedirect(session.url)



@csrf_exempt
def webhook_received(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    # Try to validate and create a local instance of the event
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, settings.STRIPE_SIGNING_SECRET)
    except ValueError as e:
        # Invalid payload
        return SuspiciousOperation(e)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return SuspiciousOperation(e)

  # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        stripe.api_key = settings.STRIPE_SECRET_KEY
        checkout_session = event['data']['object']
        # Make sure is already paid and not delayed
        if checkout_session.payment_status == "paid":
             line_items = stripe.checkout.Session.list_line_items(checkout_session.id, stripe_account= event['account'])
             for x in line_items.data:
                 print(x.price.id)
                 if subsplans.objects.filter(stripe_price_id = x.price.id).exists():
                      c_m = customer(user=Seller.objects.get(stripe_user_id = event['account']).user,email = checkout_session.customer_details.email, active = True ,stripe_id =checkout_session.customer , stripe_sub_id = checkout_session.id, product = subsplans.objects.get(stripe_price_id= x.price.id))
                      c_m.save()
    if event['type'] == 'invoice.paid':

           prc_id = event['data']['object']['lines']['data'][0]['price']['id']
           x =   subsplans.objects.filter(stripe_price_id = prc_id)
           if x.exists():
             y = transactions(user =x[0].user,product = x[0], customer_email = str(event['data']['object']['customer_email']),customer_id = event['data']['object']['customer'], price_id = prc_id,invoice_id=event['id'])
             y.save()
    if event['type'] == 'customer.subscription.deleted':
        
        x = customer.objects.filter(stripe_id = event['data']['object']['customer'])
        if x.exists():
          x[0].active = False
          x.save()

    # Passed signature verification
    return HttpResponse(status=200)