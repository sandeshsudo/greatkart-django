import imp
from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'created_date')
    prepopulated_fields = {'slug': ('product_name',)} 

# Register your models here.
admin.site.register(Product, ProductAdmin)