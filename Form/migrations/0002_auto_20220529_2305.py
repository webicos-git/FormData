# Generated by Django 3.2.7 on 2022-05-29 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='profit',
        ),
        migrations.AddField(
            model_name='userdata',
            name='buyAmount',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='userdata',
            name='sellAmount',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='userdata',
            name='transaction',
            field=models.CharField(default='', max_length=100),
        ),
    ]
