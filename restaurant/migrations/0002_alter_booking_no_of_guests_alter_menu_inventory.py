# Generated by Django 5.0.3 on 2024-03-31 12:02

import restaurant.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='no_of_guests',
            field=restaurant.fields.IntegerRangeField(),
        ),
        migrations.AlterField(
            model_name='menu',
            name='inventory',
            field=restaurant.fields.IntegerRangeField(),
        ),
    ]
