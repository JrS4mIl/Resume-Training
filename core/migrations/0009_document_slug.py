# Generated by Django 4.2.6 on 2023-10-12 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='slug',
            field=models.SlugField(default='', max_length=200, verbose_name='Slug'),
        ),
    ]
