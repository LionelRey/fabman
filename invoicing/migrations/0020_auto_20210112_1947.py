# Generated by Django 3.1.5 on 2021-01-12 18:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing', '0019_auto_20210112_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usage',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date used'),
        ),
    ]
