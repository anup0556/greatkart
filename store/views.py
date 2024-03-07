from django.shortcuts import render, get_object_or_404
from .models import product
from category.models import category

def store(request,category_slug=None):
    categorys = None
    products = None
    
    if category_slug != None:
        categorys = get_object_or_404(category,slug=category_slug)
        products = product.objects.filter(category=categorys,is_available=True)
        product_count = products.count()
    else:   
        products = product.objects.all().filter(is_available=True)
        product_count = products.count()
    context = {
        'products': products,
        'product_count ': product_count,
    }
    return render (request, 'store/store.html',context)
