from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Seller) 
admin.site.register(subsplans) 
admin.site.register(business_auth) 
admin.site.register(customer) 
admin.site.register(transactions) 
admin.site.register(ot_product) 
admin.site.register(invoice_s) 
admin.site.register(invoice_p) 
