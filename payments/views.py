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
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
import stripe
#Signup---------------------------------------------------------------------------------
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
UserModel = get_user_model()

#_--------------

from .tasks import mail_sender

def signup(request):
    if request.method == 'GET':
        return render(request, 'registration/signup.html')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(form.errors.as_data())
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = "Activate your account."
            message = render_to_string("emails/acc_active_email.html", {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            mail_sender.delay(mail_subject,message,to_email)
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponseRedirect(reverse_lazy("login"))
    else:
        return HttpResponse('Activation link is invalid!')

@login_required
class administration():
  @login_required
  def HomePageView(request):
    context = {}
    template = 'payments/index.html'
    return render(request, template, context)
  
  @login_required
  def settings(request):
    plan = request.user.business_auth
    if request.method == 'POST':
        form = businessmaker(request.POST, instance = plan)
        if form.is_valid():
              a = form.save(commit = False)
              s = business_auth.objects.get(user = request.user)
              s.priv_url = a.priv_url
              s.tos_url = a.tos_url
              s.business_name = a.business_name 
              s.save()

              return HttpResponseRedirect(reverse_lazy('home'))

    else:
      form = businessmaker(instance = plan)
    context = {'form':form}
    template = "payments/settings.html"
    return render(request, template, context)

  @login_required
  def signup_step(request):
    if request.method == 'POST':
        form = businessmaker(request.POST)
        if form.is_valid():
              a = form.save(commit = False)
              if business_auth.objects.filter(user=request.user).exists():
                  s = business_auth.objects.get(user = request.user)
              else:
                  s = business_auth(user = request.user)
              s.priv_url = a.priv_url
              s.tos_url = a.tos_url
              s.business_name = a.business_name 
              s.save()

              return HttpResponseRedirect("/")

    else:
      form = businessmaker()
    context = {'form':form}
    template = "payments/signup_process.html"
    return render(request, template, context)





@login_required
class Invoice():
    class Product():
       @login_required
       def invoicep(request):
              product = invoice_p.objects.filter(user = request.user)
              context = {'subplans':product}
              template = 'payments/Catalog/payment_forms.html'
              return render(request, template, context)
       @login_required
       def invoiceproductadd(request):
              if request.method == 'POST':
                     form = pinvoiceadder(request.user, request.POST)
                     print(form.errors.as_data())
                     if form.is_valid():
                          a = form.save(commit=False)
                          a.user = request.user
                          a.save()
                          messages.success(request, "Invoice Created")
                          return HttpResponseRedirect("/payment/invoice/product")

              else:
                     form = pinvoiceadder(request.user)
              context = {'form':form}
              template = "payments/Catalog/addinvoicep.html"
              return render(request, template, context)
    class Subscription():
      @login_required
      def invoices(request):
         product = invoice_s.objects.filter(user = request.user)
         context = {'subplans':product}
         template = 'payments//Catalog/sub_form.html'
         return render(request, template, context)

      @login_required
      def invoicesubplanadd(request):
           if request.method == 'POST':
             form = sinvoiceadder(request.user, request.POST)
             if form.is_valid():
               a = form.save(commit=False)
               a.user = request.user
               form.save()
               messages.success(request, "Invoice Created")
               return HttpResponseRedirect("/payment/invoice/subscription")
 
           else:
             form = sinvoiceadder(request.user)
           context = {'form':form}
           template = "payments/Catalog/addinvoices.html"
           return render(request, template, context)

@login_required
class Catalog():
    class Subscription():
        @login_required
        def subplan(request):
                 product = subsplans.objects.filter(user = request.user)
                 context = {'subplans':product}
                 template = 'payments/Catalog/subscriptionplan.html'
                 return render(request, template, context)
        
        @login_required
        def subplanadd(request):
            if request.method == 'POST':
                form = subplanadder(request.POST)
                if form.is_valid():
                  a = form.save(commit=False)
                  a.user = request.user
                  messages.success(request, "Plan Added")
                  user = Seller.objects.get(user = request.user)
                  stripe.api_key = settings.STRIPE_SECRET_KEY
                  product = stripe.Product.create(name = a.name,stripe_account= user.stripe_user_id)
                  price = stripe.Price.create(
                     product=product,
                     unit_amount=a.price*100,
                     currency=a.currency,
                     stripe_account= user.stripe_user_id,
                     recurring={'interval': a.recurrance,'interval_count':a.interval_count})
                  product_s = stripe.Product.create(name = a.name + " One Time Setup Fees",stripe_account= user.stripe_user_id)
                  price_s = stripe.Price.create(
                     product=product_s,
                     unit_amount=a.setupfees*100,
                     currency=a.currency,
                     stripe_account= user.stripe_user_id)

                  a.stripe_prod_id = product.get('id')
                  a.stripe_price_id = price.get('id')
                  a.prod_setupfees = product_s.get('id')
                  a.price_setupfees = price_s.get('id')
                  a.save()
                  return HttpResponseRedirect("/payment/subscriptionplans")
            else:
                 form = subplanadder()
            context = {'form':form}
            template = "payments/Catalog/addsubplan.html"
            return render(request, template, context)

    class Products():
            @login_required
            def ot(request):
                product = ot_product.objects.filter(user = request.user)
                context = {'subplans':product}
                template = 'payments/Catalog/products.html'
                return render(request, template, context)

            @login_required
            def ot_add(request):
                if request.method == 'POST':
                    form = productadder(request.POST)
                    if form.is_valid():
                          a = form.save(commit=False)
                          a.user = request.user
                          messages.success(request, "Plan Added")
                          user = Seller.objects.get(user = request.user)
                          stripe.api_key = settings.STRIPE_SECRET_KEY
                          product = stripe.Product.create(name = a.name, stripe_account= user.stripe_user_id,)
                          price = stripe.Price.create(product=product,unit_amount=a.price*100, currency=a.currency,stripe_account= user.stripe_user_id,)
                          a.stripe_prod_id = product.get('id')
                          a.stripe_price_id = price.get('id')
                          a.save()
                          return HttpResponseRedirect("/payment/products")
                else:
                  form = productadder()
                context = {'form':form}
                template = "payments/Catalog/addproduct.html"
                return render(request, template, context)

@login_required
class Overview():
             @login_required
             def customers(request):
                 customers = customer.objects.filter(user = request.user)
                 print(customers)
                 context = {'customer':customers}
                 template = 'payments/customers.html'
                 return render(request, template, context)
             @login_required
             def transaction(request):
                 product = transactions.objects.filter(user = request.user)
                 context = {'subplans':product}
                 template = 'payments/transactions.html'
                 return render(request, template, context)
             @login_required
             def subscriptions(request):
               subs = customer.objects.filter(user = request.user, active = True)
               context = {'subs':subs}
               template = 'payments/subscriptions.html'
               return render(request, template, context)



@login_required
def coupons(request):
    context = {}
    template = 'payments/Catalog/coupons.html'
    return render(request, template, context)
@login_required
def deleter(request,stockid):
    x= stockid.split('.')
    stripe.api_key = settings.STRIPE_SECRET_KEY
    if x[0] == "sub":
       plan = subsplans.objects.get(id=x[1])
       acc = plan.user.seller.stripe_user_id
       pric = plan.stripe_price_id
       stripe.Plan.delete(pric,stripe_account=acc)
       plan.delete()
    elif x[0] == "prod":
       plan = ot_product.objects.get(id=x[1])
       plan.delete()
    elif x[0] == "ip":
       plan = invoice_p.objects.get(id=x[1])
       plan.delete()
    if x[0] == "is":
       plan = invoice_s.objects.get(id=x[1])
       plan.delete()
    return HttpResponseRedirect("/")

@login_required
def editor(request,stockid):
    x= stockid.split('.')
       
    if x[0] == "ip":
       plan = invoice_p.objects.get( id=x[1])
       if request.method == 'POST':
        form = pinvoiceadder(request.user,request.POST, instance = plan)
        if form.is_valid():
           form.save()    
           return HttpResponseRedirect("/")
       else:
        form = pinvoiceadder(request.user,instance = plan)
       context = {'form':form, 'cb':"ip."+str(plan.id)}
       template = "payments/Catalog/editinvoicep.html"

    elif x[0] == "is":
       plan = invoice_s.objects.get( id=x[1])
       if request.method == 'POST':
        form = sinvoiceadder(request.user,request.POST, instance = plan)
        if form.is_valid():
           form.save()    
           return HttpResponseRedirect("/")
       else:
        form = sinvoiceadder(request.user,instance = plan)
       context = {'form':form, 'cb':"is."+str(plan.id)}
       template = "payments/Catalog/editinvoicep.html"
    else:
        from django.http import Http404
        raise Http404("Editor does not exist, Contact Support") 

    
    return render(request, template, context)


@login_required
def Celery(request):
    message = render_to_string('emails/email-default.html', {'user': str(request.user.username),'message': 'HI',})
    mail_sender.delay("Hi",message,'sraghav@tisb.ac.in')
    return HttpResponse('response done')











