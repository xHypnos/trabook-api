# Generated by Django 4.2.7 on 2023-11-13 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0004_alter_country_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='city',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='country',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='country',
            name='updated_at',
        ),
    ]
