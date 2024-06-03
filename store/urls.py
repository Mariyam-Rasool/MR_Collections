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
# from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('category/<slug:slug>/', views.products_by_category, name='products_by_category'),
    path('', include('accounts.urls')),
    path('account/', views.account, name='account'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add_to_wishlist/<int:product_id>/',views.add_to_wishlist, name='add_to_wishlist'),
    path('delete_from_wishlist/<int:item_id>/', views.delete_from_wishlist, name='delete_from_wishlist'),
    # path('cart_view/', views.cart_view, name='cart_view'),
    # path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('remove-from-cart/', views.remove_from_cart, name='remove_from_cart'),  # Add this line
    path('product/<int:product_id>/', views.product_detail_view, name='product_detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('shipping/', views.shipping, name='shipping'),
    path('returns/', views.returns, name='returns'),
]
