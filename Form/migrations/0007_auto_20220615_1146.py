# Generated by Django 3.2.7 on 2022-06-15 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0006_auto_20220615_1133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='asiaProfit',
            new_name='profit',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='interProfit',
        ),
    ]