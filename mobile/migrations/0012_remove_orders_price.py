# Generated by Django 3.1.7 on 2021-04-13 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0011_orders_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='price',
        ),
    ]
