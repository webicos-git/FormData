# Generated by Django 3.2.7 on 2022-05-29 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0002_auto_20220529_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='phone',
            field=models.CharField(default='', max_length=100),
        ),
    ]