# Generated by Django 3.2 on 2021-05-02 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0036_auto_20210217_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='is_resigned',
            field=models.BooleanField(default=False, verbose_name='Démission'),
        ),
    ]
