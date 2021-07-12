# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
import uuid
from django.utils import timezone
# Create your models here.


class PAData(models.Model):
    zipcode = models.CharField(verbose_name='Zipcode', max_length=25, blank=True, null=True)
    state = models.CharField(verbose_name='State', max_length=25, blank=True, null=True)
    utility_name = models.CharField(verbose_name='Utility Name', max_length=125, blank=True, null=True)
    utility_code = models.CharField(verbose_name='Utility Code', max_length=125, blank=True, null=True)
    company_name = models.CharField(verbose_name='Company Name', max_length=500, blank=True, null=True )
    plan_type = models.CharField(verbose_name='Plan type', max_length=500, blank=True, null=True )
    
    price_rate = models.FloatField(verbose_name='Price rate', default=None, null=True)
    monthly_fee = models.FloatField(verbose_name='Monthly free', default=None, null=True)
    enrollment_fee = models.FloatField(verbose_name='Enrollment fee', default=None, null=True)
    cancellation_fee = models.FloatField(verbose_name='Cancellation fee', default=None, null=True)

    term_length = models.IntegerField(verbose_name='Term length', blank=True, null=True )
    renewable = models.CharField(verbose_name='Renewable', max_length=25, blank=True, null=True )
    product_info = models.TextField(verbose_name='Product info', max_length=500, blank=True, null=True)
    phone_number = models.CharField(verbose_name='Phone number', max_length=250, blank=True, null=True )
    signup_url = models.CharField(verbose_name='Signup url', max_length=500, blank=True, null=True )
    product_last_update = models.CharField(verbose_name='Last update', max_length=65, blank=True, null=True )
    
    site_name = models.CharField(verbose_name='Site name', max_length=500, blank=True, null=True )
    domain_name = models.CharField(verbose_name='Domain name', max_length=500, blank=True, null=True )
    
    last_scraped = models.DateTimeField(verbose_name='Scraped time', auto_now_add=True)


    current_ptc = models.FloatField(verbose_name='Current PTC', blank=True, null=True )
    future_ptc = models.FloatField(verbose_name='Future PTC', blank=True, null=True)
    future_ptc_date = models.CharField(verbose_name='Fureture PTC date', max_length=500, default='', blank=True, null=True)

    # This for ohio scraper
    new_customer_offer = models.CharField(verbose_name='New Customer Offer ', max_length=225, default='', blank=True, null=True)
    # This for ohio scraper
    term_of_service = models.CharField(verbose_name='Terms of Service ', max_length=1000, default='', blank=True, null=True)

    # Specifix for PowerToChoos
    fact_sheet = models.CharField(verbose_name='EFL Fact Sheet', max_length=1000, default='', blank=True, null=True)
    fiveh_kwh = models.FloatField(verbose_name='500 kWh', default=None, null=True)
    onek_kwh = models.FloatField(verbose_name='1000 kWh', default=None, null=True)
    twok_kwh = models.FloatField(verbose_name='2000 kWh', default=None, null=True)
    rating = models.FloatField(verbose_name='Rating', default=None, null=True)
    
    ref_url = models.CharField(verbose_name='Refernce url', max_length=500, blank=True, null=True )
    
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=50, blank=True, null=True)
    scraped_key = models.CharField(max_length=50, blank=True, null=True)
    table_name = models.CharField(max_length=65, blank=True, null=True)
    
    
    def __str__(self):
        return self.company_name
    
    class Meta:
        
        ordering = ['price_rate', 'zipcode', 'state', 'plan_type', 'term_length', 'monthly_fee', 'product_last_update']



class Shop(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='Shop Name', max_length=255, blank=True, null=True)
    url = models.CharField(verbose_name='Shop Url', max_length=1000, blank=True, null=True)
    product_no = models.PositiveIntegerField(verbose_name='Number of products', null=True, default=0)
    sale_no = models.PositiveIntegerField(verbose_name='Number of sales', null=True, default=0)
    review_no = models.PositiveIntegerField(verbose_name='Number of review', null=True, default=0)
    stars = models.FloatField(verbose_name='Shop review stars', null=True, default=0)
    author = models.CharField(verbose_name='Author', max_length=125, blank=True, null=True, default='')
    update_at = models.DateTimeField(auto_now=True)
    table_name = models.CharField(max_length=65, blank=True, null=True, default='app_shop')
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name', 'sale_no']

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(verbose_name='Product Code', max_length=125, blank=True, null=True)
    name = models.CharField(verbose_name='Product Name', max_length=500, blank=True, null=True)
    price = models.FloatField(verbose_name='Product Price', blank=True, null=True)
    url = models.CharField(verbose_name='Url', max_length=1000, blank=True, null=True)
    update_at = models.DateTimeField(auto_now=True)
    table_name = models.CharField(max_length=65, blank=True, null=True, default='app_product')
    shop = models.ForeignKey( 
        Shop, related_name='product_shop', db_constraint=False, blank = True, null=True, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.name

    def get_review_no(self):
        return Review.objects.filter(product__id__iexact=self.id).count()
    
    def get_first_review_date(self):
        first_review = Review.objects.filter(product__id__iexact=self.id).order_by('review_date')
        if first_review:
            if first_review[0].review_date:
                return first_review[0].review_date.strftime("%m/%d/%Y")
        return ''


class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.CharField(verbose_name='Review Author', max_length=125, blank=True, null=True)
    stars = models.FloatField(verbose_name='Stars', null=True, default=0)
    review_date = models.DateField(verbose_name='Review date', blank=True, null=True)
    variants = models.CharField(verbose_name='Variant', max_length=225, blank=True, null=True)
    content = models.CharField(verbose_name='Content', max_length=1000, blank=True, null=True)
    update_at = models.DateTimeField(auto_now=True)
    table_name = models.CharField(max_length=65, blank=True, null=True, default='app_review')

    product = models.ForeignKey( 
        Product, related_name='review_product', db_constraint=False, blank = True, null=True, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.content
    
    class Meta:
        ordering = ['-review_date']

class Keyword(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='Keyword', max_length=125, blank=True, null=True)
    rank = models.CharField(verbose_name='Rank', max_length=125, blank=True, null=True)
    update_at = models.DateTimeField(auto_now=True)
    table_name = models.CharField(max_length=65, blank=True, null=True, default='app_keyword')

    product = models.ForeignKey( 
        Product, related_name='keyword_product', db_constraint=False, blank = True, null=True, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.name + self.rank

    
    # Fix bug Product matching query does not exist.
    from django.db.models.fields.related_descriptors import ForwardManyToOneDescriptor
    def get_object(self, instance):
        qs = self.get_queryset(instance=instance)
        # Assuming the database enforces foreign keys, this won't fail.
        return qs.filter(self.field.get_reverse_related_filter(instance)).first()
    ForwardManyToOneDescriptor.get_object = get_object
    
    class Meta:
        ordering = ['-update_at', 'rank']