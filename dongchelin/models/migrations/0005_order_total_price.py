# Generated by Django 2.2.1 on 2019-05-21 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0004_order_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(default=0),
        ),
    ]
