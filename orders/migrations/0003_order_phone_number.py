# Generated by Django 4.1.3 on 2023-01-03 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.CharField(max_length=20, null=True),
        ),
    ]