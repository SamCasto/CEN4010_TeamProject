# Generated by Django 4.2.2 on 2023-06-27 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_app', '0002_remove_websiteuser_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='websiteuser',
            name='address',
            field=models.CharField(blank=True, max_length=255, verbose_name='Home Address'),
        ),
    ]
