# Generated by Django 4.1 on 2022-08-30 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0025_alter_bakeries_image_alter_bakeries_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bakeries',
            name='sku',
            field=models.IntegerField(default=668),
        ),
    ]