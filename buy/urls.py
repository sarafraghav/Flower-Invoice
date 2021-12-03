from . import views
from django.conf.urls import url
from django.urls import path


urlpatterns = [
    url(r'^buy/sub/(?P<stockid>[0-9]+)/$', views.buy , name='buys'),
    url(r'^buy/prod/(?P<stockid>[0-9]+)/$', views.buy_prod , name='buyp'),
    path('config/<stockid>/<limited>/', views.stripe_config , name='config'),
    path('pconfig/<stockid>/<limited>', views.stripe_config_p , name='pconfig'),
    path('create-checkout-session/<stockid>/<limited>', views.create_checkout_session , name='createsession'),
    path('pcreate-checkout-session/<stockid>/<limited>', views.create_checkout_session_p , name='pcreatesession'),
    path('success', views.success , name='success'),
    path('customer-portal/<cust_id>', views.customer_portal , name='portal'),
    path('webhook', views.webhook_received , name='webhook'),
    url(r'^invoice/sub/(?P<stockid>[0-9]+)/$', views.in_sub , name='insub'),
    url(r'^invoice/prod/(?P<stockid>[0-9]+)/$', views.in_prod , name='inprod'),
    #path('sentry-debug/', views.trigger_error),
 ]


