from django.db import models
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
    sub_category_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return f'{self.sub_category_name}'

# Product
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    # slug = models.SlugField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    sub_category_name = models.ForeignKey(SubCategory,on_delete=models.CASCADE,default=1)
    price = models.DecimalField(default=0,decimal_places=2,max_digits=8)
    desc = models.CharField(max_length=250,default='',blank=True,null=True)
    image = models.ImageField(upload_to='uploads/products/')
    on_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0,decimal_places=2,max_digits=8)

    def __str__(self):
        return f'{self.product_name}'

# ProductDetail Model
class ProductDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='details')
    size = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    # image = models.ImageField(upload_to='uploads/products/details/', blank=True, null=True)

    def __str__(self):
        return f"{self.product.name} - {self.size or 'No Size'} - {self.color or 'No Color'}"

class Customer(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.TextField()
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.username}'

    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

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
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2)
    shipped_at = models.DateTimeField(blank=True, null=True)
    delivered_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Shipping for Order {self.order}"

class Wishlist(models.Model):
    wishlist_product = models.ForeignKey(Product,on_delete=models.CASCADE,default=0)
    # slug = models.SlugField(max_length=255)

    def __str__(self):
        return f'{self.wishlist_product}'

class Cart(models.Model):
    product_name = models.ForeignKey(Product,on_delete=models.CASCADE,default=0)
    # slug = models.SlugField(max_length=255)

    def __str__(self):
        return f'{self.product_name}'

