# Generated by Django 3.2 on 2021-04-29 06:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payments', '0014_rename_products_subsplans'),
    ]

    operations = [
        migrations.CreateModel(
            name='ot_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('icon', models.CharField(max_length=100)),
                ('currency', models.CharField(choices=[('usd', 'USD '), ('aed', 'AED '), ('afn', 'AFN '), ('all', 'ALL '), ('amd', 'AMD '), ('ang', 'ANG '), ('aoa', 'AOA '), ('ars', 'ARS '), ('aud', 'AUD '), ('awg', 'AWG '), ('azn', 'AZN '), ('bam', 'BAM '), ('bbd', 'BBD '), ('bdt', 'BDT '), ('bgn', 'BGN '), ('bif', 'BIF '), ('bmd', 'BMD '), ('bnd', 'BND '), ('bob', 'BOB '), ('brl', 'BRL '), ('bsd', 'BSD '), ('bwp', 'BWP '), ('bzd', 'BZD '), ('cad', 'CAD '), ('cdf', 'CDF '), ('chf', 'CHF '), ('clp', 'CLP '), ('cny', 'CNY '), ('cop', 'COP '), ('crc', 'CRC '), ('cve', 'CVE '), ('czk', 'CZK '), ('djf', 'DJF '), ('dkk', 'DKK '), ('dop', 'DOP '), ('dzd', 'DZD '), ('egp', 'EGP '), ('etb', 'ETB '), ('eur', 'EUR '), ('fjd', 'FJD '), ('fkp', 'FKP '), ('gbp', 'GBP '), ('gel', 'GEL '), ('gip', 'GIP '), ('gmd', 'GMD '), ('gnf', 'GNF '), ('gtq', 'GTQ '), ('gyd', 'GYD '), ('hkd', 'HKD '), ('hnl', 'HNL '), ('hrk', 'HRK '), ('htg', 'HTG '), ('huf', 'HUF '), ('idr', 'IDR '), ('ils', 'ILS '), ('inr', 'INR '), ('isk', 'ISK '), ('jmd', 'JMD '), ('jpy', 'JPY '), ('kes', 'KES '), ('kgs', 'KGS '), ('khr', 'KHR '), ('kmf', 'KMF '), ('krw', 'KRW '), ('kyd', 'KYD '), ('kzt', 'KZT '), ('lak', 'LAK '), ('lbp', 'LBP '), ('lkr', 'LKR '), ('lrd', 'LRD '), ('lsl', 'LSL '), ('mad', 'MAD '), ('mdl', 'MDL '), ('mga', 'MGA '), ('mkd', 'MKD '), ('mmk', 'MMK '), ('mnt', 'MNT '), ('mop', 'MOP '), ('mro', 'MRO '), ('mur', 'MUR '), ('mvr', 'MVR '), ('mwk', 'MWK '), ('mxn', 'MXN '), ('myr', 'MYR '), ('mzn', 'MZN '), ('nad', 'NAD '), ('ngn', 'NGN '), ('nio', 'NIO '), ('nok', 'NOK '), ('npr', 'NPR '), ('nzd', 'NZD '), ('pab', 'PAB '), ('pen', 'PEN '), ('pgk', 'PGK '), ('php', 'PHP '), ('pkr', 'PKR '), ('pln', 'PLN '), ('pyg', 'PYG '), ('qar', 'QAR '), ('ron', 'RON '), ('rsd', 'RSD '), ('rub', 'RUB '), ('rwf', 'RWF '), ('sar', 'SAR '), ('sbd', 'SBD '), ('scr', 'SCR '), ('sek', 'SEK '), ('sgd', 'SGD '), ('shp', 'SHP '), ('sll', 'SLL '), ('sos', 'SOS '), ('srd', 'SRD '), ('std', 'STD '), ('szl', 'SZL '), ('thb', 'THB '), ('tjs', 'TJS '), ('top', 'TOP '), ('try', 'TRY '), ('ttd', 'TTD '), ('twd', 'TWD '), ('tzs', 'TZS '), ('uah', 'UAH '), ('ugx', 'UGX '), ('uyu', 'UYU '), ('uzs', 'UZS '), ('vnd', 'VND '), ('vuv', 'VUV '), ('wst', 'WST '), ('xaf', 'XAF '), ('xcd', 'XCD '), ('xof', 'XOF '), ('xpf', 'XPF '), ('yer', 'YER '), ('zar', 'ZAR '), ('zmw', 'ZMW ')], max_length=100)),
                ('stripe_prod_id', models.CharField(max_length=1000)),
                ('stripe_price_id', models.CharField(max_length=1000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
