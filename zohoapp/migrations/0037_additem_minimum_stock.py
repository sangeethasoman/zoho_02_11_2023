# Generated by Django 3.2.20 on 2023-10-20 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0036_auto_20231018_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='additem',
            name='minimum_stock',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
