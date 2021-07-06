# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
import uuid

# Create your models here.






# class PAData(models.Model):
#     zipcode = models.CharField(verbose_name='Zipcode', max_length=25, blank=True, null=True)
#     state = models.CharField(verbose_name='State', max_length=25, blank=True, null=True)
#     utility_name = models.CharField(verbose_name='Utility Name', max_length=125, blank=True, null=True)
#     utility_code = models.CharField(verbose_name='Utility Code', max_length=125, blank=True, null=True)
#     company_name = models.CharField(verbose_name='Company Name', max_length=500, blank=True, null=True )
#     plan_type = models.CharField(verbose_name='Plan type', max_length=500, blank=True, null=True )
    
#     price_rate = models.FloatField(verbose_name='Price rate', default=None, null=True)
#     monthly_fee = models.FloatField(verbose_name='Monthly free', default=None, null=True)
#     enrollment_fee = models.FloatField(verbose_name='Enrollment fee', default=None, null=True)
#     cancellation_fee = models.FloatField(verbose_name='Cancellation fee', default=None, null=True)

#     term_length = models.IntegerField(verbose_name='Term length', blank=True, null=True )
#     renewable = models.CharField(verbose_name='Renewable', max_length=25, blank=True, null=True )
#     product_info = models.TextField(verbose_name='Product info', max_length=500, blank=True, null=True)
#     phone_number = models.CharField(verbose_name='Phone number', max_length=250, blank=True, null=True )
#     signup_url = models.CharField(verbose_name='Signup url', max_length=500, blank=True, null=True )
#     product_last_update = models.CharField(verbose_name='Last update', max_length=65, blank=True, null=True )
    
#     site_name = models.CharField(verbose_name='Site name', max_length=500, blank=True, null=True )
#     domain_name = models.CharField(verbose_name='Domain name', max_length=500, blank=True, null=True )
    
#     last_scraped = models.DateTimeField(verbose_name='Scraped time', auto_now_add=True)


#     current_ptc = models.FloatField(verbose_name='Current PTC', blank=True, null=True )
#     future_ptc = models.FloatField(verbose_name='Future PTC', blank=True, null=True)
#     future_ptc_date = models.CharField(verbose_name='Fureture PTC date', max_length=500, default='', blank=True, null=True)

#     # This for ohio scraper
#     new_customer_offer = models.CharField(verbose_name='New Customer Offer ', max_length=225, default='', blank=True, null=True)
#     # This for ohio scraper
#     term_of_service = models.CharField(verbose_name='Terms of Service ', max_length=1000, default='', blank=True, null=True)

#     # Specifix for PowerToChoos
#     fact_sheet = models.CharField(verbose_name='EFL Fact Sheet', max_length=1000, default='', blank=True, null=True)
#     fiveh_kwh = models.FloatField(verbose_name='500 kWh', default=None, null=True)
#     onek_kwh = models.FloatField(verbose_name='1000 kWh', default=None, null=True)
#     twok_kwh = models.FloatField(verbose_name='2000 kWh', default=None, null=True)
#     rating = models.FloatField(verbose_name='Rating', default=None, null=True)
    
#     ref_url = models.CharField(verbose_name='Refernce url', max_length=500, blank=True, null=True )
    
#     created_at = models.DateTimeField(auto_now_add=True)
#     created_by = models.CharField(max_length=50, blank=True, null=True)
#     modified_at = models.DateTimeField(auto_now=True)
#     modified_by = models.CharField(max_length=50, blank=True, null=True)
#     scraped_key = models.CharField(max_length=50, blank=True, null=True)
#     table_name = models.CharField(max_length=65, blank=True, null=True)
    
    
#     def __str__(self):
#         return self.company_name
    
#     class Meta:
        
#         ordering = ['price_rate', 'zipcode', 'state', 'plan_type', 'term_length', 'monthly_fee', 'product_last_update']