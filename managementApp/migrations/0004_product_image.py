# Generated by Django 5.2.3 on 2025-07-05 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("managementApp", "0003_product_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="product_images/"),
        ),
    ]
