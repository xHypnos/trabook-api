# Generated by Django 4.2.7 on 2023-11-13 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0003_city_created_at_city_updated_at_country_created_at_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='country',
            table='countries',
        ),
    ]