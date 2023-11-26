# Generated by Django 4.2.6 on 2023-10-31 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('salary', models.PositiveSmallIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]