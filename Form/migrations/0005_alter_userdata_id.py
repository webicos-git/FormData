# Generated by Django 3.2.7 on 2022-05-30 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0004_alter_userdata_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
