from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from django.db import models
from .models import Order,OrderProduct
# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=('id','ord_date','ord_state','ord_total')
    list_filter=('ord_state',)

@admin.register(OrderProduct)
class OrderProduct(admin.ModelAdmin):
    list_display=('id','order','product','quantity',)