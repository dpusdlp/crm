# Generated by Django 4.2.6 on 2023-11-09 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_employee_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='image',
            new_name='profile_pic',
        ),
    ]
