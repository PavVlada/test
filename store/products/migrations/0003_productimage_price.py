# Generated by Django 2.2 on 2021-11-07 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20211107_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
