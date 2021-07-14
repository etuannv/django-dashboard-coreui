import django_tables2 as tables
from .models import *
from django_tables2.utils import A

class NumberColumn(tables.Column):
    decimal_no = 4
    attrs={
        'td': {
            'style': 'text-align:right;'
        }
    }
    def render(self, value):
        if isinstance(value, int):
            return '{:,}'.format(value)
        else:
            return '{:0.4f}'.format(value)

class ShopTable(tables.Table):   
    name  = tables.LinkColumn(
        'shop_detail', 
        text=lambda record: record.name, 
        args=[A('pk')],
        footer=lambda table: 'Total: {} records'.format(len(table.data))
        )
    sale_no = NumberColumn(verbose_name='Sale No')
    review_no = NumberColumn(verbose_name='Review No')
    stars = NumberColumn(verbose_name='Review Stars')
    review_percent = tables.Column(
        accessor='get_review_percent',
        verbose_name='Review Percent',
        attrs={
            'td': {
                'style': 'text-align:right;'
            }
        }
    )

    url = tables.TemplateColumn(
        '<a target="_blank" href="{{record.url}}">Visit</a>',
        verbose_name='Esty URL',
        attrs={
        'td': {
            'style': 'text-align:center;'
        }
    }
    )
    
    class Meta:
        attrs = {
            'class':'table table-responsive-sm table-bordered table-striped table-sm'
        }
        model = Shop
        fields = (
            'name',
            # 'product_no', 
            'sale_no',
            'review_no',
            'review_percent',
            'stars', 
            'author',
            'url'
        )


class ProductTable(tables.Table):   
    name  = tables.LinkColumn(
        'product_detail', 
        text=lambda record: record.name, 
        args=[A('pk')],
        footer=lambda table: 'Total: {} records'.format(len(table.data))
        )
    
    shop = tables.LinkColumn(
        'shop_detail', 
        text=lambda record: record.shop.name, 
        args=[A('shop_id')],
        )
    

    url = tables.TemplateColumn(
        '<a target="_blank" href="{{record.url}}">Visit</a>',
        verbose_name='Esty URL'
    )

    first_review = tables.Column(
        accessor='get_first_review_date', 
        verbose_name='First Review Date', 
        attrs={
            'td': {
                'style': 'text-align:center;'
            }
        }
    )

    reviews = tables.TemplateColumn(
        '<a href="/review/list?content=&product__id={{record.id}}">{{record.get_review_no}}</a>',
        attrs={
            'td': {
                'style': 'text-align:right;'
            }
        }
    )
    

    price = tables.Column(
        accessor="price",
        verbose_name='Price', 
        attrs={
            'td': {
                'style': 'text-align:right;'
            }
        }
    )
    
    class Meta:
        attrs = {
            'class':'table table-responsive-sm table-bordered table-striped table-sm'
        }
        model = Product
        fields = (
            'name', 
            'price',
            'first_review',
            'reviews',
            'shop',
            'url',
        )


class ReviewTable(tables.Table):   
    content  = tables.LinkColumn(
        'review_detail', 
        text=lambda record: record.content, 
        args=[A('pk')],
        footer=lambda table: 'Total: {} records'.format(len(table.data))
        )

    stars = tables.Column(
        accessor='stars', 
        verbose_name='Review Rate', 
        attrs={
            'td': {
                'style': 'text-align:right;'
            }
        }
    )

    class Meta:
        attrs = {
            'class':'table table-responsive-sm table-bordered table-striped table-sm'
        }
        model = Review
        fields = (
            'author',
            'stars',
            'review_date',
            'variants',
        )



class KeywordTable(tables.Table):
    name  = tables.LinkColumn(
        'keyword_detail', 
        text=lambda record: record.name, 
        args=[A('pk')],
        footer=lambda table: 'Total: {} records'.format(len(table.data))
        )
    
    rank = tables.Column(
        accessor='rank',
        verbose_name='Rank', 
        attrs={
            'td': {
                'style': 'text-align:center;min-width:60px;'
            }
        }
    )
    
    product  = tables.LinkColumn(
        'product_detail', 
        text=lambda record: record.product.name if record.product.name else 'is scraping or unavailable', 
        args=[A('product_id')],
        )
    
    first_review = tables.Column(
        accessor='product.get_first_review_date',
        verbose_name='First Review Date', 
        attrs={
            'td': {
                'style': 'text-align:center;'
            }
        }
    )

    reviews = tables.TemplateColumn(
        '<a href="/review/list?content=&product__id={{record.product.id}}">{{record.product.get_review_no}}</a>',
        attrs={
            'td': {
                'style': 'text-align:right;'
            }
        }
    )
    

    # price = tables.Column(
    #     accessor="price",
    #     verbose_name='Price', 
    #     attrs={
    #         'td': {
    #             'style': 'text-align:right;'
    #         }
    #     }
    # )
    
    url = tables.TemplateColumn(
        '<a target="_blank" href="{{record.product.url}}">Visit</a>',
        verbose_name='Esty URL'
    )

    class Meta:
        attrs = {
            'class':'table table-responsive-sm table-bordered table-striped table-sm'
        }
        model = Keyword
        fields = (
            'name',
            'rank',
        )





























