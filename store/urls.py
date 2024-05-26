# from django.urls import path,include
# from store import views

# urlpatterns = [
#     path('', views.base, name='base'),
#     path('product/', views.product, name='product'),
#     path('wishlist/', views.wishlist, name='wishlist'),
#     path('', include('accounts.urls')),
#     # path('account/', views.account, name='account'),
#     path('cart/', views.cart, name='cart'),
# ]
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('category/<slug:slug>/', views.products_by_category, name='products_by_category'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('', include('accounts.urls')),
    path('account/', views.account, name='account'),
    path('cart/', views.cart, name='cart'),
]
