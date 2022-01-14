# Generated by Django 4.0.1 on 2022-01-13 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_user', '0007_alter_customuser_is_technician_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_Technician',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_customer',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phoneNumber',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]