# Generated by Django 5.2.3 on 2025-06-28 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("managementApp", "0002_rename_products_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
