# Generated by Django 4.0.6 on 2022-09-02 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0032_alter_bakeries_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bakeries',
            name='sku',
            field=models.IntegerField(default=1703),
        ),
    ]
