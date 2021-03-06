# Generated by Django 4.0.1 on 2022-01-12 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_user', '0002_alter_technician_profilepicture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='technician',
            old_name='User',
            new_name='user',
        ),
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
