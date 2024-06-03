import random
from django.shortcuts import render, get_object_or_404,redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Case, When, Value, DecimalField, F
import json
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from decimal import Decimal
from .models import Product, Category,BasePoster,WishlistItem, Product_Detail, Product_Image,Cart,Customer,Order,OrderItem,Payment,Shipping

def base(request):
    posters = list(BasePoster.objects.all())

    return render(request, 'base.html',{'posters':posters})

def home(request):
    search_query = request.GET.get('search', '')
    sort_option = request.GET.get('sort', '')

    products = Product.objects.all()

    if search_query:
        products = products.filter(product_name__icontains=search_query)

    if sort_option:
        if sort_option == 'price_asc':
            products = products.annotate(
                effective_price=Case(
                    When(on_sale=True, then='sale_price'),
                    default='price',
                    output_field=DecimalField()
                )
            ).order_by('effective_price')
        elif sort_option == 'price_desc':
            products = products.annotate(
                effective_price=Case(
                    When(on_sale=True, then='sale_price'),
                    default='price',
                    output_field=DecimalField()
                )
            ).order_by('-effective_price')
        elif sort_option == 'name_asc':
            products = products.order_by('product_name')
        elif sort_option == 'name_desc':
            products = products.order_by('-product_name')
    else:
        products = list(products)  # Convert to list for shuffling
        random.shuffle(products)

    paginator = Paginator(products, 20)  # Show 20 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'sort_option': sort_option,
    }

    return render(request, 'product.html', context)

def products_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    
    search_query = request.GET.get('search', '')
    sort_option = request.GET.get('sort', '')

    if search_query:
        products = products.filter(product_name__icontains=search_query)
        
    if sort_option:
        if sort_option == 'price_asc':
            products = products.annotate(
                effective_price=Case(
                    When(on_sale=True, then='sale_price'),
                    default='price',
                    output_field=DecimalField()
                )
            ).order_by('effective_price')
        elif sort_option == 'price_desc':
            products = products.annotate(
                effective_price=Case(
                    When(on_sale=True, then='sale_price'),
                    default='price',
                    output_field=DecimalField()
                )
            ).order_by('-effective_price')
        elif sort_option == 'name_asc':
            products = products.order_by('product_name')
        elif sort_option == 'name_desc':
            products = products.order_by('-product_name')
    else:
        products = list(products)  # Convert to list for shuffling
        random.shuffle(products)

    paginator = Paginator(products, 20)  # Show 20 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'sort_option': sort_option,
        'category': category
    }

    return render(request, 'product.html', context)

def product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product_details = Product_Detail.objects.filter(product=product).prefetch_related('images')
    show_size_option = product.category.id in [1, 2]
    return render(request, 'single-product.html', {
        'product': product,
        'product_details': product_details,
        'show_size_option': show_size_option
    })

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    WishlistItem.objects.get_or_create(user=request.user, product=product)
    return redirect('wishlist')

@login_required
def wishlist(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})

@login_required
def delete_from_wishlist(request, item_id):
    item = get_object_or_404(WishlistItem, id=item_id, user=request.user)
    item.delete()
    return redirect('wishlist')

def account(request):
    return render(request, 'login.html')

