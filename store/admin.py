# from django.contrib import admin
# from .models import Category,SubCategory,Product,Order,Customer
# from .models import WishlistItem,Cart,OrderItem,Product_Detail
# from .models import Payment,Shipping,BasePoster,Product_Image
# from .utils import export_as_csv, export_as_excel, export_as_pdf


# @admin.register(YourModel)
# class YourModelAdmin(admin.ModelAdmin):
#     actions = [export_as_csv, export_as_excel, export_as_pdf]

# class ProductAdmin(admin.ModelAdmin):
#     actions = [export_csv, export_excel, export_pdf]

# class OrderAdmin(admin.ModelAdmin):
#     actions = [export_csv, export_excel, export_pdf]

# # Register your models here.

# admin.site.register(Category)
# admin.site.register(SubCategory)
# admin.site.register(Product)
# admin.site.register(Customer)
# admin.site.register(Order)
# admin.site.register(WishlistItem)
# admin.site.register(Cart)
# admin.site.register(Product_Detail)
# admin.site.register(OrderItem)
# admin.site.register(Payment)
# admin.site.register(Shipping)
# admin.site.register(BasePoster)
# admin.site.register(Product_Image)
from django.contrib import admin
from .models import Category, SubCategory, Product, Order, Customer, WishlistItem, Cart, OrderItem, Product_Detail, Payment, Shipping, BasePoster, Product_Image
from .utils import export_as_csv_category, export_as_excel_category, export_as_pdf_category
from .utils import export_as_csv_subcategory, export_as_excel_subcategory, export_as_pdf_subcategory
from .utils import export_as_csv_product, export_as_excel_product, export_as_pdf_product
from .utils import export_as_csv_customer, export_as_excel_customer, export_as_pdf_customer
from .utils import export_as_csv_order, export_as_excel_order, export_as_pdf_order
from .utils import export_as_csv_wishlistitem, export_as_excel_wishlistitem, export_as_pdf_wishlistitem
from .utils import export_as_csv_cart, export_as_excel_cart, export_as_pdf_cart
from .utils import export_as_csv_product_detail, export_as_excel_product_detail, export_as_pdf_product_detail
from .utils import export_as_csv_orderitem, export_as_excel_orderitem, export_as_pdf_orderitem
from .utils import export_as_csv_payment, export_as_excel_payment, export_as_pdf_payment
from .utils import export_as_csv_shipping, export_as_excel_shipping, export_as_pdf_shipping
from .utils import export_as_csv_baseposter, export_as_excel_baseposter, export_as_pdf_baseposter
from .utils import export_as_csv_product_image, export_as_excel_product_image, export_as_pdf_product_image

class CategoryAdmin(admin.ModelAdmin):
    actions = [export_as_csv_category, export_as_excel_category, export_as_pdf_category]

class SubCategoryAdmin(admin.ModelAdmin):
    actions = [export_as_csv_subcategory, export_as_excel_subcategory, export_as_pdf_subcategory]

class ProductAdmin(admin.ModelAdmin):
    actions = [export_as_csv_product, export_as_excel_product, export_as_pdf_product]

class CustomerAdmin(admin.ModelAdmin):
    actions = [export_as_csv_customer, export_as_excel_customer, export_as_pdf_customer]

class OrderAdmin(admin.ModelAdmin):
    actions = [export_as_csv_order, export_as_excel_order, export_as_pdf_order]

class WishlistItemAdmin(admin.ModelAdmin):
    actions = [export_as_csv_wishlistitem, export_as_excel_wishlistitem, export_as_pdf_wishlistitem]

class CartAdmin(admin.ModelAdmin):
    actions = [export_as_csv_cart, export_as_excel_cart, export_as_pdf_cart]

class ProductDetailAdmin(admin.ModelAdmin):
    actions = [export_as_csv_product_detail, export_as_excel_product_detail, export_as_pdf_product_detail]

class OrderItemAdmin(admin.ModelAdmin):
    actions = [export_as_csv_orderitem, export_as_excel_orderitem, export_as_pdf_orderitem]

class PaymentAdmin(admin.ModelAdmin):
    actions = [export_as_csv_payment, export_as_excel_payment, export_as_pdf_payment]

class ShippingAdmin(admin.ModelAdmin):
    actions = [export_as_csv_shipping, export_as_excel_shipping, export_as_pdf_shipping]

class BasePosterAdmin(admin.ModelAdmin):
    actions = [export_as_csv_baseposter, export_as_excel_baseposter, export_as_pdf_baseposter]

class ProductImageAdmin(admin.ModelAdmin):
    actions = [export_as_csv_product_image, export_as_excel_product_image, export_as_pdf_product_image]

# Register the models with their admin classes
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(WishlistItem, WishlistItemAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Product_Detail, ProductDetailAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Shipping, ShippingAdmin)
admin.site.register(BasePoster, BasePosterAdmin)
admin.site.register(Product_Image, ProductImageAdmin)
