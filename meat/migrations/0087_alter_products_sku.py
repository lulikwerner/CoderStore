# Generated by Django 4.1 on 2022-09-03 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meat', '0086_remove_products_unic_alter_products_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='sku',
            field=models.IntegerField(default=857),
        ),
    ]
