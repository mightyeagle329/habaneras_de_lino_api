# Generated by Django 3.2.8 on 2021-10-30 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0004_cart_productvariation'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariation',
            name='clothing_s',
            field=models.CharField(default='S', max_length=256),
        ),
    ]
