import csv
from io import BytesIO
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from PIL import Image as PILImage
import io
from reportlab.lib.units import inch

def export_as_csv_category(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=categories.csv'
    writer = csv.writer(response)
    writer.writerow(['Category Name', 'Slug'])

    for obj in queryset:
        writer.writerow([obj.category_name, obj.slug])

    return response

def export_as_excel_category(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=categories.xlsx'

    data = []
    for obj in queryset:
        data.append([obj.category_name, obj.slug])

    df = pd.DataFrame(data, columns=['Category Name', 'Slug'])
    with BytesIO() as b:
        writer = pd.ExcelWriter(b, engine='openpyxl')
        df.to_excel(writer, index=False)
        writer.save()
        response.write(b.getvalue())

    return response

def export_as_pdf_category(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=categories.pdf'

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    p.drawString(100, 750, "Category Data")
    y = 730
    for obj in queryset:
        p.drawString(100, y, f'{obj.category_name}, {obj.slug}')
        y -= 20

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()

    response.write(pdf)
    return response

def export_as_csv_subcategory(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=subcategories.csv'
    writer = csv.writer(response)
    writer.writerow(['Category', 'Sub Category Name', 'Slug'])

    for obj in queryset:
        writer.writerow([obj.category.category_name, obj.sub_category_name, obj.slug])

    return response

def export_as_excel_subcategory(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=subcategories.xlsx'

    data = []
    for obj in queryset:
        data.append([obj.category.category_name, obj.sub_category_name, obj.slug])

    df = pd.DataFrame(data, columns=['Category', 'Sub Category Name', 'Slug'])
    with BytesIO() as b:
        writer = pd.ExcelWriter(b, engine='openpyxl')
        df.to_excel(writer, index=False)
        writer.save()
        response.write(b.getvalue())

    return response

def export_as_pdf_subcategory(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=subcategories.pdf'

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    p.drawString(100, 750, "Sub Category Data")
    y = 730
    for obj in queryset:
        p.drawString(100, y, f'{obj.category.category_name}, {obj.sub_category_name}, {obj.slug}')
        y -= 20

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()

    response.write(pdf)
    return response

def export_as_csv_product(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=products.csv'
    writer = csv.writer(response)
    writer.writerow(['Product Name', 'Category', 'Sub Category', 'Price', 'Description', 'On Sale', 'Sale Price'])

    for obj in queryset:
        writer.writerow([obj.product_name, obj.category.category_name, obj.sub_category_name.sub_category_name,
                         obj.price, obj.desc, obj.on_sale, obj.sale_price])

    return response

def export_as_excel_product(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=products.xlsx'

    data = []
    for obj in queryset:
        data.append([obj.product_name, obj.category.category_name, obj.sub_category_name.sub_category_name,
                     obj.price, obj.desc, obj.on_sale, obj.sale_price])

    df = pd.DataFrame(data, columns=['Product Name', 'Category', 'Sub Category', 'Price', 'Description', 'On Sale', 'Sale Price'])
    with BytesIO() as b:
        df.to_excel(b, index=False, engine='openpyxl')  # Save DataFrame to Excel
        response.write(b.getvalue())  # Write Excel file content to response

    return response

def generate_pdf(products):
    response = io.BytesIO()
    doc = SimpleDocTemplate(response, pagesize=letter)
    styles = getSampleStyleSheet()

    table_data = []

    # Table Heading
    table_data.append([
        Paragraph("Product Name", styles['Heading2']),
        Paragraph("Category", styles['Heading2']),
        Paragraph("Sub Category", styles['Heading2']),
        Paragraph("Price", styles['Heading2']),
        Paragraph("Description", styles['Heading2']),
        Paragraph("Image", styles['Heading2']),
        Paragraph("On Sale", styles['Heading2']),
        Paragraph("Sale Price", styles['Heading2']),
    ])

    # Populate table rows with product data
    for product in products:
        product_image = Image(product.image.path, width=1*inch, height=1.5*inch) if product.image else ''
                
        table_data.append([
            Paragraph(product.product_name, styles['Normal']),
            Paragraph(product.category.category_name, styles['Normal']),
            Paragraph(product.sub_category.sub_category, styles['Normal']),
            Paragraph(str(product.price), styles['Normal']),
            Paragraph(product.desc or '', styles['Normal']),
            product_image,
            Paragraph(str(product.on_sale), styles['Normal']),
            Paragraph(str(product.sale_price), styles['Normal']),
        ])

    # Create the table
    table = Table(table_data, repeatRows=1)

  # Set column widths
    table._argW[0] = 1*inch  # Product Name
    table._argW[1] = 1.2*inch  # Category
    table._argW[2] = 1.5*inch  # Sub Category
    table._argW[3] = 0.75*inch    # Price
    table._argW[4] = 1.3*inch    # Description
    table._argW[5] = 1*inch  # Image
    table._argW[6] = 0.75*inch  # On Sale
    table._argW[7] = 0.75*inch    # Sale Price

    # Add style to the table
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)]))

    # Build PDF document
    doc.build([table])
    response.seek(0)
    return response
    
def export_as_pdf_product(modeladmin, request, queryset):
    products = queryset
    
    # Call the new generate_pdf function
    pdf_response = generate_pdf(products)
    
    # Set HTTP headers for the response
    response = HttpResponse(pdf_response, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="products.pdf"'
    
    return response


# Repeat similar functions for other models, adjusting the fields accordingly

def export_as_csv_customer(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=customers.csv'
    writer = csv.writer(response)
    writer.writerow(['Username', 'Email', 'First Name', 'Last Name', 'Address', 'City', 'Postal Code', 'Country', 'Phone Number', 'Date Joined'])

    for obj in queryset:
        writer.writerow([obj.username, obj.email, obj.first_name, obj.last_name, obj.address, obj.city, obj.postal_code, obj.country, obj.phone_number, obj.date_joined])

    return response

def export_as_excel_customer(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=customers.xlsx'

    data = []
    for obj in queryset:
        data.append([obj.username, obj.email, obj.first_name, obj.last_name, obj.address, obj.city, obj.postal_code, obj.country, obj.phone_number, obj.date_joined])

    df = pd.DataFrame(data, columns=['Username', 'Email', 'First Name', 'Last Name', 'Address', 'City', 'Postal Code', 'Country', 'Phone Number', 'Date Joined'])
    with BytesIO() as b:
        writer = pd.ExcelWriter(b, engine='openpyxl')
        df.to_excel(writer, index=False)
        writer.save()
        response.write(b.getvalue())

    return response

def export_as_pdf_customer(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=customers.pdf'

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    p.drawString(100, 750, "Customer Data")
    y = 730
    for obj in queryset:
        p.drawString(100, y, f'{obj.username}, {obj.email}, {obj.first_name}, {obj.last_name}, {obj.address}, {obj.city}, {obj.postal_code}, {obj.country}, {obj.phone_number}, {obj.date_joined}')
        y -= 20

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()

    response.write(pdf)
    return response
# Order export functions
def export_as_csv_order(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=orders.csv'
    writer = csv.writer(response)
    writer.writerow(['Customer', 'Total Price', 'Created At', 'Updated At'])

    for obj in queryset:
        writer.writerow([obj.customer.username, obj.total_price, obj.created_at, obj.updated_at])

    return response

def export_as_excel_order(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=orders.xlsx'

    data = []
    for obj in queryset:
        data.append([obj.customer.username, obj.total_price, obj.created_at, obj.updated_at])

    df = pd.DataFrame(data, columns=['Customer', 'Total Price', 'Created At', 'Updated At'])
    with BytesIO() as b:
        writer = pd.ExcelWriter(b, engine='openpyxl')
        df.to_excel(writer, index=False)
        writer.save()
        response.write(b.getvalue())

    return response

def export_as_pdf_order(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=orders.pdf'

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    p.drawString(100, 750, "Order Data")
    y = 730
    for obj in queryset:
        p.drawString(100, y, f'{obj.customer.username}, {obj.total_price}, {obj.created_at}, {obj.updated_at}')
        y -= 20

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()

    response.write(pdf)
    return response
# OrderItem export functions
def export_as_csv_orderitem(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=order_items.csv'
    writer = csv.writer(response)
    writer.writerow(['Order', 'Product', 'Quantity', 'Price'])

    for obj in queryset:
        writer.writerow([obj.order.customer.username, obj.product.product_name, obj.quantity, obj.price])

    return response

def export_as_excel_orderitem(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=order_items.xlsx'

    data = []
    for obj in queryset:
        data.append([obj.order.customer.username, obj.product.product_name, obj.quantity, obj.price])

    df = pd.DataFrame(data, columns=['Order', 'Product', 'Quantity', 'Price'])
    with BytesIO() as b:
        writer = pd.ExcelWriter(b, engine='openpyxl')
        df.to_excel(writer, index=False)
        writer.save()
        response.write(b.getvalue())

    return response

def export_as_pdf_orderitem(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=order_items.pdf'

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    p.drawString(100, 750, "Order Item Data")
    y = 730
    for obj in queryset:
        p.drawString(100, y, f'{obj.order.customer.username}, {obj.product.product_name}, {obj.quantity}, {obj.price}')
        y -= 20

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()

    response.write(pdf)
    return response
# Payment export functions
def export_as_csv_payment(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=payments.csv'
    writer = csv.writer(response)
    writer.writerow(['Order', 'Payment Method', 'Payment Status', 'Created At'])

    for obj in queryset:
        writer.writerow([obj.order.customer.username, obj.payment_method, obj.payment_status, obj.created_at])

    return response

def export_as_excel_payment(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=payments.xlsx'

    data = []
    for obj in queryset:
        data.append([obj.order.customer.username, obj.payment_method, obj.payment_status, obj.created_at])

    df = pd.DataFrame(data, columns=['Order', 'Payment Method', 'Payment Status', 'Created At'])
    with BytesIO() as b:
        writer = pd.ExcelWriter(b, engine='openpyxl')
        df.to_excel(writer, index=False)
        writer.save()
        response.write(b.getvalue())

    return response

def export_as_pdf_payment(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=payments.pdf'

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    p.drawString(100, 750, "Payment Data")
    y = 730
    for obj in queryset:
        p.drawString(100, y, f'{obj.order.customer.username}, {obj.payment_method}, {obj.payment_status}, {obj.created_at}')
        y -= 20

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()

    response.write(pdf)
    return response

# Shipping export functions
def export_as_csv_shipping(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=shippings.csv'
    writer = csv.writer(response)
    writer.writerow(['Order', 'Address', 'City', 'State', 'Postal Code', 'Country', 'Shipping Cost', 'Shipped At', 'Delivered At'])

    for obj in queryset:
        writer.writerow([obj.order.customer.username, obj.address, obj.city, obj.state, obj.postal_code, obj.country, obj.shipping_cost, obj.shipped_at, obj.delivered_at])

    return response

def export_as_excel_shipping(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=shippings.xlsx'

    data = []
    for obj in queryset:
        data.append([obj.order.customer.username, obj.address, obj.city, obj.state, obj.postal_code, obj.country, obj.shipping_cost, obj.shipped_at, obj.delivered_at])

    df = pd.DataFrame(data, columns=['Order', 'Address', 'City', 'State', 'Postal Code', 'Country', 'Shipping Cost', 'Shipped At', 'Delivered At'])
    with BytesIO() as b:
        writer = pd.ExcelWriter(b, engine='openpyxl')
        df.to_excel(writer, index=False)
        writer.save()
        response.write(b.getvalue())

    return response

def export_as_pdf_shipping(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=shippings.pdf'

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    p.drawString(100, 750, "Shipping Data")
    y = 730
    for obj in queryset:
        p.drawString(100, y, f'{obj.order.customer.username}, {obj.address}, {obj.city}, {obj.state}, {obj.postal_code}, {obj.country}, {obj.shipping_cost}, {obj.shipped_at}, {obj.delivered_at}')
        y -= 20

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()

    response.write(pdf)
    return response

# WishlistItem export functions
def export_as_csv_wishlistitem(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=wishlist_items.csv'
    writer = csv.writer(response)
    writer.writerow(['User', 'Product'])

    for obj in queryset:
        writer.writerow([obj.user.username, obj.product.product_name])

    return response

def export_as_excel_wishlistitem(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=wishlist_items.xlsx'

    data = []
    for obj in queryset:
        data.append([obj.user.username, obj.product.product_name])

    df = pd.DataFrame(data, columns=['User', 'Product'])
    with BytesIO() as b:
        writer = pd.ExcelWriter(b, engine='openpyxl')
        df.to_excel(writer, index=False)
        writer.save()
        response.write(b.getvalue())

    return response

def export_as_pdf_wishlistitem(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=wishlist_items.pdf'

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    p.drawString(100, 750, "Wishlist Item Data")
    y = 730
    for obj in queryset:
        p.drawString(100, y, f'{obj.user.username}, {obj.product.product_name}')
        y -= 20

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()

    response.write(pdf)
    return response

# Cart export functions
def export_as_csv_cart(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=carts.csv'
    writer = csv.writer(response)
    writer.writerow(['User', 'Product', 'Quantity'])

    for obj in queryset:
        writer.writerow([obj.user.username, obj.product.product_name, obj.quantity])

    return response

def export_as_excel_cart(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=carts.xlsx'

    data = []
    for obj in queryset:
        data.append([obj.user.username, obj.product.product_name, obj.quantity])

    df = pd.DataFrame(data, columns=['User', 'Product', 'Quantity'])
    with BytesIO() as b:
        writer = pd.ExcelWriter(b, engine='openpyxl')
        df.to_excel(writer, index=False)
        writer.save()
        response.write(b.getvalue())

    return response

def export_as_pdf_cart(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=carts.pdf'

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    p.drawString(100, 750, "Cart Data")
    y = 730
    for obj in queryset:
        p.drawString(100, y, f'{obj.user.username}, {obj.product.product_name}, {obj.quantity}')
        y -= 20

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()

    response.write(pdf)
    return response

# Product_Detail export functions
def export_as_csv_product_detail(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=product_details.csv'
    writer = csv.writer(response)
    writer.writerow(['Product', 'Model No', 'Fabric', 'Color'])

    for obj in queryset:
        writer.writerow([obj.product.product_name, obj.model_no, obj.fabric, obj.color])

    return response

def export_as_excel_product_detail(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=product_details.xlsx'

    data = []
    for obj in queryset:
        data.append([obj.product.product_name, obj.model_no, obj.fabric, obj.color])

    df = pd.DataFrame(data, columns=['Product', 'Model No', 'Fabric', 'Color'])
    with BytesIO() as b:
        writer = pd.ExcelWriter(b, engine='openpyxl')
        df.to_excel(writer, index=False)
        writer.save()
        response.write(b.getvalue())

    return response

def export_as_pdf_product_detail(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=product_details.pdf'

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    p.drawString(100, 750, "Product Detail Data")
    y = 730
    for obj in queryset:
        p.drawString(100, y, f'{obj.product.product_name}, {obj.model_no}, {obj.fabric}, {obj.color}')
        y -= 20

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()

    response.write(pdf)
    return response

# Product_Image export functions
def export_as_csv_product_image(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=product_images.csv'
    writer = csv.writer(response)
    writer.writerow(['Product', 'Image'])

    for obj in queryset:
        writer.writerow([obj.product_detail.product.product_name, obj.image.url])

    return response

def export_as_excel_product_image(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=product_images.xlsx'

    data = []
    for obj in queryset:
        data.append([obj.product_detail.product.product_name, obj.image.url])

    df = pd.DataFrame(data, columns=['Product', 'Image'])
    with BytesIO() as b:
        writer = pd.ExcelWriter(b, engine='openpyxl')
        df.to_excel(writer, index=False)
        writer.save()
        response.write(b.getvalue())

    return response

def export_as_pdf_product_image(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=product_images.pdf'

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    p.drawString(100, 750, "Product Image Data")
    y = 730
    for obj in queryset:
        p.drawString(100, y, f'{obj.product_detail.product.product_name}, {obj.image.url}')
        y -= 20

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()

    response.write(pdf)
    return response

# BasePoster export functions
def export_as_csv_baseposter(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=baseposters.csv'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Image'])

    for obj in queryset:
        writer.writerow([obj.name, obj.image.url])

    return response

def export_as_excel_baseposter(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=baseposters.xlsx'

    data = []
    for obj in queryset:
        data.append([obj.name, obj.image.url])

    df = pd.DataFrame(data, columns=['Name', 'Image'])
    with BytesIO() as b:
        writer = pd.ExcelWriter(b, engine='openpyxl')
        df.to_excel(writer, index=False)
        writer.save()
        response.write(b.getvalue())

    return response

def export_as_pdf_baseposter(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=baseposters.pdf'

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    p.drawString(100, 750, "Base Poster Data")
    y = 730
    for obj in queryset:
        p.drawString(100, y, f'{obj.name}, {obj.image.url}')
        y -= 20

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()

    response.write(pdf)
    return response


# Continue this pattern for  , Cart, Product_Detail, Product_Image, BasePoster
