# Generated by Django 3.2.7 on 2022-06-15 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0005_alter_userdata_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='asiaProfit',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userdata',
            name='interProfit',
            field=models.IntegerField(default=0),
        ),
    ]
