# Generated by Django 2.2.1 on 2019-05-27 10:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('models', '0008_restaurant_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='likes',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='favo',
            field=models.ManyToManyField(related_name='favo', to=settings.AUTH_USER_MODEL),
        ),
    ]