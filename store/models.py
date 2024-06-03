from django.db import models
from django.contrib.auth.models import User
# import datetime


#categories
class Category(models.Model):
    category_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    def __str__(self):
        return f'{self.category_name}'

#SubCategories
class SubCategory(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    sub_category = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return f'{self.sub_category}'

# Product
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    # slug = models.SlugField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    sub_category= models.ForeignKey(SubCategory,on_delete=models.CASCADE,default=1)
    price = models.DecimalField(default=0,decimal_places=0,max_digits=8)
    desc = models.CharField(max_length=250,default='',blank=True,null=True)
    image = models.ImageField(upload_to='uploads/products/')
    on_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0,decimal_places=0,max_digits=8)

    def __str__(self):
        return f'{self.product_name}'

class Product_Detail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='details')
    model_no = models.CharField(max_length=50, blank=True, null=True)
    fabric = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.product.product_name} - {self.model_no}"

class Product_Image(models.Model):
    product_detail = models.ForeignKey(Product_Detail, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='uploads/products/details/', blank=True, null=True)

    def __str__(self):
        return f'{self.product_detail.product.product_name}'



class BasePoster(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/base')
    def __str__(self):
        return f'{self.name}'

class Customer(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.TextField()
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}'

    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.DecimalField(default=0,decimal_places=0,max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(default=0,decimal_places=0,max_digits=10)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Order {self.order}"

class Shipping(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    address = models.TextField()
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2)
    shipped_at = models.DateTimeField(blank=True, null=True)
    delivered_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Shipping for Order {self.order}"

class WishlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.product.product_name}'
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)  # Assuming product ID 1 is valid
    size = models.CharField(max_length=10, default='M')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.user.username} - {self.product.product_name} - {self.size}'


