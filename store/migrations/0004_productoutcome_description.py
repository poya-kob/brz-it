# Generated by Django 4.2.3 on 2023-08-11 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_products_unit_productinventory_unit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productoutcome',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
