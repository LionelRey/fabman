# Generated by Django 3.1.5 on 2021-01-12 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing', '0023_auto_20210112_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usage',
            name='qty',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
