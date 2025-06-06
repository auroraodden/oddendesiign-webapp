# Generated by Django 5.2.1 on 2025-05-20 23:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_teaserproduct_remove_order_uploaded_files_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="is_outlet",
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name="OutletOrder",
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
                ("full_name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=20)),
                ("address", models.TextField()),
                ("postal_code", models.CharField(max_length=10)),
                ("city", models.CharField(max_length=100)),
                ("birth_date", models.DateField()),
                ("agree_to_terms", models.BooleanField(default=False)),
                (
                    "total_price",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core.product",
                    ),
                ),
            ],
        ),
    ]
