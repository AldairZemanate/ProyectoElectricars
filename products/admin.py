from django.contrib import admin
from .models import Product
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('prod_name','prod_count','prod_is_active','prod_discount')
    list_filter=('prod_is_active','prod_warranty',)