# Generated by Django 5.0 on 2023-12-31 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0007_alter_country_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='published_countries',
            field=models.ManyToManyField(to='book_outlet.country'),
        ),
    ]
