# Generated by Django 4.0.6 on 2022-08-19 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meat', '0002_alter_products_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='sku',
            field=models.IntegerField(default=330),
        ),
    ]