# Generated by Django 4.2.6 on 2024-01-25 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_remove_products_unic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products_image'),
        ),
    ]
