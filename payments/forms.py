from django.forms import ModelForm, Form
from .models import *
from pyuploadcare.dj.forms import ImageField
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):  
        class Meta:  
            model = User  
            fields = ('email', 'first_name', 'last_name', 'username')

class subplanadder(ModelForm):
    icon = ImageField(label='')
    class Meta:
        model = subsplans
        fields = ['name','description','price','recurrance','interval_count','setupfees','trial','icon','currency']

class productadder(ModelForm):
    icon = ImageField(label='')
    class Meta:
        model = ot_product
        fields = ['name','description','price','icon','currency']

class producteditor(ModelForm):
    icon = ImageField(label='')
    class Meta:
        model = ot_product
        fields = ['name','description','icon']
class businessmaker(ModelForm):
    class Meta:
        model = business_auth
        fields = ['priv_url','tos_url','business_name']
      
class sinvoiceadder(ModelForm):
    class Meta:
        model = invoice_s
        fields = ['name','description','address','product']
    def __init__(self,user,*args,**kwargs):
         super (sinvoiceadder,self ).__init__(*args,**kwargs) # populates the post
         self.fields['product'].queryset = subsplans.objects.filter(user=user)
         self.fields['product'].label_from_instance = lambda obj: "%s" % (obj.name)
   

class pinvoiceadder(ModelForm):
    class Meta:
        model = invoice_p
        fields = ['name','description','address','product']
    def __init__(self,user,*args,**kwargs):
         super (pinvoiceadder,self ).__init__(*args,**kwargs) # populates the post
         self.fields['product'].queryset = ot_product.objects.filter(user=user)
         self.fields['product'].label_from_instance = lambda obj: "%s" % (obj.name)
