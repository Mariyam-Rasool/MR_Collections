from django.contrib import admin
from .models import Category,SubCategory,Product,Order,Customer,Wishlist,Cart,OrderItem,ProductDetail,Payment,Shipping,BasePoster
# Register your models here.

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(ProductDetail)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(Shipping)
admin.site.register(BasePoster)
