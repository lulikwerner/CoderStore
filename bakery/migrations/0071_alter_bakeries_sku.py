# Generated by Django 4.0.6 on 2022-09-03 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0070_alter_bakeries_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bakeries',
            name='sku',
            field=models.IntegerField(default=78),
        ),
    ]
