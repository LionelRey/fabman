# Generated by Django 3.1.5 on 2021-01-12 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing', '0018_resource_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usage',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date used'),
        ),
    ]
