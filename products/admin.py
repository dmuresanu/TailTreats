from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin) : 
    list_display = (
        'image',
        'sku',
        'name', 
        'category',
        'rating', 
        'price',
    )
    
    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin) :
    list_display = (
        'friendly_name',
        'name',
    )
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)