# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView

from django_tables2.export.export import TableExport
from django_tables2 import RequestConfig
import django_tables2 as tables
from django_tables2.export.views import ExportMixin

from .models import *
from .filters import *
from .tables import *
from pytz import timezone
import time

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        template = loader.get_template('pages/' + load_template)
        return HttpResponse(template.render(context, request))

    except:

        template = loader.get_template( 'pages/error-404.html' )
        return HttpResponse(template.render(context, request))


# @login_required(login_url="/login/")
# def index(request):
#     return render(request, "index.html")

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "app/index.html"
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['keyword_no'] = Keyword.objects.order_by().values('name').distinct().count()
        context['shop_no'] = Shop.objects.all().count()
        context['product_no'] = Product.objects.all().count()
        context['review_no'] = Review.objects.all().count()
        
        return context
       


class ShopListView(LoginRequiredMixin, ExportMixin, tables.SingleTableView):
    model = Shop
    
    table_class = ShopTable
    context_object_name = 'data_table'
    template_name = "app/shop_list.html"
    my_export_data = None
    export_name='ShopList_' + time.strftime('%Y%m%d_%H_%M_%S')
    

    def get_context_data(self, **kwargs):
        list = Shop.objects.all()
        filter = ShopFilter(self.request.GET, queryset=list)
        data_table = ShopTable(filter.qs)
        
        RequestConfig(self.request).configure(data_table)
        per_page = self.request.GET.get('per_page', 100)
        data_table.paginate(page=self.request.GET.get('page', 1), per_page=per_page)
        self.my_export_data = data_table
        context = super(ShopListView, self).get_context_data(**kwargs)
        context['data_table'] = data_table
        context['filter'] = filter
        
        return context
    
    def create_export(self, export_format):
        
        exporter = self.export_class(
            export_format=export_format,
            table=self.my_export_data,
            # exclude_columns=self.exclude_columns,
            # dataset_kwargs=self.get_dataset_kwargs(),
        )

        return exporter.response(filename=self.get_export_filename(export_format))


class ShopDetailView(LoginRequiredMixin, DetailView):
    model = Shop
    template_name = "app/shop_detail.html"
    def get_object(self, queryset=None):
        return Shop.objects.get(id=self.kwargs.get("id"))






class ProductListView(LoginRequiredMixin, ExportMixin, tables.SingleTableView):
    model = Product
    
    table_class = ProductTable
    context_object_name = 'data_table'
    template_name = "app/product_list.html"
    my_export_data = None
    export_name='ProductList_' + time.strftime('%Y%m%d_%H_%M_%S')
    

    def get_context_data(self, **kwargs):
        list = Product.objects.all()
        filter = ProductFilter(self.request.GET, queryset=list)
        data_table = ProductTable(filter.qs)
        
        RequestConfig(self.request).configure(data_table)
        per_page = self.request.GET.get('per_page', 100)
        data_table.paginate(page=self.request.GET.get('page', 1), per_page=per_page)
        self.my_export_data = data_table
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['data_table'] = data_table
        context['filter'] = filter
        
        return context
    
    def create_export(self, export_format):
        
        exporter = self.export_class(
            export_format=export_format,
            table=self.my_export_data,
            # exclude_columns=self.exclude_columns,
            # dataset_kwargs=self.get_dataset_kwargs(),
        )

        return exporter.response(filename=self.get_export_filename(export_format))


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "app/product_detail.html"
    def get_object(self, queryset=None):
        return Product.objects.get(id=self.kwargs.get("id"))





