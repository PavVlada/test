# Generated by Django 2.2 on 2021-11-07 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20211107_1246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total_anount',
            new_name='total_price',
        ),
    ]