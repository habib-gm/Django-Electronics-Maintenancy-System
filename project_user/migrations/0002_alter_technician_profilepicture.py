# Generated by Django 4.0.1 on 2022-01-12 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technician',
            name='ProfilePicture',
            field=models.ImageField(upload_to='images/'),
        ),
    ]