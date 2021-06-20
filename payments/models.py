from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from pyuploadcare.dj.models import ImageField
# Create your models here.

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stripe_access_token = models.CharField(max_length=100)
    stripe_user_id = models.CharField(max_length=100)
    


class business_auth(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    priv_url = models.CharField(max_length=100)
    tos_url = models.CharField(max_length=100)
    business_name = models.CharField(max_length=100)
    stripe_id = models.CharField(max_length=100)

class subsplans(models.Model):
    Currency_CHOICES = (('usd','USD '),('aed','AED '),('afn','AFN '),('all','ALL '),('amd','AMD '),('ang','ANG '),('aoa','AOA '),('ars','ARS '),('aud','AUD '),('awg','AWG '),('azn','AZN '),('bam','BAM '),('bbd','BBD '),('bdt','BDT '),('bgn','BGN '),('bif','BIF '),('bmd','BMD '),('bnd','BND '),('bob','BOB '),('brl','BRL '),('bsd','BSD '),('bwp','BWP '),('bzd','BZD '),('cad','CAD '),('cdf','CDF '),('chf','CHF '),('clp','CLP '),('cny','CNY '),('cop','COP '),('crc','CRC '),('cve','CVE '),('czk','CZK '),('djf','DJF '),('dkk','DKK '),('dop','DOP '),('dzd','DZD '),('egp','EGP '),('etb','ETB '),('eur','EUR '),('fjd','FJD '),('fkp','FKP '),('gbp','GBP '),('gel','GEL '),('gip','GIP '),('gmd','GMD '),('gnf','GNF '),('gtq','GTQ '),('gyd','GYD '),('hkd','HKD '),('hnl','HNL '),('hrk','HRK '),('htg','HTG '),('huf','HUF '),('idr','IDR '),('ils','ILS '),('inr','INR '),('isk','ISK '),('jmd','JMD '),('jpy','JPY '),('kes','KES '),('kgs','KGS '),('khr','KHR '),('kmf','KMF '),('krw','KRW '),('kyd','KYD '),('kzt','KZT '),('lak','LAK '),('lbp','LBP '),('lkr','LKR '),('lrd','LRD '),('lsl','LSL '),('mad','MAD '),('mdl','MDL '),('mga','MGA '),('mkd','MKD '),('mmk','MMK '),('mnt','MNT '),('mop','MOP '),('mro','MRO '),('mur','MUR '),('mvr','MVR '),('mwk','MWK '),('mxn','MXN '),('myr','MYR '),('mzn','MZN '),('nad','NAD '),('ngn','NGN '),('nio','NIO '),('nok','NOK '),('npr','NPR '),('nzd','NZD '),('pab','PAB '),('pen','PEN '),('pgk','PGK '),('php','PHP '),('pkr','PKR '),('pln','PLN '),('pyg','PYG '),('qar','QAR '),('ron','RON '),('rsd','RSD '),('rub','RUB '),('rwf','RWF '),('sar','SAR '),('sbd','SBD '),('scr','SCR '),('sek','SEK '),('sgd','SGD '),('shp','SHP '),('sll','SLL '),('sos','SOS '),('srd','SRD '),('std','STD '),('szl','SZL '),('thb','THB '),('tjs','TJS '),('top','TOP '),('try','TRY '),('ttd','TTD '),('twd','TWD '),('tzs','TZS '),('uah','UAH '),('ugx','UGX '),('uyu','UYU '),('uzs','UZS '),('vnd','VND '),('vuv','VUV '),('wst','WST '),('xaf','XAF '),('xcd','XCD '),('xof','XOF '),('xpf','XPF '),('yer','YER '),('zar','ZAR '),('zmw','ZMW '),)
    Recurrance_Choices = (("day","Daily"),("week","Weekly"),("month","Monthly"),("year","Yearly"))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(999999)])
    recurrance = models.CharField(max_length=100, choices=Recurrance_Choices)
    setupfees = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(999999)])
    trial = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(730)])
    interval_count = models.IntegerField(default=1,validators=[MinValueValidator(0),MaxValueValidator(365)])
    icon = ImageField(blank=True, manual_crop="")
    currency = models.CharField(max_length=100, choices=Currency_CHOICES,default =Currency_CHOICES[0] )
    stripe_prod_id = models.CharField(max_length=1000)
    stripe_price_id = models.CharField(max_length=1000)
    prod_setupfees = models.CharField(max_length=1000)
    price_setupfees = models.CharField(max_length=1000)


class customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    stripe_id = models.CharField(max_length=1000)
    stripe_sub_id = models.CharField(max_length=1000)
    product = models.ForeignKey(subsplans, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)

class transactions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(subsplans, on_delete=models.CASCADE)
    customer_email = models.CharField(max_length=100)
    customer_id = models.CharField(max_length=100)
    price_id = models.CharField(max_length=1000)
    invoice_id = models.CharField(max_length=1000)
    
class ot_product(models.Model):
    Currency_CHOICES = (('usd','USD '),('aed','AED '),('afn','AFN '),('all','ALL '),('amd','AMD '),('ang','ANG '),('aoa','AOA '),('ars','ARS '),('aud','AUD '),('awg','AWG '),('azn','AZN '),('bam','BAM '),('bbd','BBD '),('bdt','BDT '),('bgn','BGN '),('bif','BIF '),('bmd','BMD '),('bnd','BND '),('bob','BOB '),('brl','BRL '),('bsd','BSD '),('bwp','BWP '),('bzd','BZD '),('cad','CAD '),('cdf','CDF '),('chf','CHF '),('clp','CLP '),('cny','CNY '),('cop','COP '),('crc','CRC '),('cve','CVE '),('czk','CZK '),('djf','DJF '),('dkk','DKK '),('dop','DOP '),('dzd','DZD '),('egp','EGP '),('etb','ETB '),('eur','EUR '),('fjd','FJD '),('fkp','FKP '),('gbp','GBP '),('gel','GEL '),('gip','GIP '),('gmd','GMD '),('gnf','GNF '),('gtq','GTQ '),('gyd','GYD '),('hkd','HKD '),('hnl','HNL '),('hrk','HRK '),('htg','HTG '),('huf','HUF '),('idr','IDR '),('ils','ILS '),('inr','INR '),('isk','ISK '),('jmd','JMD '),('jpy','JPY '),('kes','KES '),('kgs','KGS '),('khr','KHR '),('kmf','KMF '),('krw','KRW '),('kyd','KYD '),('kzt','KZT '),('lak','LAK '),('lbp','LBP '),('lkr','LKR '),('lrd','LRD '),('lsl','LSL '),('mad','MAD '),('mdl','MDL '),('mga','MGA '),('mkd','MKD '),('mmk','MMK '),('mnt','MNT '),('mop','MOP '),('mro','MRO '),('mur','MUR '),('mvr','MVR '),('mwk','MWK '),('mxn','MXN '),('myr','MYR '),('mzn','MZN '),('nad','NAD '),('ngn','NGN '),('nio','NIO '),('nok','NOK '),('npr','NPR '),('nzd','NZD '),('pab','PAB '),('pen','PEN '),('pgk','PGK '),('php','PHP '),('pkr','PKR '),('pln','PLN '),('pyg','PYG '),('qar','QAR '),('ron','RON '),('rsd','RSD '),('rub','RUB '),('rwf','RWF '),('sar','SAR '),('sbd','SBD '),('scr','SCR '),('sek','SEK '),('sgd','SGD '),('shp','SHP '),('sll','SLL '),('sos','SOS '),('srd','SRD '),('std','STD '),('szl','SZL '),('thb','THB '),('tjs','TJS '),('top','TOP '),('try','TRY '),('ttd','TTD '),('twd','TWD '),('tzs','TZS '),('uah','UAH '),('ugx','UGX '),('uyu','UYU '),('uzs','UZS '),('vnd','VND '),('vuv','VUV '),('wst','WST '),('xaf','XAF '),('xcd','XCD '),('xof','XOF '),('xpf','XPF '),('yer','YER '),('zar','ZAR '),('zmw','ZMW '),)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(999999)])
    icon = ImageField(blank=True, manual_crop="")
    currency = models.CharField(max_length=100, choices=Currency_CHOICES)
    stripe_prod_id = models.CharField(max_length=1000)
    stripe_price_id = models.CharField(max_length=1000)

class invoice_s(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    product = models.ForeignKey(subsplans, on_delete=models.CASCADE)

class invoice_p(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    product = models.ForeignKey(ot_product, on_delete=models.CASCADE)