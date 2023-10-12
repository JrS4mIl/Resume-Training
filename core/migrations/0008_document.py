# Generated by Django 4.2.6 on 2023-10-12 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_sosyalmedia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('order', models.IntegerField(default='0', verbose_name='Order')),
                ('file', models.FileField(default='', upload_to='documents/', verbose_name='Document Name')),
                ('button_text', models.CharField(blank=True, default='', max_length=120, verbose_name='Butoon Text')),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
                'ordering': ('order',),
            },
        ),
    ]