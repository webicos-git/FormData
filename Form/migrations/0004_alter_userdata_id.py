# Generated by Django 3.2.7 on 2022-05-30 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0003_userdata_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='id',
            field=models.AutoField(default='', primary_key=True, serialize=False),
        ),
    ]
