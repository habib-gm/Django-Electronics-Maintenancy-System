# Generated by Django 4.0.1 on 2022-01-13 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_user', '0006_rename_devicename_device_devicename_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_Technician',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_customer',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phoneNumber',
            field=models.IntegerField(null=True),
        ),
    ]
