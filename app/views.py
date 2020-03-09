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
        
        context['total_records'] = PAData.objects.all().count()
        context['company_no'] = PAData.objects.exclude(company_name__isnull=True).values('company_name').order_by('company_name').distinct().count()
        context['state_no'] = PAData.objects.exclude(state__isnull=True).values('state').order_by('state').distinct().count()
        latest_item = PAData.objects.latest('created_at')
        context['last_scraped'] = latest_item.created_at.replace(tzinfo=timezone('Europe/Vienna'))

        return context

class PADataListView(LoginRequiredMixin, ExportMixin, tables.SingleTableView):
    model = PAData
    
    table_class = PADataTable
    context_object_name = 'data_table'
    ordering = ['company_name']
    
    template_name = "app/padata_list.html"

    

    def get_context_data(self, **kwargs):
        list = PAData.objects.all()
        filter = PADataFilter(self.request.GET, queryset=list)
        data_table = PADataTable(filter.qs)
        RequestConfig(self.request).configure(data_table)
        per_page = self.request.GET.get('per_page', 10)
        data_table.paginate(page=self.request.GET.get('page', 1), per_page=per_page)

        self.dataset_kwargs = data_table
        context = super(PADataListView, self).get_context_data(**kwargs)
        context['data_table'] = data_table
        context['filter'] = filter
        # import pdb; pdb.set_trace()
        
        return context

class PADataDetailView(LoginRequiredMixin, DetailView):
    model = PAData
    template_name = "app/padata_detail.html"