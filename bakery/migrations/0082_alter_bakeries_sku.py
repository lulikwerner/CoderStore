# Generated by Django 4.0.6 on 2022-09-03 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0081_alter_bakeries_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bakeries',
            name='sku',
            field=models.IntegerField(default=1488),
        ),
    ]
