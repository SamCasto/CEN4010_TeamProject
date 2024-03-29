# Generated by Django 4.2.3 on 2023-07-15 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_app', '0004_remove_book_ratings_book_ratings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='ratings',
        ),
        migrations.AlterField(
            model_name='rating',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='bookstore_app.book'),
        ),
    ]