class PersonColumn(tables.Column):

    def render(self, record):
        return "{} {}".format(record.price_rate, record.price_rate)

class PADataTable(tables.Table):
    
    company_name  = tables.LinkColumn(
        'pa_detail', 
        text=lambda record: record.company_name, 
        args=[A('pk')],
        footer=lambda table: 'Total: {} records'.format(len(table.data))
        )
    
    est_monthly = tables.Column(
        accessor='price_rate', 
        verbose_name='Est Monthly Bill', 
        attrs={
            'td': {
                'style': 'text-align:center;'
            }
        }
    )
    def render_est_monthly(self, value, record):
        return  round(700*record.price_rate + record.monthly_fee,2)


    # defind hindden column for export data
    
    utility_code = tables.Column(visible=False)
    enrollment_fee = tables.Column(visible=False)
    cancellation_fee = tables.Column(visible=False)
    renewable = tables.Column(visible=False)
    phone_number = tables.Column(visible=False)
    signup_url = tables.Column(visible=False)
    site_name = tables.Column(visible=False)
    domain_name = tables.Column(visible=False)
    
    product_info = tables.Column(visible=False)
    current_ptc = tables.Column(visible=False)
    future_ptc = tables.Column(visible=False)
    future_ptc_date = tables.Column(visible=False)

    last_scraped = tables.DateTimeColumn(format ='M d,Y-h:iA')
    
    class Meta:
        attrs = {
            'class':'table table-responsive-sm table-bordered table-striped table-sm'
        }
        model = PAData
        fields = (
            'zipcode',
            'state', 
            'utility_name',
            'utility_code', 
            'company_name', 
            'price_rate',
            'plan_type',
            'monthly_fee', 
            'enrollment_fee',
            'cancellation_fee',
            'est_monthly',
            'term_length',
            'renewable',
            'product_info',
            'phone_number',
            'signup_url',
            'site_name',
            'domain_name',
            'current_ptc',
            'future_ptc',
            'future_ptc_date',
            'product_last_update',
            'last_scraped',
        )

class OhioTable(PADataTable):
    company_name  = tables.LinkColumn(
        'ohio_detail', 
        text=lambda record: record.company_name, 
        args=[A('pk')],
        footer=lambda table: 'Total: {} records'.format(len(table.data))
        )
    new_customer_offer = tables.Column(visible=False)
    term_of_service = tables.Column(visible=False)
    est_monthly = tables.Column(visible=False)
    product_last_update = tables.Column(visible=False)

    def render_est_monthly(self, value, record):
        return  ''
    class Meta:
        attrs = {
            'class':'table table-responsive-sm table-bordered table-striped table-sm'
        }
        model = PAData
        fields = (
            'zipcode',
            'state', 
            'utility_name',
            'utility_code', 
            'company_name', 
            'price_rate',
            'plan_type',
            'monthly_fee', 
            'enrollment_fee',
            'cancellation_fee',
            'est_monthly',
            'term_length',
            'renewable',
            'product_info',
            'phone_number',
            'signup_url',
            'site_name',
            'domain_name',
            'current_ptc',
            'future_ptc',
            'future_ptc_date',
            'product_last_update',
            'last_scraped',
            'new_customer_offer',
            'term_of_service',
        )

class OhioGasTable(OhioTable):
    company_name  = tables.LinkColumn(
        'ohio_gas_detail', 
        text=lambda record: record.company_name, 
        args=[A('pk')],
        footer=lambda table: 'Total: {} records'.format(len(table.data))
        )


class P2ChooseTable(PADataTable):
    company_name  = tables.LinkColumn(
        'p2choose_detail', 
        text=lambda record: record.company_name, 
        args=[A('pk')],
        footer=lambda table: 'Total: {} records'.format(len(table.data))
        )
    new_customer_offer = tables.Column(visible=False)
    term_of_service = tables.Column(visible=False)
    est_monthly = tables.Column(visible=False)
    product_last_update = tables.Column(visible=False)
    fact_sheet = tables.Column(visible=False)
    fiveh_kwh = tables.Column(visible=False)
    onek_kwh = tables.Column(visible=False)
    twok_kwh = tables.Column(visible=False)
    rating = tables.Column(visible=False)

    class Meta:
        attrs = {
            'class':'table table-responsive-sm table-bordered table-striped table-sm'
        }
        model = PAData
        fields = (
            'zipcode',
            'state', 
            'utility_name',
            'utility_code', 
            'company_name', 
            'price_rate',
            'plan_type',
            'monthly_fee', 
            'enrollment_fee',
            'cancellation_fee',
            'est_monthly',
            'term_length',
            'renewable',
            'product_info',
            'phone_number',
            'signup_url',
            'site_name',
            'domain_name',
            'current_ptc',
            'future_ptc',
            'future_ptc_date',
            'product_last_update',
            'last_scraped',
            'new_customer_offer',
            'term_of_service',
            'fact_sheet',
            'fiveh_kwh',
            'onek_kwh',
            'twok_kwh',
            'rating'
        )