class ReviewListView(LoginRequiredMixin, ExportMixin, tables.SingleTableView):
    model = Review
    
    table_class = ReviewTable
    context_object_name = 'data_table'
    template_name = "app/review_list.html"
    my_export_data = None
    export_name='ReviewList_' + time.strftime('%Y%m%d_%H_%M_%S')
    

    def get_context_data(self, **kwargs):
        list = Review.objects.all()
        filter = ReviewFilter(self.request.GET, queryset=list)
        data_table = ReviewTable(filter.qs)
        
        RequestConfig(self.request).configure(data_table)
        per_page = self.request.GET.get('per_page', 100)
        data_table.paginate(page=self.request.GET.get('page', 1), per_page=per_page)
        self.my_export_data = data_table
        context = super(ReviewListView, self).get_context_data(**kwargs)
        context['data_table'] = data_table
        context['filter'] = filter
        
        return context
    
    def create_export(self, export_format):
        
        exporter = self.export_class(
            export_format=export_format,
            table=self.my_export_data,
            # exclude_columns=self.exclude_columns,
            # dataset_kwargs=self.get_dataset_kwargs(),
        )

        return exporter.response(filename=self.get_export_filename(export_format))


class ReviewDetailView(LoginRequiredMixin, DetailView):
    model = Review
    template_name = "app/review_detail.html"
    def get_object(self, queryset=None):
        return Review.objects.get(id=self.kwargs.get("id"))





class KeywordListView(LoginRequiredMixin, ExportMixin, tables.SingleTableView):
    model = Keyword
    
    table_class = KeywordTable
    context_object_name = 'data_table'
    template_name = "app/keyword_list.html"
    my_export_data = None
    export_name='KeywordList_' + time.strftime('%Y%m%d_%H_%M_%S')
    

    def get_context_data(self, **kwargs):
        list = Keyword.objects.all()
        filter = KeywordFilter(self.request.GET, queryset=list)
        data_table = KeywordTable(filter.qs)
        
        RequestConfig(self.request).configure(data_table)
        per_page = self.request.GET.get('per_page', 100)
        data_table.paginate(page=self.request.GET.get('page', 1), per_page=per_page)
        self.my_export_data = data_table
        context = super(KeywordListView, self).get_context_data(**kwargs)
        context['data_table'] = data_table
        context['filter'] = filter
        
        return context
    
    def create_export(self, export_format):
        
        exporter = self.export_class(
            export_format=export_format,
            table=self.my_export_data,
            # exclude_columns=self.exclude_columns,
            # dataset_kwargs=self.get_dataset_kwargs(),
        )

        return exporter.response(filename=self.get_export_filename(export_format))


class KeywordDetailView(LoginRequiredMixin, DetailView):
    model = Keyword
    template_name = "app/keyword_detail.html"
    def get_object(self, queryset=None):
        return Keyword.objects.get(id=self.kwargs.get("id"))























class PADataListView(LoginRequiredMixin, ExportMixin, tables.SingleTableView):
    model = PAData
    
    table_class = PADataTable
    context_object_name = 'data_table'
    template_name = "app/padata_list.html"
    my_export_data = None
    export_name='Papowerswitch_' + time.strftime('%Y%m%d_%H_%M_%S')
    

    def get_context_data(self, **kwargs):
        list = PAData.objects.all().filter(created_by='pa_spd')
        filter = PADataFilter(self.request.GET, queryset=list)
        data_table = PADataTable(filter.qs)
        
        RequestConfig(self.request).configure(data_table)
        per_page = self.request.GET.get('per_page', 100)
        data_table.paginate(page=self.request.GET.get('page', 1), per_page=per_page)
        self.my_export_data = data_table
        context = super(PADataListView, self).get_context_data(**kwargs)
        context['data_table'] = data_table
        context['filter'] = filter
        
        return context
    
    def create_export(self, export_format):
        
        exporter = self.export_class(
            export_format=export_format,
            table=self.my_export_data,
            # exclude_columns=self.exclude_columns,
            # dataset_kwargs=self.get_dataset_kwargs(),
        )

        return exporter.response(filename=self.get_export_filename(export_format))

class PADataDetailView(LoginRequiredMixin, DetailView):
    model = PAData
    template_name = "app/padata_detail.html"



