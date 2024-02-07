from django.contrib import admin
from .models import product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','price','stok','category','modifield_date','is_available')
    prepopulated_fields = {'slug':('product_name',)}
    
    
admin.site.register(product,ProductAdmin)    
    