@login_required
@csrf_exempt
def add_to_cart(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            product_id = data.get('product_id')
            size = data.get('size')  # size might be None
            quantity = data.get('quantity')

            product = get_object_or_404(Product, id=product_id)

            # Adjust logic to handle cases where size is not required
            if size:
                cart_item, created = Cart.objects.get_or_create(
                    user=request.user,
                    product=product,
                    size=size,
                    defaults={'quantity': quantity}
                )
            else:
                cart_item, created = Cart.objects.get_or_create(
                    user=request.user,
                    product=product,
                    defaults={'quantity': quantity}
                )

            if not created:
                cart_item.quantity += int(quantity)
                cart_item.save()

            return JsonResponse({'success': True})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
    else:
        return JsonResponse({'success': False, 'error': 'Only POST method is accepted'}, status=405)


def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    cart_subtotal = sum(
        (item.product.sale_price if item.product.on_sale else item.product.price) * item.quantity
        for item in cart_items
    )
    cart_tax = cart_subtotal * Decimal('0.05')  # Example tax rate
    cart_shipping = Decimal('500')  # Example flat rate
    cart_total = cart_subtotal + cart_tax + cart_shipping

    context = {
        'cart_items': cart_items,
        'cart_subtotal': cart_subtotal,
        'cart_tax': cart_tax,
        'cart_shipping': cart_shipping,
        'cart_total': cart_total,
    }
    return render(request, 'cart.html', context)

@csrf_exempt
def remove_from_cart(request):
    if request.method == 'POST':
        try:
            product_id = request.POST.get('product_id')
            size = request.POST.get('size')

            cart_item = Cart.objects.get(user=request.user, product_id=product_id, size=size)
            cart_item.delete()

            cart_items = Cart.objects.filter(user=request.user)
            cart_subtotal = sum(
                (item.product.sale_price if item.product.on_sale else item.product.price) * item.quantity
                for item in cart_items
            )
            cart_tax = cart_subtotal * Decimal('0.05')  # Example tax rate
            cart_shipping = Decimal('50')  # Example flat rate
            cart_total = cart_subtotal + cart_tax + cart_shipping

            return JsonResponse({
                'success': True,
                'cart_subtotal': float(cart_subtotal),
                'cart_tax': float(cart_tax),
                'cart_shipping': float(cart_shipping),
                'cart_total': float(cart_total)
            })
        except Cart.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Item not found in cart'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
    else:
        return JsonResponse({'success': False, 'error': 'Only POST method is accepted'}, status=405)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'single-product.html', {'product': product})

@login_required
def checkout(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        
        # Create or get the customer
        customer, created = Customer.objects.get_or_create(
            username=request.user,
            defaults={'email': email, 'first_name': first_name, 'last_name': last_name, 'address': address, 'phone_number': phone_number}
        )
        
        # Calculate total price
        cart_items = Cart.objects.filter(user=request.user)
        total_price = sum(item.product.price * item.quantity for item in cart_items)
        
        # Create the order
        order = Order.objects.create(customer=customer, total_price=total_price)
        
        # Add order items
        order_items_text = ""
        for cart_item in cart_items:
            order_item = OrderItem.objects.create(order=order, product=cart_item.product, quantity=cart_item.quantity, price=cart_item.product.price)
            order_items_text += f"{cart_item.product.product_name} - Quantity: {cart_item.quantity}, Price: {cart_item.product.price}\n"

        # Send a confirmation email with order details
        email_body = f'Thank you, {first_name}, for placing your order! Your order will be delivered within 5-7 days.\n\n'
        email_body += 'Order Details:\n'
        email_body += order_items_text
        email_body += f'\nTotal Price: {total_price}\n'
        email_body += 'If you have any questions, feel free to contact us.\n Phone no: +92 3256811411\n Email: mrcollections.store.gmail.com\n\nBest regards,\nMR Collections'

        send_mail(
            'Order Confirmation - MR Collections',
            email_body,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        
        # Add order items
        # order_items_text = ""
        # for cart_item in cart_items:
        #     order_item = OrderItem.objects.create(order=order, product=cart_item.product, quantity=cart_item.quantity, price=cart_item.product.price)
        #     order_items_text += f"{cart_item.product.product_name} - Quantity: {cart_item.quantity}, Price: {cart_item.product.price}\n"
        #     order_items_text += f"Image URL: {request.build_absolute_uri(cart_item.product.image.url)}\n"  # Add image URL to the order details

        # # Send a confirmation email with order details and images
        # email_body = f'Thank you, {first_name}, for placing your order! Your order will be delivered within 5-7 days.\n\n'
        # email_body += 'Order Details:\n'
        # email_body += order_items_text
        # email_body += f'\nTotal Price: {total_price}\n'
        # email_body += 'If you have any questions, feel free to contact us.\n\nBest regards,\nMR Collections'

        # send_mail(
        #     'Order Confirmation - MR Collections',
        #     email_body,
        #     settings.EMAIL_HOST_USER,
        #     [email],
        #     fail_silently=False,
        # )


        # Clear the cart
        Cart.objects.filter(user=request.user).delete()
        
        messages.success(request, 'Your order has been placed successfully!')
        return redirect('home')
    
    return render(request, 'checkout.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def shipping(request):
    return render(request, 'shipping.html')

def returns(request):
    return render(request, 'returns.html')