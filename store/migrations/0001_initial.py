# Generated by Django 5.0.6 on 2024-05-12 09:12

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("slug", models.SlugField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Customers",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=55)),
                ("last_name", models.CharField(max_length=55)),
                ("phone", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=55)),
                ("password", models.CharField(max_length=100)),
                ("address", models.CharField(default="", max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("slug", models.SlugField(max_length=255)),
                (
                    "price",
                    models.DecimalField(decimal_places=2, default=0, max_digits=8),
                ),
                (
                    "desc",
                    models.CharField(blank=True, default="", max_length=250, null=True),
                ),
                ("image", models.ImageField(upload_to="uploads/products/")),
            ],
        ),
        migrations.CreateModel(
            name="Orders",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField(default=1)),
                ("address", models.CharField(max_length=255)),
                ("phone", models.CharField(max_length=255)),
                ("date", models.DateField(default=datetime.date.today)),
                ("status", models.BooleanField(default=False)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="store.customers",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.product"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SubCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("slug", models.SlugField(max_length=255)),
                (
                    "category",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="store.category",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="sub_category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="store.subcategory",
            ),
        ),
    ]