class OhioListView(LoginRequiredMixin, ExportMixin, tables.SingleTableView):
    model = PAData
    
    table_class = OhioTable
    context_object_name = 'data_table'
    template_name = "app/ohio_list.html"
    my_export_data = None
    export_name='Enerygychoiceohio_' + time.strftime('%Y%m%d_%H_%M_%S')
    

    def get_context_data(self, **kwargs):
        list = PAData.objects.filter(created_by='ohio_spd')
        filter = OhioFilter(self.request.GET, queryset=list)
        data_table = OhioTable(filter.qs)
        
        RequestConfig(self.request).configure(data_table)
        per_page = self.request.GET.get('per_page', 100)
        data_table.paginate(page=self.request.GET.get('page', 1), per_page=per_page)
        self.my_export_data = data_table
        context = super(OhioListView, self).get_context_data(**kwargs)
        context['data_table'] = data_table
        context['filter'] = filter
        
        return context
    
    def create_export(self, export_format):
        
        exporter = self.export_class(
            export_format=export_format,
            table=self.my_export_data,
            # exclude_columns=self.exclude_columns,
            # dataset_kwargs=self.get_dataset_kwargs(),
        )

        return exporter.response(filename=self.get_export_filename(export_format))


class OhioDetailView(LoginRequiredMixin, DetailView):
    model = PAData
    template_name = "app/ohio_detail.html"



class OhioGasListView(LoginRequiredMixin, ExportMixin, tables.SingleTableView):
    model = PAData
    
    table_class = OhioGasTable
    context_object_name = 'data_table'
    template_name = "app/ohio_gas_list.html"
    my_export_data = None
    export_name='Enerygychoiceohio_gas_' + time.strftime('%Y%m%d_%H_%M_%S')
    

    def get_context_data(self, **kwargs):
        list = PAData.objects.filter(created_by='ohio_gas_spd')
        filter = OhioGasFilter(self.request.GET, queryset=list)
        data_table = OhioGasTable(filter.qs)
        
        RequestConfig(self.request).configure(data_table)
        per_page = self.request.GET.get('per_page', 100)
        data_table.paginate(page=self.request.GET.get('page', 1), per_page=per_page)
        self.my_export_data = data_table
        context = super(OhioGasListView, self).get_context_data(**kwargs)
        context['data_table'] = data_table
        context['filter'] = filter
        
        return context
    
    def create_export(self, export_format):
        
        exporter = self.export_class(
            export_format=export_format,
            table=self.my_export_data,
            # exclude_columns=self.exclude_columns,
            # dataset_kwargs=self.get_dataset_kwargs(),
        )

        return exporter.response(filename=self.get_export_filename(export_format))


class OhioGasDetailView(LoginRequiredMixin, DetailView):
    model = PAData
    template_name = "app/ohio_gas_detail.html"


class P2ChooseListView(LoginRequiredMixin, ExportMixin, tables.SingleTableView):
    model = PAData
    
    table_class = P2ChooseTable
    context_object_name = 'data_table'
    template_name = "app/p2choose_list.html"
    my_export_data = None
    export_name='PowerToChoose_' + time.strftime('%Y%m%d_%H_%M_%S')
    

    def get_context_data(self, **kwargs):
        list = PAData.objects.filter(created_by='p2choose_spd')
        filter = P2ChooseFilter(self.request.GET, queryset=list)
        data_table = P2ChooseTable(filter.qs)
        
        RequestConfig(self.request).configure(data_table)
        per_page = self.request.GET.get('per_page', 100)
        data_table.paginate(page=self.request.GET.get('page', 1), per_page=per_page)
        self.my_export_data = data_table
        context = super(P2ChooseListView, self).get_context_data(**kwargs)
        context['data_table'] = data_table
        context['filter'] = filter
        
        return context
    
    def create_export(self, export_format):
        
        exporter = self.export_class(
            export_format=export_format,
            table=self.my_export_data,
            # exclude_columns=self.exclude_columns,
            # dataset_kwargs=self.get_dataset_kwargs(),
        )

        return exporter.response(filename=self.get_export_filename(export_format))


class P2ChooseDetailView(LoginRequiredMixin, DetailView):
    model = PAData
    template_name = "app/p2choose_detail.html"