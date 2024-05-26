# from django.shortcuts import render
# from .models import Product
# # from .models import Category
# # Create your views here.

# def base(request):
#     return render(request,'base.html')
# def product(request):
#     product_abaya = Product.objects.filter(category_id='1')
#     return render(request,'product.html',{'product_abaya':product_abaya})
# def wishlist(request):
#     return render(request,'wishlist.html')
# def account(request):
#     return render(request,'signup.html')
# def cart(request):
#     return render(request,'cart.html')



import random
from django.shortcuts import render, get_object_or_404
# from django.core import paginator
from django.core.paginator import Paginator
from .models import Product, Category

def base(request):
    return render(request, 'base.html')

def home(request):
    all_products = list(Product.objects.all())
    random.shuffle(all_products)
    
    paginator = Paginator(all_products, 20)  # Show 12 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'product.html', {'page_obj': page_obj})

def products_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = list(Product.objects.filter(category=category))
    random.shuffle(products)
    
    paginator = Paginator(products, 20)  # Show 12 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    return render(request, 'product.html', {'page_obj': page_obj, 'category': category})

def wishlist(request):
    return render(request, 'wishlist.html')

def account(request):
    return render(request, 'login.html')

def cart(request):
    return render(request, 'cart.html')
