# Generated by Django 4.2.6 on 2024-01-25 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meat', '0087_alter_products_sku'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Products',
        ),
    ]