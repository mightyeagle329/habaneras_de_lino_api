# Generated by Django 3.2.8 on 2021-12-05 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0011_productvariation_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='code',
            field=models.CharField(default='', max_length=256),
        ),
    ]