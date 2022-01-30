from unicodedata import name
from django.contrib import admin
from .models import Product, Contact

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'mehsulun_kodu', 'available', 'product_of_month')
    search_fields = ('name', 'mehsulun_kodu')

admin.site.register(Contact)