# Generated by Django 4.0.6 on 2022-09-02 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drink', '0036_alter_drinks_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drinks',
            name='sku',
            field=models.IntegerField(default=1092),
        ),
    ]
