# Generated by Django 4.2.7 on 2023-11-13 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0007_remove_card_country_alter_card_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
