# Generated by Django 5.0.6 on 2024-05-14 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0005_product_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="on_sale",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="product",
            name="sale_price",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
