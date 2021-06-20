from django.urls import path


from . import views, ptm

urlpatterns = [

#Admmin    

    path('signup/', views.signup, name='signup'),
    path('bizsignup/', views.administration.signup_step, name='bizsignup'),
    path('', views.Invoice.Product.invoicep, name='home'),
    path('authorize/', ptm.StripeAuthorizeView, name='authorize'),
    path('oauth/callback/', ptm.StripeAuthorizeCallbackView, name='authorize_callback'),
     path('activate/<uidb64>/<token>/',views.activate, name='activate'),

#Invoice 
    
    path('payment/invoice/product', views.Invoice.Product.invoicep, name = 'invoicep'),
    path('payment/invoice/subscription', views.Invoice.Subscription.invoices, name = 'invoices'),
    path('payment/invoice/product/add', views.Invoice.Product.invoiceproductadd, name = 'invoicepadd'),
    path('payment/invoice/subscription/add', views.Invoice.Subscription.invoicesubplanadd, name = 'invoicesadd'),
   
#Catalog 

    path('payment/subscriptionplans', views.Catalog.Subscription.subplan, name = 'subplan'),
    path('payment/subscriptionplans/add', views.Catalog.Subscription.subplanadd, name = 'subplanadd'),
    path('payment/products', views.Catalog.Products.ot, name = 'product'),
    path('payment/products/add', views.Catalog.Products.ot_add, name = 'productadd'),


#Overview    

    path('payment/subscriptions', views.Overview.subscriptions, name = 'subscriptions'),
    path('payment/transactions', views.Overview.transaction, name = 'transactions'),
    path('payment/customers', views.Overview.customers, name = 'customers'),

#General 
    path('delete/<stockid>', views.deleter , name='delete'),
    path('edit/<stockid>', views.editor , name='editor'),
    path('payment/coupons', views.coupons, name = 'coupons'),
    path('celery-test/',views.Celery, name='celery_test_url'),
    
]